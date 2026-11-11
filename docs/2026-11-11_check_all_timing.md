# Where the full tier of check-all spends its time

Process lane, 2026-11-11. One full-tier run measured with the new timing summary, on the lane's own tree
(snapshot tree `904cc798a1afd37c4ab92589472a7462aea6dae2`, background run started 03:03:48, green at 03:20:51),
set beside the step times that thirteen earlier full-tier runs of the last day left in their worktrees' git directories.
Nothing in section 5 is implemented: each option changes the full tier's content or parallelism and is the
owner's decision.

Files beside this one: `times_run1.txt` (the summary as the run printed it), `times_run1.raw` (the recorded
lines), `run1.log` (the run's log), `samples.txt` (process samples every 15 s during the run),
`other_runs.txt` (the earlier runs' step times).

## 1. What was measured, and how far it can be trusted

- **Measured, one run:** the wall time of every step, stage and self-test (whole seconds), from the run itself.
- **Measured, thirteen earlier runs:** each step's wall time, from `.git/worktrees/<agent>/check-all-times`
  (written by the old code: steps only, no stages; one file per worktree, so each is that worktree's last run. An
  older file in the main checkout, from before the New York steps, is left out). Stage times for them are reconstructed as the slowest step of
  each stage, which is what a stage's wall time is; the reconstruction matches the measured stages of the new run.
- **Sampled, one run:** every 15 s, the CPU time and %CPU of the run's process tree and the machine's load
  average. Sampling misses processes that live for a fraction of a second, so it understates the steps that
  spawn many short processes (`compare`, `test_fixtures`); for `compare` the per-case cost was measured directly.
- **Measured directly, on a quiet machine after the run:** 100 serial runs of the Lean evaluator (10.7 s, 9.8 s
  of it user CPU); one `node engine/dist/main.js build` (76.6 s wall, 78.0 s user CPU) and its CPU profile.
- **Not measured:** the split of `engine_differential` among its four engines; the cost of `mutate` and
  `engine_differential` on an otherwise idle machine; any option's saving (all savings below are estimates from
  the measurements, and are stated as bounds where the data gives a bound).
- **The machine during the run:** 18 cores (6 performance, 12 efficiency). Another lane's full-tier run held the
  second slot until 03:18, and for the first six minutes an unrelated Xcode simulator test run was also active
  (1-minute load average 108 at its peak, 6 at the end). Wave 1 of this run is therefore slower than usual
  (324 s against a median of 174 s in the earlier runs); the other stages are close to the median.

## 2. The measured table

Stages run one after another. The steps of a stage run side by side, so a stage lasts as long as its slowest
step and the step times within a stage do not add up to wall time.

| stage | wall s | share | steps | sum of step times s | slowest step, then the next |
|---|---:|---:|---:|---:|---|
| compile | 0 | 0% | 1 | 0 | compile 0 |
| build | 73 | 7% | 3 | 75 | build 73, then check_self_test 1 |
| wave1 | 324 | 32% | 44 | 1262 | self_tests 324, then check_extraction 248 |
| wave2 | 537 | 53% | 18 | 2912 | engine_differential 537, then compare 537 |
| wave3 | 73 | 7% | 3 | 83 | human_review 73, then review_packets 7 |
| **run** | **1007** | | 69 | | 16.8 minutes; 1023 s from the background run's start to its record |

Steps of 60 s or more (all 69 are in `times_run1.txt`):

| s | stage | step | note |
|---:|---|---|---|
| 537 | wave2 | compare | ties with engine_differential |
| 537 | wave2 | engine_differential | sets wave 2; shortening it alone saves 0 s (compare is as long) |
| 347 | wave2 | mutate | |
| 347 | wave2 | ny_compare | |
| 324 | wave1 | self_tests | sets wave 1; alone it can save at most 76 s |
| 248 | wave1 | check_extraction | |
| 232 | wave1 | check_logs | |
| 162 | wave2 | interview_rules | |
| 157 | wave2 | properties | |
| 138 | wave2 | test_fixtures | |
| 126 | wave2 | test_serve | |
| 116 | wave2 | test_integration | |
| 105 | wave2 | coverage | |
| 102 | wave2 | classm_job_seeds | |
| 100 | wave2 | ny_mutate | |
| 94 | wave1 | citations | |
| 79 | wave2 | ny_properties | |
| 73 | build | build | sets its stage; the only long step in it |
| 73 | wave3 | human_review | sets wave 3; alone it can save at most 66 s |
| 66 | wave1 | ny_check_extraction | |

Self-tests inside `self_tests` (a pool of 45): review_tools 324, ny_review_tools 187, year_diff_self_test 124,
interview_length_self_test 104, citations_self_test 75; every other one 25 s or less.

The fourteen runs (stage = its slowest step; the last row is the measured run):

| finished | build | wave1 | wave2 | wave3 | total s | minutes |
|---|---:|---:|---:|---:|---:|---:|
| 11-10 16:16 | 67 | 117 | 450 | 71 | 706 | 11.8 |
| 11-10 19:00 | 75 | 147 | 1214 | 99 | 1535 | 25.6 |
| 11-10 19:33 | 210 | 161 | 776 | 244 | 1392 | 23.2 |
| 11-10 19:40 | 104 | 196 | 558 | 72 | 930 | 15.5 |
| 11-10 20:58 | 120 | 187 | 920 | 139 | 1367 | 22.8 |
| 11-10 22:36 | 82 | 174 | 664 | 111 | 1031 | 17.2 |
| 11-10 22:54 | 65 | 117 | 616 | 72 | 871 | 14.5 |
| 11-10 23:36 | 105 | 191 | 770 | 87 | 1153 | 19.2 |
| 11-11 00:19 | 214 | 166 | 572 | 72 | 1025 | 17.1 |
| 11-11 00:54 | 102 | 180 | 607 | 71 | 961 | 16.0 |
| 11-11 01:20 | 143 | 132 | 752 | 79 | 1107 | 18.4 |
| 11-11 02:37 | 73 | 189 | 559 | 84 | 905 | 15.1 |
| 11-11 03:18 | 96 | 124 | 729 | 85 | 1035 | 17.2 |
| 11-11 03:20 | 73 | 324 | 537 | 73 | 1007 | 16.8 |

Minimum 11.8 minutes, median 17.2, maximum 25.6. Waiting for a slot is not in these figures.

## 3. Which steps dominate

1. **Wave 2 is 53% to 79% of every run**, and in all fourteen runs its length is set by
   `engine_differential` and `compare` together: the two finish within 9% of each other every time (537/537,
   607/607, 725/729, 776/773, 1214/1116). Shortening one of them alone saves almost nothing; both must come
   down before `mutate` and `ny_compare` (another pair that moves together, 347/347 here) set the stage.
2. **The run-to-run spread is contention, not content.** Every wave-2 step is slower or faster by about the
   same factor from run to run (engine_differential 450 to 1214 s, compare 437 to 1116 s, mutate 265 to 686 s,
   with their ratios steady). That is what CPU starvation predicts and what the samples show: in wave 2 this
   run alone had about sixty runnable threads (six worker pools of eight open at once, plus a dozen
   single-threaded steps) on 18 cores, beside a second run doing the same. Single-threaded steps then crawl:
   `coverage` used 30 s of CPU and took 105 s; `properties` 49 s of CPU, 157 s.
3. **Wave 1 and the build barely use the machine.** The build stage is one core for 73 s while every other step
   waits for it. In wave 1 this run averaged two cores, and for its last 75 s it was one core: a single test
   file (`test_review_tools.py`).
4. A full run needs roughly 5,000 CPU-seconds (4,400 sampled, plus the short Lean and CLI processes the samples
   miss). On 18 cores that is under five minutes of work if it were spread evenly; the measured run took 16.8.
   The gap is the serial parts (build, the long poles of wave 1 and wave 2, wave 3) and the contention.

## 4. The top five steps

**compare (537 s; 437 to 1116 across the fourteen runs).** Runs 2,368 cases (every federal fixture plus 400 generated returns)
through the TypeScript evaluator and the Lean reference evaluator and compares 6.4 million line values. Each
case starts the Lean binary once, one after another (`spawnSync` in a loop). Measured on a quiet machine: 0.107 s
per start, CPU-bound, so at least 253 s of strictly serial single-core work plus about 30 s in Node. It is
single-threaded and CPU-bound; everything above about 285 s is waiting for a core.

**engine_differential (537 s; 450 to 1214).** Generates 1,700 returns, evaluates them with the project, then
runs them through PolicyEngine-US, Tax-Calculator, OpenTaxSolver and UsTaxes and compares 568,880 lines. It is a
serial pipeline: one Python process runs the engines in turn, with one Node child for UsTaxes. The samples put it
at about 360 CPU-seconds on roughly one core (a 68% mean of one core under contention, 100% once the machine was
quiet). Single-threaded and CPU-bound. The engines' outputs depend only on the generated cases, the adapters and
the installed engines (`run_engines.py` is given the cases and nothing of the project's: read in `run.sh`, not
tested), so a change to a form cannot change them.

**mutate (347 s; 265 to 686).** Applies 5,725 single-atom mutations to the federal data and judges each against
the checker and every fixture, on eight worker threads. It is CPU-bound and already parallel: 1,548 CPU-seconds,
so about 195 s on eight free cores. In this run it sat at a third of one core for its first 100 s (single-threaded
set-up, starved; each worker also rebuilds the mutant list) and reached eight cores only afterwards.

**ny_compare (347 s; 273 to 669).** The same comparison for the 938 New York cases (2.8 million values): serial
Lean starts, at least 100 s of single-core work, the rest waiting.

**self_tests (324 s; 117 to 324).** A pool running 45 self-tests side by side; its wall time is its slowest
member, `test_review_tools.py`: 246 unit tests in one single-threaded process, 161 s when run alone on a
moderately loaded machine, 324 s inside this run. CPU-bound, single-threaded; the pool has free workers while it
runs.

Close behind, and relevant to the options: **build (73 s)**. Its CPU profile shows 94% of the time in
`checkSalesInterview` (the interview path walks over the fixtures, which re-evaluate the return at every step);
loading, checking and writing the canonical data is a few seconds. It is single-threaded, and it is the same
67 to 77 s every time anyone runs `npm run build`.

## 5. Options (not implemented)

Savings are for the measured run (1007 s) unless stated. "Integrity" is what the option could let through.

**A. Commit wording-only lanes on the fast tier; run the full tier once per batch on main.** No code change:
the pre-commit hook already asks only the fast tier of a commit that changes forms and nothing in
`tools/full_paths.txt` (checked with `tier_paths.py required` on two of last night's wording commits: both
"fast"). The session's rule asked for the full tier on every lane. The fast tier drops the five slowest wave-2
steps and `human_review`; wave 2 would be set by `interview_rules` (162 s here, with less contention to slow it)
and wave 3 by `review_packets` (7 s): roughly 570 s here, 7 minutes at the median wave 1, against 17:
roughly ten minutes less per lane run. Integrity: nothing is skipped for good, since main is full-tier
green before a release and `pre-push` holds a release tag to it; but a lane's defect that only `mutate`,
`compare` or the engine differential catches surfaces after its merge, mixed with the other lanes'. The known
case is T-267 (open in `TASKS.md`): rewording a question that a pinned mutation argument reads fails `mutate`.
Doing T-267 first removes that case.

**B. Reuse the external engines' outputs when their inputs are unchanged.** Key `engines.json` by a hash of the
generated cases, the adapter code and the installed engine versions, keep it outside the per-run work folder, and
rerun the four engines only when the key changes; the project's own evaluation of the 1,700 cases and the
line-by-line comparison still run every time. Saves most of `engine_differential` (hundreds of seconds of
single-core work) on every run that does not touch `tools/engines/` or the installs, which is nearly all of them.
Integrity: the comparison of current project values is never skipped; the exposure is a key that misses an
input (an engine reinstalled in place, an environment variable such as `ENGINE_CASES`), which would compare
against outdated engine outputs. A release run could ignore the cache.

**C. Run the Lean cases through the worker pool.** `compare` and `ny_compare` start the Lean binary 3,306 times
in series; `test_fixtures` already runs its command-line cases through `mapPool`. With eight at a time,
`compare` needs about 40 s of wall time on free cores instead of 285 s or more. With B it brings wave 2 down
to `mutate` (347 s here): about 190 s saved; alone it saves nothing, because `engine_differential` is as long.
Integrity: none for content (the same binary, inputs and comparison per case); it adds eight more runnable
processes to a wave that is already oversubscribed, so the gain shrinks when two runs overlap. A batch mode in
the Lean evaluator (one process for all cases) would also cut the CPU, but changes the reference evaluator.

**D. Take the interview path walks out of the build.** Make them a step of their own beside the waves, on the
worker pool, leaving the build to check and write the canonical data in a few seconds. Saves about 65 s of
every run in every tier (the docs tier is, by the README, nearly all build), and about 65 s of every
`npm run build` in every lane's edit-build-review loop, which is where it was paid most often last night.
Integrity: today a build whose path walks fail writes no canonical data; after the split the data exists while
the walks may be failing, so tools run between a build and the next check-all would read data whose interview
paths are unchecked. Check-all still fails on them. The docs tier would need the new step or would stop
checking the walks.

**E. Split `test_review_tools.py` across the self-test pool.** Three or four entries by test class, and the
same for `test_ny_review.py`. Wave 1 is then set by `check_extraction` (248 s here, median 138): up to 76 s
saved here, about 35 s at the median. Integrity: none if the classes do not depend on each other's state (the
file sets two environment variables at import, which every shard would also do).

**F. Start the long single-threaded evaluator steps during wave 1.** `engine_differential`, `compare` and
`ny_compare` read only the build's output, the fixtures and the Lean binary, and wave 1 leaves sixteen cores
idle for three to five minutes. Started with wave 1 they would be mostly done when `mutate` starts. Saves up to
the length of wave 1 (174 s at the median) if B and C are not done; little if they are. Integrity: a failing
cheap check no longer stops the run before the expensive steps (cost, not correctness); and the header of
`check_all_steps.sh` says nothing checks that a step does not read what another step of its wave writes, so
moving steps between waves needs that audit first, or a check of declared reads and writes.

**G. Skip `mutate`, `compare` and `properties` when the computation is unchanged.** For a wording-only change
none of their outcomes can differ. A key over the canonical data with the wording fields left out (as
`subjects.of_computation` hashes a form for class M: each line's id, type and expression without the question text), the fixtures and the engine code would let a run
reuse the last green result. Saves up to all of wave 2's long poles on wording lanes. Integrity: this is the
riskiest option: the key must cover every input, and a field wrongly treated as wording would turn a real
change into a reused green. It overlaps with A, which gets the same saving with no new mechanism.

**H. Record the machine's load with the times.** Not a saving: one line with the load average at the start and
end of the run, and how many check-all slots were held, would let a slow run be read as "the machine was busy"
instead of "the suite got slower". This run's wave 1 is the example.

Not recommended: lowering `CHECK_ALL_MAX_RUNS` to 1. Overlapping runs slow each other (median 17 minutes against
11.8 for the fastest run on record), but two at a time still finish more runs per hour, because the serial
stretches of one run leave cores for the other. The evidence for the solo figure is one run whose
circumstances are not recorded.

Order by return for effort, on this evidence: A (no code), then B and C together (they free wave 2 only as a
pair), D (also speeds every lane's build), E. F and G add risk for savings the others mostly capture.

## 6. Also noticed

- `tools/README.md` says the full tier takes "about 38 minutes" and the fast tier "about 10". The fourteen
  recorded full runs took 12 to 26 minutes for their steps. The lane left the sentence as it is; the figure
  moves by a factor of two with what else the machine is doing.
- The compile stage records 0 s and `lean_build` 1 s: the TypeScript compiler finishes within the second and
  the Lean build is cached between background runs.
