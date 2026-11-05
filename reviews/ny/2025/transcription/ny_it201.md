# Transcription agreement — ny_it201

Second transcription of `Form IT-201 (2025), Resident Income Tax Return — New York State and New York City` by an isolated model (spec 6.5), compared line by line with `forms/ny/2025/ny_it201.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-04 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f3f8c326d3828cbc0684a46ec47d3e018d206a842853958ee0bad5afb279af0b |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | fail |
| required input context sha256 | d104b5038b448ab12d9eaa1f8fdc5a1c1f436db08920362e1f3df0abcc7c6673 |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | 83e9ed0ae4edc40db4c301ed52bf00d46afb0b4bd30dea929e35960993911093 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 2393cb72f2535e7c3f747e4b47682ef39151358f6455398ceb716845b03a9c6b |
| printed lines compared | 166 |
| agree / disagree / missing | 85 / 81 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 30, 31, 32 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 3, 4, 5, 6, 7, 8, 9, 10, 15, 17, 18, 19, 20, 21, 22, 23, 24, 30, 31, 32 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |
| ny_it201 | Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12 | 1, 2, 3, 4 | whole document | c924371c32a986a1903c9216bd60c6df8fb52f8e506e5c462851226b71e2154d | - | 895c4b15bba606353fd49f5779f969877e55196eda7f7b9f633f02cbd3dbbb3d |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: All others:; Calculation of NYC school tax credit (rate reduction amount) for head of household ④; Calculation of NYC school tax credit (rate reduction amount) for married filing jointly ② and qualifying surviving spouse ⑤; Calculation of NYC school tax credit (rate reduction amount) for single ① and married filing separately ③; Joint returns; Line 40: New York State household credit; New York City household credit table 4—Filing status ① only (Single); New York City household credit table 5—Filing status ②, ④, and ⑤; New York State household credit table 1—Filing status ① only (Single); New York State household credit table 2—Filing status ②, ④, and ⑤; New York State standard deduction table; Table 1 - Full-year New York City residents: New York City school tax credit table; Tax computation worksheet 1; Tax computation worksheet 10; Tax computation worksheet 12; Tax computation worksheet 13; Tax computation worksheet 14; Tax computation worksheet 15; Tax computation worksheet 2; Tax computation worksheet 3; Tax computation worksheet 4; Tax computation worksheet 5; Tax computation worksheet 6; Tax computation worksheet 7; Tax computation worksheet 8; Tax computation worksheet 9; Tax computation—New York adjusted gross income of more than $107,650 | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |
| ny_it270i | Form IT-270-I, Instructions for Form IT-270, New York City Income Tax Elimination Credit, for tax year 2025 (no printed edition line; address /pdf/2025/inc/, PDF metadata Title '... Tax Year 2025'); PDF modified 2025-10-27 | 1 | whole document | 66b713fa6ae58aafa2189310ed7d140b64c05d2c8bf2958a9651af7751ae15d5 | - | cc437e692bd1fcdbcc44f0e850e95f1cacee9a0e3285396d87e580ca559e082c |

## Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | ny_city_rs, ny_rs, ny_tcw, ny_tcw_first |
| named lines: f1040.line11a, f1040.line15, f1040.line1z, f1040.line27a, f1040.line2a, f1040.line2b, f1040.line3b, f1040.line4b, f1040.line5b, f1040.line6b, f1040.line7a, f1040.status | f1040 |
| named lines: person.sep_s3 | person |
| named lines: s1.line1, s1.line26, s1.line2a, s1.line3, s1.line7, s1.line9 | s1 |
| named lines: s2.line4 | s2 |
| shared page | ny_it2 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- model changed a published result type
- model changed a published result type
- ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]
- ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]
- ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]

## Lines

### C — Can you be claimed as a dependent on another taxpayer's federal return?
Status: **AGREE**

### H (count) — Number of dependents listed in item H
Status: **DISAGREE**

Project:

```json
{"collection": "dependent", "field": "dependent.one", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.lawful"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "household_member"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.qr_all_year"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.spouse_relative"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "in_law"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "parent_relative"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"args": [{"args": [{"param": "qc.age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"param": "qc.student_age_limit"}, {"input": "dependent.age"}], "test": "le"}, {"args": [{"const": true}, {"input": "dependent.student"}], "test": "ne"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "ne"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "ne"}], "test": "all"}, {"args": [{"input": "dependent.months"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "ne"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "dependent.supported"}], "test": "eq"}, {"args": [{"input": "dependent.gross_income"}, {"param": "qr.gross_income_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"args": [{"const": true}, {"input": "dependent.student"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.student_age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.younger"}], "test": "eq"}, {"args": [{"input": "dependent.age"}, {"param": "qc.age_limit"}], "test": "lt"}], "test": "all"}, {"args": [{"const": true}, {"input": "dependent.disabled"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "child"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling"}, {"input": "dependent.relationship"}], "test": "eq"}, {"args": [{"const": "sibling_descendant"}, {"input": "dependent.relationship"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"input": "dependent.joint_return"}], "test": "eq"}, {"args": [{"const": false}, {"input": "dependent.self_support"}], "test": "eq"}, {"args": [{"const": 6, "type": "Count"}, {"input": "dependent.months"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "dependent.canada_mexico"}], "test": "eq"}, {"args": [{"const": true}, {"input": "dependent.citizen"}], "test": "eq"}], "test": "any"}, {"args": [{"const": false}, {"ref": "sa.dependent"}], "test": "eq"}], "test": "all"}], "test": "any"}}
```

Second:

```json
{"cap": 100, "op": "percent_floor", "part": {"const": 0}, "whole": {"param": "ny.dependent_exemption"}}
```

Second transcription's note: Open: item H lists each dependent claimed (or entitled to be claimed) on federal Form 1040, but the closed interface supplies no dependent count (no dependent collection with a count field, no federal dependents line in the catalog) and no new input may be added. Encoded as a constant 0 (a percent_floor of zero, the only way to form a zero Count from the supplied parameters). This understates line 36 and the household credits for filers with dependents; the project must wire item H to the federal dependents.

Ruling: interface gap; the reviewer was not given the federal dependent fields (dependent.claimed, dependent.one), which the New York text never names, and encoded zero. The project counts the dependents for whom dependent.claimed is true, the federal qualifying-child and qualifying-relative tests, which is the class item H lists: IT-201-I p. 6, Item H, "Enter the required information for each dependent you claimed on federal Form 1040. Also enter the required information for any dependent you were entitled to claim on your federal return but chose not to". No New York fact reads differently; not a defect.

### 1 — Wages, salaries, tips, etc.
Status: **DISAGREE**

Project:

```json
{"of": {"ref": "f1040.line1z"}, "op": "round", "rule": "half_up", "unit": 100}
```

Second:

```json
{"ref": "f1040.line1z"}
```

Second transcription's note: Scope refusals for the whole return are placed on line 1: not a full-year resident (Form IT-203), a joint return with a spouse who was not also a full-year State and City resident (separate-sheet computations for lines 51 and 55), special accruals (IT-225 A-115/S-129), a decedent return, and special condition codes (including A6, which changes the household credit income).

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds each federal amount half-up to the dollar as it is entered on lines 1 to 18; the reply copies f1040.line1z in cents. Same reference otherwise. The reply's note puts the same whole-return scope refusals on line 1 as the project.

### 2 — Taxable interest income
Status: **DISAGREE**

Project:

```json
{"of": {"ref": "f1040.line2b"}, "op": "round", "rule": "half_up", "unit": 100}
```

Second:

```json
{"ref": "f1040.line2b"}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds each federal amount half-up to the dollar as it is entered on lines 1 to 18; the reply copies f1040.line2b in cents. Same reference otherwise.

### 3 — Ordinary dividends
Status: **DISAGREE**

Project:

```json
{"of": {"ref": "f1040.line3b"}, "op": "round", "rule": "half_up", "unit": 100}
```

Second:

```json
{"ref": "f1040.line3b"}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds each federal amount half-up to the dollar as it is entered on lines 1 to 18; the reply copies f1040.line3b in cents. Same reference otherwise.

### 4 — Taxable refunds, credits, or offsets of state and local income taxes (also enter on line 2
Status: **DISAGREE**

Project:

```json
{"of": {"ref": "s1.line1"}, "op": "round", "rule": "half_up", "unit": 100}
```

Second:

```json
{"ref": "s1.line1"}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds each federal amount half-up to the dollar as it is entered on lines 1 to 18; the reply copies s1.line1 in cents. Same reference otherwise.

### 5 — Alimony received
Status: **DISAGREE**

Project:

```json
{"of": {"ref": "s1.line2a"}, "op": "round", "rule": "half_up", "unit": 100}
```

Second:

```json
{"ref": "s1.line2a"}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds each federal amount half-up to the dollar as it is entered on lines 1 to 18; the reply copies s1.line2a in cents. Same reference otherwise.

### 6 — Business income or loss (submit a copy of federal Schedule C, Form 1040)
Status: **DISAGREE**

Project:

```json
{"of": {"ref": "s1.line3"}, "op": "round", "rule": "half_up", "unit": 100}
```

Second:

```json
{"ref": "s1.line3"}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds each federal amount half-up to the dollar as it is entered on lines 1 to 18; the reply copies s1.line3 in cents. Same reference otherwise.

### 7 — Capital gain or loss (if required, submit a copy of federal Schedule D, Form 1040)
Status: **DISAGREE**

Project:

```json
{"of": {"ref": "f1040.line7a"}, "op": "round", "rule": "half_up", "unit": 100}
```

Second:

```json
{"ref": "f1040.line7a"}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds each federal amount half-up to the dollar as it is entered on lines 1 to 18; the reply copies f1040.line7a in cents. Same reference otherwise.

### 8 — Other gains or losses (submit a copy of federal Form 4797)
Status: **AGREE**

### 9 — Taxable amount of IRA distributions
Status: **DISAGREE**

Project:

```json
{"of": {"ref": "f1040.line4b"}, "op": "round", "rule": "half_up", "unit": 100}
```

Second:

```json
{"ref": "f1040.line4b"}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds each federal amount half-up to the dollar as it is entered on lines 1 to 18; the reply copies f1040.line4b in cents. Same reference otherwise.

### 10 — Taxable amount of pensions and annuities
Status: **DISAGREE**

Project:

```json
{"of": {"ref": "f1040.line5b"}, "op": "round", "rule": "half_up", "unit": 100}
```

Second:

```json
{"ref": "f1040.line5b"}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds each federal amount half-up to the dollar as it is entered on lines 1 to 18; the reply copies f1040.line5b in cents. Same reference otherwise.

### 11 — Rental real estate, royalties, partnerships, S corporations, trusts, etc.
Status: **AGREE**

### 12 — Rental real estate included in line 11
Status: **AGREE**

### 13 — Farm income or loss
Status: **AGREE**

### 14 — Unemployment compensation
Status: **DISAGREE**

Project:

```json
{"of": {"ref": "s1.line7"}, "op": "round", "rule": "half_up", "unit": 100}
```

Second:

```json
{"ref": "s1.line7"}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds each federal amount half-up to the dollar as it is entered on lines 1 to 18; the reply copies s1.line7 in cents. Same reference otherwise.

### 15 — Taxable amount of Social Security benefits (also enter on line 27)
Status: **DISAGREE**

Project:

```json
{"of": {"ref": "f1040.line6b"}, "op": "round", "rule": "half_up", "unit": 100}
```

Second:

```json
{"ref": "f1040.line6b"}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds each federal amount half-up to the dollar as it is entered on lines 1 to 18; the reply copies f1040.line6b in cents. Same reference otherwise.

### 16 — Other income
Status: **DISAGREE**

Project:

```json
{"of": {"ref": "s1.line9"}, "op": "round", "rule": "half_up", "unit": 100}
```

Second:

```json
{"ref": "s1.line9"}
```

Second transcription's note: Other income is read as federal Schedule 1, line 9 (total other income), the only federal additional-income item not already on lines 4 to 15.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds each federal amount half-up to the dollar as it is entered on lines 1 to 18; the reply copies s1.line9 in cents. Same reference otherwise.

### 17 — Add lines 1 through 11 and 13 through 16
Status: **AGREE**

### 18 — Total federal adjustments to income
Status: **DISAGREE**

Project:

```json
{"of": {"ref": "s1.line26"}, "op": "round", "rule": "half_up", "unit": 100}
```

Second:

```json
{"ref": "s1.line26"}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds each federal amount half-up to the dollar as it is entered on lines 1 to 18; the reply copies s1.line26 in cents. Same reference otherwise.

### 19 — Federal adjusted gross income (subtract line 18 from line 17)
Status: **AGREE**

### (check) — Line 19 equals federal adjusted gross income rounded to the whole dollar
Status: **DISAGREE**

Project:

```json
{"args": [{"line": "19"}, {"of": {"ref": "f1040.line11a"}, "op": "round", "rule": "half_up", "unit": 100}], "test": "eq"}
```

Second:

```json
{"args": [{"line": "19"}, {"ref": "f1040.line11a"}], "test": "eq"}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The check compares line 19 with federal AGI rounded once to the dollar (decision C3; the line's own label); the reply compares it with unrounded federal AGI, which would fail whenever federal AGI has cents.

### 20 — Interest income on state and local bonds and obligations (but not those of NYS or its loca
Status: **AGREE**

### 21 — Public employee 414(h) retirement contributions from your wage and tax statements
Status: **AGREE**

### 22 — New York’s 529 college savings program distributions
Status: **AGREE**

### 23 — Other (Form IT-225, line 9)
Status: **AGREE**

### 24 — Add lines 19 through 23
Status: **AGREE**

### 25 — Taxable refunds, credits, or offsets of state and local income taxes (from line 4)
Status: **DISAGREE**

Project:

```json
{"const": 0}
```

Second:

```json
{"line": "4"}
```

Second transcription's note: Open: the form says line 25 is the line 4 amount, while the 2025 instructions speak only of the inflation refund check included in federal AGI. Read as the line 4 amount (as printed); a return that included an inflation refund check is refused, since where it was reported and its amount are not supplied.

Ruling: ambiguity; amb.ny.2025.line25 (owner decision B1): the form labels line 25 "(from line 4)" but IT-201-I p. 8 says only "If you received an inflation refund check from the Tax Department and included the check amount in the calculation of federal adjusted gross income reported on line 19, then enter that amount on line 25." The project refuses (ny_it201.gate.line25) when line 4 is more than zero or an inflation check was included, and is zero otherwise; wherever it is not refused the reply's line 4 is also zero.

### 26 — Pensions of NYS and local governments and the federal government
Status: **AGREE**

### 27 — Taxable amount of Social Security benefits (from line 15)
Status: **DISAGREE**

Project:

```json
{"line": "15"}
```

Second:

```json
{"expression": {"line": "15"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 28 — Interest income on U.S. government bonds
Status: **AGREE**

### 29 — Pension and annuity income exclusion
Status: **AGREE**

### 30 — New York’s 529 college savings program deduction/earnings
Status: **AGREE**

### 31 — Other (Form IT-225, line 18)
Status: **AGREE**

### 32 — Add lines 25 through 31
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "25"}, {"line": "26"}, {"line": "27"}, {"line": "28"}, {"line": "29"}, {"line": "30"}, {"line": "31"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"line": "25"}, {"line": "26"}, {"line": "27"}, {"line": "28"}, {"line": "29"}, {"line": "30"}, {"line": "31"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 33 — New York adjusted gross income (subtract line 32 from line 24)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "24"}, "op": "subtract", "take": {"line": "32"}}
```

Second:

```json
{"expression": {"from": {"line": "24"}, "op": "subtract", "take": {"line": "32"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (table) (ny_it201.std_deduction) — New York State standard deduction for the filing status
Status: **AGREE**

### (table) (ny_it201.std_deduction_dependent) — Single and you marked item C Yes
Status: **AGREE**

### 34 — Enter your standard deduction
Status: **AGREE**

### 35 — Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"line": "34"}}
```

Second:

```json
{"expression": {"from": {"line": "33"}, "op": "subtract_floor0", "take": {"line": "34"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 36 — Dependent exemption amount (multiply the number of dependents listed in item H by 1,000)
Status: **AGREE**

### 37 — Taxable income (subtract line 36 from line 35)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "35"}, "op": "subtract_floor0", "take": {"line": "36"}}
```

Second:

```json
{"expression": {"from": {"line": "35"}, "op": "subtract_floor0", "take": {"line": "36"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Second transcription's note: If line 36 is more than line 35 the instructions say to leave lines 37 and 38 blank; encoded as 0.

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 38 — Taxable income (from line 37 on page 2)
Status: **DISAGREE**

Project:

```json
{"line": "37"}
```

Second:

```json
{"expression": {"line": "37"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tax_table) — New York State tax from the 2025 New York State Tax Table
Status: **DISAGREE**

Project:

```json
{"key": {"line": "38"}, "op": "table_lookup", "status": {"ref": "f1040.status"}, "table": "ny_tax_table"}
```

Second:

```json
{"expression": {"key": {"line": "38"}, "op": "table_lookup", "status": {"ref": "f1040.status"}, "table": "ny_tax_table"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tax_schedule) — New York State tax from the New York State tax rate schedule
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"; ny_it201.tax_schedule: "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tax_low) — Tax for New York AGI of $107,650 or less: the Tax Table below $65,000 of taxable income, t
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"param": "ny.table.limit"}, {"line": "38"}], "test": "le"}, "then": {"line": "(39) (ny_it201.tax_schedule)"}}, {"guard": {"args": [{"line": "38"}, {"param": "ny.table.limit"}], "test": "lt"}, "then": {"line": "(39) (ny_it201.tax_table)"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"param": "ny.table.limit"}, {"line": "38"}], "test": "le"}, "then": {"line": "(39) (ny_it201.tax_schedule)"}}, {"guard": {"args": [{"line": "38"}, {"param": "ny.table.limit"}], "test": "lt"}, "then": {"line": "(39) (ny_it201.tax_table)"}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"; ny_it201.tax_schedule: "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.w1) — Tax computation worksheet 1
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"param": "ny.tcw.first.stop"}, {"line": "33"}], "test": "le"}, "then": {"amount": {"line": "38"}, "op": "multiply_rate", "rate": {"param": "ny.tcw.first.rate"}, "unit": 100}}, {"guard": {"args": [{"line": "33"}, {"param": "ny.tcw.first.stop"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"from": {"amount": {"line": "38"}, "op": "multiply_rate", "rate": {"param": "ny.tcw.first.rate"}, "unit": 100}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.first.start"}}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"param": "ny.tcw.first.stop"}, {"line": "33"}], "test": "le"}, "then": {"amount": {"line": "38"}, "op": "multiply_rate", "rate": {"param": "ny.tcw.first.rate"}, "unit": 100}}, {"guard": {"args": [{"line": "33"}, {"param": "ny.tcw.first.stop"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"from": {"amount": {"line": "38"}, "op": "multiply_rate", "rate": {"param": "ny.tcw.first.rate"}, "unit": 100}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.first.start"}}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}], "op": "sum"}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.w7) — Tax computation worksheet 7
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"param": "ny.tcw.first.stop"}, {"line": "33"}], "test": "le"}, "then": {"amount": {"line": "38"}, "op": "multiply_rate", "rate": {"param": "ny.tcw.first.rate6"}, "unit": 100}}, {"guard": {"args": [{"line": "33"}, {"param": "ny.tcw.first.stop"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"from": {"amount": {"line": "38"}, "op": "multiply_rate", "rate": {"param": "ny.tcw.first.rate6"}, "unit": 100}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.first.start"}}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"param": "ny.tcw.first.stop"}, {"line": "33"}], "test": "le"}, "then": {"amount": {"line": "38"}, "op": "multiply_rate", "rate": {"param": "ny.tcw.first.rate6"}, "unit": 100}}, {"guard": {"args": [{"line": "33"}, {"param": "ny.tcw.first.stop"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"from": {"amount": {"line": "38"}, "op": "multiply_rate", "rate": {"param": "ny.tcw.first.rate6"}, "unit": 100}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.first.start"}}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}], "op": "sum"}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.w12) — Tax computation worksheet 12
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"param": "ny.tcw.first.stop"}, {"line": "33"}], "test": "le"}, "then": {"amount": {"line": "38"}, "op": "multiply_rate", "rate": {"param": "ny.tcw.first.rate6"}, "unit": 100}}, {"guard": {"args": [{"line": "33"}, {"param": "ny.tcw.first.stop"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"from": {"amount": {"line": "38"}, "op": "multiply_rate", "rate": {"param": "ny.tcw.first.rate6"}, "unit": 100}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.first.start"}}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}], "op": "sum"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"param": "ny.tcw.first.stop"}, {"line": "33"}], "test": "le"}, "then": {"amount": {"line": "38"}, "op": "multiply_rate", "rate": {"param": "ny.tcw.first.rate6"}, "unit": 100}}, {"guard": {"args": [{"line": "33"}, {"param": "ny.tcw.first.stop"}], "test": "lt"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"from": {"amount": {"line": "38"}, "op": "multiply_rate", "rate": {"param": "ny.tcw.first.rate6"}, "unit": 100}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.first.start"}}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}], "op": "sum"}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.w2) — Tax computation worksheet 2
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.mfj.w2.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.mfj.w2.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.mfj.w2.recapture"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.mfj.w2.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.mfj.w2.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.mfj.w2.recapture"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.w3) — Tax computation worksheet 3
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.mfj.w3.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.mfj.w3.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.mfj.w3.recapture"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.mfj.w3.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.mfj.w3.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.mfj.w3.recapture"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.w4) — Tax computation worksheet 4
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.mfj.w4.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.mfj.w4.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.mfj.w4.recapture"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.mfj.w4.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.mfj.w4.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.mfj.w4.recapture"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.w5) — Tax computation worksheet 5
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.mfj.w5.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.mfj.w5.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.mfj.w5.recapture"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.mfj.w5.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.mfj.w5.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.mfj.w5.recapture"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.w8) — Tax computation worksheet 8
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.single.w8.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.single.w8.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.single.w8.recapture"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.single.w8.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.single.w8.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.single.w8.recapture"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.w9) — Tax computation worksheet 9
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.single.w9.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.single.w9.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.single.w9.recapture"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.single.w9.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.single.w9.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.single.w9.recapture"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.w10) — Tax computation worksheet 10
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.single.w10.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.single.w10.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.single.w10.recapture"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.single.w10.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.single.w10.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.single.w10.recapture"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.w13) — Tax computation worksheet 13
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.hoh.w13.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.hoh.w13.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.hoh.w13.recapture"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.hoh.w13.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.hoh.w13.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.hoh.w13.recapture"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.w14) — Tax computation worksheet 14
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.hoh.w14.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.hoh.w14.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.hoh.w14.recapture"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.hoh.w14.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.hoh.w14.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.hoh.w14.recapture"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.w15) — Tax computation worksheet 15
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.hoh.w15.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.hoh.w15.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.hoh.w15.recapture"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"line": "38"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "38"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, {"amount": {"amount": {"amount": {"param": "ny.tcw.hoh.w15.incremental"}, "count": {"param": "ny.hundred"}, "op": "multiply_count"}, "op": "prorate", "part": {"of": [{"from": {"line": "33"}, "op": "subtract_floor0", "take": {"param": "ny.tcw.hoh.w15.start"}}, {"param": "ny.tcw.phase"}], "op": "smaller_of"}, "places": 4, "whole": {"param": "ny.tcw.phase"}}, "op": "multiply_rate", "rate": {"param": "ny.hundredth"}, "unit": 100}, {"param": "ny.tcw.hoh.w15.recapture"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.top) — Tax computation worksheets 6, 11 and 16: multiply line 1 (taxable income) by 10.9%
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "38"}, "op": "multiply_rate", "rate": {"param": "ny.tcw.top_rate"}, "unit": 100}
```

Second:

```json
{"expression": {"amount": {"line": "38"}, "op": "multiply_rate", "rate": {"param": "ny.tcw.top_rate"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.mfj) — Married filing jointly and qualifying surviving spouse: the worksheet for the taxable inco
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.tcw.mfj.w1.ti_limit"}], "test": "le"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w1)"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.tcw.mfj.w2.ti_limit"}], "test": "le"}, {"args": [{"param": "ny.tcw.mfj.w1.ti_limit"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w2)"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.tcw.mfj.w3.ti_limit"}], "test": "le"}, {"args": [{"param": "ny.tcw.mfj.w2.ti_limit"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w3)"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.tcw.mfj.w4.ti_limit"}], "test": "le"}, {"args": [{"param": "ny.tcw.mfj.w3.ti_limit"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w4)"}}, {"guard": {"args": [{"param": "ny.tcw.mfj.w4.ti_limit"}, {"line": "38"}], "test": "lt"}, "then": {"line": "(39) (ny_it201.tcw.w5)"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.tcw.mfj.w2.ti_limit"}], "test": "le"}, {"args": [{"param": "ny.tcw.mfj.w1.ti_limit"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w2)"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.tcw.mfj.w3.ti_limit"}], "test": "le"}, {"args": [{"param": "ny.tcw.mfj.w2.ti_limit"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w3)"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.tcw.mfj.w4.ti_limit"}], "test": "le"}, {"args": [{"param": "ny.tcw.mfj.w3.ti_limit"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w4)"}}, {"guard": {"args": [{"line": "38"}, {"param": "ny.tcw.mfj.w1.ti_limit"}], "test": "le"}, "then": {"line": "(39) (ny_it201.tcw.w1)"}}, {"guard": {"args": [{"param": "ny.tcw.mfj.w4.ti_limit"}, {"line": "38"}], "test": "lt"}, "then": {"line": "(39) (ny_it201.tcw.w5)"}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Second transcription's note: Each worksheet's line 33 condition (more than the worksheet's start) is implied by its taxable-income range, since line 38 cannot exceed line 33; the worksheets are selected by taxable income alone.

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.single) — Single and married filing separately: the worksheet for the taxable income
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.tcw.single.w1.ti_limit"}], "test": "le"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w7)"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.tcw.single.w8.ti_limit"}], "test": "le"}, {"args": [{"param": "ny.tcw.single.w1.ti_limit"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w8)"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.tcw.single.w9.ti_limit"}], "test": "le"}, {"args": [{"param": "ny.tcw.single.w8.ti_limit"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w9)"}}, {"guard": {"args": [{"param": "ny.tcw.single.w9.ti_limit"}, {"line": "38"}], "test": "lt"}, "then": {"line": "(39) (ny_it201.tcw.w10)"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.tcw.single.w8.ti_limit"}], "test": "le"}, {"args": [{"param": "ny.tcw.single.w1.ti_limit"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w8)"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.tcw.single.w9.ti_limit"}], "test": "le"}, {"args": [{"param": "ny.tcw.single.w8.ti_limit"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w9)"}}, {"guard": {"args": [{"line": "38"}, {"param": "ny.tcw.single.w1.ti_limit"}], "test": "le"}, "then": {"line": "(39) (ny_it201.tcw.w7)"}}, {"guard": {"args": [{"param": "ny.tcw.single.w9.ti_limit"}, {"line": "38"}], "test": "lt"}, "then": {"line": "(39) (ny_it201.tcw.w10)"}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.hoh) — Head of household: the worksheet for the taxable income
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "38"}], "test": "le"}, {"args": [{"line": "38"}, {"param": "ny.tcw.hoh.w1.ti_limit"}], "test": "le"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w12)"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.tcw.hoh.w13.ti_limit"}], "test": "le"}, {"args": [{"param": "ny.tcw.hoh.w1.ti_limit"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w13)"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.tcw.hoh.w14.ti_limit"}], "test": "le"}, {"args": [{"param": "ny.tcw.hoh.w13.ti_limit"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w14)"}}, {"guard": {"args": [{"param": "ny.tcw.hoh.w14.ti_limit"}, {"line": "38"}], "test": "lt"}, "then": {"line": "(39) (ny_it201.tcw.w15)"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.tcw.hoh.w13.ti_limit"}], "test": "le"}, {"args": [{"param": "ny.tcw.hoh.w1.ti_limit"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w13)"}}, {"guard": {"args": [{"args": [{"line": "38"}, {"param": "ny.tcw.hoh.w14.ti_limit"}], "test": "le"}, {"args": [{"param": "ny.tcw.hoh.w13.ti_limit"}, {"line": "38"}], "test": "lt"}], "test": "all"}, "then": {"line": "(39) (ny_it201.tcw.w14)"}}, {"guard": {"args": [{"line": "38"}, {"param": "ny.tcw.hoh.w1.ti_limit"}], "test": "le"}, "then": {"line": "(39) (ny_it201.tcw.w12)"}}, {"guard": {"args": [{"param": "ny.tcw.hoh.w14.ti_limit"}, {"line": "38"}], "test": "lt"}, "then": {"line": "(39) (ny_it201.tcw.w15)"}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tcw.by_status) — The tax computation worksheet for the filing status
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"line": "(39) (ny_it201.tcw.mfj)"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"line": "(39) (ny_it201.tcw.single)"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"line": "(39) (ny_it201.tcw.hoh)"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"line": "(39) (ny_it201.tcw.mfj)"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"line": "(39) (ny_it201.tcw.single)"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"line": "(39) (ny_it201.tcw.hoh)"}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (39) (ny_it201.tax_high) — Tax for New York AGI of more than $107,650: the tax computation worksheets
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "33"}, {"param": "ny.tcw.agi_top"}], "test": "le"}, "then": {"line": "(39) (ny_it201.tcw.by_status)"}}, {"guard": {"args": [{"param": "ny.tcw.agi_top"}, {"line": "33"}], "test": "lt"}, "then": {"line": "(39) (ny_it201.tcw.top)"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"line": "33"}, {"param": "ny.tcw.agi_top"}], "test": "le"}, "then": {"line": "(39) (ny_it201.tcw.by_status)"}}, {"guard": {"args": [{"param": "ny.tcw.agi_top"}, {"line": "33"}], "test": "lt"}, "then": {"line": "(39) (ny_it201.tcw.top)"}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 39 — NYS tax on line 38 amount
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "33"}, {"param": "ny.table.agi_limit"}], "test": "le"}, "then": {"line": "(39) (ny_it201.tax_low)"}}, {"guard": {"args": [{"param": "ny.table.agi_limit"}, {"line": "33"}], "test": "lt"}, "then": {"line": "(39) (ny_it201.tax_high)"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"line": "33"}, {"param": "ny.table.agi_limit"}], "test": "le"}, "then": {"line": "(39) (ny_it201.tax_low)"}}, {"guard": {"args": [{"param": "ny.table.agi_limit"}, {"line": "33"}], "test": "lt"}, "then": {"line": "(39) (ny_it201.tax_high)"}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"; ny_it201.tax_schedule: "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (Note 1) — Federal adjusted gross income for the household credit tables (line 19; a negative amount
Status: **AGREE**

### (column) — The number of dependents listed in item H, plus one for you (and one for your spouse if ma
Status: **AGREE**

### (table 2, column 1) — New York State household credit table 2, column 1
Status: **AGREE**

### (table 5, column 1) — New York City household credit table 5, column 1
Status: **AGREE**

### (table 2, column 2) — New York State household credit table 2, column 2
Status: **AGREE**

### (table 5, column 2) — New York City household credit table 5, column 2
Status: **AGREE**

### (table 2, column 3) — New York State household credit table 2, column 3
Status: **AGREE**

### (table 5, column 3) — New York City household credit table 5, column 3
Status: **AGREE**

### (table 2, column 4) — New York State household credit table 2, column 4
Status: **AGREE**

### (table 5, column 4) — New York City household credit table 5, column 4
Status: **AGREE**

### (table 2, column 5) — New York State household credit table 2, column 5
Status: **AGREE**

### (table 5, column 5) — New York City household credit table 5, column 5
Status: **AGREE**

### (table 2, column 6) — New York State household credit table 2, column 6
Status: **AGREE**

### (table 5, column 6) — New York City household credit table 5, column 6
Status: **AGREE**

### (table 2, column 7) — New York State household credit table 2, column 7
Status: **AGREE**

### (table 5, column 7) — New York City household credit table 5, column 7
Status: **AGREE**

### (table 2) — New York State household credit table 2 for the number of people (column 7 for 7 or more)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"line": "(column)"}], "test": "le"}, {"args": [{"line": "(column)"}, {"const": 1, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"line": "(table 2, column 1)"}}, {"guard": {"args": [{"args": [{"line": "(column)"}, {"const": 2, "type": "Count"}], "test": "le"}, {"args": [{"const": 1, "type": "Count"}, {"line": "(column)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(table 2, column 2)"}}, {"guard": {"args": [{"args": [{"line": "(column)"}, {"const": 3, "type": "Count"}], "test": "le"}, {"args": [{"const": 2, "type": "Count"}, {"line": "(column)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(table 2, column 3)"}}, {"guard": {"args": [{"args": [{"line": "(column)"}, {"const": 4, "type": "Count"}], "test": "le"}, {"args": [{"const": 3, "type": "Count"}, {"line": "(column)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(table 2, column 4)"}}, {"guard": {"args": [{"args": [{"line": "(column)"}, {"const": 5, "type": "Count"}], "test": "le"}, {"args": [{"const": 4, "type": "Count"}, {"line": "(column)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(table 2, column 5)"}}, {"guard": {"args": [{"args": [{"line": "(column)"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": 5, "type": "Count"}, {"line": "(column)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(table 2, column 6)"}}, {"guard": {"args": [{"const": 6, "type": "Count"}, {"line": "(column)"}], "test": "lt"}, "then": {"line": "(table 2, column 7)"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": 2, "type": "Count"}, {"line": "(column)"}], "test": "eq"}, "then": {"line": "(table 2, column 2)"}}, {"guard": {"args": [{"const": 3, "type": "Count"}, {"line": "(column)"}], "test": "eq"}, "then": {"line": "(table 2, column 3)"}}, {"guard": {"args": [{"const": 4, "type": "Count"}, {"line": "(column)"}], "test": "eq"}, "then": {"line": "(table 2, column 4)"}}, {"guard": {"args": [{"const": 5, "type": "Count"}, {"line": "(column)"}], "test": "eq"}, "then": {"line": "(table 2, column 5)"}}, {"guard": {"args": [{"const": 6, "type": "Count"}, {"line": "(column)"}], "test": "eq"}, "then": {"line": "(table 2, column 6)"}}, {"guard": {"args": [{"const": 7, "type": "Count"}, {"line": "(column)"}], "test": "eq"}, "then": {"line": "(table 2, column 7)"}}, {"guard": {"args": [{"line": "(column)"}, {"const": 1, "type": "Count"}], "test": "le"}, "then": {"line": "(table 2, column 1)"}}, {"guard": {"args": [{"const": 7, "type": "Count"}, {"line": "(column)"}], "test": "lt"}, "then": {"from": {"of": [{"line": "(table 2, column 7)"}, {"from": {"amount": {"from": {"line": "(table 2, column 7)"}, "op": "subtract", "take": {"line": "(table 2, column 6)"}}, "count": {"line": "(column)"}, "op": "multiply_count"}, "op": "subtract", "take": {"amount": {"from": {"line": "(table 2, column 7)"}, "op": "subtract", "take": {"line": "(table 2, column 6)"}}, "count": {"param": "ny.hh.max_people"}, "op": "multiply_count"}}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}
```

Ruling: scope; for 1 to 7 people both pick the same column. Over 7 people the reply extrapolates column 7 by the column 6 to 7 step, which equals the printed over-7 column in every row (IT-201-I pp. 13 and 14, "Note 3 For each individual over 7, add the amount in this column to the column 7 amount."); the project instead refuses that case wherever a credit is allowed (state, refused on line 40 by ny_it201.gate.hh_state_over7), a refusal of the author's choosing, not a wrong amount.

### (table 5) — New York City household credit table 5 for the number of people (column 7 for 7 or more)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"line": "(column)"}], "test": "le"}, {"args": [{"line": "(column)"}, {"const": 1, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"line": "(table 5, column 1)"}}, {"guard": {"args": [{"args": [{"line": "(column)"}, {"const": 2, "type": "Count"}], "test": "le"}, {"args": [{"const": 1, "type": "Count"}, {"line": "(column)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(table 5, column 2)"}}, {"guard": {"args": [{"args": [{"line": "(column)"}, {"const": 3, "type": "Count"}], "test": "le"}, {"args": [{"const": 2, "type": "Count"}, {"line": "(column)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(table 5, column 3)"}}, {"guard": {"args": [{"args": [{"line": "(column)"}, {"const": 4, "type": "Count"}], "test": "le"}, {"args": [{"const": 3, "type": "Count"}, {"line": "(column)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(table 5, column 4)"}}, {"guard": {"args": [{"args": [{"line": "(column)"}, {"const": 5, "type": "Count"}], "test": "le"}, {"args": [{"const": 4, "type": "Count"}, {"line": "(column)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(table 5, column 5)"}}, {"guard": {"args": [{"args": [{"line": "(column)"}, {"const": 6, "type": "Count"}], "test": "le"}, {"args": [{"const": 5, "type": "Count"}, {"line": "(column)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(table 5, column 6)"}}, {"guard": {"args": [{"const": 6, "type": "Count"}, {"line": "(column)"}], "test": "lt"}, "then": {"line": "(table 5, column 7)"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": 2, "type": "Count"}, {"line": "(column)"}], "test": "eq"}, "then": {"line": "(table 5, column 2)"}}, {"guard": {"args": [{"const": 3, "type": "Count"}, {"line": "(column)"}], "test": "eq"}, "then": {"line": "(table 5, column 3)"}}, {"guard": {"args": [{"const": 4, "type": "Count"}, {"line": "(column)"}], "test": "eq"}, "then": {"line": "(table 5, column 4)"}}, {"guard": {"args": [{"const": 5, "type": "Count"}, {"line": "(column)"}], "test": "eq"}, "then": {"line": "(table 5, column 5)"}}, {"guard": {"args": [{"const": 6, "type": "Count"}, {"line": "(column)"}], "test": "eq"}, "then": {"line": "(table 5, column 6)"}}, {"guard": {"args": [{"const": 7, "type": "Count"}, {"line": "(column)"}], "test": "eq"}, "then": {"line": "(table 5, column 7)"}}, {"guard": {"args": [{"line": "(column)"}, {"const": 1, "type": "Count"}], "test": "le"}, "then": {"line": "(table 5, column 1)"}}, {"guard": {"args": [{"const": 7, "type": "Count"}, {"line": "(column)"}], "test": "lt"}, "then": {"from": {"of": [{"line": "(table 5, column 7)"}, {"from": {"amount": {"from": {"line": "(table 5, column 7)"}, "op": "subtract", "take": {"line": "(table 5, column 6)"}}, "count": {"line": "(column)"}, "op": "multiply_count"}, "op": "subtract", "take": {"amount": {"from": {"line": "(table 5, column 7)"}, "op": "subtract", "take": {"line": "(table 5, column 6)"}}, "count": {"param": "ny.hh.max_people"}, "op": "multiply_count"}}], "op": "sum"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}
```

Ruling: scope; for 1 to 7 people both pick the same column. Over 7 people the reply extrapolates column 7 by the column 6 to 7 step, which equals the printed over-7 column in every row (IT-201-I pp. 13 and 14, "Note 3 For each individual over 7, add the amount in this column to the column 7 amount."); the project instead refuses that case wherever a credit is allowed (city, refused on line 48 by ny_it201.gate.hh_city_over7), a refusal of the author's choosing, not a wrong amount.

### (table 1) — New York State household credit table 1 (single)
Status: **AGREE**

### (table 4) — New York City household credit table 4 (single)
Status: **AGREE**

### (40) — The state household credit table for the filing status
Status: **AGREE**

### (48) — The city household credit table for the filing status
Status: **AGREE**

### 40 — NYS household credit
Status: **AGREE**

### 41 — Resident credit
Status: **AGREE**

### 42 — Other NYS nonrefundable credits (Form IT-201-ATT, line 7)
Status: **AGREE**

### 43 — Add lines 40, 41, and 42
Status: **AGREE**

### 44 — Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "39"}, "op": "subtract_floor0", "take": {"line": "43"}}
```

Second:

```json
{"expression": {"from": {"line": "39"}, "op": "subtract_floor0", "take": {"line": "43"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"; ny_it201.tax_schedule: "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 45 — Net other NYS taxes (Form IT-201-ATT, line 30)
Status: **AGREE**

### 46 — Total New York State taxes (add lines 44 and 45)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "44"}, {"line": "45"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"line": "44"}, {"line": "45"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"; ny_it201.tax_schedule: "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 47 — NYC taxable income
Status: **DISAGREE**

Project:

```json
{"line": "38"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"const": true}, {"line": "(question) (ny_it201.ask.city_resident)"}], "test": "eq"}, "then": {"line": "38"}}, {"guard": {"args": [{"const": true}, {"line": "(question) (ny_it201.ask.city_resident)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Second transcription's note: Without a Charitable Gifts Trust Fund itemized deduction (itemizers are refused at line 34), line 47 is the line 38 amount. A filer who was not a full-year NYC resident enters nothing; the interface does not distinguish a part-year NYC resident (Form IT-360.1, line 50) from a nonresident, so both are treated as nonresidents.

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (47a) (ny_it201.city_tax_table) — New York City resident tax from the 2025 New York City Tax Table
Status: **DISAGREE**

Project:

```json
{"key": {"line": "47"}, "op": "table_lookup", "status": {"ref": "f1040.status"}, "table": "ny_city_tax_table"}
```

Second:

```json
{"expression": {"key": {"line": "47"}, "op": "table_lookup", "status": {"ref": "f1040.status"}, "table": "ny_city_tax_table"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (47a) (ny_it201.city_tax_schedule) — New York City resident tax from the New York City tax rate schedule
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "47"}], "test": "le"}, {"args": [{"line": "47"}, {"param": "ny.city.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.city.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "47"}, {"param": "ny.city.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.city.mfj.b1.upper"}, {"line": "47"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b2.rate"}, "unit": 100}, {"param": "ny.city.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "47"}, {"param": "ny.city.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.city.mfj.b2.upper"}, {"line": "47"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b3.rate"}, "unit": 100}, {"param": "ny.city.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.city.mfj.b3.upper"}, {"line": "47"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b4.rate"}, "unit": 100}, {"param": "ny.city.mfj.b4.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "47"}], "test": "le"}, {"args": [{"line": "47"}, {"param": "ny.city.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.city.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "47"}, {"param": "ny.city.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.city.single.b1.upper"}, {"line": "47"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b2.rate"}, "unit": 100}, {"param": "ny.city.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "47"}, {"param": "ny.city.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.city.single.b2.upper"}, {"line": "47"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b3.rate"}, "unit": 100}, {"param": "ny.city.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.city.single.b3.upper"}, {"line": "47"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b4.rate"}, "unit": 100}, {"param": "ny.city.single.b4.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "47"}], "test": "le"}, {"args": [{"line": "47"}, {"param": "ny.city.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.city.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"line": "47"}, {"param": "ny.city.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.city.hoh.b1.upper"}, {"line": "47"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b2.rate"}, "unit": 100}, {"param": "ny.city.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "47"}, {"param": "ny.city.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.city.hoh.b2.upper"}, {"line": "47"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b3.rate"}, "unit": 100}, {"param": "ny.city.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.city.hoh.b3.upper"}, {"line": "47"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b4.rate"}, "unit": 100}, {"param": "ny.city.hoh.b4.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "47"}, {"param": "ny.city.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.city.mfj.b1.upper"}, {"line": "47"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b2.rate"}}, {"param": "ny.city.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "47"}, {"param": "ny.city.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.city.mfj.b2.upper"}, {"line": "47"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b3.rate"}}, {"param": "ny.city.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"line": "47"}, {"param": "ny.city.mfj.b1.upper"}], "test": "le"}, "then": {"amount": {"line": "47"}, "op": "multiply_rate", "rate": {"param": "ny.city.b1.rate"}}}, {"guard": {"args": [{"param": "ny.city.mfj.b3.upper"}, {"line": "47"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b4.rate"}}, {"param": "ny.city.mfj.b4.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"ref": "f1040.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "47"}, {"param": "ny.city.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.city.single.b1.upper"}, {"line": "47"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b2.rate"}}, {"param": "ny.city.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "47"}, {"param": "ny.city.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.city.single.b2.upper"}, {"line": "47"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b3.rate"}}, {"param": "ny.city.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"line": "47"}, {"param": "ny.city.single.b1.upper"}], "test": "le"}, "then": {"amount": {"line": "47"}, "op": "multiply_rate", "rate": {"param": "ny.city.b1.rate"}}}, {"guard": {"args": [{"param": "ny.city.single.b3.upper"}, {"line": "47"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b4.rate"}}, {"param": "ny.city.single.b4.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"ref": "f1040.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"line": "47"}, {"param": "ny.city.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.city.hoh.b1.upper"}, {"line": "47"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b2.rate"}}, {"param": "ny.city.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"line": "47"}, {"param": "ny.city.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.city.hoh.b2.upper"}, {"line": "47"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b3.rate"}}, {"param": "ny.city.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"line": "47"}, {"param": "ny.city.hoh.b1.upper"}], "test": "le"}, "then": {"amount": {"line": "47"}, "op": "multiply_rate", "rate": {"param": "ny.city.b1.rate"}}}, {"guard": {"args": [{"param": "ny.city.hoh.b3.upper"}, {"line": "47"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.city.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b4.rate"}}, {"param": "ny.city.hoh.b4.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Second transcription's note: The NYC rate schedule itself is not in the supplied pages; it is built from the supplied ny.city band parameters as base plus rate times the excess over the band's 'over' amount, each product rounded half-up to the cent (the form takes whole dollars; no further rounding is stated).

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 47a — NYC resident tax on line 47 amount
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"param": "ny.city.table.limit"}, {"line": "47"}], "test": "le"}, "then": {"line": "(47a) (ny_it201.city_tax_schedule)"}}, {"guard": {"args": [{"line": "47"}, {"param": "ny.city.table.limit"}], "test": "lt"}, "then": {"line": "(47a) (ny_it201.city_tax_table)"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"line": "(question) (ny_it201.ask.city_resident)"}], "test": "eq"}, {"args": [{"param": "ny.city.table.limit"}, {"line": "47"}], "test": "le"}], "test": "all"}, "then": {"line": "(47a) (ny_it201.city_tax_schedule)"}}, {"guard": {"args": [{"args": [{"const": true}, {"line": "(question) (ny_it201.ask.city_resident)"}], "test": "eq"}, {"args": [{"line": "47"}, {"param": "ny.city.table.limit"}], "test": "lt"}], "test": "all"}, "then": {"line": "(47a) (ny_it201.city_tax_table)"}}, {"guard": {"args": [{"const": true}, {"line": "(question) (ny_it201.ask.city_resident)"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 48 — NYC household credit
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "C"}], "test": "eq"}, "then": {"line": "(48)"}}, {"guard": {"args": [{"const": true}, {"line": "C"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"line": "C"}], "test": "eq"}, {"args": [{"const": true}, {"line": "(question) (ny_it201.ask.city_resident)"}], "test": "eq"}], "test": "all"}, "then": {"line": "(48)"}}, {"guard": {"args": [{"args": [{"const": true}, {"line": "C"}], "test": "eq"}, {"args": [{"const": true}, {"line": "(question) (ny_it201.ask.city_resident)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; the reply adds a full-year City resident guard. The project refuses a part-year City resident for the whole return (ny_it201.gate.part_year_city on line 1; IT-201-I p. 14, "If you were a New York City resident for only part of 2025, complete Form IT-360.1"), so on every computed return the guard is true and the two agree (p. 13, "If you marked the Yes box at item C on the front of Form IT-201, you do not qualify for this credit and should go to line 49.").

### 49 — Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "47a"}, "op": "subtract_floor0", "take": {"line": "48"}}
```

Second:

```json
{"expression": {"from": {"line": "47a"}, "op": "subtract_floor0", "take": {"line": "48"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 50 — Part-year NYC resident tax (Form IT-360.1)
Status: **AGREE**

### 51 — Other NYC taxes (Form IT-201-ATT, line 34)
Status: **AGREE**

### 52 — Add lines 49, 50, and 51
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "49"}, {"line": "50"}, {"line": "51"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"line": "49"}, {"line": "50"}, {"line": "51"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 53 — NYC nonrefundable credits (Form IT-201-ATT, line 10)
Status: **AGREE**

### 54 — Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "52"}, "op": "subtract_floor0", "take": {"line": "53"}}
```

Second:

```json
{"expression": {"from": {"line": "52"}, "op": "subtract_floor0", "take": {"line": "53"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 54a — MCTMT net earnings base for Zone 1
Status: **AGREE**

### 54b — MCTMT net earnings base for Zone 2
Status: **AGREE**

### 54c — MCTMT for Zone 1
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "54a"}, "op": "multiply_rate", "rate": {"param": "ny.mctmt.zone1"}, "unit": 100}
```

Second:

```json
{"amount": {"line": "54a"}, "op": "multiply_rate", "rate": {"param": "ny.mctmt.zone1"}}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once to the dollar; the reply keeps cents. The MCTMT is refused when it applies (decision B5, ny_it201.gate.mctmt), and lines 54a and 54b are 0 on every computed return and both give 0.

### 54d — MCTMT for Zone 2
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "54b"}, "op": "multiply_rate", "rate": {"param": "ny.mctmt.zone2"}, "unit": 100}
```

Second:

```json
{"amount": {"line": "54b"}, "op": "multiply_rate", "rate": {"param": "ny.mctmt.zone2"}}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once to the dollar; the reply keeps cents. The MCTMT is refused when it applies (decision B5, ny_it201.gate.mctmt), and lines 54a and 54b are 0 on every computed return and both give 0.

### 54e — Total MCTMT (add lines 54c and 54d)
Status: **AGREE**

### 55 — Yonkers resident income tax surcharge
Status: **AGREE**

### 56 — Yonkers nonresident earnings tax (Form Y-203)
Status: **AGREE**

### 57 — Part-year Yonkers resident income tax surcharge (Form IT-360.1)
Status: **AGREE**

### 58 — Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 54e through
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "54"}, {"line": "54e"}, {"line": "55"}, {"line": "56"}, {"line": "57"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"line": "54"}, {"line": "54e"}, {"line": "55"}, {"line": "56"}, {"line": "57"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (chart) (ny_it201.sut.b1) — Sales and use tax chart, row 1
Status: **AGREE**

### (chart) (ny_it201.sut.b2) — Sales and use tax chart, row 2
Status: **AGREE**

### (chart) (ny_it201.sut.b3) — Sales and use tax chart, row 3
Status: **AGREE**

### (chart) (ny_it201.sut.b4) — Sales and use tax chart, row 4
Status: **AGREE**

### (chart) (ny_it201.sut.b5) — Sales and use tax chart, row 5
Status: **AGREE**

### (chart) (ny_it201.sut.b6) — Sales and use tax chart, row 6
Status: **AGREE**

### (chart) (ny_it201.sut.b7) — Sales and use tax chart, row 7
Status: **AGREE**

### (chart) (ny_it201.sut.top_product) — 0.0175% (0.000175) of income
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "(Note 1)"}, "op": "multiply_rate", "rate": {"param": "ny.sut.top_rate"}, "unit": 100}
```

Second:

```json
{"amount": {"from": {"line": "19"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.sut.top_rate"}}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The reply rounds 0.0175% of income to the cent, the register once to the dollar. Its floor of line 19 at zero equals the project's (Note 1) helper (line 19 floored at zero) on this row, which applies only above $200,000.

### (chart) (ny_it201.sut.cap) — $125
Status: **AGREE**

### (chart) (ny_it201.sut.top) — 0.0175% (0.000175) of income, or $125, whichever amount is smaller
Status: **AGREE**

### (chart) (ny_it201.sut.chart) — The sales and use tax chart amount for federal adjusted gross income (line 19; zero or a n
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"line": "(Note 1)"}], "test": "le"}, {"args": [{"line": "(Note 1)"}, {"param": "ny.sut.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"line": "(chart) (ny_it201.sut.b1)"}}, {"guard": {"args": [{"args": [{"line": "(Note 1)"}, {"param": "ny.sut.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.sut.b1.upper"}, {"line": "(Note 1)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(chart) (ny_it201.sut.b2)"}}, {"guard": {"args": [{"args": [{"line": "(Note 1)"}, {"param": "ny.sut.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.sut.b2.upper"}, {"line": "(Note 1)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(chart) (ny_it201.sut.b3)"}}, {"guard": {"args": [{"args": [{"line": "(Note 1)"}, {"param": "ny.sut.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.sut.b3.upper"}, {"line": "(Note 1)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(chart) (ny_it201.sut.b4)"}}, {"guard": {"args": [{"args": [{"line": "(Note 1)"}, {"param": "ny.sut.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.sut.b4.upper"}, {"line": "(Note 1)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(chart) (ny_it201.sut.b5)"}}, {"guard": {"args": [{"args": [{"line": "(Note 1)"}, {"param": "ny.sut.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.sut.b5.upper"}, {"line": "(Note 1)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(chart) (ny_it201.sut.b6)"}}, {"guard": {"args": [{"args": [{"line": "(Note 1)"}, {"param": "ny.sut.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.sut.b6.upper"}, {"line": "(Note 1)"}], "test": "lt"}], "test": "all"}, "then": {"line": "(chart) (ny_it201.sut.b7)"}}, {"guard": {"args": [{"param": "ny.sut.b7.upper"}, {"line": "(Note 1)"}], "test": "lt"}, "then": {"line": "(chart) (ny_it201.sut.top)"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"line": "19"}, {"param": "ny.sut.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.sut.b1.upper"}, {"line": "19"}], "test": "lt"}], "test": "all"}, "then": {"line": "(chart) (ny_it201.sut.b2)"}}, {"guard": {"args": [{"args": [{"line": "19"}, {"param": "ny.sut.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.sut.b2.upper"}, {"line": "19"}], "test": "lt"}], "test": "all"}, "then": {"line": "(chart) (ny_it201.sut.b3)"}}, {"guard": {"args": [{"args": [{"line": "19"}, {"param": "ny.sut.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.sut.b3.upper"}, {"line": "19"}], "test": "lt"}], "test": "all"}, "then": {"line": "(chart) (ny_it201.sut.b4)"}}, {"guard": {"args": [{"args": [{"line": "19"}, {"param": "ny.sut.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.sut.b4.upper"}, {"line": "19"}], "test": "lt"}], "test": "all"}, "then": {"line": "(chart) (ny_it201.sut.b5)"}}, {"guard": {"args": [{"args": [{"line": "19"}, {"param": "ny.sut.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.sut.b5.upper"}, {"line": "19"}], "test": "lt"}], "test": "all"}, "then": {"line": "(chart) (ny_it201.sut.b6)"}}, {"guard": {"args": [{"args": [{"line": "19"}, {"param": "ny.sut.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.sut.b6.upper"}, {"line": "19"}], "test": "lt"}], "test": "all"}, "then": {"line": "(chart) (ny_it201.sut.b7)"}}, {"guard": {"args": [{"line": "19"}, {"param": "ny.sut.b1.upper"}], "test": "le"}, "then": {"line": "(chart) (ny_it201.sut.b1)"}}, {"guard": {"args": [{"param": "ny.sut.b7.upper"}, {"line": "19"}], "test": "lt"}, "then": {"line": "(chart) (ny_it201.sut.top)"}}], "op": "choose"}
```

Second transcription's note: Bands are whole-dollar ranges ('$15,001 - $30,000'); each is read as over the previous upper amount and not over its own. The 0.0175% product is rounded half-up to the cent (no rounding is stated). Form ST-141 cases and the part-year abode proration (months over 12) are refused.

Ruling: representation; IT-201-I-html, Sales and use tax chart, "If your federal adjusted gross income (line 19) is:" ... "up to $15,000*" ... "*This may be any amount up to $15,000, including 0 or a negative amount." The project selects on line 19 floored at zero ((Note 1)), the reply on line 19 with the first row reached by "not over $15,000"; a zero or negative AGI falls in the first row either way, and the other rows are the same.

### 59 — Sales or use tax (do not leave blank)
Status: **AGREE**

### 60 — Voluntary contributions (Form IT-227, Part 2, line 1)
Status: **AGREE**

### 61 — Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and voluntary
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "46"}, {"line": "58"}, {"line": "59"}, {"line": "60"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"line": "46"}, {"line": "58"}, {"line": "59"}, {"line": "60"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"; ny_it201.tax_schedule: "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 62 — Enter amount from line 61
Status: **DISAGREE**

Project:

```json
{"line": "61"}
```

Second:

```json
{"expression": {"line": "61"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"; ny_it201.tax_schedule: "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 63 — Empire State child credit
Status: **AGREE**

### 64 — NYS/NYC child and dependent care credit
Status: **AGREE**

### 65 — NYS earned income credit (EIC)
Status: **AGREE**

### 66 — NYS noncustodial parent EIC
Status: **AGREE**

### 67 — Real property tax credit
Status: **AGREE**

### 68 — College tuition credit
Status: **AGREE**

### (69) (ny_it201.stc_income) — Income for the school tax credit: federal AGI (line 19) minus IRA distributions included i
Status: **AGREE**

### (69) (ny_it201.stc_fixed_amount) — Table 1 - Full-year New York City residents: the credit for the filing status
Status: **AGREE**

### 69 — NYC school tax credit (fixed amount)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"line": "C"}], "test": "eq"}, {"args": [{"line": "(69) (ny_it201.stc_income)"}, {"param": "ny.stc.fixed.limit"}], "test": "le"}], "test": "all"}, "then": {"line": "(69) (ny_it201.stc_fixed_amount)"}}, {"guard": {"args": [{"args": [{"param": "ny.stc.fixed.limit"}, {"line": "(69) (ny_it201.stc_income)"}], "test": "lt"}, {"args": [{"const": false}, {"line": "C"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"line": "C"}], "test": "eq"}, {"args": [{"const": true}, {"line": "(question) (ny_it201.ask.city_resident)"}], "test": "eq"}, {"args": [{"line": "(69) (ny_it201.stc_income)"}, {"param": "ny.stc.fixed.limit"}], "test": "le"}], "test": "all"}, "then": {"line": "(69) (ny_it201.stc_fixed_amount)"}}, {"guard": {"args": [{"args": [{"param": "ny.stc.fixed.limit"}, {"line": "(69) (ny_it201.stc_income)"}], "test": "lt"}, {"args": [{"const": false}, {"line": "C"}], "test": "ne"}, {"args": [{"const": true}, {"line": "(question) (ny_it201.ask.city_resident)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; as line 48: the reply's full-year City resident guard is always true on a computed return (ny_it201.gate.part_year_city refuses the rest); the item C and income tests are the same.

### (69a) (ny_it201.stc_rr_low) — 0.171% of taxable income
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "47"}, "op": "multiply_rate", "rate": {"param": "ny.stc.rr.low_rate"}, "unit": 100}
```

Second:

```json
{"expression": {"amount": {"line": "47"}, "op": "multiply_rate", "rate": {"param": "ny.stc.rr.low_rate"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (69a) (ny_it201.stc_rr_excess) — The excess of New York City taxable income over the bracket amount
Status: **DISAGREE**

Project:

```json
{"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.stc.rr.over"}}
```

Second:

```json
{"expression": {"from": {"line": "47"}, "op": "subtract_floor0", "take": {"param": "ny.stc.rr.over"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (69a) (ny_it201.stc_rr_excess_product) — 0.228% of the excess
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "(69a) (ny_it201.stc_rr_excess)"}, "op": "multiply_rate", "rate": {"param": "ny.stc.rr.high_rate"}, "unit": 100}
```

Second:

```json
{"expression": {"amount": {"line": "(69a) (ny_it201.stc_rr_excess)"}, "op": "multiply_rate", "rate": {"param": "ny.stc.rr.high_rate"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (69a) (ny_it201.stc_rr_base) — The bracket's base amount ($21, $37 or $25)
Status: **AGREE**

### (69a) (ny_it201.stc_rr_high) — The base amount plus 0.228% of the excess
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "(69a) (ny_it201.stc_rr_base)"}, {"line": "(69a) (ny_it201.stc_rr_excess_product)"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"line": "(69a) (ny_it201.stc_rr_base)"}, {"line": "(69a) (ny_it201.stc_rr_excess_product)"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (69a) (ny_it201.stc_rr) — The rate reduction amount from the table for the filing status
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "47"}, {"param": "ny.stc.rr.over"}], "test": "le"}, "then": {"line": "(69a) (ny_it201.stc_rr_low)"}}, {"guard": {"args": [{"param": "ny.stc.rr.over"}, {"line": "47"}], "test": "lt"}, "then": {"line": "(69a) (ny_it201.stc_rr_high)"}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"line": "47"}, {"param": "ny.stc.rr.over"}], "test": "le"}, "then": {"line": "(69a) (ny_it201.stc_rr_low)"}}, {"guard": {"args": [{"param": "ny.stc.rr.over"}, {"line": "47"}], "test": "lt"}, "then": {"line": "(69a) (ny_it201.stc_rr_high)"}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Second transcription's note: The printed schedules stop at city taxable income of $500,000; above that the second band's formula is applied (the $500,000 income test on line 69a governs eligibility). Products are rounded half-up to the cent.

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 69a — NYC school tax credit (rate reduction amount)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "C"}], "test": "eq"}, "then": {"line": "(69a) (ny_it201.stc_rr)"}}, {"guard": {"args": [{"const": true}, {"line": "C"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"expression": {"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"line": "C"}], "test": "eq"}, {"args": [{"const": true}, {"line": "(question) (ny_it201.ask.city_resident)"}], "test": "eq"}, {"args": [{"line": "(69) (ny_it201.stc_income)"}, {"param": "ny.stc.rr.limit"}], "test": "le"}], "test": "all"}, "then": {"line": "(69a) (ny_it201.stc_rr)"}}, {"guard": {"args": [{"args": [{"param": "ny.stc.rr.limit"}, {"line": "(69) (ny_it201.stc_income)"}], "test": "lt"}, {"args": [{"const": false}, {"line": "C"}], "test": "ne"}, {"args": [{"const": true}, {"line": "(question) (ny_it201.ask.city_resident)"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 70 — NYC earned income credit
Status: **AGREE**

### 70a — NYC income tax elimination credit
Status: **AGREE**

### 71 — Other refundable credits (Form IT-201-ATT, line 18)
Status: **AGREE**

### 72 — Total New York State tax withheld
Status: **AGREE**

### 73 — Total New York City tax withheld
Status: **AGREE**

### 74 — Total Yonkers tax withheld
Status: **DISAGREE**

Project:

```json
{"const": 0}
```

Second:

```json
{"collection": "ny_it2", "field": "ny_it2.yonkers_withheld", "op": "sum_over", "where": null}
```

Ruling: representation; the project enters 0 and the reply sums ny_it2.yonkers_withheld. Every W-2 record with Yonkers tax withheld is refused (ny_it2.yonkers_gate on ny_it2 line 19; Yonkers is outside the tool, ny_it201.gate.yonkers), so on a computed return the sum is 0 too.

### 76 — Total payments (add lines 63 through 75)
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "63"}, {"line": "64"}, {"line": "65"}, {"line": "66"}, {"line": "67"}, {"line": "68"}, {"line": "69"}, {"line": "69a"}, {"line": "70"}, {"line": "70a"}, {"line": "71"}, {"line": "72"}, {"line": "73"}, {"line": "74"}, {"line": "75"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"line": "63"}, {"line": "64"}, {"line": "65"}, {"line": "66"}, {"line": "67"}, {"line": "68"}, {"line": "69"}, {"line": "69a"}, {"line": "70"}, {"line": "70a"}, {"line": "71"}, {"line": "72"}, {"line": "73"}, {"line": "74"}, {"line": "75"}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (80) — If line 76 is less than line 62, subtract line 76 from line 62
Status: **DISAGREE**

Project:

```json
{"from": {"line": "62"}, "op": "subtract_floor0", "take": {"line": "76"}}
```

Second:

```json
{"expression": {"from": {"line": "62"}, "op": "subtract_floor0", "take": {"line": "76"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"; ny_it201.tax_schedule: "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### (81) (ny_it201.prepayments) — Your 2025 prepayments: New York tax withheld and estimated tax payments (lines 72 to 75)
Status: **AGREE**

### (81) (ny_it201.safe_harbor_100) — 100% of your 2024 New York income tax
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "(question) (ny_it201.ask.prior_year_tax)"}, "op": "multiply_rate", "rate": {"param": "ny.est.prior_rate"}, "unit": 100}
```

Second:

```json
{"amount": {"line": "(question) (ny_it201.ask.prior_year_tax)"}, "op": "multiply_rate", "rate": {"param": "ny.est.prior_rate"}}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds the product (100% of the typed 2024 tax; IT-201-I p. 23, "the amount of your 2024 New York income tax") once to the dollar; the reply keeps cents. At most a 50-cent difference in the safe-harbor threshold.

### (81) (ny_it201.safe_harbor_110) — 110% of your 2024 New York income tax
Status: **DISAGREE**

Project:

```json
{"amount": {"line": "(question) (ny_it201.ask.prior_year_tax)"}, "op": "multiply_rate", "rate": {"param": "ny.est.prior_rate_high"}, "unit": 100}
```

Second:

```json
{"amount": {"line": "(question) (ny_it201.ask.prior_year_tax)"}, "op": "multiply_rate", "rate": {"param": "ny.est.prior_rate_high"}}
```

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds the product (110% of the typed 2024 tax; IT-201-I p. 23, "the amount of your 2024 New York income tax") once to the dollar; the reply keeps cents. At most a 50-cent difference in the safe-harbor threshold.

### (81) (ny_it201.safe_harbor) — The prepayments required to be safe from the estimated tax penalty
Status: **AGREE**

### 81 — Estimated tax penalty (include this amount in line 80 or reduce the overpayment on line 77
Status: **AGREE**

### 82 — Other penalties and interest
Status: **AGREE**

### (77) — If line 76 is more than line 62, subtract line 62 from line 76
Status: **DISAGREE**

Project:

```json
{"from": {"line": "76"}, "op": "subtract_floor0", "take": {"line": "62"}}
```

Second:

```json
{"expression": {"from": {"line": "76"}, "op": "subtract_floor0", "take": {"line": "62"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"; ny_it201.tax_schedule: "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 77 — Amount overpaid
Status: **DISAGREE**

Project:

```json
{"from": {"line": "(77)"}, "op": "subtract_floor0", "take": {"line": "81"}}
```

Second:

```json
{"expression": {"from": {"line": "(77)"}, "op": "subtract_floor0", "take": {"line": "81"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"; ny_it201.tax_schedule: "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 78 — Amount of line 77 available for refund (subtract line 79 from line 77)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "77"}, "op": "subtract_floor0", "take": {"line": "79"}}
```

Second:

```json
{"expression": {"from": {"line": "77"}, "op": "subtract_floor0", "take": {"line": "79"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"; ny_it201.tax_schedule: "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 78a — Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195, line 4)
Status: **AGREE**

### 78b — Total refund after NYS 529 account deposit (subtract line 78a from line 78)
Status: **DISAGREE**

Project:

```json
{"from": {"line": "78"}, "op": "subtract_floor0", "take": {"line": "78a"}}
```

Second:

```json
{"expression": {"from": {"line": "78"}, "op": "subtract_floor0", "take": {"line": "78a"}}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}]}
```

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"; ny_it201.tax_schedule: "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"), so the line was not executed. This adjudicates the declaration, not the tax reading.

### 80 — Amount you owe
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "(80)"}, {"line": "81"}, {"line": "82"}], "op": "sum"}
```

Second:

```json
{"expression": {"of": [{"line": "(80)"}, {"line": "82"}, {"from": {"line": "81"}, "op": "subtract_floor0", "take": {"line": "(77)"}}], "op": "sum"}, "invalid_model_types": [{"line": "ny_it201.line27", "message": "model changed a published result type"}, {"line": "ny_it201.line32", "message": "model changed a published result type"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}, {"line": "ny_it201.tax_schedule", "message": "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"}]}
```

Second transcription's note: Line 80 is the tax owed plus the estimated tax penalty (all of it when tax is owed; only the part exceeding the overpayment otherwise) plus line 82, which the instructions say to include in line 80.

Ruling: model error on the declaration, ruled mechanically: the reply fails the host's schema, type or reference validation on this line or a line it reads (ny_it201.line27: "model changed a published result type"; ny_it201.line32: "model changed a published result type"; ny_it201.tax_schedule: "ny_it201.ny_it201.tax_schedule: instance of 'ny_rs' must bind exactly [amount, status]"), so the line was not executed. This adjudicates the declaration, not the tax reading.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1 | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 8 | scope.schedule1, sd.other_forms | scope.schedule1, sd.other_forms |
| 11 | scope.schedule1 | scope.schedule1 |
| 12 | scope.schedule1 | scope.schedule1 |
| 13 | scope.schedule1 | scope.schedule1 |
| 17 | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 19 | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (check) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 20 | ny_it201.ask.out_of_state_bond_interest | ny_it201.ask.out_of_state_bond_interest |
| 21 | ny_it201.ask.414h | ny_it201.ask.414h |
| 22 | ny_it201.ask.529_nonqualified | ny_it201.ask.529_nonqualified |
| 23 | ny_it201.ask.it225 | ny_it201.ask.it225 |
| 24 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.decedent, ny_it201.ask.it225, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.decedent, ny_it201.ask.it225, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 25 | ny_it201.ask.inflation_check | ny_it201.ask.inflation_check |
| 26 | ny_it201.ask.gov_pension | ny_it201.ask.gov_pension |
| 28 | ny_it201.ask.us_obligation_interest | ny_it201.ask.us_obligation_interest |
| 29 | ny_it201.ask.pension_exclusion | ny_it201.ask.pension_exclusion |
| 30 | ny_it201.ask.529_owner | ny_it201.ask.529_owner |
| 31 | ny_it201.ask.it225 | ny_it201.ask.it225 |
| 32 | ny_it201.ask.529_owner, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.pension_exclusion, ny_it201.ask.us_obligation_interest | ny_it201.ask.529_owner, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.pension_exclusion, ny_it201.ask.us_obligation_interest |
| 33 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 34 | ny_it201.ask.itemize | ny_it201.ask.itemize |
| 35 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 37 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 38 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tax_table) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tax_schedule) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tax_low) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.w1) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.w7) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.w12) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.w2) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.w3) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.w4) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.w5) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.w8) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.w9) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.w10) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.w13) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.w14) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.w15) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.top) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.mfj) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.single) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.hoh) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tcw.by_status) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (39) (ny_it201.tax_high) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 39 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (Note 1) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 2, column 1) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 5, column 1) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 2, column 2) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 5, column 2) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 2, column 3) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 5, column 3) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 2, column 4) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 5, column 4) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 2, column 5) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 5, column 5) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 2, column 6) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 5, column 6) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 2, column 7) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 5, column 7) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 2) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 5) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 1) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (table 4) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (40) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_fs_mfs, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_fs_mfs, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (48) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_fs_mfs, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_fs_mfs, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 40 | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_fs_mfs, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_fs_mfs, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 41 | ny_it201.ask.resident_credit | ny_it201.ask.resident_credit |
| 42 | ny_it201.ask.other_credits | ny_it201.ask.other_credits |
| 43 | ny_it201.ask.decedent, ny_it201.ask.other_credits, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_fs_mfs, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.other_credits, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_fs_mfs, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 44 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.other_credits, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.other_credits, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 45 | ny_it201.ask.other_taxes | ny_it201.ask.other_taxes |
| 46 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 47 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (47a) (ny_it201.city_tax_table) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (47a) (ny_it201.city_tax_schedule) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 47a | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 48 | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_fs_mfs, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_fs_mfs, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 49 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 51 | ny_it201.ask.other_taxes | ny_it201.ask.other_taxes |
| 52 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.other_taxes, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.other_taxes, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 53 | ny_it201.ask.city_credits | ny_it201.ask.city_credits |
| 54 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.city_credits, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.other_taxes, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.city_credits, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.other_taxes, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 54a | ny_it201.ask.mctmt | ny_it201.ask.mctmt |
| 54b | ny_it201.ask.mctmt | ny_it201.ask.mctmt |
| 54c | ny_it201.ask.mctmt | ny_it201.ask.mctmt |
| 54d | ny_it201.ask.mctmt | ny_it201.ask.mctmt |
| 54e | ny_it201.ask.mctmt | ny_it201.ask.mctmt |
| 55 | ny_it201.ask.yonkers | ny_it201.ask.yonkers |
| 56 | ny_it201.ask.yonkers | ny_it201.ask.yonkers |
| 57 | ny_it201.ask.yonkers | ny_it201.ask.yonkers |
| 58 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.city_credits, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.other_taxes, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.yonkers, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.city_credits, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.other_taxes, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.yonkers, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (chart) (ny_it201.sut.top_product) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (chart) (ny_it201.sut.top) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (chart) (ny_it201.sut.chart) | ny_it201.ask.abode_part_year, ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.use_tax_st141, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.abode_part_year, ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.use_tax_st141, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 59 | ny_it201.ask.abode_part_year, ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.use_tax_st141, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.abode_part_year, ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.use_tax_st141, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 60 | ny_it201.ask.contributions | ny_it201.ask.contributions |
| 61 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 62 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fs_mfs, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 64 | ny_it201.ask.dependent_care | ny_it201.ask.dependent_care |
| 65 | ny_it201.h_fed_eic | ny_it201.h_fed_eic |
| 66 | ny_it201.ask.noncustodial | ny_it201.ask.noncustodial |
| 67 | ny_it201.ask.real_property_credit | ny_it201.ask.real_property_credit |
| 68 | ny_it201.ask.college_tuition | ny_it201.ask.college_tuition |
| (69) (ny_it201.stc_income) | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 69 | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.decedent, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (69a) (ny_it201.stc_rr_low) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (69a) (ny_it201.stc_rr_excess) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (69a) (ny_it201.stc_rr_excess_product) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (69a) (ny_it201.stc_rr_high) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (69a) (ny_it201.stc_rr) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 69a | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.decedent, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 70 | ny_it201.h_fed_eic | ny_it201.h_fed_eic |
| 70a | ny_it201.h_it270_possible | ny_it201.h_it270_possible |
| 71 | ny_it201.ask.other_credits | ny_it201.ask.other_credits |
| 72 | ny_it201.ask.other_withholding | ny_it201.ask.other_withholding |
| 73 | ny_it201.ask.other_withholding | ny_it201.ask.other_withholding |
| 74 | ny_it201.ask.other_withholding | ny_it201.ask.other_withholding |
| 76 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.college_tuition, ny_it201.ask.decedent, ny_it201.ask.dependent_care, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.noncustodial, ny_it201.ask.other_credits, ny_it201.ask.other_withholding, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.real_property_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_fed_eic, ny_it201.h_it270_possible, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.college_tuition, ny_it201.ask.decedent, ny_it201.ask.dependent_care, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.noncustodial, ny_it201.ask.other_credits, ny_it201.ask.other_withholding, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.real_property_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.h_fed_eic, ny_it201.h_it270_possible, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (80) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.college_tuition, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.dependent_care, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.noncustodial, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.other_withholding, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.real_property_credit, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fed_eic, ny_it201.h_fs_mfs, ny_it201.h_it270_possible, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.college_tuition, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.dependent_care, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.noncustodial, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.other_withholding, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.real_property_credit, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fed_eic, ny_it201.h_fs_mfs, ny_it201.h_it270_possible, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| (81) (ny_it201.prepayments) | ny_it201.ask.other_withholding | ny_it201.ask.other_withholding |
| 81 | ny_it201.h_pen_possible | ny_it201.h_pen_possible |
| 82 | ny_it201.ask.late_penalty | ny_it201.ask.late_penalty |
| (77) | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.college_tuition, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.dependent_care, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.noncustodial, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.other_withholding, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.real_property_credit, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fed_eic, ny_it201.h_fs_mfs, ny_it201.h_it270_possible, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.college_tuition, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.dependent_care, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.noncustodial, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.other_withholding, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.real_property_credit, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fed_eic, ny_it201.h_fs_mfs, ny_it201.h_it270_possible, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres |
| 77 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.college_tuition, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.dependent_care, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.noncustodial, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.other_withholding, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.real_property_credit, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fed_eic, ny_it201.h_fs_mfs, ny_it201.h_it270_possible, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_pen_possible, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.college_tuition, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.dependent_care, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.noncustodial, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.other_withholding, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.real_property_credit, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fed_eic, ny_it201.h_fs_mfs, ny_it201.h_it270_possible, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_pen_possible, ny_it201.h_spouse_nonres |
| 78 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.college_tuition, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.dependent_care, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.noncustodial, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.other_withholding, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.real_property_credit, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fed_eic, ny_it201.h_fs_mfs, ny_it201.h_it270_possible, ny_it201.h_line19_mismatch, ny_it201.h_line79_excess, ny_it201.h_not_state_resident, ny_it201.h_pen_possible, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.college_tuition, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.dependent_care, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.noncustodial, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.other_withholding, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.real_property_credit, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fed_eic, ny_it201.h_fs_mfs, ny_it201.h_it270_possible, ny_it201.h_line19_mismatch, ny_it201.h_line79_excess, ny_it201.h_not_state_resident, ny_it201.h_pen_possible, ny_it201.h_spouse_nonres |
| 78a | ny_it201.ask.refund_529 | ny_it201.ask.refund_529 |
| 78b | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.college_tuition, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.dependent_care, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.noncustodial, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.other_withholding, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.real_property_credit, ny_it201.ask.refund_529, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fed_eic, ny_it201.h_fs_mfs, ny_it201.h_it270_possible, ny_it201.h_line19_mismatch, ny_it201.h_line79_excess, ny_it201.h_not_state_resident, ny_it201.h_pen_possible, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.college_tuition, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.dependent_care, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.mctmt, ny_it201.ask.noncustodial, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.other_withholding, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.real_property_credit, ny_it201.ask.refund_529, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fed_eic, ny_it201.h_fs_mfs, ny_it201.h_it270_possible, ny_it201.h_line19_mismatch, ny_it201.h_line79_excess, ny_it201.h_not_state_resident, ny_it201.h_pen_possible, ny_it201.h_spouse_nonres |
| 80 | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.college_tuition, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.dependent_care, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.late_penalty, ny_it201.ask.mctmt, ny_it201.ask.noncustodial, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.other_withholding, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.real_property_credit, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fed_eic, ny_it201.h_fs_mfs, ny_it201.h_it270_possible, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_pen_possible, ny_it201.h_spouse_nonres, scope.schedule1, sd.other_forms | ny_it201.ask.414h, ny_it201.ask.529_nonqualified, ny_it201.ask.529_owner, ny_it201.ask.abode_part_year, ny_it201.ask.city_credits, ny_it201.ask.college_tuition, ny_it201.ask.contributions, ny_it201.ask.decedent, ny_it201.ask.dependent_care, ny_it201.ask.gov_pension, ny_it201.ask.inflation_check, ny_it201.ask.it225, ny_it201.ask.itemize, ny_it201.ask.late_penalty, ny_it201.ask.mctmt, ny_it201.ask.noncustodial, ny_it201.ask.other_credits, ny_it201.ask.other_taxes, ny_it201.ask.other_withholding, ny_it201.ask.out_of_state_bond_interest, ny_it201.ask.pension_exclusion, ny_it201.ask.real_property_credit, ny_it201.ask.resident_credit, ny_it201.ask.special_accrual, ny_it201.ask.special_code, ny_it201.ask.us_obligation_interest, ny_it201.ask.use_tax_st141, ny_it201.ask.yonkers, ny_it201.h_fed_eic, ny_it201.h_fs_mfs, ny_it201.h_it270_possible, ny_it201.h_line19_mismatch, ny_it201.h_not_state_resident, ny_it201.h_pen_possible, ny_it201.h_spouse_nonres |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| C | e206d709b10e936a693e89d2d4b8a1be997ef8f727873f85a46ca90a120bc600 |
| H (count) | 9772181dca51664de890acd4fe418df5669a11be967acdfede3d7c83aabf2ead |
| 1 | 79efdbc49b9848d316ae9f014c4ac9c764bd09013c016bd242a3dcee5374b6b7 |
| 2 | fdcb465984ab522217889d4654ae7a80a56bb0c06db15cc57803f069838c7016 |
| 3 | 2993a87a79c1c9e6447dd04c332f2512732c94443241b987abde727a94ab3dbd |
| 4 | eb5ef1e6ab97b5bfdda0fb866826b4bf74ef2856c99d70dbebef72dc72cdb59f |
| 5 | 3ac84bed0875496202afe0775822a067747f6cf594e1701cff0729f4ed04a297 |
| 6 | e063f11ebcd3052cadf0b7c236648d01ecb571c05f69fefd6b9f5b1158f3996a |
| 7 | 727ee3573b4c29873c5b0822d58ed166def3a781a3c0ad779cd5f62cd48f66ef |
| 8 | a9cf0c8b8d0757df90fe4d97ad1fd2e16c5d846e45110518bb008842eeca90e0 |
| 9 | 17f7eed8970c09df2f059cd44f0bd6ff3e991f2254f4f2f4c9149208080288fc |
| 10 | f491eebbd6ac3fdf8cee92d405318d8c1d2811db64e9b7ae9c1b0fc677996651 |
| 11 | 42c1a3c08bf82e10c59db57fe18cc36a7511fa34fa1343267cdbd61405656707 |
| 12 | ee53d392d8f5303fb576ca3ae2ceb8324bdb8a8577398b303c2407446470326b |
| 13 | bdfa4fac6471c4d3f3eb1e07fa3e38e167efef48366061d93876a8a5767db3a4 |
| 14 | fb38030daf0a2bbe087e7256c5dc145a91679d0db8b4a2c2acf35a665efa7a7d |
| 15 | dcac1caf642042f5fbefd7ada76a4aba053765208004b6b210e795e40ec0031f |
| 16 | 59c4e9d6030296a57ae294d26d0db84b3c8b1789770365645de48ce08a5b6986 |
| 17 | a58a074cf0feb80e6b16198929489c1238d67e0b4bcb4a710fb09740e9958420 |
| 18 | be44ee1478e5bddc747182fde726ce681be9cd60098d21f5c82408812e88e303 |
| 19 | 0eed89e7d006e598db60d0565aa83e2d36c9f29e3a70229fa9ae0798cd478d55 |
| (check) | ef205f691fbc1a3a7cf23958f9eaad91e30b257feb23b545ec1e4eea84f811ad |
| 20 | 09190ca61a03915045ebeeebd000d1c7f1a2318afcef36500a05da88f48477d0 |
| 21 | ef0f472e09ce20fbbcf47a173739ab9d2305bb36c983b978f7e995f9de815df2 |
| 22 | 1197dc4fd50e88ed91b1d3801d1438313c7b5a8d7446052d5e2c3b4cb69852df |
| 23 | 44874d303a0b7ff524fbd5c6bebf7fbe775baa828a6d3be42a2e5a2a91622fc8 |
| 24 | 23d4a312a63ef041ca385d36c9ea256ad46d7179700ec5b4a3c7dac809166653 |
| 25 | 36922d23ca496dbc41a8f2eda97a5a2c35fa2aea7c2c0cf90d09961da6cde59e |
| 26 | 07d2616c8adbd63bf6add484981d675458c8f2342b14e4632b74c4cc60e621a3 |
| 27 | ea5b43da0ab08698fa86f7cc9a00311b894e877c6bd85079903923b105a7bac2 |
| 28 | aacbc3e60d798ae3c41cb9bcb166e47706a178d8c7b70355b77ce86b7d0148ae |
| 29 | c8ac9155e6fdfaacd5aa3e07691f94813f0d8961e3c9ffb49404325350c0f9ec |
| 30 | d21eaf2ec916817a82c0a0fbbafed940fa2456a205fb4176f9aef376c6afb27a |
| 31 | bc189f3c10c62215d3ba9e34b84c27ec6242fefa5a59a2024ecfef07e15fea28 |
| 32 | 4aa48afb43639462af1c29c889ce40bebda3bd5adc330107240096ef1582d670 |
| 33 | 4da2a0abe620ae662590e4a36efdffd0403da7c179cd0785fba4e5b6d2417fa8 |
| (table) (ny_it201.std_deduction) | 84f234a9fb459ca8cfd31a2dffaeb5709b2d2391d637912e4145429cf69ea888 |
| (table) (ny_it201.std_deduction_dependent) | f5607e6acd199e65695391a6657d56ddaa2be910c7089265075a6549d1ca061a |
| 34 | 0c81ad0c2e1db863ff1f5ee1edc34dc5b454a028730aa1faffddecdb53635885 |
| 35 | d8778e779d6db3bbea7e05b5000a1cc644af1e658ecf696627b9ae0100388678 |
| 36 | 768efbbcfc7648a02cd54719d8d7a7f1f02888501e0038e47a5549900d4502ee |
| 37 | 2bf1e78e3717b6baae6e0a18470013c6dfbb9b752f212d0567c720f49d76b29b |
| 38 | 82e0c9a622bd50e92a3b9b0d2f69255b2fdece0b20529bae8882d90607ab83f9 |
| (39) (ny_it201.tax_table) | 810f9659800e510c7fac929f4cb02e1c8fed6ee72bfaca7984e2d7ad26c974f7 |
| (39) (ny_it201.tax_schedule) | 40bf304aab99a3d8e77e869b882e7154146898fed694c91ee5a6fb724237b6c3 |
| (39) (ny_it201.tax_low) | 84798a688b8ce62f1df0826509115a93cda66272dc7b73f9bc90a8dd9a73a20d |
| (39) (ny_it201.tcw.w1) | b669a7ff5c7b2e66e047089f9e82e59518ac89e4e21eb3b91d852e8dbb17e544 |
| (39) (ny_it201.tcw.w7) | f2f7dad06c690e3486a78237b787c86ec85ecd066fb2e8b7914315330a21e77c |
| (39) (ny_it201.tcw.w12) | 894fa2cefc56e4ab3b538799901b1d661bfa1de98bf2961f5fea41e03bda2eee |
| (39) (ny_it201.tcw.w2) | 8bf766e93a21724f2715a33b6e676653c5c7ebc0ad8648dc4d13d977a794c514 |
| (39) (ny_it201.tcw.w3) | 6fe26c21b6c6b784f1035ef7e40f7c377cec1e7b185e30ea628522222f596376 |
| (39) (ny_it201.tcw.w4) | d4fb70ec3028a88201d1e4c80af0fcf6dba2ace951a43535277601c1a64a9579 |
| (39) (ny_it201.tcw.w5) | 1a72549b5fc0f14f3356bb3e338041a59899f8bf74a22be5fda454689b5ef29d |
| (39) (ny_it201.tcw.w8) | e7dc8e214bed7eda39ba9ca4c035cf58ace345ed34c3c2f2282006bc5da1a268 |
| (39) (ny_it201.tcw.w9) | eb4c3f6f19d1c0227d62a1b7df587485dd7bf7babd9c7746fdbe7e0793f43166 |
| (39) (ny_it201.tcw.w10) | 16ae3a82440ba13c871956b252b1f6b2c6588fd982a6bf6f23ad30cef509fe5b |
| (39) (ny_it201.tcw.w13) | 00341e6835fc565cfecaf29870da8e9127d7bfbdf41821716c4e647f70bef6d7 |
| (39) (ny_it201.tcw.w14) | dd47d67890d84f90557be2aa66bab8af498d98f886f0a5847f81df75a4504910 |
| (39) (ny_it201.tcw.w15) | 20e79d82e45f164a84a8a60d21287b6c29904c80ef1e4bfe6f765a7c90bbbaaf |
| (39) (ny_it201.tcw.top) | ac9eee928b1b9bc7734bf4ece4d3b838af92cc7feb3d238b2dbc45a7ad699378 |
| (39) (ny_it201.tcw.mfj) | b0226e7f673162a85672d78ef1a53b4af91bbb5c8d1637e4bf0d8c1aa8cdb8d5 |
| (39) (ny_it201.tcw.single) | 028a4f9c895276faa0e5ba894ba995d4c382d63dc3ea5ab20cdf6c6089d36fdc |
| (39) (ny_it201.tcw.hoh) | 1e5614f68847fa145a32abc08029e3b6356061bc12398a903eae7cdf5f356fd9 |
| (39) (ny_it201.tcw.by_status) | 84d346dea9bbc291d0d274f88fe4da824ddfecc0e4acdcb2e91efb7016bf2054 |
| (39) (ny_it201.tax_high) | 15eb0108c44d71a5387fec9294ff8954e4be66011c5a7521024a076b1c7cf2e6 |
| 39 | 2115be5c064e2e149c217bf109ed5a688cd6e5b361cfb48459d908251c67dcf8 |
| (Note 1) | c143f38d06d4ae9c6024f8f3bf645fc3f7ed911721769e28b6a8271dd8a0c144 |
| (column) | cc74f837e50fb8314c13f6d40f363998d97b72581fb9020dd3113942160c0513 |
| (table 2, column 1) | 9c5c38829439c86e92c2854aad8df526e096d3ab22055f2509942d48201100fc |
| (table 5, column 1) | fe616f8a66125e8c297119e636698d6165104b17e3aa4f624adb99008ac6be81 |
| (table 2, column 2) | 7863a2beeed9ee4dc4f033de60d4a52ca6d88ec89762a09408d553615de45be9 |
| (table 5, column 2) | f23f89f62e53f0ae3b983740049bc5ea9d3b964d77e236eb4a3164e6f871b0f5 |
| (table 2, column 3) | 50416262a9bf883107778eae60a3c4d71320e4cc45ab9eb69e5d89f1a8e82ffa |
| (table 5, column 3) | 103fb69ffd305f9dd1a772c1c2a93ff02423a80a0df2e2f12ffa984ca84ac4ca |
| (table 2, column 4) | 7743f0133425cb29caaee818ab23f5253ef0fa5cdad1e88c9a60aa51aff132d5 |
| (table 5, column 4) | eac36d15ef79a46312eaa17c4b91d1224f6938f60b7f4a3b8369192535be403e |
| (table 2, column 5) | af54d68511f6a06dfff617650479959b4bd7e01ae2f94746e85d85cca97611b8 |
| (table 5, column 5) | f1c94ba33fc83728d64d881de2dbfdab690693f38ea9d2e55484ce9da137b6e4 |
| (table 2, column 6) | 2e59e38bffd2cf93a1234b5550df7eff83a4bdc514d18090d22879c368cd79a9 |
| (table 5, column 6) | 0124bc0d87231f7ea70d1f2f9cfc148cb4e99db7136ad7001486a127a9cde148 |
| (table 2, column 7) | 8c7de40ff59fda38c0126d90fa8bf0721cd0774dee0baad37b2cab7b61eabb66 |
| (table 5, column 7) | eabb0634f29a613aec9d0def5a2686b938e046e7629dfa9a625785c07f9e4e5f |
| (table 2) | 132a8d5f453371c144cf0872835c121cc64759d597bce42f4d1b4bc92d994773 |
| (table 5) | 254ff137b7be80c8349c54dbf0f53f8c46086b1d3a081eb345f8f5049d886d36 |
| (table 1) | 758cf024002b13712bfbf6f77dbea22c87eb0371de942c4413357bb666af3039 |
| (table 4) | 3ee893f7861099b47c1bfad52a579e00564ca76d3799753e01bd545c02d2fa8e |
| (40) | 450ced7e6da574992267b7c4fe0a2ba1d9019e669cd1c4226313ee111b7e18a7 |
| (48) | f58f61b3df5968669ce462612b8c5d4c6e8043df4d8b2d74907e8845595b6aa0 |
| 40 | 25114268fe1a56766b50913071f29f7af7a93df67cac74595092aea1518669fa |
| 41 | d48a104418f41fe0301eb31b086bdf0ee3542b7d4467dcea9f5bec6bc16ada0e |
| 42 | c3d4d4076e1355877a09f359f68bd5158c7657e64be484e9aff220b6ab723d2b |
| 43 | 0bc17412387de71307d8bf4a3235c56c89f8e984af9a7fd9ef4bc1b1dfed8234 |
| 44 | 275f1f4bdb5d1542f8daf5c3738e05bf84db7e8ae8f756d2986c0c01e8ecca5f |
| 45 | 0060e1ab7de4d8a2f24de6b4bcc751a3891430a713ec55fbbdf7266b58fd5c48 |
| 46 | 4b05c1f1e480b3cbf332c3201aa8bcee4c8093312ca6126e2474177d383e58d6 |
| 47 | ea5decf22310a3655be9c88130da6dbd07bbd23693a10f90ad90ef3be013d6ad |
| (47a) (ny_it201.city_tax_table) | e24e7299193bfc457a4fe8ccbd77ba5cb4c1e295e91741be2447b1531830d34d |
| (47a) (ny_it201.city_tax_schedule) | 687b3f1f0299c47bd14b96373e24488d4ede4bffd26ce522244b5b3682ab58a8 |
| 47a | bf07e26ede720b4aa441477129f00303076bbcd2ed8a265572b9bfd2dd29460a |
| 48 | 3466c616e04b7e8a72df8972d56db45fa1509663580effcaeb5b44b9fcd8eabf |
| 49 | 30e34b0efb88363b1c3df11a80ec65161cb1a466be99d7c730dd4bd9a6c445ef |
| 50 | 448d9614e81b072ce43c4d63e181bd5870d2650d081186cdc10d0c3e97569337 |
| 51 | 07e4c1de34b20e41fad31c6bf9cbeb160435f2ae9c34886cc5b857b7f11889ea |
| 52 | 3fec90c4889207a9717bc5fcf14f289084945671ce1209f6f81e9f61fc428658 |
| 53 | 4128075264d8e3ec53af11be8f5693ba9b4e08852882a38beb3fd5a2dcf4ae65 |
| 54 | 181d8ff312476822d6bb2fc2e00c2cc1fa51dcfbd74eec78ef59b013a6569e01 |
| 54a | 0a985369d50d2ad161ce892a1574087c1535952815f582a4a2ee169a1816c857 |
| 54b | 04f133c0295b3c4ec868091e96c60d35d99ea289a08f1334b09fa5cb62cc70bc |
| 54c | 550e861c5fe50bd93715d31feed37708ba2d435d2f9b3ba6fd8985f1a81b2d1e |
| 54d | 9f4642fbd12447b6f60c16f4c5ce485625ef2a88940ae2155a6b6f6d384a53ae |
| 54e | 4130186c26605169ab9f9c54be5d403f47dbfa7a6dae22132b5e4d36c099a205 |
| 55 | 73d4aa2e4b946fb66d95d69db83ecb3b9a5c76882dbfc34fa4cae11eafbd837b |
| 56 | 8332a01b6e89739e2dc5c1b912589e45d4fa9470a903fd5ab30cc56aed127790 |
| 57 | 4227663b57d086f680d104bb090f315cd8339c00e6efb45aab3f215817129c89 |
| 58 | 51c64c12cf5779c92673d26d239cb710c3e72cec4326ef3ac292a5b208fbe47c |
| (chart) (ny_it201.sut.b1) | e43916a67515f6ea747b968bd19a21a57487791d67a386c53bdb70c32d8659ce |
| (chart) (ny_it201.sut.b2) | ed042da74e8f650fc26462e4e11ac8478a0a6411d661157e03d0e69b0260c191 |
| (chart) (ny_it201.sut.b3) | 7ee98fb24ccb4ff9c585a15fb899b7831426cb45c18efce9ab1a5ab37f66450f |
| (chart) (ny_it201.sut.b4) | be4c7e8c34b29c10447f7c3cd8fcf94a2331aa01792f5f277159705a72024ae8 |
| (chart) (ny_it201.sut.b5) | 610bf8796eba06614fd3b93dee830d8276ad568d626d37cf14473ce694be28f6 |
| (chart) (ny_it201.sut.b6) | 318bb28fff7744c39bc62c13a5a3a2d684bf21af8d04dfb6be4817210b5fe873 |
| (chart) (ny_it201.sut.b7) | fc040cbb69f4d170b3a0d0b54d7269280d0e3cb803cbd327ef096674d59a5ea6 |
| (chart) (ny_it201.sut.top_product) | 019f1d65ade32238135065acfb22e93925ded9b720c11a3f8c152b3b8a622594 |
| (chart) (ny_it201.sut.cap) | 480a005d95567a9a87ac0357bf5f04bd2c305592685e6f3db805efe287f74118 |
| (chart) (ny_it201.sut.top) | 81212b989e0a9c72d4e29af4a1619f540bd9388fb8dca72a82fa0ea6d2db491a |
| (chart) (ny_it201.sut.chart) | 434bb295cdec4e6fff2986dda8572c190d65dd90597d0e6e16956bfad5abc746 |
| 59 | b28484ef1e24397583a562c9464dd3d68d2f6817cb14fd56280d0b300beabd21 |
| 60 | b012ec83dd1cece2e816e8a48b1e031e7138e020ea8d9b2f8572032f263fee6a |
| 61 | 0b1a9a7e004852b7f3a94814a1e24052d4022bd1865add071eb08fed53e081d9 |
| 62 | 241df0575de9833259f382dc1d60b387706e4cc608116fc5e156466dc822670a |
| 63 | 5596d02bc245916d78c77d3a4805fb88c0f7ff8abe226c841dd44dec06a5cbf8 |
| 64 | 48e5ab55ab375a2011423033cd155ae551c8a485912aa6c75bc00d33cb95a8d3 |
| 65 | 9b8ec4931c5964c73aa4d5a0a9d2df2349715d79281cf60fb58a6e21e3cc3155 |
| 66 | f448c4d10f84f3065185eeb222de3b366f2cff433f65a3790be55ed876ffe87a |
| 67 | cdbc89eadc19fc8f8c21a7ddc2bf87c09553cc8ad8973ebfc54ad2425062a117 |
| 68 | 84d4ec698bc91d142b4987d2b9eaaee1c66b020d3c3eee36ab4a9595d89679c1 |
| (69) (ny_it201.stc_income) | 056de19fb359c9a9829a97621c0d00e6160c05e5cb48ccd212186cc5e43ad3ba |
| (69) (ny_it201.stc_fixed_amount) | 3e671bd6a29a93359cf372c8c3c9fa7881c04ea39cb12571816084a4d7122499 |
| 69 | e2aa16e3e98ba426514e330e97acfaff59eb26f0ea6219f1b966b88914f31a5f |
| (69a) (ny_it201.stc_rr_low) | 0c8f9e190ce7993d05dde50a4e8c0741023626b38ba1dd40a222f0531c632c4e |
| (69a) (ny_it201.stc_rr_excess) | 189843cfc030f619f81972f607d5bd6f84dc0f69fda16243448b4ee41f93605c |
| (69a) (ny_it201.stc_rr_excess_product) | fdc7a679372e3fcef4cfacdd205c39e1976ce903bfea72da21ecd446edd5231a |
| (69a) (ny_it201.stc_rr_base) | 231a6c1bf70d13ce127f196cb4a9c0ce83546dd50d90ffd25672d0595ae75548 |
| (69a) (ny_it201.stc_rr_high) | cf06afdb622f00909c54a25d374010eac13e68c33602e5d0d7e2ac78025fc228 |
| (69a) (ny_it201.stc_rr) | 92a189cd248234614eb9516d6436483abb121b63b6ae3fbd9f4c523aa0159bf1 |
| 69a | f7a1d6b907f32ae907accdbf58e5bc3da3184be381abb4de6d741570e423aadf |
| 70 | 7a416976a022e7aaff081fff4cf762ef25d5372f3715dc8e6bfa4f6e66de3c63 |
| 70a | d8b8e02c503e56d3f728cf3341d25517f5b1eb84ec50b85138597c3b5e935e27 |
| 71 | cccb715af97b789b022f77fd4823f4fd389d9e4dc85d6450501c16fce4dde1d2 |
| 72 | 6096869ff7419c2199070aade4903c6fa7fa58af77fcdc707ef08b26e94fc4f0 |
| 73 | 903116c79984970451c909bf87c76ff7d406612ecd31de7296e99954b8fab99a |
| 74 | fd1ba9fd05f4791d4878e8d85a91a3a8d80344786979dda55a1133f4c331c924 |
| 76 | 4d6fd869f5ed1db4a927124a97c8bfcab3f17bf1eb3b12d4402b9d9909491f51 |
| (80) | e4a55e3e1356e14cf8245b2bd36d7af6ede398f2adf1771c329e4dc15fcaf46c |
| (81) (ny_it201.prepayments) | ade29155bbdf4391c6139ec8c16489c9534e657c7fe402c71f6bb234998ae930 |
| (81) (ny_it201.safe_harbor_100) | d592b1098834709ba71a339e37edab727d8d4bf070a98e2b2f547d107b4b8b86 |
| (81) (ny_it201.safe_harbor_110) | 3154538f383fe996aac83870e051ff3379d7d56ca8ffb2dd7c94a3d4e91e5c6f |
| (81) (ny_it201.safe_harbor) | a39ab47c10d19ad90f4eb14e243a5d072273ce4ed63fbef77a8239ea531dac2a |
| 81 | 55cf1b8ffc23defefe65384a782de885a482e76c2abbeed6c4864306af0d862b |
| 82 | 0ef538bbbc9a8be4404df14c3b97df3faf3e044a136320a9b3955a2f212bc137 |
| (77) | 212097eab2c9296063daf2ba2bc1ff29cd77053d428311586e08c55b0da8fe56 |
| 77 | 46ab920524b1c97c2068cf9fa2788b3aafd21b78c64a63dec721154ad51f6b9c |
| 78 | 098f09ec2c30547b235fe4336e9557899e7f4b2519108ef4438e72a7428af597 |
| 78a | 2dec834b5965add3ed087cb6424fc204ebf36174859d6c9ea3bf3b762bd08a25 |
| 78b | bea6d134c0f07d35505bbe96b5043c214983959f44986b5b8b0c22a504c06ece |
| 80 | 10d7bc72a06ed608c27e1dfa05ed569531ced10dbd52314dc55f4818ec48de2d |
| (rest of the document) | 9b8e1400e9ed29bae97a2ef3b82bfebd260de441d31e5edaee1d2a9cc93e1284 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| C | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| H (count) | 5bbcc5d1caf027b187fc89eccf2bb910be795eed1cb2b810c6c8fc805bec0cdf |
| 1 | db8517858ef828ebeecf59583a46ac018977f95fd60cd3216d797cff46b8c229 |
| 2 | 37553ac0dd1921e4f151ad8b0243b815ea0001b6d76125dd79dfc42b5cec69dd |
| 3 | 4e26f0f3fa313f1ffd6edec92adb28fefa00764c88b8a6e12a6ffa5b1d422def |
| 4 | d70b36dfb1e886e21a87de8d623fdee26b7884df60194071abc923d4910ec5db |
| 5 | deef43d4826a4457bd51fbc26a75a604d2ab5092761c5aa8d06ac8e24674b450 |
| 6 | 8c5c092c09eee7fa99aad01476aa0fd2a2b9c27c0e28b51404a0cac5a4e7b91e |
| 7 | eddd40e2316d0c89721d62967a0b57dc83362f36901c18d270b3590e8947595e |
| 8 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 9 | 1524937991a344954550454584d2ce7b46c7885d971a17fcb987d2dceba6d55d |
| 10 | f71b1a0c84b4acc28c4bb0fef0e2a1f63a1ecbd09df4eb1eba0633999ccff642 |
| 11 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 12 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 13 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 14 | 096009a19b5ac466d447ac37369ae95778eab9caf54d79a809755fcf0f70a887 |
| 15 | 43f56340cb28bacf1d63358e7e8e4bf5bfc4a2f2429661c0847274bac424b2a9 |
| 16 | ea3d5bae5b27cb4a21fe8c7d93c83a78d8a5e22e8a2f49e3da279d5febe64c8b |
| 17 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 18 | e0436ca291374ee6b9ca824a57b73cdc61e0895908ace373530866803bfe056d |
| 19 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (check) | 6d41e4e13caaba2306b7554eeb9238e86ac64fbdd47dc4696d7e1414b37dd1d3 |
| 20 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 21 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 22 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 23 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 24 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 25 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 26 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 27 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 28 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 29 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 30 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 31 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 32 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 33 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (table) (ny_it201.std_deduction) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (table) (ny_it201.std_deduction_dependent) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 34 | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| 35 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 36 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 37 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 38 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (39) (ny_it201.tax_table) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (39) (ny_it201.tax_schedule) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| (39) (ny_it201.tax_low) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (39) (ny_it201.tcw.w1) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| (39) (ny_it201.tcw.w7) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| (39) (ny_it201.tcw.w12) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| (39) (ny_it201.tcw.w2) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| (39) (ny_it201.tcw.w3) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| (39) (ny_it201.tcw.w4) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| (39) (ny_it201.tcw.w5) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| (39) (ny_it201.tcw.w8) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| (39) (ny_it201.tcw.w9) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| (39) (ny_it201.tcw.w10) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| (39) (ny_it201.tcw.w13) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| (39) (ny_it201.tcw.w14) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| (39) (ny_it201.tcw.w15) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| (39) (ny_it201.tcw.top) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (39) (ny_it201.tcw.mfj) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (39) (ny_it201.tcw.single) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (39) (ny_it201.tcw.hoh) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (39) (ny_it201.tcw.by_status) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (39) (ny_it201.tax_high) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 39 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (Note 1) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (column) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 2, column 1) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 5, column 1) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 2, column 2) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 5, column 2) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 2, column 3) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 5, column 3) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 2, column 4) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 5, column 4) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 2, column 5) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 5, column 5) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 2, column 6) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 5, column 6) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 2, column 7) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 5, column 7) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 2) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (table 5) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (table 1) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (table 4) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (40) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (48) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| 40 | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| 41 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 42 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 43 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 44 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 45 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 46 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 47 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (47a) (ny_it201.city_tax_table) | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| (47a) (ny_it201.city_tax_schedule) | 6d467107cbd3e1573da9abd73b3a2cafca2d91e50bbf11debcdd897823744dc8 |
| 47a | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 48 | 9dd1ec1bd082157ef6a4a29c8730c41da35d3de158f69a8a51d1ee491c6115b0 |
| 49 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 50 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 51 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 52 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 53 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 54 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 54a | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 54b | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 54c | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 54d | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 54e | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 55 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 56 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 57 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 58 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (chart) (ny_it201.sut.b1) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (chart) (ny_it201.sut.b2) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (chart) (ny_it201.sut.b3) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (chart) (ny_it201.sut.b4) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (chart) (ny_it201.sut.b5) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (chart) (ny_it201.sut.b6) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (chart) (ny_it201.sut.b7) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (chart) (ny_it201.sut.top_product) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (chart) (ny_it201.sut.cap) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (chart) (ny_it201.sut.top) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (chart) (ny_it201.sut.chart) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 59 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 60 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 61 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 62 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 63 | ae083ca1e053beaf072d860c3f4538073c2ec04c5212631a92f5ddb1c98f9c68 |
| 64 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 65 | dcd9172040fa80b96b5cfdea5d56ff709411c35bd1952db1164291b1e4a20b1b |
| 66 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 67 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 68 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (69) (ny_it201.stc_income) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (69) (ny_it201.stc_fixed_amount) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 69 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (69a) (ny_it201.stc_rr_low) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (69a) (ny_it201.stc_rr_excess) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (69a) (ny_it201.stc_rr_excess_product) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (69a) (ny_it201.stc_rr_base) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (69a) (ny_it201.stc_rr_high) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (69a) (ny_it201.stc_rr) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 69a | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 70 | dcd9172040fa80b96b5cfdea5d56ff709411c35bd1952db1164291b1e4a20b1b |
| 70a | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 71 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 72 | 57c3181b9c23f4fff4ecc97aa6b03bd0b2de79eec56b741e3c9c341e7d36fa0b |
| 73 | fd1502625ab212170cfb5ecddf54bb5b97b48de8c2d51a2b07fecf78881ecfde |
| 74 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 76 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (80) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (81) (ny_it201.prepayments) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (81) (ny_it201.safe_harbor_100) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (81) (ny_it201.safe_harbor_110) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (81) (ny_it201.safe_harbor) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 81 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 82 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| (77) | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 77 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 78 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 78a | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 78b | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 80 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |

## Raw second transcription

```yaml
```yaml
lines:
  - id: ny_it201.h_not_state_resident
    printed: "(helper)"
    label: "Not a full-year New York State resident (Form IT-201 is not the right return; use Form IT-203)"
    type: Bool
    expr: {op: test, eq: [ny_it201.ask.state_resident, {const: false}]}
  - id: ny_it201.h_spouse_nonres
    printed: "(helper)"
    label: "Joint return on which the spouse was not also a full-year New York State and New York City resident"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [f1040.status, {const: "mfj"}]}
        - {op: test, eq: [ny_it201.ask.spouse_resident, {const: false}]}
  - id: ny_it201.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
  - id: ny_it201.h_fs_mfj
    printed: "(helper)"
    label: "Filing status married filing jointly or qualifying surviving spouse"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [f1040.status, {const: "mfj"}]}
        - {op: test, eq: [f1040.status, {const: "qss"}]}
  - id: ny_it201.h_fs_single
    printed: "(helper)"
    label: "Filing status single or married filing separately"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [f1040.status, {const: "single"}]}
        - {op: test, eq: [f1040.status, {const: "mfs"}]}
  - id: ny_it201.h_fs_hoh
    printed: "(helper)"
    label: "Filing status head of household"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "hoh"}]}
  - id: ny_it201.h_fs_mfs
    printed: "(helper)"
    label: "Filing status married filing separate return"
    type: Bool
    expr: {op: test, eq: [f1040.status, {const: "mfs"}]}
  - id: ny_it201.h_city
    printed: "(helper)"
    label: "Full-year New York City resident"
    type: Bool
    expr: {op: test, eq: [ny_it201.ask.city_resident, {const: true}]}

  - id: ny_it201.item_c
    printed: "C"
    label: "Can you be claimed as a dependent on another taxpayer's federal return?"
    type: Bool
    expr: {op: copy, from: ny_it201.ask.item_c}
  - id: ny_it201.item_h_count
    printed: "H (count)"
    label: "Dependent information: number of dependents listed in item H"
    type: Count
    expr: {op: percent_floor, part: ny_it201.h_zero, whole: {param: ny.dependent_exemption}, cap: 100}
    note: "Open: item H lists each dependent claimed (or entitled to be claimed) on federal Form 1040, but the closed interface supplies no dependent count (no dependent collection with a count field, no federal dependents line in the catalog) and no new input may be added. Encoded as a constant 0 (a percent_floor of zero, the only way to form a zero Count from the supplied parameters). This understates line 36 and the household credits for filers with dependents; the project must wire item H to the federal dependents."
  - id: ny_it201.line1
    printed: "1"
    label: "Wages, salaries, tips, etc."
    type: NonNegDollars
    expr: {op: copy, from: f1040.line1z}
    refuses: [ny_it201.h_not_state_resident, ny_it201.h_spouse_nonres, ny_it201.ask.special_accrual, ny_it201.ask.decedent, ny_it201.ask.special_code]
    note: "Scope refusals for the whole return are placed on line 1: not a full-year resident (Form IT-203), a joint return with a spouse who was not also a full-year State and City resident (separate-sheet computations for lines 51 and 55), special accruals (IT-225 A-115/S-129), a decedent return, and special condition codes (including A6, which changes the household credit income)."
  - id: ny_it201.line2
    printed: "2"
    label: "Taxable interest income"
    type: Dollars
    expr: {op: copy, from: f1040.line2b}
  - id: ny_it201.line3
    printed: "3"
    label: "Ordinary dividends"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line3b}
  - id: ny_it201.line4
    printed: "4"
    label: "Taxable refunds, credits, or offsets of state and local income taxes (also enter on line 25)"
    type: NonNegDollars
    expr: {op: copy, from: s1.line1}
  - id: ny_it201.line5
    printed: "5"
    label: "Alimony received"
    type: NonNegDollars
    expr: {op: copy, from: s1.line2a}
  - id: ny_it201.line6
    printed: "6"
    label: "Business income or loss (submit a copy of federal Schedule C, Form 1040)"
    type: Dollars
    expr: {op: copy, from: s1.line3}
  - id: ny_it201.line7
    printed: "7"
    label: "Capital gain or loss (if required, submit a copy of federal Schedule D, Form 1040)"
    type: Dollars
    expr: {op: copy, from: f1040.line7a}
  - id: ny_it201.line8
    printed: "8"
    label: "Other gains or losses (submit a copy of federal Form 4797)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [scope.schedule1, sd.other_forms]
  - id: ny_it201.line9
    printed: "9"
    label: "Taxable amount of IRA distributions"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line4b}
  - id: ny_it201.line10
    printed: "10"
    label: "Taxable amount of pensions and annuities"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line5b}
  - id: ny_it201.line11
    printed: "11"
    label: "Rental real estate, royalties, partnerships, S corporations, trusts, etc. (submit copy of federal Schedule E, Form 1040)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [scope.schedule1]
  - id: ny_it201.line12
    printed: "12"
    label: "Rental real estate included in line 11"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [scope.schedule1]
  - id: ny_it201.line13
    printed: "13"
    label: "Farm income or loss (submit a copy of federal Schedule F, Form 1040)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [scope.schedule1]
  - id: ny_it201.line14
    printed: "14"
    label: "Unemployment compensation"
    type: NonNegDollars
    expr: {op: copy, from: s1.line7}
  - id: ny_it201.line15
    printed: "15"
    label: "Taxable amount of Social Security benefits (also enter on line 27)"
    type: NonNegDollars
    expr: {op: copy, from: f1040.line6b}
  - id: ny_it201.line16
    printed: "16"
    label: "Other income"
    type: Dollars
    expr: {op: copy, from: s1.line9}
    note: "Other income is read as federal Schedule 1, line 9 (total other income), the only federal additional-income item not already on lines 4 to 15."
  - id: ny_it201.line17
    printed: "17"
    label: "Add lines 1 through 11 and 13 through 16"
    type: Dollars
    expr:
      op: sum
      of: [ny_it201.line1, ny_it201.line2, ny_it201.line3, ny_it201.line4, ny_it201.line5, ny_it201.line6, ny_it201.line7, ny_it201.line8, ny_it201.line9, ny_it201.line10, ny_it201.line11, ny_it201.line13, ny_it201.line14, ny_it201.line15, ny_it201.line16]
  - id: ny_it201.line18
    printed: "18"
    label: "Total federal adjustments to income"
    type: NonNegDollars
    expr: {op: copy, from: s1.line26}
  - id: ny_it201.line19
    printed: "19"
    label: "Federal adjusted gross income (subtract line 18 from line 17)"
    type: Dollars
    expr: {op: subtract, from: ny_it201.line17, take: ny_it201.line18}
  - id: ny_it201.line19_agrees
    printed: "(check)"
    label: "Line 19 equals federal adjusted gross income (federal Form 1040, line 11a)"
    type: Bool
    expr: {op: test, eq: [ny_it201.line19, f1040.line11a]}
  - id: ny_it201.h_line19_mismatch
    printed: "(helper)"
    label: "Line 19 differs from federal adjusted gross income"
    type: Bool
    expr: {op: test, ne: [ny_it201.line19, f1040.line11a]}
  - id: ny_it201.line20
    printed: "20"
    label: "Interest income on state and local bonds and obligations (but not those of NYS or its local governments)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.out_of_state_bond_interest]
  - id: ny_it201.line21
    printed: "21"
    label: "Public employee 414(h) retirement contributions from your wage and tax statements"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.414h]
  - id: ny_it201.line22
    printed: "22"
    label: "New York's 529 college savings program distributions"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.529_nonqualified]
  - id: ny_it201.line23
    printed: "23"
    label: "Other (Form IT-225, line 9)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.it225]
  - id: ny_it201.line24
    printed: "24"
    label: "Add lines 19 through 23"
    type: Dollars
    expr: {op: sum, of: [ny_it201.line19, ny_it201.line20, ny_it201.line21, ny_it201.line22, ny_it201.line23]}
    refuses: [{when: ny_it201.h_line19_mismatch, when_known: true}]
  - id: ny_it201.line25
    printed: "25"
    label: "Taxable refunds, credits, or offsets of state and local income taxes (from line 4)"
    type: NonNegDollars
    expr: {op: copy, from: ny_it201.line4}
    refuses: [ny_it201.ask.inflation_check]
    note: "Open: the form says line 25 is the line 4 amount, while the 2025 instructions speak only of the inflation refund check included in federal AGI. Read as the line 4 amount (as printed); a return that included an inflation refund check is refused, since where it was reported and its amount are not supplied."
  - id: ny_it201.line26
    printed: "26"
    label: "Pensions of NYS and local governments and the federal government"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.gov_pension]
  - id: ny_it201.line27
    printed: "27"
    label: "Taxable amount of Social Security benefits (from line 15)"
    type: NonNegDollars
    expr: {op: copy, from: ny_it201.line15}
  - id: ny_it201.line28
    printed: "28"
    label: "Interest income on U.S. government bonds"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.us_obligation_interest]
  - id: ny_it201.line29
    printed: "29"
    label: "Pension and annuity income exclusion"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.pension_exclusion]
  - id: ny_it201.line30
    printed: "30"
    label: "New York's 529 college savings program deduction/earnings"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.529_owner]
  - id: ny_it201.line31
    printed: "31"
    label: "Other (Form IT-225, line 18)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.it225]
  - id: ny_it201.line32
    printed: "32"
    label: "Add lines 25 through 31"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.line25, ny_it201.line26, ny_it201.line27, ny_it201.line28, ny_it201.line29, ny_it201.line30, ny_it201.line31]}
  - id: ny_it201.line33
    printed: "33"
    label: "New York adjusted gross income (subtract line 32 from line 24)"
    type: Dollars
    expr: {op: subtract, from: ny_it201.line24, take: ny_it201.line32}
  - id: ny_it201.std_deduction
    printed: "(table) (ny_it201.std_deduction)"
    label: "New York State standard deduction table: standard deduction for your filing status"
    type: NonNegDollars
    expr: {op: param, ref: ny.std_deduction}
  - id: ny_it201.std_deduction_dependent
    printed: "(table) (ny_it201.std_deduction_dependent)"
    label: "New York State standard deduction table: Single and you marked item C Yes"
    type: NonNegDollars
    expr: {op: param, ref: ny.std_deduction.dependent_single}
  - id: ny_it201.line34
    printed: "34"
    label: "Enter your standard deduction or your itemized deduction (from Form IT-196)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [f1040.status, {const: "single"}]}
              - {op: test, eq: [ny_it201.item_c, {const: true}]}
          then: ny_it201.std_deduction_dependent
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [f1040.status, {const: "single"}]}
                - {op: test, eq: [ny_it201.item_c, {const: true}]}
          then: ny_it201.std_deduction
    refuses: [ny_it201.ask.itemize]
    note: "The table distinguishes item C only for filing status Single; other statuses use the table amount for the status whatever item C says."
  - id: ny_it201.line35
    printed: "35"
    label: "Subtract line 34 from line 33 (if line 34 is more than line 33, enter 0)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line33, take: ny_it201.line34}
  - id: ny_it201.h_dep_exemption
    printed: "(helper)"
    label: "Value of each New York State dependent exemption ($1,000)"
    type: NonNegDollars
    expr: {op: param, ref: ny.dependent_exemption}
  - id: ny_it201.line36
    printed: "36"
    label: "Dependent exemption amount (multiply the number of dependents listed in item H by 1,000)"
    type: NonNegDollars
    expr: {op: multiply_count, amount: ny_it201.h_dep_exemption, count: ny_it201.item_h_count}
  - id: ny_it201.line37
    printed: "37"
    label: "Taxable income (subtract line 36 from line 35)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line35, take: ny_it201.line36}
    note: "If line 36 is more than line 35 the instructions say to leave lines 37 and 38 blank; encoded as 0."
  - id: ny_it201.line38
    printed: "38"
    label: "Taxable income (from line 37 on page 2)"
    type: NonNegDollars
    expr: {op: copy, from: ny_it201.line37}

  - id: ny_it201.h_agi_low
    printed: "(helper)"
    label: "Line 33 is $107,650 or less"
    type: Bool
    expr: {op: test, le: [ny_it201.line33, {param: ny.table.agi_limit}]}
  - id: ny_it201.h_agi_high
    printed: "(helper)"
    label: "Line 33 is more than $107,650"
    type: Bool
    expr: {op: test, gt: [ny_it201.line33, {param: ny.table.agi_limit}]}
  - id: ny_it201.h_agi_top
    printed: "(helper)"
    label: "Line 33 is more than $25,000,000"
    type: Bool
    expr: {op: test, gt: [ny_it201.line33, {param: ny.tcw.agi_top}]}
  - id: ny_it201.h_agi_mid
    printed: "(helper)"
    label: "Line 33 is more than $107,650 but not more than $25,000,000"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, gt: [ny_it201.line33, {param: ny.table.agi_limit}]}
        - {op: test, le: [ny_it201.line33, {param: ny.tcw.agi_top}]}
  - id: ny_it201.h_show_table
    printed: "(helper)"
    label: "Use the NYS tax table (line 33 $107,650 or less and line 38 less than $65,000)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_agi_low, {const: true}]}
        - {op: test, lt: [ny_it201.line38, {param: ny.table.limit}]}
  - id: ny_it201.h_show_schedule
    printed: "(helper)"
    label: "Use the NYS tax rate schedule (line 33 $107,650 or less and line 38 $65,000 or more)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_agi_low, {const: true}]}
        - {op: test, ge: [ny_it201.line38, {param: ny.table.limit}]}
  - id: ny_it201.h_show_mfj
    printed: "(helper)"
    label: "Tax computation worksheets 1 to 5 apply (married filing jointly or qualifying surviving spouse)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_agi_mid, {const: true}]}
        - {op: test, eq: [ny_it201.h_fs_mfj, {const: true}]}
  - id: ny_it201.h_show_single
    printed: "(helper)"
    label: "Tax computation worksheets 7 to 10 apply (single and married filing separately)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_agi_mid, {const: true}]}
        - {op: test, eq: [ny_it201.h_fs_single, {const: true}]}
  - id: ny_it201.h_show_hoh
    printed: "(helper)"
    label: "Tax computation worksheets 12 to 15 apply (head of household)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_agi_mid, {const: true}]}
        - {op: test, eq: [ny_it201.h_fs_hoh, {const: true}]}
  - id: ny_it201.h_w1
    printed: "(helper)"
    label: "Tax computation worksheet 1 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_show_mfj, {const: true}]}
        - {op: test, le: [ny_it201.line38, {param: ny.tcw.mfj.w1.ti_limit}]}
  - id: ny_it201.h_w2
    printed: "(helper)"
    label: "Tax computation worksheet 2 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_show_mfj, {const: true}]}
        - {op: test, gt: [ny_it201.line38, {param: ny.tcw.mfj.w1.ti_limit}]}
        - {op: test, le: [ny_it201.line38, {param: ny.tcw.mfj.w2.ti_limit}]}
  - id: ny_it201.h_w3
    printed: "(helper)"
    label: "Tax computation worksheet 3 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_show_mfj, {const: true}]}
        - {op: test, gt: [ny_it201.line38, {param: ny.tcw.mfj.w2.ti_limit}]}
        - {op: test, le: [ny_it201.line38, {param: ny.tcw.mfj.w3.ti_limit}]}
  - id: ny_it201.h_w4
    printed: "(helper)"
    label: "Tax computation worksheet 4 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_show_mfj, {const: true}]}
        - {op: test, gt: [ny_it201.line38, {param: ny.tcw.mfj.w3.ti_limit}]}
        - {op: test, le: [ny_it201.line38, {param: ny.tcw.mfj.w4.ti_limit}]}
  - id: ny_it201.h_w5
    printed: "(helper)"
    label: "Tax computation worksheet 5 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_show_mfj, {const: true}]}
        - {op: test, gt: [ny_it201.line38, {param: ny.tcw.mfj.w4.ti_limit}]}
  - id: ny_it201.h_w7
    printed: "(helper)"
    label: "Tax computation worksheet 7 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_show_single, {const: true}]}
        - {op: test, le: [ny_it201.line38, {param: ny.tcw.single.w1.ti_limit}]}
  - id: ny_it201.h_w8
    printed: "(helper)"
    label: "Tax computation worksheet 8 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_show_single, {const: true}]}
        - {op: test, gt: [ny_it201.line38, {param: ny.tcw.single.w1.ti_limit}]}
        - {op: test, le: [ny_it201.line38, {param: ny.tcw.single.w8.ti_limit}]}
  - id: ny_it201.h_w9
    printed: "(helper)"
    label: "Tax computation worksheet 9 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_show_single, {const: true}]}
        - {op: test, gt: [ny_it201.line38, {param: ny.tcw.single.w8.ti_limit}]}
        - {op: test, le: [ny_it201.line38, {param: ny.tcw.single.w9.ti_limit}]}
  - id: ny_it201.h_w10
    printed: "(helper)"
    label: "Tax computation worksheet 10 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_show_single, {const: true}]}
        - {op: test, gt: [ny_it201.line38, {param: ny.tcw.single.w9.ti_limit}]}
  - id: ny_it201.h_w12
    printed: "(helper)"
    label: "Tax computation worksheet 12 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_show_hoh, {const: true}]}
        - {op: test, le: [ny_it201.line38, {param: ny.tcw.hoh.w1.ti_limit}]}
  - id: ny_it201.h_w13
    printed: "(helper)"
    label: "Tax computation worksheet 13 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_show_hoh, {const: true}]}
        - {op: test, gt: [ny_it201.line38, {param: ny.tcw.hoh.w1.ti_limit}]}
        - {op: test, le: [ny_it201.line38, {param: ny.tcw.hoh.w13.ti_limit}]}
  - id: ny_it201.h_w14
    printed: "(helper)"
    label: "Tax computation worksheet 14 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_show_hoh, {const: true}]}
        - {op: test, gt: [ny_it201.line38, {param: ny.tcw.hoh.w13.ti_limit}]}
        - {op: test, le: [ny_it201.line38, {param: ny.tcw.hoh.w14.ti_limit}]}
  - id: ny_it201.h_w15
    printed: "(helper)"
    label: "Tax computation worksheet 15 applies"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_show_hoh, {const: true}]}
        - {op: test, gt: [ny_it201.line38, {param: ny.tcw.hoh.w14.ti_limit}]}

  - id: ny_it201.tax_table
    printed: "(39) (ny_it201.tax_table)"
    label: "New York State tax on the line 38 amount from the 2025 New York State Tax Table"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_tax_table, key: ny_it201.line38, status: f1040.status}
    shown_when: ny_it201.h_show_table
  - id: ny_it201.tax_schedule
    printed: "(39) (ny_it201.tax_schedule)"
    label: "New York State tax on the line 38 amount from the New York State tax rate schedule"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ny_it201.h_fs_single, {const: true}]}
          then: {def: ny_rs, bind: {amount: ny_it201.line38}, line: single.result}
        - guard: {op: test, eq: [ny_it201.h_fs_mfj, {const: true}]}
          then: {def: ny_rs, bind: {amount: ny_it201.line38}, line: mfj.result}
        - guard: {op: test, eq: [ny_it201.h_fs_hoh, {const: true}]}
          then: {def: ny_rs, bind: {amount: ny_it201.line38}, line: hoh.result}
    shown_when: ny_it201.h_show_schedule
  - id: ny_it201.tax_low
    printed: "(39) (ny_it201.tax_low)"
    label: "Line 33 is $107,650 or less: NYS tax from the tax table, or the tax rate schedule if line 38 is $65,000 or more"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, lt: [ny_it201.line38, {param: ny.table.limit}]}
          then: ny_it201.tax_table
        - guard: {op: test, ge: [ny_it201.line38, {param: ny.table.limit}]}
          then: ny_it201.tax_schedule
    shown_when: ny_it201.h_agi_low
  - id: ny_it201.tcw.w1
    printed: "(39) (ny_it201.tcw.w1)"
    label: "Tax computation worksheet 1, line 9 (married filing jointly and qualifying surviving spouse)"
    type: NonNegDollars
    expr:
      op: copy
      from: {def: ny_tcw_first, bind: {agi: ny_it201.line33, ti: ny_it201.line38, rate: {param: ny.tcw.first.rate}, status: f1040.status}, line: tax}
    shown_when: ny_it201.h_w1
  - id: ny_it201.tcw.w7
    printed: "(39) (ny_it201.tcw.w7)"
    label: "Tax computation worksheet 7, line 9 (single and married filing separately)"
    type: NonNegDollars
    expr:
      op: copy
      from: {def: ny_tcw_first, bind: {agi: ny_it201.line33, ti: ny_it201.line38, rate: {param: ny.tcw.first.rate6}, status: f1040.status}, line: tax}
    shown_when: ny_it201.h_w7
  - id: ny_it201.tcw.w12
    printed: "(39) (ny_it201.tcw.w12)"
    label: "Tax computation worksheet 12, line 9 (head of household)"
    type: NonNegDollars
    expr:
      op: copy
      from: {def: ny_tcw_first, bind: {agi: ny_it201.line33, ti: ny_it201.line38, rate: {param: ny.tcw.first.rate6}, status: f1040.status}, line: tax}
    shown_when: ny_it201.h_w12
  - id: ny_it201.tcw.w2
    printed: "(39) (ny_it201.tcw.w2)"
    label: "Tax computation worksheet 2, line 10"
    type: NonNegDollars
    expr:
      op: copy
      from: {def: ny_tcw, bind: {agi: ny_it201.line33, ti: ny_it201.line38, start: {param: ny.tcw.mfj.w2.start}, recapture: {param: ny.tcw.mfj.w2.recapture}, incremental: {param: ny.tcw.mfj.w2.incremental}, status: f1040.status}, line: tax}
    shown_when: ny_it201.h_w2
  - id: ny_it201.tcw.w3
    printed: "(39) (ny_it201.tcw.w3)"
    label: "Tax computation worksheet 3, line 10"
    type: NonNegDollars
    expr:
      op: copy
      from: {def: ny_tcw, bind: {agi: ny_it201.line33, ti: ny_it201.line38, start: {param: ny.tcw.mfj.w3.start}, recapture: {param: ny.tcw.mfj.w3.recapture}, incremental: {param: ny.tcw.mfj.w3.incremental}, status: f1040.status}, line: tax}
    shown_when: ny_it201.h_w3
  - id: ny_it201.tcw.w4
    printed: "(39) (ny_it201.tcw.w4)"
    label: "Tax computation worksheet 4, line 10"
    type: NonNegDollars
    expr:
      op: copy
      from: {def: ny_tcw, bind: {agi: ny_it201.line33, ti: ny_it201.line38, start: {param: ny.tcw.mfj.w4.start}, recapture: {param: ny.tcw.mfj.w4.recapture}, incremental: {param: ny.tcw.mfj.w4.incremental}, status: f1040.status}, line: tax}
    shown_when: ny_it201.h_w4
  - id: ny_it201.tcw.w5
    printed: "(39) (ny_it201.tcw.w5)"
    label: "Tax computation worksheet 5, line 10"
    type: NonNegDollars
    expr:
      op: copy
      from: {def: ny_tcw, bind: {agi: ny_it201.line33, ti: ny_it201.line38, start: {param: ny.tcw.mfj.w5.start}, recapture: {param: ny.tcw.mfj.w5.recapture}, incremental: {param: ny.tcw.mfj.w5.incremental}, status: f1040.status}, line: tax}
    shown_when: ny_it201.h_w5
  - id: ny_it201.tcw.w8
    printed: "(39) (ny_it201.tcw.w8)"
    label: "Tax computation worksheet 8, line 10"
    type: NonNegDollars
    expr:
      op: copy
      from: {def: ny_tcw, bind: {agi: ny_it201.line33, ti: ny_it201.line38, start: {param: ny.tcw.single.w8.start}, recapture: {param: ny.tcw.single.w8.recapture}, incremental: {param: ny.tcw.single.w8.incremental}, status: f1040.status}, line: tax}
    shown_when: ny_it201.h_w8
  - id: ny_it201.tcw.w9
    printed: "(39) (ny_it201.tcw.w9)"
    label: "Tax computation worksheet 9, line 10"
    type: NonNegDollars
    expr:
      op: copy
      from: {def: ny_tcw, bind: {agi: ny_it201.line33, ti: ny_it201.line38, start: {param: ny.tcw.single.w9.start}, recapture: {param: ny.tcw.single.w9.recapture}, incremental: {param: ny.tcw.single.w9.incremental}, status: f1040.status}, line: tax}
    shown_when: ny_it201.h_w9
  - id: ny_it201.tcw.w10
    printed: "(39) (ny_it201.tcw.w10)"
    label: "Tax computation worksheet 10, line 10"
    type: NonNegDollars
    expr:
      op: copy
      from: {def: ny_tcw, bind: {agi: ny_it201.line33, ti: ny_it201.line38, start: {param: ny.tcw.single.w10.start}, recapture: {param: ny.tcw.single.w10.recapture}, incremental: {param: ny.tcw.single.w10.incremental}, status: f1040.status}, line: tax}
    shown_when: ny_it201.h_w10
  - id: ny_it201.tcw.w13
    printed: "(39) (ny_it201.tcw.w13)"
    label: "Tax computation worksheet 13, line 10"
    type: NonNegDollars
    expr:
      op: copy
      from: {def: ny_tcw, bind: {agi: ny_it201.line33, ti: ny_it201.line38, start: {param: ny.tcw.hoh.w13.start}, recapture: {param: ny.tcw.hoh.w13.recapture}, incremental: {param: ny.tcw.hoh.w13.incremental}, status: f1040.status}, line: tax}
    shown_when: ny_it201.h_w13
  - id: ny_it201.tcw.w14
    printed: "(39) (ny_it201.tcw.w14)"
    label: "Tax computation worksheet 14, line 10"
    type: NonNegDollars
    expr:
      op: copy
      from: {def: ny_tcw, bind: {agi: ny_it201.line33, ti: ny_it201.line38, start: {param: ny.tcw.hoh.w14.start}, recapture: {param: ny.tcw.hoh.w14.recapture}, incremental: {param: ny.tcw.hoh.w14.incremental}, status: f1040.status}, line: tax}
    shown_when: ny_it201.h_w14
  - id: ny_it201.tcw.w15
    printed: "(39) (ny_it201.tcw.w15)"
    label: "Tax computation worksheet 15, line 10"
    type: NonNegDollars
    expr:
      op: copy
      from: {def: ny_tcw, bind: {agi: ny_it201.line33, ti: ny_it201.line38, start: {param: ny.tcw.hoh.w15.start}, recapture: {param: ny.tcw.hoh.w15.recapture}, incremental: {param: ny.tcw.hoh.w15.incremental}, status: f1040.status}, line: tax}
    shown_when: ny_it201.h_w15
  - id: ny_it201.tcw.top
    printed: "(39) (ny_it201.tcw.top)"
    label: "Tax computation worksheets 6, 11 and 16: multiply line 38 by 10.9% (0.109)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.line38, rate: {param: ny.tcw.top_rate}}
    shown_when: ny_it201.h_agi_top
  - id: ny_it201.tcw.mfj
    printed: "(39) (ny_it201.tcw.mfj)"
    label: "Married filing jointly and qualifying surviving spouse: tax from worksheet 1, 2, 3, 4 or 5 by taxable income"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [ny_it201.line38, {param: ny.tcw.mfj.w1.ti_limit}]}
          then: ny_it201.tcw.w1
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line38, {param: ny.tcw.mfj.w1.ti_limit}]}
              - {op: test, le: [ny_it201.line38, {param: ny.tcw.mfj.w2.ti_limit}]}
          then: ny_it201.tcw.w2
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line38, {param: ny.tcw.mfj.w2.ti_limit}]}
              - {op: test, le: [ny_it201.line38, {param: ny.tcw.mfj.w3.ti_limit}]}
          then: ny_it201.tcw.w3
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line38, {param: ny.tcw.mfj.w3.ti_limit}]}
              - {op: test, le: [ny_it201.line38, {param: ny.tcw.mfj.w4.ti_limit}]}
          then: ny_it201.tcw.w4
        - guard: {op: test, gt: [ny_it201.line38, {param: ny.tcw.mfj.w4.ti_limit}]}
          then: ny_it201.tcw.w5
    shown_when: ny_it201.h_show_mfj
    note: "Each worksheet's line 33 condition (more than the worksheet's start) is implied by its taxable-income range, since line 38 cannot exceed line 33; the worksheets are selected by taxable income alone."
  - id: ny_it201.tcw.single
    printed: "(39) (ny_it201.tcw.single)"
    label: "Single and married filing separately: tax from worksheet 7, 8, 9 or 10 by taxable income"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [ny_it201.line38, {param: ny.tcw.single.w1.ti_limit}]}
          then: ny_it201.tcw.w7
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line38, {param: ny.tcw.single.w1.ti_limit}]}
              - {op: test, le: [ny_it201.line38, {param: ny.tcw.single.w8.ti_limit}]}
          then: ny_it201.tcw.w8
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line38, {param: ny.tcw.single.w8.ti_limit}]}
              - {op: test, le: [ny_it201.line38, {param: ny.tcw.single.w9.ti_limit}]}
          then: ny_it201.tcw.w9
        - guard: {op: test, gt: [ny_it201.line38, {param: ny.tcw.single.w9.ti_limit}]}
          then: ny_it201.tcw.w10
    shown_when: ny_it201.h_show_single
  - id: ny_it201.tcw.hoh
    printed: "(39) (ny_it201.tcw.hoh)"
    label: "Head of household: tax from worksheet 12, 13, 14 or 15 by taxable income"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [ny_it201.line38, {param: ny.tcw.hoh.w1.ti_limit}]}
          then: ny_it201.tcw.w12
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line38, {param: ny.tcw.hoh.w1.ti_limit}]}
              - {op: test, le: [ny_it201.line38, {param: ny.tcw.hoh.w13.ti_limit}]}
          then: ny_it201.tcw.w13
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line38, {param: ny.tcw.hoh.w13.ti_limit}]}
              - {op: test, le: [ny_it201.line38, {param: ny.tcw.hoh.w14.ti_limit}]}
          then: ny_it201.tcw.w14
        - guard: {op: test, gt: [ny_it201.line38, {param: ny.tcw.hoh.w14.ti_limit}]}
          then: ny_it201.tcw.w15
    shown_when: ny_it201.h_show_hoh
  - id: ny_it201.tcw.by_status
    printed: "(39) (ny_it201.tcw.by_status)"
    label: "Tax computation worksheet within your filing status (line 33 more than $107,650 but not more than $25,000,000)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ny_it201.h_fs_mfj, {const: true}]}
          then: ny_it201.tcw.mfj
        - guard: {op: test, eq: [ny_it201.h_fs_single, {const: true}]}
          then: ny_it201.tcw.single
        - guard: {op: test, eq: [ny_it201.h_fs_hoh, {const: true}]}
          then: ny_it201.tcw.hoh
    shown_when: ny_it201.h_agi_mid
  - id: ny_it201.tax_high
    printed: "(39) (ny_it201.tax_high)"
    label: "Tax computation – New York adjusted gross income of more than $107,650"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [ny_it201.line33, {param: ny.tcw.agi_top}]}
          then: ny_it201.tcw.top
        - guard: {op: test, le: [ny_it201.line33, {param: ny.tcw.agi_top}]}
          then: ny_it201.tcw.by_status
    shown_when: ny_it201.h_agi_high
  - id: ny_it201.line39
    printed: "39"
    label: "NYS tax on line 38 amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [ny_it201.line33, {param: ny.table.agi_limit}]}
          then: ny_it201.tax_low
        - guard: {op: test, gt: [ny_it201.line33, {param: ny.table.agi_limit}]}
          then: ny_it201.tax_high

  - id: ny_it201.hh_agi
    printed: "(Note 1)"
    label: "Federal adjusted gross income for the household credit tables (Form IT-201, line 19; Note 2: this amount could be 0 or a negative amount)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line19, take: {param: ny.zero}}
    note: "A zero or negative line 19 falls in the first band of every table ('$ (see Note 2) ... but not over'), so the amount is floored at 0 without changing the table result. The A6 Build America Bond adjustment is excluded by the special-condition-code refusal on line 1."
  - id: ny_it201.h_one
    printed: "(helper)"
    label: "One for you"
    type: Count
    expr: {op: param, ref: ny.one}
  - id: ny_it201.h_hh_spouse
    printed: "(helper)"
    label: "One for your spouse if Married filing joint return"
    type: Count
    expr: {op: keyed_lookup, table: ny_hh_spouse_count, keys: [f1040.status]}
  - id: ny_it201.hh_people
    printed: "(column)"
    label: "Number of dependents listed on Form IT-201, item H, plus one for you (and one for your spouse if Married filing joint return)"
    type: Count
    expr: {op: sum, of: [ny_it201.item_h_count, ny_it201.h_one, ny_it201.h_hh_spouse]}
  - id: ny_it201.h_max_people
    printed: "(helper)"
    label: "Column 7 (seven individuals)"
    type: Count
    expr: {op: param, ref: ny.hh.max_people}
  - id: ny_it201.hh_state_p1
    printed: "(table 2, column 1)"
    label: "New York State household credit table 2, column 1"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_state_t2_p1, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_city_p1
    printed: "(table 5, column 1)"
    label: "New York City household credit table 5, column 1"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_city_t5_p1, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_state_p2
    printed: "(table 2, column 2)"
    label: "New York State household credit table 2, column 2"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_state_t2_p2, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_city_p2
    printed: "(table 5, column 2)"
    label: "New York City household credit table 5, column 2"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_city_t5_p2, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_state_p3
    printed: "(table 2, column 3)"
    label: "New York State household credit table 2, column 3"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_state_t2_p3, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_city_p3
    printed: "(table 5, column 3)"
    label: "New York City household credit table 5, column 3"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_city_t5_p3, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_state_p4
    printed: "(table 2, column 4)"
    label: "New York State household credit table 2, column 4"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_state_t2_p4, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_city_p4
    printed: "(table 5, column 4)"
    label: "New York City household credit table 5, column 4"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_city_t5_p4, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_state_p5
    printed: "(table 2, column 5)"
    label: "New York State household credit table 2, column 5"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_state_t2_p5, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_city_p5
    printed: "(table 5, column 5)"
    label: "New York City household credit table 5, column 5"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_city_t5_p5, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_state_p6
    printed: "(table 2, column 6)"
    label: "New York State household credit table 2, column 6"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_state_t2_p6, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_city_p6
    printed: "(table 5, column 6)"
    label: "New York City household credit table 5, column 6"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_city_t5_p6, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_state_p7
    printed: "(table 2, column 7)"
    label: "New York State household credit table 2, column 7"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_state_t2_p7, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_city_p7
    printed: "(table 5, column 7)"
    label: "New York City household credit table 5, column 7"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_city_t5_p7, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.h_hh_state_step
    printed: "(helper)"
    label: "Table 2 'over 7' column amount for the row (equal in every printed row to column 7 minus column 6)"
    type: Dollars
    expr: {op: subtract, from: ny_it201.hh_state_p7, take: ny_it201.hh_state_p6}
    note: "No table interface supplies the 'over 7' column. In every printed row of table 2 (15, 15, 15, 15, 10, 10, 5, 5; 0 above $32,000) it equals column 7 minus column 6, so it is derived that way."
  - id: ny_it201.h_hh_state_step_n
    printed: "(helper)"
    label: "Over-7 amount times the number of individuals"
    type: Dollars
    expr: {op: multiply_count, amount: ny_it201.h_hh_state_step, count: ny_it201.hh_people}
  - id: ny_it201.h_hh_state_step_7
    printed: "(helper)"
    label: "Over-7 amount times 7"
    type: Dollars
    expr: {op: multiply_count, amount: ny_it201.h_hh_state_step, count: ny_it201.h_max_people}
  - id: ny_it201.h_hh_state_extra
    printed: "(helper)"
    label: "For each individual over 7, the over-7 column amount (Note 3)"
    type: Dollars
    expr: {op: subtract, from: ny_it201.h_hh_state_step_n, take: ny_it201.h_hh_state_step_7}
  - id: ny_it201.h_hh_state_over7_raw
    printed: "(helper)"
    label: "Column 7 amount plus the over-7 amounts (Note 3)"
    type: Dollars
    expr: {op: sum, of: [ny_it201.hh_state_p7, ny_it201.h_hh_state_extra]}
  - id: ny_it201.h_hh_state_over7
    printed: "(helper)"
    label: "Table 2 credit for more than 7 individuals"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.h_hh_state_over7_raw, take: {param: ny.zero}}
  - id: ny_it201.h_hh_city_step
    printed: "(helper)"
    label: "Table 5 'over 7' column amount for the row (equal in every printed row to column 7 minus column 6)"
    type: Dollars
    expr: {op: subtract, from: ny_it201.hh_city_p7, take: ny_it201.hh_city_p6}
    note: "No table interface supplies the 'over 7' column. In every printed row of table 5 (30, 25, 15, 10; 0 above $22,500) it equals column 7 minus column 6, so it is derived that way."
  - id: ny_it201.h_hh_city_step_n
    printed: "(helper)"
    label: "Over-7 amount times the number of individuals"
    type: Dollars
    expr: {op: multiply_count, amount: ny_it201.h_hh_city_step, count: ny_it201.hh_people}
  - id: ny_it201.h_hh_city_step_7
    printed: "(helper)"
    label: "Over-7 amount times 7"
    type: Dollars
    expr: {op: multiply_count, amount: ny_it201.h_hh_city_step, count: ny_it201.h_max_people}
  - id: ny_it201.h_hh_city_extra
    printed: "(helper)"
    label: "For each individual over 7, the over-7 column amount (Note 3)"
    type: Dollars
    expr: {op: subtract, from: ny_it201.h_hh_city_step_n, take: ny_it201.h_hh_city_step_7}
  - id: ny_it201.h_hh_city_over7_raw
    printed: "(helper)"
    label: "Column 7 amount plus the over-7 amounts (Note 3)"
    type: Dollars
    expr: {op: sum, of: [ny_it201.hh_city_p7, ny_it201.h_hh_city_extra]}
  - id: ny_it201.h_hh_city_over7
    printed: "(helper)"
    label: "Table 5 credit for more than 7 individuals"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.h_hh_city_over7_raw, take: {param: ny.zero}}
  - id: ny_it201.hh_state_t2
    printed: "(table 2)"
    label: "New York State household credit table 2 (Filing status 2, 4 and 5)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [ny_it201.hh_people, {const: 1, type: Count}]}
          then: ny_it201.hh_state_p1
        - guard: {op: test, eq: [ny_it201.hh_people, {const: 2, type: Count}]}
          then: ny_it201.hh_state_p2
        - guard: {op: test, eq: [ny_it201.hh_people, {const: 3, type: Count}]}
          then: ny_it201.hh_state_p3
        - guard: {op: test, eq: [ny_it201.hh_people, {const: 4, type: Count}]}
          then: ny_it201.hh_state_p4
        - guard: {op: test, eq: [ny_it201.hh_people, {const: 5, type: Count}]}
          then: ny_it201.hh_state_p5
        - guard: {op: test, eq: [ny_it201.hh_people, {const: 6, type: Count}]}
          then: ny_it201.hh_state_p6
        - guard: {op: test, eq: [ny_it201.hh_people, {const: 7, type: Count}]}
          then: ny_it201.hh_state_p7
        - guard: {op: test, gt: [ny_it201.hh_people, {const: 7, type: Count}]}
          then: ny_it201.h_hh_state_over7
  - id: ny_it201.hh_city_t5
    printed: "(table 5)"
    label: "New York City household credit table 5 (Filing status 2, 4 and 5)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [ny_it201.hh_people, {const: 1, type: Count}]}
          then: ny_it201.hh_city_p1
        - guard: {op: test, eq: [ny_it201.hh_people, {const: 2, type: Count}]}
          then: ny_it201.hh_city_p2
        - guard: {op: test, eq: [ny_it201.hh_people, {const: 3, type: Count}]}
          then: ny_it201.hh_city_p3
        - guard: {op: test, eq: [ny_it201.hh_people, {const: 4, type: Count}]}
          then: ny_it201.hh_city_p4
        - guard: {op: test, eq: [ny_it201.hh_people, {const: 5, type: Count}]}
          then: ny_it201.hh_city_p5
        - guard: {op: test, eq: [ny_it201.hh_people, {const: 6, type: Count}]}
          then: ny_it201.hh_city_p6
        - guard: {op: test, eq: [ny_it201.hh_people, {const: 7, type: Count}]}
          then: ny_it201.hh_city_p7
        - guard: {op: test, gt: [ny_it201.hh_people, {const: 7, type: Count}]}
          then: ny_it201.h_hh_city_over7
  - id: ny_it201.hh_state_t1
    printed: "(table 1)"
    label: "New York State household credit table 1 (Filing status 1 only, Single)"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_state_t1, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_city_t4
    printed: "(table 4)"
    label: "New York City household credit table 4 (Filing status 1 only, Single)"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_hh_city_t4, key: ny_it201.hh_agi, status: f1040.status}
  - id: ny_it201.hh_state_by_status
    printed: "(40)"
    label: "New York State household credit from the table for your filing status (1, 2, or 3)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "single"}]}
          then: ny_it201.hh_state_t1
        - guard:
            op: test
            any:
              - {op: test, eq: [f1040.status, {const: "mfj"}]}
              - {op: test, eq: [f1040.status, {const: "hoh"}]}
              - {op: test, eq: [f1040.status, {const: "qss"}]}
          then: ny_it201.hh_state_t2
        - guard: {op: test, eq: [f1040.status, {const: "mfs"}]}
          then: ny_it201.h_zero
    refuses: [ny_it201.h_fs_mfs]
    note: "Table 3 (married filing separately) uses both spouses' federal AGI and dependents from both returns; no table interface or input supplies it, so a separate filer who can claim the credit is refused."
  - id: ny_it201.hh_city_by_status
    printed: "(48)"
    label: "New York City household credit from the table for your filing status (4, 5, or 6)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [f1040.status, {const: "single"}]}
          then: ny_it201.hh_city_t4
        - guard:
            op: test
            any:
              - {op: test, eq: [f1040.status, {const: "mfj"}]}
              - {op: test, eq: [f1040.status, {const: "hoh"}]}
              - {op: test, eq: [f1040.status, {const: "qss"}]}
          then: ny_it201.hh_city_t5
        - guard: {op: test, eq: [f1040.status, {const: "mfs"}]}
          then: ny_it201.h_zero
    refuses: [ny_it201.h_fs_mfs]
    note: "Table 6 (married filing separately) uses both spouses' federal AGI and dependents from both returns; no table interface or input supplies it, so a separate filer who can claim the credit is refused."
  - id: ny_it201.line40
    printed: "40"
    label: "NYS household credit"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ny_it201.item_c, {const: true}]}
          then: ny_it201.h_zero
        - guard: {op: test, eq: [ny_it201.item_c, {const: false}]}
          then: ny_it201.hh_state_by_status
  - id: ny_it201.line41
    printed: "41"
    label: "Resident credit"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.resident_credit]
  - id: ny_it201.line42
    printed: "42"
    label: "Other NYS nonrefundable credits (Form IT-201-ATT, line 7)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.other_credits]
  - id: ny_it201.line43
    printed: "43"
    label: "Add lines 40, 41, and 42"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.line40, ny_it201.line41, ny_it201.line42]}
  - id: ny_it201.line44
    printed: "44"
    label: "Subtract line 43 from line 39 (if line 43 is more than line 39, enter 0)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line39, take: ny_it201.line43}
  - id: ny_it201.line45
    printed: "45"
    label: "Net other NYS taxes (Form IT-201-ATT, line 30)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.other_taxes]
  - id: ny_it201.line46
    printed: "46"
    label: "Total New York State taxes (add lines 44 and 45)"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.line44, ny_it201.line45]}
  - id: ny_it201.line47
    printed: "47"
    label: "NYC taxable income"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ny_it201.h_city, {const: true}]}
          then: ny_it201.line38
        - guard: {op: test, eq: [ny_it201.h_city, {const: false}]}
          then: ny_it201.h_zero
    note: "Without a Charitable Gifts Trust Fund itemized deduction (itemizers are refused at line 34), line 47 is the line 38 amount. A filer who was not a full-year NYC resident enters nothing; the interface does not distinguish a part-year NYC resident (Form IT-360.1, line 50) from a nonresident, so both are treated as nonresidents."
  - id: ny_it201.h_city_table
    printed: "(helper)"
    label: "Full-year NYC resident with line 47 less than $65,000 (use the NYC tax table)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_city, {const: true}]}
        - {op: test, lt: [ny_it201.line47, {param: ny.city.table.limit}]}
  - id: ny_it201.h_city_sched
    printed: "(helper)"
    label: "Full-year NYC resident with line 47 of $65,000 or more (use the NYC tax rate schedule)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_city, {const: true}]}
        - {op: test, ge: [ny_it201.line47, {param: ny.city.table.limit}]}
  - id: ny_it201.city_tax_table
    printed: "(47a) (ny_it201.city_tax_table)"
    label: "New York City resident tax on the line 47 amount from the 2025 New York City Tax Table"
    type: NonNegDollars
    expr: {op: table_lookup, table: ny_city_tax_table, key: ny_it201.line47, status: f1040.status}
    shown_when: ny_it201.h_city_table
  - id: ny_it201.h_cs_b1
    printed: "(helper)"
    label: "NYC tax rate schedule, first band: rate times line 47"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.line47, rate: {param: ny.city.b1.rate}}
  - id: ny_it201.h_cs_mfj_b2_excess
    printed: "(helper)"
    label: "NYC schedule (married filing jointly), excess over band 2 'over' amount"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line47, take: {param: ny.city.mfj.b2.over}}
  - id: ny_it201.h_cs_mfj_b2_product
    printed: "(helper)"
    label: "Band 2 rate times the excess"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.h_cs_mfj_b2_excess, rate: {param: ny.city.b2.rate}}
  - id: ny_it201.h_cs_mfj_b2_base
    printed: "(helper)"
    label: "Band 2 base amount"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.mfj.b2.base}
  - id: ny_it201.h_cs_mfj_b2_tax
    printed: "(helper)"
    label: "Band 2 tax"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.h_cs_mfj_b2_base, ny_it201.h_cs_mfj_b2_product]}
  - id: ny_it201.h_cs_mfj_b3_excess
    printed: "(helper)"
    label: "NYC schedule (married filing jointly), excess over band 3 'over' amount"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line47, take: {param: ny.city.mfj.b3.over}}
  - id: ny_it201.h_cs_mfj_b3_product
    printed: "(helper)"
    label: "Band 3 rate times the excess"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.h_cs_mfj_b3_excess, rate: {param: ny.city.b3.rate}}
  - id: ny_it201.h_cs_mfj_b3_base
    printed: "(helper)"
    label: "Band 3 base amount"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.mfj.b3.base}
  - id: ny_it201.h_cs_mfj_b3_tax
    printed: "(helper)"
    label: "Band 3 tax"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.h_cs_mfj_b3_base, ny_it201.h_cs_mfj_b3_product]}
  - id: ny_it201.h_cs_mfj_b4_excess
    printed: "(helper)"
    label: "NYC schedule (married filing jointly), excess over band 4 'over' amount"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line47, take: {param: ny.city.mfj.b4.over}}
  - id: ny_it201.h_cs_mfj_b4_product
    printed: "(helper)"
    label: "Band 4 rate times the excess"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.h_cs_mfj_b4_excess, rate: {param: ny.city.b4.rate}}
  - id: ny_it201.h_cs_mfj_b4_base
    printed: "(helper)"
    label: "Band 4 base amount"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.mfj.b4.base}
  - id: ny_it201.h_cs_mfj_b4_tax
    printed: "(helper)"
    label: "Band 4 tax"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.h_cs_mfj_b4_base, ny_it201.h_cs_mfj_b4_product]}
  - id: ny_it201.h_cs_mfj
    printed: "(helper)"
    label: "NYC tax rate schedule, married filing jointly and qualifying surviving spouse"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [ny_it201.line47, {param: ny.city.mfj.b1.upper}]}
          then: ny_it201.h_cs_b1
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line47, {param: ny.city.mfj.b1.upper}]}
              - {op: test, le: [ny_it201.line47, {param: ny.city.mfj.b2.upper}]}
          then: ny_it201.h_cs_mfj_b2_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line47, {param: ny.city.mfj.b2.upper}]}
              - {op: test, le: [ny_it201.line47, {param: ny.city.mfj.b3.upper}]}
          then: ny_it201.h_cs_mfj_b3_tax
        - guard: {op: test, gt: [ny_it201.line47, {param: ny.city.mfj.b3.upper}]}
          then: ny_it201.h_cs_mfj_b4_tax
  - id: ny_it201.h_cs_single_b2_excess
    printed: "(helper)"
    label: "NYC schedule (single), excess over band 2 'over' amount"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line47, take: {param: ny.city.single.b2.over}}
  - id: ny_it201.h_cs_single_b2_product
    printed: "(helper)"
    label: "Band 2 rate times the excess"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.h_cs_single_b2_excess, rate: {param: ny.city.b2.rate}}
  - id: ny_it201.h_cs_single_b2_base
    printed: "(helper)"
    label: "Band 2 base amount"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.single.b2.base}
  - id: ny_it201.h_cs_single_b2_tax
    printed: "(helper)"
    label: "Band 2 tax"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.h_cs_single_b2_base, ny_it201.h_cs_single_b2_product]}
  - id: ny_it201.h_cs_single_b3_excess
    printed: "(helper)"
    label: "NYC schedule (single), excess over band 3 'over' amount"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line47, take: {param: ny.city.single.b3.over}}
  - id: ny_it201.h_cs_single_b3_product
    printed: "(helper)"
    label: "Band 3 rate times the excess"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.h_cs_single_b3_excess, rate: {param: ny.city.b3.rate}}
  - id: ny_it201.h_cs_single_b3_base
    printed: "(helper)"
    label: "Band 3 base amount"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.single.b3.base}
  - id: ny_it201.h_cs_single_b3_tax
    printed: "(helper)"
    label: "Band 3 tax"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.h_cs_single_b3_base, ny_it201.h_cs_single_b3_product]}
  - id: ny_it201.h_cs_single_b4_excess
    printed: "(helper)"
    label: "NYC schedule (single), excess over band 4 'over' amount"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line47, take: {param: ny.city.single.b4.over}}
  - id: ny_it201.h_cs_single_b4_product
    printed: "(helper)"
    label: "Band 4 rate times the excess"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.h_cs_single_b4_excess, rate: {param: ny.city.b4.rate}}
  - id: ny_it201.h_cs_single_b4_base
    printed: "(helper)"
    label: "Band 4 base amount"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.single.b4.base}
  - id: ny_it201.h_cs_single_b4_tax
    printed: "(helper)"
    label: "Band 4 tax"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.h_cs_single_b4_base, ny_it201.h_cs_single_b4_product]}
  - id: ny_it201.h_cs_single
    printed: "(helper)"
    label: "NYC tax rate schedule, single and married filing separately"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [ny_it201.line47, {param: ny.city.single.b1.upper}]}
          then: ny_it201.h_cs_b1
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line47, {param: ny.city.single.b1.upper}]}
              - {op: test, le: [ny_it201.line47, {param: ny.city.single.b2.upper}]}
          then: ny_it201.h_cs_single_b2_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line47, {param: ny.city.single.b2.upper}]}
              - {op: test, le: [ny_it201.line47, {param: ny.city.single.b3.upper}]}
          then: ny_it201.h_cs_single_b3_tax
        - guard: {op: test, gt: [ny_it201.line47, {param: ny.city.single.b3.upper}]}
          then: ny_it201.h_cs_single_b4_tax
  - id: ny_it201.h_cs_hoh_b2_excess
    printed: "(helper)"
    label: "NYC schedule (head of household), excess over band 2 'over' amount"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line47, take: {param: ny.city.hoh.b2.over}}
  - id: ny_it201.h_cs_hoh_b2_product
    printed: "(helper)"
    label: "Band 2 rate times the excess"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.h_cs_hoh_b2_excess, rate: {param: ny.city.b2.rate}}
  - id: ny_it201.h_cs_hoh_b2_base
    printed: "(helper)"
    label: "Band 2 base amount"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.hoh.b2.base}
  - id: ny_it201.h_cs_hoh_b2_tax
    printed: "(helper)"
    label: "Band 2 tax"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.h_cs_hoh_b2_base, ny_it201.h_cs_hoh_b2_product]}
  - id: ny_it201.h_cs_hoh_b3_excess
    printed: "(helper)"
    label: "NYC schedule (head of household), excess over band 3 'over' amount"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line47, take: {param: ny.city.hoh.b3.over}}
  - id: ny_it201.h_cs_hoh_b3_product
    printed: "(helper)"
    label: "Band 3 rate times the excess"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.h_cs_hoh_b3_excess, rate: {param: ny.city.b3.rate}}
  - id: ny_it201.h_cs_hoh_b3_base
    printed: "(helper)"
    label: "Band 3 base amount"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.hoh.b3.base}
  - id: ny_it201.h_cs_hoh_b3_tax
    printed: "(helper)"
    label: "Band 3 tax"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.h_cs_hoh_b3_base, ny_it201.h_cs_hoh_b3_product]}
  - id: ny_it201.h_cs_hoh_b4_excess
    printed: "(helper)"
    label: "NYC schedule (head of household), excess over band 4 'over' amount"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line47, take: {param: ny.city.hoh.b4.over}}
  - id: ny_it201.h_cs_hoh_b4_product
    printed: "(helper)"
    label: "Band 4 rate times the excess"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.h_cs_hoh_b4_excess, rate: {param: ny.city.b4.rate}}
  - id: ny_it201.h_cs_hoh_b4_base
    printed: "(helper)"
    label: "Band 4 base amount"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.hoh.b4.base}
  - id: ny_it201.h_cs_hoh_b4_tax
    printed: "(helper)"
    label: "Band 4 tax"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.h_cs_hoh_b4_base, ny_it201.h_cs_hoh_b4_product]}
  - id: ny_it201.h_cs_hoh
    printed: "(helper)"
    label: "NYC tax rate schedule, head of household"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [ny_it201.line47, {param: ny.city.hoh.b1.upper}]}
          then: ny_it201.h_cs_b1
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line47, {param: ny.city.hoh.b1.upper}]}
              - {op: test, le: [ny_it201.line47, {param: ny.city.hoh.b2.upper}]}
          then: ny_it201.h_cs_hoh_b2_tax
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line47, {param: ny.city.hoh.b2.upper}]}
              - {op: test, le: [ny_it201.line47, {param: ny.city.hoh.b3.upper}]}
          then: ny_it201.h_cs_hoh_b3_tax
        - guard: {op: test, gt: [ny_it201.line47, {param: ny.city.hoh.b3.upper}]}
          then: ny_it201.h_cs_hoh_b4_tax
  - id: ny_it201.city_tax_schedule
    printed: "(47a) (ny_it201.city_tax_schedule)"
    label: "New York City resident tax on the line 47 amount from the New York City tax rate schedule"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ny_it201.h_fs_mfj, {const: true}]}
          then: ny_it201.h_cs_mfj
        - guard: {op: test, eq: [ny_it201.h_fs_single, {const: true}]}
          then: ny_it201.h_cs_single
        - guard: {op: test, eq: [ny_it201.h_fs_hoh, {const: true}]}
          then: ny_it201.h_cs_hoh
    shown_when: ny_it201.h_city_sched
    note: "The NYC rate schedule itself is not in the supplied pages; it is built from the supplied ny.city band parameters as base plus rate times the excess over the band's 'over' amount, each product rounded half-up to the cent (the form takes whole dollars; no further rounding is stated)."
  - id: ny_it201.line47a
    printed: "47a"
    label: "NYC resident tax on line 47 amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ny_it201.h_city, {const: false}]}
          then: ny_it201.h_zero
        - guard: {op: test, eq: [ny_it201.h_city_table, {const: true}]}
          then: ny_it201.city_tax_table
        - guard: {op: test, eq: [ny_it201.h_city_sched, {const: true}]}
          then: ny_it201.city_tax_schedule
  - id: ny_it201.line48
    printed: "48"
    label: "NYC household credit"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            any:
              - {op: test, eq: [ny_it201.h_city, {const: false}]}
              - {op: test, eq: [ny_it201.item_c, {const: true}]}
          then: ny_it201.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [ny_it201.h_city, {const: true}]}
              - {op: test, eq: [ny_it201.item_c, {const: false}]}
          then: ny_it201.hh_city_by_status
  - id: ny_it201.line49
    printed: "49"
    label: "Subtract line 48 from line 47a (if line 48 is more than line 47a, enter 0)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line47a, take: ny_it201.line48}
  - id: ny_it201.line50
    printed: "50"
    label: "Part-year NYC resident tax (Form IT-360.1)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    note: "Open: a part-year NYC resident completes Form IT-360.1, but the closed interface has no part-year question (ask.city_resident asks only about full-year residence) and no IT-360.1 amount. Encoded as 0; part-year NYC residents are outside the supported scope and cannot be screened out here."
  - id: ny_it201.line51
    printed: "51"
    label: "Other NYC taxes (Form IT-201-ATT, line 34)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.other_taxes]
  - id: ny_it201.line52
    printed: "52"
    label: "Add lines 49, 50, and 51"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.line49, ny_it201.line50, ny_it201.line51]}
  - id: ny_it201.line53
    printed: "53"
    label: "NYC nonrefundable credits (Form IT-201-ATT, line 10)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.city_credits]
  - id: ny_it201.line54
    printed: "54"
    label: "Subtract line 53 from line 52 (if line 53 is more than line 52, enter 0)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line52, take: ny_it201.line53}
  - id: ny_it201.line54a
    printed: "54a"
    label: "MCTMT net earnings base for Zone 1"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.mctmt]
  - id: ny_it201.line54b
    printed: "54b"
    label: "MCTMT net earnings base for Zone 2"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.mctmt]
  - id: ny_it201.line54c
    printed: "54c"
    label: "MCTMT for Zone 1 (multiply line 54a by 0.60% (0.0060))"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.line54a, rate: {param: ny.mctmt.zone1}}
  - id: ny_it201.line54d
    printed: "54d"
    label: "MCTMT for Zone 2 (multiply line 54b by 0.34% (0.0034))"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.line54b, rate: {param: ny.mctmt.zone2}}
  - id: ny_it201.line54e
    printed: "54e"
    label: "Total MCTMT (add lines 54c and 54d)"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.line54c, ny_it201.line54d]}
  - id: ny_it201.line55
    printed: "55"
    label: "Yonkers resident income tax surcharge"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.yonkers]
  - id: ny_it201.line56
    printed: "56"
    label: "Yonkers nonresident earnings tax (Form Y-203)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.yonkers]
  - id: ny_it201.line57
    printed: "57"
    label: "Part-year Yonkers resident income tax surcharge (Form IT-360.1)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.yonkers]
  - id: ny_it201.line58
    printed: "58"
    label: "Total New York City and Yonkers taxes / surcharges and MCTMT (add lines 54 and 54e through 57)"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.line54, ny_it201.line54e, ny_it201.line55, ny_it201.line56, ny_it201.line57]}

  - id: ny_it201.sut.b1
    printed: "(chart) (ny_it201.sut.b1)"
    label: "Sales and use tax chart: federal adjusted gross income up to $15,000"
    type: NonNegDollars
    expr: {op: param, ref: ny.sut.b1.amount}
  - id: ny_it201.sut.b2
    printed: "(chart) (ny_it201.sut.b2)"
    label: "Sales and use tax chart: $15,001 - $30,000"
    type: NonNegDollars
    expr: {op: param, ref: ny.sut.b2.amount}
  - id: ny_it201.sut.b3
    printed: "(chart) (ny_it201.sut.b3)"
    label: "Sales and use tax chart: $30,001 - $50,000"
    type: NonNegDollars
    expr: {op: param, ref: ny.sut.b3.amount}
  - id: ny_it201.sut.b4
    printed: "(chart) (ny_it201.sut.b4)"
    label: "Sales and use tax chart: $50,001 - $75,000"
    type: NonNegDollars
    expr: {op: param, ref: ny.sut.b4.amount}
  - id: ny_it201.sut.b5
    printed: "(chart) (ny_it201.sut.b5)"
    label: "Sales and use tax chart: $75,001 - $100,000"
    type: NonNegDollars
    expr: {op: param, ref: ny.sut.b5.amount}
  - id: ny_it201.sut.b6
    printed: "(chart) (ny_it201.sut.b6)"
    label: "Sales and use tax chart: $100,001 - $150,000"
    type: NonNegDollars
    expr: {op: param, ref: ny.sut.b6.amount}
  - id: ny_it201.sut.b7
    printed: "(chart) (ny_it201.sut.b7)"
    label: "Sales and use tax chart: $150,001 - $200,000"
    type: NonNegDollars
    expr: {op: param, ref: ny.sut.b7.amount}
  - id: ny_it201.h_sut_income
    printed: "(helper)"
    label: "Federal adjusted gross income (line 19), not less than 0"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line19, take: {param: ny.zero}}
  - id: ny_it201.sut.top_product
    printed: "(chart) (ny_it201.sut.top_product)"
    label: "Sales and use tax chart, $200,001 and greater: 0.0175% (0.000175) of income"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.h_sut_income, rate: {param: ny.sut.top_rate}}
  - id: ny_it201.sut.cap
    printed: "(chart) (ny_it201.sut.cap)"
    label: "Sales and use tax chart, $200,001 and greater: $125"
    type: NonNegDollars
    expr: {op: param, ref: ny.sut.cap}
  - id: ny_it201.sut.top
    printed: "(chart) (ny_it201.sut.top)"
    label: "0.0175% (0.000175) of income, or $125, whichever amount is smaller"
    type: NonNegDollars
    expr: {op: smaller_of, of: [ny_it201.sut.top_product, ny_it201.sut.cap]}
  - id: ny_it201.sut.chart
    printed: "(chart) (ny_it201.sut.chart)"
    label: "Sales and use tax chart: amount for your federal adjusted gross income (line 19)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [ny_it201.line19, {param: ny.sut.b1.upper}]}
          then: ny_it201.sut.b1
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line19, {param: ny.sut.b1.upper}]}
              - {op: test, le: [ny_it201.line19, {param: ny.sut.b2.upper}]}
          then: ny_it201.sut.b2
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line19, {param: ny.sut.b2.upper}]}
              - {op: test, le: [ny_it201.line19, {param: ny.sut.b3.upper}]}
          then: ny_it201.sut.b3
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line19, {param: ny.sut.b3.upper}]}
              - {op: test, le: [ny_it201.line19, {param: ny.sut.b4.upper}]}
          then: ny_it201.sut.b4
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line19, {param: ny.sut.b4.upper}]}
              - {op: test, le: [ny_it201.line19, {param: ny.sut.b5.upper}]}
          then: ny_it201.sut.b5
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line19, {param: ny.sut.b5.upper}]}
              - {op: test, le: [ny_it201.line19, {param: ny.sut.b6.upper}]}
          then: ny_it201.sut.b6
        - guard:
            op: test
            all:
              - {op: test, gt: [ny_it201.line19, {param: ny.sut.b6.upper}]}
              - {op: test, le: [ny_it201.line19, {param: ny.sut.b7.upper}]}
          then: ny_it201.sut.b7
        - guard: {op: test, gt: [ny_it201.line19, {param: ny.sut.b7.upper}]}
          then: ny_it201.sut.top
    refuses: [ny_it201.ask.use_tax_st141, ny_it201.ask.abode_part_year]
    note: "Bands are whole-dollar ranges ('$15,001 - $30,000'); each is read as over the previous upper amount and not over its own. The 0.0175% product is rounded half-up to the cent (no rounding is stated). Form ST-141 cases and the part-year abode proration (months over 12) are refused."
  - id: ny_it201.line59
    printed: "59"
    label: "Sales or use tax (do not leave blank)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ny_it201.ask.owes_use_tax, {const: false}]}
          then: ny_it201.h_zero
        - guard: {op: test, eq: [ny_it201.ask.owes_use_tax, {const: true}]}
          then: ny_it201.sut.chart
  - id: ny_it201.line60
    printed: "60"
    label: "Voluntary contributions (Form IT-227, Part 2, line 1)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.contributions]
  - id: ny_it201.line61
    printed: "61"
    label: "Total New York State, New York City, Yonkers, and sales or use taxes, MCTMT, and voluntary contributions (add lines 46, 58, 59, and 60)"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.line46, ny_it201.line58, ny_it201.line59, ny_it201.line60]}
  - id: ny_it201.line62
    printed: "62"
    label: "Enter amount from line 61"
    type: NonNegDollars
    expr: {op: copy, from: ny_it201.line61}
  - id: ny_it201.line63
    printed: "63"
    label: "Empire State child credit"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    note: "Open: the credit is figured on Form IT-213, whose text is not supplied, and the closed interface has no screening question for a qualifying child under 17. Encoded as 0; a filer with a qualifying child may be understated and the project should add a screen."
  - id: ny_it201.line64
    printed: "64"
    label: "NYS/NYC child and dependent care credit"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.dependent_care]
  - id: ny_it201.h_fed_eic
    printed: "(helper)"
    label: "A federal earned income credit is claimed (federal Form 1040, line 27a, more than 0)"
    type: Bool
    expr: {op: test, gt: [f1040.line27a, {const: 0}]}
  - id: ny_it201.line65
    printed: "65"
    label: "NYS earned income credit (EIC)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.h_fed_eic]
    note: "Form IT-215 is not supplied; a return claiming the federal earned income credit is refused. A filer who could have claimed it but did not is not screened by the interface."
  - id: ny_it201.line66
    printed: "66"
    label: "NYS noncustodial parent EIC"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.noncustodial]
  - id: ny_it201.line67
    printed: "67"
    label: "Real property tax credit"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.real_property_credit]
  - id: ny_it201.line68
    printed: "68"
    label: "College tuition credit"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.college_tuition]
  - id: ny_it201.stc_income
    printed: "(69) (ny_it201.stc_income)"
    label: "Income for the NYC school tax credit: federal adjusted gross income (line 19) minus IRA distributions (line 9)"
    type: Dollars
    expr: {op: subtract, from: ny_it201.line19, take: ny_it201.line9}
  - id: ny_it201.stc_fixed_amount
    printed: "(69) (ny_it201.stc_fixed_amount)"
    label: "Table 1 - Full-year New York City residents: New York City school tax credit for your filing status"
    type: NonNegDollars
    expr: {op: param, ref: ny.stc.fixed}
  - id: ny_it201.line69
    printed: "69"
    label: "NYC school tax credit (fixed amount)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [ny_it201.h_city, {const: true}]}
              - {op: test, eq: [ny_it201.item_c, {const: false}]}
              - {op: test, le: [ny_it201.stc_income, {param: ny.stc.fixed.limit}]}
          then: ny_it201.stc_fixed_amount
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [ny_it201.h_city, {const: true}]}
                - {op: test, eq: [ny_it201.item_c, {const: false}]}
                - {op: test, le: [ny_it201.stc_income, {param: ny.stc.fixed.limit}]}
          then: ny_it201.h_zero
  - id: ny_it201.stc_rr_low
    printed: "(69a) (ny_it201.stc_rr_low)"
    label: "0.171% of city taxable income"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.line47, rate: {param: ny.stc.rr.low_rate}}
  - id: ny_it201.stc_rr_excess
    printed: "(69a) (ny_it201.stc_rr_excess)"
    label: "Excess of city taxable income over $21,600 ($12,000 single and married filing separately; $14,400 head of household)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line47, take: {param: ny.stc.rr.over}}
  - id: ny_it201.stc_rr_excess_product
    printed: "(69a) (ny_it201.stc_rr_excess_product)"
    label: "0.228% of the excess"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.stc_rr_excess, rate: {param: ny.stc.rr.high_rate}}
  - id: ny_it201.stc_rr_base
    printed: "(69a) (ny_it201.stc_rr_base)"
    label: "$37 ($21 single and married filing separately; $25 head of household)"
    type: NonNegDollars
    expr: {op: param, ref: ny.stc.rr.base}
  - id: ny_it201.stc_rr_high
    printed: "(69a) (ny_it201.stc_rr_high)"
    label: "Base amount plus 0.228% of the excess"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.stc_rr_base, ny_it201.stc_rr_excess_product]}
  - id: ny_it201.stc_rr
    printed: "(69a) (ny_it201.stc_rr)"
    label: "Calculation of NYC school tax credit (rate reduction amount) for your filing status"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [ny_it201.line47, {param: ny.stc.rr.over}]}
          then: ny_it201.stc_rr_low
        - guard: {op: test, gt: [ny_it201.line47, {param: ny.stc.rr.over}]}
          then: ny_it201.stc_rr_high
    note: "The printed schedules stop at city taxable income of $500,000; above that the second band's formula is applied (the $500,000 income test on line 69a governs eligibility). Products are rounded half-up to the cent."
  - id: ny_it201.line69a
    printed: "69a"
    label: "NYC school tax credit (rate reduction amount)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [ny_it201.h_city, {const: true}]}
              - {op: test, eq: [ny_it201.item_c, {const: false}]}
              - {op: test, le: [ny_it201.stc_income, {param: ny.stc.rr.limit}]}
          then: ny_it201.stc_rr
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [ny_it201.h_city, {const: true}]}
                - {op: test, eq: [ny_it201.item_c, {const: false}]}
                - {op: test, le: [ny_it201.stc_income, {param: ny.stc.rr.limit}]}
          then: ny_it201.h_zero
  - id: ny_it201.line70
    printed: "70"
    label: "NYC earned income credit"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.h_fed_eic]
  - id: ny_it201.h_it270_possible
    printed: "(helper)"
    label: "May qualify for the NYC income tax elimination credit: NYC resident, one or more dependents in item H, and federal AGI not more than $5,000 above the highest income threshold for the filing status"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.h_city, {const: true}]}
        - {op: test, ge: [ny_it201.item_h_count, {const: 1, type: Count}]}
        - {op: test, le: [ny_it201.line19, {param: ny.it270.max_threshold_plus}]}
  - id: ny_it201.line70a
    printed: "70a"
    label: "NYC income tax elimination credit"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.h_it270_possible]
    note: "Form IT-270's partial-credit percentage reduction is not in the supplied text, so a filer who may qualify (by the IT-270-I eligibility tests that can be checked here) is refused; otherwise the credit is 0."
  - id: ny_it201.line71
    printed: "71"
    label: "Other refundable credits (Form IT-201-ATT, line 18)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.other_credits]
  - id: ny_it201.line72
    printed: "72"
    label: "Total New York State tax withheld"
    type: NonNegDollars
    expr: {op: sum_over, collection: ny_it2, field: ny_it2.state_whole}
    refuses: [ny_it201.ask.other_withholding]
  - id: ny_it201.line73
    printed: "73"
    label: "Total New York City tax withheld"
    type: NonNegDollars
    expr: {op: sum_over, collection: ny_it2, field: ny_it2.city_whole}
    refuses: [ny_it201.ask.other_withholding]
  - id: ny_it201.line74
    printed: "74"
    label: "Total Yonkers tax withheld"
    type: NonNegDollars
    expr: {op: sum_over, collection: ny_it2, field: ny_it2.yonkers_withheld}
    refuses: [ny_it201.ask.other_withholding]
  - id: ny_it201.line76
    printed: "76"
    label: "Total payments (add lines 63 through 75)"
    type: NonNegDollars
    expr:
      op: sum
      of: [ny_it201.line63, ny_it201.line64, ny_it201.line65, ny_it201.line66, ny_it201.line67, ny_it201.line68, ny_it201.line69, ny_it201.line69a, ny_it201.line70, ny_it201.line70a, ny_it201.line71, ny_it201.line72, ny_it201.line73, ny_it201.line74, ny_it201.line75]
  - id: ny_it201.tax_due
    printed: "(80)"
    label: "Amount you owe before penalties (if line 76 is less than line 62, subtract line 76 from line 62)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line62, take: ny_it201.line76}
  - id: ny_it201.prepayments
    printed: "(81) (ny_it201.prepayments)"
    label: "Total 2025 prepayments (withholding and estimated tax payments)"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.line72, ny_it201.line73, ny_it201.line74, ny_it201.line75]}
  - id: ny_it201.safe_harbor_100
    printed: "(81) (ny_it201.safe_harbor_100)"
    label: "100% of your 2024 New York income tax based on a 12-month return"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.ask.prior_year_tax, rate: {param: ny.est.prior_rate}}
  - id: ny_it201.safe_harbor_110
    printed: "(81) (ny_it201.safe_harbor_110)"
    label: "110% of your 2024 New York income tax based on a 12-month return"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.ask.prior_year_tax, rate: {param: ny.est.prior_rate_high}}
  - id: ny_it201.safe_harbor
    printed: "(81) (ny_it201.safe_harbor)"
    label: "Required prepayments: 100% of 2024 tax, or 110% if 2024 New York AGI was more than $150,000 ($75,000 married filing separately)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [ny_it201.ask.prior_agi_high, {const: true}]}
          then: ny_it201.safe_harbor_110
        - guard: {op: test, eq: [ny_it201.ask.prior_agi_high, {const: false}]}
          then: ny_it201.safe_harbor_100
    note: "The farmer or fisherman exception to the 110% rule has no input; the 110% figure is used whenever 2024 AGI was over the limit."
  - id: ny_it201.h_income_tax_2025
    printed: "(helper)"
    label: "Income tax shown on your 2025 return (lines 46 and 58)"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.line46, ny_it201.line58]}
    note: "Open: 'income tax shown on your 2025 return' is read as New York State, City, Yonkers taxes and MCTMT (lines 46 and 58), excluding sales or use tax and voluntary contributions."
  - id: ny_it201.h_est_share
    printed: "(helper)"
    label: "10% of the income tax shown on your 2025 return"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: ny_it201.h_income_tax_2025, rate: {param: ny.est.share}}
  - id: ny_it201.h_safe_met
    printed: "(helper)"
    label: "2025 prepayments equal at least the required percentage of 2024 New York income tax based on a 12-month return"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [ny_it201.ask.prior_full_year, {const: true}]}
        - {op: test, ge: [ny_it201.prepayments, ny_it201.safe_harbor]}
  - id: ny_it201.h_due_test
    printed: "(helper)"
    label: "Line 80 is $300 or more and represents more than 10% of the income tax shown on your 2025 return"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, ge: [ny_it201.tax_due, {param: ny.est.min_due}]}
        - {op: test, gt: [ny_it201.tax_due, ny_it201.h_est_share]}
  - id: ny_it201.h_pen_possible
    printed: "(helper)"
    label: "You may owe an estimated tax penalty"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [ny_it201.ask.est_late, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [ny_it201.h_due_test, {const: true}]}
            - {op: test, not: {op: test, eq: [ny_it201.h_safe_met, {const: true}]}}
  - id: ny_it201.line81
    printed: "81"
    label: "Estimated tax penalty (include this amount in line 80 or reduce the overpayment on line 77)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.h_pen_possible]
    note: "The penalty is figured on Form IT-2105.9, not supplied; where the instructions say a penalty may be owed the line is refused, otherwise it is 0."
  - id: ny_it201.line82
    printed: "82"
    label: "Other penalties and interest"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.late_penalty]
  - id: ny_it201.overpaid_before_penalty
    printed: "(77)"
    label: "Overpayment (if line 76 is more than line 62, subtract line 62 from line 76)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line76, take: ny_it201.line62}
  - id: ny_it201.line77
    printed: "77"
    label: "Amount overpaid (if line 76 is more than line 62, subtract line 62 from line 76), net of any estimated tax penalty"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.overpaid_before_penalty, take: ny_it201.line81}
  - id: ny_it201.h_line79_excess
    printed: "(helper)"
    label: "Line 79 is more than line 77"
    type: Bool
    expr: {op: test, gt: [ny_it201.line79, ny_it201.line77]}
  - id: ny_it201.line78
    printed: "78"
    label: "Amount of line 77 available for refund (subtract line 79 from line 77)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line77, take: ny_it201.line79}
    refuses: [{when: ny_it201.h_line79_excess, when_known: true}]
  - id: ny_it201.line78a
    printed: "78a"
    label: "Amount of line 78 that you want to deposit into a NYS 529 account (Form IT-195, line 4)"
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    refuses: [ny_it201.ask.refund_529]
  - id: ny_it201.line78b
    printed: "78b"
    label: "Total refund after NYS 529 account deposit (subtract line 78a from line 78)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line78, take: ny_it201.line78a}
  - id: ny_it201.h_pen_excess
    printed: "(helper)"
    label: "Estimated tax penalty greater than the overpayment: the difference"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_it201.line81, take: ny_it201.overpaid_before_penalty}
  - id: ny_it201.line80
    printed: "80"
    label: "Amount you owe (if line 76 is less than line 62, subtract line 76 from line 62), plus any estimated tax penalty and other penalties and interest"
    type: NonNegDollars
    expr: {op: sum, of: [ny_it201.tax_due, ny_it201.h_pen_excess, ny_it201.line82]}
    note: "Line 80 is the tax owed plus the estimated tax penalty (all of it when tax is owed; only the part exceeding the overpayment otherwise) plus line 82, which the instructions say to include in line 80."
```
```
