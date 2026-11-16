# v2 of patches inc-m34 and inc-m12 (lane v2-income)

claude-opus-5-5, judgment, year 2025, jurisdiction us. Read only: nothing in xint was written.
**[C path:line]** = checked against that file in this session. **[I]** = inference.
Word counts are whitespace splits of the parsed YAML text.

## Summary

- **Four patches** are in `/tmp/nightplan/patches/v2/`:
  - `inc-m34.patch`: 10 files (round 2 had 9; `forms/2025/f8853c.yaml` is new).
  - `inc-m12.base.patch`: 8 files.
  - `inc-m12.cod.patch`: 11 files. It is byte-identical to round 2, because no finding touches 0810.
  - `inc-m12.patch`: 16 files. It equals base plus cod.
- **How they were made.** Each patch comes from scratch copies of xint under `/tmp/nightplan/scratch/inc-v2/`. The
  round-2 patch was applied to the copies with `patch -p1`, then the edits were made by
  `scratch/inc-v2/edit_m34.py` and `edit_m12.py`, and the patches were produced by `git diff --no-index`.
- **Checks run** (read-only; none of them is a build or engine run):
  - All four pass `git apply --check` against xint.
  - Applying base and then cod with `patch` gives a tree identical to the combined patch (`diff -r`).
  - Every edited YAML file parses.
  - `int-n10-ticks.patch`, then v2 `inc-m12.patch`, then v2 `inc-m34.patch` apply in that order on scratch copies
    with no fuzz. This bears on red-team B4 (see below).
- **Wrong-value findings applied:**
  - A5 (0873, line 24);
  - A6 (0833, "latest Form 4952", reverted);
  - A9 (0806, tipped jobs);
  - A10 (0896, the printed digital-asset answer);
  - A13 (0904, the Medicaid help);
  - A14 (0808, the gambling help);
  - A3 (0907, now in m12; see below).
- **Lower-severity findings applied:** C1 (0897 help), C3 (0899 help) and D (the 0830 help cut to 40 words).
- **Where I departed from the red team's text, decided on the source text:**
  - A5: I kept i8853's "or otherwise", which the red team's prompt drops.
  - A9: I kept barbers, who are on the Treasury list.
  - A10: I added mining to the help.
  - C1: I kept the joint-payment clause that m34 added for BUG-0894.
- **Re-derivation.** I re-derived all 23 coverage rows from the form expressions, the walked paths in
  `reports/2025/interview_coverage.md` and the params. I found **no value that differs** from the patch
  predictions. One row changes because A6 removed its premise: `sales.interest_carry_from_2023` is now
  `sales.interest_carry_from_2024`, with the same answers and the same end.
- **For the coordinator:**
  1. Remove BUG-0907 from k1sche lane A, as A3 requires.
  2. B2 (the `scope.contractor_pay` prompt) belongs in `int-n10-ticks.patch`, not here.
  3. Two new ambiguity entries are for the owner.

## Changes from round 2, by finding

### inc-m34

**A6, BUG-0833 (f4952.carryover and prior_7): "latest Form 4952" reverted.**

- **Source.**
  - Form 4952 line 2: "Disallowed investment interest expense from 2024 Form 4952, line 7" [C sources/2025/f4952.cols.txt:10].
  - Pub. 550: "You can carry over the amount of investment interest you could not deduct because of this limit to the
    next tax year. The interest carried over is treated as investment interest paid or accrued in that next year"
    [C sources/2025/p550.cols.txt:1471, p. 46].
- **Why the round-2 wording is wrong.** An older carryforward becomes 2024 investment interest. Only the part that
  2024 net investment income could not absorb carries on. So "line 7 of the latest one filed" can overstate line 2.
  The red team is right, and the round-2 lane had itself flagged this hazard.
- **What v2 does (red team option (b)).**
  - The `f4952.carryover` prompt and the `f4952.prior_7` help are back to their xint text.
  - The round-2 label, source and cite edits to both lines in `f4952.yaml` are dropped.
  - `f4952.carryover` now carries only `ambiguity: amb.2025.f4952_no_2024_form`.
  - The `f4952.line1` rewrite stays; the red team found it sound (E).
- **New register entry `amb.2025.f4952_no_2024_form`.** It replaces `amb.2025.f4952_latest_carryover`.
  - It has three readings: ask about a 2024 form only; what a 2024 form would have shown; the latest form filed.
  - Chosen: the first (the current wording), until the owner rules on red team option (a), a refusing child.
  - Reason: the first can only understate the deduction. The third can overstate it.
- **Option (a), not in the patch (a model change; owner).** A refusing child, `f4952.carry_no_2024_form`: "Was
  investment interest carried into 2024 from an earlier year, with no Form 4952 filed for 2024?". Its help would be
  "A Yes ends the interview here."
- **Sibling left unchanged, flag for the next f4952 change.** The `f4952.has_interest` label and source still say
  "(line 7 of a 2024 Form 4952, or of the latest Form 4952 filed)" [C forms/2025/f4952.yaml:21,30]. It only gates,
  and a Yes there followed by No at `carryover` gives line 2 = 0, so no value depends on it. A transcription review
  may still flag the mismatch.

**A5, BUG-0873 (f8853c.line24): prompt and help.**

- **Source.** "Enter the reimbursements you received or expect to receive through insurance or otherwise"
  [C sources/2025/i8853.cols.txt:275]. The form line's own source already says "through insurance or otherwise"
  [C forms/2025/f8853c.yaml:398-400].
- **The red team's prompt** ("paid back by insurance") drops "otherwise". That would leave out a true non-insurance
  reimbursement, which lowers line 24 and understates line 26 [I]. So I kept the source's words. I used
  "reimbursed", which is also the word box 3 of Form 1099-LTC uses ("Reimbursed amount"; the periodic help quotes
  it).
- **Prompt (31 words):** "How much of those care costs was, or will be, reimbursed by insurance or otherwise, to you
  or straight to the care provider? Leave out the payments at a set rate."
- **Help (34 words):** "Count insurance or other reimbursements of those costs, received or still due, not the payments
  at a set rate. Money family or friends gave toward the care is not counted. Give 0 if none."
- **The family-or-friends exclusion is [I].** A gift is not a reimbursement of the filer's costs; i8853 does not
  say this.
- **Owner decision 3 (Medicaid or the VA).** It is recorded as the new register entry
  `amb.2025.f8853c_line24_public`, linked from `f8853c.line24`. That link is the one f8853c.yaml change.
  - Chosen: the first reading (they count, as worded), for the owner.
  - The red team and the plan both called for an ambiguity entry. Round 2 had none.

**C1, BUG-0897 (f1040.estimated_any help).**

- **Help (44 words):** "Payments you sent the IRS for 2025, including the one due in January 2026 but not one in
  January 2025 for 2024; joint payments a spouse or former spouse sent; and an overpayment from your 2024 return or
  an amended return applied to 2025."
- **Source.** "Enter any estimated federal income tax payments you made for 2025. Include any overpayment that you
  applied to your 2025 estimated tax from your 2024 return or an amended return" [C i1040gi.cols.txt:900-901].
- **Why the joint clause stays.** It comes from round 2's BUG-0894 pairing. The red team's 38-word text predates
  that pairing. The `f1040.line26` split help (round 2) is unchanged.
- **Over N10 by about 4 words.** That is the price of the joint clause.
- **The former-spouse split remains [I].** i1040gi gives the agree-or-proportion rule for "you and your spouse paid
  joint estimated tax but are now filing separate". For divorced filers it says only to enter the former spouse's
  SSN [C i1040gi.cols.txt:902].

**Smaller changes.**

- **C3, BUG-0899 (rec.two_returns help).** "A state income tax refund counts." becomes "Count a state income tax
  refund as money back." (43 words.)
- **D, BUG-0830 (div.other_boxes help).** "Most forms show amounts only in boxes" becomes "Most forms use only boxes", so
  the help is now 40 words.

**Coverage, A6.** Row `sales.interest_carry_from_2023` described the no-2024-form case, which the chosen reading now
answers No. It becomes `sales.interest_carry_from_2024`: "A person whose 2024 Form 4952 shows $800 on line 7 paid
$500 of margin interest in 2025." The answers and the end are unchanged. It is still the only row that walks
`carryover` = Yes.

**Unchanged from round 2 (the red team found them sound or did not touch them):** 0900 (s2.amt_boat and
`amb.2025.amt_transient`), 0901, the 0873 periodic, others_paid and pre-1996 text, the 0897 tick and prompt, the
f1040.line26 prompt and help, and refund.itemized.

### inc-m12 (base, and so the combined patch)

**A9, BUG-0806 (tipjob.yaml tipjob.listed source, 41 words).**

- **New text:** "Did you get any of these tips for work on the IRS list of jobs that customarily get tips? Servers,
  bartenders, cooks, hotel housekeepers and desk clerks, hairdressers and barbers, and taxi and delivery drivers are
  on it; managers are not."
- **Each job named is on the list:**
  - bartenders, wait staff and cooks [C sources/2025/tipped-occupations.txt:245, 246, 249];
  - hotel desk clerks and maids [C :272-273];
  - barbers and hairdressers [C :301];
  - taxi drivers and goods delivery people [C :321, 323].
- **Barbers.** The red team dropped them. I kept them, because TTOC 603 lists them and the current text names them.
- **Residual [I].** "Managers are not" could make an executive chef, who is listed under 105, or a maître d', who is
  listed under 109, doubt the answer. Neither is called a manager, so I kept the red team's clause.

**A10, BUG-0896 (f1040.digital_assets prompt and help, bank only).**

- **Prompt (30 words, the red team's verbatim):** "In 2025, did you (or, on a joint return, your spouse) get crypto or
  another digital asset as pay or a reward, or sell, trade, spend or give any away?"
- **Help (42 words):** "Yes: paid in crypto, staking or mining rewards, new coins from a fork or airdrop, or selling,
  swapping, spending or giving it away. No: buying it with dollars, holding it, getting it as a gift, or moving it
  between your own wallets."
- **Source.** "(a) received (as a reward, award, or payment for property or services); or (b) sold, exchanged, or
  otherwise disposed of", and the example list "mining, staking, and similar activities" [C i1040gi.cols.txt:291,
  295]. That list is why I added "mining" to the red team's help.
- **That a gift recipient answers No is [I],** read from (a).
- **N10.** The prompt breaks N10 for a parent (25). The red team left that to the owner.
- **No form change.** The f1040.yaml source is the printed question and is unchanged. 2026 operations touch only its
  cite.locator [C changes/2026/f1040.x1-digital.yaml, per round 2].

**A13, BUG-0904 (scope.medicaid_waiver help, 42 words, the red team's verbatim).**

- **New text:** "…Pay for caring for someone who does not live with you is pay for work in someone's home."
- **Source.** "caring for someone living in your home with you" [C i1040gi.cols.txt:8661].

**A14, BUG-0808 (s1.gambling_winnings help, 44 words, the red team's verbatim).**

- **New text:** "…fantasy sports, and goods won by gambling, such as a raffle car. Give 0 if none was gambling."
- **Source.** Line 8b is gambling, including "lotteries, raffles, a lump-sum payment from the sale of a right to
  receive future lottery payments". Line 8i is "Prizes and awards" [C i1040gi.cols.txt:8611, 8634].
- **Where contest prizes go.** They are asked at `s1.prizes`, whose help says "Leave out gambling winnings"
  [C interview/2025/questions.yaml:3826].

**A3, BUG-0907 (scope.nol help and s1.nol_amount help, bank only). New in v2.**

- **Why it is here.** The red team assigns 0907 to M2, which is this patch's lane. Round 2 left it out on the
  earlier brief.
- **scope.nol help (41 words, the red team's verbatim):** "A loss bigger than that year's income, not yet used up,
  from a business, farm, rental or disaster; or a business loss held back by the yearly limit (Form 461). A loss
  still held back on Form 8582 is not one."
- **Source.** i172 lists "Rental property" among NOL sources [C sources/2025/i172.cols.txt:16]. It says "Excess
  business losses that are disallowed are treated as an NOL carryover" [C :109].
- **s1.nol_amount help (38 words; one sentence added, from med-income):** "Leave out losses held back on Form 8582
  or by basis or at-risk limits."
- **Coverage.** The existing rows `s1o.nol_*` [C interview/2025/coverage/s1_other.yaml:130-204] already walk both
  paths, so no new row was added.
- **The coordinator must drop 0907 from med-k1sche lane A,** or the two patches clash.

**Not applied here, with reasons.**

- **B2** (the `scope.contractor_pay` full prompt) corrects text in `int-n10-ticks.patch`, which adds bank prompts to
  scope.contractor_pay, household_pay, tips_unreported and wages_no_form. It belongs in that patch's v2. The
  corrected text: "In 2025, did a firm pay you (or, on a joint return, your spouse) as a contractor, with no social
  security tax taken out, when you were really its employee?"
- **B4** (lane overlap on scope.yaml). I took the "merge in sequence" option. The order int-n10-ticks, then m12 v2,
  then m34 v2 applies cleanly (tested on scratch copies).
- **Round-2 concern 0808**, the help no longer saying "small winnings, no form": the red team did not raise it.
  It is unchanged; the parent `s1.winnings_any` help still covers it.

## Re-derived values (all 23 rows; no difference found)

**Method.** I traced each row against the form expressions in xint, the walked paths of the source rows in
`reports/2025/interview_coverage.md`, and the params. The coverage rules I relied on:

- a row must answer every question its answers open;
- a stale answer fails the row;
- `any` refuses on the first true item [C interview/README.md:423-449; engine/src/interview-coverage.ts:269-276;
  engine/src/eval.ts:257-276].

No walk was run.

| Row | Predicted end | Re-derivation | Result |
|---|---|---|---|
| dividends.return_of_capital_no_form | refused div.unsupported | Same answers as `dividends.return_of_capital_over_basis` [C investments_foreign.yaml:260-274] | same |
| sales.interest_home_equity_for_stocks | proceeds f4952.line1 = 50000 | `sales.interest_election_too_large` walks line4g, line1, carryover, unsupported, alternative_allocation, s3.foreign_any [C report:1270]. Both refusals are on the always-read line2 [C f4952.yaml:301-315], so both are asked whatever line4g is. With line4g 0, bad_election (line4g > limit) is false and the walk goes on. s3.foreign_any is a background question [C report background #96], so the row's answer is used. No other f4952 input exists. | same, and lower risk than round 2's "medium" |
| sales.interest_carry_from_2024 | proceeds f4952.prior_7 = 80000 | As above, plus carryover Yes. line2 then chooses prior_7, which is asked [C f4952.yaml:283-297]. | same |
| payments.estimated_amended_overpayment | proceeds f1040.line26 = 120000 | Same answers as `payments.estimated_complete` (400000) [C household_payments.yaml:61-70]. A smaller payment with no income gives the same refund path [I]. | same |
| payments.estimated_january_2026 | proceeds f1040.line26 = 150000 | as above | same |
| other.household_nanny_payroll_service, other.household_private_driver | refused s2.other | Same answers as `other.household_employee` | same |
| s1o.ltc_reimbursed_to_provider | proceeds f8853c[mom].line24 = 3000000 | line20 = 160,600 > 0, so line24 is asked. has_line24 is true, so contract_before_ltc_date is asked; the row answers false. line21 = $420 [C params/2025.yaml:2551-2553] × 365 = $153,300; line23 = max(153,300, 120,000) = $153,300; line25 = $123,300; line26 = $37,300 (taxable, as in the source row's $7,300) [C f8853c.yaml expressions]. | same; the only new question, contract_before_ltc_date, is answered |
| s1o.ltc_others_accelerated | refused f8853c[mom].others_paid_if_periodic | Same answers as `s1o.ltc_others_paid` [C s1_other.yaml:229-239] | same |
| s1o.ltc_weekly_per_diem | proceeds f8853c[mom].line17 = 16060000 | $3,080 × 365 / 7 = $440 × 365 = $160,600 = 16060000 cents. The answers are those of `s1o.ltc_per_diem`. | same |
| pay.lockout_benefits, pay.strike_fund_nonunion | proceeds person[taxpayer].strike = 120000 / 80000 | Same answers as `pay.strike` (300000) [C pay_not_w2.yaml:131-143]. No threshold lies between $800 and $3,000 on an otherwise empty return [I]. | same |
| pay.medicaid_agency_code_ii | proceeds mw_not_box1 = 2400000 | mw_earned false: mw_other_1d = 0, line1d = 0, line8s = 0, mw_not_earned = line8s [C person.yaml:1700-1830]. Nothing is gated on false. mw_business is asked only when mw_1099 > 0 (here 0). | same; the round-2 doubt is resolved |
| scope.foreign_warrants | refused scope.other_line16 | Same answers as `scope.pfic` [C coverage/scope.yaml:538-545] | same |
| other.lottery_installment, other.lottery_rights_sale | proceeds s1.gambling_winnings = 100000 / 150000 | Source row `other.gambling_winnings` [C report:964] asks sav_* because AGI is under the saver's-credit limit. AGI = 37,500 + 1,000 = $38,500, or + 1,500 = $39,000, both under $39,500 single [C params/2025.yaml:2647-2650]. So the same sav_* questions are asked. | same (the margin is $500 on the sale row) |
| other.hobby_at_loss | proceeds s1.hobby_income = 60000 | Same answers as `other.hobby_income` [C report:974] | same |
| other.digital_airdrop | proceeds s1.digital_amount = 20000 | Same answers as `other.digital_income` [C report:961] | same |
| other.canceled_debt_exception (restated) and five `other.canceled_debt_*` | refused s1.cod_unsupported | cod_amount is seq 32, ahead of the boxes. `any` over the ten items in seq order refuses on the first true; each row answers the earlier boxes false and stops at its true box. All five true boxes are in group cod_why. The walk answers question by question, not screen by screen (there is no group handling in interview-coverage.ts). | same [I on the pending order within the `any`] |

**Notes (not value differences).**

- The two lottery rows answer `s1.prizes: 3750000` (copied from the source row), but their situations do not
  mention a prize. Consider adding "and a $37,500 prize" to each situation.
- Fixtures: the cod patch restates inputs only; no expected value was predicted, so none needed re-deriving.

## What to run (unchanged from round 2, plus)

- **Reviews made due that differ from round 2:**
  - gate:scope.nol (question, screen and false-no) and the question review of s1.nol_amount: new.
  - The question review of f8853c.line24 (now with new help).
  - gate:f4952.carryover_if_interest: **no longer due**, since its wording is unchanged.
  - The f4952 form change is now only the `ambiguity:` link on carryover. I did not check whether a link-only change
    makes the transcription review due.
- **Verify** with build, `test-fixtures`, `interview-coverage` (then `--write`), `tick-groups` and `draft-walk`, as
  in round 2.

## Owner decisions carried

1. 0833: option (a), the refusing child, or keep (b) (`amb.2025.f4952_no_2024_form`, chosen reading: a 2024 form
   only).
2. 0873: Medicaid or VA as line 24 reimbursements (`amb.2025.f8853c_line24_public`, chosen: they count).
3. 0897/0894: the former-spouse split rule [I].
4. 0907: rentals named in the NOL help, under the red team's resolution of owner decision 6. A suspended 8582 loss
   is excluded.
5. N10 overruns:
   - f1040.digital_assets prompt, 30 words;
   - f1040.estimated_any help, 44;
   - s1.gambling_winnings help, 44;
   - rec.two_returns help, 43;
   - scope.medicaid_waiver help, 42;
   - f1040.digital_assets help, 42;
   - tipjob.listed source, 41;
   - scope.nol help, 41.
