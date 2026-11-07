# Transcription agreement — ny_it201

Second transcription of `Form IT-201 (2025), Resident Income Tax Return — New York State and New York City` by an isolated model (spec 6.5), compared line by line with `forms/ny/2025/ny_it201.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-04 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
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
{"const": 0}
```

Second transcription's note: LIMITATION, NOT A COMPUTATION: this line is not correctly encoded. The zero is a stand-in only, and a return built on it is wrong whenever the filer has wages. This line must be replaced before any return is produced. The archived Form IT-201 page 2 prints this line as "Wages, salaries, tips, etc." and says nothing more. The supplied IT-201-I pages (3-5, 13-14, 30-31) do not include the line 1 instruction, so the supplied text does not say where the amount comes from. The federal line carrying the same wording (federal Form 1040, line 1z) is not in the supplied catalog. No W-2 collection field is in the catalog either. The input interface is closed, so no new input may be added. Nothing in the supplied interface can carry the filer's wages. The ny.zero parameter is the only well-formed expression available; it encodes no amount from the IRS or New York text. Fix: replace it with {op: copy, from: <federal Form 1040 line 1z id>} once that line, and the New York line 1 instruction naming it, are added to the catalog.

Ruling: interface gap; ny_it201i p. 7, Lines 1 through 19, "The amount entered on line 1 (wages, salaries, tips, etc.) should be the same as the amount reported on federal Form 1040, line 1z." R4 reran this line because its refusals read ny_it201.ask.state_resident, restructured into a question and a list (no word lost). The line-scoped request gave only the pages the line and its refusals cite (IT-201-I pp. 3-5, 13-14, 30-31; line 1 cites only the form page), so neither the p. 7 instruction nor federal Form 1040 line 1z was in the request, and the reply entered a zero stand-in, which its note says is not a computation; it differs wherever there are wages (35 value differences, all on refused records; on the federal fixtures, which carry no New York answers, the project is unknown or refuses at the residency gates). The project's line follows p. 7, rounded by amb.ny.2025.whole_dollars, as the prior ruling. executable-triage-v2 on this pass's reply (`.transcription/ny_it201.lines-6b86b273ff34.response.txt`, merged with the project's lines it names; a scratch run of triage.mjs, since triage.py evaluates the whole review's reply; 1,638 fixtures; 500 generated returns seed 20261026; 40 partial records; 2,178 comparisons): 0 of 2,178 agree; differences on returns the full interview completes: 120 project-refuses, 244 project-unknown; no completed-return value difference. Project stands; the citation gap is BUG-0439.
Reviewed in: pass 573a35290f69

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
| C | ec3d44ebace17d5b01c6e4e6c3fbc9045203535db2e6545ad6d3250167378a8b |
| H (count) | c775556cf6baebf885155f3e0e760fff74624401c1c24b030e770258031b62a5 |
| 1 | 2e68d97efd58ec2f0398cec4d680d134b85e779f056cae9ea05e011a9f7506f1 |
| 2 | 0ab699890c51786638b6f0c1b93f2c9a51e56b9ec03cfab26033df0c734de77c |
| 3 | 69f377530fe78842ed6435d2451a374c955c9ac4c0f217290631c73ceb170a92 |
| 4 | f5190222dc5ddab58aa5d89b74a4dc3d317370884faacfd2008a57428b329152 |
| 5 | 132a990696b1fde2839233bf7895b845638c4b1b785f3564f6df43b06023a2c0 |
| 6 | 9123a3a8d16b505e08083ab79f30ae367988df3551a156d0323c377915dc59f3 |
| 7 | 2d136637435f62b970b5c353e75c779fd715ede38a628d7f540cf43908766b3d |
| 8 | ddca4f9241dc13a80dac3054c79ba47e742d66a2d4527a43e24a0175bcd2ad86 |
| 9 | fa2de10ec03aa64ccf1542f423302a72ecd9b6c9cd67bb1ca30525561821dea3 |
| 10 | 58fda5324f2827306aedd0ae09b732627ff98aa73f9a7a54cab70f75d94a145e |
| 11 | 8eb82d5beb69c0454a6c759554cac2f83ac3ac26c85bb799d78878dddb7180dd |
| 12 | f93d792cc48f087f11a780f631740b170a99108e3903ab2a66a22cf6a57e9100 |
| 13 | e6186fd24690d86a5662edc53a2960ff2b88573c971dc46b90c11ca9fa80ebb7 |
| 14 | 3536134c20a3b32dca75e377fb677f868f982518f57d8a268f0a92801417d4cd |
| 15 | c8a6c6974deaaa30601d06a52ca8e95d8be9498c9c8cec9e86578122a31204dc |
| 16 | fcae79e9430e49ca07e2ca670c5fa11acdd4f2ca6b7b9bb2fedc8be3fa2fa601 |
| 17 | 2c6c63d22fd2ea3acdab25328125be88d1dffce895245f87fbcd2f975f169735 |
| 18 | 54565592a271f37c5e115a816c787c5dadc2b582917534dfd27eae600c5d37c4 |
| 19 | 05b98a40f529d1582546ba909de6efb73514a3ff483e36e56facd9ab865be2f9 |
| (check) | 1a6b59c6fdf31c7e7e5420d0e6c5fd77e83f07151a7c3183325eff1eabf29586 |
| 20 | 99961d519248e1225d52071150e8f142d409c38acfd6e8da047b4d6ded8b6a8a |
| 21 | 2b5f736cceb9bf4e2d4c90b34fdbb495ba49de40af926d50a152e6a37fea94ff |
| 22 | aca1944cd1a38f488eb5bca2e3fc850ea0813e5cc52d948d8c664b14cb08d798 |
| 23 | 5f6e9136f6366d6a8b34269668769646ed0f64834225510e482c8bdf72923580 |
| 24 | 21c0d2dfdd9596d93a352afde0aed197eaace4975ae4b553cc352faebfc98614 |
| 25 | de58098410f407e1c01c87e3cb686ffee38e692005dbdab7ce229ce8e27d6cb2 |
| 26 | 9ff90ad759ccc41be7374dd66694efdabada8127a8b6a72fd2db294693eebb67 |
| 27 | 3408d939107960440ca6f29c6127ff6b3b38dcb7addc6b2f81154360af68bc35 |
| 28 | 4097087a54b20b00c3903e405f2687cf0088b67429dd5a481752dc8cae59f33f |
| 29 | 1989d14580b73c66be8bcd89989c2fb63687766403d913d8b87dc6c1cc9689d4 |
| 30 | 09f1cf6c47cc4b6c10b8bd6306b25342787e09159a30b9ea719655b429cc8d48 |
| 31 | 4698820240520cad69161260266f113cfd5b3fd7152dc7ea1bff5e3f15a0df1c |
| 32 | ebbcaf666cfcea9cf9853233fe4f7e1b523ff86345bf133e3fa5bcf60d74792b |
| 33 | a0c21f6f0a8e7e815639bafc8edc228d1c12f5a0edb74e134b42188ab7914b5d |
| (table) (ny_it201.std_deduction) | 3e8b1b4b2e252ed6b695dc85b7a73edab55b2b040929199658937ce7a7fe82b2 |
| (table) (ny_it201.std_deduction_dependent) | c07f2439085f2c2d07e3a2b0be460af7dae29460bdd55deb9bf61f0415e4681f |
| 34 | 1904ace98a7c474a74ba6be43f742667bb42a915c6dc5d5e48b63eaaeb51b6cc |
| 35 | 9d610a8ea56ab1ad19975ad8f2472ecf605a5c0cdbaeb39e77bab3d079bdd86c |
| 36 | e8f5476b99522afe40f29c0a8e17fa58160974e4f7023814e5462af4d12b4a0c |
| 37 | 811219783cf3019c714cddd44a54c90c9f0728552d6bb4184d0f5eb659d95cfa |
| 38 | f4f472d238f61ffae2cea11f76ee5f73a5baf0c921004f916cd788fd5e9f96f4 |
| (39) (ny_it201.tax_table) | 1cdfdcbbe593b710f004ebfb414342885879cd1675d4186d5f23afc6f454a96b |
| (39) (ny_it201.tax_schedule) | b9132acdc127eb85d355530028ce8fb00f3b2403b47b8e3a0512e9edb807072a |
| (39) (ny_it201.tax_low) | bc5cd19bcab2bbb104bd259ec607457f3123ac3e24d4d396962def1b93fd06bc |
| (39) (ny_it201.tcw.w1) | 516026111e884ba28a82734945798f2bd6786666599d68de0a4b64dd389d29a0 |
| (39) (ny_it201.tcw.w7) | d15882cf1000257f1894e5df08e363d049c664daba6a591bcc7555c6bbf436f7 |
| (39) (ny_it201.tcw.w12) | 89f237ee0156482b114b8860acb5daf2aee3a6dbe34706ba99f31b4a2239b1dc |
| (39) (ny_it201.tcw.w2) | 54e5746409ba7261fa478a2080896faa2b551a371fa19531a0cfb4a20b2d676f |
| (39) (ny_it201.tcw.w3) | b48b64600656b96290757975e69ff5c26fb87908f0530c747eac878dc1db7861 |
| (39) (ny_it201.tcw.w4) | 7de9fdafd3621e29658a74b296e4245423c87e8b150f01a7664e87642f8a1ddd |
| (39) (ny_it201.tcw.w5) | 985efdcd3364618b96575b629487165d1d16f51ad9cd95d244716b0e5475b357 |
| (39) (ny_it201.tcw.w8) | 2e32fb0efa8c925b71cbdf61c92f2027386511e2d7176a3501200f351caf8976 |
| (39) (ny_it201.tcw.w9) | 6db7cefffe004fe5eaa6973dde1e45abf9420c0b2b06685bdfe6f9c2e2c73e73 |
| (39) (ny_it201.tcw.w10) | a5c63b7fbbc41a76ea1b438e34550fe0931c083f684439345ab6cb1b7bc5f7f8 |
| (39) (ny_it201.tcw.w13) | bd9c828ed79c6723b8b6f0e87844856d62d2c53c7bbb5ac3350009bb96fd838b |
| (39) (ny_it201.tcw.w14) | c916638d4f912aa9992e695c64757c3086bad398dcbccb02bea985ae5b5e8018 |
| (39) (ny_it201.tcw.w15) | cf60889b4c9e0bf72b4f8a91622acd2cdb0a0e82142ae2d909a2be1214cbec5c |
| (39) (ny_it201.tcw.top) | e2ca8b48e232dbe55906203df0ed24964edec6da3cee4cea57e300ecade5988f |
| (39) (ny_it201.tcw.mfj) | 3a3039bc16e1499c64176a93eb7dd5d3924ecbb3319f8556c8bfd74dd0ceb032 |
| (39) (ny_it201.tcw.single) | ee10cced449ae8b8ed68c121c66c00460a55d5cd26e71b8430e9cd44512cfd8a |
| (39) (ny_it201.tcw.hoh) | 3569ef749bb5bc3f312be76cc6f344a627b6a7fe2cdae1d2b26d5da1064120ea |
| (39) (ny_it201.tcw.by_status) | 8bef046691b1c67611c2bc271635bf9f65bbb73b255a8f873dd5c1f72cbce676 |
| (39) (ny_it201.tax_high) | 90710efab4694fcb1cf43e92e4cd4a04e7034361902e20e29b46be0d59cc64d8 |
| 39 | 3258e702fbcc475c837657311a68be4ea23cff6f91fc024e56e29513356e0b46 |
| (Note 1) | 6f60d08080f11567300c21e85d8e7772c8f3a34041aeecc87f114d4a3876f326 |
| (column) | 755b0e82ef970bff5cd06199221c70e429a40da96c21bc31a5d6fa3155439618 |
| (table 2, column 1) | 1b54a1cafa51f35fb05033eeb67c54babdcb14b6dda6f913ae2877cd0846a5cf |
| (table 5, column 1) | b07ead687cc845ca8cded41b804bd7877566b60651f49bcfefc686b80b3f3d25 |
| (table 2, column 2) | aa2ea0ce78568a3813b63686307e4d0a49deeab1fa343d8f1e1d6679fe1d0c46 |
| (table 5, column 2) | bef4081d863148d42af34893dde5661d4a4a7f9b1eea4eec57bc947714591ddf |
| (table 2, column 3) | a0b2f5d8afe5ee0c05e9d1adccfb89affe74f75b16440d6c24104e4f8a495540 |
| (table 5, column 3) | defb677fa2d852e5bfd9847c3d75f182c0bc41468d3f2e0afe11c61d9142f979 |
| (table 2, column 4) | c7161ceb2ceb7fddc34c18074997566e9e6a28dd3ab4a95e0485cc46aacfddaa |
| (table 5, column 4) | a9d60a5c52cb429a1ddb242b78214ba73eb3a9b0831e1ddf348ae3cb777f06bc |
| (table 2, column 5) | 8cb2ae448b0598a89e67e0ef143daebc29bf26ae06017fd28ff8ef4d783ae03a |
| (table 5, column 5) | 452fb3edb237e35f9529e00a573ab01784c352e187ce13a2059f6acd987c17f1 |
| (table 2, column 6) | c838019e9a76ce0a5c6512a6c227ed231380ac2899b8001147aefb1a07f47ac9 |
| (table 5, column 6) | e08b60f14336ce83b663b38f9bfe1055fcc4dea0cd2b679bfdd3e0aa577ee3a1 |
| (table 2, column 7) | 451ca8e43224887d28aece6df0a8e44c4a41097b8c2b5fd3286580276af832d3 |
| (table 5, column 7) | dd44690a5dafae130cba2e115a3d035f1b74b2785afb8c98b622db46029df7e1 |
| (table 2) | 5e102e162a500af5408946db853eec88b44336d13225fca36938e9e59a86f516 |
| (table 5) | 4560b7a258a59e8b3d201eed5b81e66293c43d0af05c473ba904da5e1537e044 |
| (table 1) | 63aca473979d96c8373ff3e5fb76a5353b972509a14e40c451f29205c1217067 |
| (table 4) | 0a25bd3acea2988cbb48f061c55d48273a56e48645c056a6716751fe5363c972 |
| (40) | 541ff2a2baacad5723118b887833f960ffee4c4e103ccb553b354967396894ba |
| (48) | 7d1b29555db02bc4bf10f99711c361c4e905e309334f3f1878f568f643c66f4f |
| 40 | e5d486e616ed39fe1552a5920f6af0aa1f29114c453ecce49e749e9e48ad7bf2 |
| 41 | dde2b80ea36c16b950dc1fbf212df0476a99ba82627637a622de2779b2fa7ce6 |
| 42 | 0ec8ee41986e2fd917b337e852c5779e4c03a51cc163c205a4725cbbbe021d35 |
| 43 | 0768df9e4e3c2093dd64254dab9da933e92437160ff7432ed6b497a9974db3d5 |
| 44 | d9c1f6421eb531382bf98ff1abee59ee6fcf03af4021fc84c869179ace2c1fde |
| 45 | eaa1f4b99acf5bca3dd6ee22d1cf4d933b81a8a593cd5d3c769718bb5a5e08e3 |
| 46 | 4e963942d24b2cc5816108bf07d9ea2f01f0096501b7a8b38a7f6cbda1c94eef |
| 47 | 9c9560e4bd04eb5acde237110af8f7f50ba69cb9863105422764a46a810ae929 |
| (47a) (ny_it201.city_tax_table) | bd05e12d49c8ebd491719f703f5c075b25d9ed1a27b4b062ae41b81302aca07e |
| (47a) (ny_it201.city_tax_schedule) | 955dfacc3974a6201ce7e63d003299ebb2ceba0e9c6b50c7bb76e127e010dbd4 |
| 47a | 651b0f0a32747a4c5557ef8e89c953192d4eb9c5424cc65afae17dc99711f1d1 |
| 48 | 4865deec6666bdd5f8e78028fcf7d0dfc553564d06102d3bddfb64cd52604965 |
| 49 | 1db6691ce9f81b4388b131a798061fc3bfbdbebf37bf65cbd97a99463dbe00b2 |
| 50 | 44018f281480785a1039b29dcf5c844b446f6a1766f8ab5be60df1ae9672b7e2 |
| 51 | c2d87b2d469173c3b43e86edc2fe70c02a6cbe705e92223b55b21d92e3cced66 |
| 52 | c82b7d8d8e9aa1d59a34e2e84824bed2ccb3dbfa7bd53fb5c3a3b7c24ef2f339 |
| 53 | c2d0dccc536ae22102e706b0aa8c87b1851dee4c48337d39c342599e0d7455f2 |
| 54 | 1f5ae71234b822f1433ce55adc77874d354366d3d7b7b517fbc1c509d226562f |
| 54a | 534de1ccd3484bd9464cdc8950ce30dae5ed5bb8c53e91d34eb686dbd473b275 |
| 54b | 9c9350e37ad12fdce5a9ec2ee615e69a3798275398bfee3384b30a5eb68abced |
| 54c | 783501a8ad15a7530e67431a2524856557bb9964d6b14d150a1a09017c24b61f |
| 54d | 6802883037aba3880ae4f2fbe220d6e9aa6aedc2b66e6b10ff74f7e77ce9c932 |
| 54e | 92d48f290f85d3d7dd60fe620655c3a3a265eee311bebb06013d174a23f05fbd |
| 55 | 31754bcd5c26187078347f6a2f88d928bfd640d841e5ac9d55bb6dacf9742c2f |
| 56 | 4c51383bc800e4b19d7c6d5955fb60514bb9ad6c0c4d8b6cc4bb31a640917816 |
| 57 | ded965d62f5a0157bae2a04211b9292373e6111b5998da4ead1900d7b9a7df5d |
| 58 | 8248a1165273dd22bc12f16e0f7bcf121da3db24bd4349b657060dc1550e87fc |
| (chart) (ny_it201.sut.b1) | 6a78628364c0503d8c43c79a8ac083af7091d9310cd0eb887924c557ff35f358 |
| (chart) (ny_it201.sut.b2) | a4b23068fee21e73a408f47ad53865384b0eb40335f201fa7146109eded1308d |
| (chart) (ny_it201.sut.b3) | 8d16a35855b5ba01b7e93cdde3605e2f5ef7d8d0920aee2b9c84053c8bb809f5 |
| (chart) (ny_it201.sut.b4) | 4c1e3214b55396e53f105ee3fa64246d72bcf976d69a14a0d317d92d4d5871ce |
| (chart) (ny_it201.sut.b5) | 238b937d62c8dd8666cbbc859480c2ed64c6cf00c41d2e6b510436f60c8b0e29 |
| (chart) (ny_it201.sut.b6) | 7a4fc611ceb1d78adb146f46b524b5cfcfe0ce88f03020a3c78d5adba452bb53 |
| (chart) (ny_it201.sut.b7) | d7793aa874d2cf7a903377b207bad5b714a833ee5bc2738378db3e3feb09d018 |
| (chart) (ny_it201.sut.top_product) | b19eb64bde332548ff1c6a06ca20eccc551a4066193c8b369fdc3d0f169bde57 |
| (chart) (ny_it201.sut.cap) | bc3867caeff5c2ce46a56af458bf69baf597cced77741c5a77da1d6cd50bfe65 |
| (chart) (ny_it201.sut.top) | 3f337836dcc9231409008d5ffa2d8fd4efd0f392d18987ef2eb91f6b587d3fc7 |
| (chart) (ny_it201.sut.chart) | f490093538fc554603fa13fbad139b3e32a8a2596400e226d1e3bc28d80f8fbc |
| 59 | 19025f897e86e3c72f15ed92f4ed608c2be9fe4fffc0afa4dbd9a33c62ee44cc |
| 60 | 178b3aea541212cd6e1b0cd15cbe019527381140b66487bac2fd04adfdd4a50b |
| 61 | 0b1b43168dba06f33619b3fe34032977426efaeca1c9b52368dfb6046db94791 |
| 62 | 6f15d5a82c661c9f283180e613bb2b496ada9cadd3c892cb5f65dcbf5a2ca901 |
| 63 | e639b93848b4db093b37f67361d8e81fad11f6b9a75a47905985bf8a85d8065c |
| 64 | a5f0618ac2bdd918bd9ec453f260c77349d8577320a0378415df1452a6705d7b |
| 65 | 608d5c54b046b0074bcc8348156bd1f8277fe57f0f2e287e2bc232815463d3d4 |
| 66 | 9184d921bf71f25c0b753169559508fa01f5f34f8035a24e2c258c01cfba3389 |
| 67 | ad1ffde0f4c0943b7555852ac0ebdfdd7c0a43ba7c71f2ea134e48a162294d53 |
| 68 | 28e5232bbc53db4ea6026f334d435f719337517b3831474ce5092f2e7a83e86c |
| (69) (ny_it201.stc_income) | 62ba7be73352ad33cd177abe32908842d63b53a47c561e73c6aeaea1061c5cae |
| (69) (ny_it201.stc_fixed_amount) | 465c3ee72cd12b7930ba6e0405cdcd11e4c2584be267c8cdbef3d9a89fa5daef |
| 69 | 588066351f475d0705e98077689e393c707abf08fdfa523811de1e844d378172 |
| (69a) (ny_it201.stc_rr_low) | d9b59a3b434a627b090e64b836527b08bcf6be95530ea879f4497c5d6c204285 |
| (69a) (ny_it201.stc_rr_excess) | 0c13f94345415ffbfee0e8c75359d94af1077370fe4cace8c655918f9f928815 |
| (69a) (ny_it201.stc_rr_excess_product) | 5902990a16f4487def5ecbe7bfd791270fe9a577d1e84e12238edb319275b91d |
| (69a) (ny_it201.stc_rr_base) | 37e15bd0fc1758a39110cdfec9db6c3515b48f52d4fd2ccfac96c90a6e6f3be8 |
| (69a) (ny_it201.stc_rr_high) | 43865a0c6d1329972c2ce2308462ba22c42af6ecfc31287abecbeffdaef05860 |
| (69a) (ny_it201.stc_rr) | 0b69254835ad6e07459b0e9b272c59af782c879daf6936cb07968468c941f621 |
| 69a | 80f26a95b0f8609132ea0ebca0aff81e2274a929504a3732e9a829bd4b30cfe0 |
| 70 | e3aaff16e76e6a984478fa45884823613b76ac2184a4331fe4f601c9d385b814 |
| 70a | 86ebfabea438b8b09e9a1082ab0de9768429259c76f2f63dedc36c21fb09d41d |
| 71 | ad8327098fd580d523c4e65af05619ffcffed9970e993d7abc90bc4efbe6c2b6 |
| 72 | 71786054aa33ea7b4166512cc56fe73b38bec93cdc0e5b17f6b0803970afd8ac |
| 73 | 9af397dcbfb68952a82ca6d31bcfcfe48b2bda1a37d578d8f6b59f660d8976f8 |
| 74 | 408aacfa9a75dc6246b58dbf0fe1a10e8852e1d560574e40c13e633b35d5ba08 |
| 76 | df416db18be40a8cba4f4fedb0314b8b74e00ae459737b2baf82def58e63336c |
| (80) | bdbf0aa5bd8d503b9603c6662a6f544f1cf50b9cc2292d04c953b129682f884a |
| (81) (ny_it201.prepayments) | e61a939f45dae8971d470f29b7be1a175cb128937784f470aa6a118f5609194a |
| (81) (ny_it201.safe_harbor_100) | a25a7da23d7538b98920566d546215ff1831b3bd6a6f8aca6e35bf48deb4e345 |
| (81) (ny_it201.safe_harbor_110) | d6ded2bcec460c0b15173c6b44480c051bf8456fde88f14f465a87bcaf0b0a0e |
| (81) (ny_it201.safe_harbor) | ca4509b83345181872175ebfee780dd9deb2961fdebdf14cd66e9f9e9562be82 |
| 81 | c90b9a73fe012dd1f0ac3cb5d1d29c0bafb7a33f6c6c1d04fa995e7a19b58d39 |
| 82 | 92127e1f501aba9e24c5a5d194b0fc49526947578561e9c63c364b1847e69e47 |
| (77) | 4375e1f0e0866c428c3d6d860b0d2ffb70bb1e712f017ae7680d9e995df42049 |
| 77 | 29fd7542de31bcd9346db1baf2ae8a85089faa1b107e02260b5e7fbe5a35dcea |
| 78 | 4039d7e36e0e536e72d121bd698abf2f5b07cfc55f2ee4c4f8512f6b6aed9882 |
| 78a | ac82020b889e0fa3a5dec9ec25ff3e2c17ff9dcf2c2335b28e3238c6e2ba61cf |
| 78b | 952a2407b88a305131f59dbc5b01d3c958037b4dc8c3814213eaaef2b2a23517 |
| 80 | 69f908b3b7023775621c35f6979f28695581a441a69f7ab6f7ffae21196cc082 |
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

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 573a35290f69

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines 1 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 573a35290f692a55051348194551d4d7983fa7dff89ab452864e3e0441ed2e2a |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | fail |
| required input context sha256 | 10140de2871ab559d86226041fcd6c3ce5658619653c9639fafa76a952c7867b |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | 83e9ed0ae4edc40db4c301ed52bf00d46afb0b4bd30dea929e35960993911093 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 13f1b2a29a4ff9ba988b5349985901969d73a6c4147d8843605eb8430b831a65 |
| receipt | .transcription/ny_it201.lines-6b86b273ff34 |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 3, 4, 5, 13, 14, 30, 31 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 3, 4, 5, 30, 31 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |
| ny_it201 | Form IT-201 (2025), Resident Income Tax Return; final 2025 edition (page footers 'IT-201 (2025)', scan lines 201001250094 to 201004250094); PDF modified 2025-11-12 | 1, 2, 3, 4 | whole document | c924371c32a986a1903c9216bd60c6df8fb52f8e506e5c462851226b71e2154d | - | 895c4b15bba606353fd49f5779f969877e55196eda7f7b9f633f02cbd3dbbb3d |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | ny_city_rs, ny_rs, ny_tcw, ny_tcw_first |
| named lines: f1040.line11a, f1040.line15, f1040.line2b, f1040.line3b, f1040.line4b, f1040.line5b, f1040.line6b, f1040.line7a | f1040 |
| named lines: s1.line1, s1.line26, s1.line2a, s1.line3, s1.line7 | s1 |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: ny_it201.line1
    printed: "1"
    label: "Wages, salaries, tips, etc."
    type: NonNegDollars
    expr: {op: param, ref: ny.zero}
    note: >-
      LIMITATION, NOT A COMPUTATION: this line is not correctly encoded. The zero is a stand-in
      only, and a return built on it is wrong whenever the filer has wages. This line must be
      replaced before any return is produced.
      The archived Form IT-201 page 2 prints this line as "Wages, salaries, tips, etc." and says
      nothing more. The supplied IT-201-I pages (3-5, 13-14, 30-31) do not include the line 1
      instruction, so the supplied text does not say where the amount comes from.
      The federal line carrying the same wording (federal Form 1040, line 1z) is not in the
      supplied catalog. No W-2 collection field is in the catalog either. The input interface is
      closed, so no new input may be added.
      Nothing in the supplied interface can carry the filer's wages. The ny.zero parameter is the
      only well-formed expression available; it encodes no amount from the IRS or New York text.
      Fix: replace it with {op: copy, from: <federal Form 1040 line 1z id>} once that line, and
      the New York line 1 instruction naming it, are added to the catalog.
```
```

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
