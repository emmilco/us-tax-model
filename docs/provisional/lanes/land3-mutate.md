# Lane land3-mutate: mutation, refusal reach and the Form 8959 remedy on the landing tree

Agent: claude-opus-5-5, judgment class, year 2025, jurisdiction us (New York checked too). Worktree
`.claude/worktrees/land3-mutate`, detached at `refs/scratch/land3-base` (`57b00992`, the landing tree with the mutation
patch). No commit, no paid review call, no model call from code. Run outputs: `/tmp/land3m/`.

## 1. Mutation

With the patch in the tree, both runs are green as they stand; no argument, case or table needed changing.

- `MUTATE_WORKERS=4 node engine/dist/main.js mutate`: 7480 mutants, killed by the checker 2705, by fixtures 4414,
  surviving 361 (353 equivalent on every input, 8 on answered inputs only); 0 stale equivalence arguments; every
  self-test 0 problems; exit 0. No row in "not yet explained". The tree's changes after the patch's base
  (`sa.mortgage_insurance`, the f8959 relabelling, the four extra mutants: 7480 against the lanes' 7476) left no
  unexplained survivor.
- `MUTATE_WORKERS=2 node engine/dist/main.js mutate --ny`: 878 mutants, 249 by the checker, 577 by fixtures, 52
  surviving, all 52 equivalent on every input; 0 stale; exit 0.
- The first federal run failed with `mutation baseline mismatch: stage4.refuse.8959 f8959.line18`. That was my task 3
  edit (the fixtures quote the remedy), not a mutation finding; fixed with the fixtures (task 3).
- Both reports regenerated (`reports/2025/mutation.md`, `reports/ny/2025/mutation.md`); the snapshot carried the
  pre-patch New York report.

No survivor revealed a tax-result defect; no pending bug recorded.

## 2. refusal_reach: `t264.f4952.unsupported_with_interest`

**The fixture was stale; no refusal was lost.** The redraft turned the input `person[taxpayer].age65` into
`person[taxpayer].birth_year`, and the fixture's conversion carried the old `null` (unanswered) across. Evaluated on the
full interview's targets, every target that reaches Form 4952 (`f1040.line24`, `33`, `34`, `37`) is then unknown on the
birth year before it meets the refusal; the refusal itself is intact on the Form 4952 lines (`f4952.required`,
`required_test`, `line3`, `line5`, `exception`), on `sd.filing4952` and on `sa.line9`. With the birth year answered
(1980, under 65) the full interview refuses this return at `f1040.line24`, `33`, `34`, `37` with gate
`f4952.unsupported`. A real interview always asks the birth year, so this is not a scope hole.

Change: `fixtures/2025/f4952.json`, this case only, `"person[taxpayer].birth_year": null` to `1980`. Its expected value
(the `f4952.required` refusal) is unchanged. The other case with `birth_year: null`
(`stage16.cleanup.refuse.f4952_unsupported`, a listed exception for line 1 unanswered) is left as it is.

## 3. Form 8959 remedy text

`forms/2025/f8959.yaml`: the seven `refuses` entries on `f8959.unsupported` (lines 1, 2, 3, 8, 14, 23, 19) said "The wage
and Schedule SE path does not prepare RRTA, Form 4137 or Form 8919." `f8959.unsupported` is now true only when
`f8959.territory_w2` is Yes. New remedy, from i8959 p. 1, "Forms W-2 of U.S. territories" ("However, for Form
499R-2/W-2PR, Medicare wages and tips are reported in box 22 and Medicare tax withheld is reported in box 23"):

> Form 8959 also counts the Medicare wages and Medicare tax withheld on a wage statement from an employer in Puerto
> Rico or another U.S. territory (such as Form 499R-2/W-2PR, boxes 22 and 23); this tool does not prepare Form 8959
> with one.

`form` ("Form 8959 additional source forms") and `cite` unchanged. Ripple, each a quote of the same text:

- `fixtures/2025/f8959.json`: the 8 expected refusals quoting the remedy.
- `tools/coverage/tree.json`: the gate's question in the decision tree still listed church income, Form 4137, Form 8919
  and uncollected Medicare tax; now the question `f8959.territory_w2` asks. `docs/COVERAGE.md` and the README table
  regenerated (`tools/coverage/tree.py`).
- `reports/2025/interview_coverage.md` regenerated (`interview-coverage --write`): row `other.territory_wage_statement`.
- `rendered/2025/f8959.md` re-rendered.

Instruction cites. The remedy edit changed the canonical data of lines 8, 14, 19 and 23, so their baselined
`instruction_cites` findings came due (a baseline entry holds only while its line is unchanged): each line's citation
named no page of i8959 that holds its section. Fixed rather than ruled, adding the section to each line's `cite`
locator: line 8 `i8959 p. 3, Line 8, "Enter your self-employment income from Schedule SE (Form 1040), Part I, line 6"`
(the quote `person.yaml` already uses); line 14 `i8959 p. 4, Line 14, "Enter the total of your RRTA compensation and
tips"`; line 19 `i8959 p. 4, Line 19, "Enter the amount of Medicare tax withheld, if any, reported on Form W-2, box 6"`
(replacing `i8959 pp. 1–3`); line 23 `i8959 p. 4, Line 23, "Enter the amount of Additional Medicare Tax withheld, if
any, reported on Form W-2, box 14"`. The four baseline entries removed from `reviews/2025/instruction_cites.json`
(the check then reported them stale); `reports/2025/instruction_cites.md` rewritten. `citations.py --strict` verifies
the new quotes.

Reviews due (paid, not run): `check_logs` lists f8959 transcription lines 1, 2, 3, 8, 14, 23, 19 (the lines edited
here) and render lines 1, 2, 3, 8, 14, 23, 4, 12, 16, 19, 20, 22, 24 (several already stale from the relabelling).

Not changed, for the coordinator: the form's `note` still ends "Railroad and self-employment paths are explicitly
refused." Railroad (RRTA) is refused at `person.rrta`, but self-employment income from Schedule SE is figured (line 8),
so the sentence is half wrong. It is form text a render review reads.

## Other changes in the diff (build outputs the snapshot had not regenerated)

- `rendered/2025/asset.md`, `rendered/2025/index.md`: the patch's `asset.bonus` (a choice on `placed_this_year`, with
  the new helper `asset.bonus_elected`) had not been rendered.
- `reports/2025/citations.md`: rewritten by `citations.py --strict`.

## Verification (in this worktree, after all edits)

| Command | Outcome |
| --- | --- |
| `npm run compile --silent && node engine/dist/main.js build && node engine/dist/main.js render && node engine/dist/main.js render --ny` | build OK; 68 + 12 files |
| `node engine/dist/main.js test-fixtures` | 1987/1987, exit 0 |
| `node engine/dist/main.js test-fixtures --ny` | 357/357, exit 0 |
| `MUTATE_WORKERS=4 node engine/dist/main.js mutate` | exit 0 (above) |
| `MUTATE_WORKERS=2 node engine/dist/main.js mutate --ny` | exit 0 (above) |
| `node tools/check_refusal_reach.mjs` | 463 refusal fixtures, 2 exceptions, exit 0 |
| `python3 tools/citations.py --strict` (and `--jurisdiction ny`) | exit 0 both |
| `python3 tools/coverage/tree.py --check` | 234 gates, current |
| `python3 tools/check_instruction_cites.py` | 0 new, 0 stale, exit 0 |
| `node engine/dist/main.js interview-coverage` | exit 0 (report current) |
| `tools/check_all.sh --tier fast` (run before the instruction-cite fix) | exit 1 after wave 1: `bookkeeping_self_tests classm_skipped check_logs ny_check_logs instruction_cites consumers` |

The mutation, fixture and refusal-reach rows were rerun after the last edit to `forms/2025/f8959.yaml`, with the same
results (federal mutate 7480 / 0 stale / exit 0; New York 878 / 0 stale / exit 0).

Beyond the expected failures: `instruction_cites` (fixed since, above) and `bookkeeping_self_tests`, whose
`green_self_test` fails in the tier-paths self-test (`python3 tools/tier_paths.py --self-test`):
`engine/src/draft-walk.ts`, `tick-groups-check.ts`, `tick-groups.ts` refer to `docs/*` and are not in its READERS.
Not caused by this lane (no `engine/src` change here); not fixed. Wave 2 did not run inside check-all (it stops after a
failing wave); its steps that this lane's edits touch were run one by one above.

Incident: one rerun command backgrounded its `cd` with its first job (`cd … && (mutate) & …`), so `mutate --ny`,
both `test-fixtures`, `check_refusal_reach`, `tree.py --check` and `interview-coverage` ran once in the main checkout.
The only file that wrote there was `reports/ny/2025/mutation.md`, rewritten byte-identical (no git diff in the main
checkout afterwards). All of them were rerun inside this worktree; the table shows those runs.
