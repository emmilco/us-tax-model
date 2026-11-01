# Transcription agreement — household

Second transcription of `Household facts for dependents and head of household` by an isolated model (spec 6.5), compared line by line with `forms/2025/household.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-01 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | d7bcff0582d13284000fde1202a0a6c7ad68da9fa35f67cd386b49cb1e9911f5 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 4d8eb628ca6285669d98d11acb5d12dc8d923da87657e86b584c7922cb8618bc |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 5466d64fb38b72b9dac93e0afe2ba271ce519579f173651c0c7af2c1e2eeae23 |
| printed lines compared | 17 |
| agree / disagree / missing | 4 / 13 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 13, 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 13, 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| p501 | 2025 returns; PDF created 2026-02-04 | 6, 8, 9, 11 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 6, 8, 11 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| i1040s8812 | 2025; printed date 2026-01-23 | 2 | pages named by another document's citation | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | 2 | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- malformed expression (project schema): data/gt/0 must be string, data/gt/0 must have required property 'const', data/gt/0 must NOT have additional properties
- household.household.h_has_hoh_person: comparison operands have incompatible types

## Lines

### household.persons — Number of people on the return (you, and your spouse if filing jointly)
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}
```

Second:

```json
{"of": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": null}], "op": "sum"}
```

Ruling: model error — Form 1040 p. 1 has taxpayer and joint-return spouse entries separate from Dependents. This interface counts those filers; the candidate adds claimed dependents. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails schema and type validation (`triage/household.deepseek.json`, state invalid); this declaration is outside h_has_hoh_person's dependency closure and is ruled by reading against the source and interface. No sampled equivalence is claimed.

### household.roster_bad — The people entered do not match the filing status
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}], "test": "ne"}], "test": "any"}], "test": "all"}
```

Second:

```json
{"args": [{"const": 0, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.tin"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"param": "qr.gross_income_limit"}, {"input": "dependent.gross_income"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}], "test": "all"}], "test": "any"}], "test": "all"}}], "test": "lt"}
```

Second transcription's note: The archived text does not define this aggregate; I read it as any claimed dependent who fails the qualifying-child/relative tests or is marked as lacking the required TIN.

Ruling: model error — The interface tests whether taxpayer/spouse entries match Filing Status (Form 1040 p. 1), not whether dependents fail qualifying tests or lack TINs. The candidate substitutes a dependent-screening predicate and omits the filer-roster invariant. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.

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

Second transcription's note: Read as both person entries (taxpayer and spouse) having at least one HSA/Form 8889.

Ruling: representation — i8889 p. 4 says to complete separate Forms 8889 if both spouses have HSAs. On a valid roster there are at most two persons, so >= 2 and == 2 persons with >= 1 vs > 0 Forms 8889 express the same condition. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line does not depend on h_has_hoh_person and is ruled by reading. No sampled equivalence is claimed.

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
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"ref": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "person.eic_ssn"}], "test": "eq"}}], "test": "eq"}], "test": "all"}
```

Ruling: model error — i1040gi p. 40, Step 1, question 2 tests the filer and joint spouse SSNs, whereas qualifying-child SSNs are separately counted for the worksheet credit. The candidate requires every EIC child to have an SSN as part of this filer gate. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.

### household.all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **DISAGREE**

Project:

```json
{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.itin_applied"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}], "test": "any"}}], "test": "eq"}
```

Second:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"ref": "dependent.tin"}], "test": "eq"}], "test": "all"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": false}, {"ref": "person.tin"}], "test": "eq"}}], "test": "eq"}], "test": "all"}
```

Ruling: model error — i1040gi p. 19, Step 5, question 1 concerns you and your spouse if filing jointly. The candidate adds dependent TIN eligibility to a filer-only public interface. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.

### household.ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "any"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}], "test": "any"}}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"ref": "dependent.work_ssn"}], "test": "eq"}], "test": "all"}}], "test": "eq"}, {"args": [{"const": 1, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.work_ssn"}], "test": "eq"}}], "test": "le"}], "test": "all"}
```

Second transcription's note: Read as at least one filer with an SSN valid for employment (for a joint return, only one spouse needs it) and every child for whom the CTC is claimed having such an SSN; the other spouse's SSN/ITIN is covered by all_tin.

Ruling: model error — i1040gi p. 17, Before you begin (and i1040s8812 p. 2) separates filer/spouse identification from the child SSN condition. The candidate folds the dependent-side CTC SSN condition into this filer-side interface and omits the other spouse's SSN/ITIN requirement on a joint return. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.

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

Ruling: representation — i1040gi p. 18. Both expressions restrict the sum over person to person.role == "taxpayer" and person.work_ssn == true; the candidate compares the nonnegative integral count with >= 1 instead of > 0. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line does not depend on h_has_hoh_person and is ruled by reading. No sampled equivalence is claimed.

### household.hoh_fails — Head of household checked without meeting its tests
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.born_died"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.placed"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.part_year_home"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.absence_no_return"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": true}, {"input": "household.home_cost"}], "test": "ne"}], "test": "any"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"expression": {"args": [{"args": [{"unknown": "{\"collection\": \"dependent\", \"field\": \"dependent.one\", \"op\": \"sum_over\", \"where\": {\"any\": [{\"eq\": [\"dependent.hoh_test1\", {\"const\": true}], \"op\": \"test\"}, {\"eq\": [\"dependent.hoh_test2\", {\"const\": true}], \"op\": \"test\"}], \"op\": \"test\"}}"}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": true}, {"input": "household.home_cost"}], "test": "ne"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}, "invalid_model_types": [{"line": "household.h_has_hoh_person", "message": "malformed expression (project schema): data/gt/0 must be string, data/gt/0 must have required property 'const', data/gt/0 must NOT have additional properties"}, {"line": "household.h_has_hoh_person", "message": "household.household.h_has_hoh_person: comparison operands have incompatible types"}]}
```

Ruling: model error — Validation failure and merits: the candidate expression depends on helper household.h_has_hoh_person, which fails project schema and type validation (`triage/household.deepseek.json`, state invalid: "malformed expression (project schema): data/gt/0 must be string" and "comparison operands have incompatible types"). By reading, it also applies household.home_cost to Test 1 (i1040gi p. 14). This adjudicates the invalid dependency chain and the expression reading; no sampled equivalence is claimed.

### household.qss_fails — Qualifying surviving spouse checked without meeting its tests
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.qss_eligible"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"const": true}, {"input": "household.qss_eligible"}], "test": "ne"}
```

Ruling: model error — i1040gi p. 15 Qualifying Surviving Spouse tests apply when QSS is selected. The candidate drops f1040.status == "qss" and reads household.qss_eligible unconditionally on every filing status. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.

### household.widowed_2025 — Filing as single or head of household although your spouse died in 2025
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"input": "household.spouse_died_2025"}
```

Ruling: model error — p501 p. 6 allows joint filing after a spouse dies in 2025. This owner-selected refusal gate (BUG-0277) applies only to single/HOH selections (status == "single" or status == "hoh"), as the published label specifies. The candidate copies household.spouse_died_2025 without the status guard. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.

### household.cp_marriage_ended — Not filing jointly, and married for part of 2025 while living in a community property stat
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.community_property"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.cp_married"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.community_property"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.cp_married"}], "test": "eq"}], "test": "all"}
```

Ruling: model error — i1040gi p. 23 community-income scope is implemented by the conjunction of nonjoint status (f1040.status != "mfj"), community-state residence, married == false and cp_married == true (BUG-0278). The candidate omits the f1040.status != "mfj" guard. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.

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

Ruling: model error — i1040gi p. 23 and p501 p. 6 scope the registered domestic partner community-property refusal by f1040.status != "mfj" and community_property == true. The candidate omits the f1040.status != "mfj" guard. Executable triage was unavailable for this entire reply because household.h_has_hoh_person fails validation (`triage/household.deepseek.json`, state invalid); this line is outside h_has_hoh_person's closure and is ruled by reading. No sampled equivalence is claimed.

### household.filing_status_conflict — The filing status conflicts with the marriage facts entered
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.married"}], "test": "eq"}], "test": "all"}], "test": "any"}
```

Second:

```json
{"expression": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "household.home_cost"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"unknown": "{\"collection\": \"dependent\", \"field\": \"dependent.one\", \"op\": \"sum_over\", \"where\": {\"any\": [{\"eq\": [\"dependent.hoh_test1\", {\"const\": true}], \"op\": \"test\"}, {\"eq\": [\"dependent.hoh_test2\", {\"const\": true}], \"op\": \"test\"}], \"op\": \"test\"}}"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.qss_eligible"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"unknown": "{\"collection\": \"dependent\", \"field\": \"dependent.one\", \"op\": \"sum_over\", \"where\": {\"any\": [{\"eq\": [\"dependent.hoh_test1\", {\"const\": true}], \"op\": \"test\"}, {\"eq\": [\"dependent.hoh_test2\", {\"const\": true}], \"op\": \"test\"}], \"op\": \"test\"}}"}, {"const": 0, "type": "Count"}], "test": "le"}, {"args": [{"const": true}, {"input": "household.home_cost"}], "test": "ne"}, {"args": [{"const": true}, {"input": "household.unmarried"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.qss_eligible"}], "test": "ne"}], "test": "all"}], "test": "any"}, "invalid_model_types": [{"line": "household.h_has_hoh_person", "message": "malformed expression (project schema): data/gt/0 must be string, data/gt/0 must have required property 'const', data/gt/0 must NOT have additional properties"}, {"line": "household.h_has_hoh_person", "message": "household.household.h_has_hoh_person: comparison operands have incompatible types"}]}
```

Second transcription's note: The archived text does not define this aggregate; I read it as the selected filing status conflicting with the factual marital, HOH and QSS facts: single only when no HOH/QSS qualification and not married; MFJ/MFS only when married at year end or the spouse died in 2025; HOH and QSS only when their tests pass.

Ruling: model error — Validation failure and merits: the candidate expression depends on helper household.h_has_hoh_person, which fails project schema and type validation (`triage/household.deepseek.json`, state invalid). By reading, it also conflates HOH/QSS qualification tests with the marriage/filing-status entry conflict gate (BUG-0286) and requires single filers to fail HOH/QSS tests. No sampled equivalence is claimed.

## Raw second transcription

```yaml
lines:
  - id: household.h_filers_count
    printed: "(helper)"
    label: "Number of filer entries (taxpayer and spouse, if any)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one

  - id: household.h_dependents_count
    printed: "(helper)"
    label: "Number of claimed dependents"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where:
        op: test
        eq: ["dependent.claimed", {const: true}]

  - id: household.persons
    printed: "(helper)"
    label: "Number of persons on the return (you, your spouse if filing jointly, and claimed dependents)"
    type: Count
    expr:
      op: sum
      of: ["household.h_filers_count", "household.h_dependents_count"]

  - id: household.h_bad_roster_count
    printed: "(helper)"
    label: "Claimed dependents who are not qualifying children or relatives or lack a required TIN"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where:
        op: test
        all:
          - op: test
            eq: ["dependent.claimed", {const: true}]
          - op: test
            any:
              - op: test
                eq: ["dependent.claimed_no_tin", {const: true}]
              - op: test
                all:
                  - op: test
                    eq: ["dependent.qualifying_child", {const: false}]
                  - op: test
                    eq: ["dependent.qualifying_relative", {const: false}]

  - id: household.roster_bad
    printed: "(helper)"
    label: "Dependent roster has a claimed dependent who is not a qualifying child or relative, or lacks a required TIN"
    type: Bool
    expr:
      op: test
      gt: ["household.h_bad_roster_count", {const: 0, type: Count}]
    note: "The archived text does not define this aggregate; I read it as any claimed dependent who fails the qualifying-child/relative tests or is marked as lacking the required TIN."

  - id: household.h_hsa_person_count
    printed: "(helper)"
    label: "Persons with at least one Form 8889/HSA"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        ge: ["person.hsa_forms", {const: 1, type: Count}]

  - id: household.hsa_both
    printed: "(helper)"
    label: "Both spouses have HSAs"
    type: Bool
    expr:
      op: test
      ge: ["household.h_hsa_person_count", {const: 2, type: Count}]
    note: "Read as both person entries (taxpayer and spouse) having at least one HSA/Form 8889."

  - id: household.hsa_split_count
    printed: "(helper)"
    label: "Total HSA split-count entries"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.hsa_split

  - id: household.hsa_agreed_count
    printed: "(helper)"
    label: "Total HSA agreed-allocation entries"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.hsa_agreed

  - id: household.hsa_step1_sum
    printed: "(helper)"
    label: "Total HSA Step 1 family contribution limits"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.hsa_step1

  - id: household.hsa_share_sum
    printed: "(helper)"
    label: "Total HSA allocated shares"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.hsa_share

  - id: household.h_eic_person_bad
    printed: "(helper)"
    label: "Filers without a valid EIC SSN"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        eq: ["person.eic_ssn", {const: false}]

  - id: household.h_eic_dep_bad
    printed: "(helper)"
    label: "EIC children without a valid EIC SSN"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where:
        op: test
        all:
          - op: test
            eq: ["dependent.eic_child", {const: true}]
          - op: test
            eq: ["dependent.eic_ssn", {const: false}]

  - id: household.all_eic_ssn
    printed: "(helper)"
    label: "Every person whose SSN is needed for the EIC has a valid EIC SSN"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: ["household.h_eic_person_bad", {const: 0, type: Count}]
        - op: test
          eq: ["household.h_eic_dep_bad", {const: 0, type: Count}]

  - id: household.h_tin_person_bad
    printed: "(helper)"
    label: "Filers without an SSN, ITIN or ATIN issued on time"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        eq: ["person.tin", {const: false}]

  - id: household.h_tin_dep_bad
    printed: "(helper)"
    label: "Claimed dependents without an SSN, ITIN or ATIN issued on time"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where:
        op: test
        all:
          - op: test
            eq: ["dependent.claimed", {const: true}]
          - op: test
            eq: ["dependent.tin", {const: false}]

  - id: household.all_tin
    printed: "(helper)"
    label: "Every person and claimed dependent has an SSN, ITIN or ATIN issued on time"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: ["household.h_tin_person_bad", {const: 0, type: Count}]
        - op: test
          eq: ["household.h_tin_dep_bad", {const: 0, type: Count}]

  - id: household.h_taxpayer_work_count
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
          - op: test
            eq: ["person.role", {const: "taxpayer"}]
          - op: test
            eq: ["person.work_ssn", {const: true}]

  - id: household.taxpayer_work_ssn
    printed: "(helper)"
    label: "Taxpayer has an SSN valid for employment"
    type: Bool
    expr:
      op: test
      ge: ["household.h_taxpayer_work_count", {const: 1, type: Count}]

  - id: household.h_ctc_filer_work
    printed: "(helper)"
    label: "Filers with an SSN valid for employment"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        eq: ["person.work_ssn", {const: true}]

  - id: household.h_ctc_child_bad
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
          - op: test
            eq: ["dependent.ctc_child", {const: true}]
          - op: test
            eq: ["dependent.work_ssn", {const: false}]

  - id: household.ctc_ssn
    printed: "(helper)"
    label: "At least one filer has an SSN valid for employment and every CTC child has one"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          ge: ["household.h_ctc_filer_work", {const: 1, type: Count}]
        - op: test
          eq: ["household.h_ctc_child_bad", {const: 0, type: Count}]
    note: "Read as at least one filer with an SSN valid for employment (for a joint return, only one spouse needs it) and every child for whom the CTC is claimed having such an SSN; the other spouse's SSN/ITIN is covered by all_tin."

  - id: household.h_has_hoh_person
    printed: "(helper)"
    label: "A person who satisfies the head of household qualifying-person test"
    type: Bool
    expr:
      op: test
      gt:
        - op: sum_over
          collection: dependent
          field: dependent.one
          where:
            op: test
            any:
              - op: test
                eq: ["dependent.hoh_test1", {const: true}]
              - op: test
                eq: ["dependent.hoh_test2", {const: true}]
        - {const: 0, type: Count}

  - id: household.hoh_fails
    printed: "(helper)"
    label: "Head of household tests fail"
    type: Bool
    expr:
      op: test
      not:
        op: test
        all:
          - op: test
            eq: ["household.unmarried", {const: true}]
          - op: test
            eq: ["household.home_cost", {const: true}]
          - op: test
            eq: ["household.h_has_hoh_person", {const: true}]

  - id: household.qss_fails
    printed: "(helper)"
    label: "Qualifying surviving spouse tests fail"
    type: Bool
    expr:
      op: test
      not:
        op: test
        eq: ["household.qss_eligible", {const: true}]

  - id: household.widowed_2025
    printed: "(helper)"
    label: "Spouse died in 2025"
    type: Bool
    expr:
      op: copy
      from: household.spouse_died_2025

  - id: household.cp_marriage_ended
    printed: "(helper)"
    label: "Lived in a community property state, were married during 2025, and were not married at the end of 2025"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: ["household.community_property", {const: true}]
        - op: test
          eq: ["household.cp_married", {const: true}]
        - op: test
          eq: ["household.married", {const: false}]

  - id: household.rdp_community_property
    printed: "(helper)"
    label: "Registered domestic partner in a community property state"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: ["household.rdp", {const: true}]
        - op: test
          eq: ["household.community_property", {const: true}]

  - id: household.filing_status_conflict
    printed: "(helper)"
    label: "Selected filing status conflicts with the household facts"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - op: test
              eq: ["f1040.status", {const: "single"}]
            - op: test
              any:
                - op: test
                  eq: ["household.married", {const: true}]
                - op: test
                  eq: ["household.hoh_fails", {const: false}]
                - op: test
                  eq: ["household.qss_fails", {const: false}]
        - op: test
          all:
            - op: test
              eq: ["f1040.status", {const: "mfj"}]
            - op: test
              eq: ["household.married", {const: false}]
            - op: test
              eq: ["household.widowed_2025", {const: false}]
        - op: test
          all:
            - op: test
              eq: ["f1040.status", {const: "mfs"}]
            - op: test
              eq: ["household.married", {const: false}]
            - op: test
              eq: ["household.widowed_2025", {const: false}]
        - op: test
          all:
            - op: test
              eq: ["f1040.status", {const: "hoh"}]
            - op: test
              eq: ["household.hoh_fails", {const: true}]
        - op: test
          all:
            - op: test
              eq: ["f1040.status", {const: "qss"}]
            - op: test
              eq: ["household.qss_fails", {const: true}]
    note: "The archived text does not define this aggregate; I read it as the selected filing status conflicting with the factual marital, HOH and QSS facts: single only when no HOH/QSS qualification and not married; MFJ/MFS only when married at year end or the spouse died in 2025; HOH and QSS only when their tests pass."
```
