# Transcription agreement — household

Second transcription of `Household facts for dependents and head of household` by an isolated model (spec 6.5), compared line by line with `forms/2025/household.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5b54d48924e70b6f1778ed0680b2ee4747ee4642cdc0856ae1cbf73c7e3111ef |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | b649d6f44db09182aac7e9408580eb5efbe1d5298fe2483e0c7f58df9f62c353 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | a6e69d16188a6c51f5482550733f0a1b3d89e34205791b5ee6bf8160ff2a6481 |
| printed lines compared | 11 |
| agree / disagree / missing | 4 / 7 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| i1040s8812 | 2025; printed date 2026-01-23 | 2 | pages named by another document's citation | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | 2 | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |

## Lines

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

Second transcription's note: The IRS pages do not define a roster check. Reading chosen: a return has exactly one taxpayer entry, and has a spouse entry only when the filing status is married filing jointly (1040: 'If joint return, spouse's ...'; 1040 instructions: on a separate return you report only your own income).

Ruling: ambiguity; f1040 p. 1: "If joint return, spouse's first name and middle initial" (a spouse entry exactly on a joint return, one entry for you). The candidate's test (taxpayer count not 1, or mfj without exactly one spouse, or not mfj with a spouse entry) is the exact complement of the project's household.roster_ok, so the roster formula is equivalent. Triage executable-triage-v1 (triage/household.json): 1,771 of 1,783 comparisons agree. The 1 project-refuses (audit.household.filer_under16) is the project's under-16 entry check, the owner's choice amb.2025.filer_under_16 (i1040gi p. 66, Self-Select PIN, cited by the register); the 11 project-unknown records (classm.f8889.3, classm.f8889.3.deepseek, stage16.hsa.partial.H01/H02/H05/H06 and others) are fixtures that omit person.under16, which the interview asks of every person because roster_ok reads its refusal on every return. Project stands.

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

Second transcription's note: Read as: both people on the return have a Form 8889 (i8889, Specific Instructions; How To Complete Part I).

Ruling: representation; i8889 p. 4: "If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you." The project tests exactly two people with a Form 8889, the candidate at least two; the roster gate (household.roster_bad) admits at most two person entries, so the two tests cannot differ on an accepted return. Triage executable-triage-v1 (triage/household.json): 1,783 of 1,783 comparisons agree; observed equivalence on that sample. Project stands.

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

Second transcription's note: EIC Step 1, question 2. Refuses when Form 8862 may be required, or during a 2- or 10-year ban (i1040 Form 8862, who must file); this tool does not prepare Form 8862.

Ruling: scope; i1040gi p. 40, EIC Step 1, question 2: "Do you, and your spouse if filing a joint return, have a social security number ... that allows you to work and is valid for EIC purposes". The candidate's count of people with eic_ssn false equal to zero equals the project's count with eic_ssn true equal to the number of people, since the interview answers eic_ssn for every person. The only differences come from the candidate's declared refusal household.credit_disallowed (Form 8862). Triage executable-triage-v1 (triage/household.json): 1,741 of 1,783 agree; 2 candidate-refuses (audit.s8812.credit_disallowed, audit.eic.credit_disallowed), where the project also refuses the return through the same cited gate on eic.credit and s8812.line12 (i1040gi p. 43, Form 8862, who must file; i1040s8812 p. 2); 40 candidate-unknown partial records withhold household.credit_disallowed, which the project reads on those credit lines rather than here. Project stands.

### household.all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **DISAGREE**

Project:

```json
{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}
```

Second:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "ne"}], "test": "all"}}], "test": "eq"}
```

Second transcription's note: Dependents Step 5, question 1 (needed for the credit for other dependents). Refuses when Form 8862 may be required (i1040 line 19; i8812).

Ruling: scope; i1040gi p. 19, Step 5, question 1: "Did you, and your spouse if filing a joint return, have either an SSN or ITIN issued on or before the due date ... (Answer 'Yes' if you are applying for an ITIN ...)". The candidate's count of people with neither tin nor itin_applied equal to zero is the complement of the project's count, so the predicate is equivalent; the only differences come from the candidate's declared refusal household.credit_disallowed. Triage executable-triage-v1 (triage/household.json): 1,741 of 1,783 agree; 2 candidate-refuses (audit.s8812.credit_disallowed, audit.eic.credit_disallowed), which the project refuses through the same cited Form 8862 gate on s8812.line12 and eic.credit; 40 candidate-unknown partial records withhold household.credit_disallowed (bases classm.f2441.1.deepseek, classm.asset.1, classm.carloan.1 and others). Project stands.

### household.ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "any"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "ne"}], "test": "all"}}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "le"}], "test": "all"}
```

Second transcription's note: i1040 line 19 and 'Before you begin'. Open point: whether an ITIN applied for (not yet issued) by the due date counts for the other spouse. Chosen: yes, reusing all_tin, as Step 5 allows for the ODC. Refuses when Form 8862 may be required.

Ruling: model error; i1040gi p. 17, Before you begin: "If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC. The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date of the return". The candidate requires person.tin (or an ITIN merely applied for) of everyone, including a person whose SSN valid for employment already answers the identification requirement, and counts an applied-for ITIN that the text says must have been issued. Triage executable-triage-v1 (triage/household.json): 1,717 of 1,783 agree; 47 candidate-unknown records answer person.work_ssn true and leave person.tin unasked (stage16.cleanup.refuse.rrta_medicare, stage16.cleanup.f5695_no_audit and others), an answer the text does not need; the 17 value differences (classm.otjob.2, classm.sc.3, classm.ssb.2, classm.tcw.8/10/11 recorded) answer work_ssn true with tin false, contradictory answers a truthful interview does not produce (a work-valid SSN is an SSN), project True against candidate False; the 2 candidate-refuses are the Form 8862 gate the project applies on s8812.line12. The applied-for-ITIN reading was not exercised by the sample. Project stands.

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

Second transcription's note: The pages do not say which rule uses the taxpayer's own SSN alone. Read literally as the taxpayer's work-valid SSN.

Ruling: representation; i1040gi p. 18, Step 3, question 4: "Did you, or your spouse if filing a joint return, and this child have SSNs valid for employment". Project (count of taxpayer entries with work_ssn above zero) and candidate (count at least one) are the same test on a count. Triage executable-triage-v1 (triage/household.json): 1,783 of 1,783 agree; observed equivalence on that sample. Project stands.

### household.hoh_fails — Head of household checked without meeting its tests
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12, "type": "Count"}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}], "test": "any"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": true}, {"input": "household.home_cost"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12, "type": "Count"}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12, "type": "Count"}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}], "test": "any"}}, {"const": 1, "type": "Count"}], "test": "lt"}, {"args": [{"const": true}, {"input": "household.home_cost"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12, "type": "Count"}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}], "test": "all"}}, {"const": 1, "type": "Count"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: i1040 Filing Status, Head of Household. Read as: the status claimed is HOH and the unmarried and Test 1 / Test 2 conditions are not met.

Ruling: finding; p501 p. 9, Death or birth: "To qualify you for head of household filing status, the qualifying person ... must be one of the following. • Your qualifying child or qualifying relative who lived with you for more than half the part of the year they were alive. • Your parent for whom you paid, for the entire part of the year your parent was alive, more than half the cost of keeping up the home your parent lived in" (i1040gi p. 15 sends the case there: "If the person is anyone else, see Pub. 501"). The candidate composed the project's own dependent.hoh_test1 and dependent.hoh_test2, so its review never tested them (the BUG-0146 gap); checked here against i1040gi p. 14 Tests 1 and 2 and p501 Table 4, they are right for persons alive all year, but their inputs default the death case: dependent.months tells the filer, for any non-qualifying-child person who died in 2025, to "enter 12 only if your home was their home for the entire time they were alive ... and 0 otherwise", and dependent.parent_home_paid asks about the parent's main home "for all of 2025". Witness (constructed from fixture stage8.hoh.parent.test1, evaluated by the engine): a dependent parent who died in 2025 after living with the filer for more than half but not all of her lifetime that year, filer paying over half the home cost (home_cost true, months 0 as instructed, parent_home_paid false): project household.hoh_fails true and Form 1040 line 12e refused ('Head of household is checked but the tests are not met'); Pub. 501 makes her a qualifying person, and with months 7 the same return computes line 12e $23,625.00. Triage executable-triage-v1 (triage/household.json): 1,782 of 1,783 agree; the one difference (project-refuses, audit.household.hoh_community_property) is the owner's choice amb.2025.hoh_community_property (i1040gi p. 23, Community Property States) and is ambiguity on its own. Finding recorded in .transcription/proposed/household.findings.md.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| household.all_eic_ssn | household.credit_disallowed | household.credit_disallowed |
| household.all_tin | household.credit_disallowed | household.credit_disallowed |
| household.ctc_ssn | household.credit_disallowed | household.credit_disallowed |

## Raw second transcription

```yaml
```yaml
lines:
  - id: household.h_taxpayer_count
    printed: "(helper)"
    label: "Number of person entries for the taxpayer"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.role, {const: "taxpayer"}]}
  - id: household.h_spouse_count
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
    label: "The people entered on the return do not match the filing status (exactly one taxpayer; a spouse entry only on a joint return)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, ne: [household.h_taxpayer_count, {const: 1, type: Count}]}
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "mfj"}]}
            - {op: test, ne: [household.h_spouse_count, {const: 1, type: Count}]}
        - op: test
          all:
            - {op: test, not: {op: test, eq: [f1040.status, {const: "mfj"}]}}
            - {op: test, ne: [household.h_spouse_count, {const: 0, type: Count}]}
    note: "The IRS pages do not define a roster check. Reading chosen: a return has exactly one taxpayer entry, and has a spouse entry only when the filing status is married filing jointly (1040: 'If joint return, spouse's ...'; 1040 instructions: on a separate return you report only your own income)."
  - id: household.h_hsa_persons
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
    expr: {op: test, ge: [household.h_hsa_persons, {const: 2, type: Count}]}
    note: "Read as: both people on the return have a Form 8889 (i8889, Specific Instructions; How To Complete Part I)."
  - id: household.hsa_split_count
    printed: "(helper)"
    label: "Number of spouses who divide a family contribution limit under the line 6 rules"
    type: Count
    expr: {op: sum_over, collection: person, field: person.hsa_split}
    note: "The pages do not define this aggregate. Read as the total of each person's line 6 split count, so the two spouses' Forms 8889 can be checked against each other (i8889 line 6)."
  - id: household.hsa_agreed_count
    printed: "(helper)"
    label: "Number of spouses using an agreed (not equal) allocation of the family contribution limit"
    type: Count
    expr: {op: sum_over, collection: person, field: person.hsa_agreed}
    note: "Read as the total of each person's agreed-allocation count, for checking that both spouses use the same allocation ('unless you both agree on a different allocation', i8889 line 6)."
  - id: household.hsa_step1_sum
    printed: "(helper)"
    label: "Total of each spouse's line 6 Step 1 refigured family contribution limit"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.hsa_step1}
    note: "The pages do not define this aggregate. Read as the total over people of the Step 1 amount, so other forms can check that both spouses' Step 1 amounts are the same."
  - id: household.hsa_share_sum
    printed: "(helper)"
    label: "Total of the spouses' allocated shares of the family contribution limit"
    type: NonNegDollars
    expr: {op: sum_over, collection: person, field: person.hsa_share}
    note: "Read as the total over people of each spouse's allocated share, so other forms can check that the shares add up to the Step 1 limit (i8889 line 6, Steps 2 and 3)."
  - id: household.h_no_eic_ssn
    printed: "(helper)"
    label: "Number of people on the return without an SSN valid for the EIC"
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
    refuses: [household.credit_disallowed]
    note: "EIC Step 1, question 2. Refuses when Form 8862 may be required, or during a 2- or 10-year ban (i1040 Form 8862, who must file); this tool does not prepare Form 8862."
  - id: household.h_no_tin
    printed: "(helper)"
    label: "Number of people on the return with neither an SSN nor an ITIN issued (or applied for) by the due date"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        not:
          op: test
          any:
            - {op: test, eq: [person.tin, {const: true}]}
            - {op: test, eq: [person.itin_applied, {const: true}]}
  - id: household.all_tin
    printed: "(helper)"
    label: "Did you, and your spouse if filing a joint return, have either an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? (Answer 'Yes' if you are applying for an ITIN on or before the return due date (including extensions).)"
    type: Bool
    expr: {op: test, eq: [household.h_no_tin, {const: 0, type: Count}]}
    refuses: [household.credit_disallowed]
    note: "Dependents Step 5, question 1 (needed for the credit for other dependents). Refuses when Form 8862 may be required (i1040 line 19; i8812)."
  - id: household.h_work_ssn_count
    printed: "(helper)"
    label: "Number of people on the return with an SSN valid for employment issued before the due date"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.work_ssn, {const: true}]}
  - id: household.ctc_ssn
    printed: "(helper)"
    label: "To claim the child tax credit, you must have a valid SSN ... If you are filing a joint return, only one spouse is required to have a valid SSN ... The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date of the return"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, ge: [household.h_work_ssn_count, {const: 1, type: Count}]}
        - {op: test, eq: [household.all_tin, {const: true}]}
    refuses: [household.credit_disallowed]
    note: "i1040 line 19 and 'Before you begin'. Open point: whether an ITIN applied for (not yet issued) by the due date counts for the other spouse. Chosen: yes, reusing all_tin, as Step 5 allows for the ODC. Refuses when Form 8862 may be required."
  - id: household.h_taxpayer_work_ssn_count
    printed: "(helper)"
    label: "Taxpayer entries with an SSN valid for employment"
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
    label: "Do you (the taxpayer) have an SSN valid for employment, issued before the due date of your 2025 return (including extensions)?"
    type: Bool
    expr: {op: test, ge: [household.h_taxpayer_work_ssn_count, {const: 1, type: Count}]}
    note: "The pages do not say which rule uses the taxpayer's own SSN alone. Read literally as the taxpayer's work-valid SSN."
  - id: household.h_hoh_test1_count
    printed: "(helper)"
    label: "Dependents meeting head of household Test 1 (parent's main home)"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where: {op: test, eq: [dependent.hoh_test1, {const: true}]}
  - id: household.h_hoh_test2_count
    printed: "(helper)"
    label: "Persons meeting head of household Test 2 (lived with you more than half the year)"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where: {op: test, eq: [dependent.hoh_test2, {const: true}]}
  - id: household.h_hoh_ok
    printed: "(helper)"
    label: "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies"
    type: Bool
    expr:
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
    note: "Test 2 requires that you paid over half the cost of keeping up your home (household.home_cost). Test 1 is about the parent's home (dependent.parent_home_paid), so it is left to the per-dependent hoh_test1 field. Repeating home_cost with Test 2 is harmless if dependent.hoh_test2 already includes it."
  - id: household.hoh_fails
    printed: "(helper)"
    label: "Head of household is checked but the head of household requirements are not met"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "hoh"}]}
        - {op: test, not: {op: test, eq: [household.h_hoh_ok, {const: true}]}}
    note: "i1040 Filing Status, Head of Household. Read as: the status claimed is HOH and the unmarried and Test 1 / Test 2 conditions are not met."
```
```
