> **Status: draft for the owner (2026-10-22).** Written by a read-only research agent from the archived
> sources in `sources/2025/`, before the stage it maps; its decision batch is a draft and nothing in it is
> decided. Every claim carries a locator and is testimony until checked again at authoring. Spot-checked by the integrating session: the Form 8863 Credit Limit Worksheet line 5 subtracts Schedule 3 lines 1, 2, 6d and 6l (i8863), and the 4.5% share against the coverage report.
> **Verified after Stage 15:** see `stage19-education-credits.verification.md` (2 errors, 7 items out of date), which supersedes this map where they differ.

# Stage 19 premise map: the education credits (Form 8863)

Read-only research for spec 2.4 roadmap item 5, coverage category `education` (gate `scope.credits`). Written against the tree at 6051ec0 (Stage 15 groundwork), with Stage 15 (Forms 8880, 2441, 5695 and Schedule 3 lines 2, 4, 5a, 5b) assumed to land first. I did not read the Stage 15 worktrees, so every Stage 15 line id below is a placeholder (marked "Stage 15 id") and has to be matched to the integrated encoding. Stages 16 to 18 (Schedule 1 remainder, Schedule E, the premium tax credit) also come before this one; where this stage depends on one of them, the dependency is named.

Locators are `doc p. N, heading, "quote"`. Page N is the N-th form-feed chunk of `sources/2025/<doc>.cols.txt`; for f8863, i8863, p970, i1098et and i1040s8812 the chunk number matches the printed page number (checked on the page footers). Text in double quotes is verbatim archived text. Proposed interview wording and YAML ids are in single quotes or backticks and are not source text.

## 1. Scope

### 1.1 What the stage retires

| Coverage category | Gate(s) now | Share of returns | IRS returns (2023) | Basis |
|---|---|---|---|---|
| `education` (Education credits) | `scope.credits` | 4.5% | 7,211,349 | IRS count, overlap from microdata |

Source: `reports/2025/filer_coverage.md`, table 'Refused situations', and `reports/2025/filer_coverage.json` (`share` 0.04490196447608361). The roadmap table in the same report puts the group at step 5: 'Education credits (Form 8863) | 88.9% (+4.1) | +2.7'.

How the count is built (`tools/coverage/categories.json`, category `education`): `combine: max` of two cells of `soi-23in33ar`, column 8 'Nonrefundable education credit' and column 40 'American opportunity credit'. I read both cells from the archived workbook with the engines interpreter: column 8 (number of returns) is 7,211,349 and column 40 (refundable American opportunity credit, number of returns) is 5,821,688; the amounts are 7,554,668 and 5,090,364 (thousands of dollars). The max is a lower bound on the union: returns with only a refundable credit (no tax to offset) are not in column 8. Caveat: the column 40 header the script builds reads 'Tax credits Total refundable credits American opportunity credit Mortgage interest credit Number of returns' (forward-filled header cells); the estimator accepts it because it contains 'American opportunity credit', but I did not check the workbook's merged cells by eye.

Microdata: `microdata_share_before_raking: 0.005307730052777667` against an IRS share of 4.49%. PolicyEngine flags (`american_opportunity_credit`, `lifetime_learning_credit`) only about an eighth of the IRS share (0.53% against 4.49%) before raking, so the overlap of education with the other categories rests on a thin sample. The +4.1 / +2.7 figures are an ordering, not a measurement (spec 2.4 says as much).

Already-refused neighbours that stay refused and are not this stage's to retire:

- Recapture of an education credit: `scope.other_line16` ("recapture of an education credit") refuses it on `f1040.line16`. i1040gi p. 34, "Recapture of an education credit. You may owe this tax if you claimed an education credit in an earlier year".
- Married filing separately: `s3.mfs` in `scope.ready`.
- Nonresident alien status: `scope.other_income` ('Any nonresident alien status (you or your spouse, for any part of 2025)').
- Form 2555, Form 4563, excluded Puerto Rico income: `sa.excluded_income`.

After the stage, `education` in `categories.json` becomes retired the way `schedule_c` is (`"refused": false`, `"gates": []`); its residual refusals (section 6) become unmeasured gates.

### 1.2 Recommended scope

Include now:

- Form 8863 Parts I, II and III in full, for every student the return may claim: you, your spouse on a joint return, and each dependent you claim.
- The Adjusted Qualified Education Expenses Worksheet (i8863 p. 9) per student, with tax-free educational assistance received in 2025 and in 2026 before filing, and refunds.
- The refundable 40% and the line 7 conditions that deny it (i8863 pp. 6 to 7).
- The MAGI phase-outs (lines 2 to 7 and 13 to 18), with the existing `prorate` atom at three places.
- The Credit Limit Worksheet (i8863 p. 8) and Schedule 3 line 3, in the Stage 15 credit order.
- Form 1040 line 29.
- The edits to every Stage 15 and existing worksheet that subtracts Schedule 3 line 3.

Leave refused (section 6 has the reasons): MAGI with excluded foreign or territory income (existing gate), a Form 8862 requirement or an AOC ban, recapture (existing gate), an academic period whose tax-free assistance exceeds its expenses (if the owner takes the aggregate encoding), and the filer's own taxable scholarship not on Form W-2 unless Stage 16 computes Schedule 1 line 8r.

Reasoning. The form is small (31 lines, about 15 arithmetic), every phase-out and rate is a parameter, and the only atom it needs that a `choose` cannot give (the decimal at lines 6 and 17) already exists as `prorate`. The cost is in the inputs: per-student eligibility questions, expenses split by credit, and assistance. The rare and hard parts (recapture, Form 8862, excluded income, 529 taxability) are already behind existing gates or are a single screen. Splitting the stage (LLC first, AOC later) saves little: the AOC is the larger share (5.8 million returns with a refundable part) and its extra cost is lines 23 to 30 and the line 7 test.

## 2. Sources

Archived and used (all in `sources/2025/`, revision "2025" in `manifest.json`):

| Id | Document | Used for |
|---|---|---|
| f8863 | Form 8863 (2025), "Created 9/23/25" (f8863 p. 1) | the line map |
| i8863 | Instructions for Form 8863 (2025), "Sep 16, 2025" (i8863 p. 1) | rules, worksheets, line 7 |
| p970 | Pub. 970 (2025) | chapters 1 to 3, MAGI worksheets, examples |
| i1098et | Instructions for Forms 1098-E and 1098-T (2025), dated "Nov 7, 2024" (i1098et p. 1) | Form 1098-T boxes |
| i1040gi | Form 1040 instructions | line 29 (p. 61), Schedule 1 line 8r (p. 92), Schedule 3 line 3 (p. 115) |
| f1040s3 | Schedule 3 (2025) | line 3 |
| f1040 | Form 1040 (2025) | line 29 |
| i1040s8812 | Schedule 8812 instructions | Credit Limit Worksheet A (p. 4) |
| i5695 | Form 5695 instructions | the two credit limit worksheets that subtract line 3 (pp. 5, 7) |
| p501 | Pub. 501 | the age rule (Q3) |
| plaw-119-21 | Public Law 119-21 | sec. 70606, the 2026 SSN rule (not a 2025 change) |
| soi-23in33ar | SOI table 3.3 | the coverage counts above |

Not archived:

- Form 1098-T (2025) itself. The boxes are described in i1098et p. 4; the form would confirm box captions for interview help. URL: https://www.irs.gov/pub/irs-prior/f1098t--2025.pdf (the current revision is https://www.irs.gov/pub/irs-pdf/f1098t.pdf). Not needed if the owner takes D5 (1098-T is not an input collection).
- Form 8862 and its instructions, https://www.irs.gov/pub/irs-pdf/f8862.pdf and https://www.irs.gov/pub/irs-pdf/i8862.pdf. Needed only if the Form 8862 case is computed; the recommendation is to refuse it.
- Instructions for Form 1099-Q, https://www.irs.gov/pub/irs-pdf/i1099q.pdf. Needed only if 529 or Coverdell distributions are modelled; the recommendation is help text only.
- Pub. 519, https://www.irs.gov/pub/irs-pdf/p519.pdf (nonresident aliens). Not needed: that status is refused.
- 26 U.S.C. 25A. The project formalizes IRS procedure, not the statute; listed only because two readings below (Q2, Q6) would be settled by it.

## 3. Line map

Conventions. 'Return' = a return-level line in a new `f8863` form. 'Student' = a line per student (where it lives is decision D2; this map writes `stu.*`). New inputs are listed with the collection they belong on.

### 3.1 Part I, refundable American opportunity credit (f8863 p. 1)

| Line | Printed text | Computes | Existing supply | New inputs / notes |
|---|---|---|---|---|
| 1 | "After completing Part III for each student, enter the total of all amounts from all Parts III, line 30" | sum of `stu.line30` over students | none | `sum_over` (two of them if D2 = option B: one over `person`, one over `dependent`, added) |
| 2 | f8863 p. 1: "Enter $180,000 if married filing jointly; or $90,000 if single, head of household, or qualifying surviving spouse" | param by status | `f1040.status` | param `edu.magi_limit`; MFS is not printed (refused project-wide) |
| 3 | f8863 p. 1: "Enter the amount from Form 1040 or 1040-SR, line 11b. But if you’re filing Form 2555 or 4563, or you’re excluding income from Puerto Rico, see Pub. 970 for the amount to enter instead" | copy | `f1040.line11b` | refuse on `sa.excluded_income` (p970 p. 20, Worksheet 2-1) |
| 4 | "Subtract line 3 from line 2. If zero or less, stop; you can’t take any education credit" | `subtract_floor0` | | the stop is a zero that zeroes lines 6 to 8 and, through lines 13 to 15, Part II |
| 5 | "Enter $20,000 if married filing jointly; or $10,000 if single, head of household, or qualifying surviving spouse" | param by status | | param `edu.phaseout_range` |
| 6 | "If line 4 is: • Equal to or more than line 5, enter 1.000 on line 6; or • Less than line 5, divide line 4 by line 5. Enter the result as a decimal (rounded to at least three places)." | the decimal | | not a separate line: `prorate` folds lines 6 and 7, as `sli.line8_figured` folds sli lines 7 and 8 |
| 7 | "Multiply line 1 by line 6." | `prorate(amount line1, part line4, whole line5, places 3)` | | three places: new register entry like `amb.2025.sli_ratio_places` |
| 7 box | "Caution: If you were under age 24 at the end of the year and meet the conditions described in the instructions, you can’t take the refundable American opportunity credit; skip line 8, enter the amount from line 7 on line 9, and check this box" | Bool, shown | | `f8863.no_refund` from the line 7 test (section 4.6) |
| 8 | f8863 p. 1: "Refundable American opportunity credit. Multiply line 7 by 40% (0.40). Enter the amount here and on Form 1040 or 1040-SR, line 29. Then go to line 9 below." | `choose`: box checked → 0; else `multiply_rate(line7, 40%)` | | param `aoc.refundable_rate`; to `f1040.line29` |

### 3.2 Part II, nonrefundable education credits (f8863 p. 1)

| Line | Printed text | Computes | Existing supply | New inputs / notes |
|---|---|---|---|---|
| 9 | "Subtract line 8 from line 7. Enter here and on line 2 of the Credit Limit Worksheet. See instructions" | `subtract` (never negative: line 8 ≤ line 7) | | |
| 10 | "After completing Part III for each student, enter the total of all amounts from all Parts III, line 31. If zero, skip lines 11 through 17, enter -0- on line 18, and go to line 19" | sum of `stu.line31` | | the skip is automatic (zero through lines 11, 12, 18) |
| 11 | f8863 p. 1: "Enter the smaller of line 10 or $10,000" | `smaller_of` | | param `llc.expense_cap`; the cap is per return (i8863 p. 4, "up to a maximum of $10,000 of adjusted qualified education expenses per return") |
| 12 | "Multiply line 11 by 20% (0.20)" | `multiply_rate` | | param `llc.rate` |
| 13 | "Enter $180,000 if married filing jointly; or $90,000 if single, head of household, or qualifying surviving spouse" | as line 2 | | same param; printed twice, encode twice |
| 14 | f8863 p. 1: "Enter the amount from Form 1040 or 1040-SR, line 11b." | copy | `f1040.line11b` | same refusal as line 3 |
| 15 | "Subtract line 14 from line 13. If zero or less, skip lines 16 and 17, enter -0- on line 18, and go to line 19" | `subtract_floor0` | | |
| 16 | "Enter $20,000 if married filing jointly; or $10,000 if single, head of household, or qualifying surviving spouse" | as line 5 | | |
| 17 | "If line 15 is: • Equal to or more than line 16, enter 1.000 on line 17 and go to line 18; or • Less than line 16, divide line 15 by line 16." | folded into line 18 | | as line 6 |
| 18 | "Multiply line 12 by line 17. Enter here and on line 1 of the Credit Limit Worksheet. See instructions" | `prorate(line12, line15, line16, 3)` | | |
| 19 | "Nonrefundable education credits. Enter the amount from line 7 of the Credit Limit Worksheet (see instructions) here and on Schedule 3 (Form 1040), line 3" | copy of CLW line 7 | | to new `s3.line3` |

### 3.3 Credit Limit Worksheet (i8863 p. 8, Line 19, "Complete this worksheet to figure the amount to enter on line 19.")

| Line | Printed text (i8863 p. 8) | Computes | Supply |
|---|---|---|---|
| 1 | i8863 p. 8: "Enter the amount from Form 8863, line 18" | copy | `f8863.line18` |
| 2 | i8863 p. 8: "Enter the amount from Form 8863, line 9" | copy | `f8863.line9` |
| 3 | "Add lines 1 and 2" | sum | |
| 4 | i8863 p. 8: "Enter the amount from Form 1040 or 1040-SR, line 18" | copy | `f1040.line18` |
| 5 | "Enter the total of your credits from Schedule 3 (Form 1040), lines 1, 2, 6d, and 6l" | sum | `s3.line1`, the Stage 15 `s3.line2`; 6d and 6l stay refused under the narrowed `scope.credits` (Stage 15 keeps elderly or disabled and Form 8978 refused, T-048) |
| 6 | "Subtract line 5 from line 4" | `subtract` as printed, or `subtract_floor0` (Q4, D10) | |
| 7 | "Enter the smaller of line 3 or line 6 here and on Form 8863, line 19" | `smaller_of` | |

The nonrefundable AOC (line 9) and the LLC (line 18) share one tax limit; nothing in the text orders them against each other, and the worksheet adds them before limiting.

### 3.4 Part III, per student (f8863 p. 2)

Caution, f8863 p. 2: "Complete Part III for each student for whom you’re claiming either the American opportunity credit or lifetime learning credit."

| Line | Printed text (f8863 p. 2) | Computes | Existing supply | New inputs |
|---|---|---|---|---|
| 20 | "Student name (as shown on page 1 of your tax return)" | identity, no arithmetic | the person or dependent entry | none (no strings in the data model; the values sheet names the entry) |
| 21 | "Student social security number (as shown on page 1 of your tax return)" | identity | | none; the TIN condition is a Bool (4.5) |
| 22a/b (1) | "Address. Number and street (or P.O. box). City, town or post office, state, and ZIP code." | identity | | none |
| 22(2) | "Did the student receive Form 1098-T from this institution for 2025?" | Bool per institution, shown | | per student, D5 |
| 22(3) | f8863 p. 2: "Did the student receive Form 1098-T ... from this institution for 2024 with box 7 checked?" (two-column layout interleaves Yes/No) | Bool per institution, shown | | per student; informational (no arithmetic reads it) |
| 22(4) | "Enter the institution’s employer identification number (EIN) if you’re claiming the American opportunity credit or if you checked “Yes” in (2) or (3)." | identity | | Bool 'EIN available' for AOC (D6) |
| 23 | "Has the American opportunity credit been claimed for this student for any 4 prior tax years?" | Bool input; Yes → line 31 | | `stu.aoc_four_years` |
| 24 | f8863 p. 2: "Was the student enrolled at least half-time for at least one academic period that began or is treated as having begun in 2025 at an eligible educational institution in a program leading toward a postsecondary degree, certificate, or other recognized postsecondary educational credential?" | Bool input; No → line 31 | | `stu.half_time` (help: 1098-T box 8, i1098et p. 4) |
| 25 | "Did the student complete the first 4 years of postsecondary education before 2025?" | Bool input; Yes → line 31 | | `stu.four_years_done` (help: 1098-T box 9 is a hint, not the test) |
| 26 | "Was the student convicted, before the end of 2025, of a felony for possession or distribution of a controlled substance?" | Bool input; Yes → line 31 | | `stu.felony_drug` |
| 27 | "Adjusted qualified education expenses (see instructions). Don’t enter more than $4,000" | `smaller_of(stu.aqee_aoc, param 4,000)` | | param `aoc.expense_cap` |
| 28 | "Subtract $2,000 from line 27. If zero or less, enter -0-" | `subtract_floor0` | | param `aoc.full_band` |
| 29 | "Multiply line 28 by 25% (0.25)" | `multiply_rate` | | param `aoc.second_rate` |
| 30 | "If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29 and enter the result." | `choose` on line 28 = 0: line 27; else sum(line 29, helper param 2,000) | | AOC student only (guard below) |
| 31 | "Adjusted qualified education expenses (see instructions). Include the total of all amounts from all Parts III, line 31, on Part II, line 10" | AQEE for an LLC student, else 0 | | |

Form caution between 26 and 27 (f8863 p. 2): "You can’t take the American opportunity credit and the lifetime learning credit for the same student in the same year. If you complete lines 27 through 30 for this student, don’t complete line 31."

Proposed per-student routing lines (not printed):

- `stu.claimable`: the student may be claimed at all (you or your spouse, or a dependent with `dependent.claimed`), with TIN and 1098-T conditions (4.5).
- `stu.aoc`: `stu.claimable` and not line 23 and line 24 and not line 25 and not line 26, and the AOC-only conditions (EIN, filer TIN; D6).
- line 30 = `choose(stu.aoc → printed formula; else 0)`; line 31 = `choose(stu.claimable and not stu.aoc → stu.aqee_llc; else 0)`.

### 3.5 Adjusted Qualified Education Expenses Worksheet (i8863 p. 9)

i8863 p. 9: "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025."

| Line | Printed text (i8863 p. 9) | Computes | New inputs |
|---|---|---|---|
| 1 | "Total qualified education expenses paid for or on behalf of the student in 2025 for the academic period" | input(s) | split by credit (D4): `stu.qee_institution` (tuition, required fees, and books, supplies and equipment required to be paid to the institution) and `stu.qee_materials` (other course materials needed for a course of study; AOC only) |
| 2a | "Tax-free educational assistance received in 2025 allocable to the academic period" | input | `stu.assist_2025` |
| 2b | "Tax-free educational assistance received in 2026 (and before you file your 2025 tax return) allocable to the academic period" | input | `stu.assist_2026` |
| 2c | "Refunds of qualified education expenses paid in 2025 if the refund is received in 2025 or in 2026 before you file your 2025 tax return" | input | `stu.refunds` |
| 3 | "Total adjustments (add lines 2a, 2b, and 2c)" | sum | |
| 4 | "Adjusted qualified education expenses. Subtract line 3 from line 1. If zero or less, enter -0-" | `subtract_floor0` | two versions: `stu.aqee_aoc` (line 1 = institution + materials) and `stu.aqee_llc` (line 1 = institution only) |

Per academic period or per student: see D3 and Q1. Summing the periods before the floor gives a larger result than flooring each period when one period's assistance exceeds its own expenses.

### 3.6 Form 1098-T as an input (i1098et p. 4, p970 p. 19)

The amounts on Form 8863 are what was paid, not what the 1098-T reports: i8863 p. 4, "the amount in box 1 of Form 1098-T may be different from the amount you paid (or are treated as having paid). In completing Form 8863, use only the amounts you actually paid (plus any amounts you’re treated as having paid) in 2025". So the boxes serve as interview help and as screens, not as line values.

| Box | i1098et p. 4 text | Use in this stage |
|---|---|---|
| 1 | "Enter the total amount of payments received for qualified tuition and related expenses from all sources during the calendar year." | help for `stu.qee_institution`; not the value |
| 4 | "Enter reimbursements or refunds of qualified tuition and related expenses made in 2025 that relate to payments received that were reported for any prior year after 2002." | a prior-year refund can mean recapture: help pointing to `scope.other_line16` |
| 5 | i1098et p. 4: "Enter the total amount of any scholarships or grants that you administered and processed during the calendar year for the payment of the student’s costs of attendance." | help for `stu.assist_2025` (only its tax-free part reduces expenses, p970 p. 14) |
| 6 | "Enter the amount of any reduction to the amount of scholarships or grants that were reported for any prior year after 2002." | help only (a prior-year matter) |
| 7 | "Check this box if any payments received for qualified tuition and related expenses reported for 2025 relate to an academic period that begins in January through March of 2026." | help for line 24 (the treated-as-begun rule) and line 22(3) |
| 8 | "Check this box if the student was at least a half-time student during any academic period that began in 2025." | help for line 24 |
| 9 | "Check this box if the student was a graduate student." | help for line 25 |

## 4. Rules

### 4.1 Who cannot claim (return level)

i8863 p. 3, Who cannot claim a credit: "You cannot claim an education credit on a 2025 tax return if any of the following apply. 1. You’re claimed as a dependent on another person’s tax return, such as your parent’s return. 2. Your filing status is married filing separately. 3. You (or your spouse) were a nonresident alien for any part of 2025 and didn’t elect to be treated as a resident alien for tax purposes. 4. Your MAGI is $180,000 or more if married filing jointly; or $90,000 or more if single, head of household, or qualifying surviving spouse with dependent child. 5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)."

i1040gi p. 115, Line 3, Education Credits, "You, or your spouse if filing jointly, are claimed as a dependent on someone else’s (such as your parent’s) 2025 tax return." That wording matches the existing `sli.claimed` input (its label: Are you, or your spouse if filing jointly, claimed as a dependent on someone else's (such as your parent's) 2025 tax return?; `forms/2025/sli.yaml`), which `sli.eligible` reads to zero the student loan interest deduction. Recommendation: reuse `sli.claimed` and zero both credits when it is true (the pattern of `sli.allowed`).

Item 2 is already refused (`s3.mfs`); item 3 is refused (`scope.other_income`); item 4 is the line 4 / line 15 stop.

### 4.2 Who the student can be

p970 p. 10, Who Can Claim the Credit?: "The eligible student is either yourself, your spouse, or a dependent you claim on your tax return." i8863 p. 2, Who can claim a dependent’s expenses: "If a student is claimed as a dependent on another person’s tax return, all qualified education expenses of the student are treated as having been paid by that person. Therefore, only that person can claim an education credit for the student."

p970 p. 19 (table): a dependent you do not claim "(even if entitled to claim the dependent)" means "the dependent can claim the American opportunity credit. You can’t claim the credit based on this dependent’s expenses." In the project a dependent entry is claimed when `dependent.claimed` is true; a listed person who fails the tests cannot be a student of this return.

Expenses paid by others: p970 p. 19, Expenses paid by others, "If you claim the student as a dependent on your tax return, you are considered to have paid the expenses." Help text only; the input is the amount paid by anyone for the student.

### 4.3 AOC student requirements

i8863 p. 3, Student qualifications: "Generally, you can claim the American opportunity credit for a student on a 2025 tax return only if all of the following seven requirements are met." The seven:

1. i8863 p. 3: "As of the beginning of 2025, the student had not completed the first 4 years of postsecondary education (generally, the freshman through senior years of college), as determined by the eligible educational institution." (line 25; i8863 p. 8 Line 25 adds "Disregard any academic credit awarded solely on the basis of the student’s performance on proficiency examinations.")
2. i8863 p. 3: "The American opportunity credit has not been claimed (by you or anyone else) for this student for any 4 tax years before 2025." (line 23; Examples 1 and 2, Sharon and Wilbert, are official examples for line 23)
3. i8863 p. 3: "For at least one academic period beginning or treated as beginning (see next) in 2025, the student both: a. Was enrolled in a program that leads to a degree, certificate, or other recognized educational credential; and b. Carried at least one-half the normal full-time workload for his or her course of study." (line 24) The treated-as-begun rule: "For 2025, you must treat an academic period beginning in the first 3 months of 2026 as if it began in 2025 if qualified education expenses for the student were paid in 2025 for that academic period."
4. i8863 p. 3: "As of the end of 2025, the student had not been convicted of a federal or state felony for possessing or distributing a controlled substance." (line 26)
5. i8863 p. 3: "Filers and students must have been issued a TIN by the due date of their 2025 return (including extensions)."
6. i8863 p. 4: "The student received Form 1098-T from the educational institution for 2025 or you followed the procedures under Form 1098-T requirement, earlier."
7. i8863 p. 4: "You must provide the educational institution’s employer identification number (EIN) on your Form 8863."

Failing a requirement: i8863 p. 4, Tip, "If the requirements above aren’t met for any student, you cannot claim the American opportunity credit for that student. You may be able to claim the lifetime learning credit for part or all of that student’s qualified education expenses instead if certain requirements are met."

Only 1 to 4 are Part III questions. 5 to 7 have no line; how they route is D6.

ITIN or ATIN applied for: p970 p. 11, Who Can’t Claim the Credit?, "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as ... on or before the due date of the return." The existing `person.tin` and `person.itin_applied` and `dependent.tin` (label 'SSN, ITIN or ATIN issued on or before the due date of your return?') cover this.

Ban and Form 8862: i8863 p. 3, "Don’t claim the American opportunity credit for 2 years after there was a final determination that your claim was due to reckless or intentional disregard of the rules or 10 years after there was a final determination that your claim was due to fraud." i1040gi p. 61, Line 29, "You must file Form 8862 to claim the American opportunity credit if your American opportunity credit for a year after 2015 was denied or reduced for any reason other than a math or clerical error." Exception, same place: "Don’t file Form 8862 if you filed Form 8862 for 2024 and the American opportunity credit was allowed for that year."

Felony drug conviction, LLC: p970 p. 22, Table 3-1, "Felony drug convictions don’t make the student ineligible" (the same row of i8863 p. 2, Table 1, is interleaved in the extraction).

### 4.4 Choice between the credits

p970 p. 9, "For each student, you can elect for any year only one of the credits." i8863 p. 3, Tip: "If you can choose between using a student’s adjusted qualified education expenses for the American opportunity credit or the lifetime learning credit, the American opportunity credit will always be greater than the lifetime learning credit." The form's flow sends a student who passes lines 23 to 26 to lines 27 to 30 ("No—Complete lines 27 through 30 for this student", f8863 p. 2).

Inference (checked by arithmetic, not by the text): per student, AOC = min(x, 2,000) + 25% of min(max(x − 2,000, 0), 2,000) and LLC ≤ 20% of x; AOC ≥ LLC for every x ≥ 0, both are scaled by the same phase-out decimal, and the LLC's $10,000 cap is shared across students, so moving an AOC student to the LLC never raises the current-year credit. The only reason to elect the LLC is to save one of the four AOC years. Recommendation: follow the form's flow, no election input (Q6).

### 4.5 Conditions shared by both credits

TIN of the student: i8863 p. 3, item 5 above (both credits; Table 1 on i8863 p. 2 also says, for the LLC, "Students must have been issued a TIN by the due date of their 2025 return (including extensions)").

Form 1098-T: i8863 p. 1, Form 1098-T requirement, "To be eligible to claim the American opportunity credit or the lifetime learning credit, the law requires a taxpayer (or a dependent) to have received Form 1098-T, Tuition Statement, from an eligible educational institution, whether domestic or foreign." Exceptions on the same page: the institution "isn’t required to furnish a Form 1098-T to the student under existing rules (for example, if the student is a qualified nonresident alien, has certain qualified education expenses paid entirely with scholarships, has certain qualified education expenses paid under a formal billing arrangement, or is enrolled only in courses for which no academic credit is awarded)", or the student requested it "After January 31, 2026, but before you file the return". (p970 p. 2 gives the date as "After February 2, 2026 (January 31 falls on a Saturday)"; the two archived documents differ by two days. Help text should cite p970, the later revision; Q11.)

No double benefit: p970 p. 13, No Double Benefit Allowed, "Deduct higher education expenses on your income tax return (as, for example, a business expense) and also claim an American opportunity credit based on those same expenses." and "Figure the tax-free portion of a distribution from a ... education savings account (ESA) or qualified tuition program (QTP) using the same expenses you used to figure the American opportunity credit." i8863 p. 4: "If you or the student takes a deduction for higher education expenses, such as on Schedule C (Form 1040), you cannot use those same expenses in your qualified education expenses when figuring your education credits."

### 4.6 Line 7: when the 40% is not refundable

i8863 p. 7: "You don’t qualify for a refundable American opportunity credit if 1 (a, b, or c), 2, and 3 below apply to you. 1. You were: a. Under age 18 at the end of 2025, or b. Age 18 at the end of 2025 and your earned income (defined later) was less than one-half of your support (defined later), or c. Over age 18 and under age 24 at the end of 2025 and a full-time student (defined later) and your earned income (defined later) was less than one-half of your support (defined later). 2. At least one of your parents was alive at the end of 2025. 3. You’re not filing a joint return for 2025."

p970 p. 20 states item 3 as "You are filing a return as single, head of household, qualifying surviving spouse, or married filing separately for 2025." Same set of statuses.

Definitions (i8863 p. 7): "Earned income includes wages, salaries, professional fees, and other payments received for personal services actually performed." It includes "the part of any scholarship or fellowship grant that represents payment for teaching, research, or other services performed by the student", and for a sole proprietor or partner "a reasonable allowance for compensation for personal services, but not more than 30% of your share of the net profits". This is not the EIC's earned income; recommend a Bool input for the comparison, not a computation. "Support includes food, shelter, clothing, medical and dental care, education, and the like." "a scholarship received by you isn’t considered support if you were a full-time student". "Full-time student. Solely for purposes of determining whether a scholarship is considered support, you were a full-time student for 2025 if during any part of any 5 calendar months during the year you were enrolled as a full-time student at an eligible educational institution". (The heading says "solely for purposes of ... support", but item 1c also uses "full-time student (defined later)"; Q5.)

i8863 p. 7 also gives the seven-question flow, which the encoding can follow: "1. Were you under age 24 at the end of 2025? If no, stop here; you do qualify to claim part of the allowable American opportunity credit as a refundable credit."

Encoding: on a joint return the test is false without asking. Otherwise new return-level inputs, reached only when `f8863.line7` > 0 and the status is not MFJ: age at the end of 2025 (Count, like `dependent.age`), full-time student, earned income less than half of support, a parent alive.

### 4.7 Qualified education expenses

i8863 p. 4, Qualified Education Expenses: "Generally, qualified education expenses are amounts paid in 2025 for tuition and fees required for the student’s enrollment or attendance at an eligible educational institution." Course materials differ by credit:

- AOC: "Qualified education expenses include amounts paid for tuition, fees, and course materials, which include books, supplies, and equipment needed for a course of study, whether or not the materials are purchased from the educational institution as a condition of enrollment or attendance."
- LLC: "Qualified education expenses include amounts paid for books, supplies, and equipment only if required to be paid to the institution as a condition of enrollment or attendance."

Never qualified (i8863 p. 4): "Personal expenses. This means room and board, insurance, medical expenses (including student health fees), transportation, and other similar personal, living, or family expenses." Sports, games, hobbies or noncredit courses only if part of the degree program "or (for the lifetime learning credit only) helps the student acquire or improve job skills."

Timing (i8863 p. 4, Prepaid Expenses): "Qualified education expenses paid in 2025 for an academic period that begins in the first 3 months of 2026 can be used in figuring an education credit for 2025 only." and "Caution: You cannot use any amount you paid in 2024 or 2026 to figure the qualified education expenses you use to figure your 2025 education credit(s)."

Loans: p970 p. 12, "You can claim an American opportunity credit for qualified education expenses paid with the proceeds of a loan."

### 4.8 Adjustments: tax-free assistance, scholarships, refunds

i8863 p. 4, Tax-free educational assistance: "For tax-free educational assistance received in 2025, reduce the qualified education expenses for each academic period by the amount of tax-free educational assistance allocable to that academic period." It includes (pp. 4 to 5): "The tax-free part of any scholarship or fellowship grant (including Pell grants)", "The tax-free part of any employer-provided educational assistance", "Veterans’ educational assistance", and "Any other educational assistance that is excludable from gross income (tax free), other than as a gift, bequest, devise, or inheritance."

Not reducing: p970 p. 14, Amounts that don’t reduce qualified education expenses, "Payment for services, such as wages; • A loan; • A gift;" and p970 p. 15, "An inheritance; or • A withdrawal from the student’s personal savings." Higher education emergency grants: p970 p. 2, "a student does not reduce an amount of qualified tuition and related expenses by the amount of an emergency financial aid grant."

Scholarships the student includes in income: i8863 p. 5, "a scholarship or fellowship grant isn’t treated as tax-free educational assistance to the extent the student includes it in gross income (the student may or may not be required to file a tax return) for the year the scholarship or fellowship grant is received and either" it must or may be applied to other expenses. The choice and its limit: p970 p. 15, "the amount of the scholarship or fellowship grant that is applied to nonqualified expenses can’t exceed the amount of the student’s actual nonqualified expenses that are paid in the tax year." Exception: i8863 p. 5, "A student cannot choose to include in income a scholarship or fellowship grant provided by an Indian tribal government".

Where the included amount goes: p970 p. 7, How To Report, "Include any taxable amount not reported to you in box 1 of Form W-2 on Schedule 1 (Form 1040), line 8r." i1040gi p. 92, Line 8r, "if you were a degree candidate, include on line 8r only the amounts you used for expenses other than tuition and course-related expenses." Schedule 1 line 8 other income is refused today by `scope.schedule1` (its question names 'gambling winnings, prizes or other income for Schedule 1 line 8'). So:

- If the student is a dependent, the inclusion is on the dependent's own return; this return only takes the resulting tax-free amount as `stu.assist_*`. Computable.
- If the student is you or your spouse and the included amount is not in Form W-2 box 1, this return needs line 8r: computable only if Stage 16 brings line 8r into scope; otherwise refused through the existing `scope.schedule1` (D8).

Refunds: i8863 p. 6, Refunds received in 2025, "figure the adjusted qualified education expenses for 2025 by adding all the qualified education expenses paid in 2025 and subtracting any refunds of those expenses received from the eligible educational institution during 2025." Refunds received after 2025 but before filing reduce 2025 expenses; refunds after filing are recapture on the later return ("Include that amount as an additional tax for the year the refund or tax-free assistance was received", i8863 p. 6), so they are not this return's matter. Tip, i8863 p. 6: a 2026 refund for a period paid in both years may reduce the 2026 expenses instead ("you may choose to reduce the qualified education expenses you paid in 2026 instead"); recommend help text and taking the filer's stated 2c amount.

529 and Coverdell: p970 p. 52, "An American opportunity or lifetime learning credit (education credit) can be claimed in the same year the beneficiary takes a tax-free distribution from a QTP, as long as the same expenses aren’t used for both benefits." The reduction runs against the distribution's expenses, not the credit's: "the beneficiary must further reduce them by the expenses taken into account in determining the credit." A taxable part lands on Schedule 1 line 8z and possibly Form 5329, both refused today. Recommendation: no new lines; help text telling the filer to enter only expenses not used for a tax-free distribution (D9).

### 4.9 Phase-out arithmetic (official examples)

- p970 p. 20, AOC: joint, MAGI $165,000, $5,000 of expenses, tentative $2,500, "The result is the amount of your phased out (reduced) American opportunity credit ($1,875)." (Decimal 0.750.)
- p970 p. 29, LLC: joint, MAGI $161,000, $6,600 of expenses, tentative $1,320, "The result is the amount of your phased-out (reduced) lifetime learning credit ($1,254)." (Decimal 0.950.)

Both decimals are exact at three places, so neither example tests the rounding reading.

### 4.10 Official examples usable as fixtures

| Example | Locator | What it fixes |
|---|---|---|
| Jack and Kay | p970 p. 19, Figuring the Credit, "Jack and Kay can claim a $2,500 American opportunity credit in 2025." | lines 27 to 30 at $4,300 |
| Bruce and Toni | p970 p. 28, "Bruce and Toni can claim a $1,000 (20% × $5,000) lifetime learning credit" | line 12, joint, no phase-out |
| AOC phase-out | p970 p. 20 | line 7 = $1,875 |
| LLC phase-out | p970 p. 29 | line 18 = $1,254 |
| Pell grant examples 1 and 2 | i8863 p. 5, "Your refundable American opportunity credit will be $1,000." | AQEE worksheet, line 8 |
| Bill, examples 1 to 3 | p970 pp. 15 to 16, "a credit of $2,500 and a tax liability after credits of $85 ($2,585 − $2,500)" | a whole single return; note the $85 nets the refundable $1,000 against tax, so the form values are line 19 $1,500 and line 29 $1,000 (inference) |
| Jane, example 5 | p970 p. 16, "Jane would be able to receive a $251 American opportunity credit ($200 refundable and $51 nonrefundable), a $1,700 additional child tax credit, and a $4,204 EIC." | a whole head of household return: the CLW at a $51 tax, Credit Limit Worksheet A going to zero, the ACTC and the EIC together; four scholarship variants on the same page |
| Sharon, Wilbert | i8863 p. 3 | line 23 |
| Mack, Shelly, Larry, Dee | p970 pp. 17 to 18 | lines 24 and 25 (interview help, not arithmetic) |

The Jane and Bill examples carry their AGI and tax as figured by the publication; whether the project's Tax Table gives the same tax is a check to run, not an assumption (I did not run it).

## 5. Credit order and every existing line that changes

### 5.1 Order

Which credits each worksheet subtracts (archived text):

- Form 2441 CLW: i2441 p. 5, line 2, Schedule 3 line 1 and line 6l only (per the Stage 15 map in `sources/2025/PREMISES.md`; not rechecked here).
- Form 8863 CLW line 5: "lines 1, 2, 6d, and 6l" (i8863 p. 8).
- Form 8880 CLW line 2 (per the Stage 15 map): "Enter the total of your credits from Schedule 3, lines 1 through 3, 6d, and 6l" (f8880 p. 2).
- Form 5695 Residential Clean Energy Credit Limit Worksheet (i5695 p. 5) and Energy Efficient Home Improvement Credit Limit Worksheet (i5695 p. 7): both list "Nonrefundable Education Credits, Schedule 3 (Form 1040), line 3".
- Schedule 8812 Credit Limit Worksheet A line 2 (i1040s8812 p. 4): "Schedule 3, line 1", "line 2", "Schedule 3, line 3", "line 4", "line 5b", and 6d, 6f, 6l, 6m.

Resulting order, no cycle: line 18 → FTC (s3.1) → Form 2441 (s3.2) → **Form 8863 (s3.3)** → Form 8880 (s3.4) → Form 5695 Part II (s3.5b) → Schedule 8812 (Form 1040 line 19) → Form 5695 Part I (s3.5a). Form 8863 reads only `f1040.line18`, `s3.line1`, `s3.line2` (and the refused 6d, 6l), none of which read line 3. The refundable part (line 8) is a payment on Form 1040 line 29 and is not in any credit limit.

### 5.2 Lines to add or change

| Line (id) | Now | Change | Reason |
|---|---|---|---|
| `s3.line3` (new) | absent | `copy f8863.line19`, printed "3", label "Education credits from Form 8863, line 19" (f1040s3 p. 1) | Schedule 3 line 3 |
| `s3.line8` | `sum(s3.line1, s3.zero)` here; Stage 15 adds lines 2, 4, 5a, 5b | add `s3.line3`; drop education from its `scope.credits` refusal text | f1040s3 p. 1, line 8 "Add lines 1 through 4, 5a, 5b, and 7" |
| `f1040.line29` | `param sales.zero` with a `scope.credits` refusal | `copy f8863.line8`; remove the refusal (line 29 carries only the AOC) | f1040 p. 2, line 29 "American opportunity credit from Form 8863, line 8" |
| `f1040.line30` | `scope.credits` refusal whose form text names 'Form 1040 lines 29 to 31' | reword to drop line 29 | adoption credit stays refused |
| `s8812.clw_a2` | `copy s3.line1` here; Stage 15 makes it a sum with 2, 4, 5b | add `s3.line3`; reword the refusal (3 no longer refused) | i1040s8812 p. 4, line 2 |
| Stage 15 id: Form 8880 CLW line 2 | Stage 15: s3.line1 + s3.line2, line 3 refused | add `s3.line3` | f8880 p. 2 |
| Stage 15 id: Form 5695 Line 14 worksheet (Part I) | Stage 15: line 3 refused | add `s3.line3` | i5695 p. 5 |
| Stage 15 id: Form 5695 Line 31 worksheet (Part II) | Stage 15: line 3 refused | add `s3.line3` | i5695 p. 7 |
| `scope.credits` | label and source list the supported credits | remove education credits from what it asks about (after Stage 15's narrowing) | the gate's residue |
| `scope.ready` refusal for `scope.credits` | form 'Other credit forms (Schedule 3 lines 2 to 4, 5b, 6d, 6f, 6l and 6m; Form 1040 lines 29 to 31)' | drop line 3 and line 29 | |
| `categories.json` `education` | `gates: [scope.credits]` | retire (`refused: false`, `gates: []`) | `schedule_c` precedent |

Downstream readers that do not change but whose values will move (each needs a fixture or a property, not an edit):

- `f1040.line20`, `.line21`, `.line22`, `.line24` (total tax), `.line32`, `.line33`, `.line34` (refund) through `s3.line8` and `f1040.line29`.
- `s8812.clw_a3`, `s8812.clw_a5`, `s8812.line13`, `s8812.line14` (CTC/ODC) and through them the ACTC chain (`s8812.line16a` onward): a larger education credit lowers the CTC limit and can raise the refundable ACTC (Jane, p970 p. 16).
- The Stage 15 saver's credit and Form 5695 Part I and II results.
- Nothing reads AGI differently: the credits do not change AGI. The scholarship choice does change AGI and earned income when the student is the filer (p970 p. 16, Jane); that path runs through Schedule 1 line 8r (D8), whose readers (AGI, line 9, and the earned income of the Standard Deduction Worksheet for Dependents, i1040gi p. 35, "Schedule 1, lines 3, 6, 8r, 8t, and 8u") are Stage 16's to wire.

New lines that read existing ones: `f1040.line11b` (lines 3, 14), `f1040.line18` (CLW 4), `f1040.status` (lines 2, 5, 13, 16, line 7 test), `sa.excluded_income` (refusal on 3 and 14), `sli.claimed` (zero), `dependent.claimed`, `dependent.tin`, `person.tin`, `person.itin_applied`, `person.role`.

## 6. Refuse-or-compute candidates

| # | Situation | Why it is hard | Recommendation |
|---|---|---|---|
| R1 | Filer with Form 2555, Form 4563 or excluded Puerto Rico income | MAGI is Worksheet 2-1 (p970 p. 20) | Refuse on lines 3 and 14 via the existing `sa.excluded_income` |
| R2 | You or your spouse claimed as someone's dependent | rule is plain | Compute: both credits zero (`sli.claimed`) |
| R3 | MFS, nonresident alien | already refused | No change |
| R4 | AOC needs Form 8862 (a post-2015 AOC denial, not since allowed) | Form 8862 not archived or prepared | Refuse via a new screen ('Was an AOC you claimed for a year after 2015 denied or reduced for a reason other than a math or clerical error, without an AOC allowed after filing Form 8862 for 2024?') |
| R5 | AOC ban (2 or 10 years) | a determination the filer knows | Refuse via the same screen, or treat AOC students as LLC students (D6) |
| R6 | Recapture of a prior-year credit | already refused | No change (`scope.other_line16`) |
| R7 | An academic period whose tax-free assistance exceeds its expenses | per-period floor (i8863 p. 9) | Refuse via a per-student screen if expenses are entered per student (D3); compute if a nested period collection is built |
| R8 | Expenses split across more than one academic period, no period over-assisted | sums are equal | Compute, one aggregate per student |
| R9 | More than two institutions | no arithmetic | Compute (line 22 is identity data) |
| R10 | No Form 1098-T and no exception | eligibility fails | Compute: student not claimable (no credit); or refuse to be safe (D5) |
| R11 | Missing institution EIN for an AOC student | AOC requirement 7 | Compute: student goes to line 31 (D6) |
| R12 | Student TIN not issued by the due date | both credits | Compute: student not claimable (reads `dependent.tin` / `person.tin`) |
| R13 | Filer TIN not issued by the due date | AOC requirement 5 | Compute: AOC students go to line 31 (D6, Q2) |
| R14 | Under-24 filer, refundability conditions | five facts, one an earned-income-versus-support judgment | Compute with return-level Bool and Count inputs (4.6) |
| R15 | Scholarship included in income, student a dependent | none for this return | Compute (`stu.assist_*` is the tax-free part) |
| R16 | Scholarship included in income, student is you or your spouse, not on W-2 box 1 | Schedule 1 line 8r | Compute if Stage 16 brings line 8r in; else refused by `scope.schedule1` (already) |
| R17 | 529 or Coverdell distribution in the same year | coordination on the distribution's side | Compute the credit; taxable distributions stay refused by `scope.schedule1` and Form 5329; help text |
| R18 | Education expenses also deducted on Schedule C | double benefit | Compute; help text on the expense input |
| R19 | 1098-T box 4 or box 6 prior-year adjustments | recapture or amendment of a prior year | Help text; recapture refused through `scope.other_line16` |
| R20 | Spouse is the student on a joint return | person-level | Compute (person entry) |
| R21 | Several students, mixed AOC and LLC | per-student routing | Compute |
| R22 | Prepaid expenses for a January to March 2026 period | timing rule | Compute; help text on lines 24 and 1 |
| R23 | Credit Limit Worksheet line 6 negative | not reachable if lines 1 and 2 are themselves limited | Compute; see D10 |

## 7. Parameters for `params/2025.yaml`

All in cents; status-keyed values use `{single, mfs, mfj, qss, hoh}`. MFS is refused project-wide and f8863 prints no MFS amount; give MFS the single amount (as `sli.base_other` does through its `choose`) or key it to the other column and record that it is never reached.

| Param | Type | Value | Locator |
|---|---|---|---|
| `edu.magi_limit` | NonNegDollars by status | mfj 18000000; single, hoh, qss 9000000 | f8863 p. 1, line 2, "Enter $180,000 if married filing jointly; or $90,000 if single, head of household, or qualifying surviving spouse"; again at line 13; i8863 p. 1, Reminders |
| `edu.phaseout_range` | NonNegDollars by status | mfj 2000000; single, hoh, qss 1000000 | f8863 p. 1, line 5, "Enter $20,000 if married filing jointly; or $10,000 if single, head of household, or qualifying surviving spouse"; again at line 16 |
| `aoc.refundable_rate` | Rate | 40/100 | f8863 p. 1, line 8, "Multiply line 7 by 40% (0.40)" |
| `llc.expense_cap` | NonNegDollars | 1000000 | f8863 p. 1, line 11, "Enter the smaller of line 10 or $10,000" |
| `llc.rate` | Rate | 20/100 | f8863 p. 1, line 12, "Multiply line 11 by 20% (0.20)" |
| `aoc.expense_cap` | NonNegDollars | 400000 | f8863 p. 2, line 27, "Don’t enter more than $4,000" |
| `aoc.full_band` | NonNegDollars | 200000 | f8863 p. 2, line 28, "Subtract $2,000 from line 27"; line 30, "add $2,000 to the amount on line 29" |
| `aoc.second_rate` | Rate | 25/100 | f8863 p. 2, line 29, "Multiply line 28 by 25% (0.25)" |

Second printings (for the cross-check): the MAGI limits and phase-out ranges in i8863 p. 3 ("between $80,000 and $90,000 ($160,000 and $180,000 if you file a joint return)") and p970 p. 20; the $2,500 and $2,000 maxima in i8863 p. 2, Table 1 ("Up to $2,500 credit per eligible student", "Up to $2,000 credit per return"), which are property checks (AOC per student ≤ $2,500, LLC ≤ $2,000), not params.

Not params (screen or help text): age 24, 18, the 5 calendar months, the four tax years, the Form 1098-T request date.

Year-diff note: Public Law 119-21 sec. 70606 rewrites the identification rule for "taxable years beginning after December 31, 2025" (plaw-119-21 p. 219): "No credit shall be allowed under subsection (a) to an individual unless the individual includes on the return of tax for the taxable year ... such individual’s social security number". It does not apply to 2025; the 2026 year-diff will need a valid-SSN test (an ITIN no longer suffices), probably reusing the `work_ssn`-style inputs.

## 8. Open questions (readings the text leaves undecided)

- **Q1. Academic periods.** The AQEE worksheet is "for each student for each academic period" (i8863 p. 9) and floors each period at zero. Is it acceptable to take one total per student when no period's tax-free assistance exceeds that period's expenses (equal results), refusing otherwise? Or should each student carry a nested collection of academic periods?
- **Q2. Whose TIN, for which credit.** i8863 p. 3 says the student must have a TIN "by the due date of his or her 2025 return" for both credits, and "Filers and students must have been issued a TIN by the due date of their 2025 return" for the AOC. Does the student's own return mean the return claiming the credit (the natural reading, recorded as such), and on a joint return must both spouses have a TIN for the AOC? The project's `household.all_tin` is labelled 'You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN'.
- **Q3. Age at the end of 2025.** Line 7 tests under age 24, under age 18 and age 18 at the end of 2025 (i8863 p. 7). Pub. 501's day-before-the-birthday rule is stated for age 65 (p501, "considered to reach age 65 on the day before the person’s 65th birthday"). Should the interview ask age as a whole number (like `dependent.age`) and leave the birthday edge to the filer, or ask by birth date with the day-before rule applied?
- **Q4. Credit Limit Worksheet line 6.** "Subtract line 5 from line 4" has no floor. If Schedule 3 lines 1 and 2 are each limited by their own worksheets, line 6 cannot be negative; encode as printed with a property test, or with `subtract_floor0` and a register entry?
- **Q5. Full-time student in line 7, item 1c.** The definition is headed "Solely for purposes of determining whether a scholarship is considered support" (i8863 p. 7), yet item 1c uses "a full-time student (defined later)" as a condition too. Read the same 5-month definition for both uses?
- **Q6. AOC whenever eligible.** The form routes an eligible student to lines 27 to 30; p970 p. 22 says the filer "can choose to claim either credit, but not both". Follow the form (no election input), or ask whether to elect the LLC for a student who qualifies for the AOC?
- **Q7. Requirements 5 to 7 with no line.** When a student passes lines 23 to 26 but the filer lacks a TIN, or the EIN is not available, does the student go to line 31 (the i8863 p. 4 Tip) or get no credit? The Tip supports line 31 for the LLC's own requirements being met.
- **Q8. Form 1098-T not received.** Should the tool ask one Bool per student ('Did the student receive a 2025 Form 1098-T from each institution, or does an exception in the instructions apply?') and deny both credits for that student on No, or refuse?
- **Q9. Who paid.** Expenses paid by a third party or by a claimed dependent count as yours (p970 p. 19). The input is then 'paid for this student by anyone in 2025'. Confirm no per-payer split is wanted.
- **Q10. Dependent listed but not claimed.** A listed person with `dependent.claimed` false cannot be a student of this return (p970 p. 19). Ask the education questions only for claimed dependents (by reachability), with no refusal?
- **Q11. The 1098-T request date.** i8863 p. 1 says "After January 31, 2026", p970 p. 2 says "After February 2, 2026". Help text only; which to cite?
- **Q12. Line 7 box on the values sheet.** The box is a printed checkbox; show it as a Bool line (like `f1040.line27b`)?
- **Q13. Lines 22(2) and 22(3).** Shown per student as Bools, though no arithmetic reads 22(3); or omit 22(3) as identity data?

## 9. Draft owner decision batch

Each: the question, the recommended answer, the alternative.

1. **D1 Scope.** Compute Parts I to III, the AQEE worksheet, the CLW, line 29 and Schedule 3 line 3 for all students of the return; refuse R1, R4 and R5 (Form 8862 / ban screen), R7 if aggregate; leave R3, R6 and R16 on their existing gates. *Alternative:* LLC only now, AOC later.
2. **D2 Where the students live.** (B) Part III and AQEE inputs on the `person` and `dependent` entries, reached only when 'Did you pay qualified education expenses for this person in 2025?' is yes, with the arithmetic in one shared `def` bound from each; return lines add `sum_over person` and `sum_over dependent`. This reads `dependent.claimed` and `dependent.tin` directly. *Alternatives:* (A) a return-level `student` collection (like `retirement`) with a who-is-it enum and its own TIN and claimed questions, which cannot check them against the dependent entries (spec 4.4 forbids reading another entry); (C) a `student` collection nested once under `person` and once under `dependent` (two collection definitions of the same lines). Whether a `def` instance's lines appear on the values sheet as the student's Part III needs checking in the engine before choosing B.
3. **D3 Academic periods (Q1).** One total per student, with a screen that refuses when any period's tax-free assistance exceeds that period's expenses. *Alternative:* a nested academic-period collection.
4. **D4 Expenses by credit.** Two inputs per student: amounts required to be paid to the institution (tuition, fees and required course materials), and other course materials needed for a course (counted for the AOC only). *Alternative:* one input asked per credit after routing (the filer must know the route first).
5. **D5 Form 1098-T (Q8, Q13).** No 1098-T collection; boxes 1, 4, 5, 7, 8, 9 as help text on the inputs; one Bool per student for 'received or an exception applies' (No: no credit for that student) and one for 2024 box 7, shown. *Alternative:* a 1098-T collection per student with box inputs (box 1 is not the line value, so it would only be displayed); or refuse when not received.
6. **D6 Requirements without lines (Q2, Q7).** Student TIN fails: no credit for the student. Filer TIN (both spouses on a joint return, `household.all_tin`) or EIN fails: AOC students go to line 31. Ban or Form 8862: refuse. *Alternative:* refuse in every one of these cases.
7. **D7 Refundability (Q3, Q5).** Compute line 7 from return-level inputs asked only on a non-joint return with line 7 above zero: age at the end of 2025 (Count), full-time student (5-month rule), earned income less than half of support (Bool, with the i8863 definitions as help), a parent alive. *Alternative:* refuse non-joint AOC filers under 24.
8. **D8 Scholarships.** Take the tax-free part as entered; no optimization of the inclusion choice (help text cites p970 pp. 15 to 16). When the student is you or your spouse and an included amount is not on Form W-2, it rides on Schedule 1 line 8r: computed if Stage 16 brings 8r in, else refused by the existing `scope.schedule1`. *Alternative:* a new screen that refuses any filer-student who includes a scholarship in income.
9. **D9 529 and Coverdell.** Help text only (enter expenses not used for a tax-free distribution); taxable distributions stay refused. *Alternative:* a screen refusing any Form 1099-Q in the household.
10. **D10 CLW line 6 (Q4).** `subtract_floor0`, with a register entry saying the floor is never reached when lines 1 and 2 are limited. *Alternative:* `subtract` as printed and a property test.
11. **D11 Decimal places.** Lines 6 and 17 at three places, half-up, through `prorate`, recorded as a new register entry citing f8863 lines 6 and 17 and the Stage 11 ruling. *Alternative:* full precision.
12. **D12 AOC versus LLC (Q6).** Follow the form: an eligible student is an AOC student. *Alternative:* an election input per student.
13. **D13 Reuse `sli.claimed`.** One question serves the student loan interest deduction and both credits. *Alternative:* a separate education question.
14. **D14 Coverage.** Retire `education` in `categories.json` (refused false, gates empty); list the new refusals among the unmeasured gates. *Alternative:* keep the category with the residual gates.

## 10. Verified vs inferred

Checked against the archived text (read on the cited pages): every Form 8863 line text (f8863 pp. 1 to 2, layout and reading-order text); the Credit Limit Worksheet and AQEE worksheet lines (i8863 pp. 8 to 9); the seven AOC requirements, the line 7 conditions and definitions (i8863 pp. 3 to 4, 6 to 7); the 1098-T requirement and its exceptions (i8863 p. 1, p970 p. 2); the Form 1098-T box instructions (i1098et p. 4); Schedule 3 line 3 and line 8 wording (f1040s3 p. 1); Form 1040 line 29 (f1040 p. 2); i1040gi line 29 (p. 61), Schedule 3 line 3 (p. 115) and Schedule 1 line 8r (p. 92); Credit Limit Worksheet A line 2 (i1040s8812 p. 4); the two Form 5695 worksheets subtracting line 3 (i5695 pp. 5, 7, the line-3 entries only); the p970 examples cited (pp. 15 to 20, 28, 29); Public Law 119-21 sec. 70606 and its effective date.

Checked against the repository: `scope.credits` and its refusal texts (`forms/2025/scope.yaml`); `s3.line8` and the absence of `s3.line3` (`forms/2025/s3.yaml`); `f1040.line29` as `param sales.zero` with a `scope.credits` refusal, and `f1040.line11b`, `.line18` (`forms/2025/f1040.yaml`); `s8812.clw_a2` as `copy s3.line1` (`forms/2025/s8812.yaml`); `sli.claimed`, `sli.eligible`, `sli.allowed` and the `prorate` use at three places (`forms/2025/sli.yaml`); `amb.2025.sli_ratio_places` (`ambiguities/2025.yaml`); `sa.excluded_income` (`forms/2025/sa.yaml`); the `dependent`, `person` and `household` inputs named above; the `def` mechanism (`forms/2025/se.yaml`, bound in `person.se_line6`); collection parents (`parent:` in the YAML files); the `education` category, its two SOI cells and their values in `soi-23in33ar.xls`; the coverage figures in `reports/2025/filer_coverage.md` and `.json`; the absence of any existing 8863 line, register entry or task (grep of `forms`, `ambiguities`, `interview`, `TASKS.md`).

Inferred, not verified:

- All Stage 15 line ids and shapes (Form 8880 CLW line 2, the Form 5695 worksheets, the integrated `s3.line8` and `s8812.clw_a2`): taken from the Stage 15 maps in `sources/2025/PREMISES.md` and T-048, not from code. The Form 2441 and Form 8880 worksheet texts quoted in 5.1 were not reread here.
- That a shared `def` can carry Part III with its lines shown on the values sheet (D2 option B); I read how `se` is bound, not the engine's handling of def lines on the values sheet.
- That the interview asks per-entry inputs only when reachable, from `interview/README.md` ('questions are drawn from unresolved reachable inputs'), not from a test.
- That AOC ≥ LLC per student (4.4): my arithmetic, not the text (the text asserts it in the i8863 Tip).
- That the Bill and Jane examples reproduce under the project's Tax Table and EIC Table: not run.
- That Stage 16 will or will not compute Schedule 1 line 8r: unknown; D8 is written for both.
- The column 40 SOI header: accepted by the estimator's substring test; not inspected cell by cell.
- The microdata overlap for education (0.5% flagged before raking): the figure is from the report; its effect on the +4.1 estimate is not quantified.
