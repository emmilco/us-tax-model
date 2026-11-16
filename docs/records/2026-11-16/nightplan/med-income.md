# Fix plan: open MEDIUM entries on income questions and gates (lane plan-med-income)

Lane: plan-med-income. Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Read-only planning;
nothing in the repository was changed. Tree read: `.claude/worktrees/xint` (uncommitted expansion candidate,
HEAD 0c8cd21d), compared with `main` acde74b5 and with the tree before the redraft landed (`a2f24909^`) by
`git show` only.

## Summary

- **All 16 entries are open** (`tools/bug_status.py`, run in xint: every one "open [only a proposal]").
- **All 16 are confirmed by reading** the bank and form data (none executed). Four are confirmed only in part:
  0808 (the tick-box screen already reads "get", so only the prompt and help say "win"), 0830 (div.any is not
  narrower for an owner of shares; only div.other_boxes is), 0906 (the parent's "tips not reported in full"
  already covers tips under $20, and the "wages, no W-2" case is already a child, scope.wages_no_form), and
  0905 (an ADR holder only *may* misread it).
- **Origin.** Today's redraft (a2f24909, landed 2026-11-15 16:09): 0806, 0808, 0810, 0822, 0830, 0833, 0897,
  0900, 0901, 0904, 0905, 0907, plus the parents of 0906. Tonight's expansion (uncommitted in xint): 0873
  (all of f8853c), 0899 (all of rec; refund.itemized help), 0896 (the f1040.digital_assets bank entry is new,
  and the rewording of s1.digital_income **dropped the airdrop** that main's help named), and the children of 0906
  (scope.strike_pay, person.strike). None is older than the redraft in its present wording.
- **Five of the proposals in the entries would themselves give wrong values, or break the norms, if applied
  as written.** The plan below changes them:
  1. **0907 (NOL).** Naming "rentals or K-1 losses" in the gate invites a filer whose passive losses are
     suspended (Form 8582) to enter them as an NOL on line 8a. That understates income. Guard added.
  2. **0896 (crypto).** "Or a similar reward" invites credit-card crypto rebates, which are generally not
     income. Narrowed to the airdrop.
  3. **0897 (estimated tax).** Counting joint payments with a spouse or former spouse in the gate, before
     BUG-0894's split rule is in the line 26 help, lets a separate filer enter the whole joint payment.
     The two must be done together.
  4. **0822 (hobby).** "Even if it cost more than it brought in" invites someone who sold their own collection
     at a loss to report the gross proceeds as hobby income. Guard added.
  5. **0904 (Medicaid), 0810 (canceled debt), 0905 (foreign shares).** The entries' prompts run 50 to 85 words,
     against N2 and N10. Two of these gates (0904 and 0905) are tick-box items, so the label of 12 words or fewer
     is what the filer reads, not the prompt. Reworked as tick labels, or as a tick screen.
- **Effort.** About 13 entries are bank-only or bank plus one form source line (small, about 20 to 40 minutes
  each with checks). 0810 is the only model change, if the owner takes the tick-screen option (medium). 0906
  touches three files (medium).
- **Lanes.** Four, on disjoint form files (listed at the end). Every lane edits `interview/2025/questions.yaml`
  by entry; the protocol merges the bank by structure.
- **Owner decisions:** six, listed at the end. The largest is whether 0810 becomes a tick screen, which is a
  model change. Also needed: the reading of "used on a transient basis" (0900) and whether Medicaid or VA payments
  sent straight to the care provider count as line 24 reimbursements (0873).

Evidence convention: **[checked file:line]** means read in this session. **[inferred]** means my judgment, not
read in a source. Bank line numbers are in `interview/2025/questions.yaml` (Q:), and form line numbers are in
`forms/2025/<form>.yaml` (F:).

Common to every entry:
- A wording change alters no fixture value; no fixture input changes.
- The coverage rows proposed below record the newly named situation so that the report quotes the new wording.
  `interview-coverage --write` must be rerun after any wording change, because the report quotes wording
  (tools/README.md:539-546 [checked]).
- **Reviews made due.** A change to a form's `expr.source` or `label` makes its transcription and render reviews
  due, scoped to the changed lines (CLAUDE.md, T-219). A bank-only change (prompt, help, tick) changes the subject
  of the question review and of the screen and false-no reviews of that gate (tools/README.md:520-536 [checked]).
  Each changed gate then needs its release samples again, which is paid. One review per form per round, after all
  of that form's fixes have landed.

---

## Entries

### BUG-0806 (xrelinc-06). Tips deduction: tipjob.listed reads as "all of the work"

1. **Defect, confirmed.** The tipjob.listed source (tipjob.yaml F:39-47 [checked]) asks "Is the work you got these
   tips for on the IRS list…?". Its help (Q:4670 [checked]) says "If the work is not on it, tips from this employer
   cannot be deducted". A server who also did unlisted work for the same employer can answer No, which zeroes
   qualified tips that i1040gi allows: "only those tips that were received in an occupation on the list … are
   considered qualified tips" (i1040gi.cols.txt:8935 [checked]). The mixed-tips refusal (tipjob.other_work, gated
   on listed=Yes, F:53-64 [checked]) is then never reached.
2. **Origin:** the redraft. The id is absent before a2f24909, and main's wording equals xint's [checked].
3. **Failure mode:** a reasonable misreading. "The work" is ambiguous for a mixed job.
4. **Proposal.** Source (tipjob.yaml F:46), 35 words. This is a child of the employer roster; the prompt is the
   source.
   > Did you get any of these tips for work on the IRS list of jobs that customarily get tips? Restaurant, bar and
   > hotel staff, hairdressers and barbers, and taxi and delivery drivers are on it.

   Label (F:41): "Were any of the tips from this employer received in an occupation on the IRS list …". Help (Q:4670), 33 words:
   > The whole list is at IRS.gov/TippedOccupations. If none of the work you got tips for here is on it, tips from
   > this employer cannot be deducted and nothing more is asked about them.

   **Why it does not widen a Yes wrongly.** A mixed filer now answers Yes, then ticks tipjob.other_work ("Some were
   for other work here that is not on that list"), which refuses. So no unlisted tip enters line 4a. A wholly
   unlisted filer still answers No.
   **Who could misread the new text:** someone whose only "listed" activity is incidental, such as a mechanic who
   once delivered parts. They answer Yes, then reach other_work and are refused. That is a lost case, not a wrong
   value.
5. **Coverage row** (jobs.yaml or saving.yaml, wherever the tipjob rows live): `tips.mixed_occupation`. A server and
   bookkeeper at one restaurant answers listed=true and other_work=true, and the walk ends at the tipjob.other_work
   refusal. **Siblings:** run `tools/siblings.py tipjob.listed`. The tick label of other_work is consistent already.
   **Reviews due:** tipjob transcription and render (one line), plus the question, screen and false-no reviews of
   gate:tipjob.listed.
6. **Effort:** small (about 20 minutes). No dependencies.

### BUG-0808 (xrelinc-08). The winnings gate says "won", not "received"

1. **Defect, confirmed in part.** The prompt (Q:4265 [checked]) is "In 2025, did you … win money or a prize…". A
   2025 installment of an earlier lottery win is income when received: p525 "if you win a state lottery prize
   payable in installments, you must include … the annual payments" (p525.txt:3138 [checked heading]). Also, i1040gi
   8b lists "a lump-sum payment from the sale of a right to receive future lottery payments" (i1040gi.txt:6568
   [checked]). However, the item is in tick group `money_a`, whose heading is "In 2025, did you … get any of these?"
   (Q:52-53 [checked]). Its tick, "Gambling or lottery winnings, or a prize or award", is already keyed to receipt.
   The literal "win" sits in the prompt (read by reviews, and wherever the prompt is shown) and in the help.
2. **Origin:** the redraft.
3. **Failure mode:** the prompt is wrong under a correct answer. The walked tick screen gives that wrong answer
   only to a reader who carries "won" from the help.
4. **Proposal.** Prompt (Q:4265), 21 words:
   > In 2025, did you (or, on a joint return, your spouse) receive gambling or lottery winnings, or a prize or award?

   Help, 40 words:
   > Count winnings paid to you in 2025 even if won earlier, such as a yearly lottery installment or money for
   > selling future lottery payments; winnings in a year you lost more; and prizes in goods. A scholarship is asked
   > next.

   s1.gambling_winnings help (Q:3812), 38 words:
   > Add box 1 of each Form W-2G to winnings with no form: lotteries (including a yearly installment or a sale of
   > future payments), raffles, sports bets, fantasy sports, and prizes such as a car. Give 0 if none was gambling.

   **Source check per sentence.** Installment: p525 [checked]. Sale of future payments: i1040gi 8b [checked].
   "Lost more" agrees with s1.gambling_winnings' own source, "without subtracting any losses" (s1.yaml F:671
   [checked]). Prize points and USOPC prize money are left out on purpose. Prize points are compensation, taxable
   "when paid or made available", and naming them would pull salespeople into 8b or 8i [inferred].
   **Who could misread:** a winner whose 2024 prize was *made available* in 2024 but collected in 2025. "Paid to
   you in 2025" then counts it in the wrong year (constructive receipt). This is rare; I recommend recording it as
   a residual, not wording for it. The gambling_winnings help drops "Losses are asked with deductions" to stay
   within 40 words. The prompt already says "before subtracting any losses".
5. **Coverage rows** (other.yaml): `other.lottery_installment` (winnings_any=true, gambling_winnings=N, ends with
   proceeds equal to N on 8b); `other.lottery_rights_sale` (the same, with a lump sum). **Siblings:** the tick at
   Q:4265 is unchanged; the line is the s1.has_gambling reader. **Reviews due:** question, screen and false-no
   reviews of gate:s1.winnings_any, and the question review of s1.gambling_winnings. No form change.
6. **Effort:** small. None.

### BUG-0810 (xrelinc-10). The canceled-debt screen, as asked, drops student loans, gifts, price cuts, stockholder debts and Form 982

1. **Defect, confirmed.** The asked prompt (Q:4168 [checked]) lists six items. The form source (s1.yaml F:1329
   [checked]) lists seven, including student loans, gifts, purchase-price reductions, debts owed to a corporation
   the filer holds stock in, and other Form 982 exclusions. p4681 excludes student-loan cancellations "after
   December 31, 2020, and before January 1, 2026" and debts "canceled as a gift, bequest, devise, or inheritance"
   (p4681.cols.txt:156-158 [checked]). A filer with a forgiven student loan answers No, and the debt is taxed on 8c.
2. **Origin:** the redraft condensed the source list into the prompt and dropped one bullet and a half.
3. **Failure mode:** wrong under a correct answer.
4. **Proposal.** The current prompt is already about 55 words, above N10's 40 for a child. The entry's fix would take
   it to about 85. N2 says the remedy is "never a longer parent", and protocol 3.6 says a refusing catch-all
   becomes a tick screen. Two options:
   - **Option B (recommended; a model change; owner decision).** Use protocol 3.1: s1.cod_unsupported becomes a
     derived Bool over item inputs, so every refusal on it stays as it is. Make two tick groups under s1.cod_any.
     The heading of both is "Does any of these apply to a canceled debt?" (9 words). Boxes (each 12 words or
     fewer):
     - group cod_why: "You were bankrupt, or owed more than everything you owned" · "It was a student loan, or a
       mortgage on your main home" · "It was forgiven as a gift or under someone's will" · "The seller of something
       you bought cut what you owed" · "It was owed to a company you own shares in" · "It was a business, rental or
       farm debt"
     - group cod_how: "A home or other property was taken back or given up" · "It included interest you could have
       deducted" · "You were not personally liable for it" · "You owed it with someone not on this return"

     Each box keeps "A Yes ends the interview here" in its help.
   - **Option A (bank-only fallback).** Append to the current prompt: "it was a student loan or your main home's
     mortgage; it was forgiven as a gift, by the seller of what you bought, or by a company you own shares in". This
     breaks N10 (about 80 words) and is not recommended.

   **Source check.** The student loan comes from p4681 [checked]. "Main home mortgage" stands for qualified principal
   residence indebtedness, which p4681 covers (43 hits [checked]). Every box *refuses*, so a wrongly widened Yes loses
   the case and never gives a wrong value.
   **Who could misread:** a filer whose relative "forgave" a loan in exchange for work. That is not a gift; they
   tick "gift" and are refused, so the case is lost, not wrongly valued.
5. **Coverage rows** (s1_other.yaml or other.yaml): one per new box, each ending at the s1.cod_unsupported refusal:
   `cod.student_loan`, `cod.gift`, `cod.seller_price_cut`, `cod.stockholder`, `cod.main_home`. The existing row
   that names s1.cod_unsupported must be restated under Option B, keeping its expected end. **Fixtures:** under
   Option B, cases that set s1.cod_unsupported need the item inputs. Per 3.1 these are restated inputs, and
   `defaults.json` gets an entry per new input. **Reviews due:** under B, transcription and render of s1 for the
   new lines, class M for s1 (a model change), and the screen and false-no reviews of every new box and of the
   group. Under A, the question and screen reviews of s1.cod_unsupported. Rerun the screen review on the *asked*
   wording, since the entry notes that the screen review is shown the form source.
6. **Effort:** B is medium (about 2 hours, including restated fixtures). A is about 15 minutes. B depends on the
   owner's decision.

### BUG-0822 (xrelinc-22). s1.hobby_any asks whether the filer "made money"

1. **Defect, confirmed.** The prompt (Q:3874 [checked]) is "…make money from a hobby or pastime…", and the tick is
   "Money from a hobby or pastime not run as a business". p525: "You must include on your return income from an
   activity, even if you don't expect to make a profit … Enter this income on Schedule 1 (Form 1040), line 8j"
   (p525.cols.txt:1059 [checked]). The amount help (Q:3881) already says that costs are not subtracted, so a filer
   whose hobby lost money and who answers No drops the gross receipts.
2. **Origin:** the redraft.
3. **Failure mode:** a reasonable misreading ("make money" read as coming out ahead). The group heading "get any of
   these" softens it in the walk.
4. **Proposal.** Prompt, 29 words (a group item; the tick is what is read):
   > In 2025, did you (or, on a joint return, your spouse) get money or goods from a hobby or pastime not run as a
   > business, even at a loss?

   Tick, 12 words: "Money or goods from a hobby or pastime, even at a loss". New help on s1.hobby_any, 23 words:
   > Selling things you owned for your own use, such as a collection or old gear, is not this; it is asked with sales.

   s1.hobby_income help (Q:3881), 20 words:
   > Give everything it brought in, with goods at what they were worth. The costs of a hobby are not subtracted.

   **Why the guard is needed (a wrong-value hazard in the entry's own fix).** "Even if it cost you more than it
   brought in" also describes selling a personal collection below cost. That sale is not 8j income: a gain goes to
   Form 8949, and a loss on personal-use property is not deductible [inferred from general rules; p544 is not
   archived]. Without the guard, the gross proceeds would be taxed on 8j. Goods at fair value is the general
   barter rule [inferred; p525 bartering not re-read].
5. **Coverage row** (other.yaml): `other.hobby_at_loss`. A quilter sold $600 of quilts at a cost of $900:
   hobby_any=true, hobby_income=60000, and proceeds of 60000 on 8j. **Reviews due:** question, screen and false-no
   reviews of gate:s1.hobby_any, and the question review of s1.hobby_income. **Sibling:** the s1.yaml label of the
   hobby_any source ("receive income …") is already right and is unchanged.
6. **Effort:** small. None.

### BUG-0830 (xrelinv-04). The less-common-boxes question excludes a distribution with no form, or a form in another name

1. **Defect, confirmed for div.other_boxes and not for div.any.** The help (Q:543-546 [checked]) says "If you have no
   Form 1099-DIV, answer No". But the box questions it opens say "Include your share of amounts paid in someone
   else's name, and any amount received without a form" (div.box2b and div.box3 help [checked]). f1099div: "Any
   amount received in excess of your basis is taxable to you as capital gain" (box 3), and the Nominees paragraph
   (f1099div.cols.txt:201 [checked]). div.any ("own shares of a company or a fund … or get a Form 1099-DIV") still
   catches an owner of a closely held company, since they own shares. So I find the div.any half unconfirmed.
2. **Origin:** the redraft (the help is new in a2f24909; before it, div.any's long list named distributions with no
   form [checked]).
3. **Failure mode:** wrong under a correct answer (the help instructs No).
4. **Proposal (help only; the prompt is the div.yaml source at F:428 and is kept).** Help, 41 words:
   > Most forms show amounts only in boxes 1a, 1b, 2a, 5, 7 and 12. Count your share of a form in another's name, and
   > a payment with no form, such as a return of capital or a payout when a company closed.

   **Note on N2.** The prompt still says "Look at your Forms 1099-DIV", so a no-form filer needs the help. The
   N2-pure alternative is a child of div.any, "Did a company or fund pay you anything without a Form 1099-DIV?",
   which adds one step for every shareholder (against N12). I recommend the help, because the no-form share is
   small [inferred].
   **Who could misread:** a partner reads "a payment with no form" as a partnership distribution from a K-1. They
   answer Yes, and box 3 could take a partnership distribution. The box 3 basis refusal (div.basis_reconciled)
   follows any box 3 amount [stated in the entry; not re-read]. To be safe, "a company" could become "a corporation
   or fund" (+2 words).
5. **Coverage rows** (investments_foreign.yaml): `div.roc_no_form` (div.any=true, other_boxes=true, box3>0, ends at
   the div.basis_reconciled refusal or at its stated end); `div.nominee_share_2b`. **Reviews due:** question and
   false-no reviews of gate:div.other_boxes_if_dividends. No form change.
6. **Effort:** small. None.

### BUG-0833 (xrelinv-07). Investment interest: "leave out home-loan interest", and a carryforward asked only from a 2024 Form 4952

1. **Defect, confirmed.** (1) The prompt at Q:641-647 [checked] says "Leave out interest on a home loan". The form
   source excludes only "qualified residence interest" (f4952.yaml F:89 [checked]), and the parent's source counts "a
   home equity loan … used that way, even if you received a Form 1098" [checked]. (2) The prompt at Q:648-652 asks
   only about "a 2024 Form 4952 … line 7". Form 4952 Who Must File: "You don't have any carryover of disallowed
   investment interest expense from 2024" (f4952.cols.txt:55 [checked]).
   **Mitigation found.** The filer who reports that home-equity loan on Schedule A meets sa.mortgage_other_use
   (Q:1367-1370 [checked]), which refuses "any of the money borrowed against your home used for something other
   than buying, building or improving it". So (1) loses the deduction only for the filer who does not report the
   loan with the mortgage.
2. **Origin:** the redraft (both prompts are new in a2f24909).
3. **Failure mode:** wrong under a correct answer for both.
4. **Proposal.** f4952.line1 prompt, 38 words (a child):
   > How much interest did you pay in 2025 on money borrowed to buy investments? Leave out interest on money used to
   > buy, build or improve your home, and on money that went into tax-exempt bonds or a business.

   f4952.carryover prompt, 31 words:
   > Do you (or, on a joint return, your spouse) have investment interest from before 2025 that could not be deducted
   > and is still unused (line 7 of the latest Form 4952)?

   f4952.prior_7 help (Q:653), 36 words:
   > Line 7 of the Form 4952 filed for 2024. If none was filed for 2024 because you took the standard deduction,
   > line 7 of the latest one filed. On separate 2024 returns, add the two amounts.

   **Source check and hazards.** Line 1 no longer double-counts, because a loan that bought or improved the home is
   still left out, and a home-equity loan on Schedule A still meets the refusal. For the carryforward, "latest one
   filed" is right only when no year since then used any of it. A filer who itemized in 2024 with investment income,
   should have filed a 2024 Form 4952 and did not, would overstate. The condition "because you took the standard
   deduction" limits this [inferred]. Record the reading in the ambiguity register
   (amb.2025.f4952_latest_carryover). The form source at F:135 still says "disallowed in 2024 and carried forward";
   update its label and source to "from before 2025 and not yet deducted" so that render and bank agree. That is a
   form change.
5. **Coverage rows** (investments_foreign.yaml): `f4952.heloc_for_stocks` (line1 > 0 with no Schedule A mortgage);
   `f4952.carry_from_2023_std_2024` (carryover=true, prior_7 = the 2023 amount). **Reviews due:** f4952
   transcription and render (lines carryover and label), and the question and false-no reviews of
   gate:f4952.has_interest and gate:f4952.carryover_if_interest.
6. **Effort:** small to medium (about 40 minutes). Owner sign-off on the ambiguity reading.

### BUG-0873 (xrelret-01). f8853c: reimbursement, pre-1996 and others-paid questions narrower than their lines; the rate question says only day or month

1. **Defect, confirmed.** The line 24 prompt (Q:4227 [checked]) asks what "was paid back to you". i8853: "Enter the
   reimbursements you received or expect to receive through insurance or otherwise" (i8853.cols.txt:275 [checked]).
   The contract_before_ltc_date prompt (Q:4232) is in the past tense. others_paid (Q:4204) names only "paid at a
   set rate", while its own source at F:206 also names accelerated death benefits [checked]. periodic (Q:4181) says
   "per day or month", while i8853 defines "payments of a fixed amount made on a periodic basis"
   (i8853.cols.txt:226 [checked]).
2. **Origin:** tonight's expansion (f8853c.yaml is new in xint).
3. **Failure mode:** line24, pre1996 and others_paid are wrong under a correct answer. periodic needs a misreading,
   and the box-3 "Per diem" reference mitigates it.
4. **Proposal.** line24 prompt, 32 words:
   > How much of those care costs was, or will be, paid by insurance or anyone else, to you or straight to the care
   > provider? Leave out the payments at a set rate.

   contract_before_ltc_date prompt, 17 words: "Was any of that amount paid, or due, under a policy first issued before
   August 1, 1996?". Help, 20 words: "Count a policy first issued then even if it was later exchanged or changed. A
   Yes ends the interview here." The second half widens only a refusal, which is safe.
   others_paid prompt, 38 words:
   > In 2025, was anyone besides you (or, on a joint return, your spouse) paid at a set rate under a long-term care
   > policy on this person, or paid a life insurance benefit early because this person was ill?

   periodic prompt, 28 words: "Were any of the payments a set amount per day, week, month or other period, whatever
   the care cost ("Per diem" checked in box 3 of Form 1099-LTC)?"
   **Deliberately not named: Medicaid or the VA** (the entry names them). Whether Medicaid or VA paying a nursing
   home is a "reimbursement … through insurance or otherwise" for line 24 is not settled by i8853's text. Naming it
   would lower line 26 for those filers. If that reading is wrong, the help itself would give the wrong value.
   This is an owner decision or an ambiguity entry.
   **Who could misread:** in others_paid, "paid … early" could be read by a beneficiary of an ordinary death benefit
   paid soon after death. "Because this person was ill" excludes that.
5. **Coverage rows** (retirement.yaml or a new ltc block): `ltc.reimb_to_provider` (line24 includes an amount paid
   straight to the home; line 26 as computed); `ltc.others_accelerated` (others_paid=true; refusal);
   `ltc.weekly_per_diem` (periodic=true). **Reviews due:** question and false-no reviews of
   gate:f8853c.has_periodic, has_line24 and periodic. These forms are new tonight, so this round's reviews must run
   on the changed text: fold the fix in before f8853c's first review if it has not run yet. No form change; the
   sources already say "received or expect to receive" and "per day, week or month".
6. **Effort:** small. Owner decision on Medicaid and the VA (does not block).

### BUG-0896 (xrelwide-04). Crypto: staking or fork coins while only holding read as a No; airdrops not named for 8v

1. **Defect, confirmed.** The f1040.digital_assets help (Q:3894-3900 [checked]) says that buying and holding is a No
   and gives Yes only for being paid, swapping and spending. i1040gi p. 16: Yes if you "Received new digital assets
   as a result of mining, staking, and similar activities; Received digital assets as a result of a hard fork"
   (i1040gi.cols.txt:295 [checked]). s1.digital_income (Q:3901) is a closed list without airdrops. **On main** its
   help said "(a fork, or an airdrop after one) count" [checked, acde74b5]; tonight's rewording dropped that.
2. **Origin:** tonight's expansion. The gate's bank entry is new, and the airdrop was lost in the s1.digital_income
   rewording.
3. **Failure mode:** wrong under a correct answer, because the help literally instructs No.
4. **Proposal.** f1040.digital_assets help, 39 words:
   > Buying crypto with dollars and holding it, or moving it between your own wallets, is a No. Being paid in crypto,
   > getting staking rewards or new coins from a fork or airdrop, swapping, or spending it is a Yes.

   s1.digital_income prompt, 33 words (a child): "Did you (or, on a joint return, your spouse) receive any crypto
   from staking, from mining that is not a business, from a fork (a coin split in two), or from an airdrop?". Help:
   add "A gift of crypto from a person is not counted." (total 37 words). Source: i1040gi 8v "Don't report a gift or
   inheritance of digital assets on line 8v" (i1040gi.cols.txt:8668 [checked]).
   **Changed from the entry.** I dropped "or a similar activity/reward". Credit-card or exchange "crypto rewards"
   on purchases are generally rebates, not income [inferred]. That wording would put them on 8v as a wrong value.
   An airdrop after a fork is income per rr-2019-24 (rr-2019-24.cols.txt:7, 32 [checked]). A non-fork airdrop is
   not addressed in the archived sources; it is under i1040gi's "similar activities" [inferred]. **The digital
   asset answer is printed on Form 1040**, so the gate's help also decides a printed answer. The proposed help
   matches i1040gi's Yes list.
5. **Coverage rows** (s1_other.yaml): `crypto.staking_only` (digital_assets=true, digital_income=true, amount on 8v);
   `crypto.airdrop`. **Reviews due:** question, screen and false-no reviews of gate:f1040.digital_assets and
   s1.digital_income. If the source of s1.digital_income in s1.yaml (F:558) is aligned to add airdrops, that also
   makes the s1 transcription and render due. Recommended: add ", or an airdrop" to that source.
6. **Effort:** small. None.

### BUG-0897 (xrelwide-05). The estimated tax gate misses an amended-return overpayment and joint payments sent by a (former) spouse

1. **Defect, confirmed.** Prompt, tick and help at Q:2271-2279 [checked]. i1040gi line 26: "Include any overpayment
   that you applied to your 2025 estimated tax from your 2024 return or an amended return". It also covers joint
   payments with a former spouse, and dividing joint payments on separate returns (i1040gi.cols.txt:901-902
   [checked]). This is a tick item in group `paid_already`, so the tick is what the filer reads.
2. **Origin:** the redraft.
3. **Failure mode:** wrong under a correct answer (the amended-return overpayment; a payment sent by a former
   spouse).
4. **Proposal.** Tick, 9 words: "Estimated tax payments, or an overpayment applied to 2025". Prompt, 25 words: "Were
   estimated tax payments made for 2025 by you (or, on a joint return, your spouse), or an earlier overpayment
   applied to your 2025 tax?". Help, 31 words:
   > Count payments by mail, online or card, including the one due in January 2026, and an overpayment from your 2024
   > return or an amended return that you had applied to 2025.

   **Joint payments with a spouse or former spouse (wrong-value hazard).** Do not add them to the gate until
   BUG-0894's line 26 help (the split rule) lands in the same lane. Otherwise a separate or divorced filer who now
   answers Yes enters the whole joint payment on line 26 and overstates the refund. When BUG-0894 lands, add to the
   help: "Count joint payments made with a spouse or former spouse; the next question says what share to enter."
   The f1040.line26 prompt (Q:2283) says "counting any 2024 refund applied"; change it to "any overpayment
   applied" (a sibling).
5. **Coverage rows** (household_payments.yaml or opening.yaml): `est.amended_overpayment` (estimated_any=true,
   line26=N); `est.jan_2026_payment`. **Siblings:** f1040.line26 prompt and help; NY ny_it201 "had a 2024 refund
   applied" (forms/ny/2025/ny_it201.yaml:2391 [checked]), for jurisdiction ny, noted for the NY lane only.
   **Reviews due:** question, screen and false-no reviews of gate:f1040.estimated_any and the question review of
   f1040.line26.
6. **Effort:** small. **Dependency:** do it together with BUG-0894 (same lane).

### BUG-0899 (xrelwide-07). Recoveries on a joint return: whose 2024 return the itemizing question is about

1. **Defect, confirmed.** rec.path reads refund.itemized (rec.yaml F:207-225 [checked]). refund.itemized asks "Did
   you itemize … on your 2024 federal return?" (Q:3998 [checked]). rec.two_returns' help says "Answer No if only one
   of you got money back" (Q:4259 [checked]) but, unlike refund.two_returns (Q:3974 [checked]), does not say that
   the next questions are about that person's own return. So a joint filer whose spouse alone itemized on a separate
   2024 return answers No, and the taxable recovery is dropped. The cross case also stands: one spouse's state
   refund and the other's other recovery, on separate 2024 returns, end up on one worksheet. This is outside the
   reading recorded in amb.2025.rec_two_returns (ambiguities/2025.yaml:2285-2299 [checked]).
2. **Origin:** tonight's expansion (rec is new; refund.itemized's help was changed tonight; its prompt comes from
   the redraft).
3. **Failure mode:** wrong under a correct answer.
4. **Proposal.** rec.two_returns help, 38 words:
   > Answer No if you filed one joint 2024 return, or only one of you got money back (the questions that follow are
   > then about that person's 2024 return). A state income tax refund counts. A Yes ends the interview here.

   refund.itemized help, 39 words:
   > On separate 2024 returns, answer for the return of the one who got the money back. If that return took the
   > standard deduction, the answer is No, and none of the refund or other money paid back is taxed.

   **Check.** "None … is taxed" when the standard deduction was taken agrees with p525 p. 24 "If you didn't itemize
   … don't include any of the recovery" (rec.yaml F:207 cite [checked]). Counting a state refund in rec.two_returns
   sends the cross case to the existing refusal, which is consistent with the ambiguity's first reading.
   **Who could misread:** a couple who filed jointly in 2024. The first clause still gives them No.
5. **Coverage rows** (other.yaml or a new rec block): `rec.spouse_only_itemized_separately` (two_returns=false,
   itemized=true for the spouse; the recovery taxed); `rec.cross_state_refund_and_other` (two_returns=true;
   refusal). **Reviews due:** question and false-no reviews of gate:rec.two_returns_if_joint and rec.path, and the
   question review of refund.itemized. No form change.
6. **Effort:** small. None.

### BUG-0900 (xrelwide-08). AMT mortgage interest: the help rules out a house or condominium used on a transient basis

1. **Defect, confirmed.** The help (Q:1033-1035 [checked]) says "A house, an apartment, a condominium or a mobile home
   is not one of these". i6251 line 3: "A qualified dwelling for AMT is a house, apartment, condominium, or mobile
   home not used on a transient basis. A qualified dwelling for AMT doesn't include house boats and recreational
   vehicles" (i6251.cols.txt:218 [checked]). s2.amt_boat is already a child, asked only when the AMT could apply
   (s2.yaml F:891-916 [checked]).
2. **Origin:** the redraft.
3. **Failure mode:** wrong under a correct answer, because the help instructs No.
4. **Proposal.** Prompt, 36 words:
   > Is any of the mortgage interest you (or, on a joint return, your spouse) deduct for a place, not your main home,
   > that is a boat or RV, or a home rented out for short stays?

   Help, 39 words: "A camper, travel trailer or houseboat is an RV. Count a place that was your main home for
   only part of 2025. The alternative minimum tax (Form 6251) then has to be figured; a Yes ends the interview here."
   **The reading** of "used on a transient basis" as "rented out for short stays" is mine [inferred]; the instructions
   do not define it. Every Yes refuses, so the broad reading loses cases and cannot give a wrong value. Record it as
   amb.2025.amt_transient (owner). Align the s2.yaml label and source (F:880-887), which also name only a boat or RV.
5. **Coverage rows** (home.yaml): `amt.condo_short_stay` (amt_boat=true; refusal at Form 6251).
   **Reviews due:** s2 transcription and render (one line), and the question and false-no reviews of
   gate:s2.amt_boat_ask.
6. **Effort:** small. Owner decision on the reading (does not block, since the result is only a refusal).

### BUG-0901 (xrelwide-09). Household employee gate: a nanny paid through a payroll service, a private driver, January pay for 2024 work

1. **Defect, confirmed by reading; the Schedule H source is not archived.** The prompt "work in or around your home"
   and the help "Count anyone you paid yourself … Do not count a company you hired" (Q:977 area [checked]).
   **The source for drivers and agencies (i1040sh, p926) is not in sources/2025** [checked by listing]; the entry
   says the same.
2. **Origin:** the redraft.
3. **Failure mode:** misreading for the payroll service; wrong under a correct answer for the driver ("in or around
   your home").
4. **Proposal.** Tick, 11 words: "Someone you paid to work for your household: nanny, housekeeper, driver". Help, 39
   words:
   > Count a worker you choose and direct even if a payroll service or registry handles the pay, a private driver,
   > and pay in 2025 for 2024 work. Do not count a company that sends and directs its own staff.

   **Every sentence rests on Schedule H and p926, which are not archived.** Before applying it, archive i1040sh (2025)
   and p926 (2025) and check (a) private drivers as household workers and (b) the agency-control test. That is a
   dependency. The child s2.household_employee refuses, so a widened Yes only loses cases. The help of the cash-wage
   test child is unchanged.
5. **Coverage row** (household_payments.yaml): `household.nanny_via_payroll_service` (household_help=true,
   household_employee=true; refusal). **Reviews due:** question and false-no reviews of gate:s2.household_help.
6. **Effort:** small, plus archiving two sources (`tools/` source archive flow; about 20 minutes).

### BUG-0904 (xrelwide-12). Medicaid waiver gate asks whether "a state program paid you"

1. **Defect, confirmed.** The scope.yaml source at F:628 is "did a state Medicaid program pay you … to care for
   someone who lives in your home?". The tick (Q:1851 [checked]) is "Medicaid pay for caring for someone who lives
   in your home". i1040gi 8s: "Certain Medicaid waiver payments you received for caring for someone living in your
   home with you … should be reported to you on Form(s) W-2 in box 12, Code II" (i1040gi.cols.txt:8661 [checked]).
   Pay through an agency reads as a No.
2. **Origin:** the redraft (the help was altered tonight when 8s became supported).
3. **Failure mode:** wrong under a correct answer (an agency, not the state, paid).
4. **Proposal.** This is a tick item (group other_pay), so the entry's 50-word prompt does not fit.
   Tick, 12 words: "Medicaid pay, through any agency, for care of someone living with you". Source (F:628),
   30 words:
   > In 2025, were you (or, on a joint return, your spouse) paid under Medicaid, directly or through an agency or care
   > plan, to care for someone who lived in your home with you?

   Help, 41 words:
   > Also called difficulty of care payments, often paid through an agency or care plan. A W-2 with code II in box 12
   > shows them. Care in the other person's own home, with no W-2, is pay for work in someone's home.

   **Who could misread:** an agency aide caring for a client in the *client's* home reads "through any agency" and
   ticks Yes. The children (person.mw_box1, whose help says "Count only pay for caring for someone who lives in your
   home with you", Q:1940 area [checked]) then exclude the wrong pay. The tick keeps "living with you" for that
   reason. That is the residual risk.
5. **Coverage row** (pay_not_w2.yaml): `mw.agency_paid_code_II` (medicaid_waiver=true, mw_box1=N; 8s=N).
   **Reviews due:** scope transcription and render (one line), and the question, screen and false-no reviews of
   gate:scope.medicaid_waiver.
6. **Effort:** small. None.

### BUG-0905 (xrelwide-13). Foreign shares gate: options or warrants, ADRs, foreign ETFs, holdings through an estate or pension

1. **Defect, confirmed in part.** The source at F:985 and the tick at Q:2039 [checked]. Options are not named.
   Section 1298 treats an option as stock; i8621 mentions option holders (i8621.cols.txt:12, 34 [checked]). A
   foreign ETF (where "U.S." may be read with "mutual fund" only) and an ADR are misreadings. The children
   scope.pfic and scope.cfc both refuse (Q:2045-2052 [checked]).
2. **Origin:** the redraft.
3. **Failure mode:** options are wrong under a correct answer; the rest are misreadings.
4. **Proposal.** Tick, 12 words: "Shares, options or warrants of a company or fund set up abroad". Source: "…own shares,
   or options or warrants to buy them, of a company or a fund set up outside the United States, other than through a
   fund set up in the United States?". Help, 36 words:
   > Count stock or ADRs of a company set up abroad even if bought in the U.S., a fund set up abroad, and shares held
   > for you by a partnership, trust, estate, foreign pension or insurance policy.

   **Effect.** This widens the parent to every ADR holder, who then meets two short children (both answered No for
   an operating company). That is a cost under N3 with no wrong value, since the children only refuse. Owner
   check: is the extra step for ADR holders acceptable? The alternative is to leave ADRs out and accept the
   misreading.
5. **Coverage row** (investments_foreign.yaml): `foreign.warrants_on_foreign_spac` (foreign_shares=true, pfic=true;
   refusal). **Reviews due:** scope transcription and render, and the question, screen and false-no reviews of
   gate:scope.foreign_shares.
6. **Effort:** small. Owner check (minor).

### BUG-0906 (xrelwide-14). Pay-not-on-a-W-2 gate: lockout benefits, non-union strike funds, noncash tips

1. **Defect, confirmed in part.** i1040gi 1h: "Strike or lockout benefits (other than bona fide gifts)", with no
   source restriction (i1040gi.cols.txt:502 [checked]). The parent tick "Wages, tips or strike benefits that are not
   on a W-2" (Q:1849) omits lockout. The child scope.strike_pay ("Strike or lockout pay from a union", Q:1879) and
   person.strike ("from a union", person.yaml F:1481) add a union restriction [checked]. Noncash tips: "include the
   value of any noncash tips … such as tickets, passes" (i1040gi.cols.txt:468 [checked]). The parent's help does not
   name them, though the child scope.tips_unreported does. **Not confirmed:** tips under $20 (the parent's "not
   reported in full" covers them, and person.f4137_under20 handles them), and an employer that issues no W-2 (already
   the child scope.wages_no_form, Q:1880 area [checked]).
2. **Origin:** the redraft for the parent; tonight for the strike and lockout children.
3. **Failure mode:** lockout and non-union funds are wrong under a correct answer; noncash tips are a misreading.
4. **Proposal.**
   - scope.pay_no_w2 tick, 11 words: "Wages, tips, or strike or lockout pay not on a W-2". Source (scope.yaml F:453): the
     same with "strike or lockout benefits". Help, 38 words: "Such as pay for work in someone's home, tips not
     reported in full to your employer, tips given as tickets or goods, or pay from a firm that wrongly treated you
     as a contractor. A Yes asks which."
   - scope.strike_pay tick: "Strike or lockout pay". Source (F:562-569): drop "from a union". New help, 25 words:
     "Count it from a union or a strike fund, but not true gifts. State unemployment pay is not this; it is asked
     with Form 1099-G."
   - person.strike source (person.yaml F:1481), 23 words: "How much did you get in 2025 in strike or lockout
     benefits? Leave out true gifts and state unemployment pay. Zero if none."

   **Wrong-value guard.** Without "from a union", a locked-out worker on state unemployment insurance could enter it
   here as well as from the 1099-G, counting it twice (1h and Schedule 1 line 7) [inferred]. Hence the unemployment
   exclusion.
5. **Coverage rows** (pay_not_w2.yaml): `pay.lockout_benefits` (pay_no_w2=true, strike_pay=true, person.strike=N;
   N on 1h); `pay.strike_fund_nonunion`; `pay.noncash_tips_only` (pay_no_w2=true, tips_unreported=true,
   person.tips_noncash=N; 1c). **Reviews due:** transcription and render of scope (two lines) and person (one line),
   and the question, screen and false-no reviews of gate:scope.pay_no_w2, scope.strike_pay_if_pay and
   scope.tips_unreported_if_pay.
6. **Effort:** medium (three files, about 1 hour). None.

### BUG-0907 (xrelwide-15). NOL gate: a disallowed excess business loss, a first-year carryforward, rental or K-1 losses

1. **Defect, confirmed.** The help (Q:2066-2071 [checked]) is "A loss bigger than that year's income, carried forward
   on an earlier return …". i172: "Excess business losses that are disallowed are treated as an NOL carryover to the
   following tax year" (i172.cols.txt:109 [checked]). An NOL may come from a trade or business, casualty and theft
   losses from a federally declared disaster, or rental property (i172.cols.txt:16 [checked]). "Start by carrying
   the NOL to the first tax year after the NOL year" (i172.cols.txt:61 [checked]), so a 2024 NOL used on no return
   yet is in 2025. The children (s1.nol_amount, and the refusal s1.nol_ebl "Some is a business loss held back by
   the yearly limit", Q:2084-2090) exist in xint.
2. **Origin:** the redraft (the help); tonight's expansion made a Yes compute instead of refuse.
3. **Failure mode:** an excess business loss with positive income is wrong under a correct reading of the help; the
   first-year loss is a misreading ("carried forward on an earlier return").
4. **Proposal.** Help, 44 words (the guard sentence is load-bearing):
   > A loss bigger than that year's income, not yet used up, from a business or farm (including a K-1 share) or a
   > disaster; or a business loss held back by the yearly limit (Form 461). Passive losses held back on Form 8582 are
   > not.

   **Changed from the entry (wrong-value hazard).** The entry names "rentals" and "a K-1". A landlord with suspended
   passive losses on Form 8582 would read "rentals" and enter them on s1.nol_amount, so a suspended passive loss
   would be deducted as an NOL [inferred, from the 8582 rules]. I drop "rentals" and add the 8582 exclusion. An
   excess-business-loss Yes reaches s1.nol_ebl and refuses. **Residual:** a true rental NOL (for example a real-estate
   professional, or a loss under the $25,000 allowance that exceeded income) may now answer No. That is rare; owner
   decision 6. Mirror the exclusion in the s1.nol_amount help (Q:2072): "Leave out losses held back on Form 8582 or by
   basis or at-risk limits."
5. **Coverage rows** (scope.yaml coverage or s1_other.yaml): `nol.ebl_2024` (scope.nol=true, nol_ebl=true;
   refusal); `nol.first_year_carry` (scope.nol=true, nol_amount=N; 8a=N). **Reviews due:** question, screen and
   false-no reviews of gate:scope.nol and the question review of s1.nol_amount. No form change.
6. **Effort:** small. Owner decision 6 (does not block).

---

## Lane split (disjoint form files), order, owner decisions

Every lane edits `interview/2025/questions.yaml` by bank entry only. The integrator merges the bank structurally by
input, as the protocol prescribes. Each lane claims its forms (`tools/claims.py`), works in its own worktree, uses
`tools/worktree_data.py`, and runs `tools/check_all.sh` once at the end. Model and class per CLAUDE.md:
**judgment (Opus)** for lanes M1 and M3, which contain readings; **mechanical (Sonnet)** is possible for M2 and M4
once the owner rules on the wording above.

| Lane | Forms owned (source changes) | Entries | Est. |
|---|---|---|---|
| M1 income-s1 | s1.yaml, tipjob.yaml | 0806, 0808, 0810 (A or B), 0822, 0896 (also the f1040.digital_assets bank help) | 1.5 h (B: +2 h) |
| M2 pay-scope | scope.yaml, person.yaml | 0904, 0905, 0906, 0907 (the s1.nol_amount help is bank-only) | 1.5 h |
| M3 invest | div.yaml, f4952.yaml | 0830, 0833 | 1 h |
| M4 other | f1040.yaml (bank), s2.yaml, rec.yaml/refund.yaml (bank), f8853c.yaml (bank) | 0897 (+ BUG-0894), 0899, 0900, 0901, 0873 | 1.5 h |

Conflict check: 0896 touches the f1040.digital_assets *bank* entry only, and 0897 touches f1040's bank entries.
f1040.yaml's source is changed by neither, so M1 and M4 do not share a form file. 0907's s1.nol_amount is
bank-only, so M2 does not touch s1.yaml.

**Order.**
1. M3 and M4 first. They have the most wrong-under-correct-answer cases and small diffs; 0873 lands before
   f8853c's first review.
2. M2.
3. M1 last, because 0810 waits on the owner's decision.

After each lane, rerun `interview-coverage --write`. Each lane runs its due reviews once, after all of its form's
fixes (about 14 gate subjects become due for screen and false-no samples). Estimate the cost first; runs above
$3.00 need `--approve-cost`.

**Owner decisions.**
1. **0810.** Turn s1.cod_unsupported into two tick groups through a derived line (Option B, a model change), or
   lengthen the prompt (Option A, which breaks N10)?
2. **0900.** Read "used on a transient basis" as "rented out for short stays" (recorded as amb.2025.amt_transient)?
   A wrong reading only refuses, so this does not block.
3. **0873.** Do Medicaid or VA payments sent straight to the care provider count as line 24 reimbursements? The plan
   leaves them unnamed until ruled.
4. **0897 with BUG-0894.** Count joint payments with a spouse or former spouse, with the split rule in the line 26
   help, or refuse separate returns that have joint estimated payments?
5. **0833.** Use the "latest Form 4952 filed" carryforward when no 2024 form was filed because of the standard
   deduction (amb.2025.f4952_latest_carryover)?
6. **0907.** Accept that a true rental NOL may now read as a No, in exchange for keeping suspended passive losses
   out of line 8a?
7. (Minor) **0905.** Accept the extra step for ADR holders.

**Not done or not checked in this plan.**
- No entry was executed.
- Schedule H and p926 are not archived, so 0901's help cannot be checked against them (dependency: archive them).
- p544 (personal-use sales) was not read; 0822's guard rests on general rules.
- `tools/siblings.py` was not run (each lane runs it at fix time).
- Word counts were computed by script; every proposed prompt is at most 38 words, every tick at most 12, and every
  help at most 44 words.
