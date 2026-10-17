# Transcription agreement — dependent

Second transcription of `Dependents — qualifying child and qualifying relative tests, per person listed` by an isolated model (spec 6.5), compared line by line with `forms/2025/dependent.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f855fd573d216600972cb7a3091738b13598a336c35d1c068d3f1c0753663c2e |
| printed lines compared | 10 |
| agree / disagree / missing | 3 / 7 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19, 20, 21, 41, 43, 44, 45, 46 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 17, 18, 19, 20, 21, 41, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |

## Lines

### dependent.one — One person listed
Status: **AGREE**

### dependent.ctc_child — Qualifying child for the child tax credit (Step 3)
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}
```

Second transcription's note: In Step 3, question 4, the taxpayer's own SSN valid for employment (you, or your spouse if filing jointly) comes from household.taxpayer_work_ssn.

Ruling: scope and representation; project retained. The second transcription folds the qualifying-child, dependency and credit tests into each line; it also lets the rule for children of divorced or separated parents stand in for residency and omits the 'you can be claimed as a dependent' condition (`sa.dependent`), both refused in scope (`dependent.divorced_rule` refuses the entry; `sa.dependent` refuses the standard deduction). Compared by sampling 40,000 inputs per line with every refusal trigger false and consistent answers (only a married person files a joint return; over half of a person's support cannot come from both the person and you): no difference on the child tax credit lines; the remaining differences on odc_person, odc_amount and hoh_test2 all come from the second treating `sibling_descendant` as a Step 4 relative, which the enum defines as any other descendant of a sibling (a Step 4 relative only as a household member who lived with you all year; i1040gi p. 19 lists only a son or daughter of a sibling, which is `sibling`), and from `other` living with you all year, which the all-year household bullet admits. No change.

### dependent.odc_person — Dependent for the credit for other dependents (Steps 3 and 5)
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_tin"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}], "test": "any"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_tin"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.multiple_support"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}], "test": "any"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_tin"}], "test": "eq"}], "test": "all"}], "test": "any"}
```

Ruling: scope and representation; project retained. The second transcription folds the qualifying-child, dependency and credit tests into each line; it also lets the rule for children of divorced or separated parents stand in for residency and omits the 'you can be claimed as a dependent' condition (`sa.dependent`), both refused in scope (`dependent.divorced_rule` refuses the entry; `sa.dependent` refuses the standard deduction). Compared by sampling 40,000 inputs per line with every refusal trigger false and consistent answers (only a married person files a joint return; over half of a person's support cannot come from both the person and you): no difference on the child tax credit lines; the remaining differences on odc_person, odc_amount and hoh_test2 all come from the second treating `sibling_descendant` as a Step 4 relative, which the enum defines as any other descendant of a sibling (a Step 4 relative only as a household member who lived with you all year; i1040gi p. 19 lists only a son or daughter of a sibling, which is `sibling`), and from `other` living with you all year, which the all-year household bullet admits. No change.

### dependent.ctc_amount — Child tax credit amount for this person before limits ($2,200 for a qualifying child, else
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}, "then": {"param": "ctc.per_child"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}, "then": {"param": "ctc.per_child"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}], "test": "any"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: scope and representation; project retained. The second transcription folds the qualifying-child, dependency and credit tests into each line; it also lets the rule for children of divorced or separated parents stand in for residency and omits the 'you can be claimed as a dependent' condition (`sa.dependent`), both refused in scope (`dependent.divorced_rule` refuses the entry; `sa.dependent` refuses the standard deduction). Compared by sampling 40,000 inputs per line with every refusal trigger false and consistent answers (only a married person files a joint return; over half of a person's support cannot come from both the person and you): no difference on the child tax credit lines; the remaining differences on odc_person, odc_amount and hoh_test2 all come from the second treating `sibling_descendant` as a Step 4 relative, which the enum defines as any other descendant of a sibling (a Step 4 relative only as a household member who lived with you all year; i1040gi p. 19 lists only a son or daughter of a sibling, which is `sibling`), and from `other` living with you all year, which the all-year household bullet admits. No change.

### dependent.odc_amount — Credit for other dependents amount for this person before limits ($500 for an other depend
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_tin"}], "test": "eq"}], "test": "all"}, "then": {"param": "odc.per_dependent"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"param": "qr.gross_income_limit"}, {"input": "dependent.gross_income"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_tin"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}], "test": "any"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_tin"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.multiple_support"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "ne"}], "test": "any"}, {"args": [{"param": "qr.gross_income_limit"}, {"input": "dependent.gross_income"}], "test": "le"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_tin"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}], "test": "any"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_tin"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.multiple_support"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}], "test": "any"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_tin"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"param": "odc.per_dependent"}}], "op": "choose"}
```

Ruling: scope and representation; project retained. The second transcription folds the qualifying-child, dependency and credit tests into each line; it also lets the rule for children of divorced or separated parents stand in for residency and omits the 'you can be claimed as a dependent' condition (`sa.dependent`), both refused in scope (`dependent.divorced_rule` refuses the entry; `sa.dependent` refuses the standard deduction). Compared by sampling 40,000 inputs per line with every refusal trigger false and consistent answers (only a married person files a joint return; over half of a person's support cannot come from both the person and you): no difference on the child tax credit lines; the remaining differences on odc_person, odc_amount and hoh_test2 all come from the second treating `sibling_descendant` as a Step 4 relative, which the enum defines as any other descendant of a sibling (a Step 4 relative only as a household member who lived with you all year; i1040gi p. 19 lists only a son or daughter of a sibling, which is `sibling`), and from `other` living with you all year, which the all-year household bullet admits. No change.

### dependent.actc_amount — Additional child tax credit ceiling for this person ($1,700 for a qualifying child, else 0
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}, "then": {"param": "actc.per_child"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}, "then": {"param": "actc.per_child"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}], "test": "any"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: scope and representation; project retained. The second transcription folds the qualifying-child, dependency and credit tests into each line; it also lets the rule for children of divorced or separated parents stand in for residency and omits the 'you can be claimed as a dependent' condition (`sa.dependent`), both refused in scope (`dependent.divorced_rule` refuses the entry; `sa.dependent` refuses the standard deduction). Compared by sampling 40,000 inputs per line with every refusal trigger false and consistent answers (only a married person files a joint return; over half of a person's support cannot come from both the person and you): no difference on the child tax credit lines; the remaining differences on odc_person, odc_amount and hoh_test2 all come from the second treating `sibling_descendant` as a Step 4 relative, which the enum defines as any other descendant of a sibling (a Step 4 relative only as a household member who lived with you all year; i1040gi p. 19 lists only a son or daughter of a sibling, which is `sibling`), and from `other` living with you all year, which the all-year household bullet admits. No change.

### dependent.hoh_test2 — A Test 2 person who lived with you more than half the year (the home-cost condition of Tes
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.multiple_support"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "ne"}], "test": "any"}, {"args": [{"param": "qr.gross_income_limit"}, {"input": "dependent.gross_income"}], "test": "le"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}], "test": "any"}], "test": "any"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.multiple_support"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}], "test": "any"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.divorced_rule"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.multiple_support"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}
```

Ruling: scope and representation; project retained. The second transcription folds the qualifying-child, dependency and credit tests into each line; it also lets the rule for children of divorced or separated parents stand in for residency and omits the 'you can be claimed as a dependent' condition (`sa.dependent`), both refused in scope (`dependent.divorced_rule` refuses the entry; `sa.dependent` refuses the standard deduction). Compared by sampling 40,000 inputs per line with every refusal trigger false and consistent answers (only a married person files a joint return; over half of a person's support cannot come from both the person and you): no difference on the child tax credit lines; the remaining differences on odc_person, odc_amount and hoh_test2 all come from the second treating `sibling_descendant` as a Step 4 relative, which the enum defines as any other descendant of a sibling (a Step 4 relative only as a household member who lived with you all year; i1040gi p. 19 lists only a son or daughter of a sibling, which is `sibling`), and from `other` living with you all year, which the all-year household bullet admits. No change.

### dependent.hoh_test1 — Qualifies you for head of household under Test 1 through a parent who does not live with y
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.divorced_rule"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.other_claimant"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "dependent.multiple_support"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}], "test": "any"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.multiple_support"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}], "test": "all"}
```

Second transcription's note: As specified, Test 1 here covers only a parent who doesn't live with you, read as not living with you for more than half the year. A parent who lives with you is covered by Test 2.

Ruling: representation; project retained. Following the helper label, the second transcription adds 'lives with you no more than half the year' to Test 1; the project reads only the question 'For a parent not living with you, you paid over half the cost of their main home for all of 2025?'. They differ only when that question is answered yes for a parent who lives with you; such a dependent parent qualifies the filer through Test 2, item 1 (hoh_test2 admits a claimed parent who lived with you more than half the year), so head of household eligibility is the same. Sampling (40,000 inputs, refusal triggers false) finds no other difference.

### dependent.eic_child — Qualifying child for the EIC (relationship, age, not filing a joint return, lived with you
Status: **AGREE**

### dependent.eic_ssn_child — Qualifying child for the EIC who has a valid SSN
Status: **AGREE**

## Raw second transcription

```yaml
```yaml
lines:
  - id: dependent.one
    printed: "(helper)"
    label: "One person listed"
    type: Count
    expr: {op: param, ref: dependent.one}

  - id: dependent.h_zero
    printed: "(helper)"
    label: "No amount for this person"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "The atoms cannot use a constant zero as a choose branch, so the year parameter sales.zero (0) is used here, as other forms do."

  - id: dependent.h_rel_child
    printed: "(helper)"
    label: "Son, daughter, stepchild, foster child, or a descendant of any of them"
    type: Bool
    expr: {op: test, eq: [dependent.relationship, {const: "child"}]}

  - id: dependent.h_rel_sibling
    printed: "(helper)"
    label: "Brother, sister, stepbrother, stepsister, half brother, half sister"
    type: Bool
    expr: {op: test, eq: [dependent.relationship, {const: "sibling"}]}

  - id: dependent.h_rel_sibling_descendant
    printed: "(helper)"
    label: "A descendant of a brother, sister, stepbrother, stepsister, half brother or half sister (for example, your niece or nephew)"
    type: Bool
    expr: {op: test, eq: [dependent.relationship, {const: "sibling_descendant"}]}

  - id: dependent.h_qc_relationship
    printed: "(helper)"
    label: "A qualifying child is your son, daughter, stepchild, foster child, brother, sister, stepbrother, stepsister, half brother, half sister, or a descendant of any of them"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.h_rel_child, {const: true}]}
        - {op: test, eq: [dependent.h_rel_sibling, {const: true}]}
        - {op: test, eq: [dependent.h_rel_sibling_descendant, {const: true}]}

  - id: dependent.h_under19_younger
    printed: "(helper)"
    label: "Under age 19 at the end of 2025 and younger than you (or your spouse if filing jointly)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, lt: [dependent.age, {param: qc.age_limit}]}
        - {op: test, eq: [dependent.younger, {const: true}]}

  - id: dependent.h_student_younger
    printed: "(helper)"
    label: "Under age 24 at the end of 2025, a full-time student, and younger than you (or your spouse if filing jointly)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, lt: [dependent.age, {param: qc.student_age_limit}]}
        - {op: test, eq: [dependent.student, {const: true}]}
        - {op: test, eq: [dependent.younger, {const: true}]}

  - id: dependent.h_qc_age
    printed: "(helper)"
    label: "Under 19 and younger than you, or under 24, a full-time student and younger than you, or any age and permanently and totally disabled"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.h_under19_younger, {const: true}]}
        - {op: test, eq: [dependent.h_student_younger, {const: true}]}
        - {op: test, eq: [dependent.disabled, {const: true}]}

  - id: dependent.h_lived_half
    printed: "(helper)"
    label: "Who lived with you for more than half of 2025"
    type: Bool
    expr: {op: test, gt: [dependent.months, {const: 6}]}
    note: "The text says 'more than half of 2025'. This is read as more than 6 of the months in dependent.months, which already counts temporary absences. The exceptions for a person born, who died, was adopted or was placed with you in 2025 are not modelled separately. The months input is assumed to reflect them."

  - id: dependent.h_qc_core
    printed: "(helper)"
    label: "Meets the qualifying child relationship and age tests, didn't provide over half of their own support, and isn't filing a joint return (other than only for a refund)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qc_relationship, {const: true}]}
        - {op: test, eq: [dependent.h_qc_age, {const: true}]}
        - {op: test, eq: [dependent.self_support, {const: false}]}
        - {op: test, eq: [dependent.joint_return, {const: false}]}

  - id: dependent.h_qc_raw
    printed: "(helper)"
    label: "Meets all Step 1 conditions, including living with you for more than half of 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qc_core, {const: true}]}
        - {op: test, eq: [dependent.h_lived_half, {const: true}]}

  - id: dependent.h_qualifying_child
    printed: "(helper)"
    label: "Step 1, question 1. Do you have a child who meets the conditions to be your qualifying child?"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qc_core, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [dependent.h_lived_half, {const: true}]}
            - {op: test, eq: [dependent.divorced_rule, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [dependent.other_claimant, {const: false}]}
            - {op: test, eq: [dependent.divorced_rule, {const: true}]}
    note: "Two points are open. (1) 'Qualifying child of more than one person' sends you to tie-breaker rules that can't be decided from these inputs. A child who meets the conditions for another person is conservatively treated as not your qualifying child, unless the rule for children of divorced or separated parents applies. (2) When that divorced-parents rule applies, the child is treated as the qualifying child of the noncustodial parent, so the time-lived test and the other-claimant bar are waived."

  - id: dependent.h_resident
    printed: "(helper)"
    label: "Was the person a U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico?"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.citizen, {const: true}]}
        - {op: test, eq: [dependent.canada_mexico, {const: true}]}

  - id: dependent.h_qc_dependent
    printed: "(helper)"
    label: "Step 2. Your qualifying child is your dependent"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qualifying_child, {const: true}]}
        - {op: test, eq: [dependent.h_resident, {const: true}]}
    note: "Step 2, question 2 (married child): under 'Married person', only a joint return other than for a refund blocks the claim, and Step 1 already tests that. Step 2, question 4 (could you be claimed as a dependent on someone else's return) is a taxpayer-level question with no input on this form, so it isn't encoded here."

  - id: dependent.h_rel_relative
    printed: "(helper)"
    label: "Step 4 relative: child or descendant, sibling or their son or daughter, parent or ancestor or their sibling, step-relative or in-law"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.relationship, {const: "child"}]}
        - {op: test, eq: [dependent.relationship, {const: "sibling"}]}
        - {op: test, eq: [dependent.relationship, {const: "sibling_descendant"}]}
        - {op: test, eq: [dependent.relationship, {const: "parent"}]}
        - {op: test, eq: [dependent.relationship, {const: "parent_relative"}]}
        - {op: test, eq: [dependent.relationship, {const: "in_law"}]}

  - id: dependent.h_household_all_year
    printed: "(helper)"
    label: "Any other person (other than your spouse) who lived with you all year as a member of your household"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.relationship, {const: "household_member"}]}
        - {op: test, eq: [dependent.months, {const: 12}]}
    note: "'Lived with you all year' is read as 12 months in dependent.months. The household_member value is assumed to mean the relationship didn't violate local law and the person isn't your spouse."

  - id: dependent.h_qr_relationship
    printed: "(helper)"
    label: "A relative listed in Step 4, or any other person who lived with you all year as a member of your household"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.h_rel_relative, {const: true}]}
        - {op: test, eq: [dependent.h_household_all_year, {const: true}]}

  - id: dependent.h_not_qc_of_any
    printed: "(helper)"
    label: "Who wasn't a qualifying child (see Step 1) of any taxpayer for 2025"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qc_raw, {const: false}]}
        - {op: test, eq: [dependent.other_claimant, {const: false}]}

  - id: dependent.h_qr_income
    printed: "(helper)"
    label: "Who had gross income of less than $5,200 in 2025"
    type: Bool
    expr: {op: test, lt: [dependent.gross_income, {param: qr.gross_income_limit}]}
    note: "Under the exception to the gross income test, for a permanently and totally disabled person certain sheltered-workshop income 'may be excluded' (see Pub. 501). The text doesn't give that rule. dependent.gross_income is taken as already net of any such exclusion."

  - id: dependent.h_support
    printed: "(helper)"
    label: "For whom you provided over half of the person's support in 2025 (or you're treated as having done so under a multiple support agreement)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.supported, {const: true}]}
        - {op: test, eq: [dependent.multiple_support, {const: true}]}
    note: "'Multiple support agreements' says special rules may treat you as having provided over half the support. A person claimed under such an agreement is treated as meeting the support test."

  - id: dependent.h_qualifying_relative
    printed: "(helper)"
    label: "Step 4, question 1. Does any person meet the conditions to be your qualifying relative?"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qr_relationship, {const: true}]}
        - {op: test, eq: [dependent.h_not_qc_of_any, {const: true}]}
        - {op: test, eq: [dependent.h_qr_income, {const: true}]}
        - {op: test, eq: [dependent.h_support, {const: true}]}

  - id: dependent.h_qr_dependent
    printed: "(helper)"
    label: "Step 4. Your qualifying relative is your dependent"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qualifying_relative, {const: true}]}
        - {op: test, eq: [dependent.h_resident, {const: true}]}
        - {op: test, eq: [dependent.joint_return, {const: false}]}
    note: "Step 4, question 3 (married) is applied through 'Married person': a joint return other than only for a refund blocks the claim. Question 5 (could you be claimed by someone else) has no input on this form and isn't encoded."

  - id: dependent.h_claimed
    printed: "(helper)"
    label: "Your dependent (Step 2 or Step 4)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.h_qc_dependent, {const: true}]}
        - {op: test, eq: [dependent.h_qr_dependent, {const: true}]}

  - id: dependent.h_under_ctc_age
    printed: "(helper)"
    label: "Step 3, question 3. Was the child under age 17 at the end of 2025?"
    type: Bool
    expr: {op: test, lt: [dependent.age, {param: ctc.age_limit}]}

  - id: dependent.ctc_child
    printed: "(helper)"
    label: "Qualifying child for the child tax credit (Step 3)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qc_dependent, {const: true}]}
        - {op: test, eq: [dependent.tin, {const: true}]}
        - {op: test, eq: [dependent.citizen, {const: true}]}
        - {op: test, eq: [dependent.h_under_ctc_age, {const: true}]}
        - {op: test, eq: [dependent.work_ssn, {const: true}]}
        - {op: test, eq: [household.taxpayer_work_ssn, {const: true}]}
    note: "In Step 3, question 4, the taxpayer's own SSN valid for employment (you, or your spouse if filing jointly) comes from household.taxpayer_work_ssn."

  - id: dependent.h_odc_qc
    printed: "(helper)"
    label: "Qualifying child dependent who qualifies you for the credit for other dependents (Step 3, question 3 No, or question 4 No and then Step 5)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qc_dependent, {const: true}]}
        - {op: test, eq: [dependent.tin, {const: true}]}
        - {op: test, eq: [dependent.citizen, {const: true}]}
        - {op: test, eq: [household.taxpayer_tin, {const: true}]}
        - {op: test, eq: [dependent.ctc_child, {const: false}]}
    note: "The taxpayer SSN/ITIN requirement comes from 'Before you begin' and Step 5, question 1. It is applied on both the Step 3 question 3 'No' path and the question 4 'No' to Step 5 path."

  - id: dependent.h_odc_qr
    printed: "(helper)"
    label: "Step 5. Your qualifying relative qualifies you for the credit for other dependents"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qr_dependent, {const: true}]}
        - {op: test, eq: [household.taxpayer_tin, {const: true}]}
        - {op: test, eq: [dependent.tin, {const: true}]}
        - {op: test, eq: [dependent.citizen, {const: true}]}

  - id: dependent.odc_person
    printed: "(helper)"
    label: "Dependent for the credit for other dependents (Steps 3 and 5)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [dependent.h_odc_qc, {const: true}]}
        - {op: test, eq: [dependent.h_odc_qr, {const: true}]}

  - id: dependent.h_ctc_per_child
    printed: "(helper)"
    label: "Year parameter ctc.per_child ($2,200)"
    type: NonNegDollars
    expr: {op: param, ref: ctc.per_child}

  - id: dependent.ctc_amount
    printed: "(helper)"
    label: "Child tax credit amount for this person before limits ($2,200 for a qualifying child, else 0)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.ctc_child, {const: true}]}, then: dependent.h_ctc_per_child}
        - {guard: {op: test, eq: [dependent.ctc_child, {const: false}]}, then: dependent.h_zero}

  - id: dependent.h_odc_per_dependent
    printed: "(helper)"
    label: "Year parameter odc.per_dependent ($500)"
    type: NonNegDollars
    expr: {op: param, ref: odc.per_dependent}

  - id: dependent.odc_amount
    printed: "(helper)"
    label: "Credit for other dependents amount for this person before limits ($500 for an other dependent, else 0)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.odc_person, {const: true}]}, then: dependent.h_odc_per_dependent}
        - {guard: {op: test, eq: [dependent.odc_person, {const: false}]}, then: dependent.h_zero}

  - id: dependent.h_actc_per_child
    printed: "(helper)"
    label: "Year parameter actc.per_child ($1,700)"
    type: NonNegDollars
    expr: {op: param, ref: actc.per_child}

  - id: dependent.actc_amount
    printed: "(helper)"
    label: "Additional child tax credit ceiling for this person ($1,700 for a qualifying child, else 0)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [dependent.ctc_child, {const: true}]}, then: dependent.h_actc_per_child}
        - {guard: {op: test, eq: [dependent.ctc_child, {const: false}]}, then: dependent.h_zero}

  - id: dependent.h_t2_dependent
    printed: "(helper)"
    label: "Test 2, item 1. Any person whom you can claim as a dependent, excluding a child claimed under the divorced or separated parents rule, a person who is your dependent only because they lived with you all of 2025, or a person claimed under a multiple support agreement"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_claimed, {const: true}]}
        - {op: test, eq: [dependent.divorced_rule, {const: false}]}
        - {op: test, eq: [dependent.h_household_all_year, {const: false}]}
        - {op: test, eq: [dependent.multiple_support, {const: false}]}
    note: "Exclusion (b), a dependent only because the person lived with you all of 2025, is read as the household-member path of Step 4."

  - id: dependent.h_t2_qc
    printed: "(helper)"
    label: "Test 2, item 2. Your unmarried qualifying child who isn't your dependent"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qc_raw, {const: true}]}
        - {op: test, eq: [dependent.other_claimant, {const: false}]}
        - {op: test, eq: [dependent.married, {const: false}]}
        - {op: test, eq: [dependent.h_claimed, {const: false}]}
    note: "Test 2 items 3 and 4 aren't encoded. Item 3 needs to know whether you can be claimed on someone else's return. Item 4 needs to know whether you are the custodial parent who released the claim. There are no inputs for either."

  - id: dependent.hoh_test2
    printed: "(helper)"
    label: "A Test 2 person who lived with you more than half the year (the home-cost condition of Test 2 is tested on the household form)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_lived_half, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [dependent.h_t2_dependent, {const: true}]}
            - {op: test, eq: [dependent.h_t2_qc, {const: true}]}

  - id: dependent.hoh_test1
    printed: "(helper)"
    label: "Test 1. You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent whom you can claim as a dependent, except under a multiple support agreement"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.relationship, {const: "parent"}]}
        - {op: test, eq: [dependent.h_claimed, {const: true}]}
        - {op: test, eq: [dependent.multiple_support, {const: false}]}
        - {op: test, eq: [dependent.parent_home_paid, {const: true}]}
        - {op: test, eq: [dependent.h_lived_half, {const: false}]}
    note: "As specified, Test 1 here covers only a parent who doesn't live with you, read as not living with you for more than half the year. A parent who lives with you is covered by Test 2."

  - id: dependent.eic_child
    printed: "(helper)"
    label: "Qualifying child for the EIC (relationship, age, not filing a joint return, lived with you in the United States for more than half of 2025)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.h_qc_relationship, {const: true}]}
        - {op: test, eq: [dependent.h_qc_age, {const: true}]}
        - {op: test, eq: [dependent.joint_return, {const: false}]}
        - {op: test, eq: [dependent.us_half, {const: true}]}
    note: "Following the requested definition, only the four Step 3 conditions are encoded. The 'Married child' rule and the 'Qualifying child of more than one person' tie-breaker cautions aren't applied here."

  - id: dependent.eic_ssn_child
    printed: "(helper)"
    label: "Qualifying child for the EIC who has a valid SSN"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [dependent.eic_child, {const: true}]}
        - {op: test, eq: [dependent.work_ssn, {const: true}]}
    note: "For the EIC, a valid SSN is one not limited to federally funded benefits, issued on or before the return due date. This is read as dependent.work_ssn (an SSN valid for employment issued before the due date)."
```
```
