# Lane nx-speed: interview-length and interview-coverage made fast again

Agent: `claude-opus-5-5`, class judgment, tax year 2025, jurisdiction `us`. No paid call, no model call from code,
nothing committed. Worked only in `.claude/worktrees/nx-speed`. Lines marked **RAN** were run and seen here;
**INFER** marks what was reasoned and not measured.

The machine was shared with about a dozen other lanes building and checking at once (load average 170 to 250 on
18 cores for the whole session), so every wall time below is inflated and noisy; CPU times are given beside them
and are the better comparison. None of the times is a quiet-machine measurement.

## What made the two steps slow (RAN, CPU profiles)

- **interview-length.** One minimal return (`every gate closed`) profiled without any change: 76% of CPU in the
  expected order's probes (`interviewStatus` of the state with one open question answered closed, for every open
  question at every state), and 59% of all CPU in the reach pass (`inputsAhead`) inside those probes. The probes
  repeat across returns: the walks of returns that have answered alike so far meet the same states, and the 62
  minimal returns share nearly all of theirs.
- **interview-coverage.** One row file (`care.yaml`, 9 rows, 572 answers) profiled: 73% in `applyAnswer`, which
  computed `interviewView` twice per answer (the view before the answer is the view after the previous one), and
  528 of the 572 answers were background answers that every row repeats.

## Changes

| File | Change |
|---|---|
| `engine/src/pool.ts` | `walkWorkers(name)`: the env variable, else `defaultWorkers()` (8 on this 18-core machine with `CHECK_ALL_MAX_RUNS` 2), as for mutate and interview-rules. `TaskWorkers`, a pool of worker threads serving tasks one at a time with results in input order (as interview-rules' pool, made generic), and `serveTasks`, its worker side. |
| `engine/src/interview-length.ts` | `runAll(ctx, workers, only?)` spreads the returns over `INTERVIEW_WORKERS` threads by index; each worker builds the same case list (checked by `casesDigest`); results are reassembled in list order, problems in the serial order. `measureCase`. A per-thread store of states met (`statesOf`, keyed by `stateKey`, a hash of the inputs in key order) shared by the three walks (through `walk`'s new `status` argument) and the probes. `expectedOrder` runs the reach pass only for probes whose bound can reach the best score (exact: see the comment). Self-test: the social-security returns on one thread and on two workers, run and report equal. |
| `engine/src/interview-length-worker.ts` | New: the worker. |
| `engine/src/interview-coverage.ts` | `walksOn(ctx, files, workers)` walks the rows on worker threads; `checkFiles` takes the walks through a new `walkOf` argument and judges in file order. `walkRow` keeps each applied answer by the chain of answers before it (`appliedOf`, `chain`) and passes the view it holds to `applyAnswer` as `before`. Self-test: the planted clean rows and the smallest row file walked on two workers, judged and reported the same. |
| `engine/src/interview-coverage-worker.ts` | New: the worker. |
| `engine/src/interview.ts` | `applyAnswer` takes an optional `before` view. `neededInputs` split into `neededParts` (the evaluation's reads at once, the reach pass on call); `statusParts` exported. Behaviour of every existing caller unchanged. |
| `engine/src/interview-rules.ts` | `walk` takes an optional `status` function (default `interviewStatus`). |
| `tools/check_all_steps.sh`, `tools/README.md` | The worker count, its env override and the equality guarantee documented; the stale "about 8 minutes on one core" removed. |

Every saving is exact: a stored state's status and reachable inputs, and an applied answer, are functions of the
built data, the bank and the state (or the answers given), so a stored value is the value a fresh computation gives.
The probe bound skips only probes that cannot reach or tie the best score, and the best set is taken in the order
of the open questions, as before.

## Measured

Before (the caller's last landing run, quiet machine): `interview_length` 4,490 s, `interview_coverage` 1,324 s,
wave 2 4,490 s.

After (this lane; RAN unless marked; the load average is given per row, as it changed through the session):

| Run | Load | Wall | CPU (user) | Peak RSS | Result |
|---|---|---|---|---|---|
| `interview-length --write`, `INTERVIEW_WORKERS=1` | ~200 | 5,863 s | 2,995 s | 0.7 GB | 311 measured (215 complete), 0 problems, exit 0 |
| `interview-length --write`, `INTERVIEW_WORKERS=4` | ~230 | 2,686 s | 3,845 s | 2.1 GB | the same |
| `interview-length --write`, `INTERVIEW_WORKERS=4` | 16 to 80 | 955 s | 3,609 s | | the same |
| `interview-length --write`, `INTERVIEW_WORKERS=8` | 20 to 50 (the check-all build started near its end) | 658 s | 4,655 s | | the same |
| `interview-coverage`, `INTERVIEW_WORKERS=1` | ~230 | 652 s | 210 s | 0.4 GB | 498 rows, 0 problems, exit 0 |
| `interview-coverage`, `INTERVIEW_WORKERS=4` | ~230 | 268 s | 318 s | 1.5 GB | the same |
| `interview-coverage`, `INTERVIEW_WORKERS=4` | ~80 | 125 s | 348 s | | the same |
| `interview-length --self-test` | ~230 | 926 s | 313 s | | passed, "21 social-security returns the same on two workers" |
| `interview-coverage --self-test` | ~230 | 57 s | 25 s | | passed, "13 rows the same on two workers" |

The worker default. A quarter of the cores (4 here) was tried first: interview-length then took 955 s even at low
load and would still have set wave 2. Its remaining work is mostly the eleven complete full-profile returns that share
few states with any other, and each worker also pays once for the first return of each family it meets (the CPU grows
from 2,995 s on one thread to 3,609 s on four and 4,655 s on eight). Eight workers (`defaultWorkers()`, the size the
repository already gives mutate and interview-rules) brought it to 658 s, below `engine_differential`'s 702 s of the
landing run. A scheduler that kept each family of returns on one worker would save most of that duplicated CPU; not
done here.

For scale under the same load: the two other lanes' full check-all runs that held both slots during this session
ran the unchanged `interview-length` step for over 4.5 hours of wall time and 6,170 s of CPU each, still unfinished
when last looked at (RAN, `ps`). On a sample of eight returns over four groups, CPU fell from 249 s (unchanged code)
to 132 s, with byte-identical measures (RAN): the first minimal return 92.5 s to 85.0 s (pruning only), its sibling
91.5 s to 1.5 s (states met), a sales fixture 13.6 s to 0.4 s.

**INFER, not measured:** inside wave 2 the two steps share the machine with mutate, compare and the rest, so their
wall times there will be longer than the standalone ones above; the check-all run below is the measurement.

## Equality of sharded and unsharded runs (RAN)

- interview-length: the runs started from the committed `reports/2025/interview_length.md`; the reports written
  with 1, 4 (twice) and 8 workers are byte-identical (`cmp`), stdout is identical but for the time and worker count, stderr is identical, both
  exit 0. Each differs from the committed report only by one blank line above the hand-written findings: see the
  defect below.
- interview-coverage: both runs in check mode passed, which requires the produced report to equal the committed
  `reports/2025/interview_coverage.md` byte for byte; stdout identical but for the time and worker count; both exit 0.
- The self-tests assert the same on small sets (above).

## Found, not fixed: `interview-length --write` adds a blank line each run

`interviewLength` keeps the hand-written part as `old.slice(indexOf(MARKER) + MARKER.length)`, which begins with the
newline that ended the marker line, and `renderReport` then joins the marker and that text with another `\n`. So
each `--write` adds one blank line before `## Findings` (the committed report already has nine blank lines there). Every full run
therefore leaves `reports/<year>/interview_length.md` modified. The same pattern is in `whatIf`
(`umbrella_savings.md`). Not changed here: it changes a tracked report and is outside this lane. One-line fix:
strip the leading newline from `kept` (or push `MARKER + kept`).

## Full tier (RAN)

`tools/check_all.sh --tier full` in this worktree (load about 15 to 30 at its start) failed at the end of wave 1,
so it never reached wave 2. The failing steps come from the tree, not from this lane:

- `bookkeeping_self_tests` (green_self_test): "tools/year_shared_refs.py enumerates files with '.rglob(' and is not
  in WALKERS". The worktree came with an uncommitted change to `tools/tier_paths.py` that removes that entry.
- `bookkeeping_self_tests` (siblings_self_test) and `siblings_check`: the TY2026 pending bug entries lacking `Fix lines` or
  `Siblings checked`, or naming no line of canonical/2025.
- `check_bug_inventory`: the landing round's pending bug placeholders cited in `docs/provisional/lanes/landing_work/` with no `bug_pending/` file.

To measure the later waves, the same steps were run once more under a check-all slot (`tools/check_slot.py --tier
full -- <copy>`) from a copy of `tools/check_all_steps.sh` in /tmp, changed only so that a failed wave does not stop
the run. Its stage table (load 12 to 115 during the run):

| stage | wall s | share | slowest step, then the next |
|---|---|---|---|
| compile | 1 | 0% | compile 1 |
| build | 517 | 31% | build 517 |
| wave1 | 202 | 12% | self_tests 202, then check_extraction 131 |
| wave2 | 938 | 56% | interview_length 938, then engine_differential 937 |
| wave3 | 11 | 1% | review_packets 11, then evidence 2 |
| **run** | **1,669** | | |

In wave 2: interview_length 938 s (8 workers; 4,490 s before), engine_differential 937, mutate 866, compare 725,
interview_rules 609, ny_compare 398, properties 370, test_serve 316, interview_coverage 218 (1,324 s before).
Self-tests in wave 1: interview_length_self_test 180 s, interview_coverage_self_test 18 s. Both steps passed with 0
problems. Wave 2 also failed `mutate`, on two stale equivalence arguments
(`operand.sa.sa.gift_carryover_if_no_gifts.no.then1`, `operand.eic.eic.from_step1_income.no.then1`: "the argument no
longer holds (a line or premise it pins changed)"). This lane changes no form data and not the evaluator, so this
too comes from the tree (**INFER**: not rerun on the tree without this lane's changes).

The run took 27.8 minutes, against the 15-minute goal. Wave 2 is now 938 s against 4,490 s, and interview_length no
longer stands alone at its top: it finished within a second of engine_differential, with mutate 72 s behind. A shorter
wave 2 needs those three shortened together. The build stage (517 s here, 278 s in the quiet landing run) is
the second-largest stage and was not looked at.

The generated reports and rendered pages the verification runs rewrote were restored (`git checkout -- reports/
rendered/`); the run's `interview_length.md` differed from the committed one only by the blank line described above.
