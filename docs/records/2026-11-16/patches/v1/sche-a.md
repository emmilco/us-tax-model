# Lane patch-sche-a: rental, Form 8582, royalty and listed-property fixes, plus the NOL help

Lane patch-sche-a. Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Written 2026-11-16.
Patch: `/tmp/nightplan/patches/sche-a.patch` (731 lines, 6 files). It was made from copies in
`/tmp/nightplan/scratch/sche-a/{a,b}`. Nothing in xint was written.
Tags: **[C path:line]** means checked against that file (xint paths unless stated). **[I]** means inferred, not run.

## Summary

- **What the patch fixes.** BUG-0775, 0789, 0790, 0836, 0890 and 0907, and the `rental.not_at_risk` gap that
  `/tmp/nightplan/interview.md` found. All of these are wording changes except 0836. 0836 changes arithmetic: an MFS
  filer who lived with the spouse at any time in 2025 now gets line 9 = $0, and the filing exception fails for them.
- **Applies cleanly.** `git apply --check` against xint succeeds. This check writes nothing. All five YAML files parse
  (PyYAML safe_load).
- **Not run.** No engine was run, so nothing has been rendered, fixture-tested or walked. All six new fixture values
  are worked out by hand.
- **Fixtures.** Six new cases in `fixtures/2025/rental.json`:
  - three for 0836 (MFS together_late, apart_last6, apart_all_year);
  - one for 0775 (a home converted on June 1);
  - one for 0789 (a repair the tenant paid);
  - one for 0890 (royalty with severance tax withheld).
- **Choices made (detail below).**
  - 0775 is fixed by wording: the recommended option of D1.
  - 0790 names a boat in the listed-property question rather than refusing every boat. This is the recommended option
    of D4. Whether it also lands on `main` is still the owner's call.
  - 0907: I chose a reconciled wording. It keeps "rental", which med-income dropped, and also keeps med-income's
    Form 8582 guard. Reason below.
  - 0836: the guard sits in `f8582.part2`, not in `f8582.line9`. Line 4 and line 9 both come out $0, which matches
    "Do not complete Part II". Lines 4 to 9 are also hidden for that filer through a new `f8582.part2_shown`.
- **BUG-0911** is not edited. It is a bookkeeping note: a closure entry is recommended, see the last section.
- **Siblings found and not patched:**
  - `sa.mortgage_interest` needs a counterpart help line for a converted home.
  - "Communication equipment" in the listed-property question may catch cell phones. The law that removed them is not
    archived.
  - The exclusive-business-use exception is applied to all recreation property; the source gives it only to
    photographic, phonographic, communication and video equipment.
  - The pre-1987 at-risk exemption is not asked. That only over-refuses.

## Conflict with another lane's patch (must be settled at merge)

`/tmp/nightplan/patches/int-n10.patch` (hunk `@@ -7190,6 +7196,7 @@`) adds this bank `prompt:` to `rental.not_at_risk`:
"Did you pay for it, or for work on it, with a loan you are not personally liable for, from someone other than a bank, a
government or another regular lender (for example, the seller)?"

- A bank prompt overrides the form source. If both patches land as written, int-n10's nonrecourse-only prompt would
  mask this patch's three-class source, and the gap would reopen.
- The two hunks also touch the same lines (`help: A Yes ends the interview here.`), so whichever applies second will
  fail to apply.
- **Resolution:** drop int-n10's `rental.not_at_risk` prompt and keep this patch's source and help. The new wording
  already meets N10 at 40 words with the frame.
- I checked int-n10, int-n10-ticks, inc-m12, inc-m34, int-amt, int-p18 and older-credits for my other hunks. The only
  overlap is int-amt's fixture rows that state `"scope.nol": false`, which this patch does not touch.

## Hunks, file by file

### interview/2025/questions.yaml (bank only)

1. **Groups `rental_costs_a/b/c`** (0789): the headings become "Did you, or a tenant for you, pay any of these for
   this rental in 2025?", "... for it in 2025?" and "And did you, or a tenant for you, pay either of these for it?"
   [C questions.yaml:162-167 before].
2. **`scope.nol` help** (0907): "A loss bigger than that year's income, not yet used up, from a business, farm, rental
   or K-1 share, or a disaster; or a business loss held back by the yearly limit (Form 461). Passive losses held
   back on Form 8582 are not." (43 words.)
3. **`s1.nol_amount` help** (0907, from med-income): adds "Leave out losses held back on Form 8582 or by basis or
   at-risk limits." (38 words in total.)
4. **`asset.listed` prompt** (0790): "Is it a boat, or something used for entertainment or recreation (such as a camera,
   or sound, video or communication equipment) that is not used only in your business or at your regular place of
   business?" The computer sentence is kept. At 61 words it is the same length as before, and still over N10's
   40-word target for a child question. That length predates this patch.
5. **`rental.rents` help** (0789): "Include a security deposit you kept, and repairs or bills a tenant paid for you in
   place of rent; enter those again below as costs."
6. **`rental.amt9` and `rental.amt13`** (0775) get new help: "If it was your home for part of 2025, enter only the part
   for the time it was rented or offered for rent."
7. **`rental.amt12` help** (0775): "Only the interest on this property, your share. If it was your home for part of
   2025, enter only the part for the time it was rented or offered for rent. Leave what you enter here out of your
   home mortgage interest." (42 words.) The old text, "Leave this mortgage out of your home mortgage interest",
   steered the personal months' interest away from Schedule A (BUG-0775 symptom). The new text excludes only the
   rental part.
8. **`rental.amt16` help** (0775, the sibling the plan found): the same frame, and "Leave what you enter here out of
   the taxes you deduct for your home." (37 words.)
9. **`rental.not_at_risk` help** (new gap): "A mortgage from a bank, a government or another regular lender is at
   risk. A loan from the seller, a co-owner, or a relative of either is a Yes. A Yes ends the interview here." (34
   words.)

### forms/2025/rental.yaml

1. **`rental.amt17` source** (0789): "Utilities for it, paid in 2025 by you or by a tenant in place of rent". It was
   "Utilities you paid, paid in 2025" [C rental.yaml:1298].
2. **`rental.not_at_risk` source** (new gap): "Was any money you put into it borrowed without personal liability from
   anyone but a bank or other regular lender, protected from loss by a guarantee or stop-loss agreement, or lent by
   someone with a stake in it?" This is 40 words with the frame "For this rental property — ".
   - The cite locator now quotes "In most cases, you are not at risk for amounts such as the following" and names
     Qualified nonrecourse financing.
   - Source: the three not-at-risk classes, and the definition of a qualified person (not the seller, not someone
     related to you) [C sources/2025/i1040se.cols.txt:48-49].
   - "Someone with a stake in it" is used rather than "a co-owner". BUG-0888 showed that a lender with an interest
     who is not an owner is a separate miss [C BUG_INVENTORY.md:10835-10843]. The source says "a person who has an
     interest in the activity (other than as a creditor)".
   - The refusal (`rental.line22` on `rental.not_at_risk_if_loss`) is unchanged.

### forms/2025/royalty.yaml

1. **`royalty.expenses_any` source** (0890): "Did you pay any costs for it, or did the payer take any out of your
   payments (such as fees, severance or production taxes, or production costs)?" (30 words with the frame.)
   - Source: i1040se line 4, "Include taxes withheld by the producer on line 16" [C, quoted in BUG_INVENTORY.md:10855ff].
2. **`royalty.amt19` source**: "Other costs of it (not depletion), paid in 2025 or taken out of your payments; zero if
   none".
   - `royalty.amt16` already says "including any the payer withheld" [C royalty.yaml:109], so it is unchanged.

### forms/2025/asset.yaml

1. **`asset.listed` source** (0790): the transportation limb is added first: "a boat or other property used for
   transportation; ...". The rest is unchanged.
   - The cite locator adds i4562 p. 3, "Any other property used for transportation if the nature of the property lends
     itself to personal use" [C sources/2025/i4562.cols.txt:49].
   - p946 confirms boats: "Other property used for transportation includes trucks, buses, boats, airplanes" [C
     sources/2025/p946.cols.txt:1940].
   - The exclusive-use clause stays on the entertainment limb only. Exception 1 covers only photographic,
     phonographic, communication or video equipment [C i4562.cols.txt:50], so a boat has no such exception.

### forms/2025/f8582.yaml (0836, arithmetic)

1. **New `f8582.mfs_together`** (helper, Bool): `all[ household.mfs = true, household.mfs_apart_all_year = false ]`.
   - It reuses the existing helpers [C household.yaml:1651-1662, 1723-1735].
   - `household.mfs` is needed because `mfs_apart_all_year` is false on every other status: its gate falls back to
     together_late [C household.yaml:1700-1719].
   - Cite: i8582 p. 10, Part II caution, quoted exactly [C sources/2025/i8582.cols.txt:196]. The page was counted from
     the form feeds in i8582.txt.
2. **`f8582.part2`** gets a third condition: `f8582.mfs_together = false`.
   - Line 4 then takes `f8582.zero`, and line 9 = smaller_of(line 4, line 8) = $0.
   - The cite adds "Do not complete Part II. Instead, go to Part III of Form 8582".
   - Only line 4 reads `part2` [C f8582.yaml:363,369]. Only `line9` reads line 4 [C f8582.yaml:493].
3. **New `f8582.part2_shown`** (gate): `required ∧ ¬mfs_together`. Lines 4 to 9 change `shown_when` from
   `f8582.required` to `f8582.part2_shown`. Without this, lines 5 to 8 would print $75,000 and $12,500 on a form the
   instructions say not to complete. Values are unchanged.
   - **Can be dropped:** if the coordinator wants arithmetic only, drop this gate and the six one-line `shown_when`
     changes. Line 9 is $0 either way.
4. **`f8582.exception`** gets the condition `f8582.mfs_together = false`. The label adds "and, if married filing
   separately, you lived apart from your spouse all year", and the locator adds that bullet [C i8582.cols.txt:29].
5. **Unchanged:** the status-keyed parameters ($75,000 / $12,500 / $50,000), which now apply only when the spouses
   lived apart all year [C params/2025.yaml:2801-2852].
   - Readers checked: `rental.p6_on` and `rental.p6c_share` read line 9 [C rental.yaml:1828-1860], so with line 9 at
     $0, Part VI is off. `rental.p7c` takes all of `f8582.p7_C` = loss3 − 0, so `rental.allowed` = 0
     [C rental.yaml:1861-1936; f8582.yaml:568-578]. This is hand-traced [I], not evaluated.

### fixtures/2025/rental.json: six cases, all hand-predicted [I]

| Case | Inputs (beyond the base) | Expected | Derivation |
|---|---|---|---|
| `xsa.f8582_mfs_together_late` | base x1sche.f2.small_loss_exception; status mfs; mfs_living together_late | exception false, required true, line4 0, line9 0, p7_C 213.20, rental line21 −213.20, line22 0, carryforward 213.20, s1.line5 0, AGI 50,000 | i8582 p. 10: Part II not completed. p. 1: the exception needs the spouses apart all year. Line 10 income 0, so the whole loss is unallowed. |
| `xsa.f8582_mfs_apart_last6` | same, apart_last6 | same as above | Lived together before July, which is "at any time during the year". This case pins that the helper reads apart_all_year, not apart_last6. |
| `xsa.f8582_mfs_apart_all_year` | same, apart_all_year | exception true, required false, line5 75,000, line8 12,500, line9 213.20, line22 −213.20, AGI 49,786.80 | MAGI $50,000 ≤ $50,000 (`le`, an edge); loss 213.20 ≤ 12,500. Line 7 = 75,000 − 50,000 = 25,000; half = 12,500 = cap. |
| `xsa.converted_home_june` | home until May 31, rented from June 1; days_fair 214, personal_any false; amounts entered for 7/12: mortgage 4,666.67, insurance 233.33, tax 291.67; repairs 250, utilities 200; building $120,000 placed June 2025 | line9 233.33, line12 4,666.67, line16 291.67, line18 2,364.00, line21 −1,005.67, line22 −1,005.67, AGI 48,994.33 | p946 Table A-6 month 6 = 1.970% (the same rate as xfix.f21) [C rental.json xfix.f21 note]. Expenses 5,641.67 + 2,364.00 = 8,005.67; 7,000 − 8,005.67. The exception holds. This pins the intended reading: no second division, and the amounts are already the rental part. |
| `xsa.tenant_paid_repair` | rents 12,000 including a 600 repair the tenant paid; has_repairs, amt14 600 | line14 600, line21 11,400, AGI 61,400 | p527, Expenses paid by tenant. |
| `xsa.royalty_tax_withheld` | `$rental` [], royalty line4 10,000, expenses_any true, amt16 500 | royalty line16 500, line21 9,500, AGI 59,500 | i1040se line 4 / line 16. |

Unverified points in these fixtures, to be settled by `test-fixtures`:
- The MFS cases rely on `household.married_dec31` being withheld for mfs [C defaults.json "withheld"], and on the
  other MFS inputs defaulting.
- `xsa.royalty_tax_withheld` uses `"$rental": []` with `scope.rental` true. classm.json has that pattern; a
  hand-written case does not.
- `rf4562` is in `covers` of the converted-home case, but none of its lines are asserted.
- Case ids use a new prefix, `xsa.`. Rename if the lane uses another.

No fixture was added for 0790 or for `rental.not_at_risk`. Both are wording only, and their Yes paths are already
pinned by `stage14.asset.refuse_listed_low_past_gds` and `x1sche.r6.not_at_risk`. No existing MFS fixture has a rental
or a royalty, so no existing case changes value [C: a script over every fixtures/2025 case].

## Decisions and reconciliations

- **0775 (D1):** wording. The help on the four yearly-cost questions (insurance, mortgage interest, other interest,
  taxes) frames "the part for the time it was rented or offered for rent".
  - This matches p527's "part of the year the property was used or held for rental purposes" [quoted in
    BUG_INVENTORY.md:9704ff]. A days input would not match it, because vacant-but-offered days count as held for
    rental.
  - Utilities, repairs and the other costs are normally incurred after conversion, so they get no help line. This is
    a judgment [I]. Add the line to `rental.amt17` if review disagrees.
  - Residual: the frame is in help. A converted-home filer who never opens the help still overstates. N10 accepts help
    for "one example that settles a common doubt". The refusal and days-input options remain open to the owner.
- **0790 (D4):** a boat is named in the question, not added to `asset.kind_excluded`. Refusing every boat would also
  refuse a boat used over 50% for business, which the form computes. Landing on `main` too is still the owner's
  decision. Note that `main` has no `asset.listed` source change pending from this lane; the patch is against xint.
- **0907, reconciling the entry with med-income:**
  - The entry names rentals and K-1s but has no guard. With that wording, a landlord with suspended passive losses
    enters them on line 8a, which understates income.
  - med-income adds the guard but drops "rental". That makes a true rental NOL (for example an allowed $25,000 loss
    larger than income, or a real-estate professional) a false No.
  - I keep both "rental" and the guard sentence, "Passive losses held back on Form 8582 are not". The reader who
    opens the help on a rental loss then sees the exclusion at once.
  - This makes med-income's owner decision 6 unnecessary. If the owner prefers med-income's text, the only difference
    is "from a business or farm (including a K-1 share)" in place of "from a business, farm, rental or K-1 share".
  - The excess-business-loss limb sends a Yes to the existing `s1.nol_ebl` refusal [C questions.yaml:2084-2090].
- **Not-at-risk gap:** fixed by wording on the existing input, not by a second tick. This means no model change and no
  new default, coverage row or fixture.
  - The alternative is a second Bool, `rental.not_at_risk_other`, in a two-box group. Take it if review finds the
    40-word question too dense.
  - Over-refusal left in place: real property placed in service before 1987 is exempt from the at-risk rules
    [C i1040se.cols.txt:47]. The question does not ask about it, so such a filer is refused unnecessarily (safe
    direction).

## Siblings checked

- **`sc.at_risk`** already covers all three classes [C sc.yaml:1415-1428].
- **`k1p.not_at_risk`** covers guarantee and another partner [C k1p.yaml:1838-1840]. **`k1s.not_at_risk`** has
  BUG-0888 open for its residual. **Royalty** has no at-risk question: BUG-0889, open, not this lane.
- **`rental.amt5`..`amt19`:** the other sources say "paid in 2025" with no "you" [C rental.yaml source list], so they
  are left alone. The headings carry the tenant case.
- **`sa.mortgage_interest`** help ("Count loans on your main home and one second home only") [C questions.yaml:1337-1343]
  should gain "If a home became a rental in 2025, count only the interest for the time it was your home". Not patched:
  sa is not this lane's form.
  - The rental questions (order 130) come before Schedule A (order 200), so the new amt12 help is read first.
  - Without the sa line, a converted-home filer may leave the personal months' interest off Schedule A. That only
    understates a deduction.
- **`rental.days_personal`** source is unchanged: the main-home days are correctly kept out of the home test.
- **The `asset.kind_excluded` tick** ("A building, land, a vehicle, an aircraft, ...") does not name a boat
  [C questions.yaml:5565], so a boat reaches `asset.listed`.
- **Cell phones (owner note).** "Communication equipment" is the source's own term [C i4562.cols.txt:49], so a cell
  phone used 50% or less may now be answered Yes and refused. Cell phones were removed from listed property by
  statute (2010), but that law is not in the archive [I]. i4562 lists cellular telephones only as section 179 property
  [C i4562.cols.txt:37]. Suggest an ambiguity entry or archiving the provision before telling filers to leave phones
  out. This is the safe direction (over-refusal).
- **Exception scope.** The prompt's "not used only in your business" qualifier applies to all recreation property.
  The source's exception covers only photographic, phonographic, communication and video equipment
  [C i4562.cols.txt:50]. Other recreation property used only in the business is therefore answered No; that is safe
  only when business use is over 50%. Pre-existing, rare; noted, not fixed.

## What to run to verify (in a lane worktree, not xint while frozen)

1. `node engine/dist/main.js render`, then `render --check`. The patch does not include `rendered/` files, so render
   them after applying.
2. `node engine/dist/main.js test-fixtures`, for the six new cases and to confirm no existing case moves. Watch the
   `f8582` class M cases (`classm.f8582.1-3`, all single) [C classm.json]. Their values should not change; the hidden
   lines matter only if a check compares `shown_when`.
3. `node engine/dist/main.js interview-coverage --write`. No gate changed, so rows should be unchanged.
4. `node engine/dist/main.js tick-groups`, because the headings of three groups changed.
5. `node engine/dist/main.js draft-walk` for the rental personas and a business-asset persona. Compare words: about
   +20 for a typical landlord (headings and rents help), and 0 for a filer with no rental.
6. `tools/siblings.py` per the bug conventions, then `tools/check_all.sh` in the lane's worktree.

## Reviews this makes due (estimate before running; runs over $3.00 need `--approve-cost`)

- **f8582:** transcription, line-scoped (mfs_together, part2, part2_shown, exception, lines 4 to 9 for `shown_when`).
  Class M of f8582, because the arithmetic changed. Render of the changed lines. The completeness subject of f8582
  changes (sampled per release).
- **rental:** render and transcription, line-scoped (amt17, not_at_risk). Question reviews: rents, amt9, amt12,
  amt13, amt16, amt17, not_at_risk. Screen and false-no samples of the gates whose tick heading changed: the 13
  `rental.has_*` ticks (6 + 6 + `has_other`) and `rental.vehicle`. Also false-no of `rental.not_at_risk` (interview.md asked for this).
- **royalty:** render and transcription, line-scoped (expenses_any, amt19). Question review of both. Screen and
  false-no of `gate:royalty.expenses_any`.
- **asset:** render and transcription, line-scoped (asset.listed). Question review. Screen and false-no of
  `gate:asset.listed`.
- **scope.nol / s1.nol_amount:** question reviews.
  - The screen subject leaves out help [C tools/README.md:533], so the `before_2025` screen subject should be
    unchanged.
  - Whether the false-no subject of `gate:scope.nol` includes help is not checked [I].
- In total, roughly 16 screen/false-no subjects and 13 question subjects.

## Pending bug entry for the new gap (text for `tools/new_bug.py --pending`; not in the patch)

```
python3 tools/new_bug.py "rental.not_at_risk misses money protected by a guarantee or stop-loss and loans from someone with a stake in the rental" --pending sche-a \
  --field "Caught by=interview review of the seven areas (lane plan-interview, claude-opus-5-5), 2026-11-15; drafted in lane patch-sche-a, 2026-11-16" \
  --field "Source=i1040se p. 2, At-Risk Rules: not at risk for amounts 'protected against loss by a guarantee, stop-loss agreement, or other similar arrangement' and 'Amounts borrowed for use in the activity from a person who has an interest in the activity (other than as a creditor) or who is related under section 465(b)(3)(C) to a person (other than you) having such an interest'" \
  --field "Symptom=rental.not_at_risk asked only about a loan the filer is not personally liable for. A landlord whose money is protected by a guarantee or stop-loss agreement, or who borrowed from a co-owner or someone else with a stake in the rental (or a relative of one), answers No, and the Form 6198 refusal on rental.line22 does not fire, so a rental loss is allowed that the at-risk rules may limit." \
  --field "Where=forms/2025/rental.yaml rental.not_at_risk (source); interview/2025/questions.yaml rental.not_at_risk (help)" \
  --field "Fix=wording, lane patch-sche-a. The source asks all three classes: 'Was any money you put into it borrowed without personal liability from anyone but a bank or other regular lender, protected from loss by a guarantee or stop-loss agreement, or lent by someone with a stake in it?'; help names government lenders as at risk and the seller, a co-owner or a relative of either as a Yes. The refusal is unchanged." \
  --field "Fix lines=rental.not_at_risk" \
  --field "Siblings checked=sc.at_risk (covers all three classes), k1p.not_at_risk (covers guarantee and partner loans), k1s.not_at_risk (BUG-0888 open), royalty (no at-risk question; BUG-0889 open)" \
  --field "Regression predictions=none; x1sche.r6.not_at_risk (seller financing) still refuses" \
  --field "Severity=medium" --field "Tags=rental, at-risk, question wording"
```

If the patch does not land, replace the `Fix` field with `Proposed fix` and drop `Fix lines`, `Siblings checked` and
`Regression predictions` (tools/README.md:766-769). Each of the six numbered entries this patch fixes also needs its
closure recorded the same way (below), not by editing.

## BUG-0911 bookkeeping note (no edit made)

- **Why the tool calls it open.** The entry has two `**Fix:**` fields [C BUG_INVENTORY.md:11065ff]. `bug_status.py`
  joins repeated fields into one value [C tools/bug_status.py:100-120]. The joined value begins "Either make
  k1p.box9b ...", which matches `OPEN_FIX` ("either") [C tools/bug_status.py:75], so the tool reports the entry open
  although the fix is in the tree [C per med-k1sche.md: k1p.yaml:613-621, person.yaml:7689-7692].
- **Rule-conforming way (recommended).** BUG_INVENTORY.md is append-only, and status is derived, not edited
  [C tools/README.md:780-784]. Record a closure entry:
  `python3 tools/new_bug.py "Closure: BUG-0911 is fixed" --pending <lane> --field "Closes=BUG-0911" --field
  "Closure=fixed" --field "Evidence=k1p.box9b and k1p.box9b_if_any are Dollars (forms/2025/k1p.yaml), person.k1p_total_collectibles
  is Dollars, fixture x2k1p.collectibles_loss; the entry's first Fix field was the reviewer's proposal"`.
  Then run `tools/bug_status.py --write`. This works before and after xint lands.
- **Relabelling (possible, not recommended).** HEAD's inventory ends at BUG-0757, so BUG-0911 is uncommitted in xint
  [C `git show HEAD:BUG_INVENTORY.md`]. The byte-for-byte prefix check would therefore not catch a relabel made before
  the landing commit [C tools/README.md:770-771]. The relabel would change the first `**Fix:**` to
  `**Proposed fix:**`, the label the owner's 2026-11-15 convention gives to a fix proposed and not made
  [C tools/README.md:766-768]. BUG-0919 used `Proposed fix (review)`, which the tool reads as neither. But:
  - it rewrites an entry that `--assign` produced from a pending file;
  - if the landing is a merge, the check that the appended text equals what `--assign` produces may object
    [C tools/README.md:773-776];
  - and the owner's rule is that status is never edited in.
