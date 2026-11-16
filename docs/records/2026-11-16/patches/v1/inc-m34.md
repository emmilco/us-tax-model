# Patch inc-m34: lanes M3 (div, f4952) and M4 (f1040 bank, s2, rec/refund, f8853c) of plan med-income

Lane patch-inc-m34. Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Patch:
`/tmp/nightplan/patches/inc-m34.patch` (9 files, 18 hunks). It was made from copies in
`/tmp/nightplan/scratch/inc-m34/{a,b}`. Nothing in xint was written. `git apply --check` of the patch against xint
passed; that check reads only and writes nothing.

## Summary

- **Entries covered:** BUG-0830 and BUG-0833 (M3); BUG-0897 with BUG-0894, BUG-0899, BUG-0900, BUG-0901 and BUG-0873
  (M4). BUG-0907 is left out, as the brief says.
- **Files:** `interview/2025/questions.yaml` (15 bank entries); `forms/2025/f4952.yaml` (f4952.carryover and
  f4952.prior_7); `forms/2025/s2.yaml` (s2.amt_boat); `ambiguities/2025.yaml` (2 new entries); 5 coverage files
  (11 new rows). f1040.yaml, rec.yaml, refund.yaml, div.yaml and f8853c.yaml are unchanged.
- **Checks run (all read-only):** every edited YAML file parses (PyYAML), and `git apply --check` passes against xint.
  **Not run:** the build, fixtures, interview-coverage, draft-walk and tick-groups. COMMON forbids them tonight. Every
  coverage row below is therefore **unverified**.
- **Where I departed from the plan's wording** (each is flagged below):
  1. The f1040.estimated_any help puts the plan's two sentences into one 36-word sentence, because together they
     came to 48 words, over N10.
  2. I drafted the BUG-0894 split rule for the f1040.line26 help myself. The plan gives the trigger for it but no
     wording.
  3. The f4952.prior_7 form source and label now match the new help. This is a sibling the plan did not list.
  4. The f8853c.line24 help now matches the new prompt. This is also a sibling the plan did not list.
  5. Coverage row ids use each file's prefix (`dividends.`, `sales.`, `payments.`, `other.`, `s1o.`), not the
     plan's names.
- **Owner decisions this patch drafts the plan's recommended option for:** 2 (0900, the transient reading), 3 (0873,
  Medicaid or VA paid to the provider), 4 (0897/0894, counting joint payments with the split rule) and 5 (0833, the
  latest-Form-4952 carryforward). **0833 has a wrong-value hazard that the plan did not name** (see M3, 0833). The
  owner should read it before the patch lands.

## Hunks, by entry

### M3. BUG-0830: div.other_boxes help (bank only)

- The old help "If you have no Form 1099-DIV, answer No." is replaced with the plan's text, 42 words: "...Count your
  share of a form in another's name, and a payment with no form, such as a return of capital or a payout when a
  company closed."
- The div.yaml source (the prompt, "Look at your ... Forms 1099-DIV") is kept, as the plan says.
- **Not taken: the plan's optional "a corporation or fund".** It would guard against a partner reading "a payment
  with no form" as a K-1 distribution. Adding it brings the help to 44 words. Integrator's choice.
- Source basis: f1099div box 3 and the Nominees paragraph (plan, checked there; I did not re-read them).

### M3. BUG-0833: f4952.line1 prompt, f4952.carryover prompt, f4952.prior_7 help; f4952.yaml carryover and prior_7

- **Bank.** All three are the plan's wording, verbatim:
  - line1 prompt (38 words): "Leave out interest on money used to buy, build or improve your home ..."
  - carryover prompt (31 words): "... from before 2025 that could not be deducted and is still unused (line 7 of the
    latest Form 4952)?"
  - prior_7 help (36 words).
- **Form, f4952.carryover.** The label and source now say "from before 2025 ... disallowed and not yet deducted ...
  line 7 of the latest Form 4952". The cite adds the Who Must File quotation. The line gets
  `ambiguity: amb.2025.f4952_latest_carryover`.
- **Form, f4952.prior_7 (beyond the plan; can be dropped).** The label and source add "or of the latest Form 4952
  filed if none was filed for 2024 because the standard deduction was taken". Without this, the source contradicts
  the new help, which a transcription review would flag. The form's own preamble already uses this wording
  (f4952.yaml:21 and :30, "line 7 of a 2024 Form 4952, or of the latest Form 4952 filed") [checked]. So this hunk
  brings the line into line with text the form already has.
- **Ambiguity entry `amb.2025.f4952_latest_carryover`** (new; chosen: the first reading; status: for the owner).
- **Hazard the plan did not name [inferred; owner decision 5].** Pub. 550, Limit on Deduction, says carried interest
  "is treated as investment interest paid or accrued in that next year" (sources/2025/p550.cols.txt:1471
  [checked]). So the 2023 carryforward was treated as paid in 2024. If the 2024 net investment income could have
  absorbed it, a correct 2024 Form 4952 would show a smaller line 7 than the 2023 one, even though the deduction
  was not taken because of the standard deduction. On that reading, "line 7 of the latest one filed" overstates
  line 2. The archived sources do not settle it. I recorded it as the second reading in the ambiguity entry.
  - The alternative wording is the entry's own fix (2): "the amount a correct 2024 Form 4952 would have shown".
  - It is right under either reading, but it is harder to answer.
  - Recommendation: the owner chooses between them before landing.
- **Siblings left unchanged** (helper or gate labels; a change would make more lines due for review):
  - f4952.carryover_if_interest label (f4952.yaml:114, "disallowed in 2024 and carried forward");
  - f4952.unsupported ("any of your 2024 carryforward", :168);
  - the filing-condition label at :618.
  - These are cosmetic. Fold them in at the next real f4952 change.

### M4. BUG-0897 with BUG-0894: f1040.estimated_any (tick, prompt, help) and f1040.line26 (prompt, help); bank only

- **Tick** (9 words, verbatim): "Estimated tax payments, or an overpayment applied to 2025".
- **Prompt** (25 words, verbatim).
- **Help** (36 words; **my condensation**): "Count payments by mail, online or card, including the one due in January 2026; an
  overpayment from your 2024 return or an amended return applied to 2025; and joint payments with a spouse or
  former spouse."
  - The verbatim alternative is the plan's 31-word help plus "Count joint payments made with a spouse or former
    spouse; the next question says what share to enter." That is 48 words in all.
  - The old guard "they are not tax taken out of your pay" is dropped, as in the plan. The heading of group
    paid_already ("Besides tax taken out of wages, ...", questions.yaml:67 [checked]) still carries that guard.
- **f1040.line26 prompt.** "counting any 2024 refund applied" becomes "counting any overpayment applied" (the
  plan's sibling).
- **f1040.line26 help (BUG-0894; my wording; owner decision 4, the plan's count-and-split option)**, 43 words: "On a
  joint return, add what each of you paid. For joint payments made with a spouse or former spouse whose return is
  separate from yours, enter your share: any split you both agree on, otherwise in proportion to your separate 2025
  taxes."
  - The separate-return rule is from i1040gi p. 39 (i1040gi.cols.txt:902 [checked]).
  - **The former-spouse half is unverified.** i1040gi says only to enter the former spouse's SSN. I am relying on
    my memory of Pub. 505 chapter 3, "Divorced Taxpayers", which uses the same agree-or-proportion rule. The
    archived p505 is the 2026 edition, and its text has no "former spouse" or "divorced" section (grep [checked]).
  - If that rule cannot be confirmed, the alternative is to drop "or former spouse" from both helps and leave the
    divorced case to the refusal-free status quo.
- **No form change.** The f1040.yaml source of estimated_any still says "an amount from your ... 2024 return applied
  to 2025" (f1040.yaml:992 [checked]). The bank prompt now overrides it, and the source does not mention the
  amended return. The plan keeps f1040.yaml unchanged. Align the source at the next f1040 change if the
  transcription review flags it.
- NY sibling, for the NY lane only: ny_it201 "had a 2024 refund applied" (the plan cites forms/ny/2025/ny_it201.yaml:2391).

### M4. BUG-0899: rec.two_returns help, refund.itemized help (bank only)

- Both are the plan's verbatim text (40 and 39 words).
- refund.itemized serves both the refund path and the rec path (rec.path reads refund.itemized, rec.yaml:208-225
  [checked]). Its new help has to suit both paths, and it does: "answer for the return of the one who got the
  money back".
- The help loses the clause "for 2024 deductions you could take only by itemizing". This follows the plan; no
  value depends on it.

### M4. BUG-0900: s2.amt_boat prompt and help; s2.yaml amt_boat label, source and cite

- **Bank:** the plan's verbatim prompt (36 words) and help (39 words).
- **Form.** The label and source now name "a house, apartment, condominium or mobile home used on a transient basis
  (rented out for short stays)" and "not your main home for all of 2025". The cite adds the i6251 sentence on
  qualified dwellings (i6251.cols.txt:218 [checked]). The line gets `ambiguity: amb.2025.amt_transient`.
- **Ambiguity entry `amb.2025.amt_transient`** (new; for the owner, decision 2).
- **Siblings left unchanged:** the gate labels s2.amt_could (s2.yaml:875, "boat or camper mortgage interest"),
  s2.amt_boat_if_could (:909) and the label of the AMT refusal line (:948). These are derived labels, and changing
  them makes three more lines due for review. Recommended for the same round if s2 render is being run anyway.

### M4. BUG-0901: s2.household_help tick and help (bank only)

- **Tick** (11 words) and **help** (39 words) are the plan's text, verbatim. The prompt and the s2.yaml source are
  unchanged.
- **Source check, using the coordinator's fetched sources** (`/tmp/nightplan/sources/`, **not yet archived** in
  sources/2025; the README there gives the steps):
  - Drivers: i1040sh p. 2 lists "Drivers" among the examples of household workers (i1040sh.txt:82 [checked]). The
    source's wording "work done in or around your home" is the IRS's own definition (i1040sh.txt:78), so the
    unchanged prompt agrees with the source.
  - Agency or registry: "it doesn't matter ... that you hired the worker through an agency or from a list provided
    by an agency or association" (i1040sh.txt:89-91 [checked]).
  - A company that directs its own staff: "Workers you get from an agency aren't your employees if the agency is
    responsible for who does the work and how it is done" (:107-110 [checked]).
  - Payroll service: the employer remains responsible when a third-party payer is used (:86-96 [checked]).
  - Pay in 2025 for 2024 work: the $2,800 test "applies to cash wages paid in 2025 regardless of when the wages were
    earned" (:299-301 [checked]).
- **Residual.** A Form 2678 (section 3504) agent or a government program that files for the filer means no Schedule
  H (i1040sh p. 2). Such a filer now answers Yes and is refused at s2.household_employee. That loses the case but
  gives no wrong value.
- **Dependency.** Archive i1040sh and p926 (2025 edition, the irs-prior URL) before landing, so that the cites
  resolve.

### M4. BUG-0873: f8853c periodic, others_paid, line24, contract_before_ltc_date (bank only)

- All four prompts and the pre-1996 help are the plan's text, verbatim.
- **Extra sibling (can be dropped):** the line24 help "payments that repaid those costs" becomes "payments for those
  costs, received or still due". Otherwise the help would contradict the widened prompt.
- **Owner decision 3 (Medicaid or the VA) is only partly held open.** The plan names neither. But "paid by
  insurance or anyone else ... straight to the care provider" literally includes Medicaid or the VA paying the
  nursing home. So a filer in that case is now likely to count it on line 24, which lowers line 26.
  - If the owner rules that these are not line 24 reimbursements, add to the help: "Leave out Medicaid and VA
    benefits."
  - i8853 line 24 ("through insurance or otherwise", i8853.cols.txt:275 [checked]) reads as including them, so I
    left the text as drafted [inferred].
- The pre-1996 widening ("even if it was later exchanged or changed") only widens a refusal (i8853.cols.txt:277
  [checked]).
- No form change: the f8853c.yaml sources already say "received or expect to receive" and "per day, week or month"
  [checked].
- f8853c is new tonight. Fold this in before its first question review runs.

## Coverage rows added (all unverified; none was walked)

Hand predictions: each row's expected end is the value the row itself gives (the `proceeds` form), or a refusal
reached on the row's own Yes. Where a row copies the answers of an existing passing row, the path is that row's.

| Row | File | Copied from | Expected end | Risk |
|---|---|---|---|---|
| dividends.return_of_capital_no_form | investments_foreign.yaml | dividends.return_of_capital_over_basis | refused div.unsupported | low (same answers) |
| sales.interest_home_equity_for_stocks | sales.yaml | sales.interest_election_too_large, with line4g 0 | proceeds f4952.line1 = 50000 | **medium**: a line4g of 0 may open or skip questions I could not see without a walk |
| sales.interest_carry_from_2023 | sales.yaml | as above, plus carryover true and prior_7 80000 | proceeds f4952.prior_7 = 80000 | **medium**: the carryover path is not covered by any existing row |
| payments.estimated_amended_overpayment | household_payments.yaml | payments.estimated_complete | proceeds f1040.line26 = 120000 | low |
| payments.estimated_january_2026 | household_payments.yaml | payments.estimated_complete | proceeds f1040.line26 = 150000 | low |
| other.household_nanny_payroll_service | other.yaml | other.household_employee | refused s2.other | low |
| other.household_private_driver | other.yaml | other.household_employee | refused s2.other | low |
| s1o.ltc_reimbursed_to_provider | s1_other.yaml | s1o.ltc_per_diem, with line24 3000000 and contract_before_ltc_date false | proceeds f8853c[mom].line24 = 3000000 | **medium**: no existing row has line24 > 0, so contract_before_ltc_date is asked for the first time |
| s1o.ltc_others_accelerated | s1_other.yaml | s1o.ltc_others_paid | refused f8853c[mom].others_paid_if_periodic | low |
| s1o.ltc_weekly_per_diem | s1_other.yaml | s1o.ltc_per_diem ($3,080 a week × 365/7 = $160,600) | proceeds f8853c[mom].line17 = 16060000 | low |

**Not drafted; each needs a walk to get its answers right:**

- the plan's `div.nominee_share_2b`: box 2b sits behind sub-gates such as div.capital_gain_boxes, which I did not
  trace;
- `rec.spouse_only_itemized_separately` and `rec.cross_state_refund_and_other`: no existing row walks a joint rec
  path to copy;
- `amt.condo_short_stay`: no existing row reaches s2.amt_boat, which needs s2.amt_could true;
- a joint-estimated-payment row on a separate return.

No fixture input or expected value changes. These are wording changes only, plus labels and sources on three form
lines.

## To run to verify (in the lane's worktree, after applying)

1. Build, then `tools/check_all.sh`. The relevant steps are the build's wording, gate and schema checks; the
   fixtures; `interview_coverage`; and `tick_groups`.
2. `node engine/dist/main.js interview-coverage` for the rows above, then `--write`. The report quotes the reworded
   questions, so it must be rewritten.
3. `node engine/dist/main.js tick-groups` (labels changed in groups paid_already and care_help) and
   `node engine/dist/main.js draft-walk`. Expect no change in steps. Words change slightly.
4. `node engine/dist/main.js render --check`. The f4952 and s2 labels changed.
5. `tools/siblings.py` on f4952.carryover, s2.amt_boat and f1040.estimated_any. I did not run it.

## Reviews made due (one per form per round, after all of that form's fixes)

- **Transcription and render, line-scoped:**
  - f4952: carryover, and prior_7 if that hunk is kept;
  - s2: amt_boat.
- **Question, screen and false-no reviews:**
  - gate:div.other_boxes_if_dividends;
  - gate:f4952.has_interest and gate:f4952.carryover_if_interest;
  - gate:f1040.estimated_any, plus the question review of f1040.line26;
  - gate:rec.two_returns_if_joint and rec.path, plus the question review of refund.itemized;
  - gate:s2.amt_boat_ask;
  - gate:s2.household_help;
  - gate:f8853c.has_periodic, has_line24 and periodic.
- That is about 12 gate subjects for the release samples, which are paid. Estimate first; runs above $3.00 need
  `--approve-cost`.

## Bug-inventory notes (for the integrator; no new entries proposed)

- BUG-0894 is fixed together with BUG-0897 by this patch, under owner decision 4.
- The f4952 standard-deduction-year hazard is recorded as an ambiguity reading, not as a bug. If the owner takes
  the second reading, the f4952.prior_7 help and source change again.

## Owner decisions this patch assumes (recommended option drafted)

1. **0833 (decision 5):** use line 7 of the latest Form 4952 when no 2024 form was filed. **There is a new hazard
   (see above).** The alternative is "the amount a correct 2024 Form 4952 would have shown".
2. **0897/0894 (decision 4):** count joint payments with a spouse or former spouse, with the split rule in the line
   26 help. The former-spouse split rests on Pub. 505 (2025) chapter 3, which is not archived.
3. **0900 (decision 2):** "used on a transient basis" is read as "rented out for short stays". Only a refusal
   depends on it.
4. **0873 (decision 3):** Medicaid and the VA are not named. The drafted prompt nevertheless reads as including
   them.
5. **0901:** the sources are fetched but not archived. Archive them before landing.
