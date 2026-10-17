# Transcription agreement — dependent

Second transcription of `Dependents — qualifying child and qualifying relative tests, per person listed` by an isolated model (spec 6.5), compared line by line with `forms/2025/dependent.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 7c0f29a5a11fad7247171a212d9b6ccf89b723cc2e78dc1c1c85965751113d87 |
| printed lines compared | 8 |
| agree / disagree / missing | 1 / 5 / 2 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19, 20, 21 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 |

## Lines

### dependent.one — One person listed
Status: **AGREE**

### dependent.ctc_child — Qualifying child for the child tax credit (Step 3)
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"input": "dependent.citizen"}, {"input": "dependent.tin"}, {"args": [{"input": "dependent.work_ssn"}, {"ref": "household.taxpayer_work_ssn"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "dependent.disabled"}, {"args": [{"input": "dependent.student"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}, {"args": [{"input": "dependent.joint_return"}], "test": "not"}, {"args": [{"input": "dependent.self_support"}], "test": "not"}], "test": "all"}, {"args": [{"input": "dependent.canada_mexico"}, {"input": "dependent.citizen"}], "test": "any"}], "test": "all"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}
```

Second transcription's note: The divorced/separated-parent rule (only the noncustodial parent claims CTC/ODC) is not in the flowchart, and the input does not say which parent you are. I do not apply it here.

Ruling: representation; project retained. The second transcription folds the qualifying-child, dependency and credit tests into each credit line and writes the complements with `not`; the project names them as helper lines and the per-person credit amounts read those helpers. Both read Steps 1 to 5 the same way: the age tests with the student and disabled branches and "younger than you", the relationship list, the support, joint-return and residency conditions, citizenship and TIN for the credits, and the filer's TIN or work SSN. The second transcription was made before BUG-0011 and BUG-0015 split the relationship values and before BUG-0012 split the head of household tests into `hoh_test1` and `hoh_test2` (the two lines it lacks); its `hoh_person` carries both tests in one line. The divorced-parent rule the second did not apply is refused by the project. No change to the data.

### dependent.odc_person — Dependent for the credit for other dependents (Steps 3 and 5)
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_tin"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"input": "dependent.citizen"}, {"input": "dependent.tin"}, {"ref": "household.taxpayer_tin"}, {"args": [{"args": [{"args": [{"input": "dependent.disabled"}, {"args": [{"input": "dependent.student"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}, {"args": [{"input": "dependent.joint_return"}], "test": "not"}, {"args": [{"input": "dependent.self_support"}], "test": "not"}], "test": "all"}, {"args": [{"input": "dependent.canada_mexico"}, {"input": "dependent.citizen"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "dependent.work_ssn"}], "test": "not"}, {"args": [{"ref": "household.taxpayer_work_ssn"}], "test": "not"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}], "test": "all"}, {"args": [{"input": "dependent.citizen"}, {"input": "dependent.tin"}, {"ref": "household.taxpayer_tin"}, {"args": [{"args": [{"args": [{"input": "dependent.divorced_rule"}, {"input": "dependent.multiple_support"}, {"input": "dependent.supported"}], "test": "any"}, {"args": [{"input": "dependent.joint_return"}, {"input": "dependent.self_support"}, {"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"input": "dependent.student"}], "test": "not"}], "test": "any"}, {"args": [{"input": "dependent.disabled"}], "test": "not"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "le"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}, {"args": [{"input": "dependent.other_claimant"}], "test": "not"}], "test": "all"}, {"args": [{"input": "dependent.canada_mexico"}, {"input": "dependent.citizen"}], "test": "any"}, {"args": [{"input": "dependent.joint_return"}], "test": "not"}], "test": "all"}], "test": "all"}], "test": "any"}
```

Ruling: representation; project retained. The second transcription folds the qualifying-child, dependency and credit tests into each credit line and writes the complements with `not`; the project names them as helper lines and the per-person credit amounts read those helpers. Both read Steps 1 to 5 the same way: the age tests with the student and disabled branches and "younger than you", the relationship list, the support, joint-return and residency conditions, citizenship and TIN for the credits, and the filer's TIN or work SSN. The second transcription was made before BUG-0011 and BUG-0015 split the relationship values and before BUG-0012 split the head of household tests into `hoh_test1` and `hoh_test2` (the two lines it lacks); its `hoh_person` carries both tests in one line. The divorced-parent rule the second did not apply is refused by the project. No change to the data.

### dependent.ctc_amount — Child tax credit amount for this person before limits ($2,200 for a qualifying child, else
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}, "then": {"param": "ctc.per_child"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"input": "dependent.citizen"}, {"input": "dependent.tin"}, {"args": [{"input": "dependent.work_ssn"}, {"ref": "household.taxpayer_work_ssn"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "dependent.disabled"}, {"args": [{"input": "dependent.student"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}, {"args": [{"input": "dependent.joint_return"}], "test": "not"}, {"args": [{"input": "dependent.self_support"}], "test": "not"}], "test": "all"}, {"args": [{"input": "dependent.canada_mexico"}, {"input": "dependent.citizen"}], "test": "any"}], "test": "all"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}, "then": {"param": "ctc.per_child"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"input": "dependent.canada_mexico"}], "test": "not"}, {"args": [{"input": "dependent.citizen"}], "test": "not"}], "test": "all"}, {"args": [{"input": "dependent.joint_return"}, {"input": "dependent.self_support"}, {"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"input": "dependent.student"}], "test": "not"}], "test": "any"}, {"args": [{"input": "dependent.disabled"}], "test": "not"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}], "test": "any"}], "test": "any"}, {"args": [{"args": [{"input": "dependent.work_ssn"}], "test": "not"}, {"args": [{"ref": "household.taxpayer_work_ssn"}], "test": "not"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"input": "dependent.citizen"}], "test": "not"}, {"args": [{"input": "dependent.tin"}], "test": "not"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; project retained. The second transcription folds the qualifying-child, dependency and credit tests into each credit line and writes the complements with `not`; the project names them as helper lines and the per-person credit amounts read those helpers. Both read Steps 1 to 5 the same way: the age tests with the student and disabled branches and "younger than you", the relationship list, the support, joint-return and residency conditions, citizenship and TIN for the credits, and the filer's TIN or work SSN. The second transcription was made before BUG-0011 and BUG-0015 split the relationship values and before BUG-0012 split the head of household tests into `hoh_test1` and `hoh_test2` (the two lines it lacks); its `hoh_person` carries both tests in one line. The divorced-parent rule the second did not apply is refused by the project. No change to the data.

### dependent.odc_amount — Credit for other dependents amount for this person before limits ($500 for an other depend
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_tin"}], "test": "eq"}], "test": "all"}, "then": {"param": "odc.per_dependent"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"param": "qr.gross_income_limit"}, {"input": "dependent.gross_income"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_tin"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"input": "dependent.work_ssn"}, {"ref": "household.taxpayer_work_ssn"}], "test": "all"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "dependent.canada_mexico"}], "test": "not"}, {"args": [{"input": "dependent.citizen"}], "test": "not"}], "test": "all"}, {"args": [{"input": "dependent.joint_return"}, {"input": "dependent.self_support"}, {"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"input": "dependent.student"}], "test": "not"}], "test": "any"}, {"args": [{"input": "dependent.disabled"}], "test": "not"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}], "test": "any"}], "test": "any"}, {"args": [{"input": "dependent.citizen"}], "test": "not"}, {"args": [{"input": "dependent.tin"}], "test": "not"}, {"args": [{"ref": "household.taxpayer_tin"}], "test": "not"}], "test": "any"}, {"args": [{"args": [{"input": "dependent.joint_return"}, {"args": [{"args": [{"input": "dependent.canada_mexico"}], "test": "not"}, {"args": [{"input": "dependent.citizen"}], "test": "not"}], "test": "all"}, {"args": [{"input": "dependent.other_claimant"}, {"args": [{"args": [{"input": "dependent.disabled"}, {"args": [{"input": "dependent.student"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}, {"args": [{"input": "dependent.joint_return"}], "test": "not"}, {"args": [{"input": "dependent.self_support"}], "test": "not"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "dependent.months"}, {"const": 12}], "test": "lt"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.divorced_rule"}], "test": "not"}, {"args": [{"input": "dependent.multiple_support"}], "test": "not"}, {"args": [{"input": "dependent.supported"}], "test": "not"}], "test": "all"}, {"args": [{"param": "qr.gross_income_limit"}, {"input": "dependent.gross_income"}], "test": "le"}], "test": "any"}], "test": "any"}, {"args": [{"input": "dependent.citizen"}], "test": "not"}, {"args": [{"input": "dependent.tin"}], "test": "not"}, {"args": [{"ref": "household.taxpayer_tin"}], "test": "not"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"input": "dependent.citizen"}, {"input": "dependent.tin"}, {"ref": "household.taxpayer_tin"}, {"args": [{"args": [{"args": [{"input": "dependent.disabled"}, {"args": [{"input": "dependent.student"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}, {"args": [{"input": "dependent.joint_return"}], "test": "not"}, {"args": [{"input": "dependent.self_support"}], "test": "not"}], "test": "all"}, {"args": [{"input": "dependent.canada_mexico"}, {"input": "dependent.citizen"}], "test": "any"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "dependent.work_ssn"}], "test": "not"}, {"args": [{"ref": "household.taxpayer_work_ssn"}], "test": "not"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}], "test": "all"}, {"args": [{"input": "dependent.citizen"}, {"input": "dependent.tin"}, {"ref": "household.taxpayer_tin"}, {"args": [{"args": [{"args": [{"input": "dependent.divorced_rule"}, {"input": "dependent.multiple_support"}, {"input": "dependent.supported"}], "test": "any"}, {"args": [{"input": "dependent.joint_return"}, {"input": "dependent.self_support"}, {"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"input": "dependent.student"}], "test": "not"}], "test": "any"}, {"args": [{"input": "dependent.disabled"}], "test": "not"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "le"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}, {"args": [{"input": "dependent.other_claimant"}], "test": "not"}], "test": "all"}, {"args": [{"input": "dependent.canada_mexico"}, {"input": "dependent.citizen"}], "test": "any"}, {"args": [{"input": "dependent.joint_return"}], "test": "not"}], "test": "all"}], "test": "all"}], "test": "any"}, "then": {"param": "odc.per_dependent"}}], "op": "choose"}
```

Ruling: representation; project retained. The second transcription folds the qualifying-child, dependency and credit tests into each credit line and writes the complements with `not`; the project names them as helper lines and the per-person credit amounts read those helpers. Both read Steps 1 to 5 the same way: the age tests with the student and disabled branches and "younger than you", the relationship list, the support, joint-return and residency conditions, citizenship and TIN for the credits, and the filer's TIN or work SSN. The second transcription was made before BUG-0011 and BUG-0015 split the relationship values and before BUG-0012 split the head of household tests into `hoh_test1` and `hoh_test2` (the two lines it lacks); its `hoh_person` carries both tests in one line. The divorced-parent rule the second did not apply is refused by the project. No change to the data.

### dependent.actc_amount — Additional child tax credit ceiling for this person ($1,700 for a qualifying child, else 0
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}, "then": {"param": "actc.per_child"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "ne"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.tin"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.work_ssn"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.taxpayer_work_ssn"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"input": "dependent.citizen"}, {"input": "dependent.tin"}, {"args": [{"input": "dependent.work_ssn"}, {"ref": "household.taxpayer_work_ssn"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "dependent.disabled"}, {"args": [{"input": "dependent.student"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}, {"args": [{"input": "dependent.joint_return"}], "test": "not"}, {"args": [{"input": "dependent.self_support"}], "test": "not"}], "test": "all"}, {"args": [{"input": "dependent.canada_mexico"}, {"input": "dependent.citizen"}], "test": "any"}], "test": "all"}, {"args": [{"input": "dependent.age"}, {"param": "ctc.age_limit"}], "test": "lt"}], "test": "all"}, "then": {"param": "actc.per_child"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"input": "dependent.canada_mexico"}], "test": "not"}, {"args": [{"input": "dependent.citizen"}], "test": "not"}], "test": "all"}, {"args": [{"input": "dependent.joint_return"}, {"input": "dependent.self_support"}, {"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"input": "dependent.student"}], "test": "not"}], "test": "any"}, {"args": [{"input": "dependent.disabled"}], "test": "not"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}], "test": "any"}], "test": "any"}, {"args": [{"args": [{"input": "dependent.work_ssn"}], "test": "not"}, {"args": [{"ref": "household.taxpayer_work_ssn"}], "test": "not"}], "test": "any"}, {"args": [{"param": "ctc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"input": "dependent.citizen"}], "test": "not"}, {"args": [{"input": "dependent.tin"}], "test": "not"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; project retained. The second transcription folds the qualifying-child, dependency and credit tests into each credit line and writes the complements with `not`; the project names them as helper lines and the per-person credit amounts read those helpers. Both read Steps 1 to 5 the same way: the age tests with the student and disabled branches and "younger than you", the relationship list, the support, joint-return and residency conditions, citizenship and TIN for the credits, and the filer's TIN or work SSN. The second transcription was made before BUG-0011 and BUG-0015 split the relationship values and before BUG-0012 split the head of household tests into `hoh_test1` and `hoh_test2` (the two lines it lacks); its `hoh_person` carries both tests in one line. The divorced-parent rule the second did not apply is refused by the project. No change to the data.

### dependent.hoh_test2 — A Test 2 person who lived with you more than half the year (the home-cost condition of Tes
Status: **MISSING**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"const": false}, {"input": "dependent.married"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}, {"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}], "test": "any"}
```

Second:

```json
None
```

Ruling: representation; project retained. The second transcription folds the qualifying-child, dependency and credit tests into each credit line and writes the complements with `not`; the project names them as helper lines and the per-person credit amounts read those helpers. Both read Steps 1 to 5 the same way: the age tests with the student and disabled branches and "younger than you", the relationship list, the support, joint-return and residency conditions, citizenship and TIN for the credits, and the filer's TIN or work SSN. The second transcription was made before BUG-0011 and BUG-0015 split the relationship values and before BUG-0012 split the head of household tests into `hoh_test1` and `hoh_test2` (the two lines it lacks); its `hoh_person` carries both tests in one line. The divorced-parent rule the second did not apply is refused by the project. No change to the data.

### dependent.hoh_test1 — Qualifies you for head of household under Test 1 (a parent whose main home you kept up)
Status: **MISSING**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 12}, {"input": "dependent.months"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"ref": "household.taxpayer_age"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}, {"args": [{"input": "dependent.age"}, {"ref": "household.taxpayer_age"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.parent_home_paid"}], "test": "eq"}], "test": "all"}
```

Second:

```json
None
```

Ruling: representation; project retained. The second transcription folds the qualifying-child, dependency and credit tests into each credit line and writes the complements with `not`; the project names them as helper lines and the per-person credit amounts read those helpers. Both read Steps 1 to 5 the same way: the age tests with the student and disabled branches and "younger than you", the relationship list, the support, joint-return and residency conditions, citizenship and TIN for the credits, and the filer's TIN or work SSN. The second transcription was made before BUG-0011 and BUG-0015 split the relationship values and before BUG-0012 split the head of household tests into `hoh_test1` and `hoh_test2` (the two lines it lacks); its `hoh_person` carries both tests in one line. The divorced-parent rule the second did not apply is refused by the project. No change to the data.

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

  - id: dependent.h_rel_child
    printed: "(helper)"
    label: "Son, daughter, stepchild, foster child, or a descendant of any of them"
    type: Bool
    expr: {op: test, eq: [dependent.relationship, {const: "child"}]}

  - id: dependent.h_rel_sibling
    printed: "(helper)"
    label: "Brother, sister, stepbrother, stepsister, half brother, half sister, or a descendant of any of them"
    type: Bool
    expr: {op: test, eq: [dependent.relationship, {const: "sibling"}]}

  - id: dependent.h_rel_parent
    printed: "(helper)"
    label: "Father, mother, or an ancestor or sibling of either of them"
    type: Bool
    expr: {op: test, eq: [dependent.relationship, {const: "parent"}]}

  - id: dependent.h_rel_in_law
    printed: "(helper)"
    label: "Stepfather, stepmother, son-in-law, daughter-in-law, father-in-law, mother-in-law, brother-in-law, or sister-in-law"
    type: Bool
    expr: {op: test, eq: [dependent.relationship, {const: "in_law"}]}

  - id: dependent.h_rel_household
    printed: "(helper)"
    label: "Any other person (other than your spouse) who is a member of your household"
    type: Bool
    expr: {op: test, eq: [dependent.relationship, {const: "household_member"}]}

  # ---------- Step 1: qualifying child ----------
  - id: dependent.h_qc_relationship
    printed: "(helper)"
    label: "A qualifying child is your son, daughter, stepchild, foster child, brother, sister, stepbrother, stepsister, half brother, half sister, or a descendant of any of them"
    type: Bool
    expr: {op: test, any: [dependent.h_rel_child, dependent.h_rel_sibling]}

  - id: dependent.h_younger
    printed: "(helper)"
    label: "Younger than you (or your spouse if filing jointly)"
    type: Bool
    expr: {op: test, lt: [dependent.age, household.taxpayer_age]}
    note: "The text also allows 'younger than your spouse if filing jointly'. No spouse age input exists. I compare against your age only."

  - id: dependent.h_under19
    printed: "(helper)"
    label: "Under age 19 at the end of 2025"
    type: Bool
    expr: {op: test, lt: [dependent.age, {param: qc.age_limit}]}

  - id: dependent.h_under24
    printed: "(helper)"
    label: "Under age 24 at the end of 2025"
    type: Bool
    expr: {op: test, lt: [dependent.age, {param: qc.student_age_limit}]}

  - id: dependent.h_age_a
    printed: "(helper)"
    label: "Under age 19 at the end of 2025 and younger than you"
    type: Bool
    expr: {op: test, all: [dependent.h_under19, dependent.h_younger]}

  - id: dependent.h_age_b
    printed: "(helper)"
    label: "Under age 24 at the end of 2025, a full-time student, and younger than you"
    type: Bool
    expr: {op: test, all: [dependent.h_under24, dependent.student, dependent.h_younger]}

  - id: dependent.h_qc_age
    printed: "(helper)"
    label: "Age test: under 19 and younger, or under 24 full-time student and younger, or any age and permanently and totally disabled"
    type: Bool
    expr: {op: test, any: [dependent.h_age_a, dependent.h_age_b, dependent.disabled]}

  - id: dependent.h_not_self_support
    printed: "(helper)"
    label: "Who didn't provide over half of their own support for 2025"
    type: Bool
    expr: {op: test, not: dependent.self_support}

  - id: dependent.h_not_joint
    printed: "(helper)"
    label: "Who isn't filing a joint return for 2025 or is filing a joint return only to claim a refund of withheld income tax or estimated tax paid"
    type: Bool
    expr: {op: test, not: dependent.joint_return}

  - id: dependent.h_lived_half
    printed: "(helper)"
    label: "Who lived with you for more than half of 2025"
    type: Bool
    expr: {op: test, gt: [dependent.months, {const: 6}]}
    note: "The test is 'more than half of 2025'. The input counts whole months, so I read it as more than 6 months. The born/died/adopted/foster exceptions are not modeled separately. I assume the months input already reflects them."

  - id: dependent.h_qualifying_child
    printed: "(helper)"
    label: "Step 1, question 1: Do you have a child who meets the conditions to be your qualifying child?"
    type: Bool
    expr: {op: test, all: [dependent.h_qc_relationship, dependent.h_qc_age, dependent.h_not_self_support, dependent.h_not_joint, dependent.h_lived_half]}
    note: "If the child is also the qualifying child of another person, the text points to tie-breaker rules that need facts about the other person. I do not apply them here, so dependent.other_claimant does not remove the child from Step 1. I use other_claimant only in the Step 4 qualifying-relative test."

  # ---------- Step 2 ----------
  - id: dependent.h_resident
    printed: "(helper)"
    label: "Was the person a U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico?"
    type: Bool
    expr: {op: test, any: [dependent.citizen, dependent.canada_mexico]}

  - id: dependent.h_qc_dependent
    printed: "(helper)"
    label: "Step 2: Qualifying child who is your dependent"
    type: Bool
    expr: {op: test, all: [dependent.h_qualifying_child, dependent.h_resident]}
    note: "Question 2 (Married person): a married person filing a joint return can't be claimed. That is already covered by h_not_joint in Step 1. Question 4 (could you be claimed as a dependent) has no input specific to this worksheet. I assume you cannot be claimed."

  # ---------- Step 3 ----------
  - id: dependent.h_under17
    printed: "(helper)"
    label: "Was the child under age 17 at the end of 2025?"
    type: Bool
    expr: {op: test, lt: [dependent.age, {param: ctc.age_limit}]}

  - id: dependent.h_ssn_pair
    printed: "(helper)"
    label: "Did you and this child have SSNs valid for employment and issued before the due date of your 2025 return (including extensions)?"
    type: Bool
    expr: {op: test, all: [household.taxpayer_work_ssn, dependent.work_ssn]}
    note: "The spouse alternative for joint filers is not modeled. Only your own valid SSN is tested."

  - id: dependent.ctc_child
    printed: "(helper)"
    label: "Qualifying child for the child tax credit (Step 3)"
    type: Bool
    expr: {op: test, all: [dependent.h_qc_dependent, dependent.tin, dependent.citizen, dependent.h_under17, dependent.h_ssn_pair]}
    note: "The divorced/separated-parent rule (only the noncustodial parent claims CTC/ODC) is not in the flowchart, and the input does not say which parent you are. I do not apply it here."

  - id: dependent.h_not_under17
    printed: "(helper)"
    label: "Child not under age 17 at the end of 2025"
    type: Bool
    expr: {op: test, not: dependent.h_under17}

  - id: dependent.h_not_ssn_pair
    printed: "(helper)"
    label: "You or the child lacked an SSN valid for employment (go to Step 5)"
    type: Bool
    expr: {op: test, not: dependent.h_ssn_pair}

  - id: dependent.h_qc_odc_route
    printed: "(helper)"
    label: "Step 3 question 3 No, or question 4 No"
    type: Bool
    expr: {op: test, any: [dependent.h_not_under17, dependent.h_not_ssn_pair]}

  - id: dependent.h_qc_odc
    printed: "(helper)"
    label: "Qualifying child for whom you can claim the credit for other dependents"
    type: Bool
    expr: {op: test, all: [dependent.h_qc_dependent, dependent.tin, dependent.citizen, dependent.h_qc_odc_route, household.taxpayer_tin]}
    note: "The 'Before you begin' text says that to claim ODC you must have an SSN or ITIN. I apply that requirement on both routes: the Step 3 age-17 route and the Step 5 route."

  # ---------- Step 4: qualifying relative ----------
  - id: dependent.h_all_year
    printed: "(helper)"
    label: "Lived with you all year"
    type: Bool
    expr: {op: test, ge: [dependent.months, {const: 12}]}

  - id: dependent.h_household_all_year
    printed: "(helper)"
    label: "Any other person who lived with you all year as a member of your household"
    type: Bool
    expr: {op: test, all: [dependent.h_rel_household, dependent.h_all_year]}
    note: "The condition 'relationship didn't violate local law' has no input. I assume it is met."

  - id: dependent.h_qr_relationship
    printed: "(helper)"
    label: "A qualifying relative is your child/descendant, sibling/their child, parent/ancestor or their sibling, step/in-law relative, or a household member all year"
    type: Bool
    expr: {op: test, any: [dependent.h_rel_child, dependent.h_rel_sibling, dependent.h_rel_parent, dependent.h_rel_in_law, dependent.h_household_all_year]}
    note: "The enum lumps stepbrother and stepsister with siblings or in-laws. Both categories qualify for Step 4, so the result is the same."

  - id: dependent.h_not_qc
    printed: "(helper)"
    label: "Not your qualifying child (Step 1 No)"
    type: Bool
    expr: {op: test, not: dependent.h_qualifying_child}

  - id: dependent.h_not_other_qc
    printed: "(helper)"
    label: "Who wasn't a qualifying child of any other taxpayer for 2025"
    type: Bool
    expr: {op: test, not: dependent.other_claimant}

  - id: dependent.h_qr_income
    printed: "(helper)"
    label: "Who had gross income of less than $5,200 in 2025"
    type: Bool
    expr: {op: test, lt: [dependent.gross_income, {param: qr.gross_income_limit}]}
    note: "Under the exception to the gross income test, sheltered-workshop income may be excluded (details in Pub. 501). I assume the gross_income input already reflects any such exclusion."

  - id: dependent.h_qr_support
    printed: "(helper)"
    label: "For whom you provided over half of the person's support (see divorced or separated parents and multiple support agreements)"
    type: Bool
    expr: {op: test, any: [dependent.supported, dependent.multiple_support, dependent.divorced_rule]}
    note: "The support test can also be met through a multiple support agreement, or through the divorced/separated parent rule (child treated as the noncustodial parent's qualifying relative). I read divorced_rule as true when you are the parent the rule favours."

  - id: dependent.h_qualifying_relative
    printed: "(helper)"
    label: "Step 4, question 1: Does any person meet the conditions to be your qualifying relative?"
    type: Bool
    expr: {op: test, all: [dependent.h_qr_relationship, dependent.h_not_qc, dependent.h_not_other_qc, dependent.h_qr_income, dependent.h_qr_support]}

  - id: dependent.h_qr_dependent
    printed: "(helper)"
    label: "Step 4: Qualifying relative who is your dependent"
    type: Bool
    expr: {op: test, all: [dependent.h_qualifying_relative, dependent.h_resident, dependent.h_not_joint]}
    note: "Question 3 (Married person): a married person filing a joint return, other than only to claim a refund, can't be claimed. Question 5 is assumed No, as in Step 2."

  - id: dependent.h_claimed
    printed: "(helper)"
    label: "Your dependent"
    type: Bool
    expr: {op: test, any: [dependent.h_qc_dependent, dependent.h_qr_dependent]}

  # ---------- Step 5 ----------
  - id: dependent.h_qr_odc
    printed: "(helper)"
    label: "Step 5: Qualifying relative for whom you can claim the credit for other dependents"
    type: Bool
    expr: {op: test, all: [dependent.h_qr_dependent, household.taxpayer_tin, dependent.tin, dependent.citizen]}

  - id: dependent.odc_person
    printed: "(helper)"
    label: "Dependent for the credit for other dependents (Steps 3 and 5)"
    type: Bool
    expr: {op: test, any: [dependent.h_qc_odc, dependent.h_qr_odc]}

  # ---------- Amounts ----------
  - id: dependent.h_ctc_per_child
    printed: "(helper)"
    label: "Multiply line 4 by $2,200 (per child)"
    type: NonNegDollars
    expr: {op: param, ref: ctc.per_child}

  - id: dependent.h_is_ctc
    printed: "(helper)"
    label: "Is a qualifying child for the child tax credit"
    type: Bool
    expr: {op: test, eq: [dependent.ctc_child, {const: true}]}

  - id: dependent.h_not_ctc
    printed: "(helper)"
    label: "Is not a qualifying child for the child tax credit"
    type: Bool
    expr: {op: test, not: dependent.ctc_child}

  - id: dependent.ctc_amount
    printed: "(helper)"
    label: "Child tax credit amount for this person before limits ($2,200 for a qualifying child, else 0)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: dependent.h_is_ctc, then: dependent.h_ctc_per_child}
        - {guard: dependent.h_not_ctc, then: dependent.h_zero}

  - id: dependent.h_odc_per_dependent
    printed: "(helper)"
    label: "Multiply line 6 by $500 (per dependent)"
    type: NonNegDollars
    expr: {op: param, ref: odc.per_dependent}

  - id: dependent.h_is_odc
    printed: "(helper)"
    label: "Is a dependent for the credit for other dependents"
    type: Bool
    expr: {op: test, eq: [dependent.odc_person, {const: true}]}

  - id: dependent.h_not_odc
    printed: "(helper)"
    label: "Is not a dependent for the credit for other dependents"
    type: Bool
    expr: {op: test, not: dependent.odc_person}

  - id: dependent.odc_amount
    printed: "(helper)"
    label: "Credit for other dependents amount for this person before limits ($500 for an other dependent, else 0)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: dependent.h_is_odc, then: dependent.h_odc_per_dependent}
        - {guard: dependent.h_not_odc, then: dependent.h_zero}

  - id: dependent.h_actc_per_child
    printed: "(helper)"
    label: "Number of qualifying children under age 17 with the required SSN x $1,700 (per child)"
    type: NonNegDollars
    expr: {op: param, ref: actc.per_child}

  - id: dependent.actc_amount
    printed: "(helper)"
    label: "Additional child tax credit ceiling for this person ($1,700 for a qualifying child, else 0)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: dependent.h_is_ctc, then: dependent.h_actc_per_child}
        - {guard: dependent.h_not_ctc, then: dependent.h_zero}

  # ---------- Head of household ----------
  - id: dependent.h_not_multiple
    printed: "(helper)"
    label: "Not claimed under a multiple support agreement"
    type: Bool
    expr: {op: test, not: dependent.multiple_support}

  - id: dependent.h_hoh_test1
    printed: "(helper)"
    label: "Test 1. You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent whom you can claim as a dependent, except under a multiple support agreement"
    type: Bool
    expr: {op: test, all: [dependent.h_rel_parent, dependent.h_qr_dependent, dependent.h_not_multiple, dependent.parent_home_paid]}
    note: "Test 1 says 'your parent', but the 'parent' enum also covers ancestors and siblings of a parent. I treat the whole enum value as a parent for Test 1."

  - id: dependent.h_not_divorced
    printed: "(helper)"
    label: "Not claimed as your dependent because of the rule for children of divorced or separated parents"
    type: Bool
    expr: {op: test, not: dependent.divorced_rule}

  - id: dependent.h_not_household_only
    printed: "(helper)"
    label: "Not your dependent only because the person lived with you for all of 2025"
    type: Bool
    expr: {op: test, not: dependent.h_rel_household}

  - id: dependent.h_hoh_dep
    printed: "(helper)"
    label: "Test 2, item 1: Any person whom you can claim as a dependent, excluding exceptions a, b and c"
    type: Bool
    expr: {op: test, all: [dependent.h_claimed, dependent.h_not_divorced, dependent.h_not_household_only, dependent.h_not_multiple]}

  - id: dependent.h_not_married
    printed: "(helper)"
    label: "Unmarried"
    type: Bool
    expr: {op: test, not: dependent.married}

  - id: dependent.h_not_claimed
    printed: "(helper)"
    label: "Isn't your dependent"
    type: Bool
    expr: {op: test, not: dependent.h_claimed}

  - id: dependent.h_hoh_qc_nondep
    printed: "(helper)"
    label: "Test 2, item 2: Your unmarried qualifying child who isn't your dependent"
    type: Bool
    expr: {op: test, all: [dependent.h_qualifying_child, dependent.h_not_married, dependent.h_not_claimed]}
    note: "Item 3 depends on you being claimable as a dependent, which this worksheet assumes is false. Item 4 needs to know you are the custodial parent, and no input says so. Both are omitted."

  - id: dependent.h_hoh_person_type
    printed: "(helper)"
    label: "Test 2: a person listed in items 1 through 4"
    type: Bool
    expr: {op: test, any: [dependent.h_hoh_dep, dependent.h_hoh_qc_nondep]}

  - id: dependent.h_hoh_test2
    printed: "(helper)"
    label: "Test 2. You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year"
    type: Bool
    expr: {op: test, all: [household.home_cost, dependent.h_lived_half, dependent.h_hoh_person_type]}

  - id: dependent.hoh_person
    printed: "(helper)"
    label: "Qualifies you for head of household (Test 1 or Test 2)"
    type: Bool
    expr: {op: test, any: [dependent.h_hoh_test1, dependent.h_hoh_test2]}
```
```
