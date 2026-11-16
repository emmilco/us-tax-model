# Lane D1-k1block: the 13 missing K-1 readiness items, as atomic patches

Lane D1-k1block. Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Written 2026-11-16, round 5.
Nothing in the repository, xint or `.git` was written. No build, engine run, fixture run, walk, check or review was run,
and no paid call was made. Every predicted value is hand arithmetic.

Tags:
- **[C path:line]**: checked against that file.
- **[S]**: checked in scratch. That covers YAML/JSON parsing, reference resolution, the display rule, gated-input
  readers, cycles, bank duplicates and group sizes, fixture and row input names, tree placement, and sequential
  application.
- **[I]**: inferred, not checked.

## Summary

- **Ten patches, all in `P/patches/v4/`.** Apply them in this order on the round-5 base (xint plus the fix round,
  `P/scratch/b-chain/work/`), after k1int-1, k1int-2 and k1int-4:
  - **`k1block-0-k1int3-rebased.patch`**: k1int-3 rebased. **v3 `k1int-3-return.patch` does not apply cleanly to the
    round-5 base.** One f1040 hunk fails with `-F0`, because the fix round renamed `f1040.tax_exempt_interest` to
    `f1040.tax_exempt_interest_if_any` at line 2a. The rebased patch has exactly the same +/- lines; only the context
    changes [S]. Land it in place of v3 k1int-3.
  - **`k1block-1` to `k1block-9`**, one unit each (section 2).
- **Sequential test [S].** The base copy plus k1int-1, k1int-2, k1block-0, k1int-4 and then k1block-1…9, applied with
  `patch -p1 -F0`, is byte-identical to the scratch tree `u9`. Every patch applied clean, and no file was left
  rejected or as `.orig`.
  - The static checker (`P/scratch/round5-k1block/check.py`) found **0 new findings after any unit** compared with the
    tree before it. It also found 0 new cycles across all forms.
  - The k1int stack alone left 3 gates unplaced in `tree.json`. Unit 9 places them.
  - Not run, because the rules forbid it: build, test-fixtures, walks, citations, tree.py, check_consumers,
    interview-coverage, tick-groups.
- **The lift (unit 1):**
  - `scope.k1` now asks about partnerships and S corporations only, and it leaves `scope.schedule1`.
  - A new `scope.k1e` (estate or trust) takes its place in `scope.schedule1`, so estates and trusts are still refused.
  - Every K-1 total that a return-level form reads is gated behind `scope.k1` Yes. Without that gate, every filer would
    have been asked both K-1 rosters, because after k1int-3 `sche.filed`, `sche.any`, `person.se_pos_whole` (read for
    every Schedule C) and `person.k1_se_any` read the rosters ungated [C k: sche.yaml:495-532, person.yaml:2325,8322].
- **Found while drafting:**
  - (a) **Two readers relied on `scope.schedule1` to refuse every K-1** and would have computed silently after the
    lift. Unit 1 gives each its own gate:
    - `s1a.line5_calc`, qualified tips in a trade or business: "with Schedule C, E or F" [C s1a.yaml:441].
    - `s8812.eiw_3`, the Earned Income Worksheet, whose remedy names "partnership income" [C s8812.yaml:595].
    - The other readers of `scope.schedule1` were checked:
      - f1040 lines 8 and 10 are now correct.
      - eic already refuses through `sche.any`.
      - ssb line 6 is not affected.
      - The f2441 notes are stale text only.
  - (b) **k1s box 17, codes A and B (investment income and expenses), are neither refused nor wired.** `k1s.box17_other`
    excludes A and B [C k1s.yaml:923-930]. Unit 6 refuses only partnership box 20 A/B, the readiness item. The
    S corporation sibling needs a new input or a broader refusal (decision O-1 below).
  - (c) **`classm.tipjob.1` states `scope.k1: true`** [C fixtures/2025/classm.json:65854]. It asserts only tipjob lines,
    so its expectations should not move. After the lift it describes a person with a partnership K-1 and an empty roster.
    It was left unchanged; check it at test-fixtures.
- **Not done here, needing runs or another lane:**
  - K-1 personas and walks (protocol section 7, items 1 and 8).
  - Schedule E line 27/28 rendering (item 22).
  - Class M and mutation for k1p, k1s and f8582 (item 36).
  - BUG-0836 (item 12), which is lane A's.
  - The box 14 A self-employment wiring (item 29, D2). The interim refusal from k1int-3 stays.

## 1. The 13 missing items and where each went

| # (k1int.md) | Item | Disposition |
|---|---|---|
| 3 | k1e | Not needed for the lift: estates and trusts stay refused through `scope.k1e` in `scope.schedule1` (unit 1). **The k1e lane must restate its 19 fixtures and 11 parked rows from `scope.k1` to `scope.k1e`** [C k1e.md:30-31] |
| 11 | Form 8582 exception with K-1 Part V passive income | Unit 8 |
| 12 | BUG-0836 (MFS lived together) | Lane A; still a prerequisite of the lift [C k1int.md:74] |
| 20 | `qbi.unsupported` label | Unit 7 (and the tree question) |
| 22 | Schedule E line 27/28 rendering | Not drafted: the render mechanism is not read [I]. Plan step L9 |
| 25 | `f1040.line25c_other` double count | Unit 3 |
| 26 | Form 1040 line 3a (D3) | Unit 4, plus the restatement script |
| 29 | Box 14 A self-employment | Interim refusal kept (k1int-3). Unit 1 adds the Schedule 8812 sibling refusal. Wiring is L3 (D2) |
| 31 | `f8960.unsupported` | Unit 5 |
| 32 | Form 4952 box 20 A/B | Unit 6 (k1p). The k1s sibling is open (Summary, finding b) |
| 34 | `scope.k1` split, lift, roster gating, `scope.passive`, coverage rows, personas, walks | Units 1, 2 and 9. Personas and walks are not drafted |
| 35 | tree.json placement of the new gates; consumers rulings | Units 1, 6 and 9 (tree); units 1, 2, 5 and 6 (rulings) |
| 36 | Class M and mutation | Runs only; listed under "What to run" |

## 2. The units, in landing order

Scratch is `P/scratch/round5-k1block/`:
- `base/` is the round-5 base: xint plus `b-chain/work`, plus `reviews/2025/consumers.json` and the four line-3a tool
  files copied from xint.
- `k/` is the base after k1int-1, k1int-2, the rebased k1int-3 and k1int-4.
- `u1` … `u9` are the trees after each unit.
- `gen.py` regenerates every unit from `k/`.
- `restate_line3a.py` is the line-3a restatement, run by unit 4.
- `check.py` is the static checker.
- `seq/` is the sequential-application tree.

### Unit 1: `k1block-1-lift-gate.patch` (18 files): split `scope.k1`, lift it, gate the rosters

Model:
- **scope.yaml.**
  - `scope.k1` asks: "In 2025, did you (or, on a joint return, your spouse) have income or a loss from a
    partnership or an S corporation? A paper called Schedule K-1 (Form 1065 or 1120-S) reports it."
  - The new `scope.k1e` asks the same about "an estate or a trust … Schedule K-1 (Form 1041)".
  - `scope.schedule1` reads `scope.k1e` in place of `scope.k1`.
- **person.yaml.** Each of the 23 `person.k1_*` totals that return forms read is gated:
  - The existing sum is renamed `<id>_sum`.
  - `<id>` becomes `choose(scope.k1 Yes → <id>_sum; No → person.zero)`. This is the `person.f8919_wages` pattern
    [C person.yaml:1030-1049].
  - The new `person.k1_se_pos` gates `k1p_total_se_pos` for `person.se_pos_whole`.
  - `person.k1_se_any` becomes `all(scope.k1 Yes, 14 A ≠ 0)`.
- **sche.yaml.** The K-1 row count in `sche.any` and `sche.filed` is tested only under `all(scope.k1 Yes, …)`.
  - `all` stops at a false operand, and the reach pass stops after an unknown one [C engine/src/eval.ts:793-803].
- **Guards that were the schedule-1 proxy:**
  - `s1a.line5_calc` refuses on `scope.k1` (qualified tips with a partnership or S corporation K-1).
  - `s8812.eiw_3` refuses on the new `s8812.k1_se`, a count of the people with `person.k1_se_any`.
- **sd.yaml.** Two stale locator parentheticals now name `scope.k1e`.

Interview, defaults and records:
- **Bank.**
  - The `scope.k1` tick reads "A Schedule K-1 from a partnership, LLC or S corporation". Its help: "An LLC or an
    investment fund that sends you a Schedule K-1 (Form 1065) counts as a partnership. Each K-1 is asked about later,
    with your other business income." "A Yes ends the interview here" is gone.
  - `scope.k1e` joins the same `own_income` group at seq 3, with the tick "A Schedule K-1 from an estate or trust" and
    a refusing help.
  - farm moves to seq 4 and `rent_personal` to seq 5. Order 130 seqs 5-10 were free [C questions.yaml].
  - The group grows from 3 to 4 members (limit 6) [S].
- **Defaults.** `scope.k1e` false.
- **tree.json.**
  - The `scope.schedule1` question and stop are restated; they no longer name partnerships, S corporations or rentals.
  - New placements: `scope.k1` (topic `schedule_1a`, as the s1a gate) and `s8812.k1_se` (topic k1).
- **consumers.json.**
  - The 7 rulings on `scope.k1` reached through `scope.schedule1` are re-keyed to `scope.k1e`, with the question phrase
    updated. The i1040se p. 1 reason is rewritten.
  - **6 new pairs** for `scope.k1` are drafted "same", each with a question phrase, a source phrase and a reason. They
    were computed with `check_consumers.findings` logic over the scratch forms [S]. **Adjudicate them**:
    i1040gi p40, i1040se p9, i8582 p9, i8995 p2, i8995 p4, i1040gi p104.

Fixtures (inputs only; no expected value edited):
- **`k1int.json`.** All 9 cases gain `"scope.k1": true` (each has a K-1). Every k1int.md prediction stands, because
  the gate passes the same sums [I].
- **`s1a.json`.** The 2 cases that used `scope.k1: true` only to reach the `scope.schedule1` refusal now state
  `scope.k1: false` and `scope.k1e: true`. The refusal stays the same, and the evidence notes say so.
- **`f1040.json`** (4 cases) **and `s3.json`** (3 cases) withheld `scope.k1`; they now also withhold `scope.k1e`.

New cases in `fixtures/2025/k1block.json`, single filer, defaults otherwise:

| Case | Inputs | Expected (derivation) |
|---|---|---|
| `k1block.gate_off` | scope.k1 No; `$k1p` and `$k1s` withheld (null) | `person.k1_interest` 0 and `k1_col_k` 0 through the gate without the rosters; `sche.filed` false (no rental, scope.k1 No); `s1.line5` 0 (`s1.zero_ebl`). **The gating proof** |
| `k1block.lift_portfolio` | scope.k1 Yes; LP; box 5 $300 | `scope.schedule1` false; `person.k1_interest` 30,000¢; `sb.line2` 30,000¢ (no other interest by default, as `k1int.sche_part2` assumes) |
| `k1block.estate_refuses` | scope.k1e Yes | `scope.schedule1` true |
| `k1block.s8812_partner_se` | the inputs of `k1int.se_14a_refuses` | `person.k1_se_any` true; `s8812.k1_se_count` 1; `s8812.k1_se` true |

Coverage rows (end changes are made under the lift decision, as N9 allows only by owner decision; see D6):
- `scope.k1`: end changes from `refused: scope.schedule1` to `proceeds: {scope.k1: true}`.
- New `scope.k1e`: a trust beneficiary; `refused: scope.schedule1`.
- `scope.estate_excess_deductions`: the answer changes from `scope.k1` to `scope.k1e`; the end is unchanged.
- `credits.partnership_credit`: restated to a box 15 credit. The end moves to `person[taxpayer].k1p[firm].r_b15`.
- `business.qbi_other_income`: restated to a publicly traded partnership. The end moves to
  `person[taxpayer].k1p[mlp].ptp`.

Unverified [I]:
- that `"$k1p@person[taxpayer]": null` withholds a roster in a fixture;
- that row answers which leave the other K-1 boxes unstated take their defaults, as the parked rows assume.

Walk effect [I]:
- The one-W-2 filer gets the same number of steps: one more tick label on the existing screen, 8 words.
- A K-1 filer now reaches the order-264 rosters in place of a refusal.
- A filer with only an S corporation K-1 answers an empty partnership roster (one step). Splitting the parent further
  is possible but not done.

### Unit 2: `k1block-2-passive.patch` (4 files): `scope.passive`

- **Label and source:** "… have income or a loss from, or sell, a business you owned but did not help run and that
  sent you no Schedule K-1 (a 'passive activity')?"
- **Help:** "A partnership or S corporation that sent you a Schedule K-1 is asked about with the K-1. Count a loss held
  back in an earlier year from a business or rental you no longer had in 2025. A Yes ends the interview here." (38
  words.)
- **Who could answer No wrongly:**
  - Someone with a loss held back from a partnership disposed of before 2025. No K-1 came in 2025, so the help's second
    sentence counts that loss.
  - A K-1 holder's own held-back losses are asked per K-1 (`prior_any`).
- **Coverage row `scope.passive`:** the situation now says the business sent no K-1. Answers and end are unchanged.
- **consumers:** `scope.passive@i8582:p1` question phrase and reason refreshed.
- **Fixtures:** none needed. The input is unchanged, and the 11 cases and rows that state it keep their meaning.

### Unit 3: `k1block-3-line25c.patch` (2 files): K-1 backup withholding entered once

- `f1040.line25c_other`: label and source drop Schedules K-1. The source says K-1 backup withholding "is entered with
  the K-1".
- `f1040.withheld_other_any`: the source drops K-1. `line25c_other_if_withheld_other`: the label drops K-1.
- **Bank:**
  - `line25c_other`: the prompt drops K-1; the help adds "and backup withholding on a Schedule K-1, which you entered
    with the K-1".
  - `withheld_other_any`: the help is **trimB's text** [C round4/trimB.json] with the K-1 clause removed (37 words).
- **Trim interaction:** the hunk is written against the untrimmed base. If trimB lands first, this one bank hunk must
  be rebased; its new text already includes the trim.
- **Fixtures:** none. Inputs are unchanged, and a K-1 filer who once had to put box 15 O / 13 O into line 25c_other
  would now be counting it twice (N8).

### Unit 4: `k1block-4-line3a.patch` (42 files): Form 1040 line 3a with K-1 qualified dividends (D3)

Model:
- **f1040:**
  - The input `f1040.line3a` becomes `f1040.line3a_entered` ("Qualified dividends entered from Forms 1099-DIV").
  - Its gate becomes `f1040.line3a_entered_if_ordinary`, replacing `f1040.line3a_if_ordinary`.
  - The new `f1040.k1_qual_div` is a sum over person of `person.k1_qual_div`.
  - `f1040.line3a` (printed 3a) becomes `sum(entered gate, k1_qual_div)`.
- **Readers moved to the printed line `f1040.line3a`:**
  - `f1040.gate.qdcg_applies`
  - `f4952.line4b`
  - `qdcg`
  - `qbi` (net capital gain)
  - `sdtw`
  - `sd.line22`
- **div.yaml keeps the 1099 part** (`line3a_entered_if_ordinary`) in 3 places: the box 1b display line and the
  "qualified greater than ordinary" check. Both are about the 1099-DIV itself.
- **person:** new `person.k1_qual_div_sum` and the gated `person.k1_qual_div`. `display` is dropped from
  `k1p_total_qual_div` and `k1s_total_qual_div`.

Interview and defaults:
- **Bank:** the entry is renamed. Its help adds "Leave out dividends on a Schedule K-1."
- **Defaults:** the input is renamed. No consistency rule names it [C defaults.json].

**Restatement (mechanical, `restate_line3a.py ROOT`, idempotent).** It renames the *input* only; the counts are from
the scratch run [S]:

| Where | Count | How |
|---|---|---|
| Fixture `inputs` objects, 2025 | 530, in 15 files | JSON scanner, so key paths are respected |
| Fixture `inputs` objects, ny | 209, in 3 files | same |
| Expectations keyed `f1040.line3a` (household 1, qdcg 59, returns 8) | 68 | **Not touched.** They name the printed line, whose value is unchanged without a K-1 |
| Coverage rows | 21 | all occurrences, including `not_asked` |
| Personas | 3 | all occurrences |
| `engine/src/generate.ts` | 2 | input name |
| `tools/engines/generate_cases.py`, `tools/ny_fixtures.py` | 2 | input name |
| Adapter contract `div.json` | 2 | input key |
| Adapter contract `f4952.json` (5) and `tools/transcription/test_review_tools.py:1161` (1) | 6 | Boundary line `f1040.line3a_if_ordinary` → `f1040.line3a`, because Form 4952 line 4b now reads the printed line |

The total is 775. k1int.md counted "599 facts in 16 files" [C k1int.md:88], which looks like a narrower count (2025 only,
no class M copies) [I]. The script's selection is what lands.

The review logs keyed on the old input are carried by the rename rule [C tools/README.md:370-385], or fall due.

Fixture `k1block.line3a_k1`:
- Inputs: LP, box 6a $1,000, box 6b $800, no 1099-DIV.
- Expected:
  - `person.k1_qual_div` 80,000¢; `f1040.k1_qual_div` 80,000¢.
  - `line3a_entered_if_ordinary` 0 (`div.has_ordinary` false).
  - `f1040.line3a` 80,000¢.
  - `f1040.line3b` 100,000¢ (`sb.line6` = K-1 ordinary dividends) [I: `person.k1p_total_ord_div` sums box 6a].

### Unit 5: `k1block-5-f8960.patch` (3 files): the Form 8960 screen

- The item "annuity, business or pass-through income" becomes "annuity income, or business income other than from a
  partnership or S corporation Schedule K-1".
- "Business" is kept for Schedule C. Line 4a takes Schedule 1 line 5 only, so Schedule 1 line 3 is still refused here
  [C k: f8960.yaml:188-197; sources i8960.txt:497-510].
- The tree question and the consumers ruling `f8960.unsupported@i8960:p8` are refreshed.
- **Fixtures:** none. Cases that state `f8960.unsupported: true` keep their refusal.

### Unit 6: `k1block-6-f4952.patch` (5 files): Form 4952 and K-1 box 20 A/B

Model:
- New `f4952.k1_inv_count`: a sum over person of `person.k1p_count_inv`. Its `display` is dropped.
- New gate `f4952.k1_inv` = `all(scope.k1 Yes, count > 0)`.
- The gate refuses at lines 2 and 5 and at `required_test`, after `f4952.unsupported` and before
  `alternative_allocation`.
- **Cite:** f4952 p. 3, "Include investment income reported to you on Schedule K-1 from a partnership or an S
  corporation". The words were checked against `sources/2025/f4952.txt:59-62` (p. 3) [C].

Records:
- **tree:** `f4952.k1_inv` is placed under deductions.
- **consumers:** the new pair `scope.k1@f4952:p3` is drafted.

Fixture `k1block.f4952_k1_inv` (box 20 A/B ticked): `k1_inv_count` 1 and `k1_inv` true.

The refusal itself is not asserted, so the f4952 snapshot hash was not guessed. The refusal shows only when investment
interest is claimed.

### Unit 7: `k1block-7-qbi-label.patch` (2 files)

The `qbi.unsupported` label and its tree question now say that K-1 QBI is figured. PTP income is refused on the K-1
(item D); estate, trust and Schedule F income are refused by scope. This is text only.

### Unit 8: `k1block-8-f8582-exception.patch` (2 files)

The filing exception fails when `f8582.line2a_k1` > 0, which is K-1 passive income in Part V. The i8582 p. 1 condition
is that rental real estate with active participation was the only passive activity.

The label is updated. Amounts do not change: line 9 already equals the loss when the exception holds [C k1int.md:73].

Fixture `k1block.f8582_k1_income_breaks_exception`:
- Inputs: `k1int.p4_allowance`'s general partner (box 2 −$12,000, active), plus a limited partner with box 1 +$5,000
  (passive).
- Expected:
  - `line1b` −1,200,000¢; `line2a_k1` 500,000¢.
  - `exception` false; it would hold without the second K-1, since line 4 is 12,000 and MAGI is under $100,000.
  - `required` true (a net loss is a deduction).
- Existing cases: `k1int.p4_allowance` has no Part V income, so it keeps `required` false [C k1int.json:67-131].

### Unit 9: `k1block-9-coverage.patch` (4 files): rows, categories (D7), tree

- **`interview/2025/coverage/k1p.yaml`:** the 10 parked x2-k1p rows, moved, with only the "not yet in coverage" header
  removed. They were written before v2 k1p (BUG-0837…0843) changed some questions, so `interview-coverage --rows` may
  ask for answer restatements; the ends must stand [I].
- **`interview/2025/coverage/k1s.yaml` (new, 4 rows):**

  | Row | End |
  |---|---|
  | `k1s.refuse_multi` | `…k1s[acme].multi` |
  | `k1s.refuse_disposed` | `…k1s[acme].disposed` |
  | `k1s.portfolio_interest` | proceeds `box4` 25,000; `work` and `hours500` not asked |
  | `k1s.refuse_box10` | `…k1s[acme].box10` |

  The gate names come from tree.json [C].
- **`categories.json`, `partnership_scorp`:** `refused: false`, `gates: []`. The label follows the `schedule_c` form:
  "supported …; its remaining refusals, among them partnership self-employment earnings, are unmeasured gates"
  [C categories.json:81-107].
- **tree.json:**
  - The "Business and property" table row covers partnership and S corporation K-1s. Its refused entry is reduced to
    "An estate or trust (Schedule K-1 from Form 1041)" (`estate_trust`).
  - The k1int gates `k1p.qbi_release`, `k1s.qbi_release` and `person.k1_se_any` are placed. They were the 3 unplaced
    gates [S].
- README and docs/COVERAGE.md are generated: run `tree.py` at landing.

## 3. Decisions taken under delegation

| Decision | Report's recommendation | Taken | Why / alternative |
|---|---|---|---|
| D6, `scope.k1` split | Split: "partnership or S corporation" and "estate or trust", with `scope.k1e` staying in `scope.schedule1` [C k1int.md:217, 257-258] | Split. **The id `scope.k1` is kept for partnership/S corporation; `scope.k1e` is new** | k1int-3 already names `scope.k1e` [C sche.yaml:364], and the 10 parked k1p rows use `scope.k1: true` as written. Cost: the 2 s1a cases are restated, and an old saved log's "Yes" changes meaning. The alternative is two new ids with `scope.k1` retired: more restatement and no gain |
| D3, line 3a | Option 1: rename the input to `_entered` and sum the K-1s, restated by script [C k1int.md:249-251, 218] | Option 1. Readers take the printed total, except the two 1099-DIV self-checks | Sub-decision: div's box 1b display and its "1b > 1a" check keep the 1099 part, because the K-1 dividends are not on any 1099 |
| D7, `partnership_scorp` | No explicit recommendation; three options [C k1int.md:259-260] | Option 1, `refused: false`, as `schedule_c` does | This overstates while 14 A is refused (D2). Option 2 (keep it refused until D2 is wired) is the conservative choice. **Owner, please confirm** |
| L4, Form 4952 | "refuse K-1 box 20 A/B … or wire it", sized as the 0.5 h mechanical step [C k1int.md:220] | Refuse | Wiring needs Form 4952 lines 4a and 5 from K-1 amounts that are not asked |
| f8960 wording | "drop 'pass-through', keep 'business' for others" [C k1int.md:217] | As recommended | — |
| D2 (box 14 A) | No recommendation; options [C k1int.md:245-248] | Not taken. The interim refusal stays, and the Schedule 8812 sibling refusal is added | Wiring is L3 |
| New: s1a tips with a K-1 | — (found here) | Refuse `s1a.line5_calc` on `scope.k1` | This over-refuses a W-2 tip earner who also has any K-1 (rare). Alternative: a narrower gate on nonpassive K-1 income |
| New: f8582 exception | — (readiness item 11, no recommendation) | Test K-1 Part V income | Only whether the form is filed changes |

## 4. Reviews made due

These follow CLAUDE.md: line-scoped transcription and render on changed lines; class M where computation changed; one
review per form per round, after all of a form's fixes. Not priced; run `rerun_all.py --dry-run` first, since the
$3.00 gate applies.

| Unit | Transcription (line-scoped) | Render | Class M | Question / screen / other |
|---|---|---|---|---|
| 1 | scope (k1, k1e, schedule1); person (24 gated lines, `k1_se_pos`, `k1_se_any`); sche (any, filed); sd (2 locators); s1a (line5_calc); s8812 (2 new lines, eiw_3) | scope.k1/k1e wording; the s1a and s8812 refusals | person, sche, s8812 | Question review: scope.k1, scope.k1e. Screen review (sampled): scope.k1e, s8812.k1_se, scope.k1 as the s1a gate. Consumers: 6 drafted rulings, 7 re-keyed |
| 2 | scope.passive | wording | — | Question review; screen (scope.other_income member) |
| 3 | f1040 line25c_other, _if_withheld_other, withheld_other_any | wording | — | Question review: 2 bank entries |
| 4 | f1040 (3a, 3a_entered, gate, k1_qual_div); div; f4952.line4b; qdcg; qbi; sdtw; sd.line22; person (k1_qual_div) | f1040 line 3a | f1040, qdcg, sdtw, person | Question review: line3a_entered help; rename carry for logs keyed on the input |
| 5 | f8960.unsupported | wording | — | Question and screen review; consumers p8 |
| 6 | f4952 (2 lines, 3 refusal entries); person.k1p_count_inv | refusal text | f4952 | Screen review: f4952.k1_inv; consumers f4952:p3 |
| 7 | qbi.unsupported (label) | label | — | — |
| 8 | f8582.exception | label | f8582 | — |
| 9 | — | — | — | interview-coverage on k1p and k1s; estimate.py rerun (coverage headline) |

These come on top of k1int.md L6, the reviews for k1int-1..4 and v2 k1p/k1s. Because "one review per form per round"
applies, batch person, f1040, sche and f8582 with them.

## 5. What to run at landing (lane worktree, not tonight)

1. Build.
2. `test-fixtures`, federal and `--ny`: the k1int and k1block cases, the line-3a restated files, s1a, f1040 and s3
   (withheld scope answers), and classm (tipjob.1).
3. `citations --strict`.
4. `tools/check_consumers.py`.
5. `tree.py --check`, then `tree.py` to write.
6. `tick-groups`.
7. `interview-rules`.
8. `interview-coverage --rows` on scope, credits, business, k1p, k1s and the line-3a files.
9. `draft-walk` for persona 01: the step count is expected to be unchanged and the roster must not be asked.
10. `interview-order`.
11. `year_changes --check`. The 2026 changes do not name the renamed ids; one note mentions `scope.passive`
    [C changes/2026/f8582.yaml:15].
12. `tools/defaults_guard.mjs`: a rename and an added default.
13. Mutation and class M jobs for k1p, k1s and f8582 (item 36).
14. `estimate.py` (D7).

Then write the K-1 personas: a typical limited partner with a passive loss and portfolio income; an S corporation
owner-employee; a refused publicly traded partnership. Record their walks before and after (protocol section 7).

## 6. Owner questions

- **O-1.** S corporation K-1 box 17 codes A and B (investment income and expenses) are neither refused nor carried to
  Form 4952. Options:
  - (a) A new per-K-1 tick, asked only when box 17 has an amount: one step for most S corporation holders.
  - (b) Refuse Form 4952 whenever an S corporation K-1 shows box 17. This over-refuses, because box 17 V is common.
  - (c) Accept the gap. Missing code B overstates the investment-interest deduction.
- **O-2.** Confirm D7 option 1, or keep `partnership_scorp` refused until the box 14 A wiring (D2) lands.
- **O-3.** Confirm the coverage-row end changes in unit 1 (`scope.k1`, `credits.partnership_credit`,
  `business.qbi_other_income`). They are deliberate exceptions to N9 that come with the lift.

## Provenance

Inspected:
- COMMON.md rounds 1-5; k1int.md; k1e.md; the k1int-1..4 patches; the interview construction protocol.
- In xint: scope, person, sche, s1, s1a, s8812, f1040, f4952, f8960, qbi, f8582, sd, div, k1p and k1s at the lines
  cited.
- tree.json, categories.json, consumers.json and `check_consumers.py`; engine `eval.ts` (`all`/`any`) and `gates.ts`
  (gated inputs).
- `interview/README.md` on rosters and reach; parked k1p rows; defaults.json.
- i8960 pp. 7-8; f4952 p. 3; trimA/B.
- Every patch was generated from scratch copies and applied in sequence with `-F0`, reproducing `u9` byte for byte
  [S]. Static checks: 0 new findings per unit [S].

Inferred (unverified):
- that the build accepts every new line and type (for example a `choose` of a `Dollars` line with a `NonNegDollars`
  zero, which has the `s1.line5` precedent);
- every fixture value and the null roster withholding;
- that the row harness defaults the unstated K-1 answers;
- that the withheld-scope fixtures keep their first unknown (`scope.rental`);
- the walk effects and NY effects (none expected).

Gap: the static checker sees only form references. The build's own checks (type, gate shape, the tick-group walk rule)
are unrun.
