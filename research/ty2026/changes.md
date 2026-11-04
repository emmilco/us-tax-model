# The 2026 change map

TY2026 preparation, step 3 (`docs/ty2026/2026-11-04_ty2026_cloud_brief.md`). For every worklist item of kind (a)
in `reports/2026/worklist_split.md` (changed text or amounts in a document that has a 2026 source: 426 items, 399
distinct ids, of which the 16 in C-PEOP-23 and C-PEOP-24 are counted as kind (b), owner decision 2026-11-04), what changed, quoted from the archived 2026 and 2025 sources with their pages, the project ids it
touches, and its kind: an amount (a parameter), a rule (a definition change), a new line or form, wording only, or
not encoded. Every 2026 draft's What's New, Reminders and Future Developments are accounted for in each section's
table. Sections: the priority forms first (Form 1040, Schedules 1, A, B, D, Form 8949, Form 8889, the Form W-2
inputs, and the new Schedule 3-A and Form 1062 they name), then the other forms in scope.

**Rules of the map.** Pages are PDF pages of `sources/<year>/<id>.txt` split on form feeds (a draft's page 1 is the
IRS cover). "(draft)" marks a 2026 statement that rests on an IRS draft; everything else marked final rests on a final
2026 edition, IRS guidance, or Public Law 119-21 as printed. Nothing is stated from memory. Every quote on a
**2026:** or **2025:** bullet is checked against its page by `research/ty2026/check_quotes.py` (672 quotes, 0 not
printed when the map was written). The 2026 Instructions for Form 1040 (with Schedules 1, 1-A and 2 and their
worksheets), for Schedules A and D, Form 8949, Form 8962, Form 4562 and the publications listed in
`reports/2026/archive_refresh_2026-11-04.md` are not posted: the 1,810 items of kind (b) wait on them, and several
entries below say which rule they cannot settle yet.

**Corrections.** The independent verification (`changes.verification.md`: 2 high, 11 medium, 7 low) is applied: each affected entry carries a "Correction (verification)" line, three entries are reclassified, What's New rows are added, and C-PEOP-27 is new.

**How it was made.** The priority section was written in the main session; the other four sections by four
independent agents working from the same brief and the archived sources only (logged in
`research/costs/agent_runs.jsonl`), each checked by script for quotes, coverage and ids. An independent
verification is in `changes.verification.md`.

| Section | Entries |
|---|---|
| Priority forms: Form 1040, Schedules 1, A, B and D, Form 8949, Form 8889 and the Form W-2 inputs | 29 |
| Schedules 1-A, 2, 3 and 8812; Forms 8959, 8960, 8995, 8995-A, 4952 and 1116 | 39 |
| Credits: Forms 5695, 8880, 8863 and 2441 | 20 |
| Retirement, health coverage and people: Forms 1099-R, 8606, 5329, 8962 and 1095-A; filer, dependent and household tests; other information returns | 27 |
| Business: Schedules C and SE, Forms 4562 and 7206, vehicles; Schedule E, Form 8582 and the K-1s | 18 |
| Public Law 119-21: the provisions in force for 2026, read against the encoding (statute read, 2026-11-04) | 2 |

## Priority forms: Form 1040, Schedules 1, A, B and D, Form 8949, Form 8889 and the Form W-2 inputs

Read: the 2026 drafts of Form 1040, Schedules 1, A, B, D, Form 8949, Form 8889 and its instructions, the
Schedule B instructions, Schedule 3-A and Form 1062 with its instructions (new forms the 2026 Form 1040
names); the final 2026 Form W-2 and General Instructions for Forms W-2 and W-3; Rev. Proc. 2025-32 and
2025-19; Publication 15 (2026); Public Law 119-21 as printed (`plaw-119-21`, final: the statute, quoted where
it fixes a 2026 rule the drafts show); and the continuous-use information-return forms (1099-INT, 1099-DIV,
8283), which are byte-identical to the 2025 archive. 62 worklist items of kind (a) fall in this section. The
2026 Instructions for Form 1040 and for Schedules A and D are not posted: every Form 1040, Schedule 1 and
Schedule A line instruction, and the worksheets these forms now name (the Charitable Contribution Limitation
Worksheet, the Itemized Deductions Worksheet), have no 2026 source yet. Where this section states a 2026 rule
from the statute, the IRS form text that applies it is still a draft or not posted.

Pages are PDF pages of the archived text (`sources/<year>/<id>.txt` split on form feeds); a draft's page 1 is
the IRS cover.

### What's New and Reminders accounted for

The forms themselves (Form 1040, Schedules 1, A, B, D, Forms 8949, 8889, W-2, 1062, Schedule 3-A) carry no
What's New section; their changes were read line by line against the 2025 forms and are entries below.

| document | item (quoted heading or first words) | entry or "not encoded: reason" |
|---|---|---|
| `i8889` | Future Developments ("Go to IRS.gov/Form8889") | not encoded: a pointer |
| `i8889` | What's New, "Expansions to HSA eligibility", 1. Telehealth and Remote Care Services | not encoded: unchanged from 2025 (section 71306 applies to plan years after 2024); see the correction to C-PRI-22 |
| `i8889` | What's New, 2. Bronze and Catastrophic Plans Treated as HDHPs | C-PRI-22 |
| `i8889` | What's New, 3. Direct Primary Care Service Arrangements | C-PRI-22, C-PRI-23 |
| `i8889` | Reminders, "Preventive care for purposes of qualifying as a high deductible health plan" (Notice 2024-75) | not encoded: HDHP plan design; the encoding takes the HDHP coverage as an answer (`person` coverage questions); unchanged from 2025 |
| `i8889` | Reminders, "Expenses treated as amounts paid for medical care" (condoms, Notice 2024-71) | not encoded: a kind of qualified medical expense; the encoding takes the amount of qualified expenses paid as an answer (`f8889.medical`); unchanged from 2025 |
| `i8889` | Reminders, "Q&As on certain qualified medical expenses" | not encoded: a pointer |
| `iw2w3` | What's New, State Paid Family and Medical Leave Act | not encoded: employer reporting into box 1, which the encoding reads as reported |
| `iw2w3` | What's New, "Wage reporting threshold increased" ($600 to $2,000) | not encoded: employer filing threshold |
| `iw2w3` | What's New, "Box 14 has been split into box 14a and box 14b" | C-PRI-24 |
| `iw2w3` | What's New, "Deduction for qualified tips" (new box 12 code TP, box 14b) | C-PRI-24 |
| `iw2w3` | What's New, "Deduction for qualified overtime" (new box 12 code TT) | C-PRI-24 |
| `iw2w3` | What's New, "Employer contributions to Trump accounts" (new box 12 code TA) | C-PRI-24 |
| `iw2w3` | What's New, "Penalties increased" | not encoded: employer penalties |
| `iw2w3` | What's New, "The Form W-2c was released in January 2026 and has a revision date (Rev. 1-2026)" | not encoded: employer correction form (added by the verification) |
| `iw2w3` | What's New, "Changes to boxes 9 and 14a" (box 9 reduced in size) | not encoded: form layout (added by the verification) |
| `iw2w3` | Reminders (Form 15397, OMB number, disaster relief, fillable copies, due date, extensions, rejected wage reports, and the rest) | not encoded: employer filing mechanics |
| `i1040sb` | Future Developments only; no What's New or Reminders | not encoded: a pointer |
| `i1099int` (draft) | What's New, "Change in reporting threshold for interest paid in the course of your trade or business" ($2,000) | not encoded: payer filing threshold; the encoding reads interest as reported or as the filer states it |
| `i1099int` (draft) | Reminders (Pub. 1099, continuous-use revisions, e-filing, IRIS, nonresident aliens, fillable copies) | not encoded: payer filing mechanics |
| `i1099div` | What's New, "E-filing returns"; Reminders (general instructions, continuous use, section 897 gain, fillable copies) | not encoded: payer filing mechanics; the document is byte-identical to the 2025 archive |
| `i8283` | Reminders ("Disallowance of deduction for certain conservation contributions"; "Requirement to fully complete Sections A and B") | not encoded (byte-identical to the 2025 archive; the conservation rule concerns pass-through entities, and the section rule is already in `gift.section_b`) |
| `i1062` (draft) | What's New, "New election to pay the tax on gain from the sale or exchange of qualified farmland property to qualified farmers in installments" | C-PRI-04 |
| `rp-25-32` | Section 2, Changes, .01 (rate tables, § 1(j)) | C-PRI-10 (parameters, step 4) |
| `rp-25-32` | Section 2, .02 (refundable adoption credit, § 23(a)(4)) | not encoded: the adoption credit is refused (Form 1040 line 30 is not computed; `scope` credit screen) |
| `rp-25-32` | Section 2, .03 (child tax credit, § 24) | SCHED section (Schedule 8812) |
| `rp-25-32` | Section 2, .04 (removal of § 36B(f)(2)(B)) | PEOP section (Form 8962) |
| `rp-25-32` | Section 2, .05, .06, .09, .11, .14, .16 (housing credit ceiling, § 45F, § 127, § 179D, estate exclusion, § 6726 penalty) | not encoded: business, employer, estate and penalty provisions outside the individual forms in scope |
| `rp-25-32` | Section 2, .07 (AMT exemption amounts, § 55) | not encoded: the AMT is refused (Form 6251; `s2.amt`) |
| `rp-25-32` | Section 2, .08 (standard deduction, § 63(c)(7)) | C-PRI-10 (parameters, step 4) |
| `rp-25-32` | Section 2, .10 (§ 179 limits) | BUS section (Form 4562) |
| `rp-25-32` | Section 2, .12 (§ 199A minimum deduction) | SCHED section (Forms 8995, 8995-A) |
| `rp-25-32` | Section 2, .15 (§ 6041(a) information-reporting threshold) | not encoded: payer reporting |
| `rp-25-32` | Section 2, .13 (§ 529A ABLE contribution limit) | not encoded: ABLE contributions are not computed (added by the verification) |
| `rp-25-19` | Section 3 (2026 HSA amounts; HDHP minimum deductibles and out-of-pocket maximums; excepted benefit HRA) | C-PRI-20 (HSA limits); the HDHP figures are not encoded (coverage is an answer); the HRA item is not encoded |
| `p15` | 2026 social security wage base ("The social security wage base limit is $184,500") | C-PRI-25 |

### C-PRI-01. Form 1040 line 12f: charitable contribution deduction for non-itemizers

- **Kind:** new line or form
- **2026:** `f1040` p. 3 (draft): "12f Charitable contribution deduction for non-itemizers (see instructions)"; "14 Add lines 12e, 12f, 13a, and 13b"
- **2026 (statute, final):** `plaw-119-21` p. 165: "by striking ‘‘$300 ($600’’ and inserting ‘‘$1,000 ($2,000’’" (section 70424, amending section 170(p)); p. 165: "exceeds 0.5 percent of the taxpayer’s contribution base" (section 70425, which section 70425(a)(3) coordinates with section 170(p))
- **2025:** `f1040` p. 2: "Add lines 12e, 13a, and 13b" (no line 12f)
- **Touches:** `f1040.line14`; a new line (`f1040.line12f`) and its inputs; `sa.itemizes` and `sa.deduction` (the deduction applies only when the standard deduction is taken)
- **Worklist items:** none (found by reading the form; no 2025 citation rests on it)
- **Notes:** The rule text the line applies (which contributions count, the joint amount, who may claim it) is in section 170(p), whose base text is not archived, and in the 2026 Form 1040 instructions, not posted. Adoption: archive the 2026 instructions (or 26 U.S.C. 170(p) as amended) before encoding; until then the line can only be refused or held at zero with a refusal for any non-itemizer with cash gifts.

### C-PRI-02. Form 1040 lines 13a and 13b exchange places; Schedule 1-A total moves to line 44

- **Kind:** new line or form (renumbering)
- **2026:** `f1040` p. 3 (draft): "13a Additional deductions from Schedule 1-A, line 44"; "13b Qualified business income deduction from Form 8995 or Form 8995-A"
- **2025:** `f1040` p. 2: "13a Qualified business income deduction from Form 8995 or Form 8995-A"; "Additional deductions from Schedule 1-A, line 38"
- **Touches:** `f1040.line13a`, `f1040.line13b` (the ids keep their meaning; their `printed` fields exchange), `f1040.line14`; `scope.ready` (its quote "Additional deductions from Schedule 1-A, line 38"); every reader that names "line 13a" or "line 13b" in a label or citation (Schedule A line 18 reads both, C-PRI-18; Form 8995/8995-A and Schedule 1-A worksheets, SCHED section)
- **Worklist items:** `f1040.line13b`, `scope.ready` (line), `scope.ready` (refusal)
- **Notes:** Spec 7: renumbering shows as a change to `printed` with `id` unchanged. Schedule 1-A's own renumbering to line 44 is in the SCHED section. The 2026 Form 8995 instructions (draft) still say to enter the deduction on line 13a (C-SCHED-31): the two drafts disagree; the final Form 1040 decides.

### C-PRI-03. Form 1040 lines 24a, 24b and 24c: Form 1062 installment (new form)

- **Kind:** new line or form
- **2026:** `f1040` p. 3 (draft): "24a Add lines 22 and 23. This is your total tax"; "24b Enter amount from Form 1062, line 15"; "24c Add lines 24a and 24b"; "If line 33 is more than line 24c, subtract line 24c from line 33"; "Subtract line 33 from line 24c"
- **2025:** `f1040` p. 2: "Add lines 22 and 23. This is your total tax"; "If line 33 is more than line 24, subtract line 24 from line 33"
- **Touches:** `f1040.line24` (becomes 24a), new lines 24b and 24c, `f1040.line34`, `f1040.line37`; Schedule 3-A line 3 reads line 24a (C-PRI-05)
- **Worklist items:** none
- **Notes:** See C-PRI-04 for the form. Line 24b needs a refusal (the encoding does not compute Form 1062) and line 24c a sum; with 24b refused or zero, 24c equals 24a.
- **Correction (verification):** see the correction to C-PRI-04: Schedule 3 line 13e also reads Form 1062.

### C-PRI-04. Form 1062: election to pay tax on a sale of qualified farmland property in installments

- **Kind:** new line or form (not to be computed: refuse)
- **2026:** `i1062` p. 2 (draft): "New election to pay the tax on gain from the sale or exchange of qualified farmland property to qualified farmers in installments"; `f1062` p. 2 (draft): "15 First installment due. Enter 25% (0.25) of line 14 here and on Form 1120, line 32, or the applicable line of your return"
- **2025:** no counterpart
- **Touches:** a new refusal gate (no 2025 id): a sale of farmland reported on Schedule D or Form 8949 (`sales`, which the encoding computes) could be a qualified sale for which the filer wants the election
- **Worklist items:** none
- **Notes:** The election is optional ("for which the taxpayer wants to elect"), so the refusal asks whether the filer makes the election. The draft is "Form 1062 (Rev. 12-2026)". Ambiguity to record at adoption: whether Form 1040 line 24b's "Form 1062, line 15" (25% of the net tax) is what an individual enters, since Form 1062 line 15 names Form 1120 and "the applicable line of your return".
- **Correction (verification):** Schedule 3 (2026 draft) line 13e takes Form 1062 line 14 ("Total section 1062 applicable net tax liability. Enter amount from Form 1062, line 14", `f1040s3` p. 2), so the election puts line 14 into payments (through `s3.line14`, `s3.line15`, `f1040.line31`, line 32a) and line 15 into tax; cross-reference C-SCHED-39. Line 15 is 25% of line 14, the section 1062 applicable net tax liability (`changes.verification.md`).

### C-PRI-05. Schedule 3-A and Form 1040 lines 32a to 32c: federal public benefit

- **Kind:** new line or form (rule; draft)
- **2026:** `f1040` p. 3 (draft): "32b Amount from Schedule 3-A"; "32c Subtract line 32b from line 32a"; "33 Add lines 25d, 26, and 32c"; `f1040s3a` p. 2 (draft): "Complete Schedule 3-A (Form 1040) only if you are claiming the earned income credit (EIC), additional child tax credit (ACTC), refundable American opportunity credit, or refundable adoption credit"; "Subtract line 5 from line 2. This is your federal public benefit"; "Do you want to receive your federal public benefit?"; "Are you or your spouse a U.S. citizen, U.S. national, or qualified alien? See instructions"
- **2025:** `f1040` p. 2: "Add lines 27a, 28, 29, 30, and 31. These are your total other payments and refundable credits"
- **Touches:** `f1040.line32` (becomes 32a), new lines 32b and 32c, `f1040.line33`; Schedule 3-A lines 1a to 8 (a new form definition) reading `f1040.line32`, `f1040.line31`, `f1040.line24` (24a) and Schedule 2 line 20 (renumbered Schedule 2, SCHED section); the person facts for citizenship or qualified-alien status (C-PRI-06)
- **Worklist items:** none
- **Notes:** The arithmetic is printed on the draft (lines 1a to 6) and is encodable with existing atoms; line 7 is an election and line 8 a status question whose "qualified alien" definition is in instructions not yet posted (no Schedule 3-A instructions are on the draft page). A refusal is needed for the Form 1040-NR and 1040-SS branches (not in scope). Every Schedule 3-A rule rests on a draft.
- **Owner decision (2026-11-04):** refuse Schedule 3-A returns until its instructions define "qualified alien". The proposal (`forms-proposed/s3a.yaml`) figures lines 1a to 6 and asks line 7, and refuses line 8 (and so Form 1040 lines 32b to 37) whenever line 8 is reached: line 6 is more than zero and line 7 is Yes (`s3a.gate.qualified_alien`). The line 8 question (`s3a.eligible`) is dropped until the instructions post.

### C-PRI-06. Form 1040 page 1: work-authorization question

- **Kind:** new line or form (question; draft)
- **2026:** `f1040` p. 2 (draft): "At the time you file your return, are you, and your spouse if filing jointly, a U.S. citizen, U.S. national, or an alien lawfully authorized to work in the U.S.? (see instructions)"
- **2025:** no counterpart
- **Touches:** `person` (a new question per filer); no 2025 line computes from it
- **Worklist items:** none
- **Notes:** The draft form does not say what the answer feeds; the instructions are not posted. It differs from Schedule 3-A line 8 ("qualified alien"); do not merge them without the instructions.

### C-PRI-07. Form 1040 line 28: the ACTC opt-out box is not printed

- **Kind:** new line or form (a box removed)
- **2026:** `f1040` p. 3 (draft): "28 Additional child tax credit (ACTC) from Schedule 8812"
- **2025:** `f1040` p. 2: "If you do not want to claim the ACTC, check here"
- **Touches:** `f1040.line28_box`
- **Worklist items:** none
- **Notes:** The 2025 line is a display-only box the tool never asks (its label says so); remove it at adoption, or keep it hidden if the final form restores it.

### C-PRI-08. Form 1040: labels reworded

- **Kind:** wording only
- **2026:** `f1040` p. 3 (draft): "29 Refundable American opportunity credit from Form 8863, line 8"; "23 Additional taxes, including self-employment tax, from Schedule 2, line 21"; p. 2: "If a joint return, spouse’s first name and middle initial"
- **2025:** `f1040` p. 2: "American opportunity credit from Form 8863, line 8"; "Other taxes, including self-employment tax, from Schedule 2, line 21"; p. 1: "If joint return, spouse’s first name and middle initial"
- **Touches:** `f1040.line29`, `f1040.line23` (labels); the enum `person_role` and the refusal `f1040.line1a` (their quote "If joint return, spouse’s first name and middle initial")
- **Worklist items:** `f1040.line1a` (refusal), `person_role` (enum)
- **Notes:** Relabel and requote; nothing computed changes.

### C-PRI-09. Form 1040: dates that move with the year

- **Kind:** wording only (year constants)
- **2026:** `f1040` p. 3 (draft): "Were born before January 2, 1962"; "Amount of line 34 you want applied to your 2027 estimated tax"
- **2025:** `f1040` p. 2: "Were born before January 2, 1961"
- **Touches:** the age questions and their readers (`sa.age65`, `sa.boxes_age65`, the person age facts; `--adopt` lists year-bearing ids), `f1040.line36`
- **Worklist items:** none of kind (a) (the year diff moves years before comparing)
- **Notes:** `tools/year_diff.py --adopt` lists the year constants to move.

### C-PRI-10. Standard deduction, tax rate schedules and other Rev. Proc. amounts

- **Kind:** amount (parameter)
- **2026:** `f1040` p. 3 (draft): "$16,100", "$32,200", "$24,150" (the standard deduction margin box); the final amounts are in `rp-25-32` (section 4.14; section 4.01 for the rate tables), proposed in step 4
- **2025:** `f1040` p. 2: "$15,750"
- **Touches:** `sa.standard_base` and the bracket, Tax Computation Worksheet and capital-gain parameters (step 4, `research/ty2026/params-2026.proposed.yaml`); the Tax Table (`tables/2025/tax_table.yaml`, which waits on the 2026 Form 1040 instructions)
- **Worklist items:** none in this section (the parameters' items are in step 4)
- **Notes:** The draft's margin amounts are checked against Rev. Proc. 2025-32 in step 4.

### C-PRI-11. Schedule 1: sub-line numbers printed in full; line 14 reworded

- **Kind:** wording only
- **2026:** `f1040s1` p. 2 (draft): "8b Gambling"; p. 3: "14 Moving expenses for members of the Armed Forces and the intelligence community"
- **2025:** `f1040s1` p. 2: "Moving expenses for members of the Armed Forces. Attach Form 3903"; p. 1: "b Gambling" (the sub-lines are printed with their letter only)
- **Touches:** labels of `s1.line1`, `s1.line2a`, `s1.line8b`, `s1.line8c`, `s1.line8f`, `s1.line8g`, `s1.line11`, `s1.line18`, `s1.line19a`, `s1.line20`, `s1.line24a`, `s1.cod_figured`; line 14 is refused through `scope.schedule1` (the Schedule 1 screen lists line 14 among the adjustments it refuses)
- **Worklist items:** `s1.cod_figured`, `s1.line1`, `s1.line11`, `s1.line18`, `s1.line19a`, `s1.line20`, `s1.line24a`, `s1.line2a`, `s1.line8b`, `s1.line8c`, `s1.line8f`, `s1.line8g`, `scope.schedule1`
- **Notes:** The printed numbers of the Schedule 1 lines are unchanged. The 2026 line instructions are in the Form 1040 instructions, not posted: every Schedule 1 line also waits on them (kind (b)).
- **Correction (verification):** line 14 is a definition change, not wording: `plaw-119-21` p. 95 extends the moving expense deduction to "MEMBERS OF THE INTELLIGENCE COMMUNITY". It stays refused through `scope.schedule1`; record the wider class. The other listed labels (`s1.line1`, `s1.line11` and others) are printed the same in both years; they are listed only because the worklist flagged them (`changes.verification.md`).

### C-PRI-12. Schedule 1: excess business loss threshold

- **Kind:** amount (parameter)
- **2026:** `rp-25-32`, section 4.31 "Threshold for Excess Business Loss" (final); value in step 4
- **2025:** `rp-2024-40`, the 2025 threshold (its quote is not printed in Rev. Proc. 2025-32, a different document)
- **Touches:** `s1.ebl_threshold` (parameter and line)
- **Worklist items:** `s1.ebl_threshold` (line), `s1.ebl_threshold` (parameter)
- **Notes:** The citation moves to `rp-25-32`; step 4 quotes the amount.

### C-PRI-13. Schedule A line 5e: SALT limit and phase-down threshold

- **Kind:** amount (parameter)
- **2026:** `f1040sa` p. 2 (draft): "Enter the smaller of line 5d or $40,400 ($20,200 if married filing separately)"; "$505,000 ($252,500 if married filing separately)"; `plaw-119-21` p. 99 (final): "in the case of any taxable year beginning in calendar year 2026, $40,400"; "in calendar year 2026, $505,000, and"; "the applicable limitation amount shall be reduced by 30 percent of the excess"; "shall not result in the applicable limitation amount being less than $10,000"
- **2025:** `f1040sa` p. 1: "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately)"; "line 11b is more than $500,000 ($250,000 if married filing separately)"
- **Touches:** `sa.salt_base`, `sa.salt_threshold` (parameters; the 30% rate and $10,000 floor are unchanged); `sa.line5e`, `sa.saltbase`, `sa.saltthreshold`, `sa.saltexcess`, `sa.saltreduction`, `sa.saltremaining`, `sa.saltfloor_applied`, `sa.salthalf`, `sa.saltlimit`, `sa.mfs`
- **Worklist items:** `sa.line5e` (its quote "Enter the smaller of line 5d or $40,000 ($20,000 if married filing separately)" is not printed in 2026)
- **Notes:** The amounts are final by statute; the Schedule A instructions' SALT worksheet (2026) is not posted.

### C-PRI-14. Schedule A line 8d: mortgage insurance premiums return

- **Kind:** new line or form (rule)
- **2026:** `f1040sa` p. 2 (draft): "8d Mortgage insurance premiums (see instructions)"; "8e Add lines 8a through 8d"; `plaw-119-21` p. 93 (final): "MORTGAGE INSURANCE PREMIUMS" (section 70108, "Clause (iv) of subparagraph (E) shall not apply" in section 163(h)(3)(F))
- **2025:** `f1040sa` p. 1: "d Reserved for future use"; "e Add lines 8a through 8c"
- **Touches:** `sa.line8e` (its quote "e Add lines 8a through 8c" is not printed in 2026), a new line `sa.line8d`; the refusals on `sa.line8b` and `sa.line8c` (their nearby text changed)
- **Worklist items:** `sa.line8e`, `sa.line8b` (refusal), `sa.line8c` (refusal)
- **Notes:** The limits on deductible premiums are in the Schedule A instructions, not posted, and the statute clause it revives is not archived in full. Until then: an input refused when non-zero, or a refusal question.

### C-PRI-15. Schedule A lines 11 to 15: charitable contributions after the 0.5% floor

- **Kind:** rule (definition change) and new lines
- **2026:** `f1040sa` p. 3 (draft): "13 Enter the amount from line 6 of the Charitable Contribution Limitation Worksheet"; "14 Carryover from prior year"; "15 Add lines 13 and 14"; `plaw-119-21` p. 165 (final): "exceeds 0.5 percent of the taxpayer’s contribution base"
- **2026 (statute, final):** `plaw-119-21` p. 165: "Any charitable contribution otherwise allowable (without regard to this subparagraph) as a deduction under this section shall be allowed only to the extent that the aggregate of such contributions exceeds 0.5 percent of the taxpayer’s contribution base"; p. 166: "first, by taking into account charitable con- tributions to which subparagraph (D) applies"; "CARRIED FORWARD ONLY FROM YEARS IN WHICH LIMITATION IS EXCEEDED"; p. 167: "any contribution of cash to an organization described in subparagraph (A) shall be allowed as a deduction under subsection (a) to the extent that the aggregate of such contributions does not exceed the excess of"; "shall apply to taxable years beginning after December 31, 2025"
- **2025:** `f1040sa` p. 1: "13 Carryover from prior year"; "14 Add lines 11 through 13"
- **Touches:** `sa.line11`, `sa.line12` (now inputs to a worksheet, not to the line 14 sum), `sa.line13` (now the carryover becomes line 14), `sa.line14` (its quote "Add lines 11 through 13" is not printed in 2026; the sum becomes line 15 of lines 13 and 14), `sa.charity_limited` (the income-limit refusal question), `sa.line17` (reads the new line 15); the `gift` collection (`gift.deduction`, `gift.allowed`) feeds line 12
- **Worklist items:** `sa.line14`, `sa.line13` (refusal), `sa.line12` (refusal), `gift.deduction`
- **Notes:** The Charitable Contribution Limitation Worksheet is in the 2026 Schedule A instructions, not posted: its six lines, and whether the 0.5% floor is applied on it, have no 2026 IRS source. The statute fixes the floor (final). Adoption: encode the worksheet from the instructions; until they post, the 2026 charitable lines cannot be written. `gift.deduction`'s worklist finding (figures near its citation in `i8283`) is the year shift on a byte-identical document: wording only.
- **Owner decision (2026-11-04):** encode the floor now from the statute (final) and recheck it when the Schedule A instructions post. The proposal (`forms-proposed/sa.yaml`) figures line 13 as lines 11 plus 12 less 0.5% of the contribution base (`sa.gift_floor`, `sa.line13_ws`; new parameter `sa.gift_floor_rate`, 5/1000, `params-2026.proposed.yaml`), with no refusal. Readings recorded as `amb.2026.gift_floor_base` (to enter in `ambiguities/2026.yaml`): the contribution base is Form 1040 line 11b, not less than zero (the 2025 Pub. 526 states the percentage limits against AGI; the statute's own definition, section 170(b)(1)(H), is not in the archived text); the floor is rounded half-up to the cent (`amb.2025.multiplication_subcent`); the carryover (printed line 14) is outside the floor, as the draft's line 15 adds it after line 13. The statute's order of application (i) to (vi) and its carryforward rule matter only when an income limit applies or a carryover exists, which `sa.charity_limited` refuses; its question now says the 0.5% floor is figured by the tool. The 60 percent cash limit of section 170(b)(1)(G), made permanent by the same section (p. 167), is an income limit and stays behind `sa.charity_limited`. Four source-predicted cases: `fixtures-proposed/2026-predicted.json`, `ty2026.sa.gift_floor_*`.

### C-PRI-16. Schedule A line 16 (was 15): casualty losses include state-declared disasters

- **Kind:** rule (definition change) and renumbering
- **2026:** `f1040sa` p. 3 (draft): "Casualty and theft loss(es) from a federally or state-declared disaster"; `plaw-119-21` p. 93 (final): "or a State declared disaster"
- **2025:** `f1040sa` p. 1: "Casualty and theft loss(es) from a federally declared disaster (other than net qualified disaster losses)"
- **Touches:** `sa.line15` (printed 15 becomes 16; held at zero), `sa.unsupported` (the refusal question naming casualty losses; its wording should add state-declared disasters), the refusal `sa.line15`
- **Worklist items:** `sa.line15` (refusal)
- **Notes:** The encoding refuses every casualty loss, so the change is to the refusal's wording and the printed number.

### C-PRI-17. Schedule A line 17 (was 16): other itemized deductions itemized by line; gambling losses at 90%

- **Kind:** rule (definition change) and new lines
- **2026:** `f1040sa` p. 3 (draft): "17a Deductible gambling losses"; "If you have gambling winnings that you reported on Schedule C or Schedule E, check here"; "17z Add lines 17a through 17k"; `plaw-119-21` p. 96 (final): "shall be equal to 90 percent of the amount of such losses during such taxable year"; p. 94 (final): "the deductions allowed by section 162 for educator expenses"
- **2025:** `f1040sa` p. 1: "16 Other—from list in instructions. List type and amount:"
- **Touches:** `sa.line16`, `sa.line16_gambling`, `sa.gambling_losses` (the 90% rule changes the computation: the deduction is 90% of losses, limited to gains), `sa.line17` (reads line 17z); the refusal `sa.line16`; `amb.2025.gambling_losses` (whose reading may need revisiting under the new rule)
- **Worklist items:** `sa.line16` (line), `sa.line16` (refusal)
- **Notes:** Lines 17b to 17k are the 2025 "list in instructions" items now printed (17k, educator expenses not on Schedule 1, is new by statute section 70110); they stay refused unless encoded. Whether the 90% applies before the limit to winnings, and how winnings reported on Schedule C or E (the new checkbox) enter, is for the 2026 instructions (not posted); the statute's order is "(A) 90 percent ... and (B) ... only to the extent of the gains".
- **Correction (verification):** the order is settled by the archived drafts: `i1040se` p. 2 (draft), "You must apply the 90% limitation first then apply the gambling winnings limitation", and `i1040sc` p. 2 (draft), the lesser of 90% of losses or winnings. Only how winnings reported on Schedule C or E enter stays open (`changes.verification.md`).

### C-PRI-18. Schedule A line 18: total itemized deductions may be limited (2/37 rule)

- **Kind:** rule (definition change) and new line
- **2026:** `f1040sa` p. 3 (draft): "minus the amounts on lines 13a and 13b of that form, more than $384,350?"; "Itemized Deductions Worksheet in the instructions"; "Add the amounts in far-right column for lines 4 through 17z"; `plaw-119-21` p. 94 (final): "shall be reduced by 2⁄37 of the lesser of"
- **2025:** `f1040sa` p. 1: "Add the amounts in the far right column for lines 4 through 16"
- **Touches:** `sa.line17` (becomes line 18; its quote is not printed in 2026), `sa.itemizes`, `sa.deduction`, the refusal `sa.line17`; a new worksheet; the elect-to-itemize box moves from 18 to 19 (`sa.elect_itemize`)
- **Worklist items:** `sa.line17` (line), `sa.line17` (refusal), `sa.itemizes`
- **Notes:** The Itemized Deductions Worksheet is in the Schedule A instructions, not posted. The statute keys the reduction to "the dollar amount at which the 37 percent rate bracket under section 1 begins with respect to the taxpayer"; the draft's single screening figure ($384,350) is not explained on the form; it equals the start of the 37% bracket for married filing separately in the 2026 rate tables (`rp-25-32` p. 12: "Over $384,350"), the lowest of the four, so it screens every filer whose limitation could apply. The QBI deduction is figured without regard to section 68 (`plaw-119-21` section 70111(b); C-SCHED-33), so a screen on Form 1040 line 15 avoids a cycle through Schedule A. Until the worksheet posts: refuse when line 11b less lines 13a and 13b exceeds the screening figure.

### C-PRI-19. Schedule A: other lines reworded, quote unchanged

- **Kind:** wording only
- **2026:** `f1040sa` p. 2 (draft): "Subtract line 3 from line 1. If line 3 is more than line 1, enter -0-"
- **2025:** `f1040sa` p. 1: the same sentence
- **Touches:** `sa.line4`; the refusals `sa.line6`, `sa.line16` and `sa.line17` read nearby sentences that moved
- **Worklist items:** `sa.line4`, `sa.line6` (refusal)
- **Notes:** The year diff reports the quote as printed in 2025 only; it is printed on 2026 p. 2 (a draft-page layout difference). Relocate the page only.

### C-PRI-20. Form 8889: 2026 HSA contribution limits

- **Kind:** amount (parameter)
- **2026:** `f8889` p. 2 (draft): "enter $4,400 ($8,750 for family coverage)"; `rp-25-19` p. 2 (final): "is $4,400"; "is $8,750"
- **2025:** `f8889` p. 1: "enter $4,300 ($8,550 for family coverage)"
- **Touches:** `hsa.self_only`, `hsa.family`, `hsa.self_only_55`, `hsa.family_55` (parameters); `f8889.self_amount`, `f8889.family_amount`, `f8889.age55_line3`, `f8889.age55_unmarried`, `f8889.married_family`, `f8889.line7_applies`, `f8889.line17a` (their quotes print the 2025 dollar amounts)
- **Worklist items:** `hsa.family`, `hsa.family_55`, `hsa.self_only`, `hsa.self_only_55`, `f8889.self_amount`, `f8889.family_amount`, `f8889.age55_line3`, `f8889.age55_unmarried`, `f8889.married_family`, `f8889.line7_applies`, `f8889.line17a`
- **Notes:** The age-55 additional contribution ($1,000) is statutory and checked in step 4. The line quotes are requoted from the 2026 instructions (draft) at adoption.

### C-PRI-21. Form 8889: Schedule 2 line references renumbered

- **Kind:** wording only (cross-reference)
- **2026:** `f8889` p. 2 (draft): "1040), Part II, line 13c"; "1040), Part II, line 13d"
- **2025:** `f8889` p. 1: "1040), Part II, line 17c"; "1040), Part II, line 17d"
- **Touches:** `f8889.line17b` (label and cite); `s2.line17c` (Schedule 2's own renumbering is in the SCHED section); Form 8889 Part III (line 21) is not encoded
- **Worklist items:** `f8889.rollover` (its nearby text includes the moved lines)
- **Notes:** Follow Schedule 2's renumbering.
- **Correction (verification):** `f8889.rollover` belongs to C-PRI-23 only (the coverage table already says so) (`changes.verification.md`).

### C-PRI-22. HSA eligibility: bronze and catastrophic plans and direct primary care

- **Kind:** rule (definition change) (draft)
- **2026:** `i8889` p. 2 (draft): "Expansions to HSA eligibility"; "Bronze and Catastrophic Plans Treated as HDHPs"; "Direct Primary Care Service Arrangements"
- **2025:** no counterpart
- **Touches:** the help text of the HDHP coverage questions (the `hsa_coverage` enum and the monthly coverage questions in `person`, read by `f8889.line3` and the Line 3 Limitation Chart lines)
- **Worklist items:** none (What's New)
- **Notes:** The encoding asks the filer for HDHP coverage; the computation does not change, but the definition shown with the question must say that bronze and catastrophic plans count and that a direct primary care arrangement does not end eligibility. Notice 2026-5 (cited) is not archived; archive it at adoption if a question's help quotes it.
- **Correction (verification):** the telehealth item (What's New 1) is no change from 2025 (`plaw-119-21` p. 255, section 71306, "plan years beginning after December 31, 2024"); not encoded (`changes.verification.md`).

### C-PRI-23. HSA qualified medical expenses: definition rewritten

- **Kind:** wording only for the computation; help text changes (draft)
- **2026:** `i8889` p. 3 (draft): "including amounts paid for menstrual care products"; "5. Any direct primary care service arrangement"
- **2025:** `i8889` p. 2: "You cannot treat insurance premiums as qualified medical expenses unless the premiums are for"
- **Touches:** `f8889.medical` (an amount the filer states; its seven quotes are no longer printed), `f8889.rollover` (nearby text)
- **Worklist items:** `f8889.medical`, `f8889.rollover`
- **Notes:** Requote the help text from the 2026 list ("Insurance may not be purchased from an HSA, except for the following") at adoption; nothing computed changes.

### C-PRI-24. Form W-2 (final): new box 12 codes TP, TT and TA; box 14 split into 14a and 14b

- **Kind:** new line or form (inputs)
- **2026:** `iw2w3` p. 23 (final): "Code TP—Total amount of cash tips reported to the employer"; "Code TT—Total amount of qualified overtime compensation"; "Code TA—Employer contributions under a section 128 Trump account"; p. 1: "Box 14 has been split into box 14a and box 14b"
- **2025:** no counterpart (box 12 codes end with Z in the 2025 list; box 14 "Other")
- **Touches:** `w2` (new inputs per Form W-2: code TP, code TT, the box 14b occupation code); the Schedule 1-A tip and overtime entries (`tipjob`, `otjob`; the enum `overtime_method`, whose `employer_reported` value cites "Form W-2 box 14", SCHED section); code TA has no reader (a Trump account contribution is excluded from wages)
- **Worklist items:** none
- **Notes:** For 2026 the employer reports qualified tips and overtime in box 12; the Schedule 1-A instructions (in the Form 1040 instructions, not posted) say how a filer uses them. Ripple: a new input reaches every fixture, the interview bank, `generate.ts`, `generate_cases.py` and the input contracts (`handoffs/HANDOFF-HARDENING-1.md`).

### C-PRI-25. Social security wage base: $184,500

- **Kind:** amount (parameter)
- **2026:** `p15` p. 2 (final): "The social security wage base limit is $184,500"
- **2025:** the 2025 maximum withholding, `w2.over` ("Did this employer withhold more than $10,918.20?")
- **Touches:** `w2.over` (label carries 6.2% of the wage base), the excess social security credit parameters, and Schedule SE (BUS section)
- **Worklist items:** none
- **Notes:** Step 4 records the parameter; the 2026 maximum is 6.2% of $184,500, written as a quoted amount only if a 2026 source prints it.
- **Correction (verification):** touches also `ss.base`, `ss.limit` and `person.excess` (label "Withholding above $10,918.20"). The final `iw2w3` p. 19 prints the 2026 maximum: "For 2026, the amount should not exceed $11,439 ($184,500 × 6.2%)"; step 4 uses it for `ss.limit` (`changes.verification.md`).

### C-PRI-26. Schedules B and D, Form 8949: no change beyond wording

- **Kind:** wording only
- **2026:** `f1040sb` p. 2 (draft): "list the name(s) of the foreign country(ies)"; `f1040sd` and `f8949` (drafts): only the creation date differs from 2025 once years are moved
- **2025:** `f1040sb` p. 1: "list the name(s) of the foreign country(-ies)"
- **Touches:** none computed (`sb`, `interest`, `div`, `sd`, `sales` labels)
- **Worklist items:** none of kind (a); their items wait on the 2026 Schedule D and Form 8949 instructions (kind (b))
- **Notes:** The forms carry the same lines; the instructions decide.

### C-PRI-27. Earned income credit amounts

- **Kind:** amount (parameter)
- **2026:** `rp-25-32` section 4.06 (final); values in step 4
- **2025:** `rp-2024-40` section 2.06
- **Touches:** `eic.earned_amount0` to `eic.earned_amount3`, `eic.maximum0` to `eic.maximum3`; the EIC tables (`tables/2025/eic_*.yaml`) wait on the 2026 Form 1040 instructions
- **Worklist items:** `eic.earned_amount0`, `eic.earned_amount1`, `eic.earned_amount2`, `eic.earned_amount3`, `eic.maximum0`, `eic.maximum1`, `eic.maximum2`, `eic.maximum3`
- **Notes:** Proposed in step 4.

### C-PRI-28. Enumerations whose citations moved

- **Kind:** wording only, except `early_exception` (rule)
- **2026:** `i2441` p. 4 (draft): "enter their SSN or individual taxpayer identification number (ITIN)", "LAFCP", "See Attached Statement" (Form 2441 Part I now uses lines 1a to 1e, CRED section); `i5329` p. 5 (draft): "In the space provided, enter the applicable exception number (01–24). If more than one exception applies, enter 99."; `f8962` p. 2 (draft): "Check the appropriate box for the federal poverty table used"
- **2025:** `i2441` p. 3: "If the care provider is an individual, enter their SSN or individual taxpayer identification number (ITIN)"; `i5329` p. 5: "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99."
- **Touches:** enums `dc_tin_kind` (requote and relocate), `early_exception` (a new value `e24`: on `i5329` p. 6 (draft) exception 24 is "Distributions for qualified long-term care distributions"; PEOP section), `ptc_fpl_table` (relocate: the quote is printed on 2026 p. 2 of a draft), `retirement_account` (figures near the citation in `f1099r`; wording)
- **Worklist items:** `dc_tin_kind`, `early_exception`, `ptc_fpl_table`, `retirement_account`
- **Notes:** `early_exception` gains a value: every reader of the enum (Form 5329 line 2 lines, the interview) must answer it.
- **Correction (verification):** `retirement_account` is a rule change, not wording: `f1099r` p. 9 (final), "Box 7b. If the IRA/SEP/SIMPLE box is checked, you’ve received a traditional IRA (other than a Trump account), SEP, or SIMPLE distribution"; see C-PEOP-04 and C-PEOP-11 (`changes.verification.md`).

### C-PRI-29. Net investment income MAGI sentences: printed on the same page

- **Kind:** wording only
- **2026:** `i8960` p. 22 (draft): "Regulations section 1.1411-10(e)(1)"; "section 959(d) or 1293(c)"; "excess distributions derived from a PFIC"
- **2025:** `i8960` p. 22: "If you exclude amounts under section 911 or own certain CFCs or PFICs, your MAGI is your AGI as modified by certain rules described in Regulations section 1.1411-10(e)(1)."
- **Touches:** `scope.other_line16` (its three quotes)
- **Worklist items:** `scope.other_line16`
- **Notes:** The sentences are present on 2026 p. 22 with surrounding words changed; requote from the 2026 page (SCHED section reads Form 8960).

### Worklist coverage

| item id | entry |
|---|---|
| `f1040.line13b` | C-PRI-02 |
| `f1040.line1a` (refusal) | C-PRI-08 |
| `s1.cod_figured` | C-PRI-11 |
| `s1.ebl_threshold` (line) | C-PRI-12 |
| `s1.line1` | C-PRI-11 |
| `s1.line11` | C-PRI-11 |
| `s1.line18` | C-PRI-11 |
| `s1.line19a` | C-PRI-11 |
| `s1.line20` | C-PRI-11 |
| `s1.line24a` | C-PRI-11 |
| `s1.line2a` | C-PRI-11 |
| `s1.line8b` | C-PRI-11 |
| `s1.line8c` | C-PRI-11 |
| `s1.line8f` | C-PRI-11 |
| `s1.line8g` | C-PRI-11 |
| `s1.ebl_threshold` (parameter) | C-PRI-12 |
| `sa.itemizes` | C-PRI-18 |
| `sa.line14` | C-PRI-15 |
| `sa.line16` | C-PRI-17 |
| `sa.line17` | C-PRI-18 |
| `sa.line4` | C-PRI-19 |
| `sa.line5e` | C-PRI-13 |
| `sa.line8e` | C-PRI-14 |
| `sa.line12` (refusal) | C-PRI-15 |
| `sa.line13` (refusal) | C-PRI-15 |
| `sa.line15` (refusal) | C-PRI-16 |
| `sa.line16` (refusal) | C-PRI-17 |
| `sa.line17` (refusal) | C-PRI-18 |
| `sa.line6` (refusal) | C-PRI-19 |
| `sa.line8b` (refusal) | C-PRI-14 |
| `sa.line8c` (refusal) | C-PRI-14 |
| `f8889.age55_line3` | C-PRI-20 |
| `f8889.age55_unmarried` | C-PRI-20 |
| `f8889.family_amount` | C-PRI-20 |
| `f8889.line17a` | C-PRI-20 |
| `f8889.line7_applies` | C-PRI-20 |
| `f8889.married_family` | C-PRI-20 |
| `f8889.medical` | C-PRI-23 |
| `f8889.rollover` | C-PRI-23 |
| `f8889.self_amount` | C-PRI-20 |
| `hsa.family` | C-PRI-20 |
| `hsa.family_55` | C-PRI-20 |
| `hsa.self_only` | C-PRI-20 |
| `hsa.self_only_55` | C-PRI-20 |
| `eic.earned_amount0` | C-PRI-27 |
| `eic.earned_amount1` | C-PRI-27 |
| `eic.earned_amount2` | C-PRI-27 |
| `eic.earned_amount3` | C-PRI-27 |
| `eic.maximum0` | C-PRI-27 |
| `eic.maximum1` | C-PRI-27 |
| `eic.maximum2` | C-PRI-27 |
| `eic.maximum3` | C-PRI-27 |
| `gift.deduction` | C-PRI-15 |
| `dc_tin_kind` | C-PRI-28 |
| `early_exception` | C-PRI-28 |
| `person_role` | C-PRI-08 |
| `ptc_fpl_table` | C-PRI-28 |
| `retirement_account` | C-PRI-28 |
| `scope.other_line16` | C-PRI-29 |
| `scope.ready` (line) | C-PRI-02 |
| `scope.schedule1` | C-PRI-11 |
| `scope.ready` (refusal) | C-PRI-02 |

## Schedules 1-A, 2, 3 and 8812; Forms 8959, 8960, 8995, 8995-A, 4952 and 1116

I read the 2026 archive texts of the 14 documents in this group: Schedules 1-A, 2, 3 and 8812 and the
Schedule 8812 instructions; Forms 8959, 8960, 8995, 8995-A and 4952; and the instructions for Forms 8959,
8960, 8995 and 1116. I compared each with its 2025 counterpart. Where a worklist item rests on another
document I also read that document (i5329, i1040sc, p4681, f5329 and f8889 for 2026). All of these 2026
texts are IRS drafts except Form 4952, which is the final 2026 edition. The group file has 71 worklist
items. They come down to 39 entries.

Notable points:
- **Schedule 1-A is laid out again.** Lines 4–38 become lines 4–44. Tips and overtime are now entered per
  employer, from new Form W-2 box 12 codes "TP" and "TT". The total now goes to Form 1040 line 13a
  (in 2025 it went to line 13b).
- **Schedule 2 is renumbered from line 4 on.** Additional Medicare Tax is split between Schedule 2 lines 11
  and 17b. Form 5329 taxes are split between lines 5 and 18.
- **Form 8959 is reordered** so that tax on wages and RRTA compensation (line 12) is reported apart from
  tax on self-employment income (line 18).
- **The Form 8995 thresholds rise.** A separate married-filing-separately figure appears, and there is a
  new $400 minimum deduction.
- **Form 8960 gets a section 68 limitation worksheet** for lines 9 and 10.
- **Gaps in the archive.** No 2026 edition of i1040gi (the Form 1040 instructions, which also carry the
  Schedule 1-A, 2 and 3 instructions) or of i8995a is archived. So the 2026 rules behind Schedule 1-A
  Parts II–V, Schedule 2 lines 1a and 5, Schedule 3 lines 9–10 and the CTC dependent tests can be checked
  only against the face of the forms.

### What's New and Reminders accounted for

| document | item (quoted heading or first words) | entry or "not encoded: reason" |
|---|---|---|
| f1040s1a | Part II caution "Fill out Part II only if you received qualified tips" | C-SCHED-01, C-SCHED-03 |
| f1040s1a | Part III caution "Fill out Part III only if you received qualified overtime compensation" | C-SCHED-05 |
| f1040s1a | Part IV caution "Fill out Part IV only if you ... paid or accrued qualified passenger vehicle loan interest" | C-SCHED-06 |
| f1040s1a | Part V caution "You and/or your spouse must have a valid social security number" | C-SCHED-08 (unchanged text) |
| f1040s2 | (no What's New, Reminders or caution printed on the form) | n/a |
| f1040s3 | (none printed) | n/a |
| f1040s8812 | Caution after line 6 "Do not include yourself, your spouse, or anyone who is not a U.S. citizen" | C-SCHED-24 (unchanged text) |
| f1040s8812 | Part II-A caution "If you file Form 2555, you cannot claim the additional child tax credit" | not encoded: unchanged; Form 2555 is refused through sa.excluded_income (s8812.line2b) |
| i1040s8812 | Future Developments | not encoded: no content beyond the IRS.gov link |
| i1040s8812 | Reminders "CTC amount. The maximum amount of CTC for each qualifying child is $2,200" | C-SCHED-25 (amount unchanged from 2025; ctc.per_child) |
| i1040s8812 | Reminders "ACTC amount ... $1,700" | C-SCHED-25 (unchanged; actc.per_child) |
| i1040s8812 | Reminders "Valid social security number (SSN) required to claim the child tax credit" | C-SCHED-19 |
| i1040s8812 | Reminders "Trump accounts and Form 4547" | not encoded: a Form 4547 election, not a Schedule 8812 computation (in 2025 it was a What's New item) |
| i1040s8812 | Reminders "Delayed refund for returns claiming ACTC" (mid-February 2027) | not encoded: refund timing only |
| i1040s8812 | Reminders "Abbreviations" | not encoded: definitions only |
| i1040s8812 | (body, new) "Limits on the refund of the ACTC ... See the instructions for Schedule 3-A" | C-SCHED-26 |
| f8959 | (none printed) | n/a |
| i8959 | Future Developments | not encoded: link only |
| i8959 | What's New "Changes to Form 8959 for 2026" | C-SCHED-13 |
| i8959 | Reminders "Missing or incorrect Form W-2" (February 1, 2027) | not encoded: filing mechanics; date only |
| i8959 | Reminders "Forms W-2 of U.S. territories" | not encoded: unchanged; territory W-2s are outside the slice (scope.other_income) |
| f8960 | (none printed) | n/a |
| i8960 | Future Developments | not encoded: link only |
| i8960 | What's New "Overall limitation on itemized deductions in 2026" (Lines 9 and 10 Section 68 Limitation Worksheet) | C-SCHED-27 |
| i8960 | Reminders "Digital assets" | not encoded: unchanged; no digital-asset income path in the slice |
| i8960 | Reminders "Schedule SE (Form 1040) income" | not encoded: unchanged statement of the section 1411(c)(6) exclusion; business income on Form 8960 is refused through f8960.unsupported |
| i8960 | Reminders "Trade or business income subject to net investment income tax (NIIT)" (line 4a) | not encoded: f8960.line4a is zero unless refused through f8960.unsupported |
| f8995 | (none printed) | n/a |
| i8995 | Future Developments | not encoded: link only |
| i8995 | What's New "Taxable income limitation adjustments" (inflation; "computed without regard to section 68") | C-SCHED-30, C-SCHED-33 |
| i8995 | What's New "Minimum deduction for active qualified business income" | C-SCHED-31 |
| i8995 | What's New "Amounts deductible as a qualified tip" | C-SCHED-35 |
| i8995 | What's New "Excludable tip income" | C-SCHED-35 |
| i8995 | What's New "Form has been revised. Lines 15, 16, and 20 have been added" | C-SCHED-31 |
| f8995a | (none printed; no 2026 i8995a archived) | C-SCHED-32, C-SCHED-34 |
| f4952 | Future Developments | not encoded: link only |
| f4952 | Caution "Don't include any miscellaneous itemized deductions, which aren't allowed deductions in tax years beginning after 2017" | C-SCHED-36 |
| i1116 | Future Developments | not encoded: link only |
| i1116 | What's New "Form 1116, Part I, line i" (section 904(b)(6)) | C-SCHED-38 (not encoded) |
| i1116 | What's New "Itemized deduction limit" | C-SCHED-38 (not encoded) |
| i1116 | What's New "Form 1116, Part II" (PTEP columns, reformatted) | C-SCHED-38 (not encoded) |
| i1116 | What's New "Section 951A" (NCTI replaces GILTI) | C-SCHED-38 (not encoded) |
| i1116 | Reminders "Treatment of enhanced deduction for seniors in figuring the foreign tax credit limitation" (Schedule 1-A line 43) | C-SCHED-38 (not encoded) |
| i1116 | Reminders "Final foreign tax credit regulations" | not encoded: unchanged; creditability is a supplied answer (ftc.eligible) |
| i1116 | Reminders "Alternative minimum tax (AMT)" | not encoded: AMT is refused through s2.amt |

### C-SCHED-01. Schedule 1-A renumbered; total moves to Form 1040 line 13a

- **Kind:** new line or form
- **2026:** `f1040s1a` p. 2 (draft): "Subtract line 11 from line 10. If zero or less, enter the amount from line 9 on line 15" "Multiply line 13 by $100" "Qualified tips deduction. Subtract line 14 from line 9. If zero or less, enter -0-"; p. 3: "Subtract line 23 from line 22. If zero or less, enter the amount from line 21 on line 27" "Multiply line 25 by $100" "Qualified overtime compensation deduction. Subtract line 26 from line 21. If zero or less, enter -0-"; p. 4: "Subtract line 32 from line 31. If zero or less, enter the amount from line 30 on line 36" "Multiply line 34 by $200" "Subtract line 38 from line 37. If zero or less, enter $6,000 on line 41" "Subtract line 40 from $6,000. If zero or less, enter -0-" "Add lines 15, 27, 36, and 43. Enter here and on Form 1040, 1040-SR, or 1040-NR, line 13a"
- **2025:** `f1040s1a` p. 1: "Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13" "Multiply line 11 by $100" "Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-" "Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21" "Multiply line 19 by $100" "Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less, enter -0-"; p. 2: "Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30" "Multiply line 28 by $200" "Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35" "Subtract line 34 from $6,000. If zero or less, enter -0-" "Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form 1040-NR, line 13c"
- **Touches:** s1a.line6 … s1a.line38 (every printed line from 6 on, and their helpers): s1a.line10_pos, s1a.line12_calc, s1a.line13, s1a.line18_pos, s1a.line20_calc, s1a.line21, s1a.line27_pos, s1a.line29_calc, s1a.line33_over, s1a.line33_pos, s1a.line35_calc, s1a.line38; f1040.line13b (reader of s1a.line38)
- **Worklist items:** s1a.line10_pos, s1a.line12_calc, s1a.line13, s1a.line18_pos, s1a.line20_calc, s1a.line21, s1a.line27_pos, s1a.line29_calc, s1a.line33_over, s1a.line33_pos, s1a.line35_calc
- **Notes:**
  - **Renumbering only, except for Parts II–III.** The printed numbers are renumbered and the formulas are
    otherwise the same, apart from the Part II–III input lines (C-SCHED-03 to 05). Old to new: 6→8, 7→9,
    8→10, 9→11, 10→12, 11→13, 12→14, 13→15; 15→21 … 21→27; 22→28 … 30→36; 31→37 … 37→43; 38→44.
  - **The total now feeds Form 1040 line 13a.** The 2026 Form 1040 draft prints "13a Additional deductions
    from Schedule 1-A, line 44" (`f1040` p. 3). The adoption must rename the line ids, re-cite them, and
    point the Form 1040 reader at line 13a; that change belongs to the Form 1040 section.
  - **Instructions not archived.** The line 13 and line 21 citations to i1040gi pp. 101 and 106 cannot be
    checked, because no 2026 i1040gi is archived.

### C-SCHED-02. Schedule 1-A dollar limits and rates unchanged (cited at new line numbers)

- **Kind:** wording only
- **2026:** `f1040s1a` p. 2 (draft): "Enter the smaller of the amount on line 8 or $25,000" "Enter $150,000 ($300,000 if married filing jointly)"; p. 3: "Enter the smaller of the amount on line 20 or $12,500 ($25,000 if married filing jointly)"; p. 4: "Enter the smaller of the amount on line 29 or $10,000" "Enter $100,000 ($200,000 if married filing jointly)" "Enter $75,000 ($150,000 if married filing jointly)" "Multiply line 39 by 6% (0.06)" "Subtract line 40 from $6,000"
- **2025:** `f1040s1a` p. 1: "Enter the smaller of the amount on line 6 or $25,000" "Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)"; p. 2: "Enter the smaller of the amount on line 23 or $10,000" "Multiply line 33 by 6% (0.06)" "Subtract line 34 from $6,000"
- **Touches:** params s1a.tips_max, s1a.base_other, s1a.base_joint, s1a.ot_max_other, s1a.ot_max_joint, s1a.car_max, s1a.car_base_other, s1a.car_base_joint, s1a.senior_amount, s1a.senior_base_other, s1a.senior_base_joint, s1a.senior_rate, s1a.hundred_per_thousand, s1a.two_hundred_per_thousand
- **Worklist items:** s1a.tips_max, s1a.ot_max_joint, s1a.ot_max_other, s1a.car_max, s1a.senior_amount, s1a.senior_rate
- **Notes:**
  - **What the finding meant.** The "quote printed in 2025 only" findings arise because the line numbers
    inside the quotes changed. Every figure is printed unchanged in the 2026 draft.
  - **What the adoption does.** Keep the 2025 values and re-cite them at 2026 lines 9, 11, 21, 23, 30, 32,
    38, 39–41, 13–14, 25–26 and 34–35.

### C-SCHED-03. Schedule 1-A Part II: employee tips entered per employer from W-2 box 12 code TP

- **Kind:** new line or form
- **2026:** `f1040s1a` p. 2 (draft): "4 Qualified tips received as an employee." "(iii) Qualified tips included in Form W-2, box 12, code “TP” (see instructions)" "(iv) Qualified tips included in Form 4137, line 1, column (c). If Form 4137 is not filed, enter -0-." "(v) Enter the larger of column (iii) or column (iv)." "Add lines 4a through 4e, column (v)"
- **2025:** `f1040s1a` p. 1: "Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, box 5 is more than $176,100 or you received tips that are not subject to social security and Medicare taxes" "If you only received qualified tips as an employee with respect to employment with one employer, enter the larger of line 4a or line 4b"
- **Touches:** s1a.line4a, s1a.line4a_calc, s1a.line4b, s1a.line4b_calc, s1a.line4c, s1a.line4c_calc, s1a.line4c_one, s1a.tip_employers, s1a.tip_total, s1a.tip_reported, s1a.tip_multi, tipjob.amount, tipjob.col_c, tipjob.col_d, tipjob.mixed
- **Worklist items:** s1a.line4c_one
- **Notes:**
  - **What changed on the form.** Lines 4a–4c (W-2 box 7, Form 4137, and "larger of" or a worksheet) are
    replaced by five employer rows 4a–4e, with columns (i)–(v) and a total on line 5. The source is now
    W-2 box 12 code "TP", not box 7, and the $176,100 box 5 test is gone from the form.
  - **What the adoption does.** Make tipjob the row collection, with column (iii) and column (v) =
    max((iii), (iv)), and drop s1a.line4c_one and the more-than-one-employer worksheet path.
  - **Open question.** How code "TP" amounts are determined, and what "see instructions" says, is in the
    2026 i1040gi, which is not archived.
  - **Refusal.** Form 4137 (column (iv)) stays refused, through s1a.line4b_calc.

### C-SCHED-04. Schedule 1-A Part II: trade-or-business tips entered per business with Forms 1099 columns

- **Kind:** new line or form
- **2026:** `f1040s1a` p. 2 (draft): "6 Qualified tips received in the course of a trade or business." "(xiii) Enter the smaller of column (v) or column (xii)." "Add lines 6a through 6e, column (xiii)" "Add lines 5 and 7"
- **2025:** `f1040s1a` p. 1: "Qualified tip amount included in Form 1099-NEC, box 1; Form 1099-MISC, box 3; or Form 1099-K, box 1a. Do not enter more than the net profit from the trade or business."
- **Touches:** s1a.line5, s1a.line5_calc, s1a.line6, s1a.line6_calc; refusal gate s1.sc_1a (on s1a.line13)
- **Worklist items:** none
- **Notes:**
  - **What changed on the form.** 2025 line 5 becomes rows 6a–6e with 13 columns: the business net profit
    less other allocable deductions, capped at the tips reported on up to three Forms 1099. The form cites
    Form 1099-NEC box 1(b), 1099-MISC box 13(a) and 1099-K box 1(c). Line 7 is the total, and line 8 adds
    lines 5 and 7.
  - **Effect on the encoding.** Tips in a trade or business remain refused through s1.sc_1a. Only the
    line numbers and the refusal's form text change.

### C-SCHED-05. Schedule 1-A Part III: overtime entered per employer from W-2 box 12 code TT, and per payer from Forms 1099

- **Kind:** new line or form
- **2026:** `f1040s1a` p. 3 (draft): "16 Qualified overtime compensation reported on Form W-2." "(iii) Qualified overtime compensation included in Form W-2, box 12, code “TT” (see instructions)" "Add lines 16a through 16e, column (iii)" "18 Qualified overtime compensation reported on Form 1099-MISC or 1099-NEC." "Add lines 18a through 18e, column (iv)" "Add lines 17 and 19"
- **2025:** `f1040s1a` p. 1: "Qualified overtime compensation included in Form W-2, box 1. If you received qualified overtime compensation not reported on Form W-2, box 1, see instructions" "Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3 (see instructions)" "Add lines 14a and 14b"
- **Touches:** s1a.line14a, s1a.line14a_calc, s1a.line14b, s1a.line14b_calc, s1a.line14c, s1a.line14c_calc, s1a.line15 (now 21); otjob.col_b, otjob.method, otjob.statement, otjob.figured, otjob.refused, otjob.by_third, otjob.by_half, otjob.by_quarter; params s1a.ot_third, s1a.ot_half, s1a.ot_quarter
- **Worklist items:** none
- **Notes:**
  - **What changed on the form.** Lines 14a–14c become employer rows 16a–16e (W-2 box 12 code "TT") with
    total line 17, payer rows 18a–18e (Forms 1099) with total line 19, and line 20 = 17 + 19.
  - **New 1099 boxes.** In the layout text, the column (iv) header for line 18 names Form 1099-NEC box 1d
    and Form 1099-MISC box 14, in place of the 2025 boxes 1 and 3.
  - **Open question for otjob.** The otjob methods were for overtime that is not separately reported. With
    a W-2 code "TT", the adoption must decide whether those methods (from the 2025 i1040gi and n-25-69)
    survive for 2026. The 2026 i1040gi is not archived, so the archive cannot settle this.
  - **Refusal.** Line 18 stays refused through s1.sc_1a (refusal on s1a.line13 for lines 5 and 14b).

### C-SCHED-06. Schedule 1-A Part IV: Form 1098-VLI named; original-use and final-assembly questions per VIN

- **Kind:** new line or form
- **2026:** `f1040s1a` p. 4 (draft): "Certain vehicle loan interest paid in 2026 should be reported to you on Form 1098-VLI, box 1." "Did the original use of this vehicle start with you, or your spouse if married filing jointly (a used vehicle does not qualify)?" "Did final assembly of this vehicle occur within the United States (see instructions for information on how to determine final assembly)?"
- **2025:** `f1040s1a` p. 2: "Column (iii) is the total QPVLI paid in 2025 less the amounts reported in column (ii). See instructions."
- **Touches:** carloan.requirements, carloan.vehicle, carloan.eligible, carloan.interest, carloan.col_iii, s1a.line23_total
- **Worklist items:** none
- **Notes:**
  - **What changed on the form.** Line 22 becomes line 28 and now prints Yes/No questions (1) and (2) for
    each VIN. carloan.vehicle and carloan.requirements already ask about eligibility, so each 28a/28b
    question can be displayed from them. The adoption must check that both conditions are asked separately.
  - **New information return.** Form 1098-VLI box 1 can be named as the usual source for carloan.interest.

### C-SCHED-07. Schedule C interest on a Schedule 1-A vehicle loan: rule restated under new Schedule C line 16b

- **Kind:** wording only
- **2026:** `i1040sc` p. 9 (draft): "Deduct only the business-use portion of the vehicle loan interest on Schedule C (Form 1040)." "If you claim a deduction on Schedule 1-A (Form 1040) for vehicle loan interest, then you can’t claim a deduction for that same interest on Schedule C."; p. 2: "New Line 16b, Vehicle loan interest. Use line 16b to report the business-use portion of your vehicle loan interest."
- **2025:** `i1040sc` p. 6: "If you use your vehicle for both business and personal" ... "then you can’t claim a deduction for that same interest on Schedule C."
- **Touches:** carloan.col_ii_input, carloan.sc_interest, carloan.col_ii
- **Worklist items:** carloan.col_ii_input
- **Notes:**
  - **What changed.** The rule is the same; its Line 9 caution moved to the new line 16b text. Re-cite
    `i1040sc` p. 9.
  - **Open question.** Schedule C line 16b is a Schedule C change and belongs to that section. Whether
    carloan.col_ii_input should read the 16b vehicle interest is for that adoption.
  - **Instructions not archived.** The i1040gi p. 110 column (ii) citation cannot be checked.

### C-SCHED-08. Schedule 1-A Part V: birth-date cutoff moves to January 2, 1962

- **Kind:** wording only
- **2026:** `f1040s1a` p. 4 (draft): "If you have a valid social security number (see instructions) and were born before January 2, 1962," "your spouse was born before January 2, 1962, enter the amount from line 41"
- **2025:** `f1040s1a` p. 2: "If you have a valid social security number (see instructions) and were born before January 2, 1961," "your spouse was born before January 2, 1961, enter the amount from line 35"
- **Touches:** s1a.line36a, s1a.line36b, s1a.line36a_senior, s1a.line36b_senior, s1a.senior_count, s1a.senior_any, s1a.spouse_senior, s1a.spouse_senior_count, s1a.died_before_65, s1a.spouse_died_before_65, s1a.senior_decedent, s1a.spouse_senior_decedent
- **Worklist items:** s1a.line36b
- **Notes:**
  - **What changes in the encoding.** The test stays "age 65 by the end of the year" (person.age65), so
    no computation changes. The dates hardcoded in labels move by one year, and lines 36a/36b/37 become
    42a/42b/43.
  - **Decedent window.** The decedent window (2025 i1040gi p. 110, "Death of a taxpayer in 2025") has no
    archived 2026 text. Its 2026 dates cannot be quoted, so the adoption must wait for the 2026 i1040gi.

### C-SCHED-09. Schedule 1-A captions and Part III caution (wording)

- **Kind:** wording only
- **2026:** `f1040s1a` p. 2 (draft): "These tips must have been received in an occupation listed at www.irs.gov/TippedOccupations."; p. 3: "See instructions to learn more about what is qualified overtime compensation."
- **2025:** `f1040s1a` p. 1: "These tips must have been received in an occupation listed at IRS.gov/TippedOccupations."
- **Touches:** none (caption text only; s1a.part2 and s1a.part3 cite i1040gi)
- **Worklist items:** none (context for the s1a items in C-SCHED-01)
- **Notes:** None.

### C-SCHED-10. Schedule 2 laid out again: Part II split into Sections A–C; line 21 formula changes

- **Kind:** new line or form
- **2026:** `f1040s2` p. 2 (draft): "4 Self-employment tax. Attach Schedule SE." "6 Net investment income tax. Attach Form 8960" "13c Additional tax on HSA distributions. Attach Form 8889"; p. 3: "14 Total additional income taxes. Add lines 13a through 13z" "15 Add lines 4 through 11 and line 14" "20 Total additional employment and other taxes. Add lines 16c, 17d, 18, and 19c" "Add lines 15 and 20. These are your total additional taxes. Enter here and on Form 1040 or 1040-SR, line 23; or Form 1040-NR, line 23b"
- **2025:** `f1040s2` p. 1: "12 Net investment income tax. Attach Form 8960"; p. 2: "Additional tax on HSA distributions. Attach Form 8889" "18 Total additional taxes. Add lines 17a through 17z" "Add lines 4, 7 through 16, 18, and 19. These are your total other taxes. Enter here and on Form 1040 or 1040-SR, line 23; or Form 1040-NR, line 23b"
- **Touches:** s2.line4, s2.line8, s2.line8_box, s2.line11, s2.line12, s2.line17c, s2.line18, s2.line21, s2.other, s2.line1a, s2.line1z, s2.line2, s2.line3
- **Worklist items:** s2.line21, s2.line1a
- **Notes:**
  - **Part I unchanged.** Lines 1a–3 are unchanged in text.
  - **Part II, old line to new line:**
    - 5, 6, 7 → 16a, 16b, 16c
    - 8 → 5 (with a new line 18; see C-SCHED-11)
    - 9 → 17a
    - 11 → 11 and 17b (C-SCHED-13)
    - 12 → 6
    - 13 → 17c
    - 14, 15, 16 → 7, 8, 9
    - 17a–17o → 13a–13o; 17z → 13z; 17p, 17q → 19a, 19b
    - 18 → 14
    - 19 → 10
    - 20 → 12
    - New subtotal lines 15, 17d, 19c and 20.
  - **Line 21 for the slice.** It becomes 4 + 5 + 6 + 11 + 14 + 17b + 18.
  - **Renames.** s2.line12 → line 6 (i8960 p. 23 (draft) also says "include this amount on Schedule 2
    (Form 1040), line 6"). s2.line17c → 13c (`f8889` p. 2 (draft) says "line 13c"). s2.line18 → 14.
  - **s2.other text.** The list of other lines in s2.other's question needs the new numbers.
  - **s2.line1a.** Its form text is unchanged ("1a Excess advance premium tax credit repayment. Attach Form
    8962", p. 2). Its i1040gi p. 111 citation cannot be checked.

### C-SCHED-11. Form 5329 taxes split between Schedule 2 line 5 (early distributions) and new line 18 (excess contributions)

- **Kind:** rule (definition change)
- **2026:** `f1040s2` p. 2 (draft): "5 Additional tax on IRAs or other tax-favored accounts. Attach Form 5329 if required. If not required, check here"; p. 3: "18 Additional tax on excess contributions or accumulations in IRAs or other tax-favored accounts. Attach Form 5329"
- **2026:** `f5329` p. 2 (draft): "Additional tax. Enter 10% (0.10) of line 3. Include this amount on Schedule 2 (Form 1040), line 5"; p. 3: "Include this amount on Schedule 2 (Form 1040), line 18"
- **2026:** `i5329` p. 2 (draft): "However, if distribution code 1 is correctly shown in box 7a of all your Forms 1099-R and you owe the additional tax on the full amount shown on each Form 1099-R, you don’t have to file Form 5329. Instead, see the instructions for Schedule 2 (Form 1040), line 5,"
- **2025:** `f1040s2` p. 1: "Additional tax on IRAs or other tax-favored accounts. Attach Form 5329 if required. If not required, check here"
- **2025:** `i5329` p. 1: "However, if distribution code 1 is correctly shown in box 7 of all your Forms 1099-R and you owe the additional tax on the full amount shown on each Form 1099-R, you don’t have to file Form 5329."
- **Touches:** s2.line8, s2.line8_box, s2.line8_file, s2.line8_must, person.x_tax, f5329.tax, f5329.l4, f5329.l49, s2.line21
- **Worklist items:** s2.line8_box, s2.line8_file, s2.line8_must
- **Notes:**
  - **The split.** f5329.tax (lines 4 + 49) must be split. Line 4 (early distributions) goes to Schedule 2
    line 5, together with its "if not required" box (s2.line8_box → line 5 box). Line 49 (HSA excess
    contributions; f5329 2026 p. 3) goes to new line 18.
  - **Same rule, new wording.** The i5329 filing exception is unchanged in substance. The 1099-R box
    reference becomes "box 7a", which is a Form 1099-R change for that section.
  - **Instructions not archived.** The i1040gi p. 112 citation on s2.line8_box cannot be checked.

### C-SCHED-12. Schedule 3: line 5a from Form 5695 line 3; line 5b "Reserved"; line 8 drops 5b

- **Kind:** rule (definition change)
- **2026:** `f1040s3` p. 2 (draft): "5a Residential clean energy credit from Form 5695, line 3" "5b Reserved for future use" "Add lines 1 through 4, 5a, and 7. Enter here and on Form 1040, 1040-SR, or 1040-NR, line 20"
- **2025:** `f1040s3` p. 1: "Residential clean energy credit from Form 5695, line 15" "Energy efficient home improvement credit from Form 5695, line 32" "Add lines 1 through 4, 5a, 5b, and 7. Enter here and on Form 1040, 1040-SR, or 1040-NR, line 20"
- **Touches:** s3.line5a, s3.line5b, s3.line8, s3.line10; f5695.line15, f5695.line32 (readers); s8812.clw_a2 (C-SCHED-23)
- **Worklist items:** s3.line10
- **Notes:**
  - **What the adoption does.** Point s3.line5a at the renumbered Form 5695 credit line (Form 5695 section),
    and remove s3.line5b from s3.line8 (keep it printed as reserved, or drop it).
  - **s3.line10.** Its form text is unchanged ("Amount paid with request for extension to file (see
    instructions)", p. 2). Its i1040gi p. 117 citation cannot be checked.

### C-SCHED-13. Form 8959 reordered: wages+RRTA total (line 12) to Schedule 2 line 17b; SE tax (line 18) to Schedule 2 line 11

- **Kind:** new line or form
- **2026:** `f8959` p. 2 (draft): "8 RRTA compensation and tips from Form(s) W-2, box 14a (see instructions)" "Additional Medicare Tax on RRTA compensation. Multiply line 10 by 0.9% (0.009)." "Add lines 7 and 11. Also enter this amount on Schedule 2 (Form 1040), line 17b, or Form 1040-SS, Part I, line 5b." "Subtract line 15 from line 14. If zero or less, enter -0-" "Subtract line 16 from line 13. If zero or less, enter -0-" "Additional Medicare Tax on self-employment income. Multiply line 17 by 0.9% (0.009). Enter here and on Schedule 2 (Form 1040), line 11, or Form 1040-SS, Part I, line 5a."
- **2026:** `i8959` p. 2 (draft): "Form 8959 has been revised to report Additional Medicare Tax on Medicare wages and Railroad Retirement Tax Act (RRTA) compensation separately from Additional Medicare Tax on self-employment income."
- **2026:** `f1040s2` p. 2 (draft): "Additional Medicare Tax on self-employment income. Attach Form 8959"; p. 3: "Additional Medicare tax on Medicare wages and RRTA compensation."
- **2025:** `f8959` p. 1: "Subtract line 10 from line 9. If zero or less, enter -0-" "Subtract line 11 from line 8. If zero or less, enter -0-" "Additional Medicare Tax on self-employment income. Multiply line 12 by 0.9% (0.009)." "Multiply line 16 by 0.9% (0.009)." "Add lines 7, 13, and 17. Also include this amount on Schedule 2 (Form 1040), line 11"
- **Touches:** f8959.line8, f8959.line9, f8959.line10, f8959.line11, f8959.line12, f8959.line13, f8959.line14, f8959.line15, f8959.line16, f8959.line17, f8959.line18, s2.line11, s2.line21, s8812.amt_ws7 (C-SCHED-22)
- **Worklist items:** f8959.line11, f8959.line12, f8959.line13, f8959.line17, f8959.line18
- **Notes:**
  - **Old line to new line.** Lines 1–7 and 19–24 are unchanged. Old SE part 8–13 → 13–18; old RRTA part
    14–17 → 8–11; old total 18 → 12 (lines 7 + 11 only).
  - **What the adoption does.** Schedule 2 line 11 reads the new line 18 (SE), and a new s2 line 17b reads
    line 12. Both feed s2.line21.
  - **"Printed in 2025 only" findings.** The quotes are the same sentences with new line numbers.
  - **W-2 box.** The RRTA box becomes W-2 box 14a, which is a Form W-2 change.

### C-SCHED-14. Additional Medicare Tax thresholds unchanged

- **Kind:** wording only
- **2026:** `f8959` p. 2 (draft): "Enter the following amount for your filing status:" "$250,000" "$125,000" "$200,000" "Multiply line 6 by 0.9% (0.009)" "Multiply line 20 by 1.45% (0.0145)"
- **2026:** `i8959` p. 2 (draft): "Note: The threshold amounts below aren’t indexed for inflation."; p. 4: "$250,000 threshold and Judy’s RRTA compensation isn’t"
- **2025:** `f8959` p. 1: "Enter the following amount for your filing status:" "$250,000" "$125,000" "$200,000" "Multiply line 6 by 0.9% (0.009)"
- **Touches:** medicare.threshold, medicare.additional_rate, medicare.regular_rate, f8959.line5, f8959.line9, f8959.line15
- **Worklist items:** medicare.threshold
- **Notes:**
  - **What the finding meant.** The "probable value change" findings come from sentences that differ only
    in line numbers, box 14 → 14a and the footer.
  - **Values.** The $250,000 / $125,000 / $200,000 thresholds and the 0.9% and 1.45% rates are printed
    unchanged, and the i8959 example 7 sentence is still printed (p. 4). The parameter keeps its 2025
    values; re-cite it to f8959 lines 5, 9 and 14 for 2026.

### C-SCHED-15. Form 8959 instructions: dates and W-2 box 14a (wording)

- **Kind:** wording only
- **2026:** `i8959` p. 2 (draft): "Your employer is required to furnish Form W-2, Wage and Tax Statement, to you no later than February 1, 2027." "(box 14a) is greater than $200,000."
- **2025:** `i8959` p. 1: "required to furnish Form W-2, Wage and Tax Statement, to you no later than February 2, 2026." "(box 14) is greater than $200,000."
- **Touches:** none (f8959.line14/f8959.line23 RRTA inputs are zero unless refused through f8959.unsupported; only the label box changes)
- **Worklist items:** none (context for the f8959 items in C-SCHED-13)
- **Notes:** None.

### C-SCHED-16. Schedule 8812 line 1 reads Form 1040 line 11b

- **Kind:** wording only
- **2026:** `f1040s8812` p. 1 (draft): "Enter the amount from line 11b of your Form 1040, 1040-SR, or 1040-NR"
- **2025:** `f1040s8812` p. 1: "Enter the amount from line 11a of your Form 1040, 1040-SR, or 1040-NR"
- **Touches:** s8812.line1
- **Worklist items:** none (pair context of s8812.line4, s8812.line6, s8812.show_iib)
- **Notes:**
  - **Same amount.** The 2026 Form 1040 draft prints "11b Amount from line 11a (adjusted gross income)"
    (`f1040` p. 3), so the value is unchanged.
  - **What the adoption does.** Re-point s8812.line1 to f1040.line11b and change its label.

### C-SCHED-17. Schedule 8812 line 22 and Credit Limit Worksheet B line 8 read Schedule 2 lines 16c and 17c

- **Kind:** wording only (cross-reference)
- **2026:** `f1040s8812` p. 2 (draft): "Enter the total of the amounts from Schedule 1 (Form 1040), line 15; Schedule 2 (Form 1040), line 16c; and Schedule 2 (Form 1040), line 17c"
- **2026:** `i1040s8812` p. 6 (draft): "• Schedule 2, line 16c; and" "• Schedule 2, line 17c."
- **2025:** `f1040s8812` p. 2: "Enter the total of the amounts from Schedule 1 (Form 1040), line 15; Schedule 2 (Form 1040), line 5; Schedule 2 (Form 1040), line 6; and Schedule 2 (Form 1040), line 13"
- **Touches:** s8812.line22, s8812.clwb_8; refusal s2.other on s8812.line22
- **Worklist items:** none (pair context of s8812 items)
- **Notes:**
  - **New references.** Schedule 2 16c is old 7 (= 5 + 6), and 17c is old 13. The 2026 17c is
    "Uncollected social security and Medicare or RRTA tax on tips or group-term life insurance from Form
    W-2, box 12" (`f1040s2` p. 3).
  - **What the adoption does.** In the encoding both stay refused through s2.other. Only the labels,
    citations and refusal text change.
- **Correction (verification):** reclassified from "rule (definition change)": the amounts are unchanged; only line numbers and references move (`changes.verification.md`).

### C-SCHED-18. Additional Medicare Tax and RRTA Tax Worksheet: Form 8959 line references follow the new layout

- **Kind:** wording only (cross-reference)
- **2026:** `i1040s8812` p. 10 (draft): "Enter one-half of the Additional Medicare Tax, if any, on self-employment income (one-half of Form 8959, line 18)" "Enter the Additional Medicare Tax, if any, on RRTA compensation as an employee (Form 8959, line 11)."
- **2025:** `i1040s8812` p. 9: "Enter one-half of the Additional Medicare Tax, if any, on self-employment income (one-half of Form 8959, line 13)" "Enter the Additional Medicare Tax, if any, on RRTA compensation as an employee (Form 8959, line 17)."
- **Touches:** s8812.amt_ws7, s8812.amt_ws4, s8812.amt_ws6, s8812.line21
- **Worklist items:** s8812.amt_ws7
- **Notes:**
  - **What the adoption does.** s8812.amt_ws7 must read f8959's 2026 line 18 (today f8959.line13), and
    the RRTA lines must read line 11.
  - **Unchanged worksheet lines.** Line 3 (Form 8959 line 7) and line 5 (Form 8959 line 22) are printed
    the same in both years. The worksheet's withheld-tax line is numbered 5 in 2026, against the pair's "4"
    in 2025: "Enter the Additional Medicare Tax withheld (Form 8959, line 22)" (p. 10).
- **Correction (verification):** reclassified from "rule (definition change)": the amounts are unchanged; only line numbers and references move (`changes.verification.md`).

### C-SCHED-19. Schedule 8812 SSN and TIN requirements reworded

- **Kind:** wording only
- **2026:** `i1040s8812` p. 2 (draft): "To claim the CTC or ACTC on either your original or an amended 2026 return, you must have a valid SSN. If you are filing a joint return, only one filer is required to have a valid SSN to be eligible for the CTC or ACTC." "A valid SSN is one that is valid for employment and that is issued by the Social Security Administration before the due date of your 2026 return (including extensions)." "The qualifying child used to claim the CTC or ACTC on either your original or an amended 2026 return must have a valid SSN." "The dependent used to claim the ODC on either your original or an amended 2026 return must have an SSN, ITIN, or ATIN issued on or before the due date of your return (including extensions)."
- **2025:** `i1040s8812` p. 1: "If you, and your spouse if filing jointly, do not have a valid SSN, you can’t claim the CTC or ACTC on either your original or an amended 2025 return. If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC or ACTC." "If you have a qualifying child who does not have a valid SSN, you can’t use the child to claim the CTC or ACTC on either your original or an amended 2025 return." "If you have a dependent who does not have an SSN, ITIN, or ATIN issued on or before the due date of your 2025 return (including extensions), you can’t use that dependent to claim the ODC on either your original or an amended 2025 return."
- **Touches:** s8812.line4, s8812.line6 (household/dependent eligibility helpers that cite these sentences)
- **Worklist items:** s8812.line4, s8812.line6
- **Notes:**
  - **Same tests, new wording.** The 2026 text states the same tests in the positive ("filer" instead of
    "spouse"). The adoption re-cites the 2026 sentences.
  - **Instructions not archived.** The i1040gi pp. 17–19 citations (Who Qualifies as Your Dependent)
    cannot be checked.

### C-SCHED-20. Credit Limit Worksheet B: "Continued" heading reworded

- **Kind:** wording only
- **2026:** `i1040s8812` p. 7 (draft): "Credit Limit Worksheet B (continued)" "Subtract line 10 from line 9. If the result is zero or less, enter -0-" "Enter the larger of line 5 or line 11" "Enter the smaller of line 2 or line 12"
- **2025:** `i1040s8812` p. 6: "Credit Limit Worksheet B—Continued" "Subtract line 10 from line 9. If the result is zero or less, enter -0-"
- **Touches:** s8812.clwb_10, s8812.clwb_11_figured, s8812.clwb_12, s8812.clwb_13, s8812.clwb_14, s8812.clwb_15 (citations only)
- **Worklist items:** s8812.clwb_10, s8812.clwb_11_figured, s8812.clwb_12, s8812.clwb_13, s8812.clwb_14, s8812.clwb_15
- **Notes:**
  - **What changed.** Only the heading changed. Lines 10–15 are printed the same, now on p. 7.
  - **What the adoption does.** Re-cite each line to "Credit Limit Worksheet B (continued)".

### C-SCHED-21. Schedule 8812 Part II-B routing sentence unchanged

- **Kind:** wording only
- **2026:** `f1040s8812` p. 2 (draft): "Next. On line 16b, is the amount $5,100 or more?" "Yes. If line 20 is equal to or more than line 17, skip Part II-B and enter the amount from line 17 on line 27."
- **2025:** `f1040s8812` p. 2: "Next. On line 16b, is the amount $5,100 or more?" "Yes. If line 20 is equal to or more than line 17, skip Part II-B and enter the amount from line 17 on line 27."
- **Touches:** s8812.show_iib, s8812.few_children, s8812.earned_covers
- **Worklist items:** s8812.show_iib
- **Notes:** The "printed in 2026 only" finding is not a change: the routing text is printed in both years.
  The only nearby differences are the header ("Version A, Cycle 4") and line 1 (C-SCHED-16).

### C-SCHED-22. Additional Medicare Tax and RRTA Tax Worksheet: RRTA amounts from W-2 box 14a

- **Kind:** wording only
- **2026:** `i1040s8812` p. 10 (draft): "Enter the Tier 1 tax (Form(s) W-2, box 14a)"
- **2025:** `i1040s8812` p. 9: "Enter the Tier 1 tax (Form(s) W-2, box 14)"
- **Touches:** none (the RRTA lines of the worksheet are not computed in the slice; sc.rrta and f8959.unsupported refuse RRTA)
- **Worklist items:** none
- **Notes:** The RRTA W-2 box reference becomes 14a, which is a Form W-2 change for the W-2 section.

### C-SCHED-23. Credit Limit Worksheet A line 2 drops Schedule 3 line 5b; Worksheet B credit list says "Form 5695"

- **Kind:** rule (definition change)
- **2026:** `i1040s8812` p. 5 (draft): "Schedule 3, line 4" "Schedule 3, line 6d" "c. Residential clean energy credit, Form 5695."
- **2025:** `i1040s8812` p. 4: "Schedule 3, line 5b" "c. Residential clean energy credit, Form 5695, Part I."
- **Touches:** s8812.clw_a2, s8812.clwb_complete, s8812.show_clwb
- **Worklist items:** none
- **Notes:**
  - **What changed.** CLW A line 2 now adds Schedule 3 lines 1, 2, 3, 4, 6d, 6f, 6l and 6m; line 5b is
    gone, which follows C-SCHED-12.
  - **What the adoption does.** Remove s3.line5b from s8812.clw_a2, and update the "Form 5695, Part I"
    wording in s8812.clwb_complete. Whether Form 5695 still has a Part I is for the Form 5695 section.

### C-SCHED-24. Schedule 8812 form cautions unchanged

- **Kind:** wording only
- **2026:** `f1040s8812` p. 1 (draft): "Caution: Do not include yourself, your spouse, or anyone who is not a U.S. citizen, U.S. national, or U.S. resident alien. Also, do not include anyone you included on line 4."
- **2025:** `f1040s8812` p. 1: "Caution: Do not include yourself, your spouse, or anyone who is not a U.S. citizen, U.S. national, or U.S. resident alien. Also, do not include anyone you included on line 4."
- **Touches:** s8812.line6
- **Worklist items:** none
- **Notes:** None.

### C-SCHED-25. Schedule 8812 credit amounts unchanged

- **Kind:** wording only
- **2026:** `f1040s8812` p. 1 (draft): "Multiply line 4 by $2,200" "Multiply line 6 by $500" "Married filing jointly—$400,000" "Multiply line 10 by 5% (0.05)"; p. 2: "Is the amount on line 18a more than $2,500?" "Multiply the amount on line 19 by 15% (0.15) and enter the result"
- **2026:** `i1040s8812` p. 2 (draft): "The maximum amount of CTC for each qualifying child is $2,200." "The maximum amount of ACTC for each qualifying child is $1,700."
- **2025:** `f1040s8812` p. 1: "Multiply line 4 by $2,200" "Multiply line 6 by $500" "Married filing jointly—$400,000"
- **Touches:** ctc.per_child, ctc.threshold, ctc.phaseout_rate, actc.per_child, actc.earned_floor, actc.rate, actc.three_children
- **Worklist items:** none
- **Notes:** All Schedule 8812 figures are printed unchanged, so the parameters keep their 2025 values.

### C-SCHED-26. ACTC refund limited to U.S. citizens, U.S. nationals and qualified aliens (Schedule 3-A)

- **Kind:** rule (definition change)
- **2026:** `i1040s8812` p. 3 (draft): "Limits on the refund of the ACTC. To receive a refund of the ACTC, you must be a U.S. citizen, U.S. national, or qualified alien. See the instructions for Schedule 3-A (Form 1040)."
- **2025:** no counterpart
- **Touches:** s8812.line27 (feeds Form 1040 line 28)
- **Worklist items:** none
- **Notes:** The mechanism is Schedule 3-A, which is in the Form 1040 section. The Schedule 8812 adoption
  only needs to make sure s8812.line27 is not paid out where Schedule 3-A denies the refund. The
  instructions point there, and nothing on the 2026 Schedule 8812 form itself changes.

### C-SCHED-27. Form 8960: section 68 limitation worksheet for lines 9 and 10

- **Kind:** new line or form
- **2026:** `i8960` p. 2 (draft): "Beginning in 2026, changes to the section 68 limitation generally apply to individuals, estates, and trusts in the highest tax bracket and may reduce the tax benefit of itemized deductions." "A new Lines 9 and 10 Section 68 Limitation Worksheet for Individuals, Estates, and Trusts has been created to reflect the section 68 overall limitation on itemized deductions."; p. 19: "Beginning in 2026, your deduction for investment interest expense may be limited if your taxable income is more than the threshold amount." "You can use any reasonable method to determine the portion of your state, local, and foreign income taxes; state, local, and foreign real property taxes; and state and local personal property taxes that is allocable to NII."; p. 20: "Beginning in 2026, your deduction for state, local, and foreign income taxes may be limited if your taxable income is more than the threshold amount."; p. 21: "Enter $768,700 if married filing jointly or qualifying surviving spouse; $640,600 if head of household or single; $384,350 if married filing separately."
- **2025:** `i8960` p. 18: "property taxes allocable to NII using any reasonable" "method. See Reasonable method allocations, earlier."
- **Touches:** f8960.line9a, f8960.line9b, f8960.allocated_taxes, f8960.bad_allocation, f8960.line10, f8960.line11
- **Worklist items:** f8960.line9b
- **Notes:**
  - **New rule.** Above the worksheet's line 2 thresholds (taxable income plus itemized deductions), the
    Schedule A investment interest (9a) and the allocated taxes (9b) on Form 8960 are cut by the
    worksheet. The 2025 encoding has nothing like this.
  - **Options for the adoption.** Encode the worksheet, which shares the section 68 computation with the
    Schedule A section. Or refuse returns whose worksheet line 3 is more than zero, with new parameters for
    the three thresholds.
  - **Line 9b citation.** The "reasonable method" sentence is reworded, not removed.

### C-SCHED-28. Form 8960 line 7: Schedule 1 line 8j (rental at less than fair rental value) joins line 8z

- **Kind:** rule (definition change)
- **2026:** `i8960` p. 14 (draft): "Other items of NII (or properly allocable deductions) not otherwise included on Form 8960 reported on Schedule 1 (Form 1040), lines 8j and 8z"; p. 6: "Rental at less than FRV is recharacterized as a nonpassive activity regardless of your material participation and is NII to an individual under section 1411(c)(1)(A)(i)." "Report the income on Form 8960, line 7, as a modification (originally reported on Schedule 1 (Form 1040), line 8j)."
- **2025:** `i8960` p. 13: "Other items of NII (or properly allocable deductions) not otherwise included on Form 8960 reported on Schedule 1 (Form 1040), line 8z"
- **Touches:** amb.2025.line8z_kinds, f8960.line7, f8960.unsupported, s1.line8j, oi8z (line 8z kinds)
- **Worklist items:** amb.2025.line8z_kinds
- **Notes:**
  - **What the 2026 text says.** Schedule 1 line 8j (still "Activity not engaged in for profit income" on
    the 2026 Schedule 1 draft, p. 2) can carry income that is NII.
  - **The gap.** s1.line8j is an encoded input, but in 2025 it never reaches Form 8960 (f8960.line7 is zero
    unless refused). f8960.unsupported asks about "rental" income, which arguably catches below-FRV rental.
  - **What the adoption does.** Decide whether to add 8j amounts to the Form 8960 screen, or to refuse 8j
    income when Form 8960 is used. The line 8z part of the ambiguity rests on the same sentence, now naming
    both lines.
  - **Instructions not archived.** The i1040gi p. 92 citation in the ambiguity cannot be checked.

### C-SCHED-29. Form 8960 instructions: lines 1, 2, 5, 7 and 10 reworded (wording)

- **Kind:** wording only
- **2026:** `i8960` p. 8 (draft): "Enter your taxable interest. Include the applicable amount from your return:" "• Form 1040 or 1040-SR, line 2b." "Enter your ordinary dividends. Include the applicable" "• Form 1040 or 1040-SR, line 3b."; p. 9: "If line 2 includes dividends from employer securities held in an employee stock ownership plan (ESOP) that are deductible under section 404(k), or Alaska Permanent Fund dividends, include those amounts as negative modifications on line 7."; p. 11: "Enter the amount from line 2(i) of this worksheet as calculated on your prior-year return."; p. 13: "Starting in 2014, capital loss carryforwards must be adjusted if the sum of all capital gain or loss amounts excluded from NII on lines 5b and 5c was a net loss"; p. 14: "Note: The early withdrawal penalty reported on Schedule 1 (Form 1040), line 18, is reported on Form 8960, line 10."; p. 20: "Use line 10 to report additional deductions or modifications to NII that aren’t otherwise reflected on lines 1–9."
- **2025:** `i8960` p. 7: "Enter the amount of taxable interest received. Include the following amount from your return." "If line 2 includes dividends from employer securities held in an employee stock ownership plan (ESOP) that are deductible under section 404(k) or Alaska Permanent Fund Dividends, include those amounts as negative modifications on line 7"; p. 9: "capital loss carryforwards must be adjusted if any sum of all capital gain or loss amounts excluded from NII on lines 5b and 5c was a net loss"; p. 10: "Enter the amount reported on line 2(i) of this worksheet from your prior tax year return calculations"; p. 13: "Note: Early withdrawal penalty (Schedule 1 (Form 1040), line 18) is reported on Form 8960, line 10"; p. 18: "On line 10, report additional deductions or modifications to NII that aren't otherwise reflected on lines 1–9"
- **Touches:** f8960.line1, f8960.line2, f8960.line10, f8960.prior_2i, f8960.carryforward_adj, f8960.unsupported (citations only)
- **Worklist items:** f8960.line1, f8960.line2, f8960.line10, f8960.prior_2i, f8960.carryforward_adj, f8960.unsupported
- **Notes:**
  - **Rules unchanged.** Each rule is unchanged: the same Form 1040 lines 2b/3b, the same line 2(h)/2(i)
    carryforward adjustment, the ESOP/APF modification, and the early withdrawal penalty on line 10. The
    adoption re-cites the 2026 pages.
  - **Form wording.** The Form 8960 draft rewords lines 4b ("included on line 4a") and 6 (CFC/PFIC spelled
    out) only (`f8960` p. 2).

### C-SCHED-30. QBI: Form 8995 threshold rises, with a separate married-filing-separately amount

- **Kind:** amount (parameter)
- **2026:** `f8995` p. 2 (draft): "Use this form if your taxable income, before your qualified business income deduction, is at or below $201,750 ($201,775 if married filing separately; $403,500 if married filing jointly), and you aren’t a patron of an agricultural or horticultural cooperative."
- **2026:** `i8995` p. 2 (draft): "Your 2026 taxable income before your QBI deduction is less than or equal to $403,500 if married filing jointly, $201,775 if married filing separately, and $201,750 for all other returns"
- **2025:** `f8995` p. 1: "Use this form if your taxable income, before your qualified business income deduction, is at or below $197,300 ($394,600 if married filing jointly), and you aren’t a patron of an agricultural or horticultural cooperative."
- **Touches:** qbi.threshold (single/hoh/qss 19730000 → 20175000; mfs 19730000 → 20177500; mfj 39460000 → 40350000), qbi.use_8995a, qbi.business_any, qbi.deduction
- **Worklist items:** qbi.threshold, qbi.use_8995a
- **Notes:**
  - **Possible draft error.** The draft prints an MFS amount ($201,775) that is $25 higher than the single
    amount. It is printed the same way three times (f8995, f8995a, i8995), but it should be checked against
    the final form or the 2026 revenue procedure before release.
  - **Values to use.** The values above, all from the draft.
- **Correction (verification):** the amounts are confirmed by `rp-25-32` p. 22 (final), section 4.26: "Married Individuals Filing Separate Returns $201,775 $276,775"; the MFS amount is not a draft error (`changes.verification.md`).

### C-SCHED-31. Form 8995: new lines 15–17 (minimum deduction of $400) and 20 (ESBT); carryforwards move to 18–19

- **Kind:** new line or form
- **2026:** `f8995` p. 2 (draft): "Qualified business income deduction before the minimum deduction for active qualified business income. Enter the smaller of line 10 or line 14" "Minimum deduction for active qualified business income (see instructions)" "Qualified business income deduction. Enter the greater of line 15 or line 16." "Total qualified business (loss) carryforward. Combine lines 2 and 3. If greater than zero, enter -0-"
- **2026:** `i8995` p. 2 (draft): "There is a minimum qualified business income deduction of $400 for taxpayers whose aggregate qualified business income for such taxable year is at least $1,000 with respect to all qualified trades or businesses in which the taxpayer materially participates, within the meaning of section 469(h)." "Form has been revised. Lines 15, 16, and 20 have been added to the Form for the 2026 tax year."; p. 6: "If the smaller of line 10 or 14 is less than $400, enter $400 if the aggregate qualified business income from lines 1i through 1v, column (c) with respect to all qualified trades or businesses in which you materially participated for the taxable year, within the meaning of section 469(h), is at least $1,000."
- **2025:** `f8995` p. 1: "Qualified business income deduction. Enter the smaller of line 10 or line 14. Also enter this amount on the applicable line of your return (see instructions)" "Total qualified business (loss) carryforward. Combine lines 2 and 3. If greater than zero, enter -0-"
- **Touches:** f8995.line15, f8995.line16, f8995.line17, f8995.loss, qbi.deduction, qbi.eligible, sc.passive (material participation input); f1040.line13a (2025 QBI reader)
- **Worklist items:** f8995.line15, qbi.deduction
- **Notes:**
  - **Old line to new line.** Old 15 → 15 (renamed); new 16 (minimum) and 17 (greater of 15 and 16); old
    16 → 18; old 17 → 19; new 20 (ESBT box, not encoded).
  - **New parameters.** $400 and the $1,000 aggregate.
  - **New computation.** The aggregate is the QBI of Schedule C businesses in which the filer materially
    participates (the encoding has sc.passive, Schedule C line G). The section 199A dividends path does not
    qualify.
  - **Open question.** i8995 states the $400 rule under the "Line 17" heading on p. 6, while line 16 on
    the form is the minimum. The adoption must reconcile the two.
  - **Where the deduction goes.** i8995 p. 6 (draft) says "Enter this amount on your Form 1040, 1040-SR,
    or Form 1040-NR, line 13a". The 2026 Form 1040 draft prints "13b Qualified business income deduction
    from Form 8995 or Form 8995-A" (`f1040` p. 3). This is a draft inconsistency; the Form 1040 face
    should govern.

### C-SCHED-32. Form 8995-A Part IV: new lines 39–41 (minimum deduction) and 43 (ESBT); carryforward moves to line 42

- **Kind:** new line or form
- **2026:** `f8995a` p. 3 (draft): "Qualified business income deduction before the minimum deduction for active qualified business income. Add lines 37 and 38" "Minimum deduction for active qualified business income (see instructions)" "Total qualified business income deduction. Enter the greater of line 39 or line 40." "Total qualified REIT dividends and PTP (loss) carryforward. Combine lines 28 and 29. If zero or greater, enter -0-"
- **2025:** `f8995a` p. 2: "Total qualified business income deduction. Add lines 37 and 38" "Total qualified REIT dividends and PTP (loss) carryforward. Combine lines 28 and 29. If zero or greater, enter -0-"
- **Touches:** f8995a.line27, f8995a.line28, f8995a.line29, f8995a.line30, f8995a.line31, f8995a.line32, f8995a.line33, f8995a.line34, f8995a.line35, f8995a.line36, f8995a.line37, f8995a.line38, f8995a.line39, f8995a.line40, qbi.via_8995a
- **Worklist items:** f8995a.line27, f8995a.line28, f8995a.line29, f8995a.line30, f8995a.line31, f8995a.line32, f8995a.line33, f8995a.line34, f8995a.line35, f8995a.line36, f8995a.line37, f8995a.line38, f8995a.line39, f8995a.line40
- **Notes:**
  - **Old line to new line.** Lines 27–38 are unchanged in substance; line 28 adds "(see instructions)".
    Old 39 → new 39 (renamed) + 40 (minimum) + 41 (total). Old 40 → 42. New 43 (ESBT).
  - **What the adoption does.** On the dividend-only path the minimum deduction is zero, since no
    material-participation QBI is possible. qbi.via_8995a must read line 41, and the f8995a.line40 id moves
    to line 42.
  - **No 2026 i8995a.** The 2025 citations to i8995a p. 6 ("skip Parts I through III") cannot be checked.

### C-SCHED-33. QBI: taxable income before the deduction uses Form 1040 lines 12e, 12f and 13a, without section 68

- **Kind:** rule (definition change)
- **2026:** `i8995` p. 2 (draft): "Taxable income is computed without regard to section 68."; p. 6: "Form 1040 or 1040-SR filers who file Schedule A: Form 1040 or 1040-SR, line 11a, minus the amounts on Schedule A (Form 1040) lines 4,7,10,15,16, and 17z, and Form 1040 or 1040-SR, line 13a." "Form 1040 or 1040-SR filers who do not file Schedule A: Form 1040 or 1040-SR, line 11a, minus lines 12e, 12f, and 13a."
- **2025:** `i8995-correction` p. 1: "Form 1040 or 1040-SR filers: Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b."
- **Touches:** qbi.deductions_before, qbi.taxable_before, f8995.line11, f8995a.line33, sa.deduction, f1040.line13b
- **Worklist items:** none
- **Notes:**
  - **Same idea, new inputs.** AGI is still reduced by the deductions taken before the QBI deduction.
    Itemizers now subtract Schedule A lines before any section 68 cut. Non-itemizers also subtract new
    Form 1040 line 12f. Schedule 1-A is 2026 line 13a.
  - **What the adoption does.** Rebuild qbi.deductions_before from these readers. Schedule A and line 12f
    belong to their own sections.

### C-SCHED-34. Form 8995-A Part III: threshold and phase-in range (not encoded)

- **Kind:** not encoded
- **2026:** `f8995a` p. 3 (draft): "Complete Part III only if your taxable income is more than $201,750 but not $276,750 ($201,775 and $276,775 if married filing separately; $403,500 and $553,500 if married filing jointly) and line 10 is less than line 3." "Phase-in range. Enter $75,000 ($150,000 if"
- **2025:** `f8995a` p. 2: "Complete Part III only if your taxable income is more than $197,300 but not $247,300 ($394,600 and $494,600 if married filing jointly)" "Phase-in range. Enter $50,000 ($100,000 if"
- **Touches:** none (Parts I–III are skipped on the dividend-only path; business income above the threshold is refused through qbi.business_any)
- **Worklist items:** none
- **Notes:** Record the change: the phase-in range rises from $50,000 to $75,000 ($100,000 to $150,000
  MFJ). It matters only if Form 8995-A business computations are ever encoded.

### C-SCHED-35. QBI: qualified tips excluded from QBI (clarified)

- **Kind:** not encoded
- **2026:** `i8995` p. 2 (draft): "Any amount with respect to which a deduction is allowable to the taxpayer under section 224(a) for the taxable year is not included in qualified business income."; p. 5: "Do not include any amount with respect to which a deduction is allowable as a qualified tip under section 224(a) for the taxable year."
- **2025:** `i8995` p. 3: "Tip income under section 224 that is excluded from the net profit of the trade or business."
- **Touches:** none (tips in a trade or business are refused through s1.sc_1a, so sc.qbi never carries a section 224 amount)
- **Worklist items:** none
- **Notes:** In 2025 the rule appeared in the QBI flow chart (i8995 2025 p. 7, step 11). The 2026 draft
  promotes it to What's New and to the Line 1 instructions. It needs work only if trade-or-business tips
  are ever supported.

### C-SCHED-36. Form 4952 (final 2026): line 4g election text and other wording

- **Kind:** wording only
- **2026:** `f4952` p. 4: "Write “Filed pursuant to Regulations section 301.9100-2” on the amended return and file it at the same place you filed the original return." "Once made, the net capital gain"; p. 1: "Disallowed investment interest expense from 2025 Form 4952, line 7"; p. 4: "which aren’t allowed deductions in tax years beginning after 2017."
- **2025:** `f4952` p. 4: "Write “Filed pursuant to section 301.9100-2” on the amended return and file it at the same place you filed the original return."; p. 1: "Disallowed investment interest expense from 2024 Form 4952, line 7"; p. 4: "which aren’t allowed deductions in tax years" "beginning after December 31, 2017, and before"
- **Touches:** f4952.line4g, f4952.line2, f4952.prior_7, f4952.carryover, f4952.line7, f4952.line5 (citations and the years in labels)
- **Worklist items:** f4952.line4g
- **Notes:**
  - **What changed.** The 2026 edition is final. The amended-return election text adds "Regulations",
    and the years roll forward (2025 carryforward in, 2027 carryforward out).
  - **Miscellaneous itemized deductions caution.** It now reads as permanent. f4952.line5 is zero in the
    slice (refused through f4952.unsupported), so nothing computed changes.
  - **Section 68 for interest.** The i8960 statement that investment interest may be limited under section
    68 (C-SCHED-27) concerns Schedule A line 9, not Form 4952 line 8.

### C-SCHED-37. Student loan repayment assistance text moved (p4681)

- **Kind:** wording only
- **2026:** `p4681` p. 8 (draft): "payments made to you are tax free if you received them" "Caution: You can’t deduct the interest you paid on a" "student loan to the extent payments were made through" "your participation in any of the above programs."
- **2025:** `p4681` p. 5: "Student loan repayment assistance. Stu-"
- **Touches:** sli.interest
- **Worklist items:** sli.interest
- **Notes:**
  - **What changed.** The same three programs (NHSC, the state programs eligible under the Public Health
    Service Act, and other state health-service programs) are printed on p. 8 instead of p. 5. The
    adoption re-cites.
  - **Instructions not archived.** The i1040gi p. 98 citation cannot be checked.

### C-SCHED-38. Form 1116 instructions: 2026 What's New and Reminders (election path unaffected)

- **Kind:** not encoded
- **2026:** `i1116` p. 2 (draft): "If section 904(b)(6) applies, enter the code “904(b)(6)” on Part I, line i." "P.L. 119-21 limits your itemized deductions if your taxable income exceeds certain amounts." "The enhanced deduction for seniors reported on Schedule 1-A (Form 1040), line 43, must be removed from taxable income for purposes of computing the foreign tax credit limitation."; p. 3: "Your total creditable foreign taxes aren’t more than $300 ($600 if married filing a joint return)."; p. 29: "Individuals. Enter the total of Form 1040, 1040-SR, or 1040-NR, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972 and less any tax included on line 16 that is with respect to a section 962 election."
- **2025:** `i1116` p. 1: "This deduction is reported on Schedule 1-A (Form 1040), line 37, and needs to be removed from taxable income for purposes of computing the foreign tax credit limitation." "Your total creditable foreign taxes aren’t more than $300 ($600 if married filing a joint return)."; p. 25: "line 1z, less any tax included on line 16 from Form 4972."
- **Touches:** ftc.limit (unchanged $300/$600), ftc.regular_tax, ftc.credit; gate scope.other_line16 (section 962 elections refused)
- **Worklist items:** none
- **Notes:**
  - **Election path unchanged.** The encoding claims the credit only by the election without Form 1116, so
    Part I line i, Part II, section 951A, the itemized deduction limit and the senior-deduction add-back
    (which applies to the Form 1116 limitation) are not encoded. The election's $300/$600 test is unchanged.
  - **Regular tax for the credit.** It now excludes tax on a section 962 election. That election is
    refused through scope.other_line16, so ftc.regular_tax needs only a new citation to p. 29.

### C-SCHED-39. Schedule 3: new line 13e (Form 1062 line 14) among other payments; lines 9–12 unchanged

- **Kind:** new line or form
- **2026:** `f1040s3` p. 2 (draft): "13e Total section 1062 applicable net tax liability. Enter amount from Form 1062," "Net premium tax credit. Attach Form 8962" "Total other payments or refundable credits. Add lines 13a through 13z" "Add lines 9 through 12 and 14. Enter here and on Form 1040, 1040-SR, or 1040-NR, line 31"
- **2025:** `f1040s3` p. 1: "Net premium tax credit. Attach Form 8962" "Total other payments or refundable credits. Add lines 13a through 13z" "Add lines 9 through 12 and 14. Enter here and on Form 1040, 1040-SR, or 1040-NR, line 31"
- **Touches:** s3.line14 (supplied subtotal), s3.line15, s3.line9
- **Worklist items:** s3.line9
- **Notes:**
  - **New line 13e.** It takes the Form 1062 line 14 amount. Form 1062 is covered by the Form 1040
    section. s3.line14 is a supplied subtotal, so the adoption decides whether 13e is computed from Form
    1062 or left inside the supplied total.
  - **s3.line9.** Its form text is unchanged. Its i1040gi p. 117 citation cannot be checked.

### Worklist coverage

| item id | entry |
|---|---|
| amb.2025.line8z_kinds | C-SCHED-28 |
| carloan.col_ii_input | C-SCHED-07 |
| f4952.line4g | C-SCHED-36 |
| f8959.line11 | C-SCHED-13 |
| f8959.line12 | C-SCHED-13 |
| f8959.line13 | C-SCHED-13 |
| f8959.line17 | C-SCHED-13 |
| f8959.line18 | C-SCHED-13 |
| f8960.carryforward_adj | C-SCHED-29 |
| f8960.line1 | C-SCHED-29 |
| f8960.line10 | C-SCHED-29 |
| f8960.line2 | C-SCHED-29 |
| f8960.line9b | C-SCHED-27 |
| f8960.prior_2i | C-SCHED-29 |
| f8960.unsupported | C-SCHED-29 |
| f8995.line15 | C-SCHED-31 |
| f8995a.line27 | C-SCHED-32 |
| f8995a.line28 | C-SCHED-32 |
| f8995a.line29 | C-SCHED-32 |
| f8995a.line30 | C-SCHED-32 |
| f8995a.line31 | C-SCHED-32 |
| f8995a.line32 | C-SCHED-32 |
| f8995a.line33 | C-SCHED-32 |
| f8995a.line34 | C-SCHED-32 |
| f8995a.line35 | C-SCHED-32 |
| f8995a.line36 | C-SCHED-32 |
| f8995a.line37 | C-SCHED-32 |
| f8995a.line38 | C-SCHED-32 |
| f8995a.line39 | C-SCHED-32 |
| f8995a.line40 | C-SCHED-32 |
| medicare.threshold | C-SCHED-14 |
| qbi.deduction | C-SCHED-31 |
| qbi.threshold | C-SCHED-30 |
| qbi.use_8995a | C-SCHED-30 |
| s1a.car_max | C-SCHED-02 |
| s1a.line10_pos | C-SCHED-01 |
| s1a.line12_calc | C-SCHED-01 |
| s1a.line13 | C-SCHED-01 |
| s1a.line18_pos | C-SCHED-01 |
| s1a.line20_calc | C-SCHED-01 |
| s1a.line21 | C-SCHED-01 |
| s1a.line27_pos | C-SCHED-01 |
| s1a.line29_calc | C-SCHED-01 |
| s1a.line33_over | C-SCHED-01 |
| s1a.line33_pos | C-SCHED-01 |
| s1a.line35_calc | C-SCHED-01 |
| s1a.line36b | C-SCHED-08 |
| s1a.line4c_one | C-SCHED-03 |
| s1a.ot_max_joint | C-SCHED-02 |
| s1a.ot_max_other | C-SCHED-02 |
| s1a.senior_amount | C-SCHED-02 |
| s1a.senior_rate | C-SCHED-02 |
| s1a.tips_max | C-SCHED-02 |
| s2.line1a | C-SCHED-10 |
| s2.line21 | C-SCHED-10 |
| s2.line8_box | C-SCHED-11 |
| s2.line8_file | C-SCHED-11 |
| s2.line8_must | C-SCHED-11 |
| s3.line10 | C-SCHED-12 |
| s3.line9 | C-SCHED-39 |
| s8812.amt_ws7 | C-SCHED-18 |
| s8812.clwb_10 | C-SCHED-20 |
| s8812.clwb_11_figured | C-SCHED-20 |
| s8812.clwb_12 | C-SCHED-20 |
| s8812.clwb_13 | C-SCHED-20 |
| s8812.clwb_14 | C-SCHED-20 |
| s8812.clwb_15 | C-SCHED-20 |
| s8812.line4 | C-SCHED-19 |
| s8812.line6 | C-SCHED-19 |
| s8812.show_iib | C-SCHED-21 |
| sli.interest | C-SCHED-37 |

## Credits: Forms 5695, 8880, 8863 and 2441

Read: the 2026 archive copies of `f5695`, `i5695`, `f2441`, `i2441`, `p503`, `f8880`, `f8863`, `i8863` (all IRS
drafts: 2026 statements from them are marked (draft)), `f1098t` and `i1098et` (final), plus the 2026 draft of
`i1040s8812` for one Form 5695 reader; compared with the 2025 archive copies and the 2025 encoding (`forms/2025/f5695.yaml`,
`f2441.yaml`, `dcprov.yaml`, `f8880.yaml`, `f8863.yaml`, `params/2025.yaml`, `tables/2025/dc_rate.yaml`,
`tables/2025/savers_rate.yaml`). The group file has 179 worklist items, 146 of them on Form 5695. The single change behind
all 146 is that the 2026 Form 5695 is no longer a credit computation: it is retitled "Carryforward of Residential Energy
Credit" and has four lines (carryforward in, tax-liability limit, credit, carryforward out). Part I's current-year
property lines, all of Part II (the energy efficient home improvement credit), its limit worksheet and every Form 5695 year
parameter have no 2026 counterpart; the items are grouped under that change by the part of the 2025 form they encode
(C-CRED-01 to C-CRED-09). Other notable changes: the child and dependent care credit percentage now runs from 50% down to
20% with separate bands for joint and other filers (C-CRED-10, a What's New item with no worklist item, because the line 8
encoding cites the form line, not the moved table); the dependent care exclusion rises from $5,000 to $7,500 (C-CRED-11);
Form 2441 Part I columns (a)–(e) become lines 1a–1e (C-CRED-12); the saver's credit AGI bands are re-indexed (C-CRED-15);
the education credits now require a valid SSN for the taxpayer (one spouse on a joint return) and a dependent student
(C-CRED-18), and Form 8863 reads Form 1040 line 11a instead of 11b (C-CRED-17). Sources not in the 2026 archive: IRS Fact
Sheet 2025-01 (cited by several 2025 Form 5695 lines; the year diff reports "no edition in one year"); the 2026
instructions point instead to Fact Sheet 2025-05, which is also not archived.

### What's New and Reminders accounted for

| document | item (quoted heading or first words) | entry or "not encoded: reason" |
|---|---|---|
| i5695 | Future Developments ("For the latest information about developments related to Form 5695") | not encoded: pointer to IRS.gov/Form5695 |
| i5695 | What's New, "Termination of credits." | C-CRED-01 (and C-CRED-02 to C-CRED-09) |
| i5695 | What's New, "For additional information and frequently asked questions ... see Fact Sheet 2025-05" | not encoded: pointer to a fact sheet not in the archive |
| i5695 | Purpose of Form, "Caution: You may claim only a carryforward of any unused residential clean energy credit" | C-CRED-03 |
| f5695 | (no What's New or caution printed on the 2026 form) | — |
| i2441 | Future Developments | not encoded: pointer to IRS.gov/Form2441 |
| i2441 | What's New, "Changes to the credit for child and dependent care expenses." | C-CRED-10 |
| i2441 | What's New, "Changes to dependent care benefits." | C-CRED-11 |
| i2441 | Reminders, "Married persons filing separately checkbox on line A." | not encoded: married filing separately is refused for Form 2441 (refusal on `s3.mfs` in `forms/2025/f2441.yaml`, "Form 2441 for married filing separately (line A; lines 19 and 21)"); the same reminder is printed in 2025 (i2441 p. 1); the form's line A now points to "the instructions under Line A" instead of "Married Persons Filing Separately" (wording only) |
| f2441 | (no What's New printed on the form) | — |
| p503 | Future Developments | not encoded: pointer to IRS.gov/Pub503 |
| p503 | What's New, "Changes to the credit for child and dependent care expenses." | C-CRED-10 |
| p503 | What's New, "Changes to dependent care benefits." | C-CRED-11 |
| p503 | Reminders, "Trump account and Form 4547." | not encoded: a Form 4547 election, not part of Form 2441; was a 2025 What's New item (p503 2025 p. 1) |
| p503 | Reminders, "Taxpayer identification number needed for each qualifying person." | not encoded as a change: the same reminder is printed in the 2025 edition (p503 2025 p. 1); the encoding stores no identifying numbers |
| f8880 | Future Developments | not encoded: pointer to www.irs.gov/Form8880 |
| f8880 | Reminders, "Permanent credit for Achieving a Better Life Experience (ABLE) account contributions." | C-CRED-16 (moved from What's New to Reminders; no rule change) |
| f8880 | Reminders, "New saver's match for qualified retirement contributions starting with 2027 tax returns filed in 2028." | not encoded: affects 2027 returns; the same paragraph was a 2025 What's New item |
| i8863 | Future Developments | not encoded: pointer to IRS.gov/Form8863 |
| i8863 | What's New, "Identification requirement." | C-CRED-18 |
| i8863 | Reminders, "Limits on modified adjusted gross income (MAGI)." | C-CRED-19 (unchanged) |
| i8863 | Reminders, "Form 1098-T requirement." | C-CRED-20 |
| i8863 | Reminders, "Caution: To claim the American opportunity credit, you must provide the educational institution's employer identification number (EIN)" | not encoded: the EIN is a string the data model does not hold; same caution in 2025 |
| i8863 | Reminders, "Ban on claiming the American opportunity credit." | not encoded as a change: same reminder in 2025; the encoding refuses it through `f8863.ban` / `f8863.ban_refused` |
| i8863 | Reminders, "Form 8862 may be required." | not encoded as a change: same reminder in 2025 ("any tax year beginning after 2015"); refused through `f8863.ban_refused` |
| f8863 | Form note, "Before you begin: A valid social security number (SSN) is now required to claim an education credit." | C-CRED-18 |
| i1098et | Future Developments | not encoded: pointer to IRS.gov/Form1098E and IRS.gov/Form1098T |
| i1098et | What's New, "Address fields." | not encoded: filer-side layout of Form 1098-T (separate address boxes); nothing the encoding reads |
| i1098et | What's New, "E-filing returns." | not encoded: information-return filing mechanics (same item printed in 2025) |
| i1098et | What's New, "Information Reporting Intake System (IRIS)." | not encoded: filing mechanics (same item printed in 2025) |
| i1098et | Reminders, "General instructions." / "Online fillable Copy B." / "Form W-9S." / "Electronic submission of Form W-9S." | not encoded: filer obligations and filing mechanics |
| f1098t | (no What's New, Reminders or Future Developments printed) | — |

### C-CRED-01. Form 5695 becomes a carryforward-only form

- **Kind:** new line or form
- **2026:** `f5695` p. 2 (draft): "Carryforward of Residential Energy Credit"; `i5695` p. 2 (draft): "Termination of credits. You can’t claim residential clean energy credits for expenditures made after December 31, 2025. You can’t claim energy efficient home improvement credits for expenditures or property placed in service after December 31, 2025."
- **2025:** `f5695` p. 1: "Residential Energy Credits"; `i5695` p. 1: "Use Form 5695 to figure and take your residential energy credits."
- **Touches:** the whole of `forms/2025/f5695.yaml` (form title and note); `scope.credits` (its label names "the residential energy credits (Form 5695)")
- **Worklist items:** none directly (the items are in C-CRED-02 to C-CRED-09)
- **Notes:** The 2026 form keeps only Part I's carryforward tail (C-CRED-03, C-CRED-04); Part I's current-year property lines (C-CRED-02) and all of Part II (C-CRED-06 to C-CRED-08) disappear, so Schedule 3 line 5b no longer has a Form 5695 source (the Schedule 3 owner should confirm from the 2026 Schedule 3). The termination sentence was already printed in the 2025 What's New (i5695 p. 1), so 2025 returns are unaffected; the scope question's wording should become "the residential clean energy credit carryforward (Form 5695)".

### C-CRED-02. Part I current-year property costs (lines 1 to 11) removed

- **Kind:** new line or form
- **2026:** `i5695` p. 2 (draft): "You can’t claim residential clean energy credits for expenditures made after December 31, 2025."; `i5695` p. 2 (draft): "Caution: You may claim only a carryforward of any unused residential clean energy credit (which is shown on your prior-year Form 5695, line 16)." (no counterpart for lines 1 to 11)
- **2025:** `f5695` p. 1: "Qualified solar electric property costs"; `f5695` p. 1: "Multiply line 6a by 30% (0.30)"; `f5695` p. 1: "Qualified fuel cell property. Was qualified fuel cell property installed on, or in connection with, your main home located in the United States?"; `i5695` p. 1: "If less than 80% of the use of an item is for nonbusiness purposes, only that portion of the costs that is allocable to the nonbusiness use can be used to determine either credit."
- **Touches:** `f5695.line1`, `f5695.line2`, `f5695.line3`, `f5695.line4`, `f5695.line5a`, `f5695.battery_cost`, `f5695.line5b`, `f5695.line6a` (and its refusals on `f5695.business_use` and `f5695.construction_later`), `f5695.rce_rate`, `f5695.line6b`, `f5695.line7a`, `f5695.line11` (and its refusal on `f5695.line7a`), `f5695.business_use`, `f5695.construction_later`, `f5695.zero`; ambiguities `amb.2025.f5695_battery_second_home`, `amb.2025.multiplication_subcent` (reader `f5695.line6b`)
- **Worklist items:** `f5695.business_use` (line), `f5695.construction_later` (line), `f5695.line1` (line), `f5695.line2` (line), `f5695.line3` (line), `f5695.line4` (line), `f5695.line5a` (line), `f5695.line5b` (line), `f5695.battery_cost` (line), `f5695.line6a` (refusal), `f5695.rce_rate` (line), `f5695.line7a` (line), `f5695.line11` (line), `f5695.line11` (refusal), `amb.2025.f5695_battery_second_home` (ambiguity)
- **Notes:** Retire these lines, the two Part I refusals (business use, construction) and the fuel cell refusal for 2026: with no current-year cost the questions they answer are not asked. The 2025 cites to Fact Sheet 2025-01 (lines 1, 18a, 21a, `f5695.b_new_home`) have no 2026 edition in the archive.

### C-CRED-03. Carryforward lines renumbered and rolled forward (2025 lines 12, 13, 15, 16 become lines 1, 3, 4)

- **Kind:** new line or form
- **2026:** `f5695` p. 2 (draft): "Credit carryforward from 2025. Enter the amount, if any, from your 2025 Form 5695, line 16"; `f5695` p. 2 (draft): "Residential clean energy credit. Enter the smaller of line 1 or line 2. Also include this amount on Schedule 3 (Form 1040), line 5a"; `f5695` p. 2 (draft): "Credit carryforward to 2027. If line 3 is less than line 1, subtract line 3 from line 1"; `i5695` p. 2 (draft): "Use Form 5695 to take any residential clean energy credit carryforward from 2025 or to carry the unused portion of the residential clean energy credit to 2027."; `i5695` p. 2 (draft): "If you can’t use all of the credit because of the tax liability limit (that is, line 2 is less than line 1), you can carry the unused portion of the credit to 2027."
- **2025:** `f5695` p. 1: "Credit carryforward from 2024. Enter the amount, if any, from your 2024 Form 5695, line 16"; `f5695` p. 1: "Add lines 6b, 11, and 12"; `f5695` p. 1: "Residential clean energy credit. Enter the smaller of line 13 or line 14. Also include this amount on Schedule 3 (Form 1040), line 5a"; `i5695` p. 1: "Also use Form 5695 to take any residential clean energy credit carryforward from 2024 or to carry the unused portion of the residential clean energy credit to 2026."; `i5695` p. 5: "If you can't use all of the credit because of the tax liability limit (that is, line 14 is less than line 13), you can carry the unused portion of the credit to 2026."
- **Touches:** `f5695.part1_any`, `f5695.line12`, `f5695.line13`, `f5695.line14`, `f5695.line15`, `f5695.line16`
- **Notes:** Re-encode as 2026 line 1 (input: 2025 Form 5695 line 16), line 2 (worksheet, C-CRED-04), line 3 = smaller of line 1 and line 2 (to Schedule 3 line 5a), line 4 = line 1 less line 3; 2025 line 13 (the sum of lines 6b, 11 and 12) has no counterpart because line 1 is the only source. `f5695.part1_any` becomes a carryforward-only question ("from line 16 of your 2025 Form 5695"). The 2026 text names only the 2025 line 16 carryforward; it does not say whether a 2024 carryforward still unused after 2025 is reached other than through 2025 line 16 (which already includes it, being line 13 less line 15).
- **Worklist items:** `f5695.part1_any` (line), `f5695.line12` (line), `f5695.line14` (line), `f5695.line16` (line)

### C-CRED-04. Residential Clean Energy Credit Limit Worksheet now for line 2, without the Part II credit

- **Kind:** rule (definition change)
- **2026:** `i5695` p. 2 (draft): "Residential Clean Energy Credit Limit Worksheet—Line 2"; `i5695` p. 2 (draft): "Subtract line 2 from line 1. Also enter this amount on Form 5695, line 2. If zero or less, enter -0- on Form 5695, lines 2 and 3"; `i5695` p. 2 (draft): "Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 18"; `i5695` p. 2 (draft): "Include the amount in the instructions for Schedule 8812 (Form 1040), Credit Limit Worksheet B, line 14, instead of the amount from Form 1040, 1040-SR, or 1040-NR, line 19, if the instructions for Schedule 8812 (Form 1040) direct you to complete Credit Limit Worksheet B." (the line 2 list runs Schedule 3 lines 6l, 1, 2, 6d, 3, 4, 6m, 6f, Form 1040 line 19, Schedule 3 lines 6g, 6c, 6h; no Form 5695 line)
- **2025:** `i5695` p. 5: "Residential Clean Energy Credit Limit Worksheet—Line 14"; `i5695` p. 5: "+ Energy efficient home improvement credit, Form 5695, line 32"; `i5695` p. 5: "Subtract line 2 from line 1. Also enter this amount on Form 5695, line 14. If zero or less, enter -0- on Form 5695, lines 14 and 15"
- **Touches:** `f5695.rce_ws1`, `f5695.rce_ws2` (and its refusal on `scope.credits`), `f5695.rce_ws3`, `f5695.ctc`, `f5695.ctc_line19`, `f5695.line14`
- **Worklist items:** `f5695.rce_ws1` (line), `f5695.rce_ws2` (line), `f5695.rce_ws2` (refusal), `f5695.rce_ws3` (line), `f5695.ctc` (line)
- **Notes:** Drop `s3.line5b` from the `f5695.rce_ws2` sum (2026 has no "Form 5695, line 32" entry) and point worksheet line 3 at 2026 line 2; the other entries, the Form 1040 line 18 start and the Credit Limit Worksheet B footnote are unchanged in substance, so `f5695.rce_ws1`, `f5695.rce_ws3` and `f5695.ctc` need only new cites ("Line 2" heading, p. 2). The 2026 note reads "Not all credits/adjustments are available for all years or for all filers" where 2025 had "nor" (wording).

### C-CRED-05. Schedule 8812 Credit Limit Worksheets: "Form 5695, Part I" becomes "Form 5695"; Schedule 3 line 5b dropped

- **Kind:** rule (definition change)
- **2026:** `i1040s8812` p. 5 (draft): "c. Residential clean energy credit, Form 5695."; Credit Limit Worksheet A line 2 list on `i1040s8812` p. 5 (draft) runs "Schedule 3, line 4" then "Schedule 3, line 6d" with no line 5b
- **2025:** `i1040s8812` p. 4: "c. Residential clean energy credit, Form 5695, Part I."; `i1040s8812` p. 4: "Schedule 3, line 5b"
- **Touches:** `f5695.claiming_part1`, `s8812.clw_a2` (reads `s3.line5b`), ambiguity `amb.2025.clwb_claiming_part1`
- **Worklist items:** `f5695.claiming_part1` (line)
- **Notes:** `f5695.claiming_part1` should test the 2026 carryforward credit (line 1 or line 3 more than zero) instead of Part I line 13, and its cite move to p. 5; whether `amb.2025.clwb_claiming_part1` still arises needs a re-read against the 2026 wording. `s8812.clw_a2` belongs to the Schedule 8812 group, flagged here because it read the Part II credit.

### C-CRED-06. Part II, Section A (lines 17a to 20d, qualified energy efficiency improvements) removed

- **Kind:** new line or form
- **2026:** `i5695` p. 2 (draft): "You can’t claim energy efficient home improvement credits for expenditures or property placed in service after December 31, 2025." (no counterpart for Section A)
- **2025:** `f5695` p. 2: "Section A—Qualified Energy Efficiency Improvements"; `f5695` p. 2: "Multiply line 18a by 30% (0.30). Enter the results. Do not enter more than $1,200"; `i5695` p. 1: "you must include the four-character alphanumeric unique qualified manufacturer identification number (QMID) for each item."
- **Touches:** `f5695.part2_any`, `f5695.line17a`, `f5695.line17b`, `f5695.line17c`, `f5695.sec_a_claimed`, `f5695.line17e`, `f5695.sec_a_new_home`, `f5695.eehi_rate`, `f5695.line18a`, `f5695.ins_30`, `f5695.insulation_max`, `f5695.ins_capped`, `f5695.line18b`, `f5695.line19a`, `f5695.door1_30`, `f5695.door_max`, `f5695.line19c`, `f5695.line19d_i`, `f5695.line19d_ii`, `f5695.line19e`, `f5695.line19f`, `f5695.line19g`, `f5695.doors_sum`, `f5695.doors_max`, `f5695.doors_cost`, `f5695.qmid_doors`, `f5695.doors_no_qmid`, `f5695.doors_capped` (and its refusal), `f5695.line19h`, `f5695.line20a_i` to `f5695.line20a_iv`, `f5695.line20b`, `f5695.line20c`, `f5695.windows_30`, `f5695.windows_max`, `f5695.qmid_windows`, `f5695.windows_no_qmid`, `f5695.windows_capped` (and its refusal), `f5695.line20d`; ambiguity `amb.2025.f5695_17abc_section_a`
- **Worklist items:** `f5695.part2_any` (line), `f5695.line17a` (line), `f5695.line17b` (line), `f5695.line17c` (line), `f5695.line17e` (line), `f5695.sec_a_claimed` (line), `f5695.sec_a_new_home` (line), `f5695.eehi_rate` (line), `f5695.line18a` (line), `f5695.ins_30` (line), `f5695.insulation_max` (line), `f5695.ins_capped` (line), `f5695.line18b` (line), `f5695.line19a` (line), `f5695.door1_30` (line), `f5695.door_max` (line), `f5695.line19d_i` (line), `f5695.line19d_ii` (line), `f5695.line19e` (line), `f5695.doors_sum` (line), `f5695.doors_max` (line), `f5695.doors_cost` (line), `f5695.qmid_doors` (line), `f5695.doors_no_qmid` (line), `f5695.doors_capped` (line), `f5695.doors_capped` (refusal), `f5695.line19h` (line), `f5695.line20a_i` (line), `f5695.line20a_ii` (line), `f5695.line20a_iii` (line), `f5695.line20a_iv` (line), `f5695.line20b` (line), `f5695.windows_30` (line), `f5695.windows_max` (line), `f5695.qmid_windows` (line), `f5695.windows_no_qmid` (line), `f5695.windows_capped` (line), `f5695.windows_capped` (refusal), `f5695.line20d` (line), `amb.2025.f5695_17abc_section_a` (ambiguity)
- **Notes:** Retire for 2026; Part II produces nothing, so Schedule 3 line 5b loses its Form 5695 source. No 2026 text says the same thing elsewhere; the "quote printed in one year only" findings are all explained by the removal.

### C-CRED-07. Part II, Section B (lines 21a to 29h, residential energy property expenditures) removed

- **Kind:** new line or form
- **2026:** `i5695` p. 2 (draft): "You can’t claim energy efficient home improvement credits for expenditures or property placed in service after December 31, 2025." (no counterpart for Section B)
- **2025:** `f5695` p. 3: "Section B—Residential Energy Property Expenditures"; `f5695` p. 3: "Multiply line 22c by 30% (0.30). Enter the results. Do not enter more than $600"; `f5695` p. 4: "Enter the smaller of line 27 or $1,200"
- **Touches:** `f5695.line21a`, `f5695.line21b`, `f5695.sec_b_claimed`, `f5695.b_new_home`, `f5695.sec_b_new_home`, `f5695.item_max`, `f5695.line22a`, `f5695.line22b`, `f5695.line22c`, `f5695.ac_30`, `f5695.qmid_ac`, `f5695.ac_no_qmid`, `f5695.ac_capped` (and its refusal), `f5695.line22d`, `f5695.line23a_i`, `f5695.line23a_ii`, `f5695.line23b`, `f5695.line23c`, `f5695.wh_30`, `f5695.qmid_wh`, `f5695.wh_no_qmid`, `f5695.wh_capped` (and its refusal), `f5695.line23d`, `f5695.line24a`, `f5695.line24b`, `f5695.line24c`, `f5695.furnace_30`, `f5695.qmid_furnace`, `f5695.furnace_no_qmid`, `f5695.furnace_capped` (and its refusal), `f5695.line24d`, `f5695.line25a`, `f5695.enabling_claimed`, `f5695.line25c`, `f5695.enabling_30`, `f5695.qmid_enabling`, `f5695.enabling_no_qmid`, `f5695.enabling_capped` (and its refusal), `f5695.line25e`, `f5695.line26a`, `f5695.line26b`, `f5695.audit_30`, `f5695.audit_max`, `f5695.audit_capped`, `f5695.line26c`, `f5695.line27`, `f5695.annual_max`, `f5695.line28`, `f5695.line29a` to `f5695.line29g`, `f5695.hp_30`, `f5695.heat_pump_max`, `f5695.qmid_hp`, `f5695.hp_no_qmid`, `f5695.hp_capped` (and its refusal), `f5695.line29h`; ambiguity `amb.2025.f5695_category_cap`
- **Worklist items:** `f5695.line21a` (line), `f5695.line21b` (line), `f5695.sec_b_claimed` (line), `f5695.b_new_home` (line), `f5695.sec_b_new_home` (line), `f5695.item_max` (line), `f5695.line22a` (line), `f5695.line22b` (line), `f5695.ac_30` (line), `f5695.qmid_ac` (line), `f5695.ac_no_qmid` (line), `f5695.ac_capped` (line), `f5695.ac_capped` (refusal), `f5695.line22d` (line), `f5695.line23a_i` (line), `f5695.line23a_ii` (line), `f5695.line23b` (line), `f5695.wh_30` (line), `f5695.qmid_wh` (line), `f5695.wh_no_qmid` (line), `f5695.wh_capped` (line), `f5695.wh_capped` (refusal), `f5695.line23d` (line), `f5695.line24a` (line), `f5695.line24b` (line), `f5695.furnace_30` (line), `f5695.qmid_furnace` (line), `f5695.furnace_no_qmid` (line), `f5695.furnace_capped` (line), `f5695.furnace_capped` (refusal), `f5695.line24d` (line), `f5695.line25a` (line), `f5695.enabling_claimed` (line), `f5695.line25c` (line), `f5695.enabling_30` (line), `f5695.qmid_enabling` (line), `f5695.enabling_no_qmid` (line), `f5695.enabling_capped` (line), `f5695.enabling_capped` (refusal), `f5695.line25e` (line), `f5695.line26a` (line), `f5695.line26b` (line), `f5695.audit_30` (line), `f5695.audit_max` (line), `f5695.audit_capped` (line), `f5695.line26c` (line), `f5695.annual_max` (line), `f5695.line29a` (line), `f5695.line29b` (line), `f5695.line29c` (line), `f5695.line29d` (line), `f5695.line29e` (line), `f5695.line29f` (line), `f5695.hp_30` (line), `f5695.heat_pump_max` (line), `f5695.qmid_hp` (line), `f5695.hp_no_qmid` (line), `f5695.hp_capped` (line), `f5695.hp_capped` (refusal), `f5695.line29h` (line), `amb.2025.f5695_category_cap` (ambiguity)
- **Notes:** Retire for 2026, together with the QMID attestations and their "no QMID" refusals. The 2025 enabling property line (25a) asked about property "installed in 2025"; nothing in 2026 replaces it.

### C-CRED-08. Part II totals, limit worksheet and statements (lines 30 to 32b) removed

- **Kind:** new line or form
- **2026:** `i5695` p. 2 (draft): "You can’t claim energy efficient home improvement credits for expenditures or property placed in service after December 31, 2025." (no counterpart for lines 30 to 32b or the Energy Efficient Home Improvement Credit Limit Worksheet)
- **2025:** `f5695` p. 4: "Energy efficient home improvement credit. Enter the smaller of line 30 or line 31. Also include this amount on Schedule 3 (Form 1040), line 5b"; `i5695` p. 7: "Energy Efficient Home Improvement Credit Limit Worksheet—Line 31"; `i5695` p. 7: "Occupants of a condominium or cooperative who are claiming a fractional share of the qualified energy efficiency improvements or residential energy property costs must check the box on line 32b."
- **Touches:** `f5695.line30` (and its refusals on `f5695.business_use`, `f5695.joint_occupancy`, `f5695.separate_homes_joint`, `f5695.sec_a_new_home`, `f5695.sec_b_new_home`), `f5695.joint_occupancy`, `f5695.separate_homes`, `f5695.separate_homes_joint`, `f5695.eehi_ws1`, `f5695.eehi_ws2` (and its refusal), `f5695.eehi_ws3`, `f5695.line31`, `f5695.eehi_credit`, `f5695.line32`, `f5695.line32a`, `f5695.condo`, `f5695.line32b`
- **Worklist items:** `f5695.line30` (refusal), `f5695.joint_occupancy` (line), `f5695.separate_homes` (line), `f5695.separate_homes_joint` (line), `f5695.eehi_ws1` (line), `f5695.eehi_ws2` (line), `f5695.eehi_ws2` (refusal), `f5695.eehi_ws3` (line), `f5695.line31` (line), `f5695.eehi_credit` (line), `f5695.line32a` (line), `f5695.condo` (line), `f5695.line32b` (line)
- **Notes:** Retire for 2026. Downstream readers of `f5695.line32` (Schedule 3 line 5b, `f5695.rce_ws2` via `s3.line5b`, `s8812.clw_a2`) must stop reading it (C-CRED-04, C-CRED-05).

### C-CRED-09. Form 5695 year parameters: no 2026 value

- **Kind:** new line or form
- **2026:** `i5695` p. 2 (draft): "You can’t claim residential clean energy credits for expenditures made after December 31, 2025. You can’t claim energy efficient home improvement credits for expenditures or property placed in service after December 31, 2025." (no rate or dollar limit is printed anywhere in the 2026 form or instructions)
- **2025:** `f5695` p. 1: "Multiply line 6a by 30% (0.30)"; `f5695` p. 4: "Enter the smaller of line 27 or $1,200"; `f5695` p. 4: "Multiply line 29g by 30% (0.30). Enter the results. Do not enter more than $2,000"
- **Touches:** parameters `f5695.rce_rate`, `f5695.eehi_rate`, `f5695.insulation_max`, `f5695.door_max`, `f5695.doors_max`, `f5695.windows_max`, `f5695.item_max`, `f5695.audit_max`, `f5695.annual_max`, `f5695.heat_pump_max`
- **Worklist items:** `f5695.rce_rate` (parameter), `f5695.eehi_rate` (parameter), `f5695.insulation_max` (parameter), `f5695.door_max` (parameter), `f5695.doors_max` (parameter), `f5695.windows_max` (parameter), `f5695.item_max` (parameter), `f5695.audit_max` (parameter), `f5695.annual_max` (parameter), `f5695.heat_pump_max` (parameter)
- **Notes:** The "probable value change" findings are not value changes: the figures are not printed because the lines that carry them are gone (C-CRED-02, C-CRED-06, C-CRED-07). Leave these parameters out of `params/2026.yaml`. Note that the 2026 worksheet carries no rate, so the 2025 carryforward is used at face value.

### C-CRED-10. Child and dependent care credit percentage: 50% to 20%, with separate bands for joint and other filers

- **Kind:** rule (definition change)
- **2026:** `i2441` p. 2 (draft): "Beginning in 2026, the maximum percentage used to figure the credit for child and dependent care expenses is increased from 35% to 50%, and higher adjusted gross income phaseout thresholds apply."; `i2441` p. 2 (draft): "Different phaseout thresholds apply for joint filers and other filers."; `f2441` p. 2 (draft): "Enter on line 8 the decimal amount that applies to the amount on line 7. See instructions for the amount to enter"; `i2441` p. 6 (draft): "2026 Phaseout Schedule"; `i2441` p. 6 (draft): "If your filing status is married filing jointly and line 7 is..."; `i2441` p. 6 (draft): "If your filing status is any other filing status and line 7 is..." (rows: $0–$15,000 .50, then .01 lower for each $2,000 to .36 at $41,000–$43,000; .35 from $43,000 to $150,000 (joint) or $75,000 (other); then .01 lower for each $4,000 (joint) or $2,000 (other) to .20 over $206,000 (joint) or $103,000 (other))
- **2025:** `f2441` p. 1: "Enter on line 8 the decimal amount shown below that applies to the amount on line 7."; `f2441` p. 1: "43,000—No limit .20"
- **Touches:** `f2441.line8` (table `dc_rate`, `tables/2025/dc_rate.yaml`), ambiguity `amb.2025.dc_rate_nonpositive_agi`; `f2441.line9a` (reader)
- **Worklist items:** none (What's New item; `f2441.line8` cites the form line, whose quote is not affected)
- **Notes:** Build a 2026 `dc_rate` table with two columns (married filing jointly; all other statuses, of which married filing separately is refused) from i2441 p. 6, and cite i2441 Line 8 (p. 5, "Use the table that follows to find the decimal amount that applies to the amount on line 7. Enter that decimal amount on line 8.") instead of the form, which no longer prints the table. Worksheet A (line 9b, 2025 expenses paid in 2026) keeps the 2025 single table (i2441 p. 8) but is refused through `f2441.prior_year`. Re-check whether `amb.2025.dc_rate_nonpositive_agi` still applies (the first band is again printed "$0 – $15,000").

### C-CRED-11. Dependent care exclusion limit $5,000 to $7,500 ($2,500 to $3,750 married filing separately)

- **Kind:** amount (parameter)
- **2026:** `f2441` p. 3 (draft): "Enter $7,500 ($3,750 if married filing separately and you were required to enter your spouse’s earned income on line 19)."; `i2441` p. 7 (draft): "Beginning in 2026, employers may increase the maximum amount that can be excluded from an employee’s income through a dependent care assistance program. The maximum amount is increased to $7,500 (previously $5,000)."; `i2441` p. 7 (draft): "Your employer can tell you whether your dependent care plan was amended to increase the amount that can be excluded."; `i2441` p. 7 (draft): "For example, if your dependent care plan only allows a maximum of $5,000 to be excluded, substitute $5,000 for the $7,500 amount to enter on line 21."
- **2025:** `f2441` p. 2: "Enter $5,000 ($2,500 if married filing separately and you were required to enter your spouse’s earned income on line 19)."; `i2441` p. 5: "For 2025, the maximum amount that can be excluded from your income through a dependent care assistance program is $5,000 ($2,500 if married filing separately)."; `i2441` p. 5: "For example, if your dependent care plan only allows a maximum of $4,000 to be excluded, substitute $4,000 for the $5,000 amount to enter on line 21."
- **Touches:** parameter `dc.exclusion_max` (500000 to 750000); `f2441.exclusion_max`, `f2441.plan_max`, `f2441.line21` (and its refusal on `f2441.plans_differ`); ambiguity `amb.2025.dc_plan_maximum`
- **Worklist items:** `dc.exclusion_max` (parameter), `f2441.exclusion_max` (line), `f2441.plan_max` (line)
- **Notes:** Set `dc.exclusion_max` to $7,500 and recite it to i2441 p. 7 Line 21 (the 2025 "For 2025, the maximum amount ... is $5,000" sentence is not printed in 2026; the same rule is stated as "The maximum amount is increased to $7,500"). The `f2441.plan_max` prompt ("enter $5,000 if the plan allows $5,000 or more") must change to $7,500, and since the higher limit applies only if the employer amended the plan, the plan maximum now binds far more often; the 2026 example (plan $5,000) makes that the expected case. The married-filing-separately $3,750 is not reached (refused).
- **Correction (verification):** touches also `w2.box10` and `w2.box10_wages`, whose text names the $5,000 exclusion. The final `iw2w3` p. 19 still prints "including those in excess of the $5,000 exclusion", against the `i2441` draft's $7,500 (which applies only if the plan was amended): resolve at adoption (`changes.verification.md`).

### C-CRED-12. Form 2441 Part I: columns (a) to (e) become lines 1a to 1e

- **Kind:** new line or form
- **2026:** `f2441` p. 2 (draft): "1a Care provider’s name"; `i2441` p. 4 (draft): "Complete lines 1a through 1e for each person or organization that provided the care."; `i2441` p. 4 (draft): "If you have more than three care providers, check the box at the top of Part I and attach a statement to your return with the required information."; `i2441` p. 4 (draft): "Enter “See Attached Statement” on any line for which you don’t have the information."; `i2441` p. 4 (draft): "Don’t list an ineligible related individual as a care provider in Part I."; `i2441` p. 4 (draft): "If you were covered by your employer’s dependent care plan and your employer furnished the care (either at your workplace or by hiring a care provider), enter your employer’s name on line 1a. Then enter “See W-2” on line 1b, leave line 1c blank, check the “No” box on line 1d, and enter -0- on line 1e."; `i2441` p. 4 (draft): "Enter the total amount you actually paid in 2026 to the care provider. Also include amounts your employer paid to a third party on your behalf. It doesn’t matter when the expenses were incurred. Don’t reduce this amount by any reimbursement you received."
- **2025:** `f2441` p. 1: "1 (a) Care provider’s"; `i2441` p. 2: "Complete columns (a) through (e) for each person or organization that provided the care."; `i2441` p. 2: "If you have more than three care providers, check the box above line 1 and attach a statement to your return with the required information."; `i2441` p. 3: "Enter “See Attached Statement” in the columns for which you don't have the information."; `i2441` p. 3: "Don't list an ineligible related individual as a care provider on line 1."; `i2441` p. 3: "enter your employer's name in column (a). Then, enter “See W-2” in column (b), leave column (c) blank, check the “No” box in column (d), and enter -0- in column (e)."; `i2441` p. 3: "Enter the total amount you actually paid in 2025 to the care provider. Also, include amounts your employer paid to a third party on your behalf."
- **Touches:** collection `dcprov` and `dcprov.one`, `dcprov.tin_kind` (printed 1(c)), `dcprov.household` (printed 1(d)), `dcprov.paid` (printed 1(e)), `dcprov.see_statement`; parameters `dc.one`, `dc.providers_listed`; `f2441.provider_count`, `f2441.line1_box`, `f2441.statement_count`, `f2441.provider_ineligible`, `f2441.line1_paid`, `f2441.employer_care`, `f2441.employer_care_gate`, `f2441.paid_2026`, `f2441.line17` (refusal on `f2441.employer_care_l16`), `f2441.line30` (refusal on `f2441.employer_care_gate`); ambiguities `amb.2025.dc_ineligible_providers`, `amb.2025.dc_employer_care_value`, `amb.2025.dc_line30`
- **Worklist items:** `dcprov` (collection), `dcprov.one` (line), `dcprov.paid` (line), `dcprov.see_statement` (line), `dcprov.tin_kind` (line), `dc.one` (parameter), `dc.providers_listed` (parameter), `f2441.provider_count` (line), `f2441.line1_box` (line), `f2441.statement_count` (line), `f2441.provider_ineligible` (line), `f2441.line1_paid` (line), `f2441.employer_care` (line), `f2441.employer_care_gate` (line), `f2441.paid_2026` (line), `f2441.line17` (refusal), `f2441.line30` (refusal)
- **Notes:** Layout only: the provider data, the three-provider limit (still "more than three", so `dc.providers_listed` stays 3), the "See Attached Statement", "See W-2" and ineligible-provider rules are unchanged. Re-label printed numbers 1(c)/1(d)/1(e) as 1c/1d/1e and re-cite every quote to the new wording and pages (i2441 p. 4; 2025 pp. 2–3); the year in "paid in 2026" rolls. "Columns (a) and (b)" headings become "Lines 1a and 1b"; Part II line 2 still uses columns (a)–(d).

### C-CRED-13. Credit Limit Worksheet line 3: comma added

- **Kind:** wording only
- **2026:** `i2441` p. 6 (draft): "Subtract line 2 from line 1. Also, enter this amount on Form 2441, line 10. But if zero or less, stop; you can’t take the credit"
- **2025:** `i2441` p. 5: "Subtract line 2 from line 1. Also enter this amount on Form 2441, line 10. But if zero or less, stop; you can’t take the credit"
- **Touches:** `f2441.clw3`
- **Worklist items:** `f2441.clw3` (line)
- **Notes:** Re-quote the cite ("Also, enter") and move it to p. 6. The worksheet's lines 1 and 2 are unchanged.

### C-CRED-14. Qualifying person: disabled person's gross income test $5,200 to $5,300

- **Kind:** amount (parameter)
- **2026:** `i2441` p. 2 (draft): "a. The disabled person had gross income of $5,300 or more,"
- **2025:** `i2441` p. 1: "a. The disabled person had gross income of $5,200 or more,"
- **Touches:** `f2441.nondependent` (the amount is a literal in its input prompt and cite); parameter `qr.gross_income_limit` holds the same 2025 figure for the dependent tests (another group)
- **Worklist items:** none (not flagged by the year diff)
- **Notes:** Update the literal in the `f2441.nondependent` prompt to $5,300 (or read it from the 2026 value of `qr.gross_income_limit` once that group confirms it).
- **Correction (verification):** `qr.gross_income_limit` is $5,300 for 2026 (`rp-25-32` p. 20, final, "the exemption amount referred to in § 152(d)(1)(B) is $5,300."); proposed in step 4 (`changes.verification.md`).

### C-CRED-15. Saver's credit AGI limits and line 9 bands re-indexed

- **Kind:** amount (parameter)
- **2026:** `f8880` p. 2 (draft): "The amount on Form 1040, 1040-SR, or 1040-NR, line 11a, is more than $40,250 ($60,375 if head of household; $80,500 if married filing jointly)."; `f8880` p. 2 (draft): "$80,500 --- 0.0 0.0 0.0" (band edges $24,250, $26,250, $36,375, $39,375, $40,250, $48,500, $52,500, $60,375, $80,500, rates unchanged)
- **2025:** `f8880` p. 1: "The amount on Form 1040, 1040-SR, or 1040-NR, line 11a, is more than $39,500 ($59,250 if head of household; $79,000 if married filing jointly)."; `f8880` p. 1: "$79,000 --- 0.0 0.0 0.0" (band edges $23,750, $25,500, $35,625, $38,250, $39,500, $47,500, $51,000, $59,250, $79,000)
- **Touches:** parameter `savers.agi_limit` (single/mfs/qss 3950000 to 4025000; hoh 5925000 to 6037500; mfj 7900000 to 8050000); `f8880.agi_limit`, `f8880.past9`; table `savers_rate` (`tables/2025/savers_rate.yaml`), read by `f8880.line9`
- **Worklist items:** `f8880.agi_limit` (line), `f8880.past9` (line), `savers.agi_limit` (parameter)
- **Notes:** Update `savers.agi_limit` and every band edge of `savers_rate` (the 0.5/0.2/0.1/0.0 pattern per column is the same); refresh the label of `f8880.agi_limit` and the cites. The cap of $2,000 on line 6 (`savers.cap`) is unchanged on the 2026 form.

### C-CRED-16. Form 8880 year roll (age cutoff, distribution testing period) and ABLE reminder

- **Kind:** wording only
- **2026:** `f8880` p. 2 (draft): "(a) was born after January 1, 2009; (b) is claimed as a dependent on someone else’s 2026 tax return; or (c) was a student"; `f8880` p. 2 (draft): "Certain distributions received after 2023 and before the due date (including extensions) of your 2026 tax return"; `f8880` p. 3 (draft): "P.L. 119-21 made permanent the credit for contributions by a designated beneficiary to their ABLE account."
- **2025:** `f8880` p. 1: "(a) was born after January 1, 2008; (b) is claimed as a dependent on someone else’s 2025 tax return; or (c) was a student"; `f8880` p. 1: "Certain distributions received after 2022 and before the due date (including extensions) of your 2025 tax return"; `f8880` p. 2: "P.L. 119-21, commonly known as the One Big Beautiful Bill Act, makes permanent the credit for contributions by a designated beneficiary to their ABLE account."
- **Touches:** `person.sav_born`, `person.sav_ineligible`, `f8880.inelig_a`, `f8880.inelig_b`, `person.sav_dist`, `f8880.dist_2025`, `f8880.prior_joint`, `f8880.prior_own_a`, `f8880.prior_own_b`, `f8880.line4a`, `f8880.line4b` (years in prompts, labels and cites)
- **Worklist items:** none
- **Notes:** The rule is the same with every year moved by one; the birth-date cutoff and the distribution window (now 2024, 2025, 2026 and 2027 before the due date) are literals in the input prompts and must be rolled. The ABLE paragraph moved from What's New to Reminders and now reads "made permanent".

### C-CRED-17. Form 8863 lines 3 and 14 read Form 1040 line 11a instead of 11b

- **Kind:** wording only (cross-reference)
- **2026:** `f8863` p. 2 (draft): "Enter the amount from Form 1040 or 1040-SR, line 11a."; `i8863` p. 9 (draft): "Generally, your MAGI is the amount on your Form 1040 or 1040-SR, line 11a."; `i8863` p. 4 (draft): "add to the amount on your Form 1040 or 1040-SR, line 11a, the amount of income you excluded."
- **2025:** `f8863` p. 1: "Enter the amount from Form 1040 or 1040-SR, line 11b."; `i8863` p. 8: "Generally, your MAGI is the amount on your Form 1040 or 1040-SR, line 11b."; `i8863` p. 3: "add to the amount on your Form 1040 or 1040-SR, line 11b, the amount of income you excluded."
- **Touches:** `f8863.line3`, `f8863.line14` (and their refusals on `sa.excluded_income`)
- **Worklist items:** `f8863.line3` (line), `f8863.line3` (refusal), `f8863.line14` (line), `f8863.line14` (refusal)
- **Notes:** Repoint both lines from `f1040.line11b` to `f1040.line11a` and re-quote the labels and cites. No numeric effect: the 2026 Form 1040 still prints line 11b as "Amount from line 11a (adjusted gross income)" (f1040 2026 p. 3), as in 2025. Other 2026 Form 8863 wording changes (line 17's "go to line 18" dropped; Part III institution lines printed 22a, 22a(1)–(4), 22b, 22b(1)–(4)) touch nothing encoded.
- **Correction (verification):** reclassified from "rule (definition change)": the amounts are unchanged; only line numbers and references move (`changes.verification.md`).

### C-CRED-18. Education credits: valid SSN required for the taxpayer and a dependent student

- **Kind:** rule (definition change)
- **2026:** `i8863` p. 2 (draft): "Beginning in tax year 2026, you must have a valid social security number (SSN) to claim the American opportunity credit or the lifetime learning credit. If you are filing a joint return, only one spouse must have a valid SSN."; `i8863` p. 3 (draft): "You may be able to claim an education credit if you and the student meet the identification requirement and you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution."; `i8863` p. 3 (draft): "A valid SSN to claim an education credit is one that is valid for employment and that is issued by the Social"; `i8863` p. 4 (draft): "5. You (or your spouse if filing jointly) and the student (if the student is a dependent on your tax return) have not been issued valid SSNs before the due date of your 2026 return (including extensions)."; `f8863` p. 2 (draft): "Before you begin: A valid social security number (SSN) is now required to claim an education credit."
- **2025:** `i8863` p. 2: "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution."; `i8863` p. 3: "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)."
- **Touches:** `f8863.paid`, `dependent.edu_tin_issued`, `dependent.edu_llc_tin_refused`, `dependent.edu_student`; `person.work_ssn` (an existing "SSN valid for employment, issued before the due date" input that matches the 2026 definition)
- **Worklist items:** `f8863.paid` (line)
- **Notes:** New eligibility test: the return qualifies only if the taxpayer (or, on a joint return, at least one spouse) has a valid SSN, and a dependent student must have a valid SSN (an ITIN or ATIN no longer suffices; `dependent.edu_tin_issued` and the ITIN/ATIN refusal `dependent.edu_llc_tin_refused` must be replaced by an SSN test). The 2026 text does not say whether a student who is the taxpayer or spouse needs an SSN beyond the "only one spouse" rule (the p. 3 Tip says a joint-return spouse who is the student need not have one). Re-cite `f8863.paid` to p. 3.

### C-CRED-19. Education credit MAGI limits and phaseout range unchanged

- **Kind:** wording only
- **2026:** `i8863` p. 4 (draft): "The amount of your credit is gradually reduced (phased out) if your MAGI is between $80,000 and $90,000 ($160,000 and $180,000 if you file a joint return)."; `f8863` p. 2 (draft): "Enter $20,000 if married filing jointly; or $10,000 if single, head of household,"; `i8863` p. 2 (draft): "The lifetime learning credit and the American opportunity credit MAGI limits are $180,000 if you’re married filing jointly ($90,000 if you’re filing single, head of household, or qualifying surviving spouse)."
- **2025:** `i8863` p. 3: "The amount of your credit is gradually reduced (phased out) if your MAGI is between $80,000 and $90,000 ($160,000 and $180,000 if you file a joint return)."; `f8863` p. 1: "Enter $20,000 if married filing jointly; or $10,000 if single, head of household,"
- **Touches:** parameters `edu.phaseout_range`, `edu.magi_limit`
- **Worklist items:** `edu.phaseout_range` (parameter)
- **Notes:** The "probable value change" finding is a page move (the i8863 sentence moved from p. 3 to p. 4); the values are the same. Re-cite only. The year diff also matched the new lifetime learning credit sentence on p. 5 ("up to a maximum of $10,000 of adjusted qualified education expenses per return"), which is not a phaseout figure.

### C-CRED-20. Form 1098-T request date moved for a weekend

- **Kind:** wording only
- **2026:** `i8863` p. 2 (draft): "After February 1, 2027 (January 31 falls on a Sunday), but before you file the return, you or the student must request that the educational institution furnish a Form 1098-T."
- **2025:** `i8863` p. 1: "After January 31, 2026, but before you file the return, you or the student must request that the educational institution furnish a Form 1098-T."
- **Touches:** `dependent.edu_1098t` (its prompt says "after February 2, 2026"); ambiguity `amb.2025.edu_1098t_date`
- **Worklist items:** none
- **Notes:** Roll the date in the prompt to February 1, 2027; the 2026 text now prints the weekend adjustment itself, which may settle `amb.2025.edu_1098t_date` (re-read that ambiguity). The rest of the Form 1098-T requirement is unchanged.

### Worklist coverage

| item id | entry |
|---|---|
| `dcprov` (collection) | C-CRED-12 |
| `dcprov.one` (line) | C-CRED-12 |
| `dcprov.paid` (line) | C-CRED-12 |
| `dcprov.see_statement` (line) | C-CRED-12 |
| `dcprov.tin_kind` (line) | C-CRED-12 |
| `dc.one` (parameter) | C-CRED-12 |
| `f2441.clw3` (line) | C-CRED-13 |
| `f2441.employer_care` (line) | C-CRED-12 |
| `f2441.employer_care_gate` (line) | C-CRED-12 |
| `f2441.exclusion_max` (line) | C-CRED-11 |
| `f2441.line1_box` (line) | C-CRED-12 |
| `f2441.line1_paid` (line) | C-CRED-12 |
| `f2441.paid_2026` (line) | C-CRED-12 |
| `f2441.plan_max` (line) | C-CRED-11 |
| `f2441.provider_count` (line) | C-CRED-12 |
| `f2441.provider_ineligible` (line) | C-CRED-12 |
| `f2441.statement_count` (line) | C-CRED-12 |
| `dc.exclusion_max` (parameter) | C-CRED-11 |
| `dc.providers_listed` (parameter) | C-CRED-12 |
| `f2441.line17` (refusal) | C-CRED-12 |
| `f2441.line30` (refusal) | C-CRED-12 |
| `f5695.ac_30` (line) | C-CRED-07 |
| `f5695.ac_capped` (line) | C-CRED-07 |
| `f5695.ac_no_qmid` (line) | C-CRED-07 |
| `f5695.annual_max` (line) | C-CRED-07 |
| `f5695.audit_30` (line) | C-CRED-07 |
| `f5695.audit_capped` (line) | C-CRED-07 |
| `f5695.audit_max` (line) | C-CRED-07 |
| `f5695.b_new_home` (line) | C-CRED-07 |
| `f5695.battery_cost` (line) | C-CRED-02 |
| `f5695.business_use` (line) | C-CRED-02 |
| `f5695.claiming_part1` (line) | C-CRED-05 |
| `f5695.condo` (line) | C-CRED-08 |
| `f5695.construction_later` (line) | C-CRED-02 |
| `f5695.ctc` (line) | C-CRED-04 |
| `f5695.door1_30` (line) | C-CRED-06 |
| `f5695.door_max` (line) | C-CRED-06 |
| `f5695.doors_capped` (line) | C-CRED-06 |
| `f5695.doors_cost` (line) | C-CRED-06 |
| `f5695.doors_max` (line) | C-CRED-06 |
| `f5695.doors_no_qmid` (line) | C-CRED-06 |
| `f5695.doors_sum` (line) | C-CRED-06 |
| `f5695.eehi_credit` (line) | C-CRED-08 |
| `f5695.eehi_rate` (line) | C-CRED-06 |
| `f5695.eehi_ws1` (line) | C-CRED-08 |
| `f5695.eehi_ws2` (line) | C-CRED-08 |
| `f5695.eehi_ws3` (line) | C-CRED-08 |
| `f5695.enabling_30` (line) | C-CRED-07 |
| `f5695.enabling_capped` (line) | C-CRED-07 |
| `f5695.enabling_claimed` (line) | C-CRED-07 |
| `f5695.enabling_no_qmid` (line) | C-CRED-07 |
| `f5695.furnace_30` (line) | C-CRED-07 |
| `f5695.furnace_capped` (line) | C-CRED-07 |
| `f5695.furnace_no_qmid` (line) | C-CRED-07 |
| `f5695.heat_pump_max` (line) | C-CRED-07 |
| `f5695.hp_30` (line) | C-CRED-07 |
| `f5695.hp_capped` (line) | C-CRED-07 |
| `f5695.hp_no_qmid` (line) | C-CRED-07 |
| `f5695.ins_30` (line) | C-CRED-06 |
| `f5695.ins_capped` (line) | C-CRED-06 |
| `f5695.insulation_max` (line) | C-CRED-06 |
| `f5695.item_max` (line) | C-CRED-07 |
| `f5695.joint_occupancy` (line) | C-CRED-08 |
| `f5695.line1` (line) | C-CRED-02 |
| `f5695.line11` (line) | C-CRED-02 |
| `f5695.line12` (line) | C-CRED-03 |
| `f5695.line14` (line) | C-CRED-03 |
| `f5695.line16` (line) | C-CRED-03 |
| `f5695.line17a` (line) | C-CRED-06 |
| `f5695.line17b` (line) | C-CRED-06 |
| `f5695.line17c` (line) | C-CRED-06 |
| `f5695.line17e` (line) | C-CRED-06 |
| `f5695.line18a` (line) | C-CRED-06 |
| `f5695.line18b` (line) | C-CRED-06 |
| `f5695.line19a` (line) | C-CRED-06 |
| `f5695.line19d_i` (line) | C-CRED-06 |
| `f5695.line19d_ii` (line) | C-CRED-06 |
| `f5695.line19e` (line) | C-CRED-06 |
| `f5695.line19h` (line) | C-CRED-06 |
| `f5695.line2` (line) | C-CRED-02 |
| `f5695.line20a_i` (line) | C-CRED-06 |
| `f5695.line20a_ii` (line) | C-CRED-06 |
| `f5695.line20a_iii` (line) | C-CRED-06 |
| `f5695.line20a_iv` (line) | C-CRED-06 |
| `f5695.line20b` (line) | C-CRED-06 |
| `f5695.line20d` (line) | C-CRED-06 |
| `f5695.line21a` (line) | C-CRED-07 |
| `f5695.line21b` (line) | C-CRED-07 |
| `f5695.line22a` (line) | C-CRED-07 |
| `f5695.line22b` (line) | C-CRED-07 |
| `f5695.line22d` (line) | C-CRED-07 |
| `f5695.line23a_i` (line) | C-CRED-07 |
| `f5695.line23a_ii` (line) | C-CRED-07 |
| `f5695.line23b` (line) | C-CRED-07 |
| `f5695.line23d` (line) | C-CRED-07 |
| `f5695.line24a` (line) | C-CRED-07 |
| `f5695.line24b` (line) | C-CRED-07 |
| `f5695.line24d` (line) | C-CRED-07 |
| `f5695.line25a` (line) | C-CRED-07 |
| `f5695.line25c` (line) | C-CRED-07 |
| `f5695.line25e` (line) | C-CRED-07 |
| `f5695.line26a` (line) | C-CRED-07 |
| `f5695.line26b` (line) | C-CRED-07 |
| `f5695.line26c` (line) | C-CRED-07 |
| `f5695.line29a` (line) | C-CRED-07 |
| `f5695.line29b` (line) | C-CRED-07 |
| `f5695.line29c` (line) | C-CRED-07 |
| `f5695.line29d` (line) | C-CRED-07 |
| `f5695.line29e` (line) | C-CRED-07 |
| `f5695.line29f` (line) | C-CRED-07 |
| `f5695.line29h` (line) | C-CRED-07 |
| `f5695.line3` (line) | C-CRED-02 |
| `f5695.line31` (line) | C-CRED-08 |
| `f5695.line32a` (line) | C-CRED-08 |
| `f5695.line32b` (line) | C-CRED-08 |
| `f5695.line4` (line) | C-CRED-02 |
| `f5695.line5a` (line) | C-CRED-02 |
| `f5695.line5b` (line) | C-CRED-02 |
| `f5695.line7a` (line) | C-CRED-02 |
| `f5695.part1_any` (line) | C-CRED-03 |
| `f5695.part2_any` (line) | C-CRED-06 |
| `f5695.qmid_ac` (line) | C-CRED-07 |
| `f5695.qmid_doors` (line) | C-CRED-06 |
| `f5695.qmid_enabling` (line) | C-CRED-07 |
| `f5695.qmid_furnace` (line) | C-CRED-07 |
| `f5695.qmid_hp` (line) | C-CRED-07 |
| `f5695.qmid_wh` (line) | C-CRED-07 |
| `f5695.qmid_windows` (line) | C-CRED-06 |
| `f5695.rce_rate` (line) | C-CRED-02 |
| `f5695.rce_ws1` (line) | C-CRED-04 |
| `f5695.rce_ws2` (line) | C-CRED-04 |
| `f5695.rce_ws3` (line) | C-CRED-04 |
| `f5695.sec_a_claimed` (line) | C-CRED-06 |
| `f5695.sec_a_new_home` (line) | C-CRED-06 |
| `f5695.sec_b_claimed` (line) | C-CRED-07 |
| `f5695.sec_b_new_home` (line) | C-CRED-07 |
| `f5695.separate_homes` (line) | C-CRED-08 |
| `f5695.separate_homes_joint` (line) | C-CRED-08 |
| `f5695.wh_30` (line) | C-CRED-07 |
| `f5695.wh_capped` (line) | C-CRED-07 |
| `f5695.wh_no_qmid` (line) | C-CRED-07 |
| `f5695.windows_30` (line) | C-CRED-06 |
| `f5695.windows_capped` (line) | C-CRED-06 |
| `f5695.windows_max` (line) | C-CRED-06 |
| `f5695.windows_no_qmid` (line) | C-CRED-06 |
| `f5695.annual_max` (parameter) | C-CRED-09 |
| `f5695.audit_max` (parameter) | C-CRED-09 |
| `f5695.door_max` (parameter) | C-CRED-09 |
| `f5695.doors_max` (parameter) | C-CRED-09 |
| `f5695.eehi_rate` (parameter) | C-CRED-09 |
| `f5695.heat_pump_max` (parameter) | C-CRED-09 |
| `f5695.insulation_max` (parameter) | C-CRED-09 |
| `f5695.item_max` (parameter) | C-CRED-09 |
| `f5695.rce_rate` (parameter) | C-CRED-09 |
| `f5695.windows_max` (parameter) | C-CRED-09 |
| `f5695.ac_capped` (refusal) | C-CRED-07 |
| `f5695.doors_capped` (refusal) | C-CRED-06 |
| `f5695.eehi_ws2` (refusal) | C-CRED-08 |
| `f5695.enabling_capped` (refusal) | C-CRED-07 |
| `f5695.furnace_capped` (refusal) | C-CRED-07 |
| `f5695.hp_capped` (refusal) | C-CRED-07 |
| `f5695.line11` (refusal) | C-CRED-02 |
| `f5695.line30` (refusal) | C-CRED-08 |
| `f5695.line6a` (refusal) | C-CRED-02 |
| `f5695.rce_ws2` (refusal) | C-CRED-04 |
| `f5695.wh_capped` (refusal) | C-CRED-07 |
| `f5695.windows_capped` (refusal) | C-CRED-06 |
| `f8863.line14` (line) | C-CRED-17 |
| `f8863.line3` (line) | C-CRED-17 |
| `f8863.paid` (line) | C-CRED-18 |
| `edu.phaseout_range` (parameter) | C-CRED-19 |
| `f8863.line14` (refusal) | C-CRED-17 |
| `f8863.line3` (refusal) | C-CRED-17 |
| `f8880.agi_limit` (line) | C-CRED-15 |
| `f8880.past9` (line) | C-CRED-15 |
| `savers.agi_limit` (parameter) | C-CRED-15 |
| `amb.2025.f5695_17abc_section_a` (ambiguity) | C-CRED-06 |
| `amb.2025.f5695_battery_second_home` (ambiguity) | C-CRED-02 |
| `amb.2025.f5695_category_cap` (ambiguity) | C-CRED-07 |

## Retirement, health coverage and people: Forms 1099-R, 8606, 5329, 8962 and 1095-A; filer, dependent and household tests; other information returns

I read the 90 kind-(a) worklist items in the group file and the 137 changed-sentence pairs they rest on. I also
read the What's New, Reminders and Future Developments sections, and any form-face caution, of the 22
documents in the group. Most of those are 2026 IRS drafts: f8606, i8606, p590b, p575, f5329, i5329, f8962,
i1095a and p4681. f1099r, i1099r, f1095a, f1099g, rp-25-25, fr-2025-01377 and n-25-67 are final. f1099c,
i1099ac, f1099sa, i982, p529 and p538 are continuous-use revisions whose 2026 text is byte-identical to the 2025
archive. To settle items whose quotes come from documents outside the group, I also read i8863, f8863, p503, i2441, f8889,
i8889, iw2w3, f8880, f1040s2, plaw-119-21 and rp-25-32.

Several changes are notable:
- P.L. 119-21 sec. 71305 removes the cap on repaying excess advance PTC, and the 2026 Form 8962 draft
  reserves lines 28–29.
- The 2026 Form 8962 draft adds a line 6 test: a line 5 entry of 401% means no PTC.
- Form 5329 taxes are split between Schedule 2 lines 5 and 18. In 2025 they all went to line 8.
- Form 1099-R box 7 becomes boxes 7a–7d.
- A new early-distribution exception 24 covers qualified long-term care distributions.
- Trump accounts are a new kind of traditional IRA that Form 8606 excludes.
- The education credits now require a valid SSN.
- The 2026 amounts change: $10,500 domestic-abuse cap, $7,500/$8,600 IRA limit, $24,500 deferral limit.

Items whose cited text has no 2026 edition in the archive (i1040gi, i4562, p501, p560, p590a and p970) cannot be
settled yet. Entries C-PEOP-23 and C-PEOP-24 hold them: 16 worklist items (the coverage table below), counted as
still waiting for a 2026 source, kind (b) (owner decision 2026-11-04). This paragraph first said "thirty-three
items"; the coverage table and `worklist.json` give 16, and 33 could not be reproduced.

### What's New and Reminders accounted for

| document | item (quoted heading or first words) | entry or "not encoded: reason" |
|---|---|---|
| f8606 (draft) | form note "“traditional IRA” includes ... but does not include Trump accounts" | C-PEOP-11 |
| i8606 (draft) | Future Developments | not encoded: points to IRS.gov only |
| i8606 (draft) | What's New "Trump accounts." | C-PEOP-11 |
| i8606 (draft) | What's New "References to 2026 Form 8915-F." | not encoded: qualified disaster distributions and repayments are refused by `scope.other_income` and `retirement.special` |
| i8606 (draft) | What's New "Modified adjusted gross income (AGI) limit for traditional IRA contributions increased." | C-PEOP-09 |
| i8606 (draft) | What's New "Modified AGI limit for Roth IRA contributions increased." | C-PEOP-09 (Roth limits: not encoded) |
| i8606 (draft) | What's New "Due date for contributions." | not encoded: filing mechanics (the date is only in input wording) |
| i8606 (draft) | Reminders "Definitions for IRAs." (moved from 2025 What's New) | not encoded: the definition is unchanged; it has moved from What's New to Reminders |
| i8606 (draft) | Reminders "Clarification on nondeductible contributions." (moved from 2025 What's New) | not encoded: unchanged text, moved from What's New to Reminders |
| i8606 (draft) | Reminders "Certain retirement plan distributions and their repayments." | not encoded: repayments are refused by `retirement.early_screen` and `scope.other_income`; text only changes years |
| i8606 (draft) | Reminders "Basis adjustments." | C-PEOP-10 (refused by `person.ira_basis_gate`) |
| p590b (draft) | Future Developments | not encoded: points to IRS.gov only |
| p590b (draft) | What's New "Trump accounts." | C-PEOP-11 |
| p590b (draft) | Reminders "Excise tax relief for certain 2024 required minimum distributions (RMDs)." | not encoded: missed RMDs (Form 5329 Part IX) are outside the tool |
| p590b (draft) | Reminders "Simplified employee pension (SEP) and SIMPLE plans." | not encoded: cross-reference |
| p590b (draft) | Reminders "Deemed IRAs." | not encoded: definition, nothing computed |
| p590b (draft) | Reminders "Statement of required minimum distribution (RMD)." | not encoded: custodian reporting |
| p590b (draft) | Reminders "IRA interest." | not encoded: nothing computed |
| p590b (draft) | Reminders "Net Investment Income Tax (NIIT)." | not encoded here (NIIT is another group's Form 8960) |
| p590b (draft) | Reminders "Photographs of missing children." | not encoded: not tax content |
| p590b (draft) | chapter 1 Reminders "Types of IRAs." (p. 6) | not encoded: definition, nothing computed |
| p590b (draft) | chapter 2 Reminders "Disaster relief." / "Designated Roth accounts." (p. 35) | not encoded: cross-reference and definition |
| p590b (draft) | 2025 Reminders "Income on corrective distributions of excess contributions" (dropped in 2026) | not encoded: exception 21 is unchanged in i5329 (p. 6) |
| p575 (draft) | Future Developments | not encoded: points to IRS.gov only |
| p575 (draft) | What's New "Distributions for qualified long-term care insurance." | C-PEOP-05 |
| p575 (draft) | Reminders "The direct payment requirement for certain distributions for payment of health or long-term care insurance repealed." | not encoded: the retired public safety officer exclusion is refused by `retirement.special` |
| p575 (draft) | Reminders "Photographs of missing children." | not encoded: not tax content |
| i1099r | Future Developments | not encoded: points to IRS.gov only |
| i1099r | What's New "Address fields." | not encoded: payer form layout |
| i1099r | What's New "New boxes 7a–7d of Form 1099-R." | C-PEOP-04 |
| i1099r | What's New "Renumbered box 8 of Form 1099-R." | not encoded: box 8 (annuity contract value) is not read |
| i1099r | What's New "Reporting the actuarial value of the contract in box 8a is optional" | not encoded: box 8a is not read |
| i1099r | What's New "Qualified long-term care distribution reported on Form 1099-R." | C-PEOP-05 |
| i1099r | What's New "New code HP for box 14b of Form 5498." | not encoded: Form 5498 is not read |
| i1099r | Reminders "Due dates." / "Information Returns Intake System (IRIS)." / "Online fillable forms." | not encoded: filing mechanics |
| i1099r | Reminders "Code Y for box 7a on Form 1099-R." | not encoded: code Y falls in `retirement_code` `other` and is refused by `retirement.bad_code` (box renumbering is C-PEOP-04) |
| f1099r | Instructions for Recipient, boxes 7a–7d (form face; no What's New) | C-PEOP-04 |
| f5329 (draft) | form-face caution "If you only owe the additional 10% tax ... Schedule 2 (Form 1040), line 5" | C-PEOP-03 |
| f5329 (draft) | Part I "(including an IRA and Trump account (after the growth period of the Trump account))"; Parts X and XI | C-PEOP-11 |
| i5329 (draft) | Future Developments | not encoded: points to IRS.gov only |
| i5329 (draft) | What's New "Distributions for qualified long-term care insurance." | C-PEOP-05 |
| f8962 (draft) | form face, line 6 "Did you enter 401% on line 5?" (no What's New on the form) | C-PEOP-14 |
| f8962 (draft) | form face, lines 28 and 29 "Reserved for future use" | C-PEOP-12 |
| f1095a | form and Instructions for Recipient (no What's New) | not encoded: only the year and capitalisation change ("call center", "zero" for "-0-"); nothing read changes |
| i1095a (draft) | Future Developments / Additional Information | not encoded: points to IRS.gov only (wording change on line 33 is C-PEOP-02) |
| rp-25-25 | (no What's New; section 3.01 Applicable Percentage Table for 2026) | C-PEOP-15 |
| fr-2025-01377 | (no What's New; 2025 poverty guidelines) | C-PEOP-15 |
| n-25-67 | (no What's New; 2026 retirement limits) | C-PEOP-05, C-PEOP-06, C-PEOP-08, C-PEOP-09, C-PEOP-20 |
| p4681 (draft) | Future Developments | not encoded: points to IRS.gov only |
| p4681 (draft) | What's New "Discharge of qualified principal residence indebtedness after 2025." | C-PEOP-25 |
| p4681 (draft) | What's New "Student loan discharges after 2025." | C-PEOP-25 |
| p4681 (draft) | Reminders "Photographs of missing children." | not encoded: not tax content |
| f1099g | "Future developments." (Instructions for Recipient; no What's New) | not encoded: points to IRS.gov only. The Rev. December 2026 form splits the address fields; the box 1, 2 and 8 text read by `refund.yaml` and `s1.yaml` is unchanged (p. 5) |
| f1099c | "Future developments." (same text as 2025) | not encoded: points to IRS.gov only; document unchanged |
| i1099ac | What's New "Mortgage and student loan forgiveness relief expires in 2025." (same text as 2025) | C-PEOP-25 |
| i1099ac | Reminders (general instructions, continuous-use revision, online fillable Copy B) (same text as 2025) | not encoded: filing mechanics |
| f1099sa | "Future developments." (same text as 2025) | not encoded: points to IRS.gov only; document unchanged |
| i982 | What's New "Discharge of qualified principal residence indebtedness before 2026." / "Amount eligible for the exclusion." (same text as 2025) | C-PEOP-25 |
| p529 | Reminders "Future developments." / "Photographs of missing children." (same text as 2025) | not encoded: points to IRS.gov only |
| p538 | Future Developments (same text as 2025) | not encoded: points to IRS.gov only |

### C-PEOP-01. Form 1040 spouse name line: "If a joint return"

- **Kind:** wording only
- **2026:** `f1040` p. 2 (draft): "If a joint return, spouse’s first name and middle initial"
- **2025:** `f1040` p. 1: "If joint return, spouse’s first name and middle initial"
- **Touches:** household.persons, household.roster_bad, household.roster_ok, household.spouses, household.taxpayers, person, person.role (and the enum person_role)
- **Worklist items:** household.persons, household.roster_bad, household.roster_ok, household.spouses, household.taxpayers, person, person.role
- **Notes:** The 2026 draft adds "a" to the label and reorders the filing-status boxes. The roster of filer and spouse
  is unchanged. Re-quote the locators with "If a joint return". The nearby figures that differ are the standard
  deduction amounts and the "Created" date, which nothing here reads. The 2026 draft also adds a new
  citizenship/work-authorization question under "Other Information" (p. 2). Nothing in this group reads it.

### C-PEOP-02. Form 1095-A line 33: "Total" becomes "Add"

- **Kind:** wording only
- **2026:** `i1095a` p. 3 (draft): "Add the amounts on lines 21 through 32 and enter on line 33."
- **2025:** `i1095a` p. 2: "Total the amounts on lines 21 through 32 and enter on line 33."
- **Touches:** f1095a.line33a, f1095a.line33b, f1095a.line33c, f1095a.yr_a_monthly, f1095a.yr_a_uniform, f1095a.yr_b_monthly, f1095a.yr_b_uniform, f1095a.yr_c_monthly, ptc.months
- **Worklist items:** f1095a.line33a, f1095a.line33b, f1095a.line33c, f1095a.yr_a_monthly, f1095a.yr_a_uniform, f1095a.yr_b_monthly, f1095a.yr_b_uniform, f1095a.yr_c_monthly, ptc.months
- **Notes:** Same rule; the instruction has moved to p. 3 of the draft. Re-quote the locators. The other nearby changes are
  "Social security number (SSN)" shortened to "SSN" and "1/1/2026". The Form 1095-A face is unchanged
  apart from the year.

### C-PEOP-03. Form 5329 taxes now go to Schedule 2 line 5 (early distributions) and line 18 (excess contributions)

- **Kind:** rule (definition change)
- **2026:** `f5329` p. 2 (draft): "Additional tax. Enter 10% (0.10) of line 3. Include this amount on Schedule 2 (Form 1040), line 5" ... `f1040s2` p. 2 (draft): "Additional tax on IRAs or other tax-favored accounts. Attach Form 5329 if required. If not required, check here" ... `f1040s2` p. 3 (draft): "Additional tax on excess contributions or accumulations in IRAs or other tax-favored accounts."
- **2025:** `f5329` p. 1: "Additional tax. Enter 10% (0.10) of line 3. Include this amount on Schedule 2 (Form 1040), line 8"
- **Touches:** f5329.l4, f5329.rate10, f5329.tax10, f5329.tax, f5329.l49, person.x_tax, s2.line8, s2.line8_file, s2.line8_box
- **Worklist items:** f5329.l4, f5329.rate10, f5329.tax10
- **Notes:** The 10% rate is unchanged. The routing splits. Line 4 (and the line 8 education/ABLE tax) goes to
  Schedule 2 line 5. Line 49 (HSA excess, "Include this amount on Schedule 2 (Form 1040), line 18", f5329 p. 3 (draft))
  goes to new line 18. `f5329.tax` and `person.x_tax` sum lines 4 and 49 into one Schedule 2 line 8, so they must be
  split into two totals, and the "If not required, check here" box (`s2.line8_box`) moves to line 5. Coordinate with
  the Schedule 2 group.

### C-PEOP-04. Form 1099-R box 7 becomes boxes 7a–7d (code in 7a, IRA/SEP/SIMPLE box in 7b, Trump account 7c, excess earnings 7d)

- **Kind:** new line or form
- **2026:** `i1099r` p. 1: "We renumbered box 7 and the “IRA/SEP/SIMPLE” checkbox to boxes 7a and 7b and we added boxes 7c (Trump account) and 7d (Earnings on excess contributions)." ... `f1099r` p. 9: "Box 7b. If the IRA/SEP/SIMPLE box is checked, you’ve received a traditional IRA (other than a Trump account), SEP, or SIMPLE distribution." ... `i5329` p. 2 (draft): "However, if distribution code 1 is correctly shown in box 7a of all your Forms 1099-R and you owe the additional tax on the full amount shown on each Form 1099-R, you don’t have to file Form 5329."
- **2025:** `f1099r` p. 9: "If the IRA/SEP/SIMPLE box is checked, you’ve received a traditional IRA, SEP, or SIMPLE distribution." ... `i5329` p. 1: "However, if distribution code 1 is correctly shown in box 7 of all your Forms 1099-R and you owe the additional tax on the full amount shown on each Form 1099-R, you don’t have to file Form 5329."
- **Touches:** retirement.account, retirement.code, retirement.bad_code, retirement.code_screen, f5329, f5329.files, f5329.must, f5329.one, person.x_must, s2.line8_must (enums retirement_account, retirement_code)
- **Worklist items:** retirement.account, retirement.bad_code, retirement.code_screen, f5329, f5329.files, f5329.must, f5329.one, person.x_must
- **Notes:** The code list is unchanged (f1099r pp. 7 and 9 list the same codes 1–9 and A–Y in both years). Only the
  box number moves: `f1099r` p. 7: "Box 7a. The following codes identify the distribution you received." Re-point the
  input questions and locators from "box 7" to "box 7a" and from "IRA/SEP/SIMPLE box" to "box 7b". The i5329 sentence
  also changes "Schedule 2 (Form 1040), line 8" to "line 5" (C-PEOP-03).
  The `retirement.account` enum has no Trump-account value, so a box 7c distribution needs a refusal (C-PEOP-11).
  Box 7d earnings are taxed 100% on Form 5329 Part XI ("Enter the earnings attributable to the excess contributions
  distributed from Form 1099-R, box 7d", f5329 p. 4 (draft)), which is not encoded.

### C-PEOP-05. New early-distribution exception 24: qualified long-term care distributions (exception range 01–24)

- **Kind:** rule (definition change)
- **2026:** `i5329` p. 5 (draft): "exception number (01–24). If more than one exception applies, enter 99." ... `i5329` p. 2 (draft): "Beginning with distributions made after December 29, 2025, a distribution from your employer’s defined contribution plan for or with respect to certified long-term care insurance is not subject to the 10% additional tax on early distributions if certain requirements are met." ... `p590b` p. 30 (draft): "if the individual covered by the long-term care coverage is the spouse of the em­ ployee, this exception applies only if the employee and employee’s spouse file a joint return." ... `n-25-67` p. 5: "The limitation under section 401(a)(39)(B)(i)(III) on a qualified long-term care distribution from a qualified defined contribution plan with respect to certified long-term care insurance remains $2,600."
- **2025:** `i5329` p. 5: "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99."
- **Touches:** f5329.l2, retirement.early_screen, retirement.screen_refused, retirement.exception, retirement.has_exception, retirement.exc_amount, retirement.exc_capped, retirement.l2, retirement.wrong_kind, person.x_capped_sum, person.x_l2_all, person.x_limited_sum, person.x_other_exc (enum early_exception)
- **Worklist items:** f5329.l2, retirement.early_screen, retirement.screen_refused, retirement.exception, retirement.has_exception, retirement.exc_amount, retirement.exc_capped, retirement.l2, person.x_capped_sum, person.x_l2_all, person.x_limited_sum, person.x_other_exc
- **Notes:** Exception 24 must either be added to the `early_exception` enum or kept refused. In 2025 the
  `retirement.early_screen` question refuses only "a qualified long-term care distribution made December 30 or 31, 2025".
  For 2026 it must cover every such distribution unless e24 is built. Building e24 would need a joint-return condition
  for spouse coverage, and a cap of the lesser of premiums, "10% of the present value of the employee’s nonforfeit­ able
  accrued benefit" and $2,600 (p590b p. 30 (draft)).
  Exceptions 01–23 keep their numbers (i5329 p. 6 (draft) lists 19–23 as in 2025). Rewrite the locators to "(01–24)".
  Doubt: i1099r p. 1 says "For tax years after 2026, participants will be able to receive qualified long-term care
  distributions", while i5329 (draft) and p575 p. 3 (draft) say distributions "made after December 29, 2025" qualify.
  The 2026 drafts govern the exception; the reporting date in i1099r appears inconsistent.

### C-PEOP-06. Domestic abuse victim distribution cap $10,300 → $10,500

- **Kind:** amount (parameter)
- **2026:** `p590b` p. 29 (draft): "must not exceed the lesser of $10,500 for 2026 or 50% of the present value of the IRA." ... `n-25-67` p. 5: "The limitation under section 72(t)(2)(K)(ii)(I) for eligible distributions to victims of domestic abuse from applicable eligible retirement plans is increased from $10,300 to $10,500."
- **2025:** `p590b` p. 28: "must not exceed the lesser of $10,300 for 2025 or 50% of the present value of the IRA."
- **Touches:** f5329.cap_abuse, person.x_cap22, person.x_c22, person.x_e22
- **Worklist items:** f5329.cap_abuse, person.x_cap22, person.x_c22, person.x_e22
- **Notes:** Set `f5329.cap_abuse` to 1050000 cents and update the `person.x_cap22` label "($10,300)" and its locator.
  The other caps are unchanged in the 2026 draft: first home "up to $10,000" (p590b p. 28 (draft)),
  "must not ex­ ceed $5,000 per taxpayer" for birth or adoption (p. 29), and emergency "lesser of $1,000" (p. 29).

### C-PEOP-07. Birth-or-adoption and first-time-homebuyer sentences reworded

- **Kind:** wording only
- **2026:** `i5329` p. 6 (draft): "A qualified distribution from an applicable eligible retirement plan for the birth or adoption of a child is a distribution of up to $5,000 if made during the 1-year period beginning on the date your child was born or adopted." ... `p590b` p. 29 (draft): "Generally, you are a first-time homebuyer if you had no present interest in a main home during the 2-year period ending on the date of acquisition of the home that the distribution is being used to buy, build, or rebuild. If you are married, your spouse must also meet this no-ownership requirement."
- **2025:** `i5329` p. 5: "A qualified distribution from a retirement plan for the birth or adoption of a child is a distribution of up to $5,000 if made during the 1-year period beginning on the date your child was born or adopted." ... `p590b` p. 28: "you are a first-time homebuyer if you had no present interest in a main home during the 2-year period ending on the date of acquisition of the home which the distribution is being used to buy, build, or rebuild. If you are married, your spouse must also meet this no-ownership requirement."
- **Touches:** retirement.is_e19, retirement.l2_e19, retirement.exception, f5329.cap_birth, f5329.cap_first_home
- **Worklist items:** retirement.is_e19, retirement.l2_e19
- **Notes:** "a retirement plan" becomes "an applicable eligible retirement plan", and "which" becomes "that". The amounts
  and conditions are unchanged. Re-quote the locators with their new pages. `retirement.exception` is also listed under C-PEOP-05, which
  covers its other quote.

### C-PEOP-08. IRA contribution limit $7,000/$8,000 → $7,500/$8,600; spousal compensation thresholds

- **Kind:** amount (parameter)
- **2026:** `i8606` p. 6 (draft): "your limit on contributions to traditional and Roth IRAs is generally the smaller of $7,500 ($8,600 if age 50 or older at the end of 2026) or your taxable compensation" ... `n-25-67` p. 4: "is increased from $7,000 to $7,500." ... `i8606` p. 6 (draft): "combined taxable compensation of both you and your spouse is less than $15,000 ($16,100 if one spouse is age 50 or older at the end of 2026; $17,200 if both spouses are age 50 or older at the end of 2026"
- **2025:** `i8606` p. 5: "your limit on contributions to traditional and Roth IRAs is generally the smaller of $7,000 ($8,000 if age 50 or older at the end of 2025) or your taxable compensation" ... `i8606` p. 5: "combined taxable compensation of both you and your spouse is less than $14,000 ($15,000 if one spouse is age 50 or older at the end of 2025; $16,000 if both spouses are age 50 or older at the end of 2025"
- **Touches:** ira.all_total, person.ira_own_total, ira.limit, ira.limit_50, ira.kbh_none, ira.kbh_one, ira.kbh_both
- **Worklist items:** ira.all_total, person.ira_own_total
- **Notes:** The two worklist lines are sums whose rule does not change; only their locator quote moves (p. 6, new
  figures). The parameters behind them must change: `ira.limit` to 750000, `ira.limit_50` to 860000, and `ira.kbh_*` to
  1500000/1610000/1720000. n-25-67 p. 4 gives the catch-up "from $1,000 to $1,100". Those parameters cite i1040gi,
  whose 2026 edition is not archived. i8606 (draft), i5329 p. 6 (draft) and n-25-67 support the values meanwhile.

### C-PEOP-09. IRA deduction and Roth MAGI phase-outs for 2026

- **Kind:** amount (parameter)
- **2026:** `n-25-67` p. 4: "For married couples filing jointly, if the spouse who makes the IRA contribution is an active participant, the income phase-out range is between $129,000 and $149,000, increased from between $126,000 and $146,000. For an IRA contributor who is not an active participant and is married to someone who is an active participant, the deduction is phased out if the couple’s income is between $242,000 and $252,000, increased from between $236,000 and $246,000." ... `i8606` p. 2 (draft): "$91,000 if single, head of household, or married filing separately and you didn’t live with your spouse at any time in 2026"
- **2025:** `i8606` p. 1: "$146,000 if married filing jointly or qualifying surviving spouse; • $89,000 if single, head of household, or married filing separately and you didn’t live with your spouse at any time in 2025"
- **Touches:** ira.line2, ira.line2_not_covered
- **Worklist items:** none (What's New item in i8606)
- **Notes:** `ira.line2` becomes 14900000 (mfj/qss) and 9100000 (single/hoh). The mfs value of $10,000 is unchanged
  ("remains $0 to $10,000", n-25-67 p. 4). `ira.line2_not_covered` (the top of the non-participant spouse range) becomes
  25200000. The worksheet text itself waits for the 2026 i1040gi. The Roth limits (i8606 (draft): "$252,000 if married
  filing jointly", "$168,000 if single") are not encoded.

### C-PEOP-10. Form 8606 line 2: "-0-" becomes "zero"; Total Basis Chart rows move a year

- **Kind:** wording only
- **2026:** `i8606` p. 10 (draft): "However, you may need to enter an amount that is more than zero (even if this is the first year you are required to file Form 8606) or increase or decrease the amount from the chart if your basis changed because of any of the following."
- **2025:** `i8606` p. 9: "However, you may need to enter an amount that is more than -0- (even if this is the first year you are required to file Form 8606) or increase or decrease the amount from the chart if your basis changed because of any of the following."
- **Touches:** person.ira_basis_adjusted, person.ira_8606_line2, person.ira_basis_gate
- **Worklist items:** person.ira_basis_adjusted, person.ira_8606_line2
- **Notes:** Same rule, now on p. 10. Re-quote with "zero". The chart's first row is "after 2023 and before 2026"
  instead of "before 2025". The input question should say "2026" where it names years.

### C-PEOP-11. Trump accounts: a new kind of traditional IRA, excluded from Form 8606 and taxed on new Form 5329 Parts X–XI

- **Kind:** rule (definition change)
- **2026:** `f8606` p. 2 (draft): "Note: Except where stated otherwise, “traditional IRA” includes traditional SEP IRAs and traditional SIMPLE IRAs but does not include Trump accounts." ... `i8606` p. 2 (draft): "traditional IRAs do not include Trump accounts, a type of traditional IRA introduced in PL-119-21, the One Big Beautiful Bill Act." ... `f5329` p. 2 (draft): "from a qualified retirement plan (including an IRA and Trump account (after the growth period of the Trump account))" ... `f5329` p. 4 (draft): "Additional Tax on Excess Contributions to Trump Accounts During the Growth Period."
- **2025:** `f8606` p. 1: "Note: Except where stated otherwise, “traditional IRA” includes traditional SEP IRAs and traditional SIMPLE IRAs." (no Trump account counterpart)
- **Touches:** retirement.account (enum retirement_account), retirement.bad_code, person.ira_contrib, person.ira_basis, person.ira_8606_line2
- **Worklist items:** none (What's New items in i8606, p590b and the f8606/f5329 form faces)
- **Notes:** p590b p. 3 (draft): "Generally, no distributions are allowed from a Trump account before January 1 of the
  calendar year that the ac­ count beneficiary reaches age 18." The adoption must keep Trump-account contributions out of
  the traditional-IRA inputs (IRA deduction and Form 8606). It must also refuse a Form 1099-R with box 7c checked or an
  amount in box 7d, since Form 5329 Parts X and XI are not built. Whether a Trump-account contribution question is needed
  at all is a design question for the adoption.

### C-PEOP-12. Repayment limitation on excess advance PTC eliminated; Form 8962 lines 28–29 reserved

- **Kind:** rule (definition change)
- **2026:** `plaw-119-21` p. 254: "SEC. 71305. ELIMINATING LIMITATION ON RECAPTURE OF ADVANCE PAYMENT OF PREMIUM TAX CREDIT. (a) IN GENERAL.—Section 36B(f)(2) is amended by striking subparagraph (B)." ... `plaw-119-21` p. 255: "shall apply to taxable years beginning after December 31, 2025." ... `rp-25-32` p. 5: "Section 71305 of the OBBBA removes § 36B(f)(2)(B), which limited the tax increase from excess advance payments for certain households, effective for taxable years beginning after December 31, 2025. Accordingly, the inflation adjustment to § 36B(f)(2)(B) is removed from this revenue procedure." ... `f8962` p. 2 (draft): "Excess advance payment of PTC. If line 25 is greater than line 24, subtract line 24 from line 25. Enter the difference here and on Schedule 2 (Form 1040), line 1a" ... `f8962` p. 2 (draft): "Reserved for future use"
- **2025:** `rp-2024-40` p. 9: "For taxable years beginning in 2025, the limitation on tax imposed under § 36B(f)(2)(B) for excess advance credit payments is determined using the following table" ... `f8962` p. 1: "Repayment limitation (see instructions)" ... `f8962` p. 1: "Excess advance PTC repayment. Enter the smaller of line 27 or line 28 here and on Schedule 2 (Form 1040), line 1a"
- **Touches:** ptc.repay_200, ptc.repay_300, ptc.repay_400, f8962.repay_200, f8962.repay_300, f8962.repay_400, f8962.show_28, f8962.line27, f8962.line28, f8962.line29, s2.line1a
- **Worklist items:** ptc.repay_200, ptc.repay_300, ptc.repay_400, f8962.line29
- **Notes:** Drop the three `ptc.repay_*` parameters (no 2026 value exists, per rp-25-32) and lines 28–29. Line 27 now
  goes straight to Schedule 2 line 1a, so `s2.line1a` must read `f8962.line27` instead of `f8962.line29`. The heading
  "Refundable Credit for Coverage Under a Qualified Health Plan" and the "Less than 200%" rows have no 2026 counterpart
  because the limitation is repealed, not moved.

### C-PEOP-13. Form 8962 lines 24 and 25 unchanged on the 2026 draft; the 2026 instructions are not archived

- **Kind:** wording only
- **2026:** `f8962` p. 2 (draft): "Total PTC. Enter the amount from line 11, column (e), or add lines 12 through 23, column (e), and enter the total here"
- **2025:** `f8962` p. 1: "Total PTC. Enter the amount from line 11, column (e), or add lines 12 through 23, column (e), and enter the total here"
- **Touches:** f8962.line24, f8962.line25
- **Worklist items:** f8962.line24, f8962.line25
- **Notes:** The form text of lines 24 and 25 is the same. The locators cite i8962 pp. 17–18, and no 2026 i8962 is archived,
  so re-quote them when it is posted.

### C-PEOP-14. Form 8962 line 6: household income above 400% of the poverty line ends eligibility

- **Kind:** new line or form
- **2026:** `f8962` p. 2 (draft): "Did you enter 401% on line 5? (See instructions if you entered less than 100%.)" ... `f8962` p. 2 (draft): "Yes. You are not eligible to take the PTC. If advance payment of the PTC was made, see the instructions for how to report your excess advance PTC repayment amount." ... `rp-25-25` p. 3: "At least 300% but not more than 400%"
- **2025:** `f8962` p. 1: "Reserved for future use"
- **Touches:** f8962.line5, f8962.applicable, f8962.show_applicable, f8962.line7 (table ptc_applicable_figure; ambiguity amb.2025.ptc_not_applicable)
- **Worklist items:** none (form-face change; i8962 has no 2026 edition)
- **Notes:** In 2025, line 5 at 400 or 401 gave applicable figure 0.0850 (table ptc_applicable_figure, rows 400 and
  401). In 2026, 401 means no PTC, and any advance payments are repaid in full (C-PEOP-12). Add line 6 and make
  `f8962.applicable` false at 401. The rp-25-25 table ends at "not more than 400%". The 2026 i8962 is needed for the
  exact line 5 worksheet and the line 6 instructions.

### C-PEOP-15. 2026 applicable percentage table and the 2025 poverty guidelines

- **Kind:** amount (parameter)
- **2026:** `rp-25-25` p. 3: "For taxable years beginning in calendar year 2026, the Applicable Percentage Table for purposes of § 36B(b)(3)(A)(i) and § 1.36B-3(g) is:" ... `rp-25-25` p. 3: "Less than 133% 2.10% 2.10%" ... `fr-2025-01377` p. 1: "For families/households with more than 8 persons, add $5,500 for each additional person."
- **2025:** `fr-2024-00796` p. 2: "add $5,380 for each"
- **Touches:** f8962.line4, f8962.line7 (tables ptc_applicable_figure, ptc_poverty_line)
- **Worklist items:** none (documents rp-25-25 and fr-2025-01377 of this group)
- **Notes:** The 2026 rows are 2.10/2.10, 3.14–4.19, 4.19–6.60, 6.60–8.44, 8.44–9.96 and 9.96–9.96 (rp-25-25 p. 3).
  The 2025 poverty lines (fr-2025-01377 p. 1) for one person are $15,650 contiguous, $19,550 Alaska and $17,990 Hawaii;
  each additional person adds $5,500, $6,880 and $6,330.
  Both tables are generated from i8962 (Table 2 by single percentages; Tables 1-1 to 1-3), and no 2026 i8962 is archived.
  No archived 2026 text states that the 2025 guidelines are used for 2026. The 2025 table header says "For 2025, the 2024
  federal poverty lines are used", so the 2026 pairing is an inference that the 2026 i8962 must confirm before release.

### C-PEOP-16. Education credits require a valid SSN (filer and dependent student), not any TIN

- **Kind:** rule (definition change)
- **2026:** `i8863` p. 2 (draft): "Beginning in tax year 2026, you must have a valid social security number (SSN) to claim the American opportunity credit or the lifetime learning credit. If you are filing a joint return, only one spouse must have a valid SSN. When the student for whom qualified education expenses were paid is your dependent, the student must also have a valid SSN to qualify for the credit." ... `i8863` p. 3 (draft): "You may be able to claim an education credit if you and the student meet the identification requirement and you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." ... `i8863` p. 4 (draft): "You (or your spouse if filing jointly) and the student (if the student is a dependent on your tax return) have not been issued valid SSNs before the due date of your 2026 return (including extensions)."
- **2025:** `i8863` p. 2: "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." ... `i8863` p. 3: "Students must have been issued a TIN by the due date of their 2025 return (including extensions)"
- **Touches:** dependent.edu, dependent.edu_tin_issued, dependent.edu_llc_tin_refused, dependent.work_ssn, person.edu
- **Worklist items:** dependent.edu, dependent.edu_tin_issued, person.edu
- **Notes:** i8863 p. 3 (draft) defines a valid SSN as "one that is valid for employment". The 2025 test (an SSN, ITIN or
  ATIN issued by the due date) becomes an SSN valid for employment issued "before the due date". It applies to the
  student if a dependent, and to the filer or at least one spouse on a joint return. `dependent.work_ssn` already asks
  the dependent's version. A filer-level SSN question is needed, and the ITIN/ATIN refusal
  `dependent.edu_llc_tin_refused` becomes a plain disallowance.

### C-PEOP-17. Education items: the year changes and the line 24 question moves a page

- **Kind:** wording only
- **2026:** `f8863` p. 3 (draft): "Was the student enrolled at least half-time for at least 1 academic period that began or is treated as having begun in 2026 at an eligible educational institution in a program leading toward a postsecondary degree, certificate, or other recognized postsecondary educational credential?" ... `i8863` p. 9 (draft): "you were a full-time student for 2026 if during any part of any 5 calendar months during the year you were enrolled as a full-time student at an eligible educational institution (defined earlier) or took a full-time, on-farm training course given by such an institution or by a state, county, or local government agency."
- **2025:** `f8863` p. 2: "Was the student enrolled at least half-time for at least one academic period that began or is treated as having begun in 2025 at an eligible educational institution in a program leading toward a postsecondary degree, certificate, or other recognized postsecondary educational credential?" ... `i8863` p. 7: "you were a full-time student for 2025 if during any part of any 5 calendar months during the year you were enrolled as a full-time student at an eligible educational institution (defined earlier), or took a full-time, on-farm training course given by such an institution or by a state, county, or local government agency."
- **Touches:** dependent.edu_line24, person.edu_line24, person.edu_fulltime
- **Worklist items:** dependent.edu_line24, person.edu_line24, person.edu_fulltime
- **Notes:** Only "one" becomes "1", the year changes and a comma goes. Update the printed label of line 24 and the
  locators, and replace "2025" with "2026" in the input wording.

### C-PEOP-18. Dependent care expenses: Form 2441 Part I columns become lines 1a–1e; p503 sentence moves

- **Kind:** wording only
- **2026:** `i2441` p. 4 (draft): "If you were covered by your employer’s dependent care plan and your employer furnished the care (either at your workplace or by hiring a care provider), enter your employer’s name on line 1a." ... `p503` p. 7 (draft): "However, if you are required to pay for care weekly, monthly, or in another way that includes both days worked and days not worked, you can figure your credit including the expenses you paid for" ... `p503` p. 8 (draft): "days you didn’t work. Any day when you work at least 1 hour is a day of work."
- **2025:** `i2441` p. 3: "If you were covered by your employer's dependent care plan and your employer furnished the care (either at your workplace or by hiring a care provider), enter your employer's name in column (a)" ... `p503` p. 6: "However, if you are required to pay for care weekly, monthly, or in another way that includes both days worked and days not worked, you can figure your credit including the expenses you paid for days you didn't work. Any day when you work at least 1 hour is a day of work."
- **Touches:** dependent.dc_paid
- **Worklist items:** dependent.dc_paid
- **Notes:** The input rule is unchanged: the value of care the employer furnished itself is still excluded. Update the locators.
  The 2441 credit-rate and benefit-limit changes in i2441's What's New (p. 2 (draft)) belong to the Form 2441 group.

### C-PEOP-19. Form 8889 line 17b now routes to Schedule 2 line 13c

- **Kind:** wording only
- **2026:** `f8889` p. 2 (draft): "Also include this amount in the total on Schedule 2 (Form 1040), Part II, line 13c"
- **2025:** `f8889` p. 1: "Also, include this amount in the total on Schedule 2 (Form 1040), Part II, line 17c"
- **Touches:** person.hsa_addtax, s2.line17c
- **Worklist items:** person.hsa_addtax
- **Notes:** `person.hsa_addtax` still sums Form 8889 line 17b; only the destination line is renumbered. The 2026 Schedule 2
  draft p. 2 reads "Additional tax on HSA distributions. Attach Form 8889". `s2.line17c` becomes line 13c in the
  Schedule 2 group's renumbering. Re-quote the locator.

### C-PEOP-20. Elective deferral limit $23,500 → $24,500 (in the input question)

- **Kind:** amount (parameter)
- **2026:** `iw2w3` p. 21: "Even though the 2026 limit for elective deferrals and designated Roth contributions is $24,500, Alex’s total elective deferral amount of $26,500 is reported in box 12 with code D" ... `n-25-67` p. 1: "is increased from $23,500 to $24,500."
- **2025:** `iw2w3` p. 20: "Even though the 2025 limit for elective deferrals and designated Roth contributions is $23,500, Alex's total elective deferral amount of $26,500 is reported in box 12 with code D"
- **Touches:** person.sav_excess, person.sav_excess_gate, person.sav_line2
- **Worklist items:** person.sav_excess, person.sav_excess_gate, person.sav_line2
- **Notes:** The literal "$23,500" sits in the `person.sav_excess` input text and its label year. Change it to $24,500
  and 2026, and re-quote the locators at p. 21. No parameter holds it.

### C-PEOP-21. Form 8880: the ABLE and saver's-match notes move from "What's New" to "Reminders"; years move

- **Kind:** wording only
- **2026:** `f8880` p. 3 (draft): "Permanent credit for Achieving a Better Life Experience (ABLE) account contributions. P.L. 119-21 made permanent the credit for contributions by a designated beneficiary to their ABLE account. See Pub. 907, Tax Highlights for Persons With Disabilities, for more information about ABLE accounts." ... `f8880` p. 3 (draft): "(b) is claimed as a dependent on someone else’s 2026 tax return;"
- **2025:** `f8880` p. 2: "Permanent credit for Achieving a Better Life Experience (ABLE) account contributions. P.L. 119-21, commonly known as the One Big Beautiful Bill Act, makes permanent the credit for contributions by a designated beneficiary to their ABLE account. See Pub. 907, Tax Highlights for Persons With Disabilities, for more information about ABLE accounts." ... `f8880` p. 2: "(b) is claimed as a dependent on someone else’s 2025 tax return;"
- **Touches:** person.sav_line1, person.sav_prior_joint, person.sav_prior_other, person.sav_claimed, person.sav_able (ambiguity amb.2025.savers_2026_joint)
- **Worklist items:** person.sav_line1, person.sav_prior_joint, person.sav_prior_other, person.sav_claimed
- **Notes:** The ABLE refusal text is the same under the new heading. Replace "p. 2, What’s New" with "p. 3, Reminders"
  (draft) in the locators. The figures that differ near `person.sav_claimed` are the AGI limits ("more than $40,250
  ($60,375 if head of household; $80,500 if married filing jointly)", f8880 p. 2 (draft)) and the birth date "January 1,
  2009". Both belong to `savers.agi_limit` and the Form 8880 group. `person.sav_claimed` and `person.sav_trad`
  also cite i1040gi (C-PEOP-23).

### C-PEOP-22. Pub. 575 / Pub. 590-B / i8889 sentences near pension, rollover and marital-status cites

- **Kind:** wording only
- **2026:** `p575` p. 13 (draft): "If your annuity starting date is after 1986, the total amount of annuity income that you can exclude over the years as a recovery of the cost can’t exceed your total cost." ... `p575` p. 36 (draft): "For example, if you received a $18,000 qualified disaster recovery distribution in 2024, you can include $6,000 in your income in 2024, 2025, and 2026." ... `i8889` p. 6 (draft): "If, at the end of 2026, you were age 55 or older and unmarried or married with self-"
- **2025:** `p575` p. 12: "If your annuity starting date is after 1986, the total amount of annuity income that you can exclude over the years as a recovery of the cost can’t exceed your total cost." ... `p575` p. 35: "if you received a $18,000 qualified disaster recovery distribution in 2023, you can include $6,000 in your income in 2023, 2024, and 2025." ... `i8889` p. 4: "If, at the end of 2025, you were age 55 or older and unmarried or married with self-"
- **Touches:** retirement.recovered, retirement.annuity, retirement.special, retirement.rollover, household.married, scope.other_income
- **Worklist items:** retirement.recovered, retirement.annuity, retirement.special, retirement.rollover
- **Notes:** The cited sentences are unchanged or only move a year or a page. In p590b (draft) "applicable required
  beginning date" becomes "applicable age" (p. 7), and the 2025 sentence on repaying pre-2023 birth or adoption
  distributions "before January 1, 2026" is dropped. The `scope.other_income` question must move the 3-year spread
  window from "received in 2023 or 2024" to "2024 or 2025". The main sources of these items (i1040gi, p560, p501)
  wait under C-PEOP-23 and C-PEOP-24.

### C-PEOP-23. Items waiting on the 2026 Instructions for Form 1040 (i1040gi not archived)

- **Kind:** waiting for a 2026 source (kind (b); owner decision 2026-11-04: not counted as wording only)
- **2026:** no counterpart: i1040gi has no 2026 edition archived. For the lines read, `f1040` p. 2 (draft) prints "IRA distributions" and "Pensions and annuities" (lines 4a and 5a) and a new "PSO" box on line 5c
- **2025:** `i1040gi` (pages as cited by each item: pp. 17–19, 26–30, 39–43, 95, 98)
- **Touches:** dependent.tin, person.tin, household.credit_disallowed, household.married, person.sav_trad, person.sav_claimed, retirement.account, retirement.annuity, retirement.rollover, retirement.special, retirement.recovered, retirement.amount_a, retirement.taxable
- **Worklist items:** dependent.tin, person.tin, household.credit_disallowed, household.married, person.sav_trad, retirement.amount_a, retirement.taxable
- **Notes:** These cannot be settled until the 2026 i1040gi is posted. Then re-check the TIN/SSN questions (the 2026
  drafts add valid-SSN tests for education credits, C-PEOP-16, and the f1040 draft adds a citizenship/work-authorization
  question), the lines 4a–5b worksheets and the Simplified Method Worksheet. `household.married` also cites p501, which
  is not archived for 2026. The other items listed under Touches are settled in other entries for their other quotes.

### C-PEOP-24. Items waiting on other unarchived 2026 editions (i4562, p970, p590a, p560, p501)

- **Kind:** waiting for a 2026 source (kind (b); owner decision 2026-11-04: not counted as wording only)
- **2026:** no counterpart: i4562, p970, p590a, p560 and p501 have no 2026 edition archived
- **2025:** `i4562` p. 4 (section 179 and mid-quarter items); `p970` p. 11 (line 31); `p590a` p. 35 (excess contributions); `p560` p. 18 (SIMPLE rollovers); `p501` p. 6 (marital status)
- **Touches:** person.cost179, person.income179, person.mq_q4, person.mq_total, person.s179_listed, person.s179_nonlisted, person.sc_count, dependent.edu_line31, person.edu_line31, person.sav_line1
- **Worklist items:** person.cost179, person.income179, person.mq_q4, person.mq_total, person.s179_listed, person.s179_nonlisted, person.sc_count, dependent.edu_line31, person.edu_line31
- **Notes:** The section 179 and mid-quarter person lines wait on the 2026 i4562; the Form 4562 draft is archived but is not
  the cited text. The line 31 refusals wait on Pub. 970. `person.sav_line1` (p590a) is also covered by C-PEOP-21, and
  `retirement.rollover` (p560) by C-PEOP-22.

### C-PEOP-25. Exclusions for qualified principal residence debt and student loan discharges end after 2025

- **Kind:** not encoded
- **2026:** `p4681` p. 3 (draft): "However, a discharge in 2026 can still be excluded from income if the discharge arrangement was entered into and evidenced in writing before 2026." ... `p4681` p. 3 (draft): "The temporary exclusion for many student loan discharges expired after 2025."
- **2025:** `i1099ac` p. 1: "The exclusion from income of discharged mortgage debt for qualified principal residence indebtedness and qualified student loan debt under section 108(f)(5) expires on December 31, 2025."
- **Touches:** s1.cod_unsupported
- **Worklist items:** none (What's New items in p4681, i982, i1099ac)
- **Notes:** All exclusions and student-loan discharges are refused by `s1.cod_unsupported`, so nothing computed changes.
  The screen's wording ("for example qualified principal residence indebtedness") still fits. The p4681 draft adds an
  SSN valid for employment for the death/disability student-loan exclusion, which is behind the same gate.

### C-PEOP-26. Below-100% lawfully present alien branch repealed (sec. 71302)

- **Kind:** not encoded
- **2026:** `plaw-119-21` p. 252: "SEC. 71302. DISALLOWING PREMIUM TAX CREDIT DURING PERIODS OF MEDICAID INELIGIBILITY DUE TO ALIEN STATUS. (a) IN GENERAL.—Section 36B(c)(1) is amended by striking subparagraph (B)." ... `plaw-119-21` p. 253: "shall apply to taxable years beginning after December 31, 2025."
- **2025:** no counterpart (the 2025 encoding's refusal text cites i8962, which has no 2026 edition)
- **Touches:** f8962.alien_below, f8962.alien_branch
- **Worklist items:** none
- **Notes:** The 2025 tool already refuses the below-100% lawfully-present-alien case, so the refusal stays. Its remedy
  wording should no longer suggest that such a person "can be an applicable taxpayer". Sec. 71301 (p. 251) also limits
  the credit to "eligible aliens". The 2026 i8962 must say how a filer answers that question, so re-check it then.
- **Correction (verification):** section 71301 (eligible aliens) does not apply to 2026: `plaw-119-21` p. 252, "shall apply to taxable years beginning after December 31, 2026". Only section 71302 (p. 253, "taxable years beginning after December 31, 2025") is a 2026 change. Drop the sentence about "eligible aliens" for 2026.

### C-PEOP-27. No premium tax credit for a plan enrolled in during an income-based special enrollment period

- **Kind:** rule (definition change)
- **2026:** `plaw-119-21` p. 254: "SEC. 71304. DISALLOWING PREMIUM TAX CREDIT IN CASE OF CERTAIN COVERAGE ENROLLED IN DURING SPECIAL ENROLL" ... "shall apply with respect to plan years beginning after December 31, 2025."
- **2025:** no counterpart
- **Touches:** the coverage months of Form 8962 (`f1095a` entries and the monthly lines of `f8962`, which count a month when the Form 1095-A shows coverage); a new question or refusal per Form 1095-A
- **Worklist items:** none (added by the verification)
- **Notes:** Added from the independent verification. A qualified health plan "shall not include any plan enrolled in during a special enrollment period provided for by an Exchange" on the basis of expected household income and not tied to a qualifying event. The 2026 Instructions for Form 8962 (not posted) must say how a filer knows this; until then, refuse a Form 1095-A policy enrolled in during such a period.

### Worklist coverage

| item id | entry |
|---|---|
| dependent.dc_paid | C-PEOP-18 |
| dependent.edu | C-PEOP-16 |
| dependent.edu_line24 | C-PEOP-17 |
| dependent.edu_tin_issued | C-PEOP-16 |
| dependent.tin | C-PEOP-23 |
| dependent.edu_line31 | C-PEOP-24 |
| f1095a.line33a | C-PEOP-02 |
| f1095a.line33b | C-PEOP-02 |
| f1095a.line33c | C-PEOP-02 |
| f1095a.yr_a_monthly | C-PEOP-02 |
| f1095a.yr_a_uniform | C-PEOP-02 |
| f1095a.yr_b_monthly | C-PEOP-02 |
| f1095a.yr_b_uniform | C-PEOP-02 |
| f1095a.yr_c_monthly | C-PEOP-02 |
| ptc.months | C-PEOP-02 |
| f5329 | C-PEOP-04 |
| f5329.files | C-PEOP-04 |
| f5329.l2 | C-PEOP-05 |
| f5329.l4 | C-PEOP-03 |
| f5329.must | C-PEOP-04 |
| f5329.one | C-PEOP-04 |
| f5329.rate10 | C-PEOP-03 |
| f5329.tax10 | C-PEOP-03 |
| f8962.line24 | C-PEOP-13 |
| f8962.line25 | C-PEOP-13 |
| f8962.line29 | C-PEOP-12 |
| ptc.repay_200 | C-PEOP-12 |
| ptc.repay_300 | C-PEOP-12 |
| ptc.repay_400 | C-PEOP-12 |
| household.credit_disallowed | C-PEOP-23 |
| household.married | C-PEOP-23 |
| household.persons | C-PEOP-01 |
| household.roster_bad | C-PEOP-01 |
| household.roster_ok | C-PEOP-01 |
| household.spouses | C-PEOP-01 |
| household.taxpayers | C-PEOP-01 |
| ira.all_total | C-PEOP-08 |
| person | C-PEOP-01 |
| person.cost179 | C-PEOP-24 |
| person.edu | C-PEOP-16 |
| person.edu_fulltime | C-PEOP-17 |
| person.edu_line24 | C-PEOP-17 |
| person.hsa_addtax | C-PEOP-19 |
| person.income179 | C-PEOP-24 |
| person.ira_basis_adjusted | C-PEOP-10 |
| person.ira_own_total | C-PEOP-08 |
| person.mq_q4 | C-PEOP-24 |
| person.mq_total | C-PEOP-24 |
| person.role | C-PEOP-01 |
| person.s179_listed | C-PEOP-24 |
| person.s179_nonlisted | C-PEOP-24 |
| person.sav_claimed | C-PEOP-21 |
| person.sav_excess | C-PEOP-20 |
| person.sav_excess_gate | C-PEOP-20 |
| person.sav_trad | C-PEOP-23 |
| person.sc_count | C-PEOP-24 |
| person.tin | C-PEOP-23 |
| person.x_c22 | C-PEOP-06 |
| person.x_cap22 | C-PEOP-06 |
| person.x_capped_sum | C-PEOP-05 |
| person.x_e22 | C-PEOP-06 |
| person.x_l2_all | C-PEOP-05 |
| person.x_limited_sum | C-PEOP-05 |
| person.x_must | C-PEOP-04 |
| person.x_other_exc | C-PEOP-05 |
| f5329.cap_abuse | C-PEOP-06 |
| person.edu_line31 | C-PEOP-24 |
| person.ira_8606_line2 | C-PEOP-10 |
| person.sav_line1 | C-PEOP-21 |
| person.sav_line2 | C-PEOP-20 |
| person.sav_prior_joint | C-PEOP-21 |
| person.sav_prior_other | C-PEOP-21 |
| retirement.account | C-PEOP-04 |
| retirement.annuity | C-PEOP-22 |
| retirement.bad_code | C-PEOP-04 |
| retirement.code_screen | C-PEOP-04 |
| retirement.early_screen | C-PEOP-05 |
| retirement.exc_amount | C-PEOP-05 |
| retirement.exc_capped | C-PEOP-05 |
| retirement.exception | C-PEOP-05 |
| retirement.has_exception | C-PEOP-05 |
| retirement.is_e19 | C-PEOP-07 |
| retirement.l2 | C-PEOP-05 |
| retirement.l2_e19 | C-PEOP-07 |
| retirement.recovered | C-PEOP-22 |
| retirement.rollover | C-PEOP-22 |
| retirement.screen_refused | C-PEOP-05 |
| retirement.special | C-PEOP-22 |
| retirement.amount_a | C-PEOP-23 |
| retirement.taxable | C-PEOP-23 |

## Business: Schedules C and SE, Forms 4562 and 7206, vehicles; Schedule E, Form 8582 and the K-1s

I read the 2026 archive editions of Schedule C (`f1040sc`, final), its instructions (`i1040sc`, IRS draft of
Oct 8, 2026), Schedule SE and its instructions (`f1040sse`, `i1040sse`, both final), Form 4562 (`f4562`, draft;
no 2026 `i4562` is archived), Form 7206 and its instructions (`f7206`, `i7206`, drafts), Notice 2026-10 (`n-26-10`),
Announcement 2026-11 in IRB 2026-29 (`irb26-29`), Rev. Proc. 2026-15 (`rp-26-15`), and, for the section 179 SUV limit,
Rev. Proc. 2025-32 (`rp-25-32`, archived under 2026 though not in the group list). Against them I read the 2025
editions the encoding cites (`f1040sc`, `i1040sc`, `f1040sse`, `i1040sse`, `f4562`, `i4562`, `f7206`, `i7206`,
`n-25-05`, `p946`). For the Stage 17 documents (`f1040se`, `i1040se`, `f8582`, `f1065sk1`, `f1120ssk`, `i1120ssk`,
`f1041sk1`, `i1041sk1`, `f6198`, `i6198`) I read the What's New / Reminders / Future Developments and the form-level
cautions only. The group file has 24 worklist items (23 distinct ids; `sc.f7206_line1` appears once as a line and
once as a refusal). Page numbers below are PDF pages: in the 2026 drafts the IRS cover is p. 1, so most 2026 `i1040sc`
pages are the 2025 page plus one. Notable: (1) the 2026 business standard mileage rate is two rates split at July 1,
2026 (72.5 and 76 cents), one of them not a whole number of cents; (2) Schedule C line 16 is re-cut into 16a / 16b
"Vehicle loan" / 16c "Other"; (3) Form 4562 line 14 becomes 14a–14d and Part VI moves to a new Form 4562-B;
(4) the 2026 meals text adds a section 274(o) disallowance and replaces the list of fully deductible meals; (5) the
pre-January 20, 2025 bonus rate falls from 40% to 20% for property placed in service in 2026; (6) the SE wage base,
section 179 limits, SUV limit, passenger-automobile limits and long-term care premium limits all change. Several
2025 citations rest on documents with no 2026 edition archived (`i4562`, `p946`, `p463`, `i1040gi`); those cites
cannot be re-verified for 2026 and are flagged in the entries.

### What's New and Reminders accounted for

| document | item (quoted heading or first words) | entry or "not encoded: reason" |
|---|---|---|
| i1040sc (draft) | Future Developments, "For the latest information about developments related to Schedule C" | not encoded: filing mechanics (web pointer) |
| i1040sc (draft) | What's New, "Standard mileage rate." | C-BUS-01 |
| i1040sc (draft) | What's New, "New Line 16b, Vehicle loan interest." | C-BUS-02 |
| i1040sc (draft) | What's New, "New Line 16c, Other interest." | C-BUS-02 |
| i1040sc (draft) | What's New, "Energy efficient commercial buildings deduction." (construction before July 1, 2026) | C-BUS-08 (line 27a is zero, Form 7205 refused by `sc.special`) |
| i1040sc (draft) | What's New, "Business meals deduction." (no deduction for employer-operated facility / convenience-of-employer meals) | C-BUS-04 |
| i1040sc (draft) | What's New, "Threshold for certain information reporting increased." ($600 to $2,000) | not encoded: Schedule C lines I and J are not encoded in `sc.yaml`; also changes the 1099-NEC thresholds on i1040sc pp. 8 (lines 10, 11), filing mechanics only |
| i1040sc (draft) | What's New, "Gambling losses." | not encoded in this group: a Schedule A rule (the itemized-deductions group); nothing in `sc`, `scveh`, `se`, `f4562`, `asset`, `s179`, `mq`, `ltc` reads it |
| i1040sc (draft) | What's New, "Deduction for qualified productions." (film/TV/live theatrical election ended after 2025) | C-BUS-08 (the section 181 items are refused by `sc.special`; films are refused by `asset.screen`) |
| i1040sc (draft) | What's New, "Deduction for production costs of qualified sound recording productions." | C-BUS-08 |
| i1040sc (draft) | What's New, "Section 179 deduction dollar limits increased." | C-BUS-09 |
| i1040sc (draft) | Reminders, "Form 1040-SS filers and business use of home." | not encoded: Form 1040-SS is outside the tool (unchanged from 2025) |
| i1040sc (draft) | Reminders, "Bonus depreciation." ("may be eligible for 100% bonus depreciation") | C-BUS-12 |
| i1040sc (draft) | Reminders, "Gig economy tax center." | not encoded: information pointer only |
| i1040sc (draft) | Reminders, "Small Business and Self-Employed (SB/SE) Tax Center." | not encoded: information pointer only |
| i1040sc (2025 only) | What's New items dropped in 2026 (R&E expenditures, "No tax on qualified tips/overtime/car loan interest", "Redesigned Form 1040-SS", "Reporting nontaxable Medicaid waiver payments", "Excess business loss limitation") | C-BUS-08 (R&E, Medicaid waiver, sound recording stay in the `sc.special` screen text) and C-BUS-02 (car loan interest moves to line 16b); tips/overtime belong to Schedule 1-A, not this group; excess business loss text still on 2026 p. 15 (Form 461 is refused through `sc.loss_allowed`/scope) |
| f1040sc (final) | no What's New on the form; form changes: line 16b "Vehicle loan", 16c "Other"; address block split | C-BUS-02; address lines not encoded (filing mechanics) |
| i1040sse (final) | Future Developments | not encoded: web pointer |
| i1040sse (final) | What's New, "Maximum income subject to social security tax." ($184,500) | C-BUS-14 |
| i1040sse (final) | Reminder, "Form 1040-SS. Using Schedule SE (Form 1040) to report self-employment tax for residents of U.S. territories." | not encoded: Form 1040-SS is outside the tool; unchanged from 2025 |
| f1040sse (final) | no What's New; line 7 and 8a amount; optional-method amounts on p. 2 | C-BUS-14, C-BUS-15 |
| f4562 (draft) | no What's New on the form; form changes: lines 14a–14d, 19g/19h relabeled, new 19k, Part VI removed | C-BUS-10, C-BUS-11 |
| f7206 (draft) | no What's New; line 2 amounts | C-BUS-16 |
| i7206 (draft) | Future Developments | not encoded: web pointer |
| i7206 (draft) | Reminder, "This form and its separate instructions have replaced the Self-Employed Health Insurance Deduction Worksheet" | not encoded: unchanged from 2025, history only |
| n-26-10 | Section 3, business standard mileage rate 72.5 cents | C-BUS-01 |
| n-26-10 | Section 3, charitable 14 cents and medical/moving 20.5 cents | not encoded in this group (the medical and charitable rates belong to Schedule A; nothing in this group reads them) |
| n-26-10 | Section 4, "Basis reduction amount" (35 cents for 2026) | not encoded: a vehicle on which the standard mileage rate was used earlier is refused by `scveh.screen` ("you used the standard mileage rate for it in an earlier year") |
| n-26-10 | Sections 5 and 6, maximum standard automobile cost and employer-provided automobile values ($61,700) | not encoded: FAVR plans and employer fringe-benefit valuation are not encoded |
| irb26-29 | Announcement 2026-11, revised business rate 76 cents from July 1, 2026; medical and moving 23.5 cents | C-BUS-01 (business); medical/moving not in this group |
| rp-26-15 | Section 2.02, 20 percent applicable percentage for property acquired before January 20, 2025 and placed in service in 2026 | C-BUS-12 |
| rp-26-15 | Section 4.01, Tables 1 and 2 (passenger automobile limits) | C-BUS-13 |
| rp-26-15 | Section 4.02, Table 3 (lessee inclusion amounts) | not encoded: the inclusion amount for a leased vehicle is refused by `sc.special` ("an inclusion amount for leased property") |
| i1040se (draft) | Future Developments | not encoded: Stage 17 not built |
| i1040se (draft) | What's New, "Standard mileage rate." (rental activities) | not encoded: Schedule E is behind `scope.schedule1` ("rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1)"); the rate itself is C-BUS-01 |
| i1040se (draft) | What's New, "Bonus depreciation." (100% permanent after January 19, 2025) | not encoded: `scope.schedule1`; for Schedule C see C-BUS-12 |
| i1040se (draft) | What's New, "New Form 4562-B." | not encoded: `scope.schedule1`; for Schedule C see C-BUS-11 |
| i1040se (draft) | What's New, "New Publication 1099." | not encoded: filing mechanics |
| i1040se (draft) | What's New, "Reporting threshold increased." | not encoded: filing mechanics |
| i1040se (draft) | What's New, "Increased section 179 deduction dollar limits." | not encoded for Schedule E (`scope.schedule1`); the limits are C-BUS-09 |
| i1040se (draft) | What's New, "New line 13a—Vehicle loan." | not encoded: `scope.schedule1` (Stage 17); compare C-BUS-02 for Schedule C |
| i1040se (draft) | What's New, "Limitation on gambling losses." | not encoded: Schedule A rule, outside this group |
| i1040se (draft) | What's New, "Form 7205, Energy Efficient Commercial Buildings Deduction." (property placed in service on or before June 30, 2026) | not encoded: `scope.schedule1`; Schedule C side is C-BUS-08 |
| i1040se (draft) | What's New, "Qualified business income (QBI) deduction." (made permanent) | not encoded in this group (QBI group) |
| i1040se (draft) | Reminders, "Business interest expense limitation." | not encoded: `scope.schedule1`; Form 8990 refused for Schedule C by `sc.special` |
| i1040se (draft) | Reminders, "No tax on car loan interest." | not encoded: `scope.schedule1` |
| i1040se (draft) | Reminders, "Excess business loss limitation." | not encoded: `scope.schedule1` |
| f1040se (draft) | no What's New on the form (form adds line 13a/13b and a page 3 "Part V Summary", lines 40–43) | not encoded: `scope.schedule1` (Stage 17 not built) |
| f8582 (draft) | form caution "Complete Parts IV and V before completing Part I." (standing caution; no What's New; no 2026 `i8582` archived) | not encoded: passive activities refused by `sc.passive` (line G) and `scope.schedule1` |
| f1065sk1 (draft) | no What's New (form text unchanged apart from the year) | not encoded: `scope.schedule1` |
| f1120ssk (draft) | no What's New (item H, number of shares, reworded) | not encoded: `scope.schedule1` |
| i1120ssk (draft) | Future Developments | not encoded: `scope.schedule1` |
| i1120ssk (draft) | Reminders, "Schedule K-1, box 12, code X." (section 181 sound recording) | not encoded: `scope.schedule1` |
| i1120ssk (draft) | Reminders, "Schedule K-1, box 17, code BA." (section 174A R&E) | not encoded: `scope.schedule1` |
| i1120ssk (draft) | Reminders, "Schedule K-1, box 17, code ZZ." (section 1062 farmland; section 139L) | not encoded: `scope.schedule1` |
| f1041sk1 (draft) | no What's New (layout changes only) | not encoded: `scope.schedule1` |
| i1041sk1 (draft) | Future Developments | not encoded: `scope.schedule1` |
| i1041sk1 (draft) | Reminders, "Excess deductions on termination." | not encoded: `scope.schedule1` |
| f6198, i6198 (Rev. November 2025) | no What's New; the 2026 archive files are byte-identical to the 2025 archive files | not encoded: Form 6198 refused by `sc.loss_allowed` (refusal when `sc.not_at_risk`); no change |

### C-BUS-01. Business standard mileage rate: 72.5 cents to June 30, 76 cents from July 1, 2026

- **Kind:** rule (definition change)
- **2026:** `n-26-10` p. 3: "The standard mileage rate for transportation or travel expenses for 2026 is 72.5 cents per mile for all miles of business use (business standard mileage rate)."; `irb26-29` p. 13: "(1) Business 76 cents per mile" and "The revised standard mileage rates set forth in this announcement apply to deductible transportation expenses paid or incurred for business, medical, or moving expense purposes on or after July 1, 2026"; `i1040sc` p. 7 (draft): "Multiply your business miles driven from January 1, 2026, to June 30, 2026, by 72.5 cents per mile; • Multiply your business miles driven from July 1, 2026, to December 31, 2026, by 76 cents per mile"
- **2025:** `n-25-05` p. 2: "The standard mileage rate for transportation or travel expenses for 2025 is 70 cents per mile for all miles of business use (business standard mileage rate)."; `i1040sc` p. 6: "Multiply the number of business miles driven by 0.70."
- **Touches:** `sc.mileage_rate` (param), `scveh.rate`, `scveh.smr_amount`, `scveh.miles_business`, `scveh.line9_standard`, `scveh.line9`
- **Worklist items:** sc.mileage_rate, scveh.rate, scveh.smr_amount
- **Notes:** The single rate times the single business-miles input becomes two products: business miles January 1–June 30 times 72.5 cents plus business miles July 1–December 31 times 76 cents, so `scveh.miles_business` must be asked in two parts (their sum still feeds the business-use percentage and Part IV line 44a) and two parameters replace `sc.mileage_rate`. 72.5 cents is not a whole number of cents, so it cannot be held as a NonNegDollars cents value like the 2025 `70`; the adoption needs a rate type (or a finer unit) and a rounding rule for the product, which no archived 2026 source states (a new ambiguity). The 2026 cites are final (`n-26-10`, `irb26-29`); the split by date is also stated in the draft `i1040sc`.
- **Owner decision (2026-11-04):** store each rate as an exact rate (the `Rate` type, num/den) and round at the line; do not refuse mileage that spans both periods. Proposal: parameters `sc.mileage_rate_h1` (725/1000 dollars per mile, `n-26-10` p. 3) and `sc.mileage_rate_h2` (76/100, `irb26-29` p. 13) replace `sc.mileage_rate` (`params-2026.proposed.yaml`); `forms-proposed/scveh.yaml` asks the business miles of each period (`scveh.miles_business_h1`, `scveh.miles_business_h2`; `scveh.miles_business`, line 44a, becomes their sum), multiplies each period's miles, as dollars, by its rate with `multiply_rate` (half-up to the cent, the 2025 reading `amb.2025.multiplication_subcent`) and adds the two products (`scveh.smr_amount`); `scveh.rate` is removed. Only the 72.5-cent product can have a fraction of a cent (half a cent), and the 76-cent product is whole cents, so rounding each product or their sum gives the same line 9. Two source-predicted cases: `ty2026.scveh.mileage_*`.

### C-BUS-02. Schedule C line 16 split: new 16b "Vehicle loan", 16c "Other"

- **Kind:** new line or form
- **2026:** `f1040sc` p. 1: "Vehicle loan" (the line 16b caption; the text layer separates the line numbers from the captions); `i1040sc` p. 2 (draft): "New Line 16b, Vehicle loan interest. Use line 16b to report the business-use portion of your vehicle loan interest." and "New Line 16c, Other interest. Use line 16c to report interest not claimed on line 16a or 16b."; `i1040sc` p. 9 (draft): "Line 16b. Enter interest paid or accrued on debt incurred to purchase a vehicle that is used in your trade or business. Include all deductible vehicle loan interest allocable to business use ... If you use your vehicle for both business and personal purposes, allocate the vehicle loan interest between its business use and personal use. Deduct only the business-use portion of the vehicle loan interest on Schedule C (Form 1040)." and "If you did not receive a Form 1098, enter the interest on line 16c." and "include your share of the interest on line 16c" and "If you claim a deduction on Schedule 1-A (Form 1040) for vehicle loan interest, then you can’t claim a deduction for that same interest on Schedule C."; `i1040sc` p. 7 (draft): "Report the business-use portion of vehicle loan interest on line 16b, regardless of whether you use the business standard mileage rate or the actual costs of operating your vehicle." and, under the standard mileage rate, "Report the business-use portion of these expenses as follows: vehicle loan interest on line 16b and personal property taxes on your vehicle on line 23."
- **2025:** `f1040sc` p. 1: "b Other ... 16b"; `i1040sc` p. 8: "If you did not receive a Form 1098, enter the interest on line 16b." and "include your share of the interest on line 16b."; `i1040sc` p. 7: "If you use your vehicle for both business and personal purposes and you claimed a deduction in 2025 on Schedule 1-A (Form 1040) for the vehicle loan interest allocable to your personal use, then you can’t claim a deduction for that same interest on Schedule C."
- **Touches:** `sc.line16a` (cite), `sc.line16b`, `sc.line28`, `sc.line28_pre179`, `sc.line23` (source text), `scveh.operating` (source excludes interest), `carloan.col_ii_input` (outside this group), `amb.2025.vehicle_business_pct`
- **Worklist items:** sc.line16b
- **Notes:** Add a printed line 16b (business-use part of vehicle loan interest) and re-id today's `sc.line16b` as printed 16c (other interest, including mortgage interest without a Form 1098 and a co-borrower's share); add the new line to the line 28 sums. The instruction says to "allocate ... between its business use and personal use" without naming a method; if the adoption asks it per vehicle and prorates by business miles (as `scveh.operating_business` does), say so under `amb.2025.vehicle_business_pct` or a new ambiguity. The 2026 text also says, for the standard mileage rate, to deduct the business part of vehicle personal property taxes on line 23 (the 2025 text said only "Do not deduct depreciation, rent or lease payments, or your actual operating expenses"), so the `sc.line23` question should name it. `carloan.col_ii_input` (Schedule 1-A column (ii)) should read the new line 16b amount; its owner group must be told.

### C-BUS-03. Line 9 and line 20a vehicle text reworded ("business-use portion"); Schedule 1-A caution moved

- **Kind:** wording only
- **2026:** `i1040sc` p. 7 (draft): "Include on line 9 the business-use portion of expenses for gasoline, oil, repairs, insurance, license plates, etc.; and Report the business-use portion of theses expenses as follows: depreciation on line 13, vehicle loan interest on line 16b, rent or lease payments on line 20a, and personal property taxes on your vehicle on line 23." and "Add to this amount your parking fees and tolls and enter the total on line 9." and "You can’t use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle."; `i1040sc` p. 9 (draft): "Line 20a. If you rented or leased vehicles, machinery, or equipment, enter on line 20a the business-use portion of your rental cost."; `i1040sc` p. 8 (draft): "See the Instructions for Form 4562 and Pub. 946 to figure the amount to enter on line 13."
- **2025:** `i1040sc` p. 7: "Include on line 9 the business portion of expenses for gasoline, oil, repairs, insurance, license plates, etc.; and • Show depreciation on line 13 and rent or lease payments on line 20a."; `i1040sc` p. 6: "Add to this amount your parking fees and tolls; and • Enter the total on line 9." and "You can’t use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle."; `i1040sc` p. 8: "If you rented or leased vehicles, machinery, or equipment, enter on line 20a the business portion of your rental cost."; `i1040sc` p. 7: "See the Instructions for Form 4562 and Pub. 946 to figure the amount to enter on line 13."
- **Touches:** `scveh.is_actual_owned`, `scveh.operating`, `scveh.operating_business`, `scveh.line9_standard`, `scveh.lease`, `scveh.lease_smr_before`, `scveh.lease_business` (refusal), `sc.line20a`, `sc.line13`
- **Worklist items:** scveh.is_actual_owned, scveh.operating, scveh.operating_business, scveh.line9_standard, scveh.lease, sc.line20a, sc.line13, scveh.lease_smr_before, scveh.lease_business
- **Notes:** Every 2025 quote these cites carry has a 2026 counterpart that says the same thing ("business portion" becomes "business-use portion"; the routing list adds lines 16b and 23, handled in C-BUS-02); update the quotes and page numbers only. The Schedule 1-A caution printed on 2025 pp. 6, 7 and 8 now appears once, under Line 16b on 2026 p. 9 (C-BUS-02). `scveh.lease_smr_before`, `scveh.lease_business` and `sc.line13` also cite `p463` pp. 25–26 or `i4562` p. 13, which have no 2026 edition archived; those parts of the cites cannot be re-verified.

### C-BUS-04. Business meals: new section 274(o) disallowance and a new list of fully deductible meals

- **Kind:** rule (definition change)
- **2026:** `i1040sc` p. 2 (draft): "However no deduction is allowed for expenses paid or incurred after 2025 by an employer, including a sole proprietor, for meals provided to employees at an employer-operated facility or meals provided for the convenience of the employer."; `i1040sc` p. 11 (draft): "You can fully deduct the following meal expenses. • Meals provided to an employee if you include the value of the meals in the employee’s wages subject to withholding. • Meals provided to a nonemployee to the extent the value is includible in the recipient’s gross income and properly reported on Form 1099-NEC. • Meals provided to crew members on certain commercial fishing vessels and at other qualifying facilities. • Meals that are part of goods or services sold in a bona fide transaction for adequate and full consideration, such as food purchased to prepare meals for restaurant or catering customers, including meals consumed by employees at the worksite. See chapter 5 of Pub. 15, for details and other exceptions and Pub. 463." and "In general, an employer, including a sole proprietor, may not deduct costs paid or incurred after 2025 for the operation of an employer-operated eating facility ... and meals provided to employees for the convenience of the employer."
- **2025:** `i1040sc` p. 10: "However, you can fully deduct meals and incidentals furnished or reimbursed to an employee if you properly treat the expense as wages subject to withholding. You can also fully deduct meals and incidentals provided to a nonemployee to the extent the expenses are includible in the gross income of that person and reported on Form 1099-NEC. See chapter 5 of Pub. 15, Employer’s Tax Guide, for details and other exceptions. See also chapter 8 of Pub. 334."
- **Touches:** `sc.meals_100`, `sc.meals_50`, `sc.line24b`, `sc.meals_rate`, `sc.meals_rate_dot`, `amb.2025.meals_full_exceptions`
- **Worklist items:** sc.meals_100
- **Notes:** The quote `sc.meals_100` cites is not printed in 2026; its two cases survive reworded (no longer "meals and incidentals"), two cases are added (fishing-vessel crews; meals sold for full consideration, including meals consumed by employees at the worksite), and the 274(o) disallowance is new. The `sc.meals_100` question (which today also lists the Pub. 463 exceptions: client-reimbursed contractor, employee recreation, food for the public, meals sold) must be rebuilt from the 2026 list, and the meals_50 / meals_100 questions must exclude convenience-of-employer and employer-operated-facility meals; `amb.2025.meals_full_exceptions` rests on `p463` p. 16, which has no 2026 edition archived, so it must be re-ruled. The 50% and 80% rates are unchanged (2026 p. 11: "In most cases, you can deduct only 50% of your business meal expenses" and "the percentage is increased to 80%").

### C-BUS-05. Line 24a incidental expenses: "telegrams" dropped

- **Kind:** wording only
- **2026:** `i1040sc` p. 10 (draft): "They do not include expenses for laundry, cleaning and pressing of clothing, lodging taxes, or the costs of telephone calls."
- **2025:** `i1040sc` p. 9: "They do not include expenses for laundry, cleaning and pressing of clothing, lodging taxes, or the costs of telegrams or telephone calls."
- **Touches:** `sc.line24a`
- **Worklist items:** sc.line24a
- **Notes:** Drop "telegrams" from the question text and the cite; the $5-a-day optional method is unchanged (2026 p. 10: "The amount of the deduction is $5 a day").

### C-BUS-06. Simplified method: storage space allowed only if the home is the sole fixed location

- **Kind:** rule (definition change)
- **2026:** `i1040sc` p. 11 (draft): "Space used for storage is allowed only if the residence is the sole fixed location of your business."
- **2025:** no counterpart (`i1040sc` p. 10, Simplified method, has no such sentence: "In most cases, you’ll figure your deduction by multiplying the area (measured in square feet) used regularly and exclusively for business, regularly for daycare, or regularly for storage of inventory or product samples, by $5. The area you use to figure your deduction cannot exceed 300 square feet.")
- **Touches:** `sc.ho_uses`, `sc.ho_sqft`
- **Worklist items:** none (found in the 2026 text; not a worklist item)
- **Notes:** Both questions count "regularly for storing inventory or product samples" with no condition; add the sole-fixed-location condition (or screen storage use where the home is not the sole fixed location). The $5 rate and 300 square feet are unchanged (2026 p. 14, worksheet lines 2 and 3a).

### C-BUS-07. Simplified Method Worksheet line 5: unchanged

- **Kind:** wording only
- **2026:** `i1040sc` p. 14 (draft): "Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4 here and include that amount on Schedule C, line 30. If zero or less, enter -0-"
- **2025:** `i1040sc` p. 12: "Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4 here and include that amount on Schedule C, line 30. If zero or less, enter -0-"
- **Touches:** `sc.ho_line5_lim`, `sc.ho_line5`, `sc.ho_rate`
- **Worklist items:** sc.ho_line5_lim
- **Notes:** The differing sentence is only the label "3a." on the worksheet (and page moves from p. 12 to p. 14). `sc.ho_line5_lim` also cites `p946` p. 19 (no 2026 edition archived); that part of the cite cannot be re-verified.

### C-BUS-08. The `sc.special` screen: items reworded, dropped or dated in 2026

- **Kind:** wording only
- **2026:** `i1040sc` p. 11 (draft): "Enter the total salaries and wages for the tax year reduced by the amount of the following credit(s), if applicable. • Work Opportunity Credit (Form 5884). • Credit for Employer Differential Wage Payments (Form 8932). • Employer Credit for Paid Family and Medical Leave (Form 8994)."; p. 7: "If you make this election, enter the amount of interest on Schedule 2 (Form 1040), line 7."; p. 3: "• Form 4562-B to claim amortization that began in 2026."; p. 2: "The energy efficient commercial buildings deduction is available only for property for which construction began before July 1, 2026." and "Qualified sound recording productions that are produced and recorded in the United States have been added to the types of property for which certain production costs may be deductible provided the production commences before January 1, 2026, in tax years ending after July 4, 2025."; p. 10: "See the Instructions for Form 4562-B for more information on amortization."
- **2025:** `i1040sc` p. 10: "• Work Opportunity Credit (Form 5884). • Empowerment Zone Employment Credit (Form 8844). • Credit for Employer Differential Wage Payments (Form 8932). • Employer Credit for Paid Family and Medical Leave (Form 8994)."; p. 6: "If you make this election, include the interest in the total on Schedule 2 (Form 1040), line 14, and enter the amount of interest and “453(l)(3)” on the line next to the entry space."; p. 1: "Domestic research and experimental expenditures. Beginning in 2025, you can deduct your domestic research and experimental expenditures as current business expenses or you can elect to capitalize and amortize the expenditures ratable over a period of 60 months or more." and "You may be eligible to deduct up to $150,000 of qualified sound recording production costs. This applies to costs starting after July 4, 2025, but before January 1, 2026."
- **Touches:** `sc.special`, `sc.screened`, `sc.line27a`
- **Worklist items:** sc.special
- **Notes:** Nothing computed changes: every item the screen names still leads to refusal. Update the question (Form 8844 is no longer named for line 26; 2026 p. 17 still says research and experimentation costs may be amortized, "see sections 174 and 174A") and refresh the cite's page numbers (2025 p. N is generally 2026 p. N+1) and its p. 1 What's New pointers, which are not printed in 2026. The `i8995` part of the cite still holds (`i8995` p. 3 (draft): "there is a presumption that you’re providing services as an employee for purposes of section 199A for the 3-year period after ceasing to be an employee"); the `p463` p. 12 and `i4562` p. 4 parts have no 2026 edition archived. The installment-interest location (Schedule 2 line 7) matters only to the Schedule 2 group.

### C-BUS-09. Section 179 limits: $2,560,000, $4,090,000, SUV $32,000

- **Kind:** amount (parameter)
- **2026:** `rp-25-32` p. 21: "the aggregate cost of any § 179 property that a taxpayer elects to treat as an expense cannot exceed $2,560,000 and, under § 179(b)(5)(A), the cost of any sport utility vehicle that may be taken into account under § 179 cannot exceed $32,000. Under § 179(b)(2), the $2,560,000 limitation under § 179(b)(1) is reduced (but not below zero) by the amount by which the cost of § 179 property placed in service during the 2026 taxable year exceeds $4,090,000."; `i1040sc` p. 2 (draft): "For 2026, the maximum section 179 expense deduction is $2,560,000. This limit is reduced by the amount by which the cost of section 179 property placed in service during the tax year exceeds $4,090,000."
- **2025:** `i4562` p. 1: "by the amount by which the cost of section 179 property placed in service during the tax year exceeds $4,000,000. Also, the maximum section 179 expense deduction for sport utility vehicles (SUVs) placed in service in tax years beginning in 2025 is $31,300."; `i1040sc` p. 1: "Beginning in 2025, the maximum section 179 expense deduction is $2.5 million."
- **Touches:** `s179.max`, `s179.threshold`, `s179.suv_limit` (params); `s179.line1`, `s179.line3`, `scveh.suv_cap`
- **Worklist items:** none (What's New item)
- **Notes:** Set `s179.max` 256000000, `s179.threshold` 409000000, `s179.suv_limit` 3200000, cited to `rp-25-32` p. 21 (final). The 2025 cites are to `i4562` pages; with no 2026 `i4562`, the Revenue Procedure is the citable 2026 source.

### C-BUS-10. Form 4562 Part I: note moved, years advanced

- **Kind:** wording only
- **2026:** `f4562` p. 2 (draft): "5 Dollar limitation for tax year. Subtract line 4 from line 1. If zero or less, enter -0-. If married filing separately, see instructions" and "10 Carryover of disallowed deduction from line 13 of your 2025 Form 4562" and "13 Carryover of disallowed deduction to 2027. Add lines 9 and 10, less line 12"
- **2025:** `f4562` p. 1: "5 Dollar limitation for tax year. Subtract line 4 from line 1. If zero or less, enter -0-. If married filing" and "10 Carryover of disallowed deduction from line 13 of your 2024 Form 4562" and "13 Carryover of disallowed deduction to 2026. Add lines 9 and 10, less line 12"
- **Touches:** `s179.line5`, `s179.line10`, `s179.line13`
- **Worklist items:** s179.line5
- **Notes:** The differing sentences are the "Note:" before Part II moving with the page layout and the year roll; line 5's text is the same. `s179.line5` also cites `i4562` p. 5 (married filing separately allocation), which has no 2026 edition archived; that cite cannot be re-verified until it is.

### C-BUS-11. Form 4562 Part II line 14 becomes 14a–14d; line 22 sum; Part VI moves to Form 4562-B

- **Kind:** new line or form
- **2026:** `f4562` p. 2 (draft): "14a Special depreciation allowance for certain qualified property (other than listed property) under section 168(k) 14a 14b Special depreciation allowance for certain specified plants bearing fruits and nuts under section 168(k)(5) 14b 14c Special depreciation allowance for qualified reuse and recycle property under section 168(m) . . . 14c 14d Special depreciation allowance for certain qualified production property under section 168(n) (attach statement) 14d" and "19k Qualified production property 39 yrs. MM S/L"; `f4562` p. 3 (draft): "22 Total. Add amounts from line 12, lines 14a through 14d, lines 15 through 17, lines 19 and 20 in column (g), and line 21."; `i1040sc` p. 3 (draft): "• Form 4562-B to claim amortization that began in 2026."
- **2025:** `f4562` p. 1: "14 Special depreciation allowance for qualified property (other than listed property) placed in service during the tax year. See instructions"; `f4562` p. 2: "22 Total. Add amounts from line 12, lines 14 through 17, lines 19 and 20 in column (g), and line 21."; `f4562` p. 3: "Part VI Amortization"
- **Touches:** `f4562.line14`, `f4562.line22`, `sc.dep_other`, `sc.f14`, `asset.bonus`, `asset.screen`
- **Worklist items:** sc.dep_other
- **Notes:** Re-number `f4562.line14` as printed 14a (section 168(k) property) and re-quote `f4562.line22` and `sc.dep_other`; lines 14b–14d need a decision: 14c (168(m)) and qualified production property are already refused by `asset.screen` ("qualified reuse and recycling property ... section 168(m)"; "qualified production property"), but specified plants (14b) are not named in the screen and must be screened or encoded. Lines 19g/19h are relabeled ("Water utility property", "Any railroad grading or tunnel bore") and 19k is new; all are real property or 25/50-year property that `asset.screen` refuses. Part VI's removal leaves the `f4562` note ("Part VI ... refused") and `asset.screen` ("you amortize it") needing only wording (Form 4562-B).

### C-BUS-12. Special depreciation allowance: 20% (not 40%) for property acquired before January 20, 2025

- **Kind:** amount (parameter)
- **2026:** `rp-26-15` p. 2: "Accordingly, the applicable percentage for qualified property acquired after September 27, 2017, and before January 20, 2025, and placed in service during calendar year 2026 is 20 percent."; `i1040sc` p. 2 (draft): "Certain qualified property acquired and placed in service after January 19, 2025, may be eligible for 100% bonus depreciation."
- **2025:** `i4562` p. 6: "Certain qualified property (defined below) acquired after September 27, 2017, and before January 20, 2025 (other than property with a long production period and certain aircraft), is limited to a special depreciation allowance of 40% of the depreciable basis of the property." and "However, you can elect to take a 40% special depreciation allowance for certain qualified property (60% for property with a long production period and certain aircraft), instead of the 100% special depreciation allowance in the first tax year ending after January 19, 2025."
- **Touches:** `sc.bonus_rate_40` (param), `asset.rate40`, `asset.bonus_forty`, `asset.bonus_fullcase`, `asset.bonus_choice`, `asset.after_jan19`, `scveh.rate40`, `scveh.bonus_forty`, `scveh.bonus_choice`, `scveh.after_jan19`
- **Worklist items:** none (Reminder and rp-26-15 item)
- **Notes:** The phase-down rate for pre-January 20, 2025 acquisitions becomes 20% (rename or replace `sc.bonus_rate_40`). The 2025 "forty" choice for property acquired after January 19, 2025 was, by the 2025 text, an election for "the first tax year ending after January 19, 2025"; no archived 2026 source restates or extends it (`i1040sc` 2026 drops the 2025 sentence "You can also elect to use the previous bonus depreciation phase-down rates instead of 100% expensing", and no 2026 `i4562` is archived), so whether `bonus_choice = forty` survives for 2026 property cannot be settled from the archive. Placed-in-service year ranges ("2005 to 2025", "2019 to 2025") roll forward one year.

### C-BUS-13. Passenger automobile depreciation limits for vehicles placed in service in 2026

- **Kind:** amount (parameter)
- **2026:** `rp-26-15` p. 7: "REV. PROC. 2026-15 TABLE 1 DEPRECIATION LIMITATIONS FOR PASSENGER AUTOMOBILES ACQUIRED AFTER SEPTEMBER 27, 2017, AND PLACED IN SERVICE DURING CALENDAR YEAR 2026, FOR WHICH THE § 168(k) ADDITIONAL FIRST YEAR DEPRECIATION DEDUCTION APPLIES ... 1st Tax Year $ 20,300 2nd Tax Year $ 19,800 3rd Tax Year $ 11,900 Each Succeeding Year $ 7,160" and "TABLE 2 ... FOR WHICH NO § 168(k) ADDITIONAL FIRST YEAR DEPRECIATION DEDUCTION APPLIES ... 1st Tax Year $ 12,300"
- **2025:** `p946` p. 59: "2025 $20,2001 $19,600 $11,800 $7,060" and (footnote) "If you elected not to claim any special depreciation allowance or the vehicle is not qualified property, the maximum depreciation deduction is $12,200."
- **Touches:** table `auto_limit`, table `auto_limit_first_nobonus`, `scveh.lim_first_bonus`, `scveh.lim_first_none`, `scveh.lim_2025`, `scveh.lim_prior`, `scveh.is2025`, `scveh.placed`, `scveh.too_old`, table `recovery_year`
- **Worklist items:** none (rp-26-15 item)
- **Notes:** Add rows y2026 year 1 = 2030000 (with the allowance) and 1230000 (without); vehicles placed in service 2020–2025 move one recovery year on, so the table needs y2025 year 2 (the 2025 `p946` row prints $19,600), y2024 year 3, and so on, and the 2019 vehicle's post-recovery case moves to a 2020 vehicle. Those later-year amounts are printed only in 2025 or earlier sources; no 2026 `p946` is archived. The 2026 Table 1 heading says "acquired after September 27, 2017", the same acquisition test as the 2025 table.

### C-BUS-14. Social security wage base $184,500

- **Kind:** amount (parameter)
- **2026:** `f1040sse` p. 1: "Maximum amount of combined wages and self-employment earnings subject to social security tax or the 6.2% portion of the 7.65% railroad retirement (tier 1) tax for 2026 ... 7 $184,500" and "If $184,500 or more, skip lines 8b through 10, and go to line 11"; `i1040sse` p. 1: "For 2026, the maximum amount of self-employment income subject to social security tax is $184,500."
- **2025:** `f1040sse` p. 1: "Maximum amount of combined wages and self-employment earnings subject to social security tax or the 6.2% portion of the 7.65% railroad retirement (tier 1) tax for 2025 ... 7 $176,100"
- **Touches:** `se.wage_base` (param), `line7` (forms/2025/se.yaml), `line9`, `ss_base`
- **Worklist items:** line7, se.wage_base
- **Notes:** Set `se.wage_base` to 18450000 and re-quote `line7`'s cite with "$184,500" (both 2026 sources are final). The 92.35%, $400, 12.4%, 2.9% and 50% figures on lines 4a, 4c, 10, 11 and 13 are unchanged on 2026 p. 1.

### C-BUS-15. Schedule SE optional-method amounts and instructions rewording

- **Kind:** not encoded
- **2026:** `f1040sse` p. 2: "You may use this method only if (a) your gross farm income1 wasn’t more than $11,340, or (b) your net farm profits2 were less than $8,186." and "14 Maximum income for optional methods ... 14 $7,560"
- **2025:** `f1040sse` p. 2: "You may use this method only if (a) your gross farm income1 wasn’t more than $10,860, or (b) your net farm profits2 were less than $7,840." and "14 Maximum income for optional methods ... 14 $7,240"
- **Touches:** none (`line4b` is zero; the optional methods are refused, se.yaml `line4b` cite "the optional methods are refused", and `sc.hi_screen` names "you used an optional method")
- **Worklist items:** none
- **Notes:** No adoption work beyond the year in cites. The remaining `i1040sse` differences are cross-reference forms ("Schedule C (Form 1040)", "Report this income on Schedule E (Form 1040)") and "ECI" for "ECI — Exempt community income" on Schedule 2 line 4 (church and community-income cases are refused).

### C-BUS-16. Form 7206 line 2 long-term care premium limits

- **Kind:** amount (parameter)
- **2026:** `f7206` p. 2 (draft): "$500— if that person is age 40 or younger $930— if age 41 to 50 $1,860— if age 51 to 60 $4,960— if age 61 to 70 $6,200— if age 71 or older"; `i7206` p. 3 (draft): "a. Age 40 or younger — $500. b. Age 41 to 50 — $930. c. Age 51 to 60 — $1,860. d. Age 61 to 70 — $4,960. e. Age 71 or older — $6,200."
- **2025:** `f7206` p. 1: "$480— if that person is age 40 or younger $900— if age 41 to 50 $1,800— if age 51 to 60 $4,810— if age 61 to 70 $6,020— if age 71 or older"
- **Touches:** table `ltc_limit`, `ltc.limit`, `ltc.amount`
- **Worklist items:** none
- **Notes:** Rows become 50000, 93000, 186000, 496000, 620000 (from a draft; confirm against the final Form 7206 when posted).
- **Correction (verification):** the long-term care limits are confirmed by `rp-25-32` p. 22 (final), section 4.27 (`changes.verification.md`).

### C-BUS-17. Form 7206 and its instructions: years only; i1040gi cites unverifiable

- **Kind:** wording only
- **2026:** `f7206` p. 2 (draft): "Amounts for any month you were eligible to participate in a health plan subsidized by your employer or your spouse’s employer or the employer of either your dependent or your child who was under the age of 27 at the end of 2026."; `i7206` p. 3 (draft): "See Pub. 974 if the insurance plan was considered to be established under your business and was obtained through the Marketplace, and advance payments of the premium tax credit were made or you are claiming the premium tax credit."
- **2025:** `f7206` p. 1: "Amounts for any month you were eligible to participate in a health plan subsidized by your employer or your spouse’s employer or the employer of either your dependent or your child who was under the age of 27 at the end of 2025."; `i7206` p. 2: "See Pub. 974 if the insurance plan was considered to be established under your business and was obtained through the Marketplace, and advance payments of the premium tax credit were made or you are claiming the premium tax credit."
- **Touches:** `sc.f7206_line1` (line and refusal), `sc.hi_screen`, `sc.hi_uses`, `sc.hi_screened`
- **Worklist items:** sc.f7206_line1 (line), sc.f7206_line1 (refusal), sc.hi_screen
- **Notes:** The `i7206` differences are the year, layout (the "CAUTION" markers became "Caution:" headings), a comma and a URL break; apart from the C-BUS-16 amounts nothing changes. Their main cites are to `i1040gi` pp. 94–95 (the QSEHRA sentence, the Marketplace exception, "material income-producing factor"), which has no 2026 edition archived, so those cites cannot be re-verified; the `i7206` part ("can’t be more than the appropriate limit shown on line 2 for that person") is on 2026 `i7206` p. 3 (draft).

### C-BUS-18. Schedule E, Form 8582, the K-1s and Form 6198: archived, not encoded

- **Kind:** not encoded
- **2026:** `i1040se` p. 2 (draft): "New line 13a—Vehicle loan. Use line 13a to report the business-use portion of your vehicle loan interest."; `f1040se` p. 2 (draft): "13a Vehicle loan ... 13a 13b Other ... 13b"; `i1120ssk` p. 2 (draft): "Code BA is added to report domestic research and experimental expenditures needed when making a section 59(e) election."
- **2025:** `f1040se` p. 1: "13 Other interest ... 13" (no vehicle-loan line)
- **Touches:** `scope.schedule1` (refusal), `sc.passive` (line G), `sc.loss_allowed` (Form 6198 refusal)
- **Worklist items:** none
- **Notes:** Stage 17 is not built; every What's New and Reminder item of these documents is listed in the table above as not encoded. Form 6198 and its instructions are the same Rev. November 2025 files in both archives. When Stage 17 is built, the Schedule E vehicle-loan line and the mileage split (C-BUS-01) apply to Schedule E as they do to Schedule C.

### Worklist coverage

| item id | entry |
|---|---|
| s179.line5 | C-BUS-10 |
| sc.dep_other | C-BUS-11 |
| sc.f7206_line1 (line and refusal items) | C-BUS-17 |
| sc.hi_screen | C-BUS-17 |
| sc.ho_line5_lim | C-BUS-07 |
| sc.line13 | C-BUS-03 |
| sc.line16b | C-BUS-02 |
| sc.line20a | C-BUS-03 |
| sc.line24a | C-BUS-05 |
| sc.meals_100 | C-BUS-04 |
| sc.special | C-BUS-08 |
| scveh.is_actual_owned | C-BUS-03 |
| scveh.lease | C-BUS-03 |
| scveh.lease_smr_before | C-BUS-03 |
| scveh.line9_standard | C-BUS-03 |
| scveh.operating | C-BUS-03 |
| scveh.operating_business | C-BUS-03 |
| scveh.rate | C-BUS-01 |
| scveh.smr_amount | C-BUS-01 |
| sc.mileage_rate | C-BUS-01 |
| scveh.lease_business | C-BUS-03 |
| line7 | C-BUS-14 |
| se.wage_base | C-BUS-14 |

## Public Law 119-21: the provisions in force for 2026 (statute read)

Owner decision 2026-11-04 (ADOPTION.md question 6): a full read of Public Law 119-21's provisions effective for 2026 that
touch the individual income tax as encoded (every form in `forms/2025/` and `params/2025.yaml`). Read: the table of
contents of Title VII (140 sections); for every section of Title VII, Subtitle A (sections 70001 to 70607,
`plaw-119-21` pp. 88–220) and Subtitle B, chapter 3, "Health tax" (sections 71301 to 71308, pp. 251–257), its heading,
the Code sections it amends and its effective-date clause. The full text was read for sections 70101 to 70120
(pp. 88–100), 70424 and 70425 (pp. 165–167) and 70437 to 70506 (pp. 178–181); for the other sections the passages
read were those that name an encoded form, input or amount (for example the Trump account sections 530A, 128 and
6434). A provision buried in the body of a long business, international or energy section with an unrelated heading
would not have been caught; none of those sections amends a Code section the encoding computes. The rest of Title VII (sections 71101 to 71121 Medicaid, 71201 to 71203 Medicare,
71401) and the other titles amend no part of the Internal Revenue Code that the encoding uses. Pages are PDF pages of
`sources/2026/plaw-119-21.txt`; every quote below is checked by `research/ty2026/check_quotes.py`. All rest on the
statute as printed (final); the IRS text that applies them is a draft or not posted.

Two provisions touch an encoded line or gate and had no entry: sections 70118 and 70107 (C-LAW-01 and C-LAW-02
below). Every other provision in force for 2026 that touches the encoding was already covered by an entry, listed
below. No provision was found that changes an encoded computation without an entry (the kind the verification found
in section 71304).

### C-LAW-01. Hazardous duty areas: the Sinai Peninsula treatment made permanent; Kenya, Mali, Burkina Faso and Chad added (sec. 70118; statute-sourced)

- **Kind:** not encoded (statute-sourced)
- **2026 (statute, final):** `plaw-119-21` p. 97: "Section 11026(a) of Public Law 115–97 is amended by striking ‘‘, with respect to the applicable period’’"; p. 98: "‘‘(1) the Sinai Peninsula of Egypt. ‘‘(2) Kenya. ‘‘(3) Mali. ‘‘(4) Burkina Faso. ‘‘(5) Chad.’’"; "shall take effect on January 1, 2026"
- **2025:** no counterpart in the encoding's sources (the encoding reads nontaxable combat pay from Form W-2 box 12, code Q)
- **Touches:** `s8812.combat_pay` (the refusal question "Any nontaxable combat pay (Form W-2, box 12, code Q)?", read by `eic` and `s8812`), `ira.combat_gate`
- **Worklist items:** none (found by the statute read)
- **Notes:** Section 11026 of Public Law 115-97 (printed as a note to 26 U.S.C. 112, p. 98; its base text is not archived) is made permanent, and its "qualified hazardous duty area" gains four countries from January 1, 2026. The encoding can meet it only through nontaxable combat pay (Form W-2 box 12, code Q), and every case with combat pay is refused; the question's wording still fits. Nothing computed changes. At adoption, confirm from the 2026 Form 1040 instructions that pay for service in these areas is reported as code Q.

### C-LAW-02. Alternative minimum tax: exemption amounts permanent, phase-out threshold re-based and its rate doubled (sec. 70107; statute-sourced)

- **Kind:** not encoded (statute-sourced)
- **2026 (statute, final):** `plaw-119-21` p. 92: "Section 55(d)(4) is amended"; "2018 (2026, in the case of the $1,000,000 amount in subparagraph (A)(ii)(I))"; p. 93: "by substituting ‘50 percent’ for ‘25 per- cent’"; "shall apply to taxable years beginning after December 31, 2025"
- **2025:** the 2025 encoding refuses the AMT on the filer's answer (`s2.amt`, "Are you required to file Form 6251 or do you have an AMT adjustment requiring its review?")
- **Touches:** `s2.amt` (the refusal question) and the refusals that read it (Form 6251)
- **Worklist items:** none (found by the statute read; the 2026 exemption amounts are the `rp-25-32` section .07 row of the priority What's New table)
- **Notes:** From 2026 the exemption phases out faster (50 percent) from a threshold re-based to 2025, so more filers may owe AMT. The encoding does not compute Form 6251 and relies on the filer's answer; the question's help must point to the 2026 Form 1040 instructions' worksheet (not posted) at adoption. Nothing computed changes.

### Every provision in force for 2026 that touches the encoding

- **2026 (statute, final):** sec. 70101, `plaw-119-21` p. 88: "Section 1(j) is amended"; "shall apply to taxable years beginning after December 31, 2025". The reduced rates of section 1(j) made permanent. Entry: C-PRI-10 (the 2026 rate tables, `rp-25-32`).
- **2026 (statute, final):** sec. 70102, `plaw-119-21` p. 88: "by striking ‘‘$18,000’’ both places it appears"; p. 89: "shall apply to taxable years beginning after December 31, 2024". The larger standard deduction made permanent (in the 2025 encoding). Entry: C-PRI-10 (2026 amounts from `rp-25-32`).
- **2026 (statute, final):** sec. 70103, `plaw-119-21` p. 89: "there shall be allowed a deduction in an amount equal to $6,000 for each qualified individual"; p. 90: "shall apply to taxable years beginning after December 31, 2024". Personal exemptions end; the deduction for seniors (in the 2025 encoding, Schedule 1-A). Entry: C-SCHED-02, C-SCHED-08 (amounts unchanged; the birth-date cutoff moves).
- **2026 (statute, final):** sec. 70104, `plaw-119-21` p. 90: "by striking ‘‘$2,000’’ and inserting ‘‘$2,200’’"; p. 91: "In the case of a taxable year beginning after 2025, the $2,200 amount in subsection (h)(2) shall be increased". The $2,200 child tax credit, indexed from 2026; the SSN rule (in the 2025 encoding). Entry: C-SCHED-25 (2026 amount still $2,200: `i1040s8812` and `rp-25-32`), C-SCHED-19.
- **2026 (statute, final):** sec. 70105, `plaw-119-21` p. 91: "by striking ‘‘$50,000 ($100,000 in the case of a joint return)’’ each place it appears and inserting ‘‘$75,000 ($150,000 in the case of a joint return)’’"; "shall be equal to the greater of"; p. 92: "shall apply to taxable years beginning after December 31, 2025". QBI: the phase-in range widens to $75,000 ($150,000 joint); the $400 minimum deduction. Entry: C-SCHED-31, C-SCHED-32 (the minimum deduction), C-SCHED-34 (the phase-in range; not encoded).
- **2026 (statute, final):** sec. 70107, `plaw-119-21` p. 92: "Section 55(d)(4) is amended"; p. 93: "by substituting ‘50 percent’ for ‘25 per- cent’"; "shall apply to taxable years beginning after December 31, 2025". AMT exemption amounts made permanent; the phase-out threshold re-based and its rate doubled. Entry: C-LAW-02 (new).
- **2026 (statute, final):** sec. 70108, `plaw-119-21` p. 93: "MORTGAGE INSURANCE PREMIUMS TREATED AS INTEREST"; "shall apply to taxable years beginning after December 31, 2025". Mortgage insurance premiums deductible as interest again. Entry: C-PRI-14.
- **2026 (statute, final):** sec. 70109, `plaw-119-21` p. 93: "or a State declared disaster"; p. 94: "shall apply to taxable years beginning after December 31, 2025". Casualty losses: state-declared disasters added. Entry: C-PRI-16.
- **2026 (statute, final):** sec. 70110, `plaw-119-21` p. 94: "the deductions allowed by section 162 for educator expenses"; "shall apply to taxable years beginning after December 31, 2025". Miscellaneous itemized deductions stay suspended; educator expenses become an itemized deduction. Entry: C-PRI-17 (Schedule A line 17k, refused).
- **2026 (statute, final):** sec. 70111, `plaw-119-21` p. 94: "shall be reduced by 2⁄37 of the lesser of"; p. 95: "without regard to section 68 and"; "shall apply to taxable years beginning after December 31, 2025". The 2/37 limitation on itemized deductions; QBI figured without it. Entry: C-PRI-18, C-SCHED-33, C-SCHED-27.
- **2026 (statute, final):** sec. 70112, `plaw-119-21` p. 95: "(other than a qualified bicycle commuting reimbursement)"; "shall apply to taxable years beginning after December 31, 2025". The bicycle commuting exclusion ends permanently. Entry: not encoded: an employer exclusion reflected in Form W-2 box 1 (`w2` reads the box).
- **2026 (statute, final):** sec. 70113, `plaw-119-21` p. 95: "MEMBERS OF THE INTELLIGENCE COMMUNITY"; p. 96: "shall apply to taxable years beginning after December 31, 2025". Moving expense deduction and exclusion: intelligence community added. Entry: C-PRI-11 (refused through `scope.schedule1`).
- **2026 (statute, final):** sec. 70114, `plaw-119-21` p. 96: "shall be equal to 90 percent of the amount of such losses during such taxable year"; "shall apply to taxable years beginning after December 31, 2025". Wagering losses at 90 percent. Entry: C-PRI-17.
- **2026 (statute, final):** sec. 70115, `plaw-119-21` p. 96: "Section 529A(b)(2)(B) is amended"; "shall apply to contributions made after December 31, 2025". ABLE contribution limit. Entry: not encoded (the `rp-25-32` section .13 row of the priority What's New table).
- **2026 (statute, final):** sec. 70116, `plaw-119-21` p. 97: "the amount of contributions made by the eligible individual during such taxable year to the ABLE account"; "shall apply to taxable years ending after December 31, 2025"; "shall apply to taxable years beginning after December 31, 2026". Saver's credit for ABLE contributions made permanent (the $2,100 amount starts in 2027). Entry: C-CRED-16, C-PEOP-21.
- **2026 (statute, final):** sec. 70117, `plaw-119-21` p. 97: "Section 529(c)(3)(C)(i)(III) is amended by striking ‘‘before January 1, 2026,’’"; "shall apply to taxable years beginning after December 31, 2025". 529-to-ABLE rollovers continue. Entry: not encoded: Form 1099-Q distributions are not computed.
- **2026 (statute, final):** sec. 70118, `plaw-119-21` p. 98: "‘‘(1) the Sinai Peninsula of Egypt. ‘‘(2) Kenya. ‘‘(3) Mali. ‘‘(4) Burkina Faso. ‘‘(5) Chad.’’"; "shall take effect on January 1, 2026". Hazardous duty areas: the Sinai Peninsula treatment made permanent; Kenya, Mali, Burkina Faso and Chad added. Entry: C-LAW-01 (new).
- **2026 (statute, final):** sec. 70119, `plaw-119-21` p. 98: "unless the taxpayer includes the taxpayer’s social security number on the return of tax for such taxable year"; p. 99: "shall apply to discharges after December 31, 2025". Death-or-disability student loan discharges: exclusion made permanent, SSN required. Entry: C-PEOP-25 (refused through `s1.cod_unsupported`).
- **2026 (statute, final):** sec. 70120, `plaw-119-21` p. 99: "in the case of any taxable year beginning in calendar year 2026, $40,400"; "in calendar year 2026, $505,000, and"; p. 100: "shall apply to taxable years beginning after December 31, 2024". The SALT limit: 2026 amounts. Entry: C-PRI-13.
- **2026 (statute, final):** sec. 70201, `plaw-119-21` p. 100: "There shall be allowed as a deduction an amount equal to the qualified tips"; p. 103: "In the case of any cash tips required"; "to be reported for periods before January 1, 2026". No tax on tips (in the 2025 encoding); the approximate-reporting transition ends with 2025, so 2026 statements report tips separately. Entry: C-SCHED-03, C-SCHED-04, C-PRI-24 (Form W-2 code TP).
- **2026 (statute, final):** sec. 70202, `plaw-119-21` p. 104: "SEC. 70202. NO TAX ON OVERTIME."; p. 105: "In the case of qualified overtime com"; "pensation required to be reported for periods before January 1,". No tax on overtime (in the 2025 encoding); the same transition ends with 2025. Entry: C-SCHED-05, C-PRI-24 (Form W-2 code TT).
- **2026 (statute, final):** sec. 70203, `plaw-119-21` p. 106: "SEC. 70203. NO TAX ON CAR LOAN INTEREST."; p. 109: "shall apply to indebtedness incurred after December 31, 2024". Car loan interest deduction (in the 2025 encoding). Entry: C-SCHED-06, C-SCHED-07 (no 2026 rule change).
- **2026 (statute, final):** sec. 70204, `plaw-119-21` p. 110: "before the date that is 12 months after the date of the enactment of this section"; p. 116: "EMPLOYER CONTRIBUTIONS TO TRUMP ACCOUNTS"; p. 117: "TRUMP ACCOUNTS CONTRIBUTION PILOT PROGRAM"; p. 118: "shall apply to taxable years beginning after December 31, 2025". Trump accounts, the section 128 employer exclusion and the section 6434 pilot program credit. Entry: C-PEOP-04, C-PEOP-11, C-PRI-24 (code TA), the Form 4547 rows of the SCHED and CRED What's New tables; refused (owner decision 2026-11-04).
- **2026 (statute, final):** sec. 70301, `plaw-119-21` p. 118: "FULL EXPENSING FOR CERTAIN BUSINESS PROPERTY". 100 percent bonus depreciation for property acquired after January 19, 2025 (in the 2025 encoding). Entry: C-BUS-12.
- **2026 (statute, final):** sec. 70302, `plaw-119-21` p. 120: "DOMESTIC RESEARCH OR EXPERIMENTAL EXPENDIT"; p. 123: "shall apply to amounts paid or incurred in taxable years beginning after December 31, 2024". Domestic research expenditures deductible (section 174A). Entry: C-BUS-08 (the 2026 Schedule C instructions name sections 174 and 174A); in force for 2025, no 2026 rule change.
- **2026 (statute, final):** sec. 70303, `plaw-119-21` p. 125: "MODIFICATION OF LIMITATION ON BUSINESS INTEREST"; "shall apply to taxable years beginning after December 31, 2024". Business interest limitation (Form 8990). Entry: not encoded: refused by the Schedule C screen (`sc` names Form 8990).
- **2026 (statute, final):** sec. 70304, `plaw-119-21` p. 125: "EXTENSION AND ENHANCEMENT OF PAID FAMILY AND MEDICAL LEAVE CREDIT"; p. 127: "shall apply to taxable years beginning after December 31, 2025". Paid family and medical leave credit (an employer's general business credit). Entry: not encoded: general business credits are outside the encoded forms.
- **2026 (statute, final):** sec. 70305, `plaw-119-21` p. 127: "EXCEPTIONS FROM LIMITATIONS ON DEDUCTION FOR BUSINESS MEALS"; "shall apply to amounts paid or incurred after December 31, 2025". Employer-provided meals disallowed, with exceptions. Entry: C-BUS-04.
- **2026 (statute, final):** sec. 70306, `plaw-119-21` p. 127: "by striking ‘‘$1,000,000’’ and inserting ‘‘$2,500,000’’"; p. 128: "shall apply to property placed in service in taxable years beginning after December 31, 2024". Section 179 limits (in the 2025 encoding; 2026 amounts indexed). Entry: C-BUS-09.
- **2026 (statute, final):** sec. 70307, `plaw-119-21` p. 128: "SPECIAL ALLOWANCE FOR QUALIFIED PRODUCTION PROP"; p. 131: "shall apply to property placed in service after the date of the enactment of this Act". Special allowance for qualified production property. Entry: not encoded: refused by the depreciation screen (`asset` names qualified production property).
- **2026 (statute, final):** sec. 70402, `plaw-119-21` p. 143: "ENHANCEMENT OF ADOPTION CREDIT"; p. 144: "shall apply to taxable years beginning after December 31, 2024". The adoption credit partly refundable (in force for 2025). Entry: not encoded: the adoption credit is refused; Schedule 3-A names the refundable adoption credit (C-PRI-05).
- **2026 (statute, final):** sec. 70404, `plaw-119-21` p. 144: "by striking ‘‘$5,000 ($2,500’’"; "and inserting ‘‘$7,500 ($3,750’’"; "shall apply to taxable years beginning after December 31, 2025". Dependent care assistance exclusion $7,500 ($3,750); taxable years beginning after December 31, 2025. Entry: C-CRED-11.
- **2026 (statute, final):** sec. 70405, `plaw-119-21` p. 144: "ENHANCEMENT OF CHILD AND DEPENDENT CARE TAX CREDIT"; p. 145: "shall apply to taxable years beginning after December 31, 2025". Child and dependent care credit rates. Entry: C-CRED-10.
- **2026 (statute, final):** sec. 70411, `plaw-119-21` p. 145: "TAX CREDIT FOR CONTRIBUTIONS OF INDIVIDUALS TO SCHOLARSHIP GRANTING ORGANIZATIONS"; p. 148: "shall apply to taxable years ending after December 31, 2026". Scholarship-granting organization credit. Entry: not effective for 2026.
- **2026 (statute, final):** sec. 70412, `plaw-119-21` p. 148: "EXCLUSION FOR EMPLOYER PAYMENTS OF STUDENT LOANS"; "shall apply to payments made after December 31, 2025". Employer student loan payments stay excludable (section 127). Entry: not encoded: an employer exclusion reflected in Form W-2 box 1.
- **2026 (statute, final):** sec. 70413, `plaw-119-21` p. 148: "ADDITIONAL EXPENSES TREATED AS QUALIFIED HIGHER EDUCATION EXPENSES FOR PURPOSES OF 529 ACCOUNTS"; p. 149: "shall apply to taxable years beginning after December 31, 2025". 529 accounts: more qualified expenses, $20,000 elementary and secondary limit. Entry: not encoded: Form 1099-Q distributions are not computed.
- **2026 (statute, final):** sec. 70421, `plaw-119-21` p. 157: "shall apply to amounts invested in qualified opportunity funds after December 31, 2026". Opportunity zones renewed. Entry: not effective for 2026 for new investments; `sales` refuses QOF dispositions and deferrals.
- **2026 (statute, final):** sec. 70424, `plaw-119-21` p. 165: "by striking ‘‘$300 ($600’’ and inserting ‘‘$1,000 ($2,000’’"; "shall apply to taxable years beginning after December 31, 2025". Charitable deduction for non-itemizers, $1,000 ($2,000). Entry: C-PRI-01 (refused; owner decision 2026-11-04).
- **2026 (statute, final):** sec. 70425, `plaw-119-21` p. 165: "exceeds 0.5 percent of the taxpayer’s contribution base"; p. 167: "shall apply to taxable years beginning after December 31, 2025". The 0.5 percent floor on individuals' charitable contributions; the 60 percent cash limit made permanent. Entry: C-PRI-15 (encoded from the statute; owner decision 2026-11-04).
- **2026 (statute, final):** sec. 70429, `plaw-119-21` p. 169: "by striking ‘‘$10,000’’ and inserting ‘‘$50,000’’"; "shall apply to taxable years beginning after December 31, 2025". Whaling captains' charitable expenses. Entry: not encoded: no input of the encoding asks for these expenses.
- **2026 (statute, final):** sec. 70431, `plaw-119-21` p. 170: "EXPANSION OF QUALIFIED SMALL BUSINESS STOCK GAIN EXCLUSION". Section 1202 exclusion expanded (stock acquired after enactment). Entry: not encoded: `sales` refuses section 1202 stock.
- **2026 (statute, final):** sec. 70432, `plaw-119-21` p. 173: "REPEAL OF REVISION TO DE MINIMIS RULES FOR THIRD PARTY NETWORK TRANSACTIONS". Form 1099-K threshold restored. Entry: not encoded: `sc` asks for gross receipts, whether or not on a Form 1099-K.
- **2026 (statute, final):** sec. 70433, `plaw-119-21` p. 173: "INCREASE IN THRESHOLD FOR REQUIRING INFORMATION REPORTING WITH RESPECT TO CERTAIN PAYEES"; p. 174: "shall apply with respect to payments made after December 31, 2025". Forms 1099-NEC and 1099-MISC threshold $2,000. Entry: not encoded (the `i1040sc` What's New row of the BUS table: Schedule C lines I and J are not encoded).
- **2026 (statute, final):** sec. 70437, `plaw-119-21` p. 178: "TREATMENT OF CAPITAL GAINS FROM THE SALE OF CER"; p. 180: "shall apply to sales or exchanges in taxable years beginning after the date of the enactment of this Act". The farmland installment election (Form 1062). Entry: C-PRI-03, C-PRI-04 (refused).
- **2026 (statute, final):** sec. 70438, `plaw-119-21` p. 180: "EXTENSION OF RULES FOR TREATMENT OF CERTAIN DIS"; "section 301 of such Act shall be applied by sub". Qualified disaster losses extended to disasters declared through enactment. Entry: not encoded: casualty losses and the disaster addition to the standard deduction are refused (`sa.unsupported`; C-PRI-16).
- **2026 (statute, final):** sec. 70501, `plaw-119-21` p. 180: "Section 25E(g) is amended by striking ‘‘December 31, 2032’’ and inserting ‘‘September 30, 2025’’". Used clean vehicle credit ends. Entry: not encoded: Form 8936 is not prepared.
- **2026 (statute, final):** sec. 70502, `plaw-119-21` p. 180: "inserting ‘‘acquired after September 30, 2025’’". Clean vehicle credit ends. Entry: not encoded: Form 8936 is not prepared (its repayment is a refused Schedule 2 item, `s2.other`).
- **2026 (statute, final):** sec. 70504, `plaw-119-21` p. 181: "Section 30C(i) is amended by striking ‘‘December 31, 2032’’ and inserting ‘‘June 30, 2026’’". Alternative fuel refueling property credit ends after June 30, 2026. Entry: not encoded: Form 8911 is not prepared.
- **2026 (statute, final):** sec. 70505, `plaw-119-21` p. 181: "inserting ‘‘placed in service after December 31, 2025’’". Energy efficient home improvement credit ends. Entry: C-CRED-01 to C-CRED-09.
- **2026 (statute, final):** sec. 70506, `plaw-119-21` p. 181: "inserting ‘‘with respect to any expenditures made after December 31, 2025’’". Residential clean energy credit ends. Entry: C-CRED-01 to C-CRED-09.
- **2026 (statute, final):** sec. 70601, `plaw-119-21` p. 214: "shall apply to taxable years beginning after December 31, 2026"; "shall apply to taxable years beginning after December 31, 2025". Excess business loss: amounts re-based for 2026; made permanent from 2027. Entry: C-PRI-12.
- **2026 (statute, final):** sec. 70604, `plaw-119-21` p. 215: "EXCISE TAX ON CERTAIN REMITTANCE TRANSFERS"; p. 216: "shall apply to transfers made after December 31, 2025". Excise tax on remittance transfers. Entry: not encoded: an excise tax collected by the transfer provider, not an item of Form 1040 in scope.
- **2026 (statute, final):** sec. 70606, `plaw-119-21` p. 219: "SOCIAL SECURITY NUMBER REQUIREMENT FOR AMERICAN OPPORTUNITY AND LIFETIME LEARNING CREDITS"; "shall apply to taxable years beginning after December 31, 2025". Education credits require an SSN. Entry: C-CRED-18, C-PEOP-16.
- **2026 (statute, final):** sec. 71301, `plaw-119-21` p. 251: "PERMITTING PREMIUM TAX CREDIT ONLY FOR CERTAIN INDIVIDUALS"; p. 252: "shall apply to taxable years beginning after December 31, 2026". Premium tax credit only for eligible aliens. Entry: not effective for 2026 (C-PEOP-26 correction).
- **2026 (statute, final):** sec. 71302, `plaw-119-21` p. 252: "Section 36B(c)(1) is amended by striking subparagraph (B)"; p. 253: "shall apply to taxable years beginning after December 31, 2025". The below-100% lawfully present alien branch repealed. Entry: C-PEOP-26.
- **2026 (statute, final):** sec. 71303, `plaw-119-21` p. 253: "REQUIRING VERIFICATION OF ELIGIBILITY FOR PREMIUM TAX CREDIT"; p. 254: "shall apply to taxable years beginning after December 31, 2027". Pre-enrollment verification. Entry: not effective for 2026.
- **2026 (statute, final):** sec. 71304, `plaw-119-21` p. 254: "shall apply with respect to plan years beginning after December 31, 2025". No credit for income-based special enrollment period plans. Entry: C-PEOP-27.
- **2026 (statute, final):** sec. 71305, `plaw-119-21` p. 254: "ELIMINATING LIMITATION ON RECAPTURE OF ADVANCE PAYMENT OF PREMIUM TAX CREDIT"; p. 255: "shall apply to taxable years beginning after December 31, 2025". No cap on repaying excess advance credit. Entry: C-PEOP-12.
- **2026 (statute, final):** sec. 71306, `plaw-119-21` p. 255: "SAFE HARBOR FOR ABSENCE OF DEDUCTIBLE FOR TELEHEALTH"; "shall apply to plan years beginning after December 31, 2024". Telehealth safe harbor made permanent (in force for 2025). Entry: C-PRI-22 (correction: no change from 2025).
- **2026 (statute, final):** sec. 71307, `plaw-119-21` p. 255: "BRONZE AND CATASTROPHIC PLANS TREATED AS HIGH DEDUCTIBLE HE"; "shall apply to months beginning after December 31, 2025". Bronze and catastrophic plans count as HDHPs. Entry: C-PRI-22.
- **2026 (statute, final):** sec. 71308, `plaw-119-21` p. 255: "TREATMENT OF DIRECT PRIMARY CARE SERVICE ARRANGEMENTS"; p. 256: "shall apply to months beginning after December 31, 2025". Direct primary care arrangements and HSAs. Entry: C-PRI-22, C-PRI-23.

### Provisions that do not touch the encoding

Sections 70106 (estate and gift tax), 70308 (advanced manufacturing investment credit), 70309 (exempt facility bonds),
70310 to 70354 (international and business interest coordination), 70401 (employer-provided child care credit), 70403
(adoption: special needs determined by tribal governments; in force for 2025, and the adoption credit is refused),
70414 (credentialing expenses for 529 accounts), 70415 and 70416 (tax-exempt organizations), 70422 and 70423 (housing
and new markets credits), 70426 (corporations), 70427 (distilled spirits), 70428 (Alaska native villages), 70430
(construction contracts), 70434 (sound recordings, already refused by the Schedule C and depreciation screens), 70435
(lenders' interest exclusion), 70436 (firearms transfer taxes), 70439 (REITs), 70503 and 70507 to 70525 (business
energy credits, fuel credits, partnerships' qualifying income), 70531 (customs), 70602 (partnership payments), 70603
(corporate compensation), 70605 (employee retention credit enforcement) and 70607 (Direct File task force): business,
corporate, international, excise, exempt-organization or administrative provisions with no line, input or parameter in
`forms/2025/` or `params/2025.yaml`.
