# Render comparison — qdcg

The rendered English of every printed line of `Qualified Dividends and Capital Gain Tax Worksheet—Line 16` (`rendered/2025/qdcg.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 95425a4256973d579468ca5f55a9423fae12fd42b208622fb017404f80875acb |
| lines judged | 25 |
| match / mismatch / unclear / missing | 20 / 1 / 4 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |

## Lines

### 1 — Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing Form 2555 
Status: **MISMATCH**

Restated: Enter the amount from f1040 line 15.

Model: The restatement always uses f1040 line 15. The IRS text says "However, if you are filing Form 2555 (relating to foreign earned income), enter the amount from line 3 of the Foreign Earned Income Tax Worksheet." No refusal names the Form 2555 case.

Ruling: scope; project retained. The Foreign Earned Income Tax Worksheet alternative applies only to a filer who claimed the exclusion or housing deduction on Form 2555 (i1040gi p. 36, line 16: "If you claimed the foreign earned income exclusion, housing exclusion, or housing deduction on Form 2555, you must use the Foreign Earned Income Tax Worksheet"). That filer reports the exclusion on Schedule 1, line 8d (i1040gi p. 91: "Foreign earned income exclusion and housing exclusion from Form 2555"), and the return refuses any Schedule 1 income at Form 1040 line 8 (`scope.schedule1`, forms/2025/f1040.yaml) before line 16 is reached. The alternative is recorded as not encoded in the worksheet note. No change to the data.

### 2 — Enter the amount from Form 1040 or 1040-SR, line 3a
Status: **UNCLEAR**

Restated: Enter the amount from f1040 line 3a.

Model: Entering f1040 line 3a matches the line's own words. The asterisk footnote says "If you are filing Form 2555, see the footnote in the Foreign Earned Income Tax Worksheet." That footnote's text is not given, and no refusal covers Form 2555.

Ruling: scope; project retained. The footnote applies only to Form 2555 filers, who are refused at Form 1040 line 8 through `scope.schedule1` because the exclusion is a Schedule 1, line 8d entry (i1040gi p. 91). Same ground as line 1. No change to the data.

### 3 — Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Schedule D. If 
Status: **UNCLEAR**

Restated: Choose — [helper "Are you filing Schedule D?" = true → helper "Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-."] [helper "Are you filing Schedule D?" = false → sd helper "Capital gain distributions, generally Form 1099-DIV box 2a"]

Model: The Yes branch matches, because the smaller of Schedule D lines 15 and 16 floored at zero gives -0- when either line is a loss. For No, the IRS says "Enter the amount from Form 1040 or 1040-SR, line 7a" but the program uses a 1099-DIV box 2a input, and the text given does not show these are equal. The text also does not support the program's test for whether Schedule D is filed.

Ruling: representation; project retained. "Are you filing Schedule D?" is derived rather than asked: Schedule D is required when any sale is entered or a 28% or unrecaptured section 1250 amount exists, and a filer with only capital gain distributions need not file it (i1040gi p. 31, line 7a, Exception 1: "You don't have to file Form 8949 or Schedule D if you aren't deferring any capital gain by investing in a qualified opportunity fund and both of the following apply. 1. You have no capital losses, and your only capital gains are capital gain distributions"), in which case line 7a carries the Form 1099-DIV box 2a total the No branch reads. The transcription log for qdcg carries the same ruling. No change to the data.

### 4 — Add lines 2 and 3
Status: **MATCH**

Model: "Add lines 2 and 3."

### 5 — Subtract line 4 from line 1. If zero or less, enter -0-
Status: **MATCH**

Model: "Subtract line 4 from line 1. If zero or less, enter -0-."

### 6 — Enter: $48,350 if single or married filing separately, $96,700 if married filing jointly o
Status: **MATCH**

Model: The amounts match: $48,350 single/MFS, $96,700 MFJ/QSS, $64,750 HOH.

### 7 — Enter the smaller of line 1 or line 6
Status: **MATCH**

Model: "Enter the smaller of line 1 or line 6."

### 8 — Enter the smaller of line 5 or line 7
Status: **MATCH**

Model: "Enter the smaller of line 5 or line 7."

### 9 — Subtract line 8 from line 7. This amount is taxed at 0%
Status: **MATCH**

Model: "Subtract line 8 from line 7."

### 10 — Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: "Enter the smaller of line 1 or line 4."

### 11 — Enter the amount from line 9
Status: **MATCH**

Model: "Enter the amount from line 9."

### 12 — Subtract line 11 from line 10
Status: **MATCH**

Model: "Subtract line 11 from line 10."

### 13 — Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if married fili
Status: **MATCH**

Model: The amounts match: $533,400 single, $300,000 MFS, $600,050 MFJ/QSS, $566,700 HOH.

### 14 — Enter the smaller of line 1 or line 13
Status: **MATCH**

Model: "Enter the smaller of line 1 or line 13."

### 15 — Add lines 5 and 9
Status: **MATCH**

Model: "Add lines 5 and 9."

### 16 — Subtract line 15 from line 14. If zero or less, enter -0-
Status: **MATCH**

Model: "Subtract line 15 from line 14. If zero or less, enter -0-."

### 17 — Enter the smaller of line 12 or line 16
Status: **MATCH**

Model: "Enter the smaller of line 12 or line 16."

### 18 — Multiply line 17 by 15% (0.15)
Status: **MATCH**

Model: "Multiply line 17 by 15% (0.15)."

### 19 — Add lines 9 and 17
Status: **MATCH**

Model: "Add lines 9 and 17."

### 20 — Subtract line 19 from line 10
Status: **MATCH**

Model: "Subtract line 19 from line 10."

### 21 — Multiply line 20 by 20% (0.20)
Status: **MATCH**

Model: "Multiply line 20 by 20% (0.20)."

### 22 — Figure the tax on the amount on line 5. If the amount on line 5 is less than $100,000, use
Status: **UNCLEAR**

Restated: Enter "tax" of Tax on an amount — Tax Table or Tax Computation Worksheet with amount = line 5 and status = f1040 line Filing Status.

Model: The IRS says to use the Tax Table "If the amount on line 5 is less than $100,000" and the Tax Computation Worksheet if it is "$100,000 or more." The "Tax on an amount" helper is not defined in the glossary, so whether it applies this $100,000 switch cannot be checked.

Ruling: representation; project retained. "Tax on an amount" is the shared definition that applies the $100,000 switch the line states: its line (b) chooses the Tax Table when the amount is below $100,000 (`ordinary.table_boundary`) and the Tax Computation Worksheet at or above (forms/2025/tax_on_amount.yaml; its own render log, 4 lines, all MATCH). No change to the data.

### 23 — Add lines 18, 21, and 22
Status: **MATCH**

Model: "Add lines 18, 21, and 22."

### 24 — Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use
Status: **UNCLEAR**

Restated: Enter "tax" of Tax on an amount — Tax Table or Tax Computation Worksheet with amount = line 1 and status = f1040 line Filing Status.

Model: The IRS says to use the Tax Table "If the amount on line 1 is less than $100,000" and the Tax Computation Worksheet otherwise. The "Tax on an amount" helper is undefined, so whether it applies this switch cannot be checked.

Ruling: representation; project retained. Same ground as line 22. No change to the data.

### 25 — Tax on all taxable income. Enter the smaller of line 23 or line 24. Also include this amou
Status: **MATCH**

Model: "Enter the smaller of line 23 or line 24." The Form 2555 instruction only changes where the amount is entered, not its value.

## Raw response

```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The restatement always uses f1040 line 15. The IRS text says \"However, if you are filing Form 2555 (relating to foreign earned income), enter the amount from line 3 of the Foreign Earned Income Tax Worksheet.\" No refusal names the Form 2555 case."
  - key: "2"
    status: UNCLEAR
    reason: "Entering f1040 line 3a matches the line's own words. The asterisk footnote says \"If you are filing Form 2555, see the footnote in the Foreign Earned Income Tax Worksheet.\" That footnote's text is not given, and no refusal covers Form 2555."
  - key: "3"
    status: UNCLEAR
    reason: "The Yes branch matches, because the smaller of Schedule D lines 15 and 16 floored at zero gives -0- when either line is a loss. For No, the IRS says \"Enter the amount from Form 1040 or 1040-SR, line 7a\" but the program uses a 1099-DIV box 2a input, and the text given does not show these are equal. The text also does not support the program's test for whether Schedule D is filed."
  - key: "4"
    status: MATCH
    reason: "\"Add lines 2 and 3.\""
  - key: "5"
    status: MATCH
    reason: "\"Subtract line 4 from line 1. If zero or less, enter -0-.\""
  - key: "6"
    status: MATCH
    reason: "The amounts match: $48,350 single/MFS, $96,700 MFJ/QSS, $64,750 HOH."
  - key: "7"
    status: MATCH
    reason: "\"Enter the smaller of line 1 or line 6.\""
  - key: "8"
    status: MATCH
    reason: "\"Enter the smaller of line 5 or line 7.\""
  - key: "9"
    status: MATCH
    reason: "\"Subtract line 8 from line 7.\""
  - key: "10"
    status: MATCH
    reason: "\"Enter the smaller of line 1 or line 4.\""
  - key: "11"
    status: MATCH
    reason: "\"Enter the amount from line 9.\""
  - key: "12"
    status: MATCH
    reason: "\"Subtract line 11 from line 10.\""
  - key: "13"
    status: MATCH
    reason: "The amounts match: $533,400 single, $300,000 MFS, $600,050 MFJ/QSS, $566,700 HOH."
  - key: "14"
    status: MATCH
    reason: "\"Enter the smaller of line 1 or line 13.\""
  - key: "15"
    status: MATCH
    reason: "\"Add lines 5 and 9.\""
  - key: "16"
    status: MATCH
    reason: "\"Subtract line 15 from line 14. If zero or less, enter -0-.\""
  - key: "17"
    status: MATCH
    reason: "\"Enter the smaller of line 12 or line 16.\""
  - key: "18"
    status: MATCH
    reason: "\"Multiply line 17 by 15% (0.15).\""
  - key: "19"
    status: MATCH
    reason: "\"Add lines 9 and 17.\""
  - key: "20"
    status: MATCH
    reason: "\"Subtract line 19 from line 10.\""
  - key: "21"
    status: MATCH
    reason: "\"Multiply line 20 by 20% (0.20).\""
  - key: "22"
    status: UNCLEAR
    reason: "The IRS says to use the Tax Table \"If the amount on line 5 is less than $100,000\" and the Tax Computation Worksheet if it is \"$100,000 or more.\" The \"Tax on an amount\" helper is not defined in the glossary, so whether it applies this $100,000 switch cannot be checked."
  - key: "23"
    status: MATCH
    reason: "\"Add lines 18, 21, and 22.\""
  - key: "24"
    status: UNCLEAR
    reason: "The IRS says to use the Tax Table \"If the amount on line 1 is less than $100,000\" and the Tax Computation Worksheet otherwise. The \"Tax on an amount\" helper is undefined, so whether it applies this switch cannot be checked."
  - key: "25"
    status: MATCH
    reason: "\"Enter the smaller of line 23 or line 24.\" The Form 2555 instruction only changes where the amount is entered, not its value."
```
