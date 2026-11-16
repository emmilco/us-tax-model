# Lane x2-k1p: the partnership Schedule K-1 (Form 1065), collection `k1p`

Model: claude-opus-5-5. Class: judgment. Year: 2025. Jurisdiction: us.
Worktree: `.claude/worktrees/x2-k1p`, detached at `825024d8` (x1-base snapshot). Not committed (per brief).
Not done: no paid reviews, no model calls from code; `tools/check_all.sh` not run (brief); mutate not run (brief:
runs at integration); persona walks not recorded (the topic is unreachable in this tree, see 1.1).
Design: `scout-k1.md` (lane K1 of its section 7). Decisions D-K1..D-K16 settled as the scout recommends
(`docs/provisional/DECISIONS.md`, section "Lane x2-k1p").

## 1. What the merge must know

1.1 **Nothing outside `k1p` and `person` reads the new lines.** `scope.k1` still refuses every K-1 filer through
`scope.schedule1`, unchanged, so no return's value moves and no k1p question is asked in any walk. The return-
integration lane wires the totals and only then removes `scope.k1` from `scope.schedule1`. The contract (also kept at `docs/provisional/lanes/x2-k1p_work/k1-wiring-k1p.md`; generator scripts in `x2-k1p_work/scripts/`), with every
line and its destination and the f8582-dependent lines to add, is `/tmp/k1-wiring-k1p.md` (copied below in section 7).

1.2 Shared files changed (all additive, own ids only):

| File | Change |
|---|---|
| `forms/2025/k1p.yaml` | new, 168 lines (owned) |
| `forms/2025/person.yaml` | 29 sum lines `person.k1p_total_*` / `person.k1p_count*`, in a block between `# --- k1p sums (lane x2-k1p) ---` comments before `collection:`; each has `display:` (unread until wired) |
| `interview/2025/questions.yaml` | frame `k1p`; 8 groups (`k1p_*`) at the end of `groups`; 72 bank entries, order 264, at the head of `questions` (comment-delimited) |
| `fixtures/2025/defaults.json` | `$k1p` and 71 `k1p.*` defaults appended. **Base caution applied:** the file is nx-b1's copy (the x1-base copy lacks 7 defaults) plus my additions; the additions alone are reproducible with `/tmp/x2-k1p/defaults_patch.py <worktree>` on any copy |
| `fixtures/2025/k1p.json` | new, 26 cases (owned) |
| `ambiguities/2025.yaml` | 6 entries `amb.2025.k1p_*`, appended |
| `reviews/2025/consumers.json` | 28 rulings `consumer:k1p.*` (verdict same; own lines only) |
| `tools/coverage/tree.json` | new topic `k1_partnership`; 28 gate placements (k1p only). The k1s lane may add a similar topic: merge to one "Partnership and S corporation Schedules K-1" topic if wanted |
| `docs/provisional/DECISIONS.md` | section "Lane x2-k1p" appended |

No order/seq collision: order 264 was free in the base; `seq` 1-96 used. Generators (rerunnable, idempotent) are
in `/tmp/x2-k1p/`: `gen_k1p.py`, `patch_person.py`, `patch_bank.py`, `defaults_patch.py`, `gen_fixtures.py` +
`run_cases.py --fill`, `patch_tree.py`, `amb_k1p.yaml`.

## 2. What changed (forms/2025/k1p.yaml)

One entry per Schedule K-1 (Form 1065), collection parent `person`. Per K-1:
- Screens: `ptp` (item D, refusing, asked first and alone), `general` (item G).
- Box ticks in printed order (each opens its amount through a `_if_any` gate line): 1, 2, 3, 4a, 5, 6a (6b under
  it), 8, 9a (9b/9c under `has_b9bc`), 14 A, 15 O, 18 A, 19, 20 A/B, 20 Z; refusing ticks 4b, 7, 10, 11, 12, 13 (not
  AE), 14 B/C, 15 (not O), 16, 17, 20 (other codes), 21, 22/23, foreign partnership, sale of the interest.
- Box 19 children: `b19_other` (refusing), `dist_over` (refusing). 20 Z child `z_other` (199A dividends,
  cooperative; refusing).
- Box 1: `trader` (refusing); material participation `work` -> `hours500` (test 1) -> general only `most_hours`
  (test 3) -> `nearly_all` (test 2) -> `five_of_ten` (test 5) -> tick group tests 6 / 4 / 7 (refusing; 4 and 7 general
  only). `material` = any of tests 1, 2, 3, 5.
- Box 2: general only `decisions` -> `tenth`; `active` = both (Part IV).
- Prior-year unallowed losses (asked when box 1, 2 or 3 has an amount): `prior_any` -> tick group by activity ->
  amounts; `former_passive` (box 1 prior with material participation, refusing); `prior_not_active` (Part IV, refusing).
- Loss screens (any loss in 1, 2, 3, 8, 9a, 14 A): `basis_short`, `not_at_risk` (refusing). `se_loss_not_material`
  (computed refusal).
- Activities: `b{1,2,3}_net_income/_net_loss/_loss_sum/_overall_loss`; Part IV `p4_income/p4_loss/p4_prior/p6_loss`;
  Part V `p5_income/p5_loss/p5_prior`; Schedule E `col_h`, `col_k` (box 1 material + 4a), `col_i` (magnitude),
  `nonpassive_net`; `sche_row`, `passive_loss`, `prior_total`, `se_pos`.
- `k1p.screened` (true) carries all 28 refusals in asking order; every person sum filters `where screened`.

## 3. Decisions (alternative rejected)

- Interim wiring: expose totals, leave `scope.k1` refusing (rejected: removing `scope.k1` from `scope.schedule1` here,
  which would let K-1 returns complete with the K-1 amounts dropped).
- Refusals on one `screened` line read by every person sum's `where` (rejected: a refusal on each exposed line —
  28 x 25 entries — or relying on the integrator to read one particular line).
- Box presence asked as tick screens grouped by printed box ranges, refusing boxes on the same screens (rejected: one
  amount question per box with "0 if blank", 15+ steps for every K-1; and a separate rare-box catch-all, which the
  construction protocol 3.6 calls the catch-all again).
- Loss columns exposed as magnitudes (rejected: signed column values held negative).
- Prior-loss question only when box 1, 2 or 3 has an amount (`amb.2025.k1p_prior_with_activity`; rejected: asking
  every K-1, one more step on every portfolio-only K-1). This reading can only understate a deduction; flagged for the
  owner in the register.
- `general` asked as a yes/no on item G's first box (rejected: an enum; the build's selector would add nothing).
- D-K-level decisions: DECISIONS.md.

## 4. Gates replaced and residual refusals

Replaced: none in this tree (`scope.k1` stays; it is replaced at integration). New residual gates (all on
`k1p.screened`, placed in `tree.json` topic `k1_partnership`): `k1p.ptp`, `r_b4b`, `r_b7`, `r_b10`, `r_b11`, `r_b12`,
`r_b13`, `r_b14bc`, `r_b15`, `r_b16`, `r_b17`, `r_b20`, `r_b21`, `r_b2223`, `r_foreign`, `r_disposed`,
`b19_other_if_any`, `dist_over_if_any`, `z_other_if_z`, `trader_if_b1`, `t6_if_asked`, `t4_if_gp`, `t7_if_gp`,
`basis_short_if_loss`, `not_at_risk_if_loss`, `se_loss_not_material`, `former_passive`, `prior_not_active_if`.
These match scout R-K1..R-K21 for partnerships (R-K22..R-K26 are integration's or other lanes').

## 5. Next year

`changes/2026/`: no file written. Checked [V]: the 2026 draft f1065sk1 differs from 2025 only in "Current Year" ->
"Current-Year", "this" -> "the" (twice) and the creation date (word diff of the archived texts). i1065sk1 2026 is not
archived (awaited; scout 2.2). The only year-bearing text is in prompts ("In 2025", "2015 to 2024", "2024 Form 8582"),
which `year_diff.py --adopt` lists on its worklist. Rows for `changes/2026/README.md`: f1065sk1 — no change (draft
3/24/26); i1065sk1 — awaited. `year_changes.py --check`: see section 8. No new parameters.

## 6. Defects

None found in existing lines.

## 7. For other lanes and requests

- Return-integration lane: `/tmp/k1-wiring-k1p.md` (wiring table; the f8582-dependent per-activity lines
  `b{n}_p6c/_p7a/_p7c/_allowed`, `col_g`, `k1p.qbi` to add; EBL; f4952 count; SE flows). x1-sche's `rental.*` shapes
  are the template. Remove `display:` from each `person.k1p_*` line as it is wired.
- Coverage rows (10) are written but parked in `docs/provisional/lanes/x2-k1p_work/coverage_k1p.yaml`: they cannot
  walk until `scope.k1` stops refusing. Integrator: move to `interview/2025/coverage/k1p.yaml` and run
  `interview-coverage --rows`.
- Personas `15_k1_*`/`17_refused_ptp` (scout) not written: walks would end at `scope.k1`. For the interview lane (K6).
- x2-k1s / x2-k1e: naming as in the contract (`person.<coll>_total_<item>`, magnitudes for losses, `where screened`).

## 8. Verification (worktree x2-k1p)

Run in this worktree after the last edit (base caution applied: nx-b1 defaults; `npm run compile` reports the base's
`mutate-worker.ts` `sampledShare` error and emits anyway).

| Command | Result |
|---|---|
| `node engine/dist/main.js build` | build OK (earlier attempts: 31 unread-line errors, fixed with `display`; one display on a read line, fixed) |
| `render`, `render --ny` | OK (69 files; NY OK) |
| `/tmp/x2-k1p/run_cases.py` (my 26 cases, defaults filled, predictions compared) | 0 failures; all 14 value cases matched the hand prediction on the first evaluation; all 12 refusals at the predicted gate |
| `test-fixtures` | my 26 cases ok; 618 failures elsewhere, all base: 598 `s2.amt_owed: input is not declared` (fixtures stating the removed input) and 20 `no input supplied for sd.qof` (class M files take no defaults); none involves k1p |
| `test-fixtures --ny` | not run (no line New York reads changed; nothing reads k1p) |
| `python3 tools/citations.py --strict` | exit 0 (first run: 3 k1p quotes wrong page or wording; fixed) |
| `python3 tools/check_consumers.py` | 28 new k1p pairs ruled `same` in `reviews/2025/consumers.json`; remaining 44 findings are the base's (none k1p) |
| `python3 tools/transcription/check_questions.py`, `check_screens.py`, `check_false_no.py` | exit 0 (k1p screens and gates listed as due at the next release) |
| `python3 tools/coverage/tree.py --check` | exit 1 on 6 base gates not placed (household.hoh_missed, refund.two_itemized_if_two, s2.amt_pab_over, s3.business_credit_any, s3.business_fuel_any, sd.f2439_if_dividends); every k1p gate placed |
| `python3 tools/year_changes.py --check` | exit 0 |
| `tick-groups` | 0 problems; the 8 k1p groups are behind an answer the background return does not give (unreachable until wired), so not exercised |
| `siblings.py --check`, `check_bug_inventory.py` | exit 1, base findings only (the goal-1 and landing placeholders cited by other lanes, since numbered); no k1p entry |
| `interview-rules` | exit 1, 18 problems, all base: 9 Stage 5 walks fail on the removed input `s2.amt_owed`; dependent completion and baseline entries; New York reach on dependent questions; the stale pruning report. No problem names k1p. The k1p box questions show up only as existence gates the minimal returns never reach, which is expected while nothing reads k1p. Log: `/tmp/x2-k1p/chk_interview_rules.log`. |
| `interview-coverage --rows` | not run on k1p rows (parked; unreachable until `scope.k1` is wired) |
| mutate, check_all.sh | not run (brief) |

## 9. Review debt (round 2; no paid call made)

- `k1p` (new form): transcription (whole), render (whole), class M.
- `person` (new lines only): transcription and render `--lines auto`.
- Question review of the 72 new bank entries (`question_review.py`), screen review (kind `gate`) of the 28 gates,
  false-no review sample of `basis_short`, `not_at_risk`, `work`/`hours500`, `prior_any`, completeness of `k1p`.
- Price with `python3 tools/transcription/rerun_all.py --forms k1p,person --kinds transcription,render,classm
  --dry-run` on the integrated tree (not run here: no review data change wanted in this lane).

## 10. Walks before and after

Not recorded: every walk ends at `scope.k1` before and after this lane (no question added is reachable). Estimated
cost per partnership K-1 once wired [E]: investor LP with a box 2 loss — roster, ptp, general, 6 tick screens, 1 amount,
prior_any, basis, at-risk = 12 steps; operating LLC member-manager (box 1, 14 A, 20 Z) — 6 screens + 3 amounts +
trader + work + hours500 + prior_any + ptp + general + roster = 15 steps.

## 11. Left open, in rank order

1. Integration wiring (section 7); `scope.k1` leaving `scope.schedule1`; coverage rows moved and walked.
2. Personas and before/after walks (interview lane).
3. Mutation of `k1p` (integration; fixtures already take both sides of each test 1/2/3/5 branch, Part IV vs V both
   ways incl. the tenth operand, active with prior, and 12 refusal paths).
4. Engine differential: UsTaxes has a 1065 K-1 (scout 5) but the adapter passes none; not mapped (full tier).

## Lane xfix (2026-11-15): review findings fixed

claude-opus-5-5, judgment, tax year 2025, us. Uncommitted.

- BUG-0911 (box 9b loss): signed, not refused. `k1p.box9b`, `k1p.box9b_if_any`, `person.k1p_total_collectibles`
  are Dollars; `k1p.has_b9bc` and the box 9b question say "gain or loss". The wiring note now says `g28.line4` must take
  a signed sum (as for k1s box 8b). Fixture `x2k1p.collectibles_loss` (box 9a -$2,000, 9b -$1,500).
- BUG-0773 (sibling of BUG-0914): `k1p.not_at_risk` also names money borrowed from another partner or
  someone related to one (i1065sk1 p. 8, third bullet); help reworded. Refusal unchanged.
- Reviews: line-scoped transcription (3 lines: representation 2, interface gap 1) and render (9b: match). `person`
  line-scoped reviews remain the integration debt of section 9 (siblings --check names `person` for BUG-0911).
