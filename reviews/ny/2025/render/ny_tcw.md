# Render comparison — ny_tcw

The rendered English of every printed line of `Tax computation worksheets 2–5, 8–10, 13–15 (New York AGI of more than $107,650)` (`rendered/ny/2025/ny_tcw.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-04 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 012fe91b68d139feb0a35fcb38822bd5839882957c11bf701a5328f6f604d7d4 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 390d22ff0e196470cf6119d363b160934f85d1c37fcc6196dd053b2d9797cb11 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | d8db8e26f2e106fa04919145231436566a86b41dc7ca716818fda0c167664f32 |
| lines judged | 14 |
| match / mismatch / unclear / missing | 14 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: New York State tax rate schedule; Tax computation worksheet 2; Tax computation—New York adjusted gross income of more than $107,650 | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 4 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 4 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |

## Lines

### 1 — Enter your New York adjusted gross income from line 33
Status: **MATCH**

Model: Each worksheet's line 1 says "Enter your New York adjusted gross income from line 33", which is Form IT-201 line 33.

### 2 — Enter your taxable income from line 38
Status: **MATCH**

Model: Each worksheet's line 2 says "Enter your taxable income from line 38", which is Form IT-201 line 38.

### (6) — The amount the excess of line 1 is measured over
Status: **MATCH**

Model: Line 6 of each worksheet subtracts a threshold printed for that worksheet. Examples are $161,550 (ws 2), $323,200 (ws 3), $2,155,350 (ws 4), $5,000,000 (ws 5, 10, 15), $215,400 (ws 8), $1,077,550 (ws 9), $269,300 (ws 13) and $1,616,450 (ws 14). Binding that printed amount as an input matches the text.

### 3 — Enter your New York State tax on the line 2 amount from the New York State tax rate schedu
Status: **MATCH**

Model: Line 3 is "Enter your New York State tax on the line 2 amount from the New York State tax rate schedule." The glossary's bands, rates, base amounts and thresholds match all three schedules. The mapping also matches: single and MFS use the single schedule, MFJ and QSS use the MFJ schedule, HOH uses the HOH schedule. Rounding each band's product to the dollar is not stated in the schedule but changes the result by cents at most.

### 4 — Recapture Base amount
Status: **MATCH**

Model: Line 4 is the printed "Recapture Base amount" for each worksheet, for example 333, 1,140, 3,887, 64,237, 568, 2,399, 32,571, 787, 3,076 and 48,337. Binding the printed amount as an input matches.

### 5 — Incremental Benefit amount
Status: **MATCH**

Model: Line 5 is the printed "Incremental Benefit amount" for each worksheet, for example 807, 2,747, 60,350, 32,500, 1,831, 30,172, 2,289 and 45,261. Binding the printed amount as an input matches.

### 6 — Enter the excess of line 1 over the worksheet's amount
Status: **MATCH**

Model: Line 6 is "Enter the excess of line 1 over $[threshold]". Subtracting the threshold from line 1 with a floor of zero matches "excess".

### (7) — $50,000
Status: **MATCH**

Model: Line 7 says "Enter the lesser of line 6 or $50,000", so the $50,000 cap matches.

### 7 — Enter the lesser of line 6 or $50,000
Status: **MATCH**

Model: Line 7 is "Enter the lesser of line 6 or $50,000", and the smaller of line 6 or $50,000 matches.

### (scale) (hundred) — 100
Status: **MATCH**

Model: This scaling constant of 100 is not on the form. It is a computational device, and its effect is undone by the 1% factor on line 9, so it does not change any printed line.

### (scale) (line9_scaled) — The amount times 100, so that the product with a ratio of four decimal places is exact
Status: **MATCH**

Model: This is an intermediate value equal to line 5 times 100. It is not printed and is reversed on line 9, so the net effect is line 5 times line 8, as the form requires.

### 8, 9 — The ratio rounded to the fourth decimal place, times the amount (times 100: exact)
Status: **MATCH**

Model: Line 8 is "Divide line 7 by $50,000 and round the result to the fourth decimal place", and line 9 is "Multiply line 5 by line 8". The program divides with 4-decimal rounding and multiplies the scaled line 5, which matches. The clamp to [0,1] has no effect because line 7 cannot exceed $50,000.

### 9 — Multiply line 5 by line 8 (whole dollars)
Status: **MATCH**

Model: Multiplying by 0.01 reverses the ×100 scaling, giving "Multiply line 5 by line 8". Rounding to the whole dollar is not stated in the text given, but it affects cents only.

### 10 — Add lines 3, 4, and 9. Enter here and on line 39.
Status: **MATCH**

Model: Line 10 is "Add lines 3, 4, and 9. Enter here and on line 39." The restatement adds lines 3, 4 and 9.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 1 | e683e8ed87df115c479e249048fad92e9e5ff67ed5a84d2e6434d4e4febc999c |
| 2 | 213a0464dd2d750928d7f3739b53d19517107548d1bbb165abeaa90b0c6614d4 |
| (6) | 3fb33029041c7056125818938007e433b8feb76eb0bcca369ee668e4e9855fa2 |
| 3 | dc93d39430ff6ff12692275a7c70abd469ad0618a5ab38067537f9f7c932f312 |
| 4 | 15c089047f7cfbfb2e7e230b0d383864743d50c882b707d38d4583528736ccee |
| 5 | d5460a0b4a91b46ab17e06641a991fcc8dcedf1ebc412ed856f3dd38fb3bb320 |
| 6 | df56e8dd37bdb3c483a745ff460908e99c913bde4020d46247c3503b0cd3ae5a |
| (7) | ac38179ee5f36c67a6211a50d84a5f56d0e5ee3fa8efc4f45c0f108f075734c0 |
| 7 | a3b9eed023fad924980cdc7b63616a90e8f63caeb35d4a2b11344faf86d2fc6a |
| (scale) (hundred) | 569f42fadc0ec0d17a08049ea8a24f65016566d3e26f72b7d2f01ce80633c595 |
| (scale) (line9_scaled) | cdef1f16e6ff61b3cca0456104e85edc7bc1017c8e6ad8a84a5874fab507dcf2 |
| 8, 9 | 9a83ce257135067ac0b5e1283e1c75ee6cbd93b05723dfb2560d7b8b79d47c86 |
| 9 | 636c9b34cbad1cbf7677214098825d971a43accd8be6cc30d907a3d90e27e1c7 |
| 10 | a887f4b9ff2e15dee1bba891a9d5328ac984bee0e3bc590f6f0fd34d29e39d84 |
| (rest of the document) | ceb66b5911f951eaa51d177cefbded1f2d31a6109c509121ff6ca66f10e893ea |

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MATCH
    reason: "Each worksheet's line 1 says \"Enter your New York adjusted gross income from line 33\", which is Form IT-201 line 33."
  - key: "2"
    status: MATCH
    reason: "Each worksheet's line 2 says \"Enter your taxable income from line 38\", which is Form IT-201 line 38."
  - key: "(6)"
    status: MATCH
    reason: "Line 6 of each worksheet subtracts a threshold printed for that worksheet. Examples are $161,550 (ws 2), $323,200 (ws 3), $2,155,350 (ws 4), $5,000,000 (ws 5, 10, 15), $215,400 (ws 8), $1,077,550 (ws 9), $269,300 (ws 13) and $1,616,450 (ws 14). Binding that printed amount as an input matches the text."
  - key: "3"
    status: MATCH
    reason: "Line 3 is \"Enter your New York State tax on the line 2 amount from the New York State tax rate schedule.\" The glossary's bands, rates, base amounts and thresholds match all three schedules. The mapping also matches: single and MFS use the single schedule, MFJ and QSS use the MFJ schedule, HOH uses the HOH schedule. Rounding each band's product to the dollar is not stated in the schedule but changes the result by cents at most."
  - key: "4"
    status: MATCH
    reason: "Line 4 is the printed \"Recapture Base amount\" for each worksheet, for example 333, 1,140, 3,887, 64,237, 568, 2,399, 32,571, 787, 3,076 and 48,337. Binding the printed amount as an input matches."
  - key: "5"
    status: MATCH
    reason: "Line 5 is the printed \"Incremental Benefit amount\" for each worksheet, for example 807, 2,747, 60,350, 32,500, 1,831, 30,172, 2,289 and 45,261. Binding the printed amount as an input matches."
  - key: "6"
    status: MATCH
    reason: "Line 6 is \"Enter the excess of line 1 over $[threshold]\". Subtracting the threshold from line 1 with a floor of zero matches \"excess\"."
  - key: "(7)"
    status: MATCH
    reason: "Line 7 says \"Enter the lesser of line 6 or $50,000\", so the $50,000 cap matches."
  - key: "7"
    status: MATCH
    reason: "Line 7 is \"Enter the lesser of line 6 or $50,000\", and the smaller of line 6 or $50,000 matches."
  - key: "(scale) (hundred)"
    status: MATCH
    reason: "This scaling constant of 100 is not on the form. It is a computational device, and its effect is undone by the 1% factor on line 9, so it does not change any printed line."
  - key: "(scale) (line9_scaled)"
    status: MATCH
    reason: "This is an intermediate value equal to line 5 times 100. It is not printed and is reversed on line 9, so the net effect is line 5 times line 8, as the form requires."
  - key: "8, 9"
    status: MATCH
    reason: "Line 8 is \"Divide line 7 by $50,000 and round the result to the fourth decimal place\", and line 9 is \"Multiply line 5 by line 8\". The program divides with 4-decimal rounding and multiplies the scaled line 5, which matches. The clamp to [0,1] has no effect because line 7 cannot exceed $50,000."
  - key: "9"
    status: MATCH
    reason: "Multiplying by 0.01 reverses the ×100 scaling, giving \"Multiply line 5 by line 8\". Rounding to the whole dollar is not stated in the text given, but it affects cents only."
  - key: "10"
    status: MATCH
    reason: "Line 10 is \"Add lines 3, 4, and 9. Enter here and on line 39.\" The restatement adds lines 3, 4 and 9."
```
```
