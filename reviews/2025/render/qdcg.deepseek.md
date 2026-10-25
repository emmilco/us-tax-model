# Render comparison — qdcg

The rendered English of every printed line of `Qualified Dividends and Capital Gain Tax Worksheet—Line 16` (`rendered/2025/qdcg.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | bffeb9cae3b50865d62a1f53ecd761793e10d29be53a5456ccc272e251c66a7d |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | a0b25be8a95c5226b85d36309782603707173964eec03a7a57b0dc3c10ccb305 |
| lines judged | 25 |
| match / mismatch / unclear / missing | 23 / 1 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### 1 — Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing Form 2555 
Status: **MISMATCH**

Restated: Enter the amount from f1040 line 15.

Model: IRS line 1 says to use Form 1040 line 15, but adds: 'However, if you are filing Form 2555 ... enter the amount from line 3 of the Foreign Earned Income Tax Worksheet.' The restatement always uses Form 1040 line 15 and has no Form 2555 refusal or alternate.

Ruling: open

### 2 — Enter the amount from Form 1040 or 1040-SR, line 3a
Status: **MATCH**

Model: IRS line 2 says to enter the Form 1040 or 1040-SR line 3a amount, and the restatement says to use f1040 line 3a.

### 3 — Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Schedule D. If 
Status: **UNCLEAR**

Restated: Choose — [helper "Are you filing Schedule D?" = true → helper "Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-."] [helper "Are you filing Schedule D?" = false → sd helper "Capital gain distributions, generally Form 1099-DIV box 2a"]

Model: The Schedule D 'Yes' branch matches, but for the 'No' branch IRS says 'Enter the amount from Form 1040 or 1040-SR, line 7a'; the provided text does not define line 7a, so the program's use of a 'Capital gain distributions, generally Form 1099-DIV box 2a' helper cannot be verified.

Ruling: open

### 4 — Add lines 2 and 3
Status: **MATCH**

Model: IRS line 4 is 'Add lines 2 and 3'; the restatement adds line 2 and line 3.

### 5 — Subtract line 4 from line 1. If zero or less, enter -0-
Status: **MATCH**

Model: IRS line 5 is subtract line 4 from line 1 with a zero floor; the restatement is the same.

### 6 — Enter: $48,350 if single or married filing separately, $96,700 if married filing jointly o
Status: **MATCH**

Model: IRS line 6 uses $48,350 for single or MFS, $96,700 for MFJ or QSS, and $64,750 for HOH; the restatement matches.

### 7 — Enter the smaller of line 1 or line 6
Status: **MATCH**

Model: IRS line 7 is the smaller of line 1 or line 6; the restatement is the same.

### 8 — Enter the smaller of line 5 or line 7
Status: **MATCH**

Model: IRS line 8 is the smaller of line 5 or line 7; the restatement is the same.

### 9 — Subtract line 8 from line 7. This amount is taxed at 0%
Status: **MATCH**

Model: IRS line 9 is line 7 minus line 8; the restatement is the same.

### 10 — Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: IRS line 10 is the smaller of line 1 or line 4; the restatement is the same.

### 11 — Enter the amount from line 9
Status: **MATCH**

Model: IRS line 11 says to enter the amount from line 9; the restatement is the same.

### 12 — Subtract line 11 from line 10
Status: **MATCH**

Model: IRS line 12 is line 10 minus line 11; the restatement is the same.

### 13 — Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if married fili
Status: **MATCH**

Model: IRS line 13 uses $533,400 for single, $300,000 for MFS, $600,050 for MFJ or QSS, and $566,700 for HOH; the restatement matches.

### 14 — Enter the smaller of line 1 or line 13
Status: **MATCH**

Model: IRS line 14 is the smaller of line 1 or line 13; the restatement is the same.

### 15 — Add lines 5 and 9
Status: **MATCH**

Model: IRS line 15 is add lines 5 and 9; the restatement is the same.

### 16 — Subtract line 15 from line 14. If zero or less, enter -0-
Status: **MATCH**

Model: IRS line 16 is line 14 minus line 15 with a zero floor; the restatement is the same.

### 17 — Enter the smaller of line 12 or line 16
Status: **MATCH**

Model: IRS line 17 is the smaller of line 12 or line 16; the restatement is the same.

### 18 — Multiply line 17 by 15% (0.15)
Status: **MATCH**

Model: IRS line 18 multiplies line 17 by 15% (0.15); the restatement is the same.

### 19 — Add lines 9 and 17
Status: **MATCH**

Model: IRS line 19 is add lines 9 and 17; the restatement is the same.

### 20 — Subtract line 19 from line 10
Status: **MATCH**

Model: IRS line 20 is line 10 minus line 19; the restatement is the same.

### 21 — Multiply line 20 by 20% (0.20)
Status: **MATCH**

Model: IRS line 21 multiplies line 20 by 20% (0.20); the restatement is the same.

### 22 — Figure the tax on the amount on line 5. If the amount on line 5 is less than $100,000, use
Status: **MATCH**

Model: IRS line 22 figures tax on line 5, using the Tax Table below $100,000 and the Tax Computation Worksheet at $100,000 or more; the restatement uses the tax helper with amount line 5 and filing status.

### 23 — Add lines 18, 21, and 22
Status: **MATCH**

Model: IRS line 23 is add lines 18, 21, and 22; the restatement is the same.

### 24 — Figure the tax on the amount on line 1. If the amount on line 1 is less than $100,000, use
Status: **MATCH**

Model: IRS line 24 figures tax on line 1 under the same $100,000 Tax Table/Tax Computation Worksheet rule; the restatement uses the tax helper with amount line 1 and filing status.

### 25 — Tax on all taxable income. Enter the smaller of line 23 or line 24. Also include this amou
Status: **MATCH**

Model: IRS line 25 says to enter the smaller of line 23 or line 24; the restatement is the same.

## Raw response

```yaml
lines:
  - key: "1"
    status: MISMATCH
    reason: "IRS line 1 says to use Form 1040 line 15, but adds: 'However, if you are filing Form 2555 ... enter the amount from line 3 of the Foreign Earned Income Tax Worksheet.' The restatement always uses Form 1040 line 15 and has no Form 2555 refusal or alternate."
  - key: "2"
    status: MATCH
    reason: "IRS line 2 says to enter the Form 1040 or 1040-SR line 3a amount, and the restatement says to use f1040 line 3a."
  - key: "3"
    status: UNCLEAR
    reason: "The Schedule D 'Yes' branch matches, but for the 'No' branch IRS says 'Enter the amount from Form 1040 or 1040-SR, line 7a'; the provided text does not define line 7a, so the program's use of a 'Capital gain distributions, generally Form 1099-DIV box 2a' helper cannot be verified."
  - key: "4"
    status: MATCH
    reason: "IRS line 4 is 'Add lines 2 and 3'; the restatement adds line 2 and line 3."
  - key: "5"
    status: MATCH
    reason: "IRS line 5 is subtract line 4 from line 1 with a zero floor; the restatement is the same."
  - key: "6"
    status: MATCH
    reason: "IRS line 6 uses $48,350 for single or MFS, $96,700 for MFJ or QSS, and $64,750 for HOH; the restatement matches."
  - key: "7"
    status: MATCH
    reason: "IRS line 7 is the smaller of line 1 or line 6; the restatement is the same."
  - key: "8"
    status: MATCH
    reason: "IRS line 8 is the smaller of line 5 or line 7; the restatement is the same."
  - key: "9"
    status: MATCH
    reason: "IRS line 9 is line 7 minus line 8; the restatement is the same."
  - key: "10"
    status: MATCH
    reason: "IRS line 10 is the smaller of line 1 or line 4; the restatement is the same."
  - key: "11"
    status: MATCH
    reason: "IRS line 11 says to enter the amount from line 9; the restatement is the same."
  - key: "12"
    status: MATCH
    reason: "IRS line 12 is line 10 minus line 11; the restatement is the same."
  - key: "13"
    status: MATCH
    reason: "IRS line 13 uses $533,400 for single, $300,000 for MFS, $600,050 for MFJ or QSS, and $566,700 for HOH; the restatement matches."
  - key: "14"
    status: MATCH
    reason: "IRS line 14 is the smaller of line 1 or line 13; the restatement is the same."
  - key: "15"
    status: MATCH
    reason: "IRS line 15 is add lines 5 and 9; the restatement is the same."
  - key: "16"
    status: MATCH
    reason: "IRS line 16 is line 14 minus line 15 with a zero floor; the restatement is the same."
  - key: "17"
    status: MATCH
    reason: "IRS line 17 is the smaller of line 12 or line 16; the restatement is the same."
  - key: "18"
    status: MATCH
    reason: "IRS line 18 multiplies line 17 by 15% (0.15); the restatement is the same."
  - key: "19"
    status: MATCH
    reason: "IRS line 19 is add lines 9 and 17; the restatement is the same."
  - key: "20"
    status: MATCH
    reason: "IRS line 20 is line 10 minus line 19; the restatement is the same."
  - key: "21"
    status: MATCH
    reason: "IRS line 21 multiplies line 20 by 20% (0.20); the restatement is the same."
  - key: "22"
    status: MATCH
    reason: "IRS line 22 figures tax on line 5, using the Tax Table below $100,000 and the Tax Computation Worksheet at $100,000 or more; the restatement uses the tax helper with amount line 5 and filing status."
  - key: "23"
    status: MATCH
    reason: "IRS line 23 is add lines 18, 21, and 22; the restatement is the same."
  - key: "24"
    status: MATCH
    reason: "IRS line 24 figures tax on line 1 under the same $100,000 Tax Table/Tax Computation Worksheet rule; the restatement uses the tax helper with amount line 1 and filing status."
  - key: "25"
    status: MATCH
    reason: "IRS line 25 says to enter the smaller of line 23 or line 24; the restatement is the same."
```
