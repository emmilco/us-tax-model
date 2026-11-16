# Lane A3-lows-sche: lows riding with sche-a, int-amt, int-p18, int-n10 and int-rprop

claude-opus-5-5, judgment, year 2025, jurisdiction us (one NY item, BUG-0857). Written 2026-11-16, Phase A of round 4.
I read xint and did not change it. Edits were made only on scratch copies in `scratch/round4-lows-sche/`. Nothing was
built, walked, tested or reviewed, and no paid call was made.

Labels:
- **[C path:line]**: checked against that file this session. xint paths unless marked "chain", which means the scratch
  copy with the v2 chain applied.
- **[I]**: inferred, not checked.

Word counts come from a whitespace split of the bank entry or the form source, done by a script on the applied copy.

## Summary

- **Two add-on patches, both drafted against the full v2 chain:**
  - `patches/v3/sche-a-lows.patch`: `forms/2025/rental.yaml` and `interview/2025/questions.yaml`. 12 lows fixed or
    partly fixed.
  - `patches/v3/int-lows.patch`: the NY form and NY bank, a NY fixture and coverage row, and the federal bank.
    6 lows fixed.
- **Apply order.** Each patch was applied with `patch -p1 -F0` to a scratch copy of xint's files [C]. All hunks
  applied, and every changed YAML file parses with a duplicate-key-checking loader. `it201.json` parses, and a JSON
  round trip reproduces it byte for byte [C].
  - **Order A:** sche-a, int-amt, int-p18, int-personas, int-n10, int-n10-ticks, then v3 sche-a-lows, then v3
    int-lows. This is the v2 order in sche-int.md.
  - **Order B:** order A with int-rprop inserted before the v3 patches. Both orders give the same v3 text [C grep].
- **Neither v3 patch applies straight after its own v2 patch [C].**
  - sche-a then sche-a-lows fails 2 of 7 hunks. The context includes int-n10's `rental.days_personal` prompt and other
    bank lines.
  - int-amt then int-lows fails 3 of 4 hunks. The context includes int-p18 and int-n10 lines.
  - **So both v3 patches go at the end of the v2 chain.**
- **Integrator finding (not a low): v2 `int-rprop.after-v2-n10.patch` does not apply after the v2 chain.** Its 2
  `questions.yaml` hunks fail at `-F0` and `-F2`.
  - Cause: the patch was rebased onto v2 int-n10 alone. sche-a has since changed the `rental_costs_c` heading and the
    `rental.not_at_risk` help, which are context lines in those hunks.
  - Its non-bank files apply. Its own bank script works on the chain once its heading string is updated. A copy with
    that one string changed is `scratch/round4-lows-sche/apply_bank_chain.py`; it is how order B was built.
  - **Fix at merge:** rerun the int-rprop bank edit with the corrected heading string, or regenerate the patch from the
    chain.
- **BUG-0781: close when sche-a lands.**
  - The v2 `rental.not_at_risk` source covers no personal liability, a guarantee or stop-loss, and a lender "with a
    stake in it" [C chain rental.yaml:1965-1966].
  - Its help names the seller, a co-owner and a relative of either [C chain questions.yaml:7226-7227].
  - Residual (rare; can go in the closure note): property taken subject to a private nonrecourse mortgage, and the
    spouse's own nonrecourse note.
- **BUG-0857 is fixed with int-amt's new gate.** int-amt makes `f1040.tax_exempt_any` an input asked of everyone.
  - The NY gate now opens on that Yes **or** on line 2a > 0, so a premium bond whose net interest is $0 still reaches
    the line 20 question.
  - No existing NY case changes [C].
- **Deferred (13 lows, listed at the end).** Most need a new input or a refusal. A new input needs defaults, class M
  restatements and coverage rows, and so is M effort. 0791 cannot meet the 12-word tick cap as proposed. The others
  are latent K-1 items, 1040-NR line numbers I could not check against an archived source, or form-source bullets that
  would make a new review due on a form no patch changes.
- **N10 overruns introduced (owner's call):**
  - `rental.days_personal` bank prompt: 49 words (was 43; child aim 40).
  - `k1s.not_at_risk` prompt: 42 (was 37).
  - NY bond help: 44.
  - `sb.bonds_any` and `sd.sold_other` help: 42 each.
  - `rental.days_personal` form source: 72. It is the long source the bank prompt overrides; the source was already
    over before this patch.

## Per-low entries: sche-a-lows.patch

Format: **entry**, re-verified, change, text with word count, source, red team (who could answer wrongly after the
change), reviews made due.

### BUG-0772: personal-use days, sale exception
- **Re-verified:** real. The chain `rental.days_personal` bank prompt says "for 12 months in a row" only [C chain
  questions.yaml:6952]. i1040se adds "(or for a period of less than 12 consecutive months at the end of which you sold
  or exchanged it)" [C sources/2025/i1040se.cols.txt:114, p. 5].
- **Change:**
  - Form source of `rental.days_personal`: adds ", or for less if you then sold or traded it."
  - Bank prompt: adds ", or for less if you then sold it." The bank prompt is 49 words, an N10 overrun.
- **Parent help left alone, on purpose.** A filer who reads only the parent's 12-month clause answers the parent Yes.
  The child then lets them enter 0. With `personal_c` at 0, the home test is false and the costs are not divided, so
  the value is correct either way [C rental.yaml:171-190, 283-302]. So the parent help (45 words) need not grow.
- **Red team:**
  - "Then sold" could be read as a sale years later, after the rental ended. "Then" ties the sale to the end of the
    rental [I].
  - A 2025 sale already refuses at `rprop.disposed` when a building is listed.
- **Due:** rental transcription and render, line-scoped. A question review of `rental.days_personal`.

### BUG-0926: shared equity financing co-owner
- **Re-verified:** real. p527: "unless you rent it to another owner as their main home under a shared equity financing
  agreement" [C p527.cols.txt:871].
- **Change:** added to the `rental.days_personal` help (38 words): "Also leave out days a co-owner rented it from you as
  their main home at a fair rent under a shared equity financing agreement."
- **Red team:**
  - The parent `rental.personal_any` asks about "another owner", so such a filer answers Yes, reaches the child, and
    enters 0. Same outcome as 0772. Their days stay in `days_fair` (fair rent).
  - It is placed in the child, not the parent, because the parent help is already 45 words.
- **Due:** question review of `rental.days_personal` (the same review as 0772).

### BUG-0784: services from a manager or staff
- **Re-verified:** real. The chain form source says "Did you provide services ..." [C chain rental.yaml:400].
- **Change:**
  - Form source: "Did you, or a manager or staff for you, provide services for renters, such as cleaning during their stay,
    changing linen or meals?" (23 words).
  - Tick: "Renters got services, such as cleaning during stays or meals" (10).
  - Help (23): "From you, a manager or staff. Heat, light, trash collection and cleaning shared areas do not count. A Yes
    ends the interview here."
- **Source:**
  - i1040se p. 5, Line 3 (maid service).
  - p527: "basic services such as heat and light, trash collection, etc." go on Schedule E [C p527.cols.txt:581].
  - p527: "regular cleaning, changing linen, or maid service" go on Schedule C [C :599].
- **Red team:**
  - A landlord whose manager only collects rent and arranges repairs reads "services" broadly and answers Yes. That is
    an over-refusal. The help guards it, and the screen review's finding 0 (an over-refusal) is reduced.
  - "Cleaning shared areas" is my gloss of "basic services" [I].
- **Due:** rental transcription and render; screen and false-no samples of `rental.services`; question review.

### BUG-0783: 10% at any time, by value; the year a held-back loss arose
- **Re-verified:** real [C chain rental.yaml:411, 1676].
- **Change:**
  - `rental.under_tenth` source (19 words): "At any time in 2025, did you (with your spouse) own less than a tenth of it, by
    value?"
  - Its tick (12): "In 2025 you (with your spouse) owned under a tenth, even briefly".
  - `rental.prior_not_active` source (40): "...did not help make decisions for it, or when you (with your spouse) owned less
    than a tenth of it at some time that year?"
- **Source:** i8582 p. 4, "if at any time during the tax year your interest (including your spouse's interest) ... was
  less than 10% (by value)"; i8582 p. 10, column (c) rule [U as quoted in the entry; the cites already in the form].
- **Red team:**
  - "By value" is dropped from the tick to fit 12 words. A filer who owns 10% of the units but less by value is rare.
    The full prompt keeps it.
  - "Even briefly" could unsettle an owner who bought in during 2025. Before the purchase they owned nothing, not less
    than a tenth. Answering Yes then over-refuses only [I].
- **Due:** transcription and render (2 lines); the screens `rental.under_tenth` and `rental.prior_not_active`; question
  reviews.

### BUG-0782: part of a property used otherwise, or lived in earlier in 2025
- **Re-verified:** real [C chain rental.yaml:441; chain questions.yaml:6995].
- **Change:**
  - Label: "Part of a property the filer also lives in, lived in during 2025, or uses".
  - Form source (42 words): "Is it part of a property you live in or use yourself, or lived in during 2025, such as a room in your
    home, one unit of a building you live in, or space in a building that holds your own office?"
  - Bank prompt (29): "For this rental property — Is it part of a building you live in or use yourself, or lived in during
    2025, such as a room or a unit?"
  - Tick (12): "Part of a building you lived in or used yourself in 2025".
- **Remedy text left unchanged** ("…part of a home or building you also live in…"). Changing it would move every fixture
  that asserts the remedy [I: not grepped]. The owner may prefer to widen it.
- **Red team:** a landlord who keeps tools in the rental's basement reads "used yourself" and answers Yes. That is an
  over-refusal only.
- **Due:** transcription and render; screen and false-no of `rental.part_home`; question review.

### BUG-0785 (spouse half only)
- **Re-verified:** real [C chain rental.yaml:1638].
- **Change:** source (29 words): "Was a loss from this rental held back (not deducted) on a 2024 or earlier return of yours (or, on a
  joint return, your spouse's), including a separate one?"
- **Deferred half: the grouped activity.** A rental grouped in 2025 already refuses at `sche.grouped`. For one grouped
  only in earlier years, the share of the group's carryover needs an allocation rule I have no archived source for.
- **Red team:** an MFS filer sees the plain-"you" form of the spouse phrase, so the spouse's own loss is not invited
  [C per coordinator notes on the engine's MFS rendering].
- **Due:** transcription and render; screen and false-no of `gate:rental.prior_any`.

### BUG-0787: prepaid insurance
- **Re-verified:** real [C chain rental.yaml:714].
- **Change:**
  - `rental.amt9` source (22 words): "Insurance on it for 2025 coverage, paid in 2025 or paid earlier for more than one year
    (only the part for 2025)". Label: "Insurance for 2025 coverage, …".
  - The `rental.amt9` cite becomes p527 p. 5, "Insurance premiums paid in advance" [C p527.cols.txt:122, page by form-feed
    count].
  - Tick (7): "Insurance covering 2025, even if paid earlier". This is what lets a 2024 multi-year premium reach the amount
    question under the heading "did you pay any of these".
- **Red team:**
  - The v2 home-part frame in the amt9 help still applies. The two do not conflict.
  - A filer who paid a 2026 renewal in December 2025 now reads "for 2025 coverage" and leaves it out. That is correct.
- **Due:** transcription and render; screen and false-no of `gate:rental.has_insurance`; tick-groups.

### BUG-0788: citations
- **Re-verified:** real. i1040se has no Line 8, 9 or 15 headings. Its headings are 1a, 1b, 2, 3, 4, 6, 10, 12 and 13,
  14, 17, 18, 19, 21 and 22, and "General Instructions for Lines 5 Through 21" is on p. 6 [C i1040se.cols.txt:100-202].
- **Change:** the three anchors (`&id005` commissions, `&id006` insurance, `&id012` supplies) now cite "p. 6, General
  Instructions for Lines 5 Through 21", as the advertising and cleaning lines already do [C chain rental.yaml:487, 560].
- No value changes.
- **Not checked:** royalty.yaml's line 15 cite (the entry asks for it) has no "Line 15" text [C grep: 0 matches].
  `sa.yaml` shows the same wrong locator strings [C grep], but cites a different document; not in scope.
- **Due:** run `tools/citations.py`; the rental render picks up the cite.

### BUG-0777: interest on loan proceeds spent elsewhere
- **Change:** `rental.amt12` source (28 words): "…paid in 2025, leaving out interest on any part of the loan spent on something
  else".
- **Why the source and not the help:** the v2 help is already 49 words.
- **Source:** i1040se p. 7, Lines 12 and 13, "you allocate interest on a loan the same way you allocate the loan proceeds" [U, as
  quoted in the entry; the heading is at C i1040se.cols.txt:168].
- **Red team:** cash from a refinance that was spent on the rental itself still counts. "Something else" excludes only
  other uses.
- **Due:** transcription and render.

### BUG-0925: prepaid interest and points
- **Change:** `rental.amt13` source (34 words): "Other interest on loans for it (no Form 1098 in your name), paid in 2025 and not
  for a later year; for points or loan fees, only 2025's share, spread evenly over the loan".
- **Source:** i1040se p. 7, Lines 12 and 13 [U, entry's quotes].
- **Residual (deferred):**
  - The gate tick "Other interest on loans for it" sits under "In 2025, did you pay …". A filer whose only interest
    item is the 2025 share of points paid earlier may not tick it.
  - `rental.amt12` (Form 1098 interest) gets no prepaid sentence.
- **Due:** transcription and render.

### BUG-0776 and BUG-0922: capitalized fees and capital purchases (rental and royalty)
- **Change: bank help only.**
  - `rental.amt10` and `royalty.amt10` (25 words each): "Not fees to defend or protect your ownership, recover the
    property, or develop or improve it: those are added to its cost, not deducted now."
  - `rental.amt19` (22): "Not something that lasts more than a year, such as an appliance, furniture or an improvement: list it
    with the buildings below."
  - `royalty.amt19` (22): "Not the value of your own work, and not something that lasts more than a year, such as equipment
    or an improvement."
- **Source:** i1040se p. 6, Line 10, "Do not deduct legal fees paid … to defend or protect title …" [C
  i1040se.cols.txt:167]; Lines 5 Through 21, "amounts paid for capital investments or capital improvements" [U].
- **Red team:**
  - "List it with the buildings" sends an appliance to `rprop.kind = personal`, which refuses. `rental.amt14`'s
    existing help does the same.
  - p527's de minimis safe harbor, under which small items may be deducted, is not mentioned. A filer who elects it is
    told to capitalize, which loses a deduction rather than overstating one [I: the safe harbor was not read].
  - `rental.amt7` is not changed. The entry names it only in parentheses, and maintenance is rarely a capital item.
- **Due:** question reviews of the four help texts. The rental and royalty forms are unchanged by this item.

### BUG-0892: sche.re_pro: which work is real estate
- **Re-verified:** the help is still "A Yes ends the interview here." [C chain questions.yaml:7267].
- **Change:** help (38 words): "Real estate work includes building, buying, renting out, managing or brokering it, including running
  your own rentals. Work as an employee counts only if you own more than 5% of the employer. A Yes ends the interview
  here."
- **Source:** i1040se p. 3, "development, redevelopment, construction, … rental, operation, management, leasing, or
  brokerage"; employee work only with "more than 5% of the stock (or … capital or profits interest)" [C
  i1040se.cols.txt:63].
- **Red team:**
  - "Own more than 5% of the employer" covers partners through "capital or profits", read loosely [I].
  - A Yes only refuses, so a wider reading is safe.
- **Due:** question review of `sche.re_pro`. This is a bank-only change, so `sche.yaml` does not change.

## Per-low entries: int-lows.patch

### BUG-0857: NY out-of-state bonds (fixed together with int-amt's gate)
- **Re-verified:** real. `ny_it201.has_tax_exempt` is `f1040.line2a > 0` [C forms/ny/2025/ny_it201.yaml:629-633].
  Line 2a is the net tax-exempt interest plus box 12 [C chain f1040.yaml:265-275]. IT-201-I: premium "is not allowed as
  a direct offset" [U, entry's quote].
- **Change:**
  - The expression becomes `any`: `f1040.tax_exempt_any = true`, or `f1040.line2a > 0`. The label says so.
  - The `any` form is already used in this file [C ny_it201.yaml:87, 118].
  - The NY help (44 words): "Most national tax-free bond funds hold other states' bonds, and part of a New York fund may too (see
    its year-end statement). Bonds of New York State, its cities and agencies, or a U.S. territory count as No. A Yes
    ends the interview here."
  - "A Yes ends the interview here" is right: line 20 refuses on this gate [C ny_it201.yaml:643-650].
- **Interaction with int-amt.**
  - Before int-amt, line 2a was the only sign of tax-exempt interest.
  - int-amt adds the plain Yes `f1040.tax_exempt_any`, asked of everyone in the `interest_dividends` group
    [C chain questions.yaml:931-936].
  - A premium bond's holder gets a Form 1099-INT box 8 with the gross interest, so they answer Yes even when the net is
    $0 [I].
  - The second operand, line 2a, keeps the exempt-interest-dividend path (box 12, where `tax_exempt_any` may be No).
- **Equivalence.** Every NY fixture with `tax_exempt_any: true` has a non-zero amount (1 case, `ny.refuse.line20`,
  50,000) [C script over the 4 NY fixture files]. The one coverage row also has 40,000 [C coverage/ny.yaml:196-203]. So
  no existing expectation moves.
- **New proof:**
  - Fixture `ny.refuse.line20_premium`: a copy of `ny.refuse.line20` with `tax_exempt_interest: 0`, expecting the same
    refusal.
  - Coverage row `ny.other_state_bonds_premium`, expecting `refused: ny_it201.gate.line20`.
  - Both are hand-predicted [I]. Before the patch, both would complete without the question.
- **Unverified [I]:**
  - That a NY form line may read a federal input directly. It already reads `f1040.line2a`, a line.
  - That the federal input is answered before the NY questions are asked. The NY order is 1010, after the federal
    topics.
- **Due:** NY transcription and render of `ny_it201.has_tax_exempt`; NY screen and false-no of `gate:ny_it201.has_tax_exempt`;
  NY `test-fixtures --ny`; `interview-coverage`.

### BUG-0832: brokered CDs; the spouse's share on a separate return
- **Re-verified:** real [C chain questions.yaml:1721-1724, 1717-1720].
- **Change:**
  - `sb.bonds_any` help (42 words): "Interest from a bank account, a fund or a certificate of deposit from your bank is not what this asks
    about; a certificate of deposit bought through a broker, or with a Form 1099-OID, counts. If you are not sure, answer
    Yes."
  - `sb.nominee` help (40): "On a joint return, an account you own with your spouse is all yours; on a separate return, your spouse's
    share is another person's. If part of what a form shows in your name is really another person's, answer Yes."
- **Red team:**
  - A bank CD holder with a Form 1099-OID is now Yes. That is right: OID adjustments are what `sb.bond_special` lists.
  - The `sb.nominee` prompt still says "for example … not your spouse". On a separate return the help now overrides
    that example. Rewording the prompt is the owner's call, because the prompt is shared by the joint path.
- **Due:** question reviews of `sb.bonds_any` and `sb.nominee` (bank only).

### BUG-0835: oil, gas or mineral interest sold
- **Change:** `sd.sold_other` help (42 words) now reads "… counts as real estate, and so does an oil, gas or mineral
  interest, such as a royalty. …".
- **Residual:** the tick ("Sold real estate or business property, or any sale paid later", 11 words) cannot take the
  words and stay under the 12-word cap, so a filer who does not open the help can still miss it.
- **Red team:** that a mineral interest is real property is [I]. A Yes only opens `sd.business_property`, which names
  the case and refuses, so a wider reading is safe.
- **Due:** question review of `sd.sold_other`.

### BUG-0509: "correcting nothing"
- **Change:**
  - `sales.aggregate_eligible` prompt (39 words): "… none of its figures needs changing …".
  - New help (12): "A corrected statement counts if none of its own figures needs changing."
- **Source:** i1040sd p. 10, lines 1a and 8a [U, entry's quote].
- **No value effect:** a No goes to the detail route, which gives the same gain [U, entry].
- **Due:** question review.

### BUG-0888: k1s.not_at_risk residual after v2 int-n10
- **Change:** prompt (42 words): "For this S corporation — Is any money or property you put into it (for shares, a loan or a
  contribution) protected from loss, or borrowed from another owner, anyone else with a stake in its business, or a
  relative of either?"
- The v2 help (C7, 37 words) stands. It names nonrecourse loans, guarantees and stop-loss, and that a bank loan does not
  count.
- **Source:** i1120ssk p. 3 [U, entry's quotes].
- **Latent** while `scope.k1` refuses. A Yes only refuses.
- **Due:** question review of `k1s.not_at_risk`.

## Deferred, with reasons

| Entry | Why deferred | Sketch for the fix lane |
|---|---|---|
| BUG-0778 Worksheet 5-1 carryover | New input and refusal: defaults, class M restatements, coverage row (M). `rental_rare` has 5 of its 6 members [C chain questions.yaml:6965-6995]. | One slot left; or a child of `rental.prior_any` ("Was any of it carried over from a year you also used it as a home?"), which refuses. |
| BUG-0779 Form 8582 exceptions 3 to 6, dealer | M. The proposed tick is far over 12 words. Dealer status belongs to the person, not the property. | Dealer: a `rental_return` box (3 of 6 used [C chain :7262-7279]). Exceptions 3 to 6: a per-rental box (the last `rental_rare` slot). The owner should pick between 0778 and 0779 for that slot. |
| BUG-0786 accrual method | M (new refusing input). | A `rental_return` box, "You keep your rental books on the accrual method". |
| BUG-0889 royalty screens | M (4 new refusals). | `royalty_rare` has 2 members [C chain :7240-7249]. Add patent or coal and iron ore, car or travel, and depreciation boxes; an at-risk child on a royalty loss. |
| BUG-0785 grouped half | No archived allocation rule. | Owner decision or source first. |
| BUG-0565 asset wording (6 items) | M; the asset form is changed by v2 sche-a only for 0790. | At asset's next change. |
| BUG-0791 asset.industry | The proposed tick is far over 12 words; the alternative adds a question for every asset. | Owner's call. |
| BUG-0891 rprop like-kind exchange | int-rprop's `rprop_facts` group is full (6 members). | A gated child beside `rprop.year`, or a 7th fact folded with `credit` (as int-rprop.md suggests). |
| BUG-0845 k1p residual | Latent; item K1 test is M. | With the K-1 integration lane. |
| BUG-0887 k1s STMT / K-3 | Latent; many tick texts. | With the K-1 integration lane. |
| BUG-0575, BUG-0829 sales bullets | Form-source bullets in `sales.yaml`, which no int patch changes, so a new transcription review would be due. | At sales.yaml's next change. |
| BUG-0831 foreign-connection gates | Four gate rewrites; `sb.trust_any` changes meaning. | Own lane; screen and false-no reviews. |
| BUG-0502 1040-NR | 2024 Form 1040-NR line 11 and line 14 equivalence not checkable; only line 15 is in i1040sd [C i1040sd.cols.txt:236]. | Archive the 2024 1040-NR, then help only. |
| BUG-0570 line 3a builder wording | `forms/2025/f1040.yaml` source text; not read in time. | With int-amt's f1040 change, if the owner wants it. |
| BUG-0812 | Its host hunk (`s1.nol_amount`) moved to inc-m12 [C sche-int.md:42-44]. | Lane A2 (lows-inc). |

## What to run (after the v2 chain, then sche-a-lows, then int-lows)

1. Build. Then `render` and `render --check` for rental and NY IT-201. Then `tools/citations.py` (the three new
   locators and the p527 cite).
2. `test-fixtures`, federal and `--ny`. The new `ny.refuse.line20_premium` should refuse at line 20. No other
   expectation should move.
3. `tick-groups` for `rental_rare`, `rental_costs_a` and `rental_return` (tick text changed).
4. `interview-coverage --write` (the new NY row), then `draft-walk` for the rental persona (19) and persona 21.
5. `interview-rules`, `interview-order`, then `tools/check_all.sh` in the lane worktree.

## Reviews made due (one per form per round, after all of the round's fixes to that form have landed)

- **rental:** transcription and render, line-scoped, for services, under_tenth, part_home, prior_any,
  prior_not_active, days_personal, amt9, amt12, amt13 and the three cites. Screen and false-no samples for
  `rental.services`, `rental.under_tenth`, `rental.part_home`, `gate:rental.prior_any`, `gate:rental.has_insurance`.
  These ride sche-a's rental round.
- **Question reviews (bank):**
  - The rental inputs above, plus `rental.amt10` and `rental.amt19`.
  - `royalty.amt10`, `royalty.amt19`.
  - `sche.re_pro`.
  - `sb.bonds_any`, `sb.nominee`, `sd.sold_other`.
  - `sales.aggregate_eligible`.
  - `k1s.not_at_risk`.
- **NY:** transcription and render of `ny_it201.has_tax_exempt`; screen and false-no of
  `gate:ny_it201.has_tax_exempt`; question review of `ny_it201.ask.out_of_state_bond_interest`.

## Files

- Patches:
  - `patches/v3/sche-a-lows.patch`, 228 lines.
  - `patches/v3/int-lows.patch`.
- Edit scripts: `scratch/round4-lows-sche/edit_sche_lows.py` and `edit_int_lows.py` (argument: the root of a
  scratch copy).
- Scratch trees:
  - `a`, `b1`: the base and result for sche-a-lows.
  - `a2`, `b2`: the base and result for int-lows.
  - `tA`, `tB`: the two apply orders.
  - `tC`, `tD`: the direct-after-own-patch checks, which fail as expected.
