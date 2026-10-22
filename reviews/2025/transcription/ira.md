# Transcription agreement — ira

Second transcription of `IRA Deduction Worksheet — Schedule 1, Line 20` by an isolated model (spec 6.5), compared line by line with `forms/2025/ira.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | fecb2cf77aec6c7d61d5e9eedc61e931c75c40c6727241ccc0a0e27490fffcba |
| subject sha256 | 891691f523440b7cc1488f02ce1a16245da1fb869f4923a2fe99e976ec275ae3 |
| printed lines compared | 22 |
| agree / disagree / missing | 6 / 16 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 95, 96, 97, 98 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31, 95, 96, 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8606 | 2025 | 5 | cited pages | 242e712835ef634f3af8f1d0f19435b236e9c54b80921d6017c153b3e6c2aec6 | 5 | 805e59f2458d33a3fc0a1d17ebede2ecd59e18d911069bbe84987e53e297ec79 |
| p590a | 2025 | 6, 16, 35 | cited pages | be942a345a01a8f875a2a625b400d7760221e1a55a2c85dca5ab75826e6c801a | 6, 35 | cbe3b3b920a64ff514424a52a467ab8efabacfe958197d1ca8aabaee71ca5a3b |
| f8606 | 2025 | 1, 2 | whole document | 1e2747fd38afcfefc11564f9673556808470614c153f2d34458afe98a560cb2c | - | 47a023b69eb81610f8bf73059c609131854d900f1694660f8496a7791f974233 |

## Lines

### ira.joint — Married filing jointly
Status: **AGREE**

### ira.joint_type — Married filing jointly or qualifying surviving spouse
Status: **AGREE**

### ira.anyone_covered — You (or, on a joint return, your spouse) were covered by a retirement plan (Yes on line 1a
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}
```

Ruling: representation; project retained. Both test whether you or, on a joint return, your spouse was covered (lines 1a and 1b, each person's person.ira_cov). The second's lines 1a and 1b also require a traditional IRA contribution, which the project tests beside this helper wherever it is read (ira.lines2to6, ira.cov_gate, ira.excl_gate; person.ira_line7 reaches a value only through ira.line7a and person.ira_deduction, both zero without contributions), so no value differs. i1040gi p. 97, IRA Deduction Worksheet, "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6". The second's ira.special stop is the project's ira.special_gate, which refuses person.ira_line11 and so lines 12 and 20.

### ira.line20 — The total of lines 12a and 12b for Schedule 1, line 20
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_deduction", "op": "sum_over", "where": null}
```

Second:

```json
{"of": [{"line": "12a"}, {"line": "12b"}], "op": "sum"}
```

Second transcription's note: The worksheet lets you deduct a smaller amount and treat the rest as nondeductible. The tool does not compute that choice, so it refuses through ira.deduct_less.

Ruling: representation; project retained. Schedule 1 line 20 is the sum of each person's line 12 (person.ira_deduction), which is line 12a for the taxpayer and 12b for the spouse, as the second adds them; the remaining difference is the structure of line 12, ruled under 12a and 12b. The election to deduct less (the second's ira.deduct_less) is refused on this line by the project too (ira.less_gate, amb.2025.ira_deduct_less, owner decision 8). i1040gi p. 98, line 12, "Add the amounts on lines 12a and 12b and enter the total on Schedule 1, line 20".

### 1a — Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}], "test": "all"}}], "test": "lt"}
```

Second transcription's note: The worksheet says 'You may not be able to use this worksheet' and gives a list of cases that send you to Pub. 590-A. Chosen reading: the ira.special screen stands for those cases, so the tool stops at line 1a when ira.special is yes. Coverage comes from person.ira_cov, which includes the rule that a person married filing separately is treated as covered if the spouse was.

Ruling: representation; project retained. Both read the taxpayer's coverage (person.ira_cov). The project's line also requires a traditional IRA contribution (ira.any_trad), the condition for using the worksheet at all (i1040gi p. 95, Line 20, "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction"); without one every value line is zero on both sides. The deduction reads person.ira_cov, never this display line. The second's ira.special stop is the project's ira.special_gate, which refuses person.ira_line11 and so lines 12 and 20. A separate return is refused (scope.ready, s3.mfs), so the married-filing-separately amounts and rules are not reached.

### 1b — If married filing jointly, was your spouse covered by a retirement plan?
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}
```

Ruling: representation; project retained. Both read the spouse's coverage (person.ira_cov of the spouse entry). The second adds the joint-return condition; the project has a spouse entry only on a joint return (household.roster_bad refuses any other roster: "only when married filing jointly, one person with the role spouse"), so the count is zero otherwise. The project's line also requires a traditional IRA contribution (ira.any_trad), the condition for using the worksheet at all (i1040gi p. 95, Line 20, "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction"); without one every value line is zero on both sides. i1040gi p. 97, line 1b, "If married filing jointly, was your spouse covered by a retirement plan?"

### 2a — Enter the amount shown below that applies to you (your IRA)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "person.ira_line2", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"collection": "person", "field": "person.ira_line2", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}
```

Second transcription's note: Line 2 depends on facts the parameters cannot express here: $89,000 for married filing separately when you lived apart all year, and $246,000 for a person who was not covered on a joint return. Chosen reading: take your column from the per-person field person.ira_line2.

Ruling: representation; project retained. Both take the column's line 2 from person.ira_line2. The project shows zero when lines 2 through 6 are skipped (no one covered, or no traditional contributions), as the worksheet says: i1040gi p. 97, "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6"; the second shows the amount on a skipped line. Line 6 reads person.ira_line2 directly and line 7 reads line 6 only when someone is covered (person.ira_line7), so no later value differs. A separate return is refused (scope.ready, s3.mfs), so the married-filing-separately amounts and rules are not reached.

### 2b — Enter the amount shown below that applies to you (your spouse's IRA)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "person.ira_line2", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"collection": "person", "field": "person.ira_line2", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}
```

Second transcription's note: Taken from your spouse's person entry. There is a spouse entry only on a joint return, so this is zero otherwise.

Ruling: representation; project retained. As line 2a, for the spouse's column: both take person.ira_line2 of the spouse entry, the project shows zero when lines 2 through 6 are skipped (i1040gi p. 97, "skip lines 2 through 6"), and the project has a spouse entry only on a joint return (household.roster_bad refuses any other roster: "only when married filing jointly, one person with the role spouse"), so the column is zero on any other return, as the second's note says.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **AGREE**

### 4 — Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25
Status: **AGREE**

### 5 — Subtract line 4 from line 3. If married filing jointly, enter the result in both columns
Status: **AGREE**

### 6a — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line 
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "person.ira_line6", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"line": "5"}, {"line": "2a"}], "test": "lt"}], "test": "all"}, "then": {"from": {"line": "2a"}, "op": "subtract_floor0", "take": {"line": "5"}}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "ne"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "all"}, {"args": [{"line": "2a"}, {"line": "5"}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The 'No' answer (STOP) is applied to each column separately, because line 2 can differ between columns on a joint return. The line is zero when the answer is No or when lines 2 through 6 are skipped.

Ruling: representation; project retained. Both subtract line 5 from the column's line 2 with zero on the No answer when someone is covered (person.ira_line6, line 2 less line 5 floored at zero), per column as the second's note reads (i1040gi p. 97, line 6, "Subtract line 5 from line 2 in each column"; "None of your IRA contributions are deductible"). The project's display line is zero when lines 2 through 6 are skipped, including when no one made traditional contributions; line 7 reads person.ira_line6, so no value differs.

### 6b — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line 
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}], "test": "lt"}], "test": "all"}, "then": {"collection": "person", "field": "person.ira_line6", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": 0}, {"collection": "sc", "field": "sc.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": "none"}, {"input": "person.plan"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "person.ira_work_plan"}], "test": "eq"}], "test": "any"}}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"line": "5"}, {"line": "2b"}], "test": "lt"}], "test": "all"}, "then": {"from": {"line": "2b"}, "op": "subtract_floor0", "take": {"line": "5"}}}, {"guard": {"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "ne"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "all"}, {"args": [{"line": "2b"}, {"line": "5"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; project retained. As line 6a, for the spouse's column; the second's joint-return condition is met by the roster (the project has a spouse entry only on a joint return (household.roster_bad refuses any other roster: "only when married filing jointly, one person with the role spouse")). i1040gi p. 97, line 6, "Subtract line 5 from line 2 in each column".

### 7a — Multiply line 6a by the percentage that applies to you, increased to a multiple of $10 and
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"collection": "person", "field": "person.ira_line7", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"line": "5"}, {"line": "2a"}], "test": "lt"}], "test": "all"}, {"args": [{"line": "6a"}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"line": "1a"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"line": "1a"}], "test": "eq"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"line": "1a"}], "test": "ne"}], "test": "all"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "6a"}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"line": "1a"}], "test": "ne"}], "test": "all"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "6a"}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"line": "1a"}], "test": "eq"}], "test": "any"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "6a"}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"line": "1a"}], "test": "eq"}], "test": "any"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "6a"}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "ne"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "all"}, {"args": [{"line": "2a"}, {"line": "5"}], "test": "le"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"line": "5"}, {"line": "2a"}], "test": "lt"}], "test": "all"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"line": "1a"}], "test": "ne"}], "test": "all"}, "then": {"param": "ira.full_joint"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"line": "1a"}], "test": "eq"}], "test": "any"}, "then": {"param": "ira.full_narrow"}}], "op": "choose"}, {"line": "6a"}], "test": "le"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "ne"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}], "op": "choose"}
```

Second transcription's note: When line 6 is No (the STOP), this line is zero, not the $200 minimum, because none of the contributions are deductible.

Ruling: representation; project retained. The project's line 7 is person.ira_line7: the applicable amount ($7,000, or $8,000 at age 50 or older) when no one is covered or line 6 is at least $20,000 ($10,000 for a single filer or the column of a person not covered); zero on line 6's No; otherwise line 6 times 35% or 40% (joint or qualifying surviving spouse, covered column) or 70% or 80%, increased to a multiple of $10 and at least $200. The second builds the same cases from lines 1a, 1b, 2 and 6 and gives the same amount in every reachable column (its 70% test, not joint or line 1a No, and the project's, not joint type or this person not covered, part only for a qualifying surviving spouse who is not covered, whose column never has someone else covered). Zero on line 6's No, as the second's note says, is the project's person.ira_below. The project's line also requires a traditional IRA contribution (ira.any_trad), the condition for using the worksheet at all (i1040gi p. 95, Line 20, "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction"); without one every value line is zero on both sides. i1040gi p. 98, line 7, "Multiply lines 6a and 6b by the percentage below that applies to you. If the result isn’t a multiple of $10, increase it to the next multiple of $10".

### 7b — Multiply line 6b by the percentage that applies to you, increased to a multiple of $10 and
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"collection": "person", "field": "person.ira_line7", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"line": "5"}, {"line": "2b"}], "test": "lt"}], "test": "all"}, {"args": [{"line": "6b"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "1b"}], "test": "eq"}, "then": {"param": "ira.full_narrow"}}, {"guard": {"args": [{"const": false}, {"line": "1b"}], "test": "ne"}, "then": {"param": "ira.full_joint"}}], "op": "choose"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"of": {"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"line": "1b"}], "test": "eq"}, {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "6b"}, "op": "multiply_rate", "rate": {"param": "ira.rate_70"}}}, {"guard": {"args": [{"args": [{"const": false}, {"line": "1b"}], "test": "eq"}, {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "6b"}, "op": "multiply_rate", "rate": {"param": "ira.rate_80"}}}, {"guard": {"args": [{"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}, {"args": [{"const": false}, {"line": "1b"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "6b"}, "op": "multiply_rate", "rate": {"param": "ira.rate_35"}}}, {"guard": {"args": [{"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, {"args": [{"const": false}, {"line": "1b"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"line": "6b"}, "op": "multiply_rate", "rate": {"param": "ira.rate_40"}}}], "op": "choose"}, "op": "round", "rule": "up", "unit": 1000}, {"param": "ira.min"}], "op": "larger_of"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"line": "5"}, {"line": "2b"}], "test": "lt"}], "test": "all"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "1b"}], "test": "eq"}, "then": {"param": "ira.full_narrow"}}, {"guard": {"args": [{"const": false}, {"line": "1b"}], "test": "ne"}, "then": {"param": "ira.full_joint"}}], "op": "choose"}, {"line": "6b"}], "test": "le"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "ne"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}, {"const": 0}], "test": "le"}, "then": {"param": "ira.limit"}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}, {"args": [{"const": true}, {"ref": "person.ira_age50"}], "test": "eq"}], "test": "all"}}], "test": "lt"}, "then": {"param": "ira.limit_50"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "ne"}, {"args": [{"const": true}, {"line": "1b"}], "test": "ne"}], "test": "all"}, {"args": [{"line": "2b"}, {"line": "5"}], "test": "le"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"line": "1a"}], "test": "eq"}, {"args": [{"const": true}, {"line": "1b"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The spouse's column applies only on a joint return ('You must file a joint return to deduct contributions to your spouse's IRA'), so it is zero otherwise.

Ruling: representation; project retained. As line 7a, for the spouse's column (person.ira_line7 of the spouse entry): the second's zero on a return that is not joint is the project's, since the project has a spouse entry only on a joint return (household.roster_bad refuses any other roster: "only when married filing jointly, one person with the role spouse"). i1040gi p. 95, Line 20, item 6, "You must file a joint return to deduct contributions to your spouse’s IRA".

### 8 — Enter the total of your (and your spouse's if filing jointly): wages, salaries, tips, etc.
Status: **DISAGREE**

Project:

```json
{"of": [{"collection": "person", "field": "person.box1", "op": "sum_over", "where": null}, {"ref": "s1.line2a"}], "op": "sum"}
```

Second:

```json
{"of": [{"ref": "f1040.line1a"}, {"ref": "s1.line2a"}], "op": "sum"}
```

Second transcription's note: Wages are the Form W-2 box 1 total (Form 1040, line 1a). The tool has no amount for nontaxable combat pay, so a return with combat pay is refused through s8812.combat_pay. Nonqualified deferred compensation and nongovernmental section 457 income, which must be left out, are refused through ira.special.

Ruling: representation; project retained. Form 1040 line 1a is the sum of person.box1 over the people on the return (f1040.line1a), which is the project's ira.wages, so the lines are the same total; the comparison does not expand another form's printed line. Nontaxable combat pay is refused on both sides (the project's ira.combat_gate on person.ira_line11, reaching lines 12 and 20; i1040gi p. 98, line 8, "Nontaxable combat pay"), and nonqualified deferred compensation by ira.special_gate (p. 95, item 5, "don’t include that income on line 8 of the worksheet").

### 9 — Enter the earned income you (and your spouse if filing jointly) received as a self-employe
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_se", "op": "sum_over", "where": null}
```

Second:

```json
{"from": {"ref": "s1.line3"}, "op": "subtract_floor0", "take": {"of": [{"ref": "s1.line15"}, {"ref": "s1.line16"}], "op": "sum"}}
```

Second transcription's note: The text says 'generally' net earnings from self-employment. Chosen reading: Schedule C net profit or loss for both spouses (Schedule 1, line 3), the only self-employment income in scope. The floor is applied to the combined total, as the line is printed.

Ruling: binding reading; project retained. The project floors each person's self-employment earned income at zero and adds the two (person.ira_se); the second floors the couple's total as printed (i1040gi p. 98, line 9, "If zero or less, enter -0-"). The reading is the owner's decision 9(c), recorded as amb.2025.ira_se_floor: p590a p. 7, Self-employment loss, "If you have a net loss from self-employment, don’t subtract the loss from your salaries or wages when figuring your total compensation". Both take the Schedule C result less Schedule 1 lines 15 and 16 (amb.2025.ira_se_earned); they differ only on a joint return with one spouse's loss and the other's profit.

### 10 — Add lines 8 and 9
Status: **AGREE**

### 11a — Enter traditional IRA contributions made, or that will be made by the due date of your 202
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}
```

Second:

```json
{"collection": "person", "field": "person.ira_trad", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}
```

Second transcription's note: The CAUTION after line 10 says to stop there. Chosen reading: the tool stops at the next line, 11a (and 11b).

Ruling: representation; project retained. person.ira_contrib is person.ira_trad when the person answered Yes to the traditional IRA question (person.sav_trad) and zero on No; the amount is asked only after Yes, so both are the same contribution. i1040gi p. 98, line 11, "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return ... for 2025 to your IRA on line 11a". The second's stop after line 10 is the project's ira.kbh_short, which refuses person.ira_line11 and so lines 12 and 20 (p. 98, Caution, "stop here and use the worksheet in Pub. 590-A to figure your IRA deduction").

### 11b — Enter traditional IRA contributions made, or that will be made by the due date of your 202
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_contrib", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}
```

Second:

```json
{"collection": "person", "field": "person.ira_trad", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}
```

Ruling: representation; project retained. As line 11a, for the spouse entry: person.ira_contrib is person.ira_trad after a Yes to person.sav_trad. i1040gi p. 98, line 11, "and to your spouse’s IRA on line 11b".

### 12a — Enter the smallest of line 7a, 10, or 11a. This is the most you can deduct (your IRA)
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_deduction", "op": "sum_over", "where": {"args": [{"const": "taxpayer"}, {"ref": "person.role"}], "test": "eq"}}
```

Second:

```json
{"of": [{"line": "11a"}, {"of": [{"line": "10"}, {"line": "7a"}], "op": "smaller_of"}], "op": "smaller_of"}
```

Ruling: representation; project retained. person.ira_deduction is the smallest of the person's line 7 (person.ira_line7), line 10 and line 11 (person.ira_line12), and zero without traditional contributions, where line 11 is zero and the smallest is zero too; so it is the second's smallest of 7a, 10 and 11a, and the trees differ only through line 7, ruled under 7a. i1040gi p. 98, line 12, "On line 12a, enter the smallest of line 7a, 10, or 11a".

### 12b — Enter the smallest of line 7b, 10, or 11b. This is the most you can deduct (your spouse's 
Status: **DISAGREE**

Project:

```json
{"collection": "person", "field": "person.ira_deduction", "op": "sum_over", "where": {"args": [{"const": "spouse"}, {"ref": "person.role"}], "test": "eq"}}
```

Second:

```json
{"of": [{"line": "11b"}, {"of": [{"line": "10"}, {"line": "7b"}], "op": "smaller_of"}], "op": "smaller_of"}
```

Second transcription's note: As printed, each column is limited by the full combined line 10. No further limit across the two columns is applied, because the worksheet does not state one.

Ruling: representation; project retained. As line 12a, for the spouse entry. Neither side limits the two columns together, as printed: i1040gi p. 98, line 12, "On line 12b, enter the smallest of line 7b, 10, or 11b. This is the most you can deduct".

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| ira.anyone_covered | ira.special | ira.special |
| ira.line20 | ira.deduct_less, ira.h_kbh_stop, ira.special, s8812.combat_pay | ira.deduct_less, ira.h_kbh_stop, ira.special, s8812.combat_pay |
| 1a | ira.special | ira.special |
| 6a | ira.special | ira.special |
| 6b | ira.special | ira.special |
| 7a | ira.special | ira.special |
| 7b | ira.special | ira.special |
| 8 | ira.special, s8812.combat_pay | ira.special, s8812.combat_pay |
| 10 | ira.special, s8812.combat_pay | ira.special, s8812.combat_pay |
| 11a | ira.h_kbh_stop | ira.h_kbh_stop |
| 11b | ira.h_kbh_stop | ira.h_kbh_stop |
| 12a | ira.h_kbh_stop, ira.special, s8812.combat_pay | ira.h_kbh_stop, ira.special, s8812.combat_pay |
| 12b | ira.h_kbh_stop, ira.special, s8812.combat_pay | ira.h_kbh_stop, ira.special, s8812.combat_pay |

## Raw second transcription

```yaml
```yaml
lines:
  - id: ira.joint
    printed: "(helper)"
    label: "Married filing jointly"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfj"}]}

  - id: ira.joint_type
    printed: "(helper)"
    label: "Married filing jointly or qualifying surviving spouse"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [f1040.status, {const: "mfj"}]}
        - {op: test, eq: [f1040.status, {const: "qss"}]}

  - id: ira.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: ira.h_a_cov_n
    printed: "(helper)"
    label: "Number of your entries showing you were covered by a retirement plan"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.ira_cov, {const: true}]}

  - id: ira.line1a
    printed: "1a"
    label: "Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?"
    type: Bool
    expr: {op: test, gt: [ira.h_a_cov_n, {const: 0}]}
    refuses: [ira.special]
    note: "The worksheet says 'You may not be able to use this worksheet' and gives a list of cases that send you to Pub. 590-A. Chosen reading: the ira.special screen stands for those cases, so the tool stops at line 1a when ira.special is yes. Coverage comes from person.ira_cov, which includes the rule that a person married filing separately is treated as covered if the spouse was."

  - id: ira.h_b_cov_n
    printed: "(helper)"
    label: "Number of your spouse's entries showing your spouse was covered by a retirement plan"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.ira_cov, {const: true}]}

  - id: ira.line1b
    printed: "1b"
    label: "If married filing jointly, was your spouse covered by a retirement plan?"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ira.joint, {const: true}]}
        - {op: test, gt: [ira.h_b_cov_n, {const: 0}]}

  - id: ira.anyone_covered
    printed: "(helper)"
    label: "You (or, on a joint return, your spouse) were covered by a retirement plan (Yes on line 1a or 1b)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [ira.line1a, {const: true}]}
        - {op: test, eq: [ira.line1b, {const: true}]}

  - id: ira.h_a_age50_n
    printed: "(helper)"
    label: "Number of your entries showing you were age 50 or older at the end of 2025"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "taxpayer"}]}
          - {op: test, eq: [person.ira_age50, {const: true}]}

  - id: ira.h_a_age50
    printed: "(helper)"
    label: "You were age 50 or older at the end of 2025"
    type: Bool
    expr: {op: test, gt: [ira.h_a_age50_n, {const: 0}]}

  - id: ira.h_b_age50_n
    printed: "(helper)"
    label: "Number of your spouse's entries showing your spouse was age 50 or older at the end of 2025"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where:
        op: test
        all:
          - {op: test, eq: [person.role, {const: "spouse"}]}
          - {op: test, eq: [person.ira_age50, {const: true}]}

  - id: ira.h_b_age50
    printed: "(helper)"
    label: "Your spouse was age 50 or older at the end of 2025"
    type: Bool
    expr: {op: test, gt: [ira.h_b_age50_n, {const: 0}]}

  - id: ira.h_limit
    printed: "(helper)"
    label: "$7,000 if under age 50 at the end of 2025"
    type: NonNegDollars
    expr: {op: param, ref: ira.limit}

  - id: ira.h_limit_50
    printed: "(helper)"
    label: "$8,000 if age 50 or older at the end of 2025"
    type: NonNegDollars
    expr: {op: param, ref: ira.limit_50}

  - id: ira.h_a_limit
    printed: "(helper)"
    label: "The applicable amount for your column ($7,000 if under age 50; $8,000 if age 50 or older)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [ira.h_a_age50, {const: true}]}, then: ira.h_limit_50}
        - {guard: {op: test, eq: [ira.h_a_age50, {const: false}]}, then: ira.h_limit}

  - id: ira.h_b_limit
    printed: "(helper)"
    label: "The applicable amount for your spouse's column ($7,000 if under age 50; $8,000 if age 50 or older)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [ira.h_b_age50, {const: true}]}, then: ira.h_limit_50}
        - {guard: {op: test, eq: [ira.h_b_age50, {const: false}]}, then: ira.h_limit}

  - id: ira.line2a
    printed: "2a"
    label: "Enter the amount shown below that applies to you (your IRA)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.ira_line2
      where: {op: test, eq: [person.role, {const: "taxpayer"}]}
    note: "Line 2 depends on facts the parameters cannot express here: $89,000 for married filing separately when you lived apart all year, and $246,000 for a person who was not covered on a joint return. Chosen reading: take your column from the per-person field person.ira_line2."

  - id: ira.line2b
    printed: "2b"
    label: "Enter the amount shown below that applies to you (your spouse's IRA)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.ira_line2
      where: {op: test, eq: [person.role, {const: "spouse"}]}
    note: "Taken from your spouse's person entry. There is a spouse entry only on a joint return, so this is zero otherwise."

  - id: ira.line3
    printed: "3"
    label: "Enter the amount from Form 1040 or 1040-SR, line 9"
    type: Dollars
    expr: {op: copy, from: f1040.line9}

  - id: ira.line4
    printed: "4"
    label: "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25"
    type: NonNegDollars
    expr: {op: sum, of: [s1.line11, s1.line13, s1.line15, s1.line16, s1.line17, s1.line18, s1.line19a, s1.line25]}
    note: "Schedule 1 lines 12, 14 and 23 are not defined in this tool; they fall under the scope.schedule1 screen. Chosen reading: total only the lines the tool defines."

  - id: ira.line5
    printed: "5"
    label: "Subtract line 4 from line 3. If married filing jointly, enter the result in both columns"
    type: Dollars
    expr: {op: subtract, from: ira.line3, take: ira.line4}
    note: "Both columns hold the same amount, so it is kept as one line."

  - id: ira.h_a_yes
    printed: "(helper)"
    label: "Is the amount on line 5 less than the amount on line 2 (your column)?"
    type: Bool
    expr: {op: test, lt: [ira.line5, ira.line2a]}

  - id: ira.h_b_yes
    printed: "(helper)"
    label: "Is the amount on line 5 less than the amount on line 2 (your spouse's column)?"
    type: Bool
    expr: {op: test, lt: [ira.line5, ira.line2b]}

  - id: ira.h_a_go
    printed: "(helper)"
    label: "Lines 2 through 6 apply and line 6 is Yes in your column"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ira.anyone_covered, {const: true}]}
        - {op: test, eq: [ira.h_a_yes, {const: true}]}

  - id: ira.h_b_go
    printed: "(helper)"
    label: "Joint return, lines 2 through 6 apply and line 6 is Yes in your spouse's column"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ira.joint, {const: true}]}
        - {op: test, eq: [ira.anyone_covered, {const: true}]}
        - {op: test, eq: [ira.h_b_yes, {const: true}]}

  - id: ira.h_a_diff
    printed: "(helper)"
    label: "Subtract line 5 from line 2 (your column)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ira.line2a, take: ira.line5}

  - id: ira.h_b_diff
    printed: "(helper)"
    label: "Subtract line 5 from line 2 (your spouse's column)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ira.line2b, take: ira.line5}

  - id: ira.line6a
    printed: "6a"
    label: "Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line 2 (your IRA); if no, none of your IRA contributions are deductible"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [ira.h_a_go, {const: true}]}, then: ira.h_a_diff}
        - {guard: {op: test, eq: [ira.h_a_go, {const: false}]}, then: ira.h_zero}
    note: "The 'No' answer (STOP) is applied to each column separately, because line 2 can differ between columns on a joint return. The line is zero when the answer is No or when lines 2 through 6 are skipped."

  - id: ira.line6b
    printed: "6b"
    label: "Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line 2 (your spouse's IRA)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [ira.h_b_go, {const: true}]}, then: ira.h_b_diff}
        - {guard: {op: test, eq: [ira.h_b_go, {const: false}]}, then: ira.h_zero}

  - id: ira.h_full_narrow
    printed: "(helper)"
    label: "$10,000"
    type: NonNegDollars
    expr: {op: param, ref: ira.full_narrow}

  - id: ira.h_full_joint
    printed: "(helper)"
    label: "$20,000"
    type: NonNegDollars
    expr: {op: param, ref: ira.full_joint}

  - id: ira.h_min
    printed: "(helper)"
    label: "$200"
    type: NonNegDollars
    expr: {op: param, ref: ira.min}

  - id: ira.h_a_wide
    printed: "(helper)"
    label: "Your column uses 70% (80%) and the $10,000 threshold: single, head of household or married filing separately, or not covered by a plan on a joint-type return"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [ira.joint_type, {const: false}]}
        - {op: test, eq: [ira.line1a, {const: false}]}

  - id: ira.h_b_wide
    printed: "(helper)"
    label: "Your spouse's column uses 70% (80%) and the $10,000 threshold (spouse not covered by a retirement plan)"
    type: Bool
    expr: {op: test, eq: [ira.line1b, {const: false}]}

  - id: ira.h_a_full
    printed: "(helper)"
    label: "Line 6 result at or above which your column takes the applicable amount ($10,000 or $20,000)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [ira.h_a_wide, {const: true}]}, then: ira.h_full_narrow}
        - {guard: {op: test, eq: [ira.h_a_wide, {const: false}]}, then: ira.h_full_joint}

  - id: ira.h_b_full
    printed: "(helper)"
    label: "Line 6 result at or above which your spouse's column takes the applicable amount ($10,000 or $20,000)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [ira.h_b_wide, {const: true}]}, then: ira.h_full_narrow}
        - {guard: {op: test, eq: [ira.h_b_wide, {const: false}]}, then: ira.h_full_joint}

  - id: ira.h_a_at_full
    printed: "(helper)"
    label: "The line 6a result is at or above the threshold"
    type: Bool
    expr: {op: test, ge: [ira.line6a, ira.h_a_full]}

  - id: ira.h_b_at_full
    printed: "(helper)"
    label: "The line 6b result is at or above the threshold"
    type: Bool
    expr: {op: test, ge: [ira.line6b, ira.h_b_full]}

  - id: ira.h_a_p70
    printed: "(helper)"
    label: "Line 6a multiplied by 70% (0.70)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6a, rate: {param: ira.rate_70}}

  - id: ira.h_a_p80
    printed: "(helper)"
    label: "Line 6a multiplied by 80% (0.80)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6a, rate: {param: ira.rate_80}}

  - id: ira.h_a_p35
    printed: "(helper)"
    label: "Line 6a multiplied by 35% (0.35)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6a, rate: {param: ira.rate_35}}

  - id: ira.h_a_p40
    printed: "(helper)"
    label: "Line 6a multiplied by 40% (0.40)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6a, rate: {param: ira.rate_40}}

  - id: ira.h_a_prod
    printed: "(helper)"
    label: "Line 6a multiplied by the percentage that applies to your column"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [ira.h_a_wide, {const: true}]}, {op: test, eq: [ira.h_a_age50, {const: true}]}]}
          then: ira.h_a_p80
        - guard: {op: test, all: [{op: test, eq: [ira.h_a_wide, {const: true}]}, {op: test, eq: [ira.h_a_age50, {const: false}]}]}
          then: ira.h_a_p70
        - guard: {op: test, all: [{op: test, eq: [ira.h_a_wide, {const: false}]}, {op: test, eq: [ira.h_a_age50, {const: true}]}]}
          then: ira.h_a_p40
        - guard: {op: test, all: [{op: test, eq: [ira.h_a_wide, {const: false}]}, {op: test, eq: [ira.h_a_age50, {const: false}]}]}
          then: ira.h_a_p35

  - id: ira.h_a_round
    printed: "(helper)"
    label: "If the result isn't a multiple of $10, increase it to the next multiple of $10 (your column)"
    type: NonNegDollars
    expr: {op: round, of: ira.h_a_prod, unit: 1000, rule: up}

  - id: ira.h_a_floor
    printed: "(helper)"
    label: "If the result is $200 or more, enter the result; if less than $200, enter $200 (your column)"
    type: NonNegDollars
    expr: {op: larger_of, of: [ira.h_a_round, ira.h_min]}

  - id: ira.line7a
    printed: "7a"
    label: "Multiply line 6a by the percentage that applies to you, increased to a multiple of $10 and at least $200 (or the applicable amount, when lines 2 through 6 are skipped or line 6 is at or above the threshold) (your IRA)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.anyone_covered, {const: false}]}
          then: ira.h_a_limit
        - guard: {op: test, all: [{op: test, eq: [ira.anyone_covered, {const: true}]}, {op: test, eq: [ira.h_a_go, {const: false}]}]}
          then: ira.h_zero
        - guard: {op: test, all: [{op: test, eq: [ira.h_a_go, {const: true}]}, {op: test, eq: [ira.h_a_at_full, {const: true}]}]}
          then: ira.h_a_limit
        - guard: {op: test, all: [{op: test, eq: [ira.h_a_go, {const: true}]}, {op: test, eq: [ira.h_a_at_full, {const: false}]}]}
          then: ira.h_a_floor
    note: "When line 6 is No (the STOP), this line is zero, not the $200 minimum, because none of the contributions are deductible."

  - id: ira.h_b_p70
    printed: "(helper)"
    label: "Line 6b multiplied by 70% (0.70)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6b, rate: {param: ira.rate_70}}

  - id: ira.h_b_p80
    printed: "(helper)"
    label: "Line 6b multiplied by 80% (0.80)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6b, rate: {param: ira.rate_80}}

  - id: ira.h_b_p35
    printed: "(helper)"
    label: "Line 6b multiplied by 35% (0.35)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6b, rate: {param: ira.rate_35}}

  - id: ira.h_b_p40
    printed: "(helper)"
    label: "Line 6b multiplied by 40% (0.40)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ira.line6b, rate: {param: ira.rate_40}}

  - id: ira.h_b_prod
    printed: "(helper)"
    label: "Line 6b multiplied by the percentage that applies to your spouse's column"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [ira.h_b_wide, {const: true}]}, {op: test, eq: [ira.h_b_age50, {const: true}]}]}
          then: ira.h_b_p80
        - guard: {op: test, all: [{op: test, eq: [ira.h_b_wide, {const: true}]}, {op: test, eq: [ira.h_b_age50, {const: false}]}]}
          then: ira.h_b_p70
        - guard: {op: test, all: [{op: test, eq: [ira.h_b_wide, {const: false}]}, {op: test, eq: [ira.h_b_age50, {const: true}]}]}
          then: ira.h_b_p40
        - guard: {op: test, all: [{op: test, eq: [ira.h_b_wide, {const: false}]}, {op: test, eq: [ira.h_b_age50, {const: false}]}]}
          then: ira.h_b_p35

  - id: ira.h_b_round
    printed: "(helper)"
    label: "If the result isn't a multiple of $10, increase it to the next multiple of $10 (your spouse's column)"
    type: NonNegDollars
    expr: {op: round, of: ira.h_b_prod, unit: 1000, rule: up}

  - id: ira.h_b_floor
    printed: "(helper)"
    label: "If the result is $200 or more, enter the result; if less than $200, enter $200 (your spouse's column)"
    type: NonNegDollars
    expr: {op: larger_of, of: [ira.h_b_round, ira.h_min]}

  - id: ira.line7b
    printed: "7b"
    label: "Multiply line 6b by the percentage that applies to you, increased to a multiple of $10 and at least $200 (or the applicable amount) (your spouse's IRA)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ira.joint, {const: false}]}
          then: ira.h_zero
        - guard: {op: test, all: [{op: test, eq: [ira.joint, {const: true}]}, {op: test, eq: [ira.anyone_covered, {const: false}]}]}
          then: ira.h_b_limit
        - guard: {op: test, all: [{op: test, eq: [ira.joint, {const: true}]}, {op: test, eq: [ira.anyone_covered, {const: true}]}, {op: test, eq: [ira.h_b_go, {const: false}]}]}
          then: ira.h_zero
        - guard: {op: test, all: [{op: test, eq: [ira.h_b_go, {const: true}]}, {op: test, eq: [ira.h_b_at_full, {const: true}]}]}
          then: ira.h_b_limit
        - guard: {op: test, all: [{op: test, eq: [ira.h_b_go, {const: true}]}, {op: test, eq: [ira.h_b_at_full, {const: false}]}]}
          then: ira.h_b_floor
    note: "The spouse's column applies only on a joint return ('You must file a joint return to deduct contributions to your spouse's IRA'), so it is zero otherwise."

  - id: ira.line8
    printed: "8"
    label: "Enter the total of your (and your spouse's if filing jointly): wages, salaries, tips, etc.; alimony and separate maintenance payments reported on Schedule 1, line 2a; and nontaxable combat pay"
    type: NonNegDollars
    expr: {op: sum, of: [f1040.line1a, s1.line2a]}
    refuses: [ira.special, s8812.combat_pay]
    note: "Wages are the Form W-2 box 1 total (Form 1040, line 1a). The tool has no amount for nontaxable combat pay, so a return with combat pay is refused through s8812.combat_pay. Nonqualified deferred compensation and nongovernmental section 457 income, which must be left out, are refused through ira.special."

  - id: ira.h_9take
    printed: "(helper)"
    label: "Deductions on Schedule 1, lines 15 and 16"
    type: NonNegDollars
    expr: {op: sum, of: [s1.line15, s1.line16]}

  - id: ira.line9
    printed: "9"
    label: "Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner, minus any deductions on Schedule 1, lines 15 and 16. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: s1.line3, take: ira.h_9take}
    note: "The text says 'generally' net earnings from self-employment. Chosen reading: Schedule C net profit or loss for both spouses (Schedule 1, line 3), the only self-employment income in scope. The floor is applied to the combined total, as the line is printed."

  - id: ira.line10
    printed: "10"
    label: "Add lines 8 and 9"
    type: NonNegDollars
    expr: {op: sum, of: [ira.line8, ira.line9]}

  - id: ira.h_age50_n
    printed: "(helper)"
    label: "Number of people on the return age 50 or older at the end of 2025"
    type: Count
    expr:
      op: sum_over
      collection: person
      field: person.one
      where: {op: test, eq: [person.ira_age50, {const: true}]}

  - id: ira.h_kbh_none
    printed: "(helper)"
    label: "$14,000"
    type: NonNegDollars
    expr: {op: param, ref: ira.kbh_none}

  - id: ira.h_kbh_one
    printed: "(helper)"
    label: "$15,000 if one spouse is age 50 or older at the end of 2025"
    type: NonNegDollars
    expr: {op: param, ref: ira.kbh_one}

  - id: ira.h_kbh_both
    printed: "(helper)"
    label: "$16,000 if both spouses are age 50 or older at the end of 2025"
    type: NonNegDollars
    expr: {op: param, ref: ira.kbh_both}

  - id: ira.h_kbh_limit
    printed: "(helper)"
    label: "$14,000 ($15,000 if one spouse is age 50 or older; $16,000 if both)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [ira.h_age50_n, {const: 0}]}, then: ira.h_kbh_none}
        - {guard: {op: test, eq: [ira.h_age50_n, {const: 1}]}, then: ira.h_kbh_one}
        - {guard: {op: test, ge: [ira.h_age50_n, {const: 2}]}, then: ira.h_kbh_both}

  - id: ira.h_kbh_stop
    printed: "(helper)"
    label: "If married filing jointly and line 10 is less than $14,000 ($15,000; $16,000), stop here and use the worksheet in Pub. 590-A"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ira.joint, {const: true}]}
        - {op: test, lt: [ira.line10, ira.h_kbh_limit]}

  - id: ira.line11a
    printed: "11a"
    label: "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions, for 2025 to your IRA"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.ira_trad
      where: {op: test, eq: [person.role, {const: "taxpayer"}]}
    refuses: [ira.h_kbh_stop]
    note: "The CAUTION after line 10 says to stop there. Chosen reading: the tool stops at the next line, 11a (and 11b)."

  - id: ira.line11b
    printed: "11b"
    label: "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions, for 2025 to your spouse's IRA"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: person
      field: person.ira_trad
      where: {op: test, eq: [person.role, {const: "spouse"}]}
    refuses: [ira.h_kbh_stop]

  - id: ira.h_12a_7_10
    printed: "(helper)"
    label: "The smaller of line 7a or line 10"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ira.line7a, ira.line10]}

  - id: ira.line12a
    printed: "12a"
    label: "Enter the smallest of line 7a, 10, or 11a. This is the most you can deduct (your IRA)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ira.h_12a_7_10, ira.line11a]}

  - id: ira.h_12b_7_10
    printed: "(helper)"
    label: "The smaller of line 7b or line 10"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ira.line7b, ira.line10]}

  - id: ira.line12b
    printed: "12b"
    label: "Enter the smallest of line 7b, 10, or 11b. This is the most you can deduct (your spouse's IRA)"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ira.h_12b_7_10, ira.line11b]}
    note: "As printed, each column is limited by the full combined line 10. No further limit across the two columns is applied, because the worksheet does not state one."

  - id: ira.line20
    printed: "(helper)"
    label: "The total of lines 12a and 12b for Schedule 1, line 20"
    type: NonNegDollars
    expr: {op: sum, of: [ira.line12a, ira.line12b]}
    refuses: [ira.deduct_less]
    note: "The worksheet lets you deduct a smaller amount and treat the rest as nondeductible. The tool does not compute that choice, so it refuses through ira.deduct_less."
```
```
