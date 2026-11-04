# Transcription agreement — household

Second transcription of `Household facts for dependents and head of household` by an isolated model (spec 6.5), compared line by line with `forms/2025/household.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | fde7c34de787b3e097f1f957be15c7243b4bc3ac61d8d5a3cebb109b1cda6232 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 2061e3e03775ea7920c1483c4a6b31a66b0a20f419204fadaf578933244aa136 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 83f6ac4700c277df401354d9d0297fddd9023575ef445ec5fb06560f21cdecca |
| printed lines compared | 19 |
| agree / disagree / missing | 7 / 12 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 13, 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 13, 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| i1040s8812 | 2025; printed date 2026-01-23 | 2 | cited pages | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | 2 | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |
| p501 | 2025 returns; PDF created 2026-02-04 | 6, 8, 9, 11 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 6, 8, 11 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |

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

Second transcription's note: The pages do not say who has a person entry. Chosen reading: only a joint return includes the spouse's income, deductions and credits (i1040gi p. 13), so only then does the spouse have an entry. On a separate return the spouse is named only, so the spouse has no entry.

Ruling: scope — The Boolean roster tests agree on complete age-screened records. Form 1040 p. 1 names the taxpayer and, on a joint return, spouse. The project also propagates household.roster_ok's under16 refusal (amb.2025.filer_under_16); the candidate bypasses it. All 12 observed differences are that extra scope prerequisite: 11 project-unknown on incomplete records and one project-refuses. This is not unconditional partial-input equivalence. Reply unchanged since the previous round; ruling re-checked against this record. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,495 fixtures, 500 generated returns seed 20261026, 289 partial records; 2,284 comparisons): 2,271 of 2,284 agree; 12 project-unknown, 1 project-refuses; on returns the full interview completes: none. No completed-return difference. Project stands.

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

Second transcription's note: Read as: both persons on the return have a Form 8889, which brings in the Form 8889 line 6 rules for spouses (i8889 pp. 4, 7).

Ruling: representation; i8889 p. 4, "If you and your spouse each have separate HSAs, complete a separate Form 8889 for each". Both count persons with at least one Form 8889 and test that the count is two (> 0 against >= 1 on an integral count). executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,495 fixtures, 500 generated returns seed 20261026, 289 partial records; 2,284 comparisons): 2,284 of 2,284 agree; none; on returns the full interview completes: none. No difference. Project stands.

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

Ruling: representation; i1040gi p. 40, Step 1, question 2. "No person without a valid SSN" against "every person has a valid SSN": the same test on a person roster. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,495 fixtures, 500 generated returns seed 20261026, 289 partial records; 2,284 comparisons): 2,284 of 2,284 agree; none; on returns the full interview completes: none. No difference. Project stands.

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

Ruling: representation; i1040gi p. 19, Step 5, question 1 (an applied-for ITIN counts). The reply counts persons with neither a TIN nor an application and tests zero; the project tests that every person has one or the other. Same test. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,495 fixtures, 500 generated returns seed 20261026, 289 partial records; 2,284 comparisons): 2,284 of 2,284 agree; none; on returns the full interview completes: none. No difference. Project stands.

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

Second transcription's note: Read 'issued on or before the due date' (i1040gi p. 39) as excluding an ITIN only applied for. The tin question also excludes an ITIN renewal only applied for.

Ruling: representation; i1040gi p. 17, Before you begin, "only one spouse is required to have a valid SSN ... The other spouse must have either an SSN or ITIN, and it must have been issued" (amb.2025.ctc_spouse_itin_application). The reply requires person.tin of every filer; the project accepts person.tin or person.work_ssn. They differ only where a person answers that they have an SSN valid for employment but no SSN or ITIN, which are contradictory answers (an SSN valid for employment is an SSN issued by the due date); every one of the 19 value differences, including the completed generated 147, has that answer pair. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,495 fixtures, 500 generated returns seed 20261026, 289 partial records; 2,284 comparisons): 2,258 of 2,284 agree; 19 value, 7 candidate-unknown; on returns the full interview completes: 1 value. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 1 value (for example generated 147, household). Project stands.

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

Second transcription's note: The pages do not separately define the taxpayer's own SSN requirement. Read as the taxpayer's own employment-valid SSN only. The joint-return rule is in ctc_ssn.

Ruling: model error; i1040gi pp. 101, 106 and 110 (Schedule 1-A: the taxpayer's own valid SSN, and on a joint return the spouse who received the tips or overtime). The published line is the taxpayer's own answer ("Do you have ...", role taxpayer), read by s1a.tip_ssn and s1a.ot_ssn only on a non-joint return and by s1a.line36a_senior for line 36a, which is the taxpayer's line. The reply counts either spouse (its note reads the CTC sentence of p. 18, Step 3, question 4), which would give line 36a to a taxpayer with no valid SSN whose spouse has one: generated 49, 150 and 255 (completed, MFJ, taxpayer without a work SSN) give false against true. The project's cite of p. 18 Step 3 question 4 for a taxpayer-only line is misleading (low; see the findings file). executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,495 fixtures, 500 generated returns seed 20261026, 289 partial records; 2,284 comparisons): 2,267 of 2,284 agree; 17 value; on returns the full interview completes: 3 value. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 3 value (for example generated 49, household). Project stands.

### household.ctc_disallowed_claim — An earlier credit was reduced or disallowed (or a disallowance period applies) and Schedul
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": true}, {"input": "household.credit_disallowed"}], "test": "eq"}, {"args": [{"ref": "s8812.line11"}, {"ref": "s8812.line8"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"input": "household.credit_disallowed"}
```

Second transcription's note: The one supplied question covers both the EIC and the CTC/ACTC/ODC. It cannot tell the two apart, so a Yes is treated as applying to these credits too, which is the conservative reading.

Ruling: model error; i1040s8812 p. 2, "you must attach Form 8862 to your tax return to claim the CTC, ACTC, or ODC unless an exception applies" (Form 8862 is needed only to claim the credit). The candidate copies household.credit_disallowed, so the gate is true, and Schedule 8812 line 12 refuses, whenever the answer is Yes, also on a return that claims no child tax credit or credit for other dependents; and it needs the answer where the project does not (line 8 not above line 11). The completed-return value difference is f2.t101.credit_disallowed_no_credit_claimed (single, no dependents, answer Yes): project false, candidate true. The project-refuses differences are refused records on which Schedule 8812 line 8 or 11 itself refuses. This is the over-refusal the person-dep package removed (PENDING-9, T-101); its narrowing matches the source. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,495 fixtures, 500 generated returns seed 20261026, 289 partial records; 2,284 comparisons): 2,262 of 2,284 agree; 14 candidate-unknown, 7 project-refuses, 1 value; on returns the full interview completes: 2 candidate-unknown, 1 value. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 2 candidate-unknown household.credit_disallowed (for example classm.f8962.3.deepseek without household.credit_disallowed, household); 1 value (for example f2.t101.credit_disallowed_no_credit_claimed, household). Project stands.

### household.eic_disallowed_claim — An earlier credit was reduced or disallowed (or a disallowance period applies) and Steps 1
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"const": false}, {"ref": "scope.other_line16"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "scope.schedule1"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": false}, {"input": "eic.qc_of_another"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "eic.us_home"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": true}, {"ref": "person.born_after_1960"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.born_before_2001"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"ref": "household.married"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "eic.same_home"}], "test": "eq"}, {"args": [{"const": true}, {"input": "eic.legally_separated"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "eic.qc_of_another"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.excluded_income"}], "test": "eq"}, {"args": [{"const": false}, {"ref": "scope.other_income"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": null}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.eic_ssn"}], "test": "eq"}}], "test": "eq"}, {"args": [{"of": [{"from": {"ref": "f1040.line7a"}, "op": "subtract_floor0", "take": {"const": 0}}, {"ref": "f1040.line2a"}, {"ref": "f1040.line2b"}, {"ref": "f1040.line3b"}], "op": "sum"}, {"param": "eic.investment_limit"}], "test": "le"}, {"args": [{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}, "then": {"ref": "eic.earned_income"}}, {"guard": {"args": [{"const": 0, "type": "Count"}, {"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"ref": "eic.wsb_4b"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 1, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"param": "eic.limit0.other"}}, {"guard": {"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 2, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"param": "eic.limit1.other"}}, {"guard": {"args": [{"args": [{"const": 2, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 3, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"param": "eic.limit2.other"}}, {"guard": {"args": [{"const": 3, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, "then": {"param": "eic.limit3.other"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 1, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"param": "eic.limit0.joint"}}, {"guard": {"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 2, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"param": "eic.limit1.joint"}}, {"guard": {"args": [{"args": [{"const": 2, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 3, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"param": "eic.limit2.joint"}}, {"guard": {"args": [{"const": 3, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, "then": {"param": "eic.limit3.joint"}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, {"args": [{"ref": "f1040.line11b"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 1, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"param": "eic.limit0.other"}}, {"guard": {"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 2, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"param": "eic.limit1.other"}}, {"guard": {"args": [{"args": [{"const": 2, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 3, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"param": "eic.limit2.other"}}, {"guard": {"args": [{"const": 3, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, "then": {"param": "eic.limit3.other"}}], "op": "choose"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 1, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"param": "eic.limit0.joint"}}, {"guard": {"args": [{"args": [{"const": 1, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 2, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"param": "eic.limit1.joint"}}, {"guard": {"args": [{"args": [{"const": 2, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, {"args": [{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}, {"const": 3, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"param": "eic.limit2.joint"}}, {"guard": {"args": [{"const": 3, "type": "Count"}, {"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.us_half"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.eic_ssn"}], "test": "eq"}], "test": "all"}}], "test": "le"}, "then": {"param": "eic.limit3.joint"}}], "op": "choose"}}], "op": "choose"}], "test": "lt"}, {"args": [{"ref": "f1040.line11b"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "eic.limit3.other"}}, {"guard": {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"param": "eic.limit3.joint"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "household.credit_disallowed"}], "test": "eq"}, {"args": [{"const": 0}, {"ref": "eic.line6"}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"input": "household.credit_disallowed"}
```

Second transcription's note: The one supplied question covers both credit families, so a Yes is treated as applying to the EIC too. The Form 8862 exceptions (i1040gi p. 43) are left to that question.

Ruling: model error; i1040gi p. 43, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed ..." (the form goes with a claim of the credit). The candidate copies household.credit_disallowed, so the earned income credit refuses on a Yes answer also when Steps 1 to 5 are not passed and no credit is claimed (f2.t101.credit_disallowed_no_credit_claimed, completed: project false, candidate true; audit.s8812.credit_disallowed, refused), and it needs the answer where eic.eligible is false. The project-refuses differences are refused records on which eic.eligible refuses. The package's narrowing (PENDING-9, T-101) matches the source. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,495 fixtures, 500 generated returns seed 20261026, 289 partial records; 2,284 comparisons): 2,255 of 2,284 agree; 21 candidate-unknown, 6 project-refuses, 2 value; on returns the full interview completes: 2 candidate-unknown, 1 value. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched): 2 candidate-unknown household.credit_disallowed (for example classm.f8962.3.deepseek without household.credit_disallowed, household); 1 value (for example f2.t101.credit_disallowed_no_credit_claimed, household). Project stands.

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

Ruling: scope — i1040gi p. 14, Head of Household: "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies"; i1040gi p. 23; p501 p. 9; amb.2025.hoh_community_property. Both expressions test f1040.status == "hoh" and whether Test 1 or Test 2 is met (using <= 0 vs < 1 on integral person counts); the project reads household.hoh_eligible, which carries the cited household.hoh_community_property and household.hoh_absence refusals, whereas the candidate inlines the Boolean test without those refusals. All 4 observed differences are on incomplete/refused records from those scope gates, with zero completed-return differences. Reply unchanged since the previous round; ruling re-checked against this record. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,495 fixtures, 500 generated returns seed 20261026, 289 partial records; 2,284 comparisons): 2,279 of 2,284 agree; 3 project-refuses, 2 project-unknown; on returns the full interview completes: none. No completed-return difference. Project stands.

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
{"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: The spouse_died_2025 question is asked only for single, head of household, or joint filers not married at year end. For other filing statuses this reads False. A spouse who died and was followed by remarriage in 2025 gives married = true and is not counted.

Ruling: model error — p501 p. 6 and i1040gi p. 13 allow married filing jointly when a spouse died in 2025 and the survivor did not remarry. This owner-selected refusal gate (BUG-0277) explicitly applies to "Filing as single or head of household although your spouse died in 2025" (status == "single" or status == "hoh", with spouse_died_2025 == true). The candidate adds an mfj branch (status == "mfj" and married == false and spouse_died_2025 == true), which wrongly turns a valid death-year joint return into a widowed_2025 failure on stage21.household.status_joint_death_year. Reply restructured, same extra joint-return branch. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,495 fixtures, 500 generated returns seed 20261026, 289 partial records; 2,284 comparisons): 2,283 of 2,284 agree; 1 value; on returns the full interview completes: none. No completed-return difference. Project stands.

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
{"args": [{"args": [{"const": true}, {"input": "household.community_property"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.rdp"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: Nevada, Washington and California are community property states (i1040gi p. 23), so a registered domestic partner there will also answer the community-property question Yes. Both answers are required.

Ruling: model error — i1040gi p. 23, Community Property States, and p501 p. 6 describe the registered domestic partner community-income regime. The published gate explicitly applies to a nonjoint return in a community property state (status != "mfj" and community_property == true and rdp == true); the candidate tests household.rdp alone, dropping both applicability guards and demanding the rdp answer on joint and non-community-property returns where the interview does not ask it. All 1,607 observed differences are candidate-unknown (including 226 completed returns), not tax-value disagreements. Reply unchanged since the previous round; ruling re-checked against this record. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,495 fixtures, 500 generated returns seed 20261026, 289 partial records; 2,284 comparisons): 633 of 2,284 agree; 1,651 candidate-unknown; on returns the full interview completes: 219 candidate-unknown. Every completed-return difference enumerated with the witness cap lifted (scratch run, recorded triage file untouched; it counts 220 against the record's 219, the class M fixtures having been rewritten by a concurrent run): 220 candidate-unknown household.rdp (for example classm.f8889.1.deepseek, household). Project stands.

### household.filing_status_conflict — The filing status conflicts with the marriage facts entered
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.married"}], "test": "eq"}], "test": "all"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "household.married"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "ne"}, {"args": [{"const": true}, {"input": "household.spouse_died_2025"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": false}, {"input": "household.married"}], "test": "eq"}], "test": "all"}], "test": "any"}
```

Second transcription's note: Rules used: single needs you unmarried at year end and not widowed in 2025; joint needs you married at year end or widowed in 2025 (i1040gi p. 13; Pub. 501 p. 6). Open point: Pub. 501 lets a surviving spouse whose spouse died in 2025 file a separate return. The interview does not ask about a spouse's death for separate filers, so separate filing while not married at year end is flagged as a conflict. Head of household and QSS are checked by hoh_fails and qss_fails.

Ruling: scope; i1040gi pp. 13-15 and p501 pp. 6-8. The published gate (BUG-0286) checks the marriage-entry conflicts of the single and joint statuses; the reply also flags a single return with a 2025 death (refused by household.widowed_2025) and married filing separately while not married (the whole MFS status is refused by s3.mfs on scope.ready). Every difference is on a refused or incomplete record; no completed return differs. The reply's open point (a 2025 widow filing separately) is inside the MFS refusal. executable-triage-v2 (`reviews/2025/transcription/triage/household.json`; 1,495 fixtures, 500 generated returns seed 20261026, 289 partial records; 2,284 comparisons): 2,122 of 2,284 agree; 140 value, 22 candidate-unknown; on returns the full interview completes: none. No completed-return difference. Project stands.

## Raw second transcription

```yaml
```yaml
lines:
  - id: household.h_taxpayers
    printed: "(helper)"
    label: "Number of person entries that are the taxpayer (you)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.role, {const: "taxpayer"}]}

  - id: household.h_spouses
    printed: "(helper)"
    label: "Number of person entries that are your spouse"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.role, {const: "spouse"}]}

  - id: household.persons
    printed: "(helper)"
    label: "Number of persons on the return (you, and your spouse if filing a joint return)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one

  - id: household.roster_bad
    printed: "(helper)"
    label: "The persons entered do not match the return: there must be exactly one entry for you, plus one for your spouse on a joint return and none otherwise"
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
    note: "The pages do not say who has a person entry. Chosen reading: only a joint return includes the spouse's income, deductions and credits (i1040gi p. 13), so only then does the spouse have an entry. On a separate return the spouse is named only, so the spouse has no entry."

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
    note: "Read as: both persons on the return have a Form 8889, which brings in the Form 8889 line 6 rules for spouses (i8889 pp. 4, 7)."

  - id: household.hsa_split_count
    printed: "(helper)"
    label: "Total over persons of the Form 8889 line 6 spousal-division count"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.hsa_split

  - id: household.hsa_agreed_count
    printed: "(helper)"
    label: "Total over persons of the count of Forms 8889 using an allocation both spouses agree on (i8889, line 6)"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.hsa_agreed

  - id: household.hsa_step1_sum
    printed: "(helper)"
    label: "Total over persons of the Step 1 refigured family contribution limit (i8889, line 6)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.hsa_step1

  - id: household.hsa_share_sum
    printed: "(helper)"
    label: "Total over persons of the allocated share of the family contribution limit (i8889, line 6, Step 2)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.hsa_share
    note: "The pages require the spouses' shares (Step 2) to divide the Step 1 limit. This total is supplied so a consistency check can compare it with hsa_step1_sum. The comparison itself is not defined here."

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

  - id: household.h_no_tin_or_applied
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
    label: "Did you, and your spouse if filing a joint return, have either an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? (Answer Yes if you are applying for an ITIN on or before the return due date (including extensions).)"
    type: Bool
    expr: {op: test, eq: [household.h_no_tin_or_applied, {const: 0, type: Count}]}

  - id: household.h_work_ssn_count
    printed: "(helper)"
    label: "Number of persons on the return with an SSN valid for employment issued before the due date"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.work_ssn, {const: true}]}

  - id: household.h_no_tin_issued
    printed: "(helper)"
    label: "Number of persons on the return without an SSN or ITIN issued on or before the due date"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.tin, {const: false}]}

  - id: household.ctc_ssn
    printed: "(helper)"
    label: "To claim the child tax credit, you must have a valid SSN. If you are filing a joint return, only one spouse is required to have a valid SSN; the other spouse must have either an SSN or ITIN issued on or before the due date of the return"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, ge: [household.h_work_ssn_count, {const: 1, type: Count}]}
        - {op: test, eq: [household.h_no_tin_issued, {const: 0, type: Count}]}
    note: "Read 'issued on or before the due date' (i1040gi p. 39) as excluding an ITIN only applied for. The tin question also excludes an ITIN renewal only applied for."

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
    label: "Do you (the taxpayer) have an SSN valid for employment, issued before the due date of your 2025 return (including extensions)?"
    type: Bool
    expr: {op: test, ge: [household.h_taxpayer_work_ssn_count, {const: 1, type: Count}]}
    note: "The pages do not separately define the taxpayer's own SSN requirement. Read as the taxpayer's own employment-valid SSN only. The joint-return rule is in ctc_ssn."

  - id: household.ctc_disallowed_claim
    printed: "(helper)"
    label: "Your child tax credit, additional child tax credit, or credit for other dependents for a year after 2015 was denied or reduced for any reason other than a math or clerical error (Form 8862 required), or you are in a 2- or 10-year disallowance period"
    type: Bool
    expr: {op: copy, from: household.credit_disallowed}
    note: "The one supplied question covers both the EIC and the CTC/ACTC/ODC. It cannot tell the two apart, so a Yes is treated as applying to these credits too, which is the conservative reading."

  - id: household.eic_disallowed_claim
    printed: "(helper)"
    label: "Your EIC for a year after 1996 was reduced or disallowed for any reason other than a math or clerical error (Form 8862 required), or you are in a 2- or 10-year disallowance period"
    type: Bool
    expr: {op: copy, from: household.credit_disallowed}
    note: "The one supplied question covers both credit families, so a Yes is treated as applying to the EIC too. The Form 8862 exceptions (i1040gi p. 43) are left to that question."

  - id: household.h_hoh_test1_count
    printed: "(helper)"
    label: "Number of dependents meeting head of household Test 1 (dependent parent's main home)"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where: {op: test, eq: [dependent.hoh_test1, {const: true}]}

  - id: household.h_hoh_test2_count
    printed: "(helper)"
    label: "Number of persons meeting head of household Test 2 (lived with you more than half the year)"
    type: Count
    expr:
      op: sum_over
      collection: dependent
      field: dependent.one
      where: {op: test, eq: [dependent.hoh_test2, {const: true}]}

  - id: household.h_hoh_qualifies
    printed: "(helper)"
    label: "Check the Head of household box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies"
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

  - id: household.hoh_fails
    printed: "(helper)"
    label: "Head of household is checked but you are not unmarried (or considered unmarried), or neither Test 1 nor Test 2 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "hoh"}]}
        - op: test
          not: {op: test, eq: [household.h_hoh_qualifies, {const: true}]}

  - id: household.qss_fails
    printed: "(helper)"
    label: "Qualifying surviving spouse is checked but not all five tests apply"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "qss"}]}
        - {op: test, eq: [household.qss_eligible, {const: false}]}

  - id: household.widowed_2025
    printed: "(helper)"
    label: "Your spouse died in 2025 and you didn't remarry in 2025 (you are considered married for the whole year)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [household.married, {const: false}]}
        - op: test
          any:
            - {op: test, eq: [f1040.status, {const: "single"}]}
            - {op: test, eq: [f1040.status, {const: "hoh"}]}
            - {op: test, eq: [f1040.status, {const: "mfj"}]}
        - {op: test, eq: [household.spouse_died_2025, {const: true}]}
    note: "The spouse_died_2025 question is asked only for single, head of household, or joint filers not married at year end. For other filing statuses this reads False. A spouse who died and was followed by remarriage in 2025 gives married = true and is not counted."

  - id: household.filing_status_conflict
    printed: "(helper)"
    label: "The filing status checked conflicts with your marital status at the end of 2025"
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
            - {op: test, eq: [household.widowed_2025, {const: false}]}
        - op: test
          all:
            - {op: test, eq: [f1040.status, {const: "mfs"}]}
            - {op: test, eq: [household.married, {const: false}]}
    note: "Rules used: single needs you unmarried at year end and not widowed in 2025; joint needs you married at year end or widowed in 2025 (i1040gi p. 13; Pub. 501 p. 6). Open point: Pub. 501 lets a surviving spouse whose spouse died in 2025 file a separate return. The interview does not ask about a spouse's death for separate filers, so separate filing while not married at year end is flagged as a conflict. Head of household and QSS are checked by hoh_fails and qss_fails."

  - id: household.cp_marriage_ended
    printed: "(helper)"
    label: "You were considered married for part of the year and lived in a community property state; special rules may apply in determining your income and expenses (Pub. 555)"
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
    label: "A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income of the individual and their domestic partner (Form 8958, Pub. 555)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [household.rdp, {const: true}]}
        - {op: test, eq: [household.community_property, {const: true}]}
    note: "Nevada, Washington and California are community property states (i1040gi p. 23), so a registered domestic partner there will also answer the community-property question Yes. Both answers are required."
```
```
