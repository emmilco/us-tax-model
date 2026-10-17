# Render comparison — qdcg

The rendered English of every printed line of `Qualified Dividends and Capital Gain Tax Worksheet—Line 16` (`rendered/2025/qdcg.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 02379427f705c3fd04c80df1d44aecb12974a71906238a9a1e6626dc6ff2326b |
| lines judged | 25 |
| match / mismatch / unclear / missing | 21 / 1 / 3 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing Form 2555 
Status: **MISMATCH**

Restated: Enter the amount from f1040 line 15.

Model: The restatement always uses f1040 line 15 and names no refusal for Form 2555 filers. The IRS text says "However, if you are filing Form 2555 (relating to foreign earned income), enter the amount from line 3 of the Foreign Earned Income Tax Worksheet."

Ruling: scope; project retained. The Foreign Earned Income Tax Worksheet alternative applies only to a filer who claimed the exclusion or housing deduction on Form 2555 (i1040gi p. 36, line 16: "If you claimed the foreign earned income exclusion, housing exclusion, or housing deduction on Form 2555, you must use the Foreign Earned Income Tax Worksheet"). That filer reports the exclusion on Schedule 1, line 8d (i1040gi p. 91: "Foreign earned income exclusion and housing exclusion from Form 2555"), and the return refuses any Schedule 1 income at Form 1040 line 8 (`scope.schedule1`, forms/2025/f1040.yaml) before line 16 is reached. The alternative is recorded as not encoded in the worksheet note. No change to the data.

### 2 — Enter the amount from Form 1040 or 1040-SR, line 3a
Status: **MATCH**

Model: The IRS line says "Enter the amount from Form 1040 or 1040-SR, line 3a" and the restatement does the same. The asterisk sends Form 2555 filers to a Foreign Earned Income Tax Worksheet footnote, whose content is not in the pages given.

### 3 — Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Schedule D. If 
Status: **UNCLEAR**

Restated: Choose — [helper "Are you filing Schedule D?" = true → helper "Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-."] [helper "Are you filing Schedule D?" = false → sd helper "Capital gain distributions, generally Form 1099-DIV box 2a"]

Model: The Yes branch, the smaller of Schedule D lines 15 and 16 floored at zero, matches the IRS wording. But the IRS No branch says "Enter the amount from Form 1040 or 1040-SR, line 7a", while the program uses 1099-DIV box 2a distributions, and whether the program's Schedule D gate equals "Are you filing Schedule D?" depends on Form 1040 line 7a and Schedule D filing rules that are not in the text given.

Ruling: representation; project retained. "Are you filing Schedule D?" is derived rather than asked: Schedule D is required when any sale is entered or a 28% or unrecaptured section 1250 amount exists, and a filer with only capital gain distributions need not file it (i1040gi p. 31, line 7a, Exception 1: "You don't have to file Form 8949 or Schedule D if you aren't deferring any capital gain by investing in a qualified opportunity fund and both of the following apply. 1. You have no capital losses, and your only capital gains are capital gain distributions"), in which case line 7a carries the Form 1099-DIV box 2a total the No branch reads. The transcription log for qdcg carries the same ruling. No change to the data.

### 4 — Add lines 2 and 3
Status: **MATCH**

Model: The IRS line says "Add lines 2 and 3" and the restatement does the same.

### 5 — Subtract line 4 from line 1. If zero or less, enter -0-
Status: **MATCH**

Model: The IRS line says "Subtract line 4 from line 1. If zero or less, enter -0-" and the restatement does the same.

### 6 — Enter: $48,350 if single or married filing separately, $96,700 if married filing jointly o
Status: **MATCH**

Model: The amounts match the IRS text: $48,350 single/MFS, $96,700 MFJ/QSS, and $64,750 HOH.

### 7 — Enter the smaller of line 1 or line 6
Status: **MATCH**

Model: The IRS line says "Enter the smaller of line 1 or line 6" and the restatement does the same.

### 8 — Enter the smaller of line 5 or line 7
Status: **MATCH**

Model: The IRS line says "Enter the smaller of line 5 or line 7" and the restatement does the same.

### 9 — Subtract line 8 from line 7. This amount is taxed at 0%
Status: **MATCH**

Model: The IRS line says "Subtract line 8 from line 7" and the restatement does the same.

### 10 — Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: The IRS line says "Enter the smaller of line 1 or line 4" and the restatement does the same.

### 11 — Enter the amount from line 9
Status: **MATCH**

Model: The IRS line says "Enter the amount from line 9" and the restatement does the same.

### 12 — Subtract line 11 from line 10
Status: **MATCH**

Model: The IRS line says "Subtract line 11 from line 10" and the restatement does the same.

### 13 — Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if married fili
Status: **MATCH**

Model: The amounts match the IRS text: $533,400 single, $300,000 MFS, $600,050 MFJ/QSS, and $566,700 HOH.

### 14 — Enter the smaller of line 1 or line 13
Status: **MATCH**

Model: The IRS line says "Enter the smaller of line 1 or line 13" and the restatement does the same.

### 15 — Add lines 5 and 9
Status: **MATCH**

Model: The IRS line says "Add lines 5 and 9" and the restatement does the same.

### 16 — Subtract line 15 from line 14. If zero or less, enter -0-
Status: **MATCH**

Model: The IRS line says "Subtract line 15 from line 14. If zero or less, enter -0-" and the restatement does the same.

### 17 — Enter the smaller of line 12 or line 16
Status: **MATCH**

Model: The IRS line says "Enter the smaller of line 12 or line 16" and the restatement does the same.

### 18 — Multiply line 17 by 15% (0.15)
Status: **MATCH**

Model: The IRS line says "Multiply line 17 by 15% (0.15)" and the restatement does the same.

### 19 — Add lines 9 and 17
Status: **MATCH**

Model: The IRS line says "Add lines 9 and 17" and the restatement does the same.

### 20 — Subtract line 19 from line 10
Status: **MATCH**

Model: The IRS line says "Subtract line 19 from line 10" and the restatement does the same.

### 21 — Multiply line 20 by 20% (0.20)
Status: **MATCH**

Model: The IRS line says "Multiply line 20 by 20% (0.20)" and the restatement does the same.

### 22 — Figure the tax on the amount on line 5. If the amount on line 5 is less than $100,000, use
Status: **UNCLEAR**

Restated: Enter "tax" of Tax on an amount — Tax Table or Tax Computation Worksheet with amount = line 5 and status = f1040 line Filing Status.

Model: The operand (line 5) and filing status are right. The IRS requires the Tax Table "if the amount on line 5 is less than $100,000" and the Tax Computation Worksheet otherwise, but the program's tax helper is not defined in the glossary, so its selection rule cannot be checked.

Ruling: representation; project retained. 'Tax on an amount' (`forms/2025/tax_on_amount.yaml`) uses the Tax Table below $100,000 and the Tax Computation Worksheet at $100,000 or more (i1040gi line 16), as line 22 says; the glossary does not yet carry shared-definition references (T-009).

### 23 — Add lines 18, 21, and 22
Status: **MATCH**

Model: The IRS line says "Add lines 18, 21, and 22" and the restatement does the same.

### 24 — Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use
Status: **UNCLEAR**

Restated: Enter "tax" of Tax on an amount — Tax Table or Tax Computation Worksheet with amount = line 1 and status = f1040 line Filing Status.

Model: The operand (line 1) and filing status are right. The IRS requires the Tax Table if line 1 "is less than $100,000" and the Tax Computation Worksheet otherwise, but the tax helper is not defined in the glossary, so its selection rule cannot be checked.

Ruling: representation; project retained. As for line 22 (T-009).

### 25 — Tax on all taxable income. Enter the smaller of line 23 or line 24. Also include this amou
Status: **MATCH**

Model: The IRS line says "Enter the smaller of line 23 or line 24" and the restatement does the same. The Form 2555 instruction only changes where the amount is carried, not its value.

## Raw response

```yaml
```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "The restatement always uses f1040 line 15 and names no refusal for Form 2555 filers. The IRS text says \"However, if you are filing Form 2555 (relating to foreign earned income), enter the amount from line 3 of the Foreign Earned Income Tax Worksheet.\""
  - key: "2"
    status: MATCH
    reason: "The IRS line says \"Enter the amount from Form 1040 or 1040-SR, line 3a\" and the restatement does the same. The asterisk sends Form 2555 filers to a Foreign Earned Income Tax Worksheet footnote, whose content is not in the pages given."
  - key: "3"
    status: UNCLEAR
    reason: "The Yes branch, the smaller of Schedule D lines 15 and 16 floored at zero, matches the IRS wording. But the IRS No branch says \"Enter the amount from Form 1040 or 1040-SR, line 7a\", while the program uses 1099-DIV box 2a distributions, and whether the program's Schedule D gate equals \"Are you filing Schedule D?\" depends on Form 1040 line 7a and Schedule D filing rules that are not in the text given."
  - key: "4"
    status: MATCH
    reason: "The IRS line says \"Add lines 2 and 3\" and the restatement does the same."
  - key: "5"
    status: MATCH
    reason: "The IRS line says \"Subtract line 4 from line 1. If zero or less, enter -0-\" and the restatement does the same."
  - key: "6"
    status: MATCH
    reason: "The amounts match the IRS text: $48,350 single/MFS, $96,700 MFJ/QSS, and $64,750 HOH."
  - key: "7"
    status: MATCH
    reason: "The IRS line says \"Enter the smaller of line 1 or line 6\" and the restatement does the same."
  - key: "8"
    status: MATCH
    reason: "The IRS line says \"Enter the smaller of line 5 or line 7\" and the restatement does the same."
  - key: "9"
    status: MATCH
    reason: "The IRS line says \"Subtract line 8 from line 7\" and the restatement does the same."
  - key: "10"
    status: MATCH
    reason: "The IRS line says \"Enter the smaller of line 1 or line 4\" and the restatement does the same."
  - key: "11"
    status: MATCH
    reason: "The IRS line says \"Enter the amount from line 9\" and the restatement does the same."
  - key: "12"
    status: MATCH
    reason: "The IRS line says \"Subtract line 11 from line 10\" and the restatement does the same."
  - key: "13"
    status: MATCH
    reason: "The amounts match the IRS text: $533,400 single, $300,000 MFS, $600,050 MFJ/QSS, and $566,700 HOH."
  - key: "14"
    status: MATCH
    reason: "The IRS line says \"Enter the smaller of line 1 or line 13\" and the restatement does the same."
  - key: "15"
    status: MATCH
    reason: "The IRS line says \"Add lines 5 and 9\" and the restatement does the same."
  - key: "16"
    status: MATCH
    reason: "The IRS line says \"Subtract line 15 from line 14. If zero or less, enter -0-\" and the restatement does the same."
  - key: "17"
    status: MATCH
    reason: "The IRS line says \"Enter the smaller of line 12 or line 16\" and the restatement does the same."
  - key: "18"
    status: MATCH
    reason: "The IRS line says \"Multiply line 17 by 15% (0.15)\" and the restatement does the same."
  - key: "19"
    status: MATCH
    reason: "The IRS line says \"Add lines 9 and 17\" and the restatement does the same."
  - key: "20"
    status: MATCH
    reason: "The IRS line says \"Subtract line 19 from line 10\" and the restatement does the same."
  - key: "21"
    status: MATCH
    reason: "The IRS line says \"Multiply line 20 by 20% (0.20)\" and the restatement does the same."
  - key: "22"
    status: UNCLEAR
    reason: "The operand (line 5) and filing status are right. The IRS requires the Tax Table \"if the amount on line 5 is less than $100,000\" and the Tax Computation Worksheet otherwise, but the program's tax helper is not defined in the glossary, so its selection rule cannot be checked."
  - key: "23"
    status: MATCH
    reason: "The IRS line says \"Add lines 18, 21, and 22\" and the restatement does the same."
  - key: "24"
    status: UNCLEAR
    reason: "The operand (line 1) and filing status are right. The IRS requires the Tax Table if line 1 \"is less than $100,000\" and the Tax Computation Worksheet otherwise, but the tax helper is not defined in the glossary, so its selection rule cannot be checked."
  - key: "25"
    status: MATCH
    reason: "The IRS line says \"Enter the smaller of line 23 or line 24\" and the restatement does the same. The Form 2555 instruction only changes where the amount is carried, not its value."
```
```
