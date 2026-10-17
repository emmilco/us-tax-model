# Render comparison — qdcg

The rendered English of every printed line of `Qualified Dividends and Capital Gain Tax Worksheet—Line 16` (`rendered/2025/qdcg.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 02379427f705c3fd04c80df1d44aecb12974a71906238a9a1e6626dc6ff2326b |
| lines judged | 25 |
| match / mismatch / unclear / missing | 22 / 2 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | 816ff8c5ed82d0349bfa79ae008e9b4492c04005a8702145dcd8cd0139eacc47 |

## Lines

### 1 — Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing Form 2555 
Status: **MISMATCH**

Restated: Enter the amount from f1040 line 15.

Model: The restatement always uses f1040 line 15 and has no refusal for Form 2555 filers. The IRS line adds "However, if you are filing Form 2555 (relating to foreign earned income), enter the amount from line 3 of the Foreign Earned Income Tax Worksheet."

Ruling: scope; project retained. The Foreign Earned Income Tax Worksheet alternative applies only to a filer who claimed the exclusion or housing deduction on Form 2555 (i1040gi p. 36, line 16: "If you claimed the foreign earned income exclusion, housing exclusion, or housing deduction on Form 2555, you must use the Foreign Earned Income Tax Worksheet"). That filer reports the exclusion on Schedule 1, line 8d (i1040gi p. 91: "Foreign earned income exclusion and housing exclusion from Form 2555"), and the return refuses any Schedule 1 income at Form 1040 line 8 (`scope.schedule1`, forms/2025/f1040.yaml) before line 16 is reached. The alternative is recorded as not encoded in the worksheet note. No change to the data.

### 2 — Enter the amount from Form 1040 or 1040-SR, line 3a
Status: **UNCLEAR**

Restated: Enter the amount from f1040 line 3a.

Model: The restatement matches "Enter the amount from Form 1040 or 1040-SR, line 3a". However, the asterisk footnote says Form 2555 filers must "see the footnote in the Foreign Earned Income Tax Worksheet before completing this line," and that footnote's text is not provided, so its effect on the value cannot be judged.

Ruling: scope; project retained. The footnote applies only to Form 2555 filers, who are refused at Form 1040 line 8 through `scope.schedule1` because the exclusion is a Schedule 1, line 8d entry (i1040gi p. 91). Same ground as line 1. No change to the data.

### 3 — Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Schedule D. If 
Status: **MISMATCH**

Restated: Choose — [helper "Are you filing Schedule D?" = true → helper "Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-."] [helper "Are you filing Schedule D?" = false → sd helper "Capital gain distributions, generally Form 1099-DIV box 2a"]

Model: The Yes branch matches the Schedule D lines 15/16 rule. The No branch differs: the IRS says "No. Enter the amount from Form 1040 or 1040-SR, line 7a," but the program uses a separate input ("Capital gain distributions, generally Form 1099-DIV box 2a"). The text given does not tie this input to line 7a, and the Form 2555 footnote on this line is also not modeled.

Ruling: representation; project retained. "Are you filing Schedule D?" is derived rather than asked: Schedule D is required when any sale is entered or a 28% or unrecaptured section 1250 amount exists, and a filer with only capital gain distributions need not file it (i1040gi p. 31, line 7a, Exception 1: "You don't have to file Form 8949 or Schedule D if you aren't deferring any capital gain by investing in a qualified opportunity fund and both of the following apply. 1. You have no capital losses, and your only capital gains are capital gain distributions"), in which case line 7a carries the Form 1099-DIV box 2a total the No branch reads. The transcription log for qdcg carries the same ruling. No change to the data.

### 4 — Add lines 2 and 3
Status: **MATCH**

Model: Matches "Add lines 2 and 3."

### 5 — Subtract line 4 from line 1. If zero or less, enter -0-
Status: **MATCH**

Model: Matches "Subtract line 4 from line 1. If zero or less, enter -0-."

### 6 — Enter: $48,350 if single or married filing separately, $96,700 if married filing jointly o
Status: **MATCH**

Model: The amounts match: $48,350 for single or married filing separately, $96,700 for married filing jointly or qualifying surviving spouse, and $64,750 for head of household.

### 7 — Enter the smaller of line 1 or line 6
Status: **MATCH**

Model: Matches "Enter the smaller of line 1 or line 6."

### 8 — Enter the smaller of line 5 or line 7
Status: **MATCH**

Model: Matches "Enter the smaller of line 5 or line 7."

### 9 — Subtract line 8 from line 7. This amount is taxed at 0%
Status: **MATCH**

Model: Matches "Subtract line 8 from line 7."

### 10 — Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: Matches "Enter the smaller of line 1 or line 4."

### 11 — Enter the amount from line 9
Status: **MATCH**

Model: Matches "Enter the amount from line 9."

### 12 — Subtract line 11 from line 10
Status: **MATCH**

Model: Matches "Subtract line 11 from line 10."

### 13 — Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if married fili
Status: **MATCH**

Model: The amounts match: $533,400 for single, $300,000 for married filing separately, $600,050 for married filing jointly or qualifying surviving spouse, and $566,700 for head of household.

### 14 — Enter the smaller of line 1 or line 13
Status: **MATCH**

Model: Matches "Enter the smaller of line 1 or line 13."

### 15 — Add lines 5 and 9
Status: **MATCH**

Model: Matches "Add lines 5 and 9."

### 16 — Subtract line 15 from line 14. If zero or less, enter -0-
Status: **MATCH**

Model: Matches "Subtract line 15 from line 14. If zero or less, enter -0-."

### 17 — Enter the smaller of line 12 or line 16
Status: **MATCH**

Model: Matches "Enter the smaller of line 12 or line 16."

### 18 — Multiply line 17 by 15% (0.15)
Status: **MATCH**

Model: Matches "Multiply line 17 by 15% (0.15)."

### 19 — Add lines 9 and 17
Status: **MATCH**

Model: Matches "Add lines 9 and 17."

### 20 — Subtract line 19 from line 10
Status: **MATCH**

Model: Matches "Subtract line 19 from line 10."

### 21 — Multiply line 20 by 20% (0.20)
Status: **MATCH**

Model: Matches "Multiply line 20 by 20% (0.20)."

### 22 — Figure the tax on the amount on line 5. If the amount on line 5 is less than $100,000, use
Status: **MATCH**

Model: Both figure the tax on line 5 using the Tax Table or the Tax Computation Worksheet with the filer's filing status. The IRS line chooses between them at $100,000, which the named tax helper is understood to apply.

### 23 — Add lines 18, 21, and 22
Status: **MATCH**

Model: Matches "Add lines 18, 21, and 22."

### 24 — Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use
Status: **MATCH**

Model: Both figure the tax on line 1 using the Tax Table or the Tax Computation Worksheet with the filer's filing status.

### 25 — Tax on all taxable income. Enter the smaller of line 23 or line 24. Also include this amou
Status: **MATCH**

Model: Matches "Enter the smaller of line 23 or line 24." The instruction on where to carry the amount (Form 1040 line 16, or the Foreign Earned Income Tax Worksheet for Form 2555 filers) does not change this line's value.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The restatement always uses f1040 line 15 and has no refusal for Form 2555 filers. The IRS line adds \"However, if you are filing Form 2555 (relating to foreign earned income), enter the amount from line 3 of the Foreign Earned Income Tax Worksheet.\""
  - key: "2"
    status: UNCLEAR
    reason: "The restatement matches \"Enter the amount from Form 1040 or 1040-SR, line 3a\". However, the asterisk footnote says Form 2555 filers must \"see the footnote in the Foreign Earned Income Tax Worksheet before completing this line,\" and that footnote's text is not provided, so its effect on the value cannot be judged."
  - key: "3"
    status: MISMATCH
    reason: "The Yes branch matches the Schedule D lines 15/16 rule. The No branch differs: the IRS says \"No. Enter the amount from Form 1040 or 1040-SR, line 7a,\" but the program uses a separate input (\"Capital gain distributions, generally Form 1099-DIV box 2a\"). The text given does not tie this input to line 7a, and the Form 2555 footnote on this line is also not modeled."
  - key: "4"
    status: MATCH
    reason: "Matches \"Add lines 2 and 3.\""
  - key: "5"
    status: MATCH
    reason: "Matches \"Subtract line 4 from line 1. If zero or less, enter -0-.\""
  - key: "6"
    status: MATCH
    reason: "The amounts match: $48,350 for single or married filing separately, $96,700 for married filing jointly or qualifying surviving spouse, and $64,750 for head of household."
  - key: "7"
    status: MATCH
    reason: "Matches \"Enter the smaller of line 1 or line 6.\""
  - key: "8"
    status: MATCH
    reason: "Matches \"Enter the smaller of line 5 or line 7.\""
  - key: "9"
    status: MATCH
    reason: "Matches \"Subtract line 8 from line 7.\""
  - key: "10"
    status: MATCH
    reason: "Matches \"Enter the smaller of line 1 or line 4.\""
  - key: "11"
    status: MATCH
    reason: "Matches \"Enter the amount from line 9.\""
  - key: "12"
    status: MATCH
    reason: "Matches \"Subtract line 11 from line 10.\""
  - key: "13"
    status: MATCH
    reason: "The amounts match: $533,400 for single, $300,000 for married filing separately, $600,050 for married filing jointly or qualifying surviving spouse, and $566,700 for head of household."
  - key: "14"
    status: MATCH
    reason: "Matches \"Enter the smaller of line 1 or line 13.\""
  - key: "15"
    status: MATCH
    reason: "Matches \"Add lines 5 and 9.\""
  - key: "16"
    status: MATCH
    reason: "Matches \"Subtract line 15 from line 14. If zero or less, enter -0-.\""
  - key: "17"
    status: MATCH
    reason: "Matches \"Enter the smaller of line 12 or line 16.\""
  - key: "18"
    status: MATCH
    reason: "Matches \"Multiply line 17 by 15% (0.15).\""
  - key: "19"
    status: MATCH
    reason: "Matches \"Add lines 9 and 17.\""
  - key: "20"
    status: MATCH
    reason: "Matches \"Subtract line 19 from line 10.\""
  - key: "21"
    status: MATCH
    reason: "Matches \"Multiply line 20 by 20% (0.20).\""
  - key: "22"
    status: MATCH
    reason: "Both figure the tax on line 5 using the Tax Table or the Tax Computation Worksheet with the filer's filing status. The IRS line chooses between them at $100,000, which the named tax helper is understood to apply."
  - key: "23"
    status: MATCH
    reason: "Matches \"Add lines 18, 21, and 22.\""
  - key: "24"
    status: MATCH
    reason: "Both figure the tax on line 1 using the Tax Table or the Tax Computation Worksheet with the filer's filing status."
  - key: "25"
    status: MATCH
    reason: "Matches \"Enter the smaller of line 23 or line 24.\" The instruction on where to carry the amount (Form 1040 line 16, or the Foreign Earned Income Tax Worksheet for Form 2555 filers) does not change this line's value."
```
```
