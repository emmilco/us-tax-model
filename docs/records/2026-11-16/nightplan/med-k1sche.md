# Fix plan: open MEDIUM entries, K-1 / Schedule E / rental / royalty / depreciation (lane plan-med-k1sche)

Lane plan-med-k1sche. Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Written 2026-11-15.
Read only; nothing in the repository was changed. No engine, fixture or check runs were made: every "witness" value
below is the entry's own figure, not reproduced here. Tags: **[C path:line]** = checked against that file;
**[I]** = inferred.
Paths are relative to the xint worktree `/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/xint`.

## Summary

Status per `tools/bug_status.py` (run in xint, read-only):

| Old name | BUG | Status | Live or latent | Verdict | Origin | Effort |
|---|---|---|---|---|---|---|
| xrelbiz-01 | BUG-0775 | open | LIVE (rentals in scope) | confirmed | tonight (regression of tonight's BUG-0918 fix) | S (wording) / M (new input) |
| xrelbiz-15 | BUG-0789 | open | LIVE | confirmed | tonight (rental form new) | S |
| xrelbiz-16 | BUG-0790 | open | LIVE, **also on main** | confirmed | interview redraft (a2f24909, 2026-11-13) | S |
| xrelk1p-01 | BUG-0836 | open | LIVE (MFS + rental loss) | confirmed | tonight (f8582 new; MFS opened tonight) | S |
| xrelk1p-02 | BUG-0837 | open | latent (scope.k1 refuses) | confirmed | tonight (k1p new) | S |
| xrelk1p-03 | BUG-0838 | open | latent | confirmed | tonight | S |
| xrelk1p-06 | BUG-0841 | open | latent | confirmed | tonight | M (refusals) / L (build) |
| xrelk1p-07 | BUG-0842 | open | latent | confirmed (as "not yet encoded") | tonight; belongs to K-1 integration | S-M inside integration lane |
| xrelk1p-08 | BUG-0843 | open | latent | confirmed | tonight | S-M |
| xrelsche-01 | BUG-0882 | open | latent | confirmed, plus a missing k1s trading screen | tonight (k1s new) | S-M |
| xrelsche-04 | BUG-0885 | open | latent | confirmed | tonight; integration | with 0842 |
| xrelsche-05 | BUG-0886 | open | latent | confirmed | tonight | S |
| xrelsche-09 | BUG-0890 | open | LIVE | confirmed | tonight (royalty new) | S |
| xrev-01 | BUG-0911 | tool says open, **actually fixed** | — | fix is in the tree | — | bookkeeping only |
| xrevsche-02 | BUG-0919 | **fixed** | — | — | — | none |
| (extra) | BUG-0907 | open | LIVE | wording gap (scope.nol help omits rental/K-1/EBL) | tonight | S |

Headlines:
1. **Five live defects** change a return today: 0775, 0789, 0836, 0890 (rental/f8582/royalty, all new tonight) and 0790
   (asset.listed prompt, from the 2026-11-13 redraft, so also live on `main`). All are S-sized; 0836 is the only one that
   changes arithmetic.
2. **Eight K-1 entries are latent**: `scope.k1` still refuses every K-1, and no form outside `person.yaml` reads any
   `person.k1p_total_*` or `person.k1s_total_*` [C: grep over forms/2025, only person.yaml hits]. They change no return
   now; they must be fixed before the integration lane lifts `scope.k1`.
3. **0842 and 0885 are integration work, not defects of a form**: the EBL and k1p QBI pieces are already specified in
   `docs/provisional/lanes/x2-k1p_work/k1-wiring-k1p.md:61-65` and
   `docs/provisional/lanes/x2-k1e_work/k1-integration-plan.md:52,72` [C]. Tonight-safe action is none (scope.k1 already
   refuses); they should be done by the integration lane. Sibling not in any entry: `k1s.qbi` is "before the passive
   activity limitation" [C forms/2025/k1s.yaml:2608-2611], the same suspended-loss QBI gap as k1p.
4. **BUG-0911 is fixed in the tree** (k1p.box9b is `Dollars`, signed wording [C forms/2025/k1p.yaml:613-621];
   person.k1p_total_collectibles Dollars [C forms/2025/person.yaml:7689-7692]). `bug_status.py` reports it open because
   the entry's first `**Fix:**` field is the reviewer's proposal; rename that field to `**Proposed fix (review):**` (as
   BUG-0919 does). BUG-0919 is fixed; nothing to do.
5. New sibling defects found while checking: `k1s` has **no trading screen** (k1p has `k1p.trader_if_b1`); the rental
   `rental.amt16` help ("Leave these taxes out of the taxes you deduct for your own home") has the same converted-home
   problem as `rental.amt12` (0775); `rental.amt17` says "Utilities **you** paid" (0789).

Owner decisions needed (detail at the end): (D1) 0775 wording vs refusal vs new input; (D2) 0841 refuse vs build;
(D3) whether to fix latent K-1 entries now or hand them to the integration lane; (D4) whether 0790 is fixed on `main`
as well; (D5) accept the sampled-review cost that heading and gate-wording changes make due before release.

---

## Detail per entry

### BUG-0775 (xrelbiz-01): converted-to-rental home deducts the full year's costs

1. **Defect.** A home that was the filer's main home for part of 2025 and then rented deducts the whole year's
   insurance, taxes and mortgage interest, because the main-home days are excluded from `rental.days_personal` (correct
   for the home test) and so also from the expense division, and the cost questions ask the full 2025 amount.
   - **Confirmed.** `rental.days_personal` source: "Leave out ... days it was your main home before or after renting it out
     (or trying to) for 12 months or more in a row" [C forms/2025/rental.yaml, input list]; the division total
     `rental.total_c` is use days less overlap [C forms/2025/rental.yaml:230-238]; `rental.amt12` help "Leave this
     mortgage out of your home mortgage interest" [C interview/2025/questions.yaml:7074]; `rental.amt16` help "Leave these
     taxes out of the taxes you deduct for your own home" [C interview/2025/questions.yaml:7088] (sibling the entry does
     not name).
   - Source: p527 "However, this special rule doesn't apply when dividing expenses ... See Property Changed to Rental
     Use"; "You can deduct as rental expenses only the part of the expense that is for the part of the year the property
     was used or held for rental purposes. You can't deduct depreciation or insurance for the part of the year the
     property was held for personal use. However, you can include the home mortgage interest and real estate tax
     expenses for the part of the year the property was held for personal use" on Schedule A [C sources/2025/p527.cols.txt,
     grep].
2. **Origin.** Tonight: regression of tonight's BUG-0918 wording fix (lane xfix). rental.yaml is not on `main`.
3. **Failure mode.** Wrong return on correct answers (filer answers every question truthfully). Live.
4. **Fix.**
   - **Recommended (wording, S).** No arithmetic change; the source divides converted property by the part of the year
     held for rent, which a days input would not reproduce (vacant-but-offered days count as held for rent). In
     `interview/2025/questions.yaml`:
     - group headings `rental_costs_a/b` get a help or the first cost question a frame: "If it was your home for part
       of 2025 and you then rented it or offered it for rent, enter for each yearly cost (insurance, taxes, mortgage
       interest, and so on) only the part for the time from when you first rented it or offered it for rent."
     - `rental.amt12` help: "Only the interest on this property for the time in 2025 it was rented or offered for rent,
       your share. Interest for the time it was your home goes with your home mortgage interest."
     - `rental.amt16` help: "Only the tax for the time in 2025 it was rented or offered for rent. Tax for the time it was
       your home goes with the taxes on your own home."
     - `rental.amt9` source already says "(the part for 2025)"; add "(the part for the time it was rented or offered for
       rent)" only if the frame is not used.
     - Counterpart (other form, optional, coordinate with the Schedule A owner): `sa.mortgage_interest` help "If a home
       became a rental in 2025, count only the interest for the time it was your home." Without it a filer may leave the
       personal months' interest off Schedule A (understates a deduction; not an overstatement).
   - **Tonight-safe refusal (alternative).** A tick in `rental_rare` ("It was your main home at some time in 2025") as new
     input `rental.home_part_year` refusing at `rental.line21` (the same place `rental.part_home` refuses; BUG-0920 fix
     pattern), cite p527 Property Changed to Rental Use. Refuses a common case; not recommended unless the wording is
     judged too hard to answer.
   - **Alternative build (M).** New Count input `rental.days_home` (main-home days in 2025) added into the division total
     but not into the home test. Arithmetic change; departs from the p527 "part of the year held for rental" rule.
     Not recommended.
5. **Fixtures.** New `rental.json` case: June 1 conversion (days_fair 214, personal_any false, costs entered for 7/12):
   insurance 233.33-style values; the expected values follow from the entered amounts (the fix is wording, so the case
   pins the frame's intended reading). Siblings: `rental.amt9`, `rental.amt16`, `rprop.month` (depreciation already
   starts at placed-in-service month [I]). **Reviews due:** question review for each input whose help or prompt changes
   (amt12, amt16, the first cost item if framed); render line-scoped only if a form source changes (amt9); no
   transcription, no class M (no arithmetic). If headings change, the screen and false-no subjects of the `has_*` gates
   change (see 0789: do both in one edit so the subjects change once).
6. **Effort** S. Do together with 0789 (same headings).

### BUG-0789 (xrelbiz-15): expenses a tenant paid are counted in rent but not asked as expenses

1. **Defect.** `rental.rents` includes expenses a tenant paid, but the cost ticks ask "Did you pay any of these ...",
   so the tenant-paid expense is taxed as rent and not deducted.
   - **Confirmed.** Headings "Did you pay any of these for this rental in 2025?", "Did you pay any of these for it in
     2025?", "And did you pay either of these for it?" [C interview/2025/questions.yaml:162-167]; rents help names
     "repairs a tenant paid for in place of rent" [C questions.yaml:6981]; `rental.amt17` source "Utilities **you** paid,
     paid in 2025" [C rental.yaml input list]. Source p527 Expenses paid by tenant: "Because you must include this amount
     in income, you can also deduct the expenses if they are deductible rental expenses" [C p527.cols.txt].
2. **Origin.** Tonight (rental form new).
3. **Failure mode.** Wrong return on a correct, literal answer (the filer did not pay). Live.
4. **Fix (wording, S).**
   - Headings: "Did you, or a tenant for you, pay any of these for this rental in 2025?"; "... for it in 2025?";
     "And did you, or a tenant for you, pay either of these for it?"
   - `rental.rents` help: append "Then enter what the tenant paid as an expense below."
   - `rental.amt17` source: "Utilities for it, paid in 2025 (by you, or by a tenant in place of rent)".
   - The other amount sources say "paid in 2025" (no "you"); leave them.
5. **Fixtures.** One case: rent 12,000 including a 600 repair the tenant paid; has_repairs true, amt14 600 (pins the
   reading). **Reviews due:** render line-scoped on `rental.amt17`; question review for `rental.rents` (help) and the
   tick inputs whose heading changed; screen and false-no subjects of the `rental.has_*` gates change (about 13 gates:
   at the release gate each needs its sample again; estimate before running, $3.00 gate). No transcription or class M.
6. **Effort** S. Dependency: same headings as 0775; one lane, one edit.

### BUG-0790 (xrelbiz-16): asset.listed prompt narrows listed property

1. **Defect.** The redraft prompt asks about "equipment ... such as a camera, or sound or video recording equipment",
   dropping "communication" and anything not "equipment", so a boat or communication equipment used 50% or less is
   depreciated instead of refused.
   - **Confirmed.** Prompt [C interview/2025/questions.yaml:5603-5610]; encoded source keeps "photographic,
     phonographic, communication or video recording equipment" [C forms/2025/asset.yaml:1071-1075]; same prompt on
     `main` [C main interview/2025/questions.yaml:4696-4703]. Class 00.28 vessels is offered [C
     tables/2025/class_lives.yaml:31]; `asset.kind_excluded` names "a vehicle, an aircraft" but not a boat [C
     asset.yaml:142]. Witness ($4,000 vs refusal) not reproduced (no engine runs).
   - Source: i4562 Listed Property: "Any other property used for transportation if the nature of the property lends
     itself to personal use, such as motorcycles, pickup trucks, SUVs, aircraft, etc." and "Any property used for
     entertainment or recreational purposes (such as photographic, phonographic, communication, and video recording
     equipment)" [C i4562.cols.txt]; p946: "Other property used for transportation includes trucks, buses, boats,
     airplanes, motorcycles" [C p946.cols.txt]. Note: a boat is listed as **transportation** property, so the entry's
     "or a boat" belongs to the transportation limb, not the entertainment one.
2. **Origin.** Today's interview redraft (landed a2f24909). Live on `main` and in xint.
3. **Failure mode.** Wrong return on a correct answer to the prompt as worded.
4. **Fix (wording, S).** Prompt: "For this property — Is it property of a kind used for entertainment or recreation
   (such as photographic, phonographic, communication or video recording equipment) that is not used only in your
   business or at your regular place of business, or a boat or other property used for transportation? Also answer Yes
   for a computer you began using before 2018 that is not used only at your regular place of business." Keep the help.
   Optionally align `asset.listed` source in asset.yaml with "or other property used for transportation (such as a
   boat)"; that is a form-source change (render line-scoped). Alternative: add "a boat" to `asset.kind_excluded`
   (refuses every boat; simpler and safe, but refuses a boat used over 50% that the form supports) [I].
5. **Fixtures.** `asset.json`: class c00_28, pct 40, listed true → refuses (`asset.listed_low`). Siblings:
   `asset.qbu_low_if_listed`, `asset.kind_excluded`. **Reviews due:** question review of `asset.listed` (the entry asks
   for it); screen and false-no `gate:asset.listed` subjects change; render only if the asset.yaml source changes.
6. **Effort** S. Independent. Owner decision D4: also land on `main` or only via the xint candidate.

### BUG-0836 (xrelk1p-01): MFS lived together gets the $12,500 allowance and the filing exception

1. **Defect.** Form 8582 gives an MFS filer who lived with the spouse the Part II special allowance and the filing
   exception.
   - **Confirmed.** `f8582.line5`, `f8582.max8` read status-keyed params (mfs 75,000 / 12,500) [C
     forms/2025/f8582.yaml:375-385, 462-471; params/2025.yaml:2801-2822]; `f8582.exception` tests only loss and MAGI
     [C f8582.yaml:579-610]; no `mfs_living` reference in f8582, rental or sche [C grep]. MFS is not refused by scope [C
     forms/2025/scope.yaml grep]. Rental reads `f8582.line9` directly for Part VI [C rental.yaml:1830-1855], so line 9
     is the operative fix point. Source i8582 Part II caution: "If your filing status is married filing separately and
     you lived with your spouse at any time during the year, you are not eligible for the special allowances in Part
     II. Do not complete Part II" [C i8582.cols.txt].
2. **Origin.** Tonight (f8582 new; MFS opened tonight).
3. **Failure mode.** Wrong return on correct answers. Live.
4. **Fix (arithmetic, S).**
   - New helper `f8582.mfs_together` (Bool): `all[ household.mfs eq true, household.mfs_apart_all_year eq false ]`
     (reuses the existing helper [C forms/2025/household.yaml:1723-1735]); cite i8582 p. 10 caution.
   - `f8582.line9`: `choose[ mfs_together → f8582.zero ; else smaller_of(line4, line8) ]` (move the current expr to a
     helper `f8582.line9_calc` or inline the choose).
   - `f8582.exception`: add `op: test eq [f8582.mfs_together, const: false]`; cite i8582 p. 1, Exception, "If you're
     married filing separately, you lived apart from your spouse all year".
   - Keep the mfs params (they apply to apart_all_year).
5. **Fixtures** (`rental.json`, from x1sche.f2.small_loss_exception): status mfs + together_late → `f8582.line9` 0,
   `f8582.required` true, `rental[a].line22` 0, AGI 50,000; apart_last6 → same as together_late; apart_all_year →
   exception holds (loss 213.20 ≤ 12,500, MAGI ≤ 50,000), line 9 213.20. Siblings: `rental.p6_on`, `rental.p6c_share`,
   `rental.p7a` (readers; values follow), k1p/k1s Part IV rows when integrated (they will read the same line 9).
   **Reviews due:** transcription line-scoped (f8582.line9, f8582.exception, new helper), class M f8582, render for the
   changed lines.
6. **Effort** S. Independent.

### BUG-0837 (xrelk1p-02): tests 5 and 6 never asked of a partner who did no work in 2025

1. **Defect.** `k1p.ask_five` requires `k1p.under500`, which requires `work_if_b1` true, so a non-working partner is never
   asked tests 5 and 6.
   - **Confirmed** [C forms/2025/k1p.yaml:1035-1053 (under500), 1156-1178 (ask_five), 1209-1224 (ask_other)].
     Source i1065sk1 p. 9 tests 5, 6 and "Limited partners ... must meet item 1, 5, or 6" [C i1065sk1.cols.txt]. k1s
     already does this right: `k1s.past_ask = box1_any ∧ ¬mp_now` [C k1s.yaml:1150-1165].
2. **Origin.** Tonight (k1p new). 3. **Failure mode.** Wrong result on correct answers; latent.
4. **Fix (gate, S).** `k1p.ask_five` := `all[ has_b1 = true, hours500_if_work = false, most_hours_if_gp = false,
   nearly_all_if_asked = false ]`, label "Box 1 shows an amount and tests 1 to 3 are not met". Also add
   `k1p.work_if_b1 = true` to `k1p.ask_other_gp` [C k1p.yaml:1258-1273]: tests 4 and 7 need 2025 work (">100 hours"),
   so without it a non-working general partner would be asked two pointless questions. `k1p.t6` then follows through
   `ask_other` (test 6 needs no 2025 work). Check the `k1p_part_other` heading "Is any of these true of your work in
   this business?" [C questions.yaml:141-142] still reads well when only t6 is shown.
5. **Fixtures.** `x2k1p.retired_test5`: work false, five_of_ten true → material true, col_k 40,000 (entry's base case).
   `x2k1p.retired_t6_refuses`: work false, five_of_ten false, t6 true → refusal. **Reviews due:** transcription
   line-scoped (ask_five, ask_other_gp), class M k1p, interview coverage rows (gating changes); render for the two
   labels.
6. **Effort** S. Same lane as 0838/0841/0843 (all k1p).

### BUG-0838 (xrelk1p-03) and BUG-0886 (xrelsche-05): spouse counted only on a joint return

1. **Defect.** Participation questions say "(or, on a joint return, your spouse)"; spouse work counts on any return.
   - **Confirmed.** k1p.work, most_hours, nearly_all, decisions, tenth [C k1p.yaml:977, 1079, 1132, 1389, 1422];
     k1p.hours500 help "on a joint return, your spouse's hours" [C questions.yaml:431]; k1p.five_of_ten, t6, t4, t7 name
     only "you" [C k1p.yaml:1185, 1229-1230, 1278, 1311]. k1s.work, hours500, most_hours, past_years, active, tenth
     [C k1s.yaml:1027, 1060, 1108, 1174, 1283, 1317]; k1s.mp_other only "you" [C k1s.yaml:1214]. Source i8582 p. 5
     "whether or not you and your spouse file a joint return"; i1065sk1 p. 9 / i1120ssk p. 4 "you or your spouse".
2. **Origin.** Tonight. 3. **Failure mode.** Wrong result on a correct reading by an MFS filer; latent.
4. **Fix (wording, S each).** Replace "(or, on a joint return, your spouse)" / "(and, on a joint return, your
   spouse)" with "(or your spouse, whether or not you file jointly)" / "(and your spouse, whether or not you file
   jointly)"; k1p.hours500 help "Count your own hours and your spouse's hours in it together, whether or not you file
   jointly." Add "(or your spouse)" to k1p.five_of_ten, t6, t4, t7 and k1s.mp_other. Do not touch `scope.k1`'s own
   "(or, on a joint return, your spouse)" (household scope, correct).
5. **Fixtures.** None needed (wording). **Reviews due:** render line-scoped on each changed source; question review
   for the changed inputs; screen/false-no subjects of the gated questions change.
6. **Effort** S each. 0838 in the k1p lane, 0886 in the k1s lane.

### BUG-0841 (xrelk1p-06): no screen for the partner's own Schedule E items

1. **Defect.** No k1p question about basis or at-risk carryovers, unreimbursed partnership expenses (UPE), interest to
   buy the interest, or a 2024 fuel tax credit.
   - **Confirmed.** k1p has `k1p.prior_any` (passive carryover only) [C k1p.yaml:1490-1499] and `k1p.basis_short`
     (2025 only) [C k1p.yaml:1798-1810]; k1s has `k1s.basis_carry`, `k1s.risk_carry` refusing at `k1s.ok` [C
     k1s.yaml:1373-1395, 1838-1851]. i1040se: "You can deduct unreimbursed ordinary and necessary expenses you paid on
     behalf of the partnership if you were required to pay these expenses under the partnership agreement" [C
     i1040se.cols.txt].
2. **Origin.** Tonight (scout R-K5 listed them; not encoded). 3. **Failure mode.** Wrong return on correct answers
   (no question to answer); latent.
4. **Fix.**
   - **Tonight-safe refusal (M, recommended).** Five Bool inputs, ungated like k1s, as ticks in a new group
     `k1p_own` (heading "Is any of these true for this partnership?") or in `k1p_facts`:
     `k1p.basis_carry` "A loss from it was held back on an earlier return because your basis was too low";
     `k1p.risk_carry` "A loss from it was held back on an earlier return by the at-risk rules (Form 6198)";
     `k1p.upe` "You paid expenses of the partnership yourself that the partnership agreement required you to pay";
     `k1p.interest_buy` "You paid interest on money you borrowed to buy your share or put money into it";
     `k1p.fuel_2024` "Your 2024 return claimed a fuel tax credit from it".
     Each refuses at `k1p.screened` with a cited remedy (i1065sk1 p. 13 basis/at-risk; i1040se p. 9 UPE and loan
     interest, p. 10 prior-year unallowed, p. 9 fuel credit). Defaults false in `fixtures/2025/defaults.json`.
   - **Real build (L, not recommended now).** UPE and acquisition interest as separate Schedule E line 28 rows with
     their own passive/nonpassive status, box 14 A reduced by UPE for SE, basis/at-risk carryovers via Form 6198 and a
     partner basis worksheet. Several forms; needs the integration lane first.
5. **Fixtures.** Five `x2k1p.refuse_*` cases (one per tick). Sibling: k1s has no UPE analogue in the source, but
   acquisition-interest for S stock is the same Schedule E rule [I]; check whether k1s needs an `interest_buy` tick.
   **Reviews due:** transcription line-scoped (k1p.screened refusals, new inputs), render (new lines), coverage rows for
   each refusal; class M not needed for refusals only [I: per charter "when arithmetic changes"].
6. **Effort** M. Dependency: owner decision D2.

### BUG-0842 (xrelk1p-07) and BUG-0885 (xrelsche-04): EBL and suspended-loss QBI not applied to K-1 amounts

1. **Defect.** `s1.ebl_total` = Schedules C + Schedule E Part I only [C forms/2025/s1.yaml:210-222]; no `k1p.qbi`
   exists (person.k1p_total_qbi_stmt is box 20 Z as stated) [C person.yaml:7755]. **Confirmed as "specified but not
   encoded"**: the wiring contract specifies both [C docs/provisional/lanes/x2-k1p_work/k1-wiring-k1p.md:61-65] and the
   integration plan lists `s1.ebl_total + Σ k1p.ebl_part + Σ k1s.ebl_part` [C
   docs/provisional/lanes/x2-k1e_work/k1-integration-plan.md:52]. Sibling not in any entry: `k1s.qbi` is labelled
   "before the passive activity limitation" and only refuses the basis cut [C k1s.yaml:2587-2633]; the same
   suspended-passive-loss QBI exclusion (i8995 p. 3) is missing for k1s.
2. **Origin.** Tonight; by design deferred to integration. 3. **Failure mode.** Wrong return on correct answers once
   scope.k1 is lifted; latent now.
4. **Fix.** **Tonight-safe:** none needed; `scope.k1` refuses every K-1. Record in the integration plan that lifting
   scope.k1 is blocked on both (already stated in the entries). **Real build (S-M inside the integration lane):**
   `k1p.ebl_part` = −(col_i + allowed passive box 1 loss) + nonpassive/passive box 1 income (signed net of box 1 as
   allowed), likewise `k1s.ebl_part`; add `sum_over person` of both to `s1.ebl_total`. Conservative variant matching
   the existing Part I approach (`amb.2025.s1_ebl_rental`, pre-limit loss): add signed box 1 before the passive limit;
   over-refuses only. `k1p.qbi` per wiring line 61-64 (prorate of box 20 Z by the allowed share of the box 1 loss);
   `k1s.qbi` the same prorate for a passive box 1 loss.
5. **Fixtures.** In the integration lane: a K-1 box 1 loss pushing the total over $313,000 → `s1.ebl` refusal; a
   passive box 1 loss partly held back → QBI prorated. **Reviews due:** transcription + class M of s1, k1p, k1s
   (arithmetic).
6. **Effort** S-M, but only inside the integration lane. Owner decision D3: leave open with tag "blocked: K-1
   integration", or convert to tasks.

### BUG-0843 (xrelk1p-08) and BUG-0882 (xrelsche-01): box 2 (and box 3) always passive

1. **Defect.** A real estate professional who materially participates, or a dwelling a partner/shareholder used
   personally more than the greater of 14 days or 10% of fair-rental days, is nonpassive; the K-1 forms treat box 2
   (and box 3) as passive regardless. k1s also lacks any trading screen.
   - **Confirmed.** `sche.re_pro` is read only by `sche.line26`'s refusal [C forms/2025/sche.yaml:19-29, 231]; no
     `re_pro`/dwelling input in k1p or k1s, and no trading input in k1s [C grep "trad|re_pro|dwelling" over k1p, k1s;
     k1p has `k1p.trader` at k1p.yaml:939-950]. Sources: i1065sk1 p. 14 "the income (loss) in box 2 isn't from a passive
     activity if you were a real estate professional ... and you materially participated"; i1065sk1 p. 11 item 4 and
     i1120ssk p. 5 item 3 (dwelling), i1120ssk item 4 "Activities of trading personal property for the account of
     owners" [C cols.txt].
   - Note: `sche.re_pro` is asked in the rental topic's `rental_return` group [C questions.yaml:7226-7231], so a K-1-only
     filer is never asked it [I: topic gating not traced]. The K-1 forms need their own question.
2. **Origin.** Tonight. 3. **Failure mode.** Wrong result on correct answers; latent.
4. **Fix (refusals, S-M).**
   - k1p: `k1p.re_pro` (gated on `k1p.has_b2`): "Did you (or your spouse) work more than 750 hours in 2025 in real estate
     businesses, and more than half of all your work time?" (same wording as `sche.re_pro`); `k1p.dwelling` (gated on
     has_b2 or has_b3): "Did you or another partner use a home in this rental for personal purposes in 2025 for more
     than 14 days and more than a tenth of the days it was rented at a fair price?" Both refuse at `k1p.screened`.
     Refusing every real estate professional with box 2 (not only those who materially participate) is conservative and
     matches Schedule E Part I.
   - k1s: `k1s.re_pro` and `k1s.dwelling` likewise (gated on `k1s.box2_any`, and box3 for dwelling); `k1s.trader` gated on
     `k1s.box1_any`, mirroring `k1p.trader`. Refuse at `k1s.ok`.
   - Alternative: one return-level `sche.re_pro` asked when scope.rental or any K-1 box 2 (cross-form gate; the
     integration lane could do this). Not tonight.
5. **Fixtures.** `x2k1p.refuse_re_pro`, `x2k1p.refuse_dwelling`; `k1s.refuse_re_pro`, `k1s.refuse_dwelling`,
   `k1s.refuse_trader`; adjust `x2k1p.fk3_limited_rental_loss` only if its defaults change. Defaults false for new
   inputs. **Reviews due:** transcription line-scoped (refusals), render (new lines), coverage rows.
6. **Effort** S-M per form. k1p part in the k1p lane, k1s part in the k1s lane.

### BUG-0890 (xrelsche-09): royalty taxes withheld answered No

1. **Defect.** `royalty.expenses_any` "Did you pay any costs for it, such as fees, taxes or production costs?" — a payer
   withholding severance tax from a gross line 4 reads as No, so line 16 is zero.
   - **Confirmed** [C royalty.yaml input list: expenses_any, line4 "before any taxes the payer withheld", amt16 "including
     any the payer withheld"]; no interview override [C questions.yaml:7214-7216]. Source i1040se line 4 "Enter ... the
     gross amount ... even if state or local taxes were withheld ... Include taxes withheld by the producer on line 16"
     [C i1040se.cols.txt].
2. **Origin.** Tonight (and made live by tonight's BUG-0921 fix making line 4 gross).
3. **Failure mode.** Wrong return on a literal correct answer. Live.
4. **Fix (wording, S).** `royalty.expenses_any` source: "Did you pay any costs for it, or did the payer take any out of
   your payments (such as fees, severance or production taxes, or production costs)?"; `royalty.amt19` source:
   "Other costs of it (not depletion), paid in 2025 or taken out of your payments; zero if none".
5. **Fixtures.** `rental.json`: royalty 10,000 gross, 500 withheld, expenses_any true, amt16 500 → line 21 9,500.
   **Reviews due:** render line-scoped (expenses_any, amt19); screen and false-no `gate:royalty.expenses_any` subjects
   change; question review for both.
6. **Effort** S.

### BUG-0907 (extra, open medium, adjacent): scope.nol help omits rental, K-1 and EBL carryovers

Confirmed wording [C interview/2025/questions.yaml:2066-2071: "A loss bigger than that year's income, carried forward
on an earlier return. It can come from a business, or from a disaster or theft with no business."]. Origin tonight
(expansion review). Live. Fix: the entry's help text. Reviews: question review of scope.nol; screen/false-no
`gate:scope.nol` subjects change. Effort S. Put it in lane A (it is interview help only; no form overlap).

### BUG-0911, BUG-0919

0911: fixed in the tree (see summary item 4); only the inventory field name needs correcting so `bug_status.py`
reports it fixed. 0919: fixed (`rprop.screen` QIP item, fixture `xfix.r11.qip_screen`); nothing to do.

---

## Proposed lane split

All lanes read `docs/2026-11-13_interview_construction_protocol.md` before changing any question (normative), claim
forms with `tools/claims.py`, run each form's reviews once after all its fixes land (one review per form per round),
and log costs. `interview/2025/questions.yaml` is shared: each lane edits only its own entries; merge order below avoids
conflicts in the same hunks.

| Lane | Forms claimed | Entries | Live? | Model / class | Effort |
|---|---|---|---|---|---|
| A: rental-live | rental, f8582, royalty, asset, (scope help only) | 0775, 0789, 0836, 0890, 0790, 0907 | yes | Opus, judgment (0775 wording, 0790 limb choice) | ~3-4 h incl. reviews |
| B: k1p | k1p | 0837, 0838 (k1p part), 0841 (refusals), 0843 (k1p part) | latent | Opus, judgment (refusal wording, gate) | ~3 h |
| C: k1s | k1s | 0886, 0882 (k1s part + trader sibling) | latent | Sonnet, mechanical (mirrors lane B's patterns) or Opus | ~2 h |
| D: integration (existing plan) | s1, sche, person, k1p/k1s qbi | 0842, 0885, k1s.qbi sibling | latent | as the integration lane is briefed | inside that lane |
| Bookkeeping | BUG_INVENTORY.md | 0911 field rename | — | Sonnet, mechanical | minutes |

Order: A first (live; release-relevant). B and C in parallel with A (disjoint forms); C can start from B's drafted
wording for the shared patterns (spouse wording, re_pro/dwelling ticks) or simply copy the sketches above. D waits for
the integration lane; it must land before `scope.k1` is lifted.

Review cost note: lane A changes the prompts of about 15 screened gates (rental cost headings, royalty.expenses_any,
asset.listed, scope.nol). Each changed screen/false-no subject is due again at the release gate
(`tools/release_reviews.sh`). Estimate with the review tools' dry estimate before running; runs above $3.00 need
`--approve-cost`.

## Owner decisions needed

- **D1 (BUG-0775).** A home converted to a rental in 2025: fix by wording (cost questions ask only the part of each
  yearly cost for the time it was rented or offered for rent; recommended, matches p527), by refusing any rental that
  was the filer's main home during 2025 (safe, but refuses a common case), or by a new main-home-days input in the
  expense division (arithmetic change; does not match p527's "held for rental" rule)?
- **D2 (BUG-0841).** A partner's own Schedule E items (basis or at-risk carryover, unreimbursed partnership expenses,
  interest on money borrowed to buy the share, a 2024 fuel credit): refuse now with five ticks (recommended, M), or
  build them (L, after K-1 integration)?
- **D3 (latent K-1 entries).** `scope.k1` refuses every K-1 today, so 0837, 0838, 0841, 0843, 0882, 0886 change no
  return. Fix them now in lanes B and C (recommended: cheap, and they must be right before integration), or hand them to
  the integration lane? And 0842/0885: keep open tagged "blocked by K-1 integration", or convert to tasks?
- **D4 (BUG-0790).** The narrowed listed-property prompt is live on `main` too. Fix on `main` now, or only through the
  xint candidate when it lands? And name a boat in the listed question (recommended) or refuse boats outright in
  `asset.kind_excluded`?
- **D5 (review spend).** Accept that the wording fixes in lane A make roughly 15 screen/false-no subjects due before the
  next release.
