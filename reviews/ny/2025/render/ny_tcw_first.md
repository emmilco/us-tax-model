# Render comparison — ny_tcw_first

The rendered English of every printed line of `Tax computation worksheets 1, 7 and 12 (New York AGI of more than $107,650)` (`rendered/ny/2025/ny_tcw_first.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-04 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | c96979a2ec4dc3eb61edc0415d8432e62cf7553cbf4a6ccac347bdd7223e8aa5 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 390d22ff0e196470cf6119d363b160934f85d1c37fcc6196dd053b2d9797cb11 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 0f16a5578d817f9cb8635c4425a4d39c2fab4c20e3478d80fcb20014cedbb4f4 |
| lines judged | 14 |
| match / mismatch / unclear / missing | 11 / 0 / 3 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: New York State tax rate schedule; Tax computation worksheet 1; Tax computation worksheet 2; Tax computation worksheet 7; Tax computation—New York adjusted gross income of more than $107,650 | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 4 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 4 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |

## Lines

### 1 — Enter your New York adjusted gross income from line 33
Status: **MATCH**

Model: The worksheet line 1 says "Enter your New York adjusted gross income from line 33", and the restatement binds it to Form IT-201 line 33.

### 2 — Enter your taxable income from line 38
Status: **MATCH**

Model: The worksheet line 2 says "Enter your taxable income from line 38", and the restatement binds it to Form IT-201 line 38.

### (3) — The worksheet's flat rate (5.5% on worksheet 1; 6% on worksheets 7 and 12)
Status: **UNCLEAR**

Restated: Input — Bound by the calling line (ny.tcw.first.rate or ny.tcw.first.rate6).

Model: The text sets the rate at 5.5% (0.055) for worksheet 1 and 6% (0.06) for worksheets 7 and 12. The values behind ny.tcw.first.rate and ny.tcw.first.rate6, and which worksheet gets which, are not given, so the binding cannot be checked.

Ruling: interface gap; the rate is bound by the calling lines, which the reviewer of this definition does not see. Checked: ny_it201.tcw.w1 (married filing jointly and qualifying surviving spouse) binds ny.tcw.first.rate = 55/1000, and ny_it201.tcw.w7 (single and married filing separately) and ny_it201.tcw.w12 (head of household) bind ny.tcw.first.rate6 = 6/100, as IT-201-I-html prints: Tax computation worksheet 1, "3. Multiply line 2 by 5.5% (0.055)"; worksheets 7 and 12, "3. Multiply line 2 by 6% (0.06)".

### 3 — Multiply line 2 by the flat rate
Status: **UNCLEAR**

Restated: Multiply line 2 by column (3), rounded to the nearest multiple of $1 (half up).

Model: The text says only "Multiply line 2 by 5.5% (0.055)" (6% on worksheets 7 and 12) and says nothing about rounding. The pages given contain no whole-dollar rule, so the restatement's rounding to the nearest $1 cannot be confirmed.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. Worksheet 1 line 3 is "Multiply line 2 by 5.5% (0.055)"; the product is rounded once to the dollar.

### (3, Stop) — Is the line 1 amount $157,650 or more?
Status: **MATCH**

Model: The text says "Stop: If the line 1 amount is $157,650 or more, skip lines 4 through 8 and enter the line 3 amount on line 9", which matches line 1 ≥ $157,650.

### 4 — Enter your New York State tax on the line 2 amount from the New York State tax rate schedu
Status: **MATCH**

Model: The text says "Enter your New York State tax on the line 2 amount from the New York State tax rate schedule". The glossary's schedule bands, bases and rates match the printed schedules, and the filing statuses are mapped correctly (①/③ single, ②/⑤ joint, ④ head of household).

### 5 — Subtract line 4 from line 3
Status: **MATCH**

Model: The text says "Subtract line 4 from line 3". The added zero floor cannot change the result within the worksheets' taxable-income limits, because no schedule rate up to those limits exceeds the flat rate on line 3.

### 6 — Enter the excess of line 1 over $107,650
Status: **MATCH**

Model: The text says "Enter the excess of line 1 over $107,650". These worksheets apply only when line 33 is more than $107,650, so the zero floor has no effect.

### (scale) (hundred) — 100
Status: **MATCH**

Model: This is an internal scaling constant with no printed counterpart. The 100 is undone by the 0.01 factor on line 8, so it does not change the amount.

### (scale) (line8_scaled) — The amount times 100, so that the product with a ratio of four decimal places is exact
Status: **MATCH**

Model: This is an intermediate step: line 5 times 100, which line 8 later reverses. It reproduces line 5 for the "Multiply line 5 by line 7" step.

### 7, 8 — The ratio rounded to the fourth decimal place, times the amount (times 100: exact)
Status: **MATCH**

Model: The text says "Divide line 6 by $50,000 and round the result to the fourth decimal place" and then "Multiply line 5 by line 7". The cap at 1 never applies, because the Stop rule skips lines 4 through 8 whenever line 1 is $157,650 or more.

### 8 — Multiply line 5 by line 7 (whole dollars)
Status: **UNCLEAR**

Restated: Multiply line 7, 8 by 1% (0.01) (ny.hundredth), rounded to the nearest multiple of $1 (half up).

Model: The text says "Multiply line 5 by line 7" and says nothing about rounding. The pages given contain no whole-dollar rule, so the restatement's rounding to the nearest $1 cannot be confirmed.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4), which the rendering names ("Interpretation"): IT-201-I p. 7, "Enter only whole dollar amounts on your New York return.", and p. 2, "When you enter amounts on your return, enter whole dollar amounts only" ... "Increase amounts that are 50 cents or more to the next dollar." The register rounds a product of a rate and an amount once, half-up, to the dollar. Line 8, "Multiply line 5 by line 7", is the exact product of line 5 and the four-place ratio (amb.ny.2025.fourth_decimal; the "7, 8" helper carries it times 100 so it is exact), rounded once to the dollar.

### 9 (line9_phased) — Add lines 4 and 8
Status: **MATCH**

Model: The text says "Add lines 4 and 8. Enter here and on line 39."

### 9 (tax) — Add lines 4 and 8, or, at the Stop, the line 3 amount. Enter here and on line 39.
Status: **MATCH**

Model: When line 1 is $157,650 or more, the text says to "skip lines 4 through 8 and enter the line 3 amount on line 9". Otherwise line 9 is lines 4 plus 8, which matches the restatement.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 1 | 201f34ea7a148d637a94f4c13e77e67afa3a8bbef8e232768217de7b5be73b6f |
| 2 | 0f120a35db5ee3e1b6ca1c6d39578791cf8199fa32e7172362e44469f65ec487 |
| (3) | ba5b46b8366838c2b6bd9200632a9b30d480068458d6f8d2930fdb85b3901e7f |
| 3 | b3acdc3dfa178a26188de769fd23deec1515e7927266a9b4141d34f031dbb01f |
| (3, Stop) | 0d081a7ff1e20b4f1040d831a113006bfaf712301bfa95fa7da2acc9f4348413 |
| 4 | 06882c8486a72b697eee3e963e57cef8a76f8e87202bba077200c88c18e4af12 |
| 5 | 230d251dae0e755b46dbb9c94699dce65f5a7b49a5fd41c06a73f68bd9423ace |
| 6 | 45c848d02bca90b301b6700e0e56090ce390c9ab7607973a695cbc6f4d145ff9 |
| (scale) (hundred) | 996c4e74fb940b2ea9005dd011872f860efa151521931733ca00e97189b8df56 |
| (scale) (line8_scaled) | 7ba4975c5c3d3efa4a35d629e3e41efa8b493c001b6b6932da5ab113672595d5 |
| 7, 8 | bc094c6c4454638cdf55a36f93bdb4d05c3a0af6c7e23dcf52bb8dba50b2e59e |
| 8 | 05e3c3d70ea5d6627b11dee254ef516132b9cee0d6346d01c3dcc3d7584a216e |
| 9 (line9_phased) | 28ce2a4825d1584bc1cd1f36bdbc4223a0cb6e5250e4cbead790bf885a529f11 |
| 9 (tax) | 7b811a30d09b14013ebde7d37f9a4339ffdeca8569850c248dc259c917049a43 |
| (rest of the document) | 8155a4f9e17ae2938bfb77ee4bcefc3abf9982f5dd9a3e6140cd5ab5ec3cfd42 |

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "The worksheet line 1 says \"Enter your New York adjusted gross income from line 33\", and the restatement binds it to Form IT-201 line 33."
  - key: "2"
    status: MATCH
    reason: "The worksheet line 2 says \"Enter your taxable income from line 38\", and the restatement binds it to Form IT-201 line 38."
  - key: "(3)"
    status: UNCLEAR
    reason: "The text sets the rate at 5.5% (0.055) for worksheet 1 and 6% (0.06) for worksheets 7 and 12. The values behind ny.tcw.first.rate and ny.tcw.first.rate6, and which worksheet gets which, are not given, so the binding cannot be checked."
  - key: "3"
    status: UNCLEAR
    reason: "The text says only \"Multiply line 2 by 5.5% (0.055)\" (6% on worksheets 7 and 12) and says nothing about rounding. The pages given contain no whole-dollar rule, so the restatement's rounding to the nearest $1 cannot be confirmed."
  - key: "(3, Stop)"
    status: MATCH
    reason: "The text says \"Stop: If the line 1 amount is $157,650 or more, skip lines 4 through 8 and enter the line 3 amount on line 9\", which matches line 1 ≥ $157,650."
  - key: "4"
    status: MATCH
    reason: "The text says \"Enter your New York State tax on the line 2 amount from the New York State tax rate schedule\". The glossary's schedule bands, bases and rates match the printed schedules, and the filing statuses are mapped correctly (①/③ single, ②/⑤ joint, ④ head of household)."
  - key: "5"
    status: MATCH
    reason: "The text says \"Subtract line 4 from line 3\". The added zero floor cannot change the result within the worksheets' taxable-income limits, because no schedule rate up to those limits exceeds the flat rate on line 3."
  - key: "6"
    status: MATCH
    reason: "The text says \"Enter the excess of line 1 over $107,650\". These worksheets apply only when line 33 is more than $107,650, so the zero floor has no effect."
  - key: "(scale) (hundred)"
    status: MATCH
    reason: "This is an internal scaling constant with no printed counterpart. The 100 is undone by the 0.01 factor on line 8, so it does not change the amount."
  - key: "(scale) (line8_scaled)"
    status: MATCH
    reason: "This is an intermediate step: line 5 times 100, which line 8 later reverses. It reproduces line 5 for the \"Multiply line 5 by line 7\" step."
  - key: "7, 8"
    status: MATCH
    reason: "The text says \"Divide line 6 by $50,000 and round the result to the fourth decimal place\" and then \"Multiply line 5 by line 7\". The cap at 1 never applies, because the Stop rule skips lines 4 through 8 whenever line 1 is $157,650 or more."
  - key: "8"
    status: UNCLEAR
    reason: "The text says \"Multiply line 5 by line 7\" and says nothing about rounding. The pages given contain no whole-dollar rule, so the restatement's rounding to the nearest $1 cannot be confirmed."
  - key: "9 (line9_phased)"
    status: MATCH
    reason: "The text says \"Add lines 4 and 8. Enter here and on line 39.\""
  - key: "9 (tax)"
    status: MATCH
    reason: "When line 1 is $157,650 or more, the text says to \"skip lines 4 through 8 and enter the line 3 amount on line 9\". Otherwise line 9 is lines 4 plus 8, which matches the restatement."
```
```
