# int-rprop.patch: `rprop.screen` taken apart (technique 3.1)

Lane v2-rprop, claude-opus-5-5, judgment, 2025, us. Nothing was built, walked or reviewed; no paid call was made.
**[C]** means checked against a file (path:line); **[I]** means inferred.

## Summary

- **What it does.** The seven-item catch-all `rprop.screen` (one input, about 144 words by the walk's count, 151 by a
  whitespace count) becomes a **derived Bool**, the `any` of seven new inputs. Six of them are a per-building
  tick-box screen, `rprop_facts` ("For this building or improvement — Is any of these true of it?"). The seventh,
  qualified improvement property, is a gated child `rprop.qip`. It is asked only when the entry is nonresidential
  **and** was placed in service after 2017, because the old bullet stated both conditions and the filer has already
  given both facts (§2 item 5).
- **No refusal is lost or changed.** The refusal entry `when: rprop.screen` on `rprop.dep` is untouched: same gate,
  form, remedy and cite. Each old bullet maps to one new input (table below). A Yes to any of them makes
  `rprop.screen` true. The expected end of every fixture and coverage row is unchanged.
- **Steps.**
  - Residential entries (the typical case, persona 19) and nonresidential entries placed before 2018: one step,
    as today. The walk's words for that step fall from about 144 to about 82 (heading 12 + labels 70, whitespace
    count) [I: not draft-walked].
  - **Deviation:** a nonresidential entry placed in service from 2018 to 2025 gets **one more step**, the QIP
    question (39 words). The QIP is the one item whose exceptions do not fit a 12-word label, and N10 sends a rule
    out of a long prompt into a child question. The alternative that keeps the step count, a gated seventh box,
    breaks the build's six-member cap [C interview/README.md:591-592]; see "Alternatives".
- **Files (8).** `forms/2025/rprop.yaml`, `interview/2025/questions.yaml`, `fixtures/2025/defaults.json`,
  `fixtures/2025/rental.json`, `fixtures/2025/classm.json`, `interview/2025/coverage/rental.yaml`,
  `interview/2025/coverage/scope.yaml`, `interview/2025/personas/19_rental_house.yaml`.
- **Checked:** `git apply --check` is clean against xint [C, run]. The patch **conflicts textually with
  int-n10** (both edit the bank lines from 7177 to 7196). Two rebased variants are provided, each
  `git apply --check`-clean on a temporary copy of the bank with that patch applied first [C, run]:
  - `int-rprop.after-n10.patch`: on top of round-2 `int-n10.patch`, with or without `int-n10-ticks.patch`.
  - `int-rprop.after-v2-n10.patch`: on top of `v2/int-n10.patch`.

  The two variants differ from the base patch only in the `questions.yaml` hunk. The bank edit is scripted in
  `/tmp/nightplan/scratch/v2-int-rprop/apply_bank.py` (input file, output file), so it can be rebased onto any
  other base.

## Hunks

### forms/2025/rprop.yaml (one hunk, replaces the `rprop.screen` input)

New lines, in file order:

| line | kind | what |
|---|---|---|
| `rprop.no` | helper | `param household.no` (false); the gate's else, as `asset.no` [C forms/2025/asset.yaml:2121-2127] |
| `rprop.new_nonres` | gate condition | `all`: `rprop.kind = nonresidential` and `rprop.recovery_year ≤ 8` (Count), i.e. placed in service 2018 to 2025 [C tables/2025/realty_recovery_year.yaml:16-23] |
| `rprop.qip` | input, `gated_by: rprop.qip_if_new_nonres` | the QIP child |
| `rprop.qip_if_new_nonres` | gate line | `choose`: `new_nonres` true → `rprop.qip`; false → `rprop.no` (formal gates convention, docs/2026-11-06_formal_gates_design.md:73-83 [C]) |
| `rprop.disposed`, `rprop.fast`, `rprop.ads`, `rprop.basis_changed`, `rprop.credit`, `rprop.coop` | inputs, `printed: (screen)` | the six boxes |
| `rprop.screen` | **now derived** | `test any` of the six inputs and `rprop.qip_if_new_nonres`; id, label, type and cite kept |

- The `le` test on a Count is supported by the evaluator [C engine/src/eval.ts:811-825]. The Lean side is not
  checked [I].
- The form `note` is unchanged; it already lists every refused case.

### interview/2025/questions.yaml (two hunks)

- Declares the group `rprop_facts`, heading `"Is any of these true of it?"`. The build puts the frame before it:
  "For this building or improvement — Is any of these true of it?" (12 words).
- Order 130:
  - `rprop.qip` at seq 60, right after `rprop.year` (59), the second of its two parents.
  - `rprop.basis` moves from 60 to 61.
  - The six members take 62 to 67.
  - `rental.not_at_risk` moves from 62 to 68 (`$royalty` is 71).
- The old `rprop.screen` bank entry is removed: it is no longer an input.

### Fixtures and interview files

| file | change |
|---|---|
| `fixtures/2025/defaults.json` | removes the `rprop.screen` default (no longer an input); adds `false` defaults for the 7 new inputs, kept in alphabetical order |
| `fixtures/2025/rental.json` `xfix.r11.qip_screen` | `rprop[b].screen: true` → `rprop[b].qip: true`; evidence note restated. Expected refusal unchanged |
| `fixtures/2025/classm.json` | 6 cases (`classm.s1.14`, `classm.f8582.1`, `classm.sche.1`, `classm.rental.3`, `classm.rprop.1`, `classm.rf4562.1`; 10 entries) stated `…screen: false`. Each now states the six boxes false. Entry `rental[b].rprop[d]` (nonresidential, 2025) also states `qip: false`, because class M takes no defaults [C tools/README.md:557] |
| coverage `rental.yaml` set `rents_house`, coverage `scope.yaml`, persona 19 | `screen: false` → the six boxes false. Residential, so no `qip` |
| coverage `rental.yaml` row `rental.rprop_screen` | answer restated as `disposed: true` (its situation is "a building she sold in 2025"); expected end unchanged |
| coverage `rental.yaml` | 8 new rows (below) |

## Old-to-new refusal mapping

Every row refuses at the **same** entry: `rprop.dep` refuses `when: rprop.screen`. The form is "Form 4562 (real
property outside the mid-month tables)", the remedy "Real property depreciated another way, with a changed basis,
disposed of, qualified improvement property, property with a credit or deduction for part of its cost, or
cooperative stock is outside this tool.", and the cite i4562 p. 11, Column (f)—Method
[C forms/2025/rprop.yaml:174-180, unchanged by the patch].

| old bullet (rprop.yaml:80-94) | new input | asked of | tick (words) |
|---|---|---|---|
| "you depreciate it over a longer period (the alternative depreciation system), or chose to" | `rprop.ads` | every entry | Depreciated over 30 or 40 years (the alternative system, ADS) (10) |
| "its basis changed after you began depreciating it, other than by depreciation (for example, a casualty loss)" | `rprop.basis_changed` | every entry | A casualty, easement or other event changed its cost after renting began (12) |
| "you sold, gave away or stopped renting it in 2025" | `rprop.disposed` | every entry | Sold, traded, given away, torn out, or no longer rented, in 2025 (12) |
| "it is stock in a cooperative housing corporation" | `rprop.coop` | every entry | A co-op apartment (stock in a cooperative housing corporation), not a condo (12) |
| "you deducted any of its cost in one year (a special allowance or section 179) or depreciate it another way" | `rprop.fast` | every entry | Bonus depreciation or section 179 taken for it, or another method used (12) |
| "it is an improvement to the inside of a nonresidential building … placed in service in 2018 or later (not an enlargement, …)" | `rprop.qip` (child) | `kind = nonresidential` and placed in service 2018 to 2025 | none; full question (39) |
| "you took a credit or deduction for part of its cost (for example the disabled access credit or the deduction for removing barriers)" | `rprop.credit` | every entry | A tax credit or special deduction taken for part of its cost (11) |

Box order: the commonest refusal first (§3.6, §7 item 5). A sale comes first; the cooperative stock, the rarest,
comes last [I: no frequencies exist for these].

**QIP gate equivalence.**
- The old bullet itself required both "a nonresidential building" and "placed in service in 2018 or later".
- The gate reads the same two facts from `rprop.kind` and `rprop.year`.
- A QIP is an improvement to a nonresidential building, so its owner picks the nonresidential choice ("Another
  building, such as shops or offices, or an improvement to one") [C questions.yaml:7112-7119].
- `rprop.year` asks "the year it was first ready and available for rent (placed in service) by you"
  [C rprop.yaml:56]. The source asks for "placed in service by you after 2017" [C p946.cols.txt:1154].

Only a filer who already mis-classed the entry's kind could miss the question. That error already gives the wrong
table today [I].

## Each prompt and label against its source

Full prompts are frame + form `source` (the frame is 5 words).

| input | full prompt (words) | help (words) |
|---|---|---|
| `rprop.disposed` | In 2025, was it sold, traded, given away, destroyed or torn out, or did you stop renting it out for good? (26) | Yes also if you began living in it. No if it only stood empty for a while between tenants. A Yes ends the interview here. (25) |
| `rprop.fast` | Did you deduct any of its cost in one year (bonus depreciation or section 179), or depreciate it other than straight line over 27.5 or 39 years? (32) | Bonus depreciation is the special depreciation allowance. Most rentals are depreciated straight line over 27.5 years (homes) or 39 years (other buildings). A Yes ends the interview here. (28) |
| `rprop.ads` | Do you depreciate it by the alternative depreciation system (ADS), over 30 or 40 years, by choice or because you must? (26) | ADS is required, for example, for a building outside the United States. A Yes ends the interview here. (18) |
| `rprop.basis_changed` | Since you began renting it, has its cost for tax purposes changed for any reason except depreciation, such as a casualty loss or payment for an easement? (32) | Improvements entered as entries of their own do not count. A Yes ends the interview here. (16) |
| `rprop.credit` | Did you take a tax credit or special deduction for part of its cost, such as the disabled access credit or the deduction for removing barriers? (31) | Others include the energy efficient commercial building deduction. Yearly depreciation does not count. A Yes ends the interview here. (19) |
| `rprop.coop` | Is it stock in a cooperative housing corporation (a co-op apartment you rent out)? (19) | A Yes ends the interview here. (6) |
| `rprop.qip` | Is it an improvement to the inside of the building, made after the building was first placed in service by anyone, and not an enlargement, an elevator or escalator, or the internal structural framework? (39) | A new roof or an addition is not an improvement to the inside. A Yes ends the interview here. (19) |

All are under N10's 40-word limit for a child.
- Five full member prompts are over 25 words: disposed 26, fast 32, ads 26, basis_changed 32, credit 31.
- That matters only if the owner applies the 25-word limit to a member's full prompt (plan item 5, still open).
  The labels are all 12 words or fewer.

**Sources, quoted [C each]:**

- **disposed.** p527 p. 9, Retired From Service: "You retire property from service when you permanently withdraw it
  from use … because of any of the following events. • You sell or exchange the property. • You convert the
  property to personal use. • You abandon the property. • The property is destroyed." [p527.cols.txt:266-272].
  - p946 p. 40: "If you dispose of property before the end of its recovery period, see Using the Applicable
    Convention" [p946.cols.txt:1501].
  - The help's "No if it only stood empty": p527 p. 9, Idle Property, "Continue to claim a deduction for
    depreciation on property used in your rental activity even if it is temporarily idle (not in use)"
    [p527.cols.txt:262].
  - "torn out" covers abandonment (a replaced roof listed as its own entry) [I as to the reading].
- **fast.** p527 p. 1: "Bonus depreciation. The 100% special depreciation allowance …" [p527.cols.txt:7].
  - p527 p. 12, Decreases to basis: "Special depreciation allowance or a section 179 deduction claimed on qualified
    property" [p527.cols.txt:361].
  - "another way": i4562 p. 11, Column (f)—Method [i4562.cols.txt:211].
  - The 27.5 and 39 years: Form 4562 lines 19i and 19j, "27.5 yrs. MM S/L" and "39 yrs. MM S/L"
    [f4562.cols.txt:41].
- **ads.** p527 p. 12: "You must use GDS unless you are specifically required by law to use ADS or you elect to use
  ADS" [p527.cols.txt:380].
  - 30 years: i4562 p. 12, "The ADS recovery period for residential rental property placed in service after 2017
    is 30 years" [i4562.cols.txt:237].
  - 40 years: p527 p. 14, "40 years for property placed in service before January 1, 2018" [p527.cols.txt:455].
  - Form 4562 line 20d is "40-year … 40 yrs. MM S/L" [f4562.cols.txt:41].
  - Help: i4562 p. 12, "The following types of property must be depreciated under ADS. • Tangible property used
    predominantly outside the United States." [i4562.cols.txt:232].
- **basis_changed.** p946 p. 37, Rules Covering the Use of the Tables: "4. You must stop using the tables if you
  adjust the basis of the property for any reason other than: a. Depreciation allowed or allowable, or b. An
  addition or improvement to that property that is depreciated as a separate item of property." and "a reduction
  in basis for a casualty loss" [p946.cols.txt:1366-1373].
  - Easement: p527 p. 12, Decreases to basis, "Amount(s) you receive for granting an easement"
    [p527.cols.txt:352-357].
  - The help ("improvements entered as entries of their own") is rule 4b.
- **credit.** i4562 p. 11, Column (c): "The following are examples of some credits and deductions that reduce the basis
  for depreciation. • Section 179 expense deduction. • Deduction under section 179D for certain energy efficient
  commercial building property. • Deduction for removal of barriers to the disabled and the elderly. • Disabled
  access credit. …" [i4562.cols.txt:204].
  - "Yearly depreciation does not count" guards the misreading that depreciation is "a deduction for part of its
    cost" [I].
- **coop.** p527 p. 8, Cooperative apartments: "If you are a tenant-stockholder in a cooperative housing corporation
  and rent your cooperative apartment to others, you can depreciate your stock in the corporation."
  [p527.cols.txt:232].
  - "not a condo" is a misreading guard; a condo is owned real property [I].
- **qip and its gate.** p946 p. 16: "any improvement to an interior portion of a building that is nonresidential real
  property if the improvement is placed in service after the date the building was first placed in service. Also,
  qualified improvement property does not include … • The enlargement of the building. • Any elevator or
  escalator. • The internal structural framework of the building." [p946.cols.txt:563-565].
  - p946 p. 31: "placed in service by you after 2017 and after the date the building was first placed in service by
    any person" [p946.cols.txt:1154-1156].
  - i4562 p. 10: "Qualified improvement property, as defined in section 168(e)(6), placed in service by you after
    December 31, 2017" [i4562.cols.txt:195].
  - The help's roof: a roof is not interior. An addition is the source's "enlargement".

Page numbers are counted by form feeds in the `.cols.txt` files. They agree with the existing locators (i4562 p. 10
and p. 11, p946 p. 37) [C]. BUG-0919 cites the i4562 15-year text as p. 9; the form-feed count puts it on p. 10
[C/I: a line can span a page break].

**Who could pass over each box wrongly** (§2 item 3), and what guards them:

- **disposed:** the owner of an improvement that was replaced, such as an old roof torn off. The label says "torn
  out".
- **fast:** an owner who does not know the term "special depreciation allowance". The label says "Bonus", the
  publication's own word.
- **ads:**
  - An owner of a building abroad, placed in service in 2025, who has not yet chosen a method. The help names it.
    The label does not: today's bullet did not either, so this is no regression.
  - Pending bug text below.
- **basis_changed:** an owner who took insurance money after a storm. The label leads with "casualty".
- **credit:** an owner who took the disabled access credit and thinks of it as "a credit, not part of the cost".
  The label says "for part of its cost".
- **coop:** a co-op owner who thinks they "own the apartment". The label leads with "A co-op apartment".
- **qip:** an owner who fitted out a shop interior before the building was first used. The answer is No, rightly:
  the work came before the building was placed in service.

## Coverage rows and fixtures (expected ends hand-predicted [I]; none walked)

| row | answers beyond `one_w2` + `rents_house` | expected end | derivation |
|---|---|---|---|
| `rental.rprop_screen` (restated) | `disposed: true` | refused `rental[house].rprop[bldg].screen` | disposed → screen true → `rprop.dep` refusal 2 (refusal 1, `personal`, is false: residential) |
| `rental.rprop_fast` (new) | `fast: true` | refused `…screen` | same chain |
| `rental.rprop_ads` (new) | `ads: true` | refused `…screen` | same |
| `rental.rprop_basis_changed` (new) | `basis_changed: true` | refused `…screen` | same |
| `rental.rprop_credit` (new) | `credit: true` | refused `…screen` | same |
| `rental.rprop_coop` (new) | `coop: true` | refused `…screen` | same |
| `rental.rprop_qip` (new) | `rental[house].kind: commercial`, `rprop kind: nonresidential`, `year: y2019`, `qip: true` | refused `…screen` | recovery year 7 ≤ 8 → `new_nonres` true → qip asked (seq 60) → `qip_if_new_nonres` true → screen true |
| `rental.rprop_qip_not_asked_old` (new) | commercial, nonresidential, `year: y2010` | `proceeds: {year: y2010}`, `not_asked: [qip]` | recovery year 16 → gate false; the boxes are No (set); `early_nonres` needs recovery year > 32, so false |
| `rental.rprop_qip_not_asked_home` (new) | `kind: residential` | `proceeds: {kind: residential}`, `not_asked: [qip]` | gate false. The set otherwise completes (`rental.house_computed` proceeds today [C reports/2025/interview_coverage.md:1048]) |

- **Existing row `rental.nonres_before_1994`:** unchanged. 1990 gives recovery year 36, so the gate is false and
  `qip` is not asked. The six boxes come from the set, all false, so `early_nonres` refuses as before.
- **The weakest prediction [I]:** that the commercial-kind return in `rental.rprop_qip_not_asked_old` completes.
  It rests on `rental.nonres_before_1994` reaching `rprop.dep` with the same set (it refuses there, after the screen
  and the rental questions before seq 68 are answered), and on the background return answering the rest.
- **Fixture `xfix.r11.qip_screen`:** nonresidential, y2019, `qip: true` → refused at `rental[a].rprop[b].screen`,
  as before.
- **Fixtures that need no edit:**
  - Every other `rental.json` case takes the new `false` defaults.
  - `x1sche.r9.nonres_before_1994` (1990): the gate is false, so it is unchanged.
  - The office building placed in 2025 in `xfix.f21.placed_2025_form4562`: the gate is true, `qip` takes its
    default false, and the values are unchanged.
- **Class M cases:** the inputs are restated equivalently. All boxes false is equivalent to `screen: false`.

**Siblings checked.**
- The `asset` boxes (`asset_history`, `asset_method`) use the same pattern; the labels follow their style
  [C questions.yaml:5619-5662].
- No other form's line reads `rprop.screen` [C `git grep`: only `rprop.dep`]. `rental.yaml` reads `rprop.kind`
  only [C rental.yaml:2047, 2069].
- `docs/COVERAGE.md` and `tools/coverage/tree.json:233` describe the gate. The tree question still holds.
  COVERAGE.md is generated, and its "data asks or tests" for `rprop.screen` will read `(test)` instead of
  `(input)`; regenerate it.

## What to run (in xint after applying; nothing run here)

1. Build:
   - the gate rules: the `gated_by` marker; no reader of `rprop.qip` besides its gate line;
   - the tick-group rules: 6 members, 12-word labels, contiguous seq 62 to 67, one form;
   - no bank entry for a non-input.
2. `test-fixtures`: `rental.json` (QIP, nonresidential before 1994, f21) and `classm.json` (the 6 restated cases).
3. `tools/defaults_guard.mjs --self-test`. Adding defaults is the normal tier. Removing one is not counted as a
   change: the guard compares only inputs present in both [C tools/defaults_guard.mjs:25-33]. Expect no
   acknowledgement line.
4. `tick-groups`: the screen shows all six boxes on the background return, and the same answers given one at a time
   end the return the same way.
5. `interview-coverage --write`: the 8 new rows, the restated row, and `rental.nonres_before_1994`.
6. `draft-walk`: persona 19 (one step for the building, as before; fewer words), and a nonresidential 2018+ case
   (one more step).
7. `interview-rules` (no early completion), `interview-order`, and regenerate `docs/COVERAGE.md`
   (`tools/coverage/tree.py`) and `rendered/2025/rprop.md`.

## Reviews made due (none run)

| review | why | how |
|---|---|---|
| rprop transcription, render, class M | form content changed (CLAUDE.md: review what changed) | `rerun_all.py` (line-scoped) after the round's rprop fixes; class M then regenerates the `classm.rprop.1` evidence |
| screen review | `rprop.screen` was never reviewed [C reports/2025/screen_currency.md:135]; new gate condition `gate:rprop.new_nonres` | `screen_review.py --screens rprop.screen` and the gate key |
| false-no review | new gate `rprop.qip_if_new_nonres` and six new refusing members | `false_no_review.py` (rprop); check the over-25 prompts too |
| question review | 7 new inputs (`rprop.screen` was never reviewed [C reports/2025/question_currency.md:777]) | `question_review.py --inputs rprop.qip,rprop.disposed,…` |
| consumers | `rprop.new_nonres` reads `rprop.kind` and `rprop.recovery_year` under a p946 p. 31 cite | the consumer rows of `reports/2025/consumers.md` |
| completeness | sampled per release; not made due by itself | none |

Each review is one per form per round, run after all of that form's fixes have landed.

## Alternatives considered and rejected

- **The QIP as a seventh, gated box** (shown only for nonresidential entries). This keeps the step count for
  everyone, but the build refuses a group of more than six declared members [C interview/README.md:591-592].
  - Folding `credit` into `basis_changed` to make room (as the asset box "A casualty loss, tax credit or special
    deduction changed its cost" does [C questions.yaml:5632]) would allow it.
  - But a 12-word QIP label cannot carry the three exceptions. Under N10 a rule moved out of a prompt goes into a
    child question, not into help.
  - **Owner's call** if the extra step for nonresidential 2018+ entries matters more.
- **Gating the QIP on the kind alone** (the plan's wording). This asks every nonresidential owner, including those
  placed in service before 2018, about something the year already rules out (§2 item 5). Rejected.
- **A QIP choice in `rprop.kind`.** An enum change reaches `macrs_mm` keys and the `rental.yaml` readers. Rejected
  as out of scope.

## Notes for the owner and the integrator

- **Year change [I].** `rprop.new_nonres` compares the recovery year with 8, which is right for 2025. In 2026,
  2018 is recovery year 9. Existing lines have the same property: `rprop.early_nonres` (> 32) and `asset.qip_early`
  (> 8) [C rprop.yaml:121-125; asset.qip_early]. `changes/2026/` holds no operation for either [C grep]. Flag this
  to the year-change lane.
- **BUG-0891 (open; like-kind exchange or involuntary conversion) is not addressed.** Its proposed fix was another
  bullet. The screen now has its six boxes, so it would need its own home: a gated child, or an exchange question
  beside the year. Left for the owner.
- **Pending bug-entry text (new), not in the patch:**
  - **Title:** rprop: a building outside the United States must be depreciated under ADS, and nothing asks where
    the rental is.
  - **Source:** i4562 p. 12, "The following types of property must be depreciated under ADS. • Tangible property
    used predominantly outside the United States."
  - **Symptom:** a foreign rental placed in service in 2025 (no method chosen yet) can answer No to the ADS box and
    is depreciated over 27.5 or 39 years. The new `rprop.ads` help names the case.
  - **Proposed fix:** a label or a refusal on location would close it.
  - **Severity:** low.
- `rental.not_at_risk`'s seq changes from 62 to 68. Its wording is untouched; int-n10 changes that.
- `xfix.r11.qip_screen` and `rental.rprop_qip` list only the improvement, not the building it is in. The case is
  possible but simplified.
