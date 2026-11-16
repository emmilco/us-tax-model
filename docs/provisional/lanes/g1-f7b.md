# Lane g1-f7b: the alternative minimum tax as a computed screen (T-307, T-310 l7b)

claude-opus-5-5, judgment, year 2025, jurisdiction us. Worktree `.claude/worktrees/nx-f7b` (not committed). Design
note, written before the build: `docs/2026-11-15_amt_computed_screen.md`. No paid review was run, and no model call.

## What the merge must know first

- **One existing fixture value would change under the alternative design. It is not made; the coordinator decides
  (section 5).**
- **Lines added to another lane's form**: `forms/2025/person.yaml` (lane F8) gains 7 new lines, `person.amt_dep_f17`,
  `_y3`, `_y5`, `_y7`, `_y10`, `_listed` and `person.amt_dep`, inserted after `person.sehi`. They are new ids only,
  sums over `sc` of existing `sc.f17`, `sc.f19_y3` to `y10` and `sc.f26h`, and no existing line changes. A per-person
  frame is the only place a sum over businesses can be taken (spec 4.4). F8's person review round covers them (line
  scoped).
- **Fixture inputs restated across shared files, by case id; no expected value edited:**
  - `s2.amt_owed` is no longer an input, and the evaluator refuses inputs on non-input lines. The key was removed from
    819 case inputs in 12 files: `fixtures/2025/{classm, classm.deepseek, classm.gpt, mutation, returns, s2, s3,
    person, f1040}.json` and `fixtures/ny/2025/{classm, classm.deepseek, mutation}.json`. The second-family files are
    historical; they are edited only because the runner reads them.
  - 58 cases gained the "does not apply" default of an input the change made reachable, which none of them had stated:
    `f1040.tax_exempt_interest: 0` (most), `s2.amt_business: false`, `s2.mortgage_subsidy: false`, `s2.amt_boat:
    false`. They are in classm(.deepseek) and mutation (list: `/tmp/f7b-scripts/fill.log`, reproduced in section 4).
  - `stage8.refuse.s8812.s2_other`: `s1a.tips`, `s1a.overtime` and `s1a.carloan` were withheld (null) and are now
    false (protocol 3.1(c)).
  - `stage4.refuse.s2.amt` and `.simultaneous`: `s2.amt_owed: true` is replaced by $100,000 of tax-exempt interest,
    all of it private activity bond interest. The expected refusal (gate `s2.amt`, Form 6251) is unchanged.
  - `mutation.m3.sa.no_mortgage_property_tax`: `s2.has_mortgage_interest` is dropped from `covers` (the line is
    removed).
- **Shared bank and coverage, edited by entry or row id**:
  - `questions.yaml`: `s2.amt_owed` removed; `s2.amt_pab`, `s2.amt_boat` and `s2.amt_business` added.
  - `defaults.json`: the same swap.
  - coverage: `other.yaml` rows `other.amt_owed` (answers restated) and `other.amt_pab` (new), with `s2.amt_owed:
    false` dropped from 3 rows; `hsa.yaml` drops it from 1 row; `business.yaml` adds `s2.amt_business: false` beside
    each `s2.lookback: false` (6 rows) and a new row `business.amt_business_costs`.
  - `tools/coverage/tree.json`: the `s2.amt` row's question text.
  - `interview/2025/stage4.yaml` (legacy profile): `s2.amt_owed` replaced by `f1040.tax_exempt_interest`, `s2.amt_pab`,
    `s2.amt_boat` and `s2.amt_business`.
- **Code**:
  - `engine/src/generate.ts`: `s2.amt_business` is drawn in `s2.amt_owed`'s place among the root Bools, so the random
    stream is the one it was; `s2.amt_pab` and `s2.amt_boat` are not drawn.
  - `engine/src/umbrella-what-if.ts`: `s2.amt_owed` is taken out of an umbrella's list.
  - `tools/engines/generate_cases.py`: the `s2.amt` screen's questions, and `s2.amt_pab` zeroed.
- **Params**: `params/2025.yaml` gains `amt.exemption`, `amt.phaseout_start`, `amt.rate_25`, `amt.mfs_addback_start`,
  `amt.mfs_addback_max`, `amt.bracket`, `amt.bracket_subtract`, `amt.rate_26` and `amt.rate_28`. They have no 2026
  values yet: the 2026 track must stage them. `year_changes.py --check` passes. No 2026 operation names a line changed
  here.
- **Generated files regenerated here**: `reports/2025/citations.{md,html}` and `reports/2025/input_quotes.md` (by
  `citations.py --strict`), `canonical/` (by the build), and `rendered/2025`, `rendered/ny/2025` (render after the last form edit).

## 1. T-307: real (verified)

`s2.amt_owed` asked every filer "Do you … owe alternative minimum tax for 2025, or have to file Form 6251 for it?".
Answering requires lines 1 to 10 of Form 6251 (i6251 p. 1, Who Must File). Real, as the task row says.

**The fix (decision D2).** Read the design note for the argument. In brief:

- Statements 2 and 3 of Who Must File cannot arise on a return the tool completes: the credits involved are refused.
- Statements 1 and 4 are decided by an upper bound on Form 6251 line 7 against line 10:
  - Part I: lines 1a, 1b, 2a and 2b computed; private activity bond interest asked; depreciation (2l) and related
    adjustments (3) bounded by the regular-tax amounts.
  - Part II: the Exemption Worksheet and the MFS add-back computed.
  - Line 7: Part III with the regular worksheet amounts when the return used a capital gain worksheet, otherwise the
    flat 26%/28%.
  - Line 10: computed without line 1z, a lower bound.
- `s2.amt` (the gate every refusal names) = ISO items (unchanged) or `s2.amt_owed` (now derived: boat or RV mortgage
  interest, or a business's circulation, mining or drilling costs) or `s2.amt_tmt_over` (line 7 bound > line 10).

**Questions (`s2.yaml` lines; bank prompts):**

| id | asked of | prompt |
|---|---|---|
| `s2.amt_pab` (amount) | tax-exempt interest > 0 and the flat bound, with all tax-exempt interest and all mortgage interest added, above line 10 | "How much of your (or, on a joint return, your spouse's) tax-exempt interest is from private activity bonds? Add up box 9 of your Forms 1099-INT. Zero if none." |
| `s2.amt_boat` (refuses) | itemizing with mortgage interest, same bound | "Is any of the mortgage interest you (or, on a joint return, your spouse) deduct for a boat, a motor home or another recreational vehicle that was not your main home?" |
| `s2.amt_business` (refuses) | a Schedule C on the return | (form label) "Do you (or, on a joint return, your spouse) deduct in a business costs of building the readership of a newspaper, magazine or newsletter, costs of exploring for or developing a mine, or costs of drilling an oil, gas or geothermal well?" |

**Effect on the walk.** The filer with no Schedule C is asked nothing about the alternative minimum tax; a Schedule C
filer is asked one short question (order 267, after `s2.lookback`). The persona walks were not re-run here (time on a
loaded machine); the coordinator's integration walk should confirm.

**Over-refusal by design.** The bound refuses where Form 6251 may be needed:

- business filers with 200%-DB property whose AMTI bound crosses (D also counts property eligible for the special
  allowance, which has no adjustment);
- with depreciation present, the related-adjustment bound (section 179, SE retirement, SE health insurance, IRA
  deduction);
- line 10 without line 1z.

A refinement (150% DB tables from Pub. 946) is not built.

## 2. T-310 (l7b): real (verified)

`s2.mortgage_subsidy` was gated on `s2.has_mortgage_interest` (Schedule A line 8a > 0). So a filer who sold a
subsidized home in 2025 after paying off the loan, or with no Form 1098 interest in 2025, was never asked. Form 8828
recapture does not depend on the loan still being open (i1040gi p. 113, Line 17b, "If you sold your home in 2025 and it
was financed …").

**Fix.** The gate `s2.mortgage_subsidy_if_interest` (id kept) now reads `sa.home_asked`: owned a home or other real
estate at any time in 2025, or paid interest on a loan secured by a boat, camper or mobile home. That is a superset of
`line 8a > 0`, so no path that reached the question is lost. `s2.has_mortgage_interest` is removed: the build refuses an
unread helper. The cost: homeowners with no mortgage interest now answer one more short question.

## 3. New pending bugs

None filed. Found and not fixed, outside the lane:

- Form 2555 is refused (bank line 725), but the qdcg note still says its alternatives are "outside Stage 1 and not
  encoded". This is consistent, and is noted only.

## 4. Verification (this worktree, after the last model edit unless noted)

- `npm run compile`, `node engine/dist/main.js build`: Build OK.
- `test-fixtures`: 2008/2008 pass. The 5 new hand-predicted cases (`s2.reg.amt_pab_owes`, `_pab_below`,
  `_wages_none`, `_dividends_owes`, `_dividends_part3_none`) passed on their first run, so the predictions held.
- `test-fixtures --ny`: 357/357. This ran before the line 10 and s8812 restatements, which do not touch New York
  cases. It was not re-run.
- `interview-rules`: 0 problems. `tick-groups`: pass.
- `python3 tools/citations.py --strict`: 0 findings, 0 locator segments to rewrite.
- `python3 tools/year_changes.py --check`: all 1256 operations apply.
- `check_consumers.py`: 0 new, 0 stale, after one ruling was added and three stale ones removed in
  `reviews/2025/consumers.json` (by key). Added: `consumer:f1040.status@i6251:p9`, verdict same. Removed: the three
  `consumer:s2.amt_owed@…` rulings, which the check reported stale.
- `render` and `render --ny`; then `check_questions.py`, `check_screens.py` and `check_false_no.py`: pass.
- `interview-order --self-test`, `tools/engines/test_compare.py`: pass.
- `siblings.py --check` and `check_bug_inventory.py` fail only on entries from the base tree (ty26-o2/o3b/o5/o6/o8/
  o9/p2/r2 and landing-04 to 13 pending files). No bug file was touched here. Not re-run on the untouched base, so
  "pre-existing" is inferred from the entries named.
- **`interview-coverage`: 25 problems on the run before the last edits. 15 were incomplete rows; their answers are now
  stated (the vehicle/equipment `business` set, 2 home rows and 1 credits row, `other.amt_owed`, `other.amt_pab`,
  `business.amt_business_costs`). That fix was not re-run (a run takes over an hour on the loaded machine). The other
  10 rows wait on the coordinator's decision in section 5: `other.credit_recapture`, `other.household_employee`,
  `other.other_tax`, `other.w2_uncollected_tax`, `hsa.testing_period_no_account_left`, `hsa.prior_year_excess` and the 6
  `saving.*` rows with `person.x_other` refusals.**
- `mutate` was **skipped** (slow under the machine's load; expressions changed only in s2 and person). Round 2 or
  integration should run it.

Restated case inputs (the 58 cases):

- `f1040.tax_exempt_interest: 0`: classm.f2441.1, f2441.2.deepseek, f8880.3(.deepseek), f8880.4(.deepseek), f5695.2,
  .3, .5 to .17, f5695.*.deepseek, f8863.3(.deepseek), s3.10, s3.11, s2.3, mutation.m4.f5695.* (6),
  mutation.m3.sa.no_mortgage_property_tax.
- `s2.amt_business: false`: classm.f1040.4(.deepseek), f1040.6.deepseek, s8812.1(.deepseek), s3.8.
- Both of the above: classm.s2.1, classm.s2.4.
- `s2.mortgage_subsidy: false`: classm.f5695.1, s2.2, tipjob.1, f1040.4.
- `s2.amt_boat: false` (with `tax_exempt_interest: 0`): classm.f5695.11, s3.2.

## 5. For the coordinator to decide

1. **Refusals that reach Schedule 2 line 21 now arrive later, and interview-coverage fails 10 rows on it.** Lines 2, 3 and 21 refuse on `[s2.amt, s2.other]` in that
   order. `s2.amt` is now known only once the return's tax is known. So a Yes to an `s2.other` item (household
   employee, W-2 marks, recapture, other tax) is told only after the rest of the return is answered. Before, it was told
   at once, because `s2.amt_owed` had already been answered No. That conflicts with N11, and it is protocol 3.1(a)'s
   case. The remedy is to put `s2.other` first on lines 3 and 21 (or give the AMT a line of its own). It **changes one
   existing value**: `stage4.refuse.s2.amt.simultaneous` (both screens true) expects `s2.line3` and `s2.line21` to
   refuse on `s2.amt`, and they would refuse on `s2.other`. The Form 5329 refusals (`person.x_other`) wait as well, because they reach line 21 through its
   expression, which is evaluated only after line 21's gates are settled.

   The proposed fix:
   - `s2.line21` stops refusing on `s2.amt`. The AMT is line 2, which is not in line 21's sum ("Add lines 4, 7
     through 16, 18, and 19"); line 2 and line 3 still carry it.
   - `s2.line3`'s refusal list becomes `[s2.other, s2.amt]`.
   - Incentive stock option refusals are unaffected (`any` stops at the first Yes).

   Existing values it changes, 4 in 3 cases (by a scan of every fixture's `s2.amt` expectations; not run):
   - `stage4.refuse.s2.amt`: `s2.line21`, from refusal(s2.amt) to its money value;
   - `s2.reg.iso_vested_2025`: `s2.line21`, the same;
   - `stage4.refuse.s2.amt.simultaneous`: `s2.line21` and `s2.line3`, from refusal(s2.amt) to refusal(s2.other).

   Not done, per the brief. Recommendation: make it. The alternative is that every Schedule 2 and Form 5329 refusal
   is told only after the whole return is answered. Record it in DECISIONS.md and restate those 4 expectations.
2. The design's soundness arguments (monotonicity of Part III under the regular amounts; that a stock-sale 2k is never
   positive in scope) are argued, not machine-checked.

## 6. Reviews for round 2

- **s2**: transcription, render and class M. Most of the form's lines are new (about 100), and its question and gates
  changed.
- **person**: transcription and render, on the 7 new lines only (line-scoped).
- The sampled reviews at the release: question (3 new questions, 2 changed gates), screen (`s2.amt`), false-no
  (`s2.amt_pab`, `s2.amt_boat`, `s2.amt_business`, `s2.mortgage_subsidy`).
- `params/2025.yaml`: the `amt.*` quotes are checked by `citations.py`; no review family covers params.

## 7. After the coordinator's decision (2026-11-15)

**Made as approved.**
- `s2.line21` no longer refuses on `s2.amt`; `s2.line3` refuses on `[s2.other, s2.amt]`; `s2.line2` is unchanged
  (`[s2.amt, s2.other]`).
- Four expected values restated from the source, each case's evidence noting the decision:
  - `stage4.refuse.s2.amt` and `s2.reg.iso_vested_2025`: `s2.line21` = $0. Form 8959: Medicare wages $200,000 do not
    exceed the $200,000 threshold. Form 8960: no investment income. No SE, Form 5329 or HSA tax.
  - `stage4.refuse.s2.amt.simultaneous`: `s2.line21` and `s2.line3` refuse on `s2.other`.
- Recorded in `docs/provisional/DECISIONS.md`, new section 4, with the N11 reason and the f1040s2 line 21 text.

**Coverage rows completed.** The `s2.other` refusals now come at once, so these are mechanical:
- `other.w2_uncollected_tax`: 4 stale answers dropped.
- `other.amt_owed` and `other.amt_pab`: the W-2 and dividend answers their walks open.
- `business.amt_business_costs`: a stale `qbi.suspended` dropped.

**Checks** (build OK after the edit):

| Check | Result |
|---|---|
| `test-fixtures` (federal) | 2008/2008, the four restated values included |
| `test-fixtures --ny` | 357/357 |
| `interview-rules` | 0 problems |
| `tick-groups` | pass |
| `interview-coverage --rows`, hsa, home, credits, vehicles_equipment, saving | 0 problems each; the 6 saving and 2 hsa timing rows now pass |
| `interview-coverage --rows`, business | 0 problems after the stale answer was dropped |
| `interview-coverage --rows`, other | 3 problems: `other.iso_kept` and `other.iso_vested_2025` (the ISO wait below); `other.amt_owed` still incomplete. Its $1M of dividends opens the Form 8960 questions; the last run stopped at `f8960.refund`, and a few more answers are needed. Each attempt is a run of several minutes under the load. |

**A cost the decision moved and did not remove (for the coordinator).** "ISO refusals unchanged" holds for line 2 only.
Line 3, which feeds Form 1040 line 17, now checks `s2.other` first. So a Yes to `s2.iso` or `s2.iso_vested` is told
only after every `s2.other` item has been answered: those items are asked at orders 145 to 291, so a filer who
answered Yes at order 146 goes on for most of the interview. Coverage rows `other.iso_kept` and
`other.iso_vested_2025` fail on it. They are not restated, because restating their answers would hide the wait.

Options:
- **(a)** Accept the wait and restate the two rows.
- **(b)** Give `s2.line3` no refusal entries of its own, keep `s2.line2` refusing on `s2.amt` only, and refuse on
  `s2.other` at `s2.line1z`, which carries Schedule 2 Part I items 1d to 1y. Line 3's sum then returns whichever
  operand refuses first, so both refusals arrive at once. This changes more existing values: every `s2.line2`
  expectation of an `s2.other` refusal, and `s2.line1z` wherever `s2.other` is true. They are not measured here.
- **(c)** Leave the order as approved and give ISO its own gate id. This changes the `gate` field of the ISO cases'
  `s2.line3` expectations.

Not done; it needs the coordinator's choice.

**`mutate`:** not run. It has no per-form option, and a full run takes hours on the loaded machine. The integration's
full run covers it.

**Legacy profile:** `interview/2025/stage4.yaml` is deleted by lane T7, so the edits to it are dropped at the merge.
