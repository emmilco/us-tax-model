# Render comparison — eic

The rendered English of every printed line of `Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a` (`rendered/2025/eic.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 2ee84c616f427fa245e260a8ee1947e35bbee2570f5aeca790e6dc3c3d4e9063 |
| lines judged | 11 |
| match / mismatch / unclear / missing | 11 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 40, 41, 42, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### (Step 5, 1) — Enter the amount from Form 1040 or 1040-SR, line 1z
Status: **MATCH**

Model: The IRS line reads "Enter the amount from Form 1040 or 1040-SR, line 1z." Clergy and church employees must reduce this amount and use Worksheet B. Those filers fall under the Schedule SE/Schedule C refusal, which names what is excluded.

### (Step 5, 2) — Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless chosen as ear
Status: **MATCH**

Model: The IRS line asks for "the Medicaid waiver payment amounts excluded from income on Schedule 1, line 8s". When there are no such payments, that amount is $0. Any Medicaid waiver payments trigger the other_income refusal, and an exclusion on Schedule 1, line 8s also triggers the schedule1 refusal, so $0 is right within the supported cases.

### (Step 5, 3) — Subtract line 2 from line 1
Status: **MATCH**

Model: The IRS line reads "Subtract line 2 from line 1."

### (Step 5, 4) — Nontaxable combat pay you elect to include in earned income; zero in this tool
Status: **MATCH**

Model: The IRS line reads "Enter all of your nontaxable combat pay if you elect to include it in earned income." The program enters $0 and refuses whenever there is any nontaxable combat pay, so $0 is right within the supported cases.

### (Step 5, 5) — Add lines 3 and 4. This is your earned income
Status: **MATCH**

Model: The IRS line reads "Add lines 3 and 4. This is your earned income."

### 1 — Enter your earned income from Step 5
Status: **MATCH**

Model: The IRS line reads "Enter your earned income from Step 5." That is Step 5, line 5.

### 2 — Look up the amount on line 1 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: The IRS line says to look up line 1 in the EIC Table, using "the correct column for your filing status and the number of qualifying children you have who have valid SSNs". The table starts at $1, so entering $0 below that is consistent. The table's married filing separately note sends those filers to the single/HOH column, which the per-filing-status lookup covers.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 11b
Status: **MATCH**

Model: The IRS line reads "Enter the amount from Form 1040 or 1040-SR, line 11b."

### 4 — Are the amounts on lines 3 and 1 the same?
Status: **MATCH**

Model: The IRS line asks "Are the amounts on lines 3 and 1 the same?" The program tests line 3 = line 1.

### 5 — Look up the amount on line 3 in the EIC Table to find the credit, using the column for you
Status: **MATCH**

Model: In the No case the IRS line says to "Look up the amount on line 3 in the EIC Table... correct column for your filing status and the number of qualifying children you have who have valid SSNs", and the program does this. In the Yes case the IRS says to leave line 5 blank. The program still computes a lookup there, but the line 6 helper uses line 2 and ignores line 5, so the credit is unchanged.

### 6 — This is your earned income credit
Status: **MATCH**

Model: If line 4 is Yes, the program enters line 2. Otherwise, if line 3 is below the line 5 threshold, it enters line 2; if not, it enters the smaller of lines 5 and 2. The thresholds are $10,620 ($17,730 if married filing jointly) with no qualifying children and $23,350 ($30,470) with one or more, which matches "Look at the amounts on lines 5 and 2. Then, enter the smaller amount on line 6."

## Raw response

```yaml
```yaml
lines:
  - key: "(Step 5, 1)"
    status: MATCH
    reason: "The IRS line reads \"Enter the amount from Form 1040 or 1040-SR, line 1z.\" Clergy and church employees must reduce this amount and use Worksheet B. Those filers fall under the Schedule SE/Schedule C refusal, which names what is excluded."
  - key: "(Step 5, 2)"
    status: MATCH
    reason: "The IRS line asks for \"the Medicaid waiver payment amounts excluded from income on Schedule 1, line 8s\". When there are no such payments, that amount is $0. Any Medicaid waiver payments trigger the other_income refusal, and an exclusion on Schedule 1, line 8s also triggers the schedule1 refusal, so $0 is right within the supported cases."
  - key: "(Step 5, 3)"
    status: MATCH
    reason: "The IRS line reads \"Subtract line 2 from line 1.\""
  - key: "(Step 5, 4)"
    status: MATCH
    reason: "The IRS line reads \"Enter all of your nontaxable combat pay if you elect to include it in earned income.\" The program enters $0 and refuses whenever there is any nontaxable combat pay, so $0 is right within the supported cases."
  - key: "(Step 5, 5)"
    status: MATCH
    reason: "The IRS line reads \"Add lines 3 and 4. This is your earned income.\""
  - key: "1"
    status: MATCH
    reason: "The IRS line reads \"Enter your earned income from Step 5.\" That is Step 5, line 5."
  - key: "2"
    status: MATCH
    reason: "The IRS line says to look up line 1 in the EIC Table, using \"the correct column for your filing status and the number of qualifying children you have who have valid SSNs\". The table starts at $1, so entering $0 below that is consistent. The table's married filing separately note sends those filers to the single/HOH column, which the per-filing-status lookup covers."
  - key: "3"
    status: MATCH
    reason: "The IRS line reads \"Enter the amount from Form 1040 or 1040-SR, line 11b.\""
  - key: "4"
    status: MATCH
    reason: "The IRS line asks \"Are the amounts on lines 3 and 1 the same?\" The program tests line 3 = line 1."
  - key: "5"
    status: MATCH
    reason: "In the No case the IRS line says to \"Look up the amount on line 3 in the EIC Table... correct column for your filing status and the number of qualifying children you have who have valid SSNs\", and the program does this. In the Yes case the IRS says to leave line 5 blank. The program still computes a lookup there, but the line 6 helper uses line 2 and ignores line 5, so the credit is unchanged."
  - key: "6"
    status: MATCH
    reason: "If line 4 is Yes, the program enters line 2. Otherwise, if line 3 is below the line 5 threshold, it enters line 2; if not, it enters the smaller of lines 5 and 2. The thresholds are $10,620 ($17,730 if married filing jointly) with no qualifying children and $23,350 ($30,470) with one or more, which matches \"Look at the amounts on lines 5 and 2. Then, enter the smaller amount on line 6.\""
```
```
