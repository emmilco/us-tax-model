# Lows on the income forms, as add-ons to the v2 income patches (lane A2-lows-inc)

claude-opus-5-5, judgment, year 2025, jurisdiction us. Written 2026-11-16. Read only on xint; nothing in xint or the
repository was written. No build, walk, engine run, test or model call was made.

Labels: **[C path:line]** = checked against that file in this session (xint, or a scratch copy of xint with the v2
patches applied); **[I]** = my inference; **[U]** = relayed from the bug entry, not re-checked.

## Summary

- **Two add-on patches**, in `patches/v3/`:
  - `inc-m12-lows.patch`: 27 hunks in `interview/2025/questions.yaml`, `forms/2025/scope.yaml`, `person.yaml`,
    `s1.yaml`. Fixes 19 entries, 4 of them only in part.
  - `inc-m34-lows.patch`: 12 hunks in `questions.yaml`, `forms/2025/s2.yaml`, `f8853c.yaml`,
    `ambiguities/2025.yaml`. Fixes 8 entries.
  - Every change is wording, a citation, or an ambiguity entry. **No expression, input, refusal or value changes.** No
    fixture or coverage file is touched.
- **Apply checks, on scratch copies** (`scratch/round4-lows-inc/`), with `patch -p1`:
  - m12-lows applies with no fuzz or offset after `int-n10-ticks` then v2 `inc-m12`, and also after v2 `inc-m34`.
  - **It does not apply after v2 `inc-m12` alone.** Two hunks edit prompts that `int-n10-ticks.patch` adds
    (`scope.household_pay`, `s1.nol_not_married`). It needs the merge order that v2 inc.md already tested:
    int-n10-ticks, then m12 v2, then m34 v2.
  - m34-lows applies with no fuzz after v2 `inc-m34` alone, and after the whole stack.
  - Both add-ons together apply in either order on top of the stack. Every edited YAML file parses.
- **Entries:**
  - 27 fixed or partly fixed.
  - 2 closed with no new text: BUG-0893 is obsolete; BUG-0894 closes with v2 m34.
  - 11 deferred (section 4).
  - BUG-0869 is **not** here: the v3 `older-credits-lows.patch` already edits `person.edu_over` (and its sibling
    `dependent.edu_over`). I dropped my hunk to avoid a clash.
- **A decision for the coordinator: what counts as a NEW review.** I read "a new review" as a per-form review
  (transcription, render, class M, completeness) of a form the v2 patch does not change, or a model change.
  - **Under that reading, no low here makes a new per-form review or class M due.** Every form file edited is one the
    v2 patches already change: scope, person, s1, s2, f8853c. The line-scoped transcription and render runs of those
    forms take in more lines (listed in section 3).
  - **What the add-ons do add:** sampled subjects. A question review is due for each edited bank entry. A gate review
    (screen and false-no) is due where the entry is a gate's condition or a gated question. That is about 30 question
    subjects and about 20 gate subjects beyond v2 (section 3). They are sampled at the release, and no wording fix of a
    gate low can avoid them: the lows were found by exactly those reviews.
  - **If the stricter reading is wanted** (no new subject of any kind), only these are left: BUG-0916, BUG-0917, the
    `f8853c.line17` half of BUG-0923, and BUG-0771 (a citation inside a line v2 already makes due). Drop the other hunks.
- **Red team, worst cases found** (detail per low):
  - BUG-0826: I dropped the entry's "a company you served". It would invite a nonemployee director to put
    self-employment option income on line 8k, with no SE tax.
  - BUG-0828: deferred. Its help-only option would refuse every couple with a section 6013(g) election to fix a rare
    NIIT case.
  - BUG-0811: the entry's sentence on unallocated family support has no archived source (0 hits in p504), so it is
    left out.

## 1. Fixed in inc-m12-lows.patch

Format per entry: still real?; the fix (verbatim new text); red team (who answers wrongly after the fix; the source);
fixture; closure text; reviews made due beyond v2.

### BUG-0809 `s1.gambling_pro`

- **Still real.** The prompt is "Is gambling your (or, on a joint return, your spouse's) business, the way a living is
  made?" [C xint questions.yaml:3818].
- **Fix.** New prompt (25 words): "Do you (or, on a joint return, your spouse) gamble as a business, regularly and
  steadily to make money, even part time beside a job?"
- **Red team.**
  - A frequent recreational bettor may answer Yes. That is an over-refusal; a Yes ends the interview.
  - A part-time professional is now a Yes.
  - Source: "Engaging in gambling activities as a trade or business is considered self-employment"
    [C p525.cols.txt:1136].
  - "Regularly and steadily to make money" is the trade-or-business test as I understand it. It is not in an archived
    source [I].
- **Fixture.** Existing row `other.professional_gambler` walks the question (Yes, refused). No value changes. Proposed
  row `other.gambler_part_time`: copy that row's answers; situation "a nurse who plays poker regularly and steadily for
  profit". Expected end: same refusal [I, not walked].
- **Closure.** "- **Fix:** s1.gambling_pro asks whether the filer gambles as a business, regularly and steadily to
  make money, even part time beside a job (bank prompt). No value or refusal changed."
- **Due.** question:s1.gambling_pro; the screen of s1.gambling_pro; gate:s1.has_gambling.

### BUG-0811 alimony (`s1.alimony_any`, `s1.alimony_received`, `s1.alimony_paid`)

- **Still real.** [C questions.yaml:3769, 4137, 4142]: the prompt says "support paid to a husband or wife"; the amount
  helps are "Give 0 if you received/paid none."
- **Fix.**
  - Prompt: "support paid to **or for** a husband or wife after a divorce or separation".
  - Gate help, adds: "Count payments made for the other person, such as their rent or tuition paid to a landlord or
    school."
  - Received help (40 words): "Count cash payments only, including those paid to others for you, such as your rent.
    Leave out child support, property, your own share of community income, and payments to keep up or use the payer's
    property. Give 0 if none."
  - Paid help: the mirror of it.
- **Red team.**
  - A payer who pays the mortgage on a house the payer owns is told to leave it out ("keep up … your own property").
    That is right [C p504.cols.txt:413-416].
  - Sources:
    - "payments to or for your spouse or former spouse" [C i1040gi.cols.txt:8748];
    - "Payments not alimony … Child support, Noncash property settlements, … community income … Payments to keep up
      the payer's property, or Use of the payer's property" [C p504.cols.txt:413-416].
  - **Not applied:** the entry's "a combined family-support payment not split by the agreement may be". It has no
    archived source ("unallocated" and "family support" have 0 hits in p504).
- **Fixture.** Existing rows `other.alimony_old_agreement`, `other.alimony_new_agreement` and
  `other.alimony_recapture`. No value changes.
- **Closure.** "- **Fix:** the s1.alimony_any prompt says support paid 'to or for' a spouse, and its help counts
  payments to a landlord or school; the s1.alimony_received and s1.alimony_paid helps say cash only and name the
  non-alimony parts (p504 p. 13). The unallocated-support sentence of the proposal was not used (no archived source)."
- **Due.**
  - question:s1.alimony_any, alimony_received and alimony_paid;
  - gate:s1.alimony_any (screen and false-no; the unit includes both amounts);
  - the screen of s1.alimony_unsupported is unchanged.

### BUG-0812 net operating loss: the carryback year (residual)

- **Still real, in part.**
  - The scope.nol half is **already fixed by v2 m12.** Its help now names "a business loss held back by the yearly
    limit (Form 461)" [C scratch n10m12 questions.yaml, scope.nol].
  - The marital half is still real: ticks "…when it arose" and "…for a year it arose, or since" [C xint
    questions.yaml:2091, 2097]; sources "the year any of the loss arose" [C xint s1.yaml:1577, 1614].
- **Fix.**
  - Ticks: "Not married to each other in one or more of its years" (`s1.nol_not_married`) and "A joint return was
    filed for any of its years" (`s1.nol_was_joint`).
  - Both helps: "Its years are each year it arose or was carried back to, and every year since. A Yes ends the
    interview here."
  - The int-n10-ticks prompt of nol_not_married gains "or was carried back to".
  - In s1.yaml, both sources and labels say "a year any of the loss arose or was carried back to".
- **Red team.**
  - I first drafted "not married … in all its years", the source's own phrase. A couple married in all years could read
    it as "were we unmarried in every year?" and answer No wrongly. "In one or more of its years" removes that reading.
  - A farmer with a carryback is now a Yes. Both are refusing questions, so a wrong Yes only over-refuses.
  - Source: "not married to each other in all years involved in figuring NOL carrybacks and carryovers"
    [C i172.cols.txt:88-89]; "filed a joint return for any or all of the tax years involved in figuring the NOL
    carryover" [C s1.yaml cite].
- **Fixture.** Existing row `s1o.nol_was_joint`. No row walks nol_not_married with Yes. Proposed row
  `s1o.nol_carryback_joint`: copy `s1o.nol_was_joint`; situation "a farming loss of 2024 carried back to a 2022 joint
  return; separate return now". Expected end: same refusal [I].
- **Closure.** "- **Fix:** the scope.nol help names an excess business loss (Form 461) (with BUG-0907); s1.nol_was_joint
  and s1.nol_not_married (ticks, help, sources) count a year the loss was carried back to."
- **Due.**
  - question:s1.nol_not_married and s1.nol_was_joint;
  - gate:s1.nol_joint and gate:s1.nol_separate (the units that found it);
  - transcription and render of s1 (two more lines).

### BUG-0813 `s1.uc_any`

- **Still real.** Its help is only "The state sends Form 1099-G for them." [C xint questions.yaml:3805].
- **Fix.** Help (33 words): "Count all benefits paid for you in 2025, including back pay for earlier weeks and amounts
  withheld, taken for a debt or later paid back. The state sends Form 1099-G, often only online."
- **Red team.**
  - A filer who repaid 2024 benefits in 2025 but received none in 2025 might answer Yes. The amount question follows
    and gives the true figure, so the cost is one question.
  - Sources:
    - "the total unemployment compensation paid to you in 2025" and "your state may issue an electronic Form 1099-G"
      [C i1040gi.cols.txt:8554];
    - "subtract the amount you repaid" [C :8546];
    - an amount taken for a debt is still received: "Income received by an agent for you", and the Example 1 creditor
      [C p525.cols.txt:48-49; I as applied to an offset].
- **Fixture.** Existing rows `other.unemployment` and `other.unemployment_fund_contributions`.
- **Closure.** "- **Fix:** s1.uc_any help counts benefits paid in 2025 for earlier weeks, withheld, taken for a debt or
  later repaid, and says the Form 1099-G may be online only."
- **Due.** question:s1.uc_any; gate:s1.uc_any.

### BUG-0814 `s1.alaska_any`

- **Still real.** It has no help [C xint questions.yaml:3862].
- **Fix.** New help (30 words): "Answer Yes even if all of it was taken for a debt or, at your request, sent to a charity
  or a college savings account; it is still your income."
- **Red team.**
  - None found who answers No wrongly after the fix.
  - Source: "If you received a payment from Alaska's mineral income fund … report it as income on … line 8g"
    [C p525.cols.txt:1060]; assignment of income, Example 1 [C :48-49]. That a levy counts is [I].
- **Fixture.** Existing row `other.alaska_dividend`.
- **Closure.** "- **Fix:** s1.alaska_any has help: a dividend taken for a debt, or sent at the filer's request to a
  charity or a college savings account, is still income (Pub. 525, Assignment of income)."
- **Due.** question:s1.alaska_any; gate:s1.alaska_any.

### BUG-0823 `s1.inmate_wages`

- **Still real.** Tick and prompt say "while in a jail or prison" [C xint questions.yaml:3798]. Since BUG-0766 the
  question refuses ("A Yes ends the interview here"). The entry's `s1.inmate_amount` help is moot: that input no longer
  exists [C forms/2025/s1.yaml, 0 matches].
- **Fix.**
  - Tick: "Pay in 2025 for work done as an inmate, including work release".
  - Prompt: "…paid for work done while an inmate of a jail, prison or other correctional facility, including work
    release?"
- **Red team.**
  - A person on home detention or probation might answer Yes. That over-refuses.
  - Source: "services performed while an inmate in a penal institution" [C i1040gi.cols.txt:8666]. That work release
    counts is [I].
- **Fixture.** Existing rows `other.inmate_wages` and `s1o.inmate_amount`.
- **Closure.** "- **Fix:** s1.inmate_wages (tick, prompt) asks about work done while an inmate of any correctional
  facility, including work release. The s1.inmate_amount help of the proposal is moot (the input was removed with
  BUG-0766)."
- **Due.** question:s1.inmate_wages; the screen of s1.inmate_wages and its false-no.

### BUG-0824 `s1.jury_any`

- **Still real** [C xint questions.yaml:3851].
- **Fix.**
  - Tick: "Jury duty pay, even if not chosen or given to an employer".
  - Prompt: "In 2025, did you (or, on a joint return, your spouse) get jury duty pay, even for days you were not
    chosen?"
  - Help: "Count pay for days you reported for jury selection, and pay you handed over to your employer."
- **Red team.**
  - None found.
  - Source: "Jury duty pay you receive must be included", and the hand-over rule [C p525.cols.txt:1165].
- **Fixture.** Existing row `other.jury_pay`. Proposed row `other.jury_pool_only`: copy its answers with a smaller
  amount [I].
- **Closure.** "- **Fix:** s1.jury_any (tick, prompt, help) asks about any jury duty pay, including days in the jury pool
  and pay handed to an employer."
- **Due.** question:s1.jury_any; gate:s1.jury_any.

### BUG-0825 `s1.scholarship_any`

- **Still real** [C xint questions.yaml:3836].
- **Fix.**
  - Tick: "Scholarship, fellowship or grant for study or research, not on a W-2".
  - Prompt: "…get a scholarship, a fellowship or a grant, for study or research, not on a W-2?"
  - Help: "Count Pell grants and other grants paid to you or straight to the school, and fellowship stipends or living
    allowances paid to you, whether or not you were a student."
- **Red team.**
  - A graduate assistant paid on a W-2 now answers No. That is right: line 8r is "not reported on Form W-2"
    [C i1040gi.cols.txt:8659].
  - That a postdoctoral fellowship counts is [I] (p970 not re-read).
- **Fixture.** Existing rows `other.scholarship` and `other.scholarship_tuition_only`.
- **Closure.** "- **Fix:** s1.scholarship_any (tick, prompt, help) names grants for research and fellowship stipends paid
  to the filer, not on a W-2."
- **Due.** question:s1.scholarship_any; gate:s1.scholarship_any.

### BUG-0804 `oi8z.amount` (part)

- **Still real.** No help [C xint questions.yaml:3940].
- **Fix.** Help (27 words): "For damages or a settlement, count the whole taxable part, including any share your lawyer
  kept, and leave out damages paid for medical care of emotional distress."
- **Red team.**
  - The help shows for every kind of line 8z item. It opens with "For damages or a settlement", so other kinds pass
    over it.
  - Source: p525 p. 32, Court awards and damages [U, the entry's quotes; the page is already cited by oi8z.injury].
  - **The pre-September 14, 1995 agreement is not covered.** A refusal would be a model change.
- **Fixture.** Existing rows `s1o.damages_injury` and `other.other_income_item`.
- **Closure.** "- **Fix (in part):** oi8z.amount has help for damages: the whole taxable part, with the lawyer's share, less
  damages for medical care of emotional distress. The pre-1995 agreement exclusion stays open (a refusal is a model
  change)."
- **Due.** question:oi8z.amount. **oi8z.yaml is not edited**, so no oi8z per-form review is due.

### BUG-0915 `f4137row.col_c` (bank part)

- **Still real** [C xint questions.yaml:1923; f4137row.yaml:8].
- **Fix.** Help: "Include card tips, tips from other workers, and tips you reported. Tips for December 2025 reported to
  the employer in January 2026 belong to 2026; tips for December 2024 reported in January 2025 belong here."
- **Red team.**
  - A tipped worker who reported December 2024 tips in mid-January, after the employer's deadline, may count them
    here; the source's rule is "reported timely".
  - Source: "Tips reported timely are included in gross income of the employee for the month and year in which the
    report is made", with the January 12, 2026 example [C f4137.cols.txt:52].
- **Not done:** the `f4137row.yaml` source ("received in 2025"). f4137row is not a v2 form, so changing it would make
  the f4137row transcription due. Deferred.
- **Fixture.** None walks col_c (0 coverage rows). No value changes.
- **Closure.** "- **Fix (in part):** the f4137row.col_c help counts December 2024 tips reported in January 2025. The
  input source stays open until f4137row's next change."
- **Due.** question:f4137row.col_c.

### BUG-0771 `scope.other_income` citation

- **Still real.** The four Line 1b, 1c, 1h and 1d quotes are in the locator [C xint scope.yaml:1229+, locator].
- **Fix.** Replace them with `p. 25, Missing or Incorrect Form W-2?, "Even if you don’t get a Form W-2, you must still
  report your earnings"`. That is the passage scope.wages_no_form cites [C scope.yaml:605].
- **Red team.** Citation only.
- **Closure.** "- **Fix:** scope.other_income's locator drops the Line 1b, 1c, 1d and 1h quotes and cites p. 25, Missing
  or Incorrect Form W-2?."
- **Due.**
  - transcription and render of scope (one more line);
  - the screen of scope.other_income, if its prompt carries the cited pages [I].

### BUG-0902 `scope.armed_forces`

- **Still real** [C xint questions.yaml:1792; scope.yaml:96].
- **Fix.**
  - Tick: "In the armed forces, Coast Guard, reserves or National Guard since 2022".
  - New help: "Count a spouse who has died if you moved in 2025 under military orders after the death."
  - The scope.yaml source and label add "(the Coast Guard included)".
- **Red team.**
  - A Yes only opens three questions (reservist expenses, military move, reservist repaid) and New York's active-duty
    question [C scope.yaml:120-199; ny_it201.yaml:69]. So a wrong Yes costs questions, not values.
  - Sources: Form 3903 and 10 U.S.C. 101 are not archived. The surviving-spouse rule and "Coast Guard" are [I/U].
- **Fixture.** Existing rows `scope.reservist_expenses` and `ny.active_duty`.
- **Closure.** "- **Fix:** scope.armed_forces names the Coast Guard (tick, source) and its help counts a deceased spouse
  for a move under orders after the death."
- **Due.**
  - question:scope.armed_forces;
  - gate:scope.armed_forces (federal, and the New York unit if units are shared [I]);
  - transcription and render of scope (one line).

### BUG-0903 `scope.household_pay` and `person.household_wages`

- **Still real** [C xint questions.yaml:1857; scope.yaml:463; person.yaml:1438].
- **Fix.**
  - Tick: "Pay from a household for home, garden or driving work, no W-2".
  - Help: "Such as a nanny, carer, cleaner, gardener or private driver, even in a home you share. …($2,800 sentence
    kept)".
  - The int-n10-ticks prompt becomes "…paid by a household, with no W-2, for work in or around its home or for its
    members?"
  - Sources and labels in scope.yaml and person.yaml: "as a household employee, for work in or around a household's
    home or for its members".
  - The person.household_wages help gains the same phrase.
- **Red team.**
  - **The contractor risk.** A freelance tutor or a cleaning business owner who works for a family could answer Yes. The
    pay then goes on line 1b as wages, so no SE tax. The current wording has the same risk, and the help still names
    only household-employee jobs.
  - The household-employee test (Pub. 926) is not archived [I].
  - I first drafted the tick "home or family work" and replaced it, because "family work" widened that risk.
  - Source: line 1b, "wages received as a household employee" [C scope.yaml:463 cite].
- **Fixture.** Existing rows `pay.household_wages` and `scope.pay_no_w2`.
- **Closure.** "- **Fix:** scope.household_pay (tick, help, prompt, source) and person.household_wages (source, help) ask
  about household-employee pay for work in or around a household's home or for its members, naming a gardener and a
  private driver and a home the worker shares."
- **Due.**
  - question:scope.household_pay and person.household_wages;
  - gate:scope.household_pay_if_pay (and gate:scope.pay_no_w2, whose unit holds household_pay);
  - transcription and render of scope and person.

### BUG-0909 `scope.religious_work`

- **Still real** [C xint questions.yaml:1967; scope.yaml:638].
- **Fix.**
  - Tick: "Pay for church work, or as clergy or religious order member".
  - Help adds "pay in housing or offerings, and fees from families for weddings or funerals".
  - Source and label: "or paid in any form (money, housing or offerings), by anyone, for work as clergy of any title …
    or as a member of a religious order".
- **Red team.**
  - A one-time officiant paid $200 may answer Yes. The next question (scope.clergy) refuses, so it over-refuses.
  - Sources: "minister, member of a religious order, or Christian Science practitioner" [C i1040sse.cols.txt:14]; "The
    rental value of a home or an allowance for a home furnished to you" [C :31].
- **Fixture.** Existing rows `scope.clergy`, `scope.church_employee` and `scope.chaplain_403b`.
- **Closure.** "- **Fix:** scope.religious_work (tick, help, source) names members of a religious order, pay in housing or
  offerings, and clergy paid by anyone."
- **Due.**
  - question:scope.religious_work;
  - gate:scope.religious_work (with clergy and church_exempt_wages);
  - transcription and render of scope.

### BUG-0910 `scope.rental`

- **Still real.** The tick is "Anything you own…" [C xint questions.yaml:1827]. The source already names a vehicle or
  equipment [C scope.yaml:393].
- **Fix.**
  - Tick: "Anything you own or lease rented or offered for rent, or royalties".
  - Help adds "so does a car or equipment, even one you lease and rent on to others".
  - Source and label: "anything you own or lease".
- **Red team.**
  - A Yes leads first to scope.rent_personal (seq 4), which refuses personal property, ahead of the rental list
    (seq 11) [C questions.yaml:6962-6970].
  - BUG-0713 (a personal-property rental not for profit is refused) is unchanged and still open.
  - Source: "Do not use Schedule E to report income and expenses from the rental of personal property, such as equipment
    or vehicles" [C i1040se.cols.txt:93].
- **Fixture.** Existing row `scope.equipment_rental`. Proposed row `scope.car_sublet`: copy it; situation "leases a
  car and rents it out on an app". Expected end: the same refusal [I].
- **Closure.** "- **Fix:** scope.rental (tick, help, source) asks about anything owned or leased, naming a leased car
  rented on to others."
- **Due.**
  - question:scope.rental;
  - gate:scope.rental (sche.any, rent_personal);
  - transcription and render of scope.
  - changes/2026/f8960.yaml quotes the old phrase in a `note:` only [C :147], so no 2026 operation breaks.

### BUG-0866 and BUG-0865 education and ABLE accounts (part)

- **Still real** [C xint questions.yaml:3408, 3417, 6486; person.yaml:7098].
- **Fix.**
  - (0866 item 1; and 0865's label half) The x_edu_account help gains "and for money put into a Coverdell for 2025 by
    April 15, 2026".
  - The x_edu_account label and source now match the asked question: "At any time in 2025, did you have … or was one
    held for you; or was money put into a Coverdell ESA for you for 2025 by April 15, 2026?"
  - (items 2 and 3) The x_edu_taxable help: "Costs also used for an education credit, or paid by a tax-free
    scholarship, do not count as costs it paid. A Coverdell left at age 30 or at death counts as paid out. A Yes ends
    the interview here."
- **Red team.**
  - A Yes at x_edu_account only opens x_edu_taxable and x_edu_excess, and New York's 529 count
    [C ny_it201.yaml:686]. A wrong Yes costs questions.
  - Sources:
    - Part V, "contributions to your Coverdell ESAs for 2025" [U entry];
    - the coordination with the credits and tax-free assistance [C p970.cols.txt:434-439];
    - "The balance … must generally be distributed within 30 days after … The beneficiary reaches age 30 … The
      beneficiary's death" [C p970.cols.txt:1318-1319]. "Counts as paid out" is [I] from that rule.
- **Not done:**
  - Item 4, the ABLE excess contributor.
  - Item 5, `person.sav_able`. `changes/2026/person.sav.yaml:147` holds a `set_question` whose `from:` is the current
    prompt, so changing the 2025 prompt makes that 2026 operation stale. It needs a matching edit to the 2026 file.
  - 0865's 18 locators per Part. It is citation only, and it would widen the person transcription by 18 lines.
- **Closure (0866).** "- **Fix (in part):** person.x_edu_account counts a Coverdell funded for 2025 by April 15, 2026
  (help, source); the person.x_edu_taxable help counts a balance left at 30 or death and excludes credit-used and
  scholarship-paid costs. The ABLE excess contributor and person.sav_able's tense stay open (the latter needs the
  changes/2026/person.sav.yaml set_question restated)."
- **Closure (0865).** "- **Fix (in part):** person.x_edu_account's label and source match the question asked. The
  per-Part locators of the person.x_* lines stay open."
- **Due.**
  - question:person.x_edu_account and x_edu_taxable;
  - gate:person.x_edu_account;
  - transcription and render of person (one line).

### BUG-0868 `person.eligible_educator`

- **Still real.** No help [C xint questions.yaml:4281].
- **Fix.** Help: "Count the hours of a whole school year that falls partly in 2025 (2024-25 or 2025-26), not only those
  in 2025, at every K-12 school you worked in."
- **Red team.**
  - Someone who worked 900 hours only in the 2023-24 year would answer No. That is right.
  - Source: "worked in a school for at least 900 hours during a school year" [C person.yaml:374 cite].
- **Fixture.** Existing row `saving.educator`.
- **Closure.** "- **Fix:** person.eligible_educator has help: hours of a school year partly in 2025, at every K-12
  school."
- **Due.** question:person.eligible_educator; gate:person.eligible_educator.

### BUG-0872 `person.died_at_64`

- **Still real.** The source is "Is this the final return of a person who died…" [C xint person.yaml:581]. No bank
  prompt, so the source is what is asked.
- **Fix.**
  - Source: "Did this person die in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th
    birthday.)"
  - Label: "Did this person die in 2025 before reaching age 65?"
- **Red team.** A surviving spouse now answers by the facts. Source: "born before January 2, 1961, but died in 2025
  before reaching age 65" [U entry, i1040gi p. 110].
- **Fixture.** None walks it with Yes. The `fixtures/2025/mutation.json:98364` evidence_note quotes the old wording.
  That is prose, not an asserted value; it can be restated or left.
- **Closure.** "- **Fix:** person.died_at_64 asks whether the person died in 2025 before reaching 65, not whether this
  is their final return (source, label)."
- **Due.**
  - question:person.died_at_64;
  - gate:person.turned_65_this_year;
  - transcription and render of person (one line).

## 2. Fixed in inc-m34-lows.patch

### BUG-0898 `f1040.withheld_other_any`

- **Still real.** Its help names K-1 and 1042-S only [C xint questions.yaml:620]. The source already names 8805 and
  8288-A [C f1040.yaml:878].
- **Fix.** Help: "Box 4 of a Form 1099 or W-2G, box 6 of an SSA-1099 or box 10 of an RRB-1099. Tax withheld on a Schedule
  K-1 or Form 1042-S, 8805 or 8288-A counts too, even with no money paid to you. If unsure, answer Yes."
- **Red team.**
  - None found.
  - Source: "Tax withheld that is shown on Form 1042-S, Form 8805, or Form 8288-A" [C i1040gi.cols.txt:898].
- **Fixture.** Existing rows `payments.withheld_on_1099`, `withheld_on_w2g` and `withheld_complete`.
- **Closure.** "- **Fix:** f1040.withheld_other_any help names Forms 8805 and 8288-A, even with no money paid."
- **Due.** question:f1040.withheld_other_any; gate:f1040.withheld_other_any. f1040.yaml is not edited.

### BUG-0908 `scope.recovery`

- **Still real.** Its help ties the standard-deduction test to 2024 [C xint questions.yaml:2000].
- **Fix.** Help (44 words): "Such as a refund of property tax, sales tax or mortgage interest (Form 1098 box 4), a medical
  bill repaid, or a deducted bad debt repaid. It is not income if it was deductible only by itemizing and you did not
  itemize that year."
- **Red team.**
  - A filer who itemized for 2023 now answers Yes, and rec.not_2024 refuses (existing row `s1o.rec_not_2024`).
  - The tick still says "(not state/local refund)", so I dropped the help's sentence on that refund.
  - The "rebate on a credited item" clause of the entry was left out for length (rare).
  - Source: "recoveries of nonitemized deductions (such as payments on previously deducted bad debts)"
    [C p525.cols.txt:819].
- **Fixture.** Existing rows `s1o.rec_not_2024`, `rec_nonitemized` and `rec_sales_tax`.
- **Closure.** "- **Fix:** scope.recovery help ties the itemizing test to the year of the deduction and names a repaid bad
  debt and a sales tax refund."
- **Due.** question:scope.recovery; gate:scope.recovery. This is a scope bank entry; scope.yaml is not edited.

### BUG-0821 `s2.lookback`

- **Still real** [C xint questions.yaml:1009; s2.yaml:1113].
- **Fix.**
  - Prompt: "…have a contract over more than one tax year, with its income reported as the work went on, that was
    finished, or whose price or costs changed, in 2025?"
  - The source and label add "or whose price or costs were adjusted in 2025 after it was finished".
- **Red team.**
  - A Yes refuses, so a wrong Yes is an over-refusal.
  - Source: "for the tax year the contract is completed or adjusted" [C i6251.cols.txt:173].
  - changes/2026/s2.yaml:84 sets only cite.locator. Not touched.
- **Fixture.** None.
- **Closure.** "- **Fix:** s2.lookback (prompt, source) asks also about a contract whose price or costs changed in 2025
  after it was finished."
- **Due.**
  - question:s2.lookback;
  - gate:s1.has_sc (the unit that found it);
  - transcription and render of s2 (one more line).

### BUG-0826 `s2.options_any`

- **Still real** [C xint questions.yaml:954; s2.yaml:19].
- **Fix.**
  - Tick: "Employee stock options used to buy shares, or such shares sold".
  - Prompt: "…use employee stock options to buy shares, or sell shares bought that way?"
  - Help: "Count options granted to an employee that you inherited or got in a divorce, and shares bought through an
    employee stock purchase plan. Shares simply granted to you, such as restricted stock, do not count."
  - Source and label: "exercise employee stock options, including options inherited or received in a divorce".
- **Red team.**
  - **I did not use the entry's "or a company you served".** A nonemployee director would then answer Yes and enter
    option income on line 8k, which the entry itself says is usually Schedule C income. That loses SE tax [I].
  - A buyer of listed call options now reads "employee" and answers No. That is right.
  - Source: "Enter any income from the exercise of stock options not otherwise reported" [C i1040gi.cols.txt:8638].
    The divorce and heir treatment is [I] (Rev. Rul. 2002-22 is not archived).
- **Fixture.** None (0 rows answer options_any Yes). Proposed row `other.options_inherited` needs the line 8k amount
  path [I, not designed].
- **Closure.** "- **Fix:** s2.options_any (tick, prompt, help, source) asks about employee stock options, counting ones
  inherited or received in a divorce. Nonemployee directors are not named (their option income is usually Schedule C
  income)."
- **Due.**
  - question:s2.options_any;
  - gate:s2.options_any (s1.stock_options_if_options, s2.iso_if_options);
  - transcription and render of s2.

### BUG-0680 `s2.hsa_testing`

- **Still real** [C xint questions.yaml:992].
- **Fix.** Help: "A full year's amount put in for 2024 needed the health plan kept through 2025; money moved from an IRA,
  through the 12th month after the move. Losing it by death or disability does not count. A Yes ends the interview
  here."
- **Red team.**
  - The prompt still speaks of putting in more than the months allowed, and does not name an IRA transfer. Someone with
    only a 2024 IRA transfer who lost coverage in 2025 may still answer No: an under-refusal, and the case before the
    fix too. A tick or prompt change would be needed; I left it for the Schedule 2 lane.
  - Sources: "The testing period begins with the last month of your tax year and ends on the last day of the 12th month
    following that month", "other than because of death or becoming disabled" [C i8889.cols.txt:38]; the IRA
    transfer's period "lasts through the last day of the 12th month following that month" [C i8889.cols.txt, the
    paragraph after line 202].
- **Fixture.** Existing row `hsa.testing_period_no_account_left`.
- **Closure.** "- **Fix:** s2.hsa_testing help states each testing period and that losing coverage by death or disability
  does not count."
- **Due.** question:s2.hsa_testing.

### BUG-0916 `f8853c.line22`

- **Still real.** The source drops "curing", "mitigating" and "required to treat a chronically ill individual"
  [C xint f8853c.yaml:341].
- **Fix.** The source per the entry, verbatim (see the patch).
- **Red team.**
  - The asked prompt is the bank's "What did this person's long-term care cost during those days?" It does not narrow,
    so this fixes the line's own text.
  - Source: i8853 p. 9, quoted in the line's cite [C f8853c.yaml:349-351].
- **Fixture.** Existing row `s1o.ltc_per_diem`.
- **Closure.** "- **Fix:** f8853c.line22's source states the whole i8853 definition of qualified long-term care services."
- **Due.**
  - question:f8853c.line22;
  - transcription and render of f8853c (one more line);
  - the f8853c completeness subject, which v2 does not change (its source is in the completeness prompt) [I].
  - gate:f8853c.has_periodic is already due from v2.

### BUG-0917 `f8853c.line25`

- **Still real.** subtract_floor0 with no ambiguity [C xint f8853c.yaml:478].
- **Fix.** A new register entry `amb.2025.f8853c_line25_floor` (chosen: floored; reason as in the patch), and
  `ambiguity:` on f8853c.line25.
- **Red team.**
  - None (no wording).
  - Source: Form 8853 lines 25 and 26 [C f8853.cols.txt:103]. That the statute floors it ("excess (if any)") is [I]:
    the IRC is not archived.
- **Fixture.** None. No value changes.
- **Closure.** "- **Fix:** the zero floor on f8853c.line25 is recorded as amb.2025.f8853c_line25_floor and cited from the
  line."
- **Due.**
  - transcription and render of f8853c (line 25);
  - question:f8853c.line24, already due from v2 (line 25 is its reader).
- **This is the one low that adds no new subject.**

### BUG-0923 `s1.ltc_payout` and `f8853c.line17`

- **Still real** [C xint questions.yaml:3886, 4188].
- **Fix.**
  - The s1.ltc_payout help adds "Count payments the policy sent straight to a nursing home or care agency."
  - The f8853c.line17 help adds "including payments sent straight to a care provider".
- **Red team.**
  - None found.
  - Source: "The policyholder is required to report the income, even if payment is assigned to a third party or
    parties" [C i8853.cols.txt:221].
- **Fixture.** Existing rows `other.ltc_payout` and `s1o.ltc_per_diem`.
- **Closure.** "- **Fix:** the helps of s1.ltc_payout and f8853c.line17 count per diem payments sent straight to a care
  provider."
- **Due.**
  - question:s1.ltc_payout and f8853c.line17;
  - gate:s1.ltc_payout [I];
  - gate:f8853c.periodic is already due from v2.

## 3. Reviews made due, beyond v2

- **Per form: none new.**
  - Line-scoped transcription and render take in more lines:
    - scope: other_income, armed_forces, household_pay, religious_work, rental;
    - person: household_wages, x_edu_account, died_at_64;
    - s1: nol_was_joint, nol_not_married;
    - s2: lookback, options_any;
    - f8853c: line22, line25.
  - No class M: no expression changed.
  - Completeness subjects change for scope, person, s1 and s2 (v2 already changes their sources) and for **f8853c**
    (new; line 22's source) [I: the completeness prompt lists each input's source].
- **Question reviews (about 31 new subjects).**
  - s1: gambling_pro, alimony_any, alimony_received, alimony_paid, uc_any, alaska_any, inmate_wages, jury_any,
    scholarship_any, nol_not_married, nol_was_joint, ltc_payout;
  - oi8z.amount; f4137row.col_c;
  - scope: armed_forces, household_pay, religious_work, rental, recovery;
  - person: household_wages, x_edu_account, x_edu_taxable, eligible_educator, died_at_64;
  - f1040.withheld_other_any;
  - s2: lookback, options_any, hsa_testing;
  - f8853c: line17, line22.
- **Gate units (screen and false-no; about 20 new).**
  - s1: has_gambling, alimony_any, uc_any, alaska_any, inmate_wages, jury_any, scholarship_any, nol_joint,
    nol_separate, ltc_payout;
  - scope: armed_forces, household_pay_if_pay / pay_no_w2, religious_work, rental, recovery;
  - person: x_edu_account, eligible_educator, turned_65_this_year;
  - f1040.withheld_other_any; s2.options_any; s1.has_sc.
  - Gate units the v2 patches already make due are not counted.
- **Generated files to regenerate:** `rendered/2025/{scope,person,s1,s2,f8853c}.md` (the build); the coverage report
  (`interview-coverage --write`, since question wording a row meets changed); `reports/2025/stage*.txt`, which quote
  the old labels.

## 4. Deferred (their fix would make a new per-form review or a model change due, or belongs to another lane)

| Entry | Why deferred |
|---|---|
| BUG-0719 | The separate 457(b) limit has no archived source. i1040gi says "under all plans" and only "a higher limit may also apply" [C i1040gi.cols.txt:505]. Archive Pub. 575 or 4484 first. Over-refusal only. |
| BUG-0795 | A new scope input and refusal: a model change, so class M of scope. Upgrade candidate; its own lane. |
| BUG-0828 | The help-only option refuses every section 6013(g) couple (a large over-refusal) to fix a NIIT case above the threshold. The right fix is an f8960 question, and f8960 is not a v2 form. |
| BUG-0570 | The line 35a and 36 bound is an f1040.yaml model change, and v2 m34 edits only the f1040 bank. The line 3a part is int-amt's. |
| BUG-0895 | Its limb belongs in the refund.exc_who source (refund.yaml), which v2 does not change, so the refund transcription would be due. A bank-only change would leave the refusal wider than its line. |
| BUG-0764 | An s2.amt_l7 expression change (class M of s2), a fixture with a hand-computed Part III, and two mutants to kill: the mutation lane's work. |
| BUG-0765 | The remedy text in f1040.yaml and the expected refusal text of a household.json fixture. |
| BUG-0867 | Mostly dependent.age (dependent.yaml, older-credits' file). The person.age50/55/simple helps can ride with it. |
| BUG-0869 | Already in v3 `older-credits-lows.patch` (person.edu_over and dependent.edu_over). |
| BUG-0866 items 4 and 5 | Item 5 needs `changes/2026/person.sav.yaml:147` restated with the 2025 prompt. Item 4 needs a new sentence of uncertain place. |
| BUG-0713 | M: coverage intake (its own disposition). Untouched beside 0910. |

## 5. Closures with no new text

- **BUG-0893 (obsolete).** "- **Disposition:** superseded: s1.line8u and s1.inmate_amount were removed with BUG-0766,
  and s1.inmate_wages now refuses, so W-2 inmate wages are no longer counted twice. Computing line 8u waits on T-336."
  Evidence: [C xint forms/2025/s1.yaml, 0 matches for s1.line8u and s1.inmate_amount; questions.yaml:3798 help "A Yes
  ends the interview here"].
- **BUG-0894.** "- **Fix:** the f1040.line26 help says how to enter joint estimated payments on a separate return (an
  agreed split, otherwise in proportion to the separate taxes), with BUG-0897 (inc-m34)." Evidence: [C v2
  inc-m34.patch, f1040.line26 hunk].

## 6. What to run (when the machine is free)

- Apply in order: int-n10-ticks, v2 inc-m12, v2 inc-m34, then these two add-ons.
- Then: build; `test-fixtures` (no expected value should move); `interview-coverage`, then `--write`; `tick-groups`
  (every tick is 12 words or fewer [C, counted]); `draft-walk`.
- Check that `tools/check_all.sh` reports no stale 2026 operation. The only 2026 lines near these edits set
  cite.locator [C changes/2026/s2.yaml:74-92].

## 7. Not done, and limits

- No walk, build or review was run. Every misreading named is my judgment.
- The proposed coverage rows are sketches. Each copies an existing row's answers and expects the same end [I]. None is
  in the patch.
- The gate-unit list in section 3 comes from `gated_by` and `_if_` gate lines in xint, and from each entry's "Caught by"
  units. It was not computed with `tools/transcription/gates.py`.
- N10 overruns, each against a current text that is also long: scope.recovery help 44 words; f1040.withheld_other_any
  help 44; s2.hsa_testing help 42; s1.alimony_paid help 41.
- Scratch: `scratch/round4-lows-inc/` holds `edit_m12.py` and `edit_m34.py`, which produce the add-ons from the v2
  trees, and the test trees.
