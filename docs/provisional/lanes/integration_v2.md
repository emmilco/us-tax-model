# Integration notes: the second draft (`draft/v2`), ranges ra, rb and rc merged

Integrator: `claude-opus-5-5`, class judgment, tax year 2025, jurisdiction `us`. No paid call, no model call from
code, nothing pushed, nothing outside `.claude/worktrees/provisional-v2` written, no lane worktree edited. Started
from `eaeb62d9` (`lane/rc` already merged). Lines marked **RAN** were run and seen here; **INFER**Nothing is red** on what was run. What the green does not cover: per-person and per-entry screens
(`work_kind`, `dependent_facts`, `tip_kinds`, the business, vehicle and property screens) were not seen in a browser;
21 of the 43 groups are not met by the background return and are checked only by the build's rules and the
personas that reach them; review debt of all three ranges stands (headings, labels, gate lines, help no review has
read).** were not
checked.

## State

| Merged | Commit | Build | Fixtures |
|---|---|---|---|
| `lane/rc` (`ad5608bb`) | `eaeb62d9` (before this integrator) | | |
| `lane/ra` (`4b206f46`) | `311e18ae` | OK (**RAN**) | 1,854 of 1,854 (**RAN**) |
| `lane/rb` (`2cc88f9a`) | `de9f1330` | OK (**RAN**) | 1,854 of 1,854 (**RAN**) |
| coverage rows, walks, order report, generated files | `fa322095` | | |
| these notes | the commit after | | |

All three branches share the merge base `f009095a` (`lane/tickrule`). The bank declares 43 groups: rc's 13 and
`rare_credits`, ra's 13, rb's 16 (`grep -c '^  - id:'`).

## Conflicts of substance, and how each was resolved

1. **The bank head (`groups`), at the ra merge.** `tools/draft/merge_lane.sh lane/ra` stopped on a text conflict in
   the head; both sides were kept (ra's thirteen, then rc's thirteen, then `rare_credits`). The bank's entries
   merged structurally (`merge3.py`) with no entry changed by both.
2. **`coverage/home.yaml` and `coverage/other.yaml`, at the ra merge** (15 hunks). In every hunk ra's side was
   empty (it had removed `scope.business_before: false`, and in `home.refund_exception` the two 2024 refund
   figures) and rc's side added `scope.attorney_fees: false` beside the same answer. The hunks were resolved to rc's
   side (the union of answers) and the walk then named which are not asked: all of them (below, "Coverage rows").
   No `expect` changed.
3. **`interview/2025/full.yaml`, at the rb merge.** Both sides added targets after `s2.line17c`; all five kept
   (`s1.line10`, `s1a.line7`, `s1a.line15`, `sa.line17`, `s2.other`), each with its own comment.
4. **`scope.excess_deferral`, at the rb merge** (`merge3.py`: "changed by both"). ra made it a box of `w2_jobs`
   (145/5) and shortened its help ("… A Yes ends the interview here."); rb left it at 187/1 and reworded the same
   help differently ("The limit is per person across all that person's jobs …"). **ra's entry was taken whole**
   (placement as instructed; the help goes with it). rb's rewording of this help is not on the branch.
5. **`engine/src/serve-check.ts`**: the three ranges' one-condition fix merged without conflict (identical edits).
   **`engine/src/generate.ts`**: only rb changed it; taken.
6. **Moved entries.** Compared by script over the three branches and the base: no entry was given an `order`,
   `seq` or `group` by two ranges. On the merged bank (**RAN**, `/tmp` script over `questions.yaml`):
   `person.work_ssn` 150/3, `s8812.combat_pay` 158/2, `scope.excess_deferral` 145/5 (`w2_jobs`),
   `ny_it201.ask.dependent_care` 155/5 (New York bank), `f5695.carry` 290/8, `f5695.line12` 290/9,
   `person.sav_claimed` 241/5, `person.tin` 241/15, `scope.business_before` 258/1 and `s179.prior_form` 258/5,
   `scope.foreign_shares` 285/6, `scope.pfic` 285/12, `scope.cfc` 285/13, `s2.credit_recapture`, `s2.amt_owed`,
   `s2.other_tax` 291/1 to 3. No duplicate `seq` and no duplicate input in either bank.
7. **The combined model changes** (rb's two derived lines `person.sav_excess`, `ira.reservist_repaid`; ra's two W-2
   gates; rc's `s179.prior_form` gate). No fixture input had to be stated for the combination: the build passed and
   the fixtures were 1,854 of 1,854 on each merge commit with no fixture edited by this integrator, and
   `tools/draft/stale_ids.py` found 0 stale ids (890 inputs read) after the rb merge. **No conflict between two
   ranges' model changes was found**: no fixture's expected value or refusal changed (`git diff f009095a HEAD --
   fixtures` holds no `expected` or `refused` line), and no row's `expect` changed (each of the 448 rows compared
   by script with the same row on `f009095a`, `lane/ra`, `lane/rb` or `lane/rc`: 0 differ).

## Coverage rows (answers only; no `expect` changed)

`node engine/dist/main.js interview-coverage` on the build of `de9f1330`: **34 problems** (448 rows, 750 s), 33
of them answers never asked before the row's end and the 34th the stale report. `tools/draft/fix_rows.py` removed
the 33 answers:

| Rows | Removed | Why |
|---|---|---|
| eleven of `other.yaml`, four of `home.yaml` | `scope.attorney_fees: false` (all 15), `scope.business_before: false` (13; the other two had lost it on ra's side already) | ra's target `s1.line10` and the refusal ends of `refund.*`: the refusal comes on the row's own answer, before the last scope item. This is rc's added answer meeting ra's removal |
| `home.refund_exception` | `refund.line5d_2024`, `refund.line5e_2024` | as ra removed them: refused at `refund.exc_tax` first |
| `credits.mcc` | `sa.line5b`, `sa.property_tax_other_any` | refused at `s3.mcc_if_interest` before them (rb's Schedule A placement) |
| `credits.gap.foreign_tax_carryover_form` | `f5695.carry` | rb moved it to 290/8, after the row's refusal at `ftc.carryover_if_asked` |

Then each of the three files alone with `--rows`: 0 problems each (**RAN**).

## Personas

`node engine/dist/main.js draft-walk --out docs/provisional/walks/after` (**RAN**, build of `de9f1330`, rows
fixed): 14 personas, **0 problems** (no stale answer, none opened and unanswered), each at the end it states. No
persona was edited. `walks/before/` untouched (`git diff` empty).

The baseline has no tick-box screens, so its steps equal its questions; the first draft had one group
(`rare_credits`), which no persona meets.

| Persona | Steps (base / v1 / now) | Questions (base / v1 / now) | Prompt words (base / v1 / now) | Help words (base / v1 / now) | End (base / v1 / now) |
|---|---|---|---|---|---|
| `01_single_w2` | 86 / 125 / 56 | 86 / 125 / 124 | 6777 / 2567 / 1724 | 2376 / 3548 / 3065 | complete |
| `02_couple_children_mortgage` | 133 / 172 / 97 | 133 / 172 / 172 | 10168 / 4013 / 2882 | 3286 / 4798 / 4269 | complete |
| `03_single_parent_child_care` | 121 / 156 / 81 | 121 / 156 / 155 | 10100 / 3786 / 2845 | 2969 / 4402 / 3907 | complete |
| `04_retired_couple` | 122 / 159 / 82 | 122 / 159 / 156 | 9030 / 3815 / 2593 | 2970 / 4302 / 3814 | complete |
| `05_self_employed` | 133 / 168 / 94 | 133 / 168 / 165 | 9905 / 4085 / 3144 | 2360 / 4488 / 4012 | complete |
| `06_investor_loss_carryover` | 114 / 151 / 82 | 114 / 151 / 150 | 9298 / 3271 / 2428 | 2787 / 4242 / 3759 | complete |
| `07_college_student` | 110 / 145 / 76 | 110 / 145 / 144 | 7747 / 3028 / 2153 | 2681 / 4067 / 3622 | complete |
| `08_hsa_marketplace` | 150 / 201 / 125 | 150 / 201 / 200 | 10384 / 4162 / 3211 | 4105 / 5557 / 5112 | complete |
| `09_tips_overtime` | 95 / 137 / 66 | 95 / 137 / 136 | 7363 / 2840 / 1959 | 2466 / 3953 / 3470 | complete |
| `10_homeowner_solar_heat_pump` | 117 / 153 / 70 | 117 / 153 / 152 | 8425 / 2963 / 2082 | 6281 / 3967 / 3484 | complete |
| `11_refused_rental` | 4 / 17 / 12 | 4 / 17 / 19 | 490 / 285 / 249 | 231 / 538 / 504 | refused at `scope.schedule1` |
| `12_refused_nonresident` | 5 / 10 / 9 | 5 / 10 / 13 | 678 / 164 / 166 | 281 / 410 / 378 | refused at `scope.other_income` |
| `13_ira_saver` | — / 138 / 66 | — / 138 / 136 | — / 2908 / 1998 | — / 3951 / 3433 | complete |
| `13_self_employed_actual_vehicle_computer` | — / 216 / 127 | — / 216 / 213 | — / 5334 / 4123 | — / 5061 / 4585 | complete |

Persona 11 and 12 are asked more questions now than in either earlier draft (19 and 13) though on fewer steps than
the first draft: their refusing Yes is a box of `own_income` (rental) or opens a child of `about_you`
(`scope.nonresident` beneath `scope.noncitizen`), and all the boxes of a screen are answered before the refusal.

## Checks on the final tree

All on this clone, 2026-11-13, one at a time.

| What was run | On | Result |
|---|---|---|
| `npm run build --silent`, `node engine/dist/main.js test-fixtures`, `python3 tools/draft/stale_ids.py` | the trees of `311e18ae` and `de9f1330` | build OK; 1,854 of 1,854; 0 stale ids, each time |
| `node engine/dist/main.js tick-groups` | build of `de9f1330`, and again after the row fixes | passed: `full` and `ny`, 43 groups each, 22 shown whole on the background return, 0 problems |
| `node engine/dist/main.js interview-rules` | build of `de9f1330` | 0 problems; 177 walks, 415 in a random order; baseline empty, not touched |
| `node engine/dist/main.js interview-coverage` | build of `de9f1330` | 34 problems (448 rows); fixed as above; then `--rows` on `credits.yaml`, `home.yaml`, `other.yaml`: 0 each |
| `node engine/dist/main.js draft-walk --out docs/provisional/walks/after` | the same build, rows fixed | 14 personas, 0 problems |
| `node engine/dist/main.js interview-order --write docs/provisional/lanes/order_v2.md` | the same | written; 851 of 851 questions state a `seq` |
| `node engine/dist/main.js render`, `spouse-wording --report`, `properties` | the same | rendered 68 files (only `index.md` changed); wording report unchanged; properties 9 over 400 returns, 0 failing |
| **`tools/draft_check.sh`, whole (not `--quick`), once** | commit `fa322095` (its last line: "draft-check: green (fa322095, tree 442a4f605408)") | **green, all sixteen steps**: build OK (354 s); fixtures 1,854 of 1,854; interview-rules 0 problems (177 walks, 415 random orders); interview-coverage 0 problems (1,040 s, after its own `--write`, which regenerated `reports/2025/interview_coverage.md`, committed with these notes); tick-groups passed; person wording current; spouse-wording self-test; check self-test 95 cases; test-integration 1,030 CLI invocations; properties; test-serve 513 checks (29 fixture paths replayed, 665 expected values matched); draft-walk, interview-order (692 checks) and tick-groups (35 planted cases) self-tests; twins 0 problems; render check |

The quick check's steps are a subset of the whole run, so `--quick` was not run separately.

Not run: `ui/test_browser.mjs`; the New York fixtures by hand; any review, mutation run, the Lean comparison,
`tools/check_all.sh`. No tick-box screen was looked at in a browser.

## What is red

**Nothing is red** on what was run. What the green does not cover: per-person and per-entry screens
(`work_kind`, `dependent_facts`, `tip_kinds`, the business, vehicle and property screens) were not seen in a browser;
21 of the 43 groups are not met by the background return and are checked only by the build's rules and the
personas that reach them; review debt of all three ranges stands (headings, labels, gate lines, help no review has
read).

## Seen while merging (design notes; nothing changed)

- **`scope.excess_deferral`'s help** exists in two rewordings (ra's, kept; rb's, dropped). The owner may prefer
  rb's first sentence.
- `interview-order` (`order_v2.md`): 851 of 851 questions state a `seq`; 139 gated questions are not placed directly
  after their parent; late order re-entries fell from 3.1 to 0.3 per generated return and from 5.1 to 0 per minimal
  return against the first draft's `order_merged.md`. The biggest late waits are `person.blind` on `sa.dependent` (74 walks),
  `household.ever_married` on `f1040.status` (64) and **`person.eic_ssn` on `scope.attorney_fees` (57)**: rc's
  last-scope-question effect (rc notes, section 1). One delayed child late in a generated return
  (`div.box12` waiting on `person.eic_ssn`) and one in a minimal return (`person.x_ira_prior_excess` on
  `person.x_archer_excess`).
- `tick-groups`: 43 groups, 22 shown whole on the background return; the other 21 lie behind an answer the
  background return does not give and are checked only through the personas (`draft-walk`) and the build's rules.
- T-290 (order-dependent leaks): `interview-rules` was 0 problems on this tree, baseline empty and untouched. As in
  the earlier integration, that does not show the leaks are gone; rb's `ssb.ira_covered` derivation (which surfaced
  two on generated return 10) is not on the branch.
