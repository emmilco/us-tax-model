# Render comparison — eic

The rendered English of every printed line of `Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` (`rendered/2025/eic.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | a617618aeaba56eb00e596d7f9a5415df71a067cb077fd0ced48ffa4f75a1284 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | bd8402b363f39c982f3f55589e95af2b506be6447d0843c3f84746f72b0864de |
| lines judged | 13 |
| match / mismatch / unclear / missing | 13 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **MATCH**

Model: IRS Step 5 worksheet line 1 is Form 1040 line 1z; the refusal excludes clergy, church employees, and statutory employees.

### (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless chosen as ear
Status: **MATCH**

Model: IRS line 2 is the Medicaid waiver payment amount excluded from income; the program uses zero when no such payments are supported and refuses Medicaid waiver cases.

### (Step 5, 3) — Subtract line 2 from line 1
Status: **MATCH**

Model: IRS line 3 says subtract line 2 from line 1.

### (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MATCH**

Model: IRS line 4 is nontaxable combat pay only if elected; the program uses zero when no combat pay is supported and refuses combat pay cases.

### (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MATCH**

Model: IRS line 5 says add lines 3 and 4 to get earned income.

### 4b — Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned income
Status: **MATCH**

Model: Worksheet B line 4b combines lines 1e, 2c, 3, and 4a; statutory employee line 3 is excluded by the Step 5 refusal, so adding Step 5 line 5 and lines 1e/2c is correct for supported cases.

### 6 (eic.wsb_6) — Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero if line 4b 
Status: **MATCH**

Model: Worksheet B line 6 enters total earned income from line 4b; subtracting zero and flooring at zero matches the zero-or-less stop for supported cases.

### 1 — Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line 6
Status: **MATCH**

Model: Worksheet A line 1 is earned income from Step 5; when Step 5 question 2 is Yes, the program correctly switches to Worksheet B line 6.

### 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: IRS Worksheet A line 2 looks up line 1 in the EIC Table in the correct column for filing status and number of qualifying children with valid SSNs.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **MATCH**

Model: IRS Worksheet A line 3 is Form 1040 line 11b.

### 4 — Are the amounts on lines 3 and 1 the same?
Status: **MATCH**

Model: IRS Worksheet A line 4 asks whether the amounts on lines 3 and 1 are the same.

### 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: IRS line 5 uses the threshold test and, when not blank, the EIC Table credit for line 3; the threshold blank case is handled by eic.line5_blank and eic.after_line4.

### 6 (eic.line6) — This is your earned income credit
Status: **MATCH**

Model: IRS line 6 is line 2 when line 4 is Yes, and otherwise line 2 if line 5 is blank or the smaller of lines 5 and 2.

## Raw response

```yaml
lines:
  - key: "(Step 5, 1)"
    status: MATCH
    reason: "IRS Step 5 worksheet line 1 is Form 1040 line 1z; the refusal excludes clergy, church employees, and statutory employees."
  - key: "(Step 5, 2)"
    status: MATCH
    reason: "IRS line 2 is the Medicaid waiver payment amount excluded from income; the program uses zero when no such payments are supported and refuses Medicaid waiver cases."
  - key: "(Step 5, 3)"
    status: MATCH
    reason: "IRS line 3 says subtract line 2 from line 1."
  - key: "(Step 5, 4)"
    status: MATCH
    reason: "IRS line 4 is nontaxable combat pay only if elected; the program uses zero when no combat pay is supported and refuses combat pay cases."
  - key: "(Step 5, 5)"
    status: MATCH
    reason: "IRS line 5 says add lines 3 and 4 to get earned income."
  - key: "4b"
    status: MATCH
    reason: "Worksheet B line 4b combines lines 1e, 2c, 3, and 4a; statutory employee line 3 is excluded by the Step 5 refusal, so adding Step 5 line 5 and lines 1e/2c is correct for supported cases."
  - key: "6 (eic.wsb_6)"
    status: MATCH
    reason: "Worksheet B line 6 enters total earned income from line 4b; subtracting zero and flooring at zero matches the zero-or-less stop for supported cases."
  - key: "1"
    status: MATCH
    reason: "Worksheet A line 1 is earned income from Step 5; when Step 5 question 2 is Yes, the program correctly switches to Worksheet B line 6."
  - key: "2"
    status: MATCH
    reason: "IRS Worksheet A line 2 looks up line 1 in the EIC Table in the correct column for filing status and number of qualifying children with valid SSNs."
  - key: "3"
    status: MATCH
    reason: "IRS Worksheet A line 3 is Form 1040 line 11b."
  - key: "4"
    status: MATCH
    reason: "IRS Worksheet A line 4 asks whether the amounts on lines 3 and 1 are the same."
  - key: "5"
    status: MATCH
    reason: "IRS line 5 uses the threshold test and, when not blank, the EIC Table credit for line 3; the threshold blank case is handled by eic.line5_blank and eic.after_line4."
  - key: "6 (eic.line6)"
    status: MATCH
    reason: "IRS line 6 is line 2 when line 4 is Yes, and otherwise line 2 if line 5 is blank or the smaller of lines 5 and 2."
```
