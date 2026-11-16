# Lane v2-sche-int: corrected v2 of sche-a and the five int-* patches

claude-opus-5-5, judgment, year 2025, jurisdiction us. Written 2026-11-16. Read only on xint. Edits made on copies in
`/tmp/nightplan/scratch/v2-sche-int/<lane>/{a,b}`, with patches made by `git diff --no-index` (prefixes rewritten).
Edit scripts: `/tmp/nightplan/scratch/v2-sche-int/edit_sche_a.py`, `edit_sche_a_fixtures.py`, `edit_int_n10.py`.
**[C path:line]** = checked against that file this session (xint paths unless stated). **[I]** = inferred, not run.
No engine, build, walk, test or model call was run.

## Summary

- **Six v2 patches** in `/tmp/nightplan/patches/v2/`: `sche-a.patch`, `int-amt.patch`, `int-p18.patch`,
  `int-personas.patch`, `int-n10.patch`, `int-n10-ticks.patch`. int-p18 and int-personas are byte-identical to round 2
  apart from the `index` lines, because the red team found nothing to change in them (its section E lists both as sound).
- **Apply checks.**
  - `git apply --check` succeeds for each patch alone against xint [C].
  - **Combined, in this order:** sche-a, int-amt, int-p18, int-personas, int-n10, int-n10-ticks. All six applied with
    `patch -p1 -F0` (no fuzz) in sequence to a scratch copy of the 43 files they touch
    (`/tmp/nightplan/scratch/v2-sche-int/combined`) [C]. Every changed YAML and JSON file parses, and the combined bank
    has no duplicate mapping key (strict loader) [C].
  - **Caution about the multi-patch `git apply --check`.** It also passes for the six together, but it passed for the
    round-2 set as well. Applying round-2 sche-a and then round-2 int-n10 in sequence fails 1 of 10 hunks [C]. So the
    multi-patch `git apply --check` did not catch that conflict. Only the sequential scratch application is evidence
    for the combined order.
- **The merge conflict is resolved.** int-n10 no longer adds a bank `prompt:` to `rental.not_at_risk`, so sche-a's
  three-class form source and help are what the filer sees [C combined questions.yaml:7223-7227].
- **The fixture values.** I re-derived all six sche-a hand-predicted values from the form expressions and got the
  same numbers for every asserted line (table below). I added one case: the reverse conversion that red-team A1 asked
  for.
- **One correction to the red team (it changes a value).** A1's frame read literally ("enter only the part for the
  days in 2025 it was rented") divides the costs twice in A1's own reverse case. The form already divides by days of
  use whenever personal-use days are counted [C forms/2025/rental.yaml:736-766]. The v2 frame applies only when the
  main-home days were **not** counted. The new fixture pins that reading.
- **N10 overruns introduced (owner's call):**
  - `sa.mortgage_interest` help is 78 words (it was 46);
  - `rental.amt12` and `rental.amt16` help are 49 each;
  - `sa.line5b` help is 52;
  - `rprop.basis` prompt is 44 (C5 verbatim);
  - `scope.contractor_pay` full prompt is 30 (B2 verbatim; the red team flags it as an owner judgment).

## Coordinator change after drafting (00:4x): BUG-0907 moved out of sche-a

- **BUG-0907 is dropped from v2 sche-a.patch.** The coordinator placed it in `v2/inc-m12.patch` with the same A3 single
  text [C inc-m12.patch:1780-1787]. v2 sche-a no longer touches `scope.nol` or `s1.nol_amount` [C grep: 0 matches].
  The A3 rows in the table below and decision 3 now describe inc-m12's hunk, not this patch.
- **B2 is already in v2 int-n10-ticks.patch.** It uses the text inc.md gives, word for word [C inc.md:190-191].
- **Sequential checks with `patch -p1 -F0` on scratch copies [C]:**
  - int-n10-ticks → inc-m12 (v2) → inc-m34 (v2) → sche-a (v2): all apply.
  - sche-a → int-amt → int-p18 → int-personas → int-n10 → int-n10-ticks: all apply.
  - **All eight together does not apply.** I tried int-n10-ticks, inc-m12, inc-m34, sche-a, int-amt, int-p18,
    int-personas, int-n10. Every patch applies except int-amt, which fails 2 of its 8 `questions.yaml` hunks, even at
    fuzz 2 [C].
    - inc-m12 adds groups (`cod_why`, `cod_how`) at the same spot after `money_b` where int-amt adds
      `interest_dividends` [C inc-m12.patch:1725-1733].
    - inc-m34 edits the `div.other_boxes` help inside int-amt's renumbered `div.*` block (lines 543-547).
    - The conflict is textual only: no entry is changed by both. **Fix at merge:** apply int-amt before inc-m12 and
      inc-m34, or rebase int-amt's two `questions.yaml` hunks onto them. I have not rebased it, because the inc
      patches are not this lane's.

## Red-team findings applied, by patch

### sche-a.patch

| Finding | Entry | v2 text | Words |
|---|---|---|---|
| A1 (0775) | `rental.amt9`, `rental.amt13` help | "If it was your home for part of 2025 and you did not count those days as days you used it, enter only the part for the days it was rented or offered for rent." | 35 |
| A1 | `rental.amt12` help | same frame + "Interest for the time it was your home goes with your home mortgage interest." | 49 |
| A1 | `rental.amt16` help | same frame + "Tax for the time it was your home goes with your home's property tax." | 49 |
| A1 (required counterpart) | `sa.mortgage_interest` help, appended | "If a home was rented or offered for rent for part of 2025, count only the interest for the rest of the year; the rental part is asked with the rental." | +30 (78 total) |
| A1 | `sa.line5b` (the Schedule A property-tax amount) help, inserted | "If the home was rented or offered for rent for part of 2025, count only the tax for the rest of the year." | +22 (52 total) |
| A1 coverage | new fixture `xsa.rental_then_home_june` | see the values table | |
| A3 (0907, single text; **moved to inc-m12, not in this patch**) | `scope.nol` help | "A loss bigger than that year's income, not yet used up, from a business, farm, rental or disaster; or a business loss held back by the yearly limit (Form 461). A loss still held back on Form 8582 is not one." | 41 |
| A3 (**moved to inc-m12**) | `s1.nol_amount` help | as round 2: "… Leave out losses held back on Form 8582 or by basis or at-risk limits." | 38 |
| A11 (0790) | `asset.listed` bank prompt | "For this property — Is it property of a kind used for entertainment or recreation (such as photographic, sound, communication or video recording equipment) that is not used only in your business or at your regular place of business? Also answer Yes for a computer …" (the computer sentence is unchanged) | 61, as before |
| A11 | `asset.kind_excluded` tick | "A building, land, a vehicle, boat or aircraft, a film or recording" | 12 (the red team's 14-word text is over the 12-word tick cap) |
| A11 | `forms/2025/asset.yaml` `asset.kind_excluded` source and label | source "Is this a building or part of one, land, a vehicle, a boat, an aircraft, a film or a recording?"; label adds "a boat" | |
| A11 | `asset.screen` label | new bullet "- it is a boat" after the vehicle bullet | |
| A11 | `asset.listed` form source | round-2 change **dropped**; xint's source stays | |
| C2 (0789) | headings of `rental_costs_a/b/c` | "In 2025, did you pay any of these for this rental, or did a tenant pay any in place of rent?" / "In 2025, did you pay any of these for it, or did a tenant pay any in place of rent?" / "And did you pay either of these for it, or did a tenant pay either in place of rent?" | 21 / 20 / 19 |
| B3 (0890) | `royalty.amt19` source | "Other costs of it (not depletion), paid in 2025, or taken out of your payments if the royalties you entered are before they were taken out; zero if none" | |

Unchanged from round 2:
- f8582 (0836);
- `rental.amt17` source;
- the `rental.not_at_risk` source and help;
- `rental.rents` help;
- `royalty.expenses_any` (E lists it as sound);
- the five original fixture cases.

The one exception among the fixtures is the converted-home case. Its evidence note now states the lease assumption
(below).

### int-amt.patch (A4)

- Heading of `interest_dividends`: "In 2025, did you (or, on a joint return, your spouse) **have** either of these?"
  (15 words).
- `div.any` tick: "Shares or funds owned outside a retirement account, or a 1099-DIV" (11 words).
  - Source: "own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV"
    [C forms/2025/div.yaml:368].
- The `f1040.tax_exempt_any` tick is unchanged.
- Only these two `+` lines differ from round 2. Neither is in a fixture, coverage row or persona, so nothing else
  moves [C grep of the patch].

### int-n10.patch

| Finding | Entry | v2 |
|---|---|---|
| merge conflict | `rental.not_at_risk` | the bank `prompt:` override is removed (sche-a's source and help stand) |
| A2 | `rental.personal_any` help | red-team verbatim, 45 words by my count: "Family means a spouse, parent, grandparent, child, grandchild, brother or sister. Not personal use: family renting at a fair rent as their main home, and days it was your main home before or after renting it out (or trying to) for 12 months or more." |
| B1 | `k1s.past_years` prompt | "(or your spouse, whether or not you file jointly)" in place of "(or, on a joint return, your spouse)"; 40 words |
| C7 | `k1s.not_at_risk` help | "Such as a loan you are not personally liable for, or money protected from loss by a guarantee or stop-loss agreement. A bank loan you must repay yourself does not count. A Yes ends the interview here." (37) |
| C4 | `rprop.kind` residential choice | "A building with 80% or more of its rent from homes or apartments, or an improvement to one" |
| C5 | `rprop.basis` prompt | "For this building or improvement — Your share of what it cost, not counting the land. If you used it yourself before renting it, use the smaller of what the building was worth then and what you paid plus improvements, both without the land." (44) |

The other entries are unchanged. The red team's section E lists them as sound: `rental.days_personal`, `days_fair`,
`person.*`, `s2.amt_business`, `k1p.*`.

### int-n10-ticks.patch

- B2: the `scope.contractor_pay` full prompt is now "In 2025, did a firm pay you (or, on a joint return, your spouse)
  as a contractor, with no social security tax taken out, when you were really its employee?" (30 words). The form
  computes Form 8919 on a Yes [C per red team, person.yaml:1040-1046], so the condition has to be in the prompt.
- C6 (`rec.has_other`, `scope.wages_no_form`): the red team gave no corrected text and calls it the owner's 25-word
  decision, so these entries are unchanged.
- B4 (scope prompts against lane M2): I found no inc-* patch that changes these four `scope.*` sources; inc-m12 only
  adds coverage answers and touches the bank entries' neighbours [C grep]. So there is no masking now. If M2 later
  edits these form sources, the bank prompts here override them.

### int-p18.patch, int-personas.patch

No change. The red team's section E lists the `sales_rare` reorder and the `refund.you_born` rule as sound.

## Where the red team and a patch's .md disagree, decided on the source

1. **0775 frame (A1 vs sche-a.md vs the model). Decision: a conditional frame.**
   - p527: "this special rule doesn't apply when dividing expenses between rental and personal use. See Property Changed
     to Rental Use" [C sources/2025/p527.cols.txt:902].
   - p527: "You can deduct as rental expenses only the part of the expense that is for the part of the year the property
     was used or held for rental purposes" [C :745].
   - The form divides every cost by fair days over days of use when `rental.personal_any` is Yes
     [C rental.yaml:736-766, `rental.line9` = `div9`; the same for every line].
   - When the main-home days **are** counted, which happens when the rental ran under 12 months and did not end in a
     sale [C p527.cols.txt:897-901], the form's division already gives about the rental part of a full-year amount.
   - Entering only the rental part as well would divide twice. In A1's own reverse case that gives
     5/12 × 151/365 ≈ 17% of the costs instead of 5/12.
   - So the frame tells the filer to enter only the rental part when they did not count the main-home days.
   - The two Schedule A sentences (red-team verbatim, with "this home" made "a home" because `sa.mortgage_interest`
     asks about all homes) then hold in both cases.
   - The amt12 and amt16 closing sentences say where the home-time amount goes. They replace "Leave … out of your home
     mortgage interest", which contradicts the Schedule A note when the full year is entered.
2. **0790 (A11 vs sche-a.md). Decision: the red team's version (refuse boats).**
   - p946: "Other property used for transportation includes trucks, buses, boats, airplanes"
     [C sources/2025/p946.cols.txt:1940]. The page is 53 by the page markers at :1929/:1983 [I].
   - So a boat is not entertainment property, and the computed path needs the filer to apply the fourth `asset.qbu_low`
     bullet, "use that is nondeductible under section 274" [C forms/2025/asset.yaml:748].
   - That is the red team's yacht case. It is partly guarded, but only by jargon (N6). The refusal is the safer of the
     two.
   - Cost: a boat used more than 50% in business is now refused (over-refusal).
   - **The owner may still prefer sche-a's round-2 version.** It is recoverable from `/tmp/nightplan/patches/sche-a.patch`.
3. **0907 (A3 vs sche-a.md). Decision: A3 verbatim.**
   - sche-a's text named "K-1 share". A K-1 loss is a loss "from a business", and i172 lists trade or business,
     employee work, disaster and rental property [C per BUG_INVENTORY.md:11030, the entry's quote of i172].
   - The guard sentence keeps the Form 8582 exclusion.
   - 0907 is in no other lane's patch [C inc-m12.md:17 and inc-m34.md:11 leave it out].
4. **`rental.personal_any` (A2 vs int-n10.md). Decision: A2 verbatim.**
   - Both keep the 12-month clause.
   - p527: "unless the family member uses the dwelling unit as their main home and pays a fair rental price"
     [C p527.cols.txt:872]. Either wording fits.
   - A2 is closer to the current text, so the questions review has less to re-read.
   - Half siblings (p527: "siblings, half siblings") are not named. "Brother or sister" is commonly read to include
     them [I].
   - Not in either text: the sale exception (a rental of under 12 months that ended in a sale [C p527.cols.txt:900]).
     It predates both patches. The child `rental.days_personal` omits it too [C rental.yaml:115-117].

## Fixture values: independent re-derivation (sche-a, `fixtures/2025/rental.json`)

The method traces each expression from the forms. Tables: `macrs_mm` [residential, m2, 6] = 3.636% and
[residential, m6, 1] = 1.970% [C tables/2025/macrs_mm.yaml:67,222]; recovery year y2020 → 6 [C realty_recovery_year.yaml:21].
Params (mfs): phaseout_end 75,000, special_max 12,500, exception_magi 50,000, exception_loss 12,500 [C params/2025.yaml:2801-2850].
Prorate: ratio half-up to 6 places, then product half-up to the cent [C engine/src/eval.ts:533-545].
Defaults: personal_any false, active true, prior_any false, not_at_risk false [C fixtures/2025/defaults.json].

| Case | Line | Patch value | My value | Trace |
|---|---|---|---|---|
| f8582_mfs_together_late | exception | false | false | `mfs_together` = mfs ∧ ¬apart_all_year = true |
| | required | true | true | `deductions` (p4b 213.20 > 0) ∧ ¬exception |
| | line4 | 0 | 0 | `part2` false (mfs_together) → zero |
| | line9 | 0 | 0 | min(0, line8 12,500) |
| | p7_C | 213.20 | 213.20 | loss3 213.20 − 0 |
| | rental line21 | −213.20 | −213.20 | 13,500 − (8,000+400+500+250+200+4,363.20) |
| | rental line22 | 0 | 0 | p6_on false (line9 0) → p7a 213.20 → p7c 213.20 (ratio 1) → allowed 0 |
| | carryforward | 213.20 | 213.20 | = p7c |
| | s1.line5 | 0 | 0 | sche.line41 = rent_income 0 + line22 0 |
| | AGI | 50,000 | 50,000 | |
| f8582_mfs_apart_last6 | all | same | same | apart_last6 ≠ apart_all_year → mfs_together true [C household.yaml:1723-1735] |
| f8582_mfs_apart_all_year | exception | true | true | 21,320 ≤ 1,250,000; line6 5,000,000 ≤ 5,000,000 (`le`) |
| | required | false | false | |
| | line5 / line8 | 75,000 / 12,500 | same | line7 25,000, half 12,500, cap 12,500 |
| | line9 | 213.20 | 213.20 | min(line4 213.20, 12,500) |
| | line22 / AGI | −213.20 / 49,786.80 | same | p6c 213.20 → p7a 0 → allowed 213.20 |
| converted_home_june | line9/12/16 | 233.33 / 4,666.67 / 291.67 | same | personal_any false → the amounts as entered |
| | line18 | 2,364.00 | 2,364.00 | 120,000 × 1.970% |
| | line21 / line22 | −1,005.67 | same | 7,000 − 8,005.67; exception holds (loss ≤ 25,000, MAGI 50,000) → line9 1,005.67 → allowed in full |
| | AGI | 48,994.33 | same | |
| tenant_paid_repair | line14 / line21 / AGI | 600 / 11,400 / 61,400 | same | no loss, so f8582 is not required and line22 is 0 |
| royalty_tax_withheld | line16 / line21 / AGI | 500 / 9,500 / 59,500 | same | line20 = 0 + 500 + 0 |
| **new** rental_then_home_june | home | — | true | 214 > 14; 10 × 214 = 2,140 > 151 (cents) |
| | line9 | — | 165.48 | 40,000 × 413,699 / 10⁶ = 16,547.96 → 16,548 |
| | line12 | — | 3,309.59 | 800,000 × 0.413699 = 330,959.2 → 330,959 |
| | line16 | — | 206.85 | 50,000 × 0.413699 = 20,684.95 → 20,685 |
| | line21 | — | refusal at `rental[a].ws51` | the refusal object is copied from the cottage case in the same file |

- None differ.
- **What the new case pins.** With the main-home days counted, full-year amounts give about 5/12 of each cost
  (5/12 would be 166.67 / 3,333.33 / 208.33). The days fraction differs from months by under 1%. The tool then refuses
  the return (Worksheet 5-1), so the reverse case never reaches a return. The case pins the division, not a return
  value.
- **The converted-home case** now states its premise: a lease running 12 months or more, so the main-home days are not
  personal days and personal_any is No. A June conversion with a shorter rental would count those days and take the
  reverse path.

**Unverified** (to be settled by `test-fixtures`):
- the MFS cases' other inputs defaulting cleanly (`household.married_dec31` is withheld for mfs);
- `"$rental": []` with `scope.rental` true in the royalty case;
- that a refused `line21` leaves `line9`/`line12`/`line16` evaluated in the new case (the cottage case asserts
  `rental.home` beside its refusal, which suggests it does).

## Siblings and residuals (not patched)

- **Vacation-home Schedule A gap (pre-existing).** For a rental with counted personal days that is not a converted
  home, the personal part of mortgage interest and tax reaches Schedule A only if the filer adds it there. No sentence
  steers it. Such a rental is usually refused at `rental.ws51` once it is used as a home. A rental with 14 or fewer
  personal days still divides, with nothing pointing the personal part to Schedule A [I]. Low.
- **The `k1s.past_years` form source** still says "(or, on a joint return, your spouse)" [C forms/2025/k1s.yaml:1173-1174].
  The int-n10 bank prompt overrides it. Whoever lands BUG-0886 should fix the source too. This is latent while
  `scope.k1` refuses.
- **C8 (cell phones under "communication equipment")**: over-refusal only. Left as sche-a.md describes.

## What to run (in a lane worktree, after applying in the order above)

1. Build; `render` and `render --check` (asset, rental, royalty, f8582 forms changed).
2. `test-fixtures`, federal and `--ny`: the 7 xsa cases, plus int-amt's restated inputs. Expect no existing expectation
   to move.
3. `tick-groups`: `rental_costs_a/b/c`, `asset_kind` and `interest_dividends` changed.
4. `interview-coverage --write`, and `draft-walk` for the rental, sales, business-asset and K-1 personas and personas
   01, 03, 04, 07, 08, 18, 21 and 22.
5. `interview-rules`, `interview-order`, then `tools/check_all.sh` in the lane worktree.

## Reviews this makes due (changes from the round-2 .md files only)

- **Added: asset.**
  - `asset.kind_excluded` and `asset.screen`: render and transcription, line-scoped.
  - Screen and false-no samples of `gate:asset.kind_excluded`.
  - Question review of the `asset.kind_excluded` tick and the `asset.listed` prompt.
  - The `asset.listed` form source no longer changes, so its transcription is no longer due.
- **Added: Schedule A.** Question reviews of `sa.mortgage_interest` and `sa.line5b` (help only, so the screen subjects
  do not change [C per sche-a.md, tools/README.md:533]).
- **Changed: royalty.** `royalty.amt19` is still render and transcription line-scoped (new text).
- **Removed: `rental.not_at_risk`.** The bank prompt is gone from int-n10, so the bank override is no longer reviewed.
  The form-source review from sche-a remains.
- **Unchanged otherwise:** f8582 class M and the rest, as in sche-a.md, int-amt.md and int-n10.md.
