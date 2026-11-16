# Plan: cutting the wall time of `mutate` (and the other slow full-tier steps)

Lane plan-mutate. Model claude-opus-5-5, judgment class; tax year 2025, jurisdiction us. Code-reading study only:
nothing was run, built or edited. Read on the xint worktree (`engine/src/mutate.ts` there differs from HEAD only by
three keyed arguments and the open-defect table). Every claim is marked **[checked: path:line]** or **[inferred]**.

## Summary

1. **The premise has moved.** The "29 of 38 minutes" figure is from 2026-11-05 (mutate 1,733 s,
   `docs/2026-11-05_release_gating_design.md:15`). On 11-09 mutation runs started evaluating only the expected lines
   (commit ce07280f) and mutate fell to 265-686 s (`docs/2026-11-11_check_all_timing.md:131-134`). On 11-15 the
   **sampled check of keyed arguments (T-280)** landed (commit 0c8cd21d), and the latest full run (worktree nx-b1,
   22:30 on 11-15) shows **mutate 2,491 s out of a 3,933 s run, ny_mutate 647 s**, against compare 828,
   engine_differential 568, ny_compare 452 and test_fixtures 231 [checked: `.git/worktrees/nx-b1/check-all-times`].
   Mutate is now the only long pole: it runs about 1,660 s past the next-slowest step.
2. **The sampled check is probably the largest part of mutate today** [inferred]. The lane that built it measured
   about 40 of 65 minutes in the sampled check (4 workers, load 150-240; `docs/provisional/lanes/g1-t3.md:110-113`).
   Its structure does a lot of repeated work. It loops site-major: 92 sites, each over about 9,360 input sets
   ((300 generated + about 2,040 fixture cases) × 4 withholding rates). For **every site and every set** it
   recomputes `allTargets(baseline, …)` and the filter of about 5,600 keys through `lineOfKey`, and it re-evaluates
   the **baseline** cone [checked: `mutate.ts:2944-2948`]. One worker also handles a whole site, the sites are
   split statically (`i += count`), and the per-site cost is very uneven [checked: `mutate.ts:3022`, `3041`].
3. **Phase 1 (judging the 7,758 mutants) does an avoidable full-data copy per mutant.** `cloneData` is a JSON
   round trip of the whole canonical data, about 10 MB pretty-printed on disk [checked: `mutate.ts:34-36`,
   `canonical/2025` totals 10,088,697 bytes]. It also runs the whole checker per mutant
   [checked: `mutate.ts:2628-2630`]. Killed mutants search the fixture cases in a fixed order, and survivors
   (about 330) evaluate every one of the 2,383 federal cases [checked: `mutate.ts:2639-2643`].
4. **Top three proposals by return for effort:**
   - **(a) Restructure the sampled check set-major.** Compute the baseline once per set, then run all of the
     worker's sites against it, and split the work by sets (or with a dynamic queue), not by static site shares.
     This keeps the same verdicts.
   - **(b) Add a kill-witness cache.** Try last run's killing case first. A kill is re-verified on the current
     tree, so this is sound with no "incremental" caveat. It is the honest form of an incremental mutate.
   - **(c) Use a dynamic task queue for both phases** (`TaskWorkers` already exists in `pool.ts`), with more workers
     once mutate is the only step left. The machine has 6 performance and 12 efficiency cores, so static equal
     shares strand work on the slow cores.

   After those come copy-on-write mutant data, a coverage filter (skip cases whose baseline evaluation never read
   the mutated atom), and seeded (incremental) evaluation of mutants. These are bigger but could save several
   times more.
5. **Measure before changing anything** (section 4). Nothing measured splits mutate into setup, phase 1, sampled
   check and self-tests, or phase 1 into clone, checker and evaluation. Every saving below is an estimate.
6. **The other slow steps.**
   - `compare` / `ny_compare`: the Lean evaluator now runs in batches of 50, but the batches still run one after
     another with `spawnSync` in a loop, and the TypeScript side is single-threaded [checked:
     `compare.ts:51,161,452-454`]. Running the batches through a pool would bring compare below mutate on free
     cores.
   - `test_fixtures`: one Node process per case, 2,383 processes, each parsing the whole canonical data
     [checked: `fixtures.ts:55-58`]. Batching (the CLI already has `eval --batch`, `main.ts:124-137`) with a
     per-case sample would save most of its 231-276 s.
   - `engine_differential`: the engine cache now exists [checked: `run_engines.py:621-626`]. Its remaining 568 s
     is not broken down and needs measuring first.

## 1. How mutate works today (what the plan rests on)

- **Setup on the main thread** [checked: `mutate.ts:3050-3068`]. Load the canonical data, build the judging cases
  (`allTargets` per case), run the checker on the baseline, evaluate every fixture case on the baseline, generate
  the mutant list, then `retargetSelfTest` (serial) before any worker starts.
- **Phase 1** [checked: `mutate.ts:2661-2694`]. `defaultWorkers()` workers: `min(cores-6, floor((cores-2)/runs))`,
  which is 8 on 18 cores with CHECK_ALL_MAX_RUNS=2 [checked: `pool.ts` defaultWorkers]. Each worker loads the
  canonical data again, rebuilds the judging cases and the whole mutant list, and takes every `count`-th mutant
  (static round-robin). For each mutant:
  - JSON-clone the data and apply the mutation.
  - Run `runChecks` on the whole data; if it fails, the outcome is "check".
  - Otherwise evaluate cases in a fixed order until the first kill: `mutation.json`, then the file named for the
    mutant's document, then every other non-class-M file, then the class M cases (where the first in file order
    is reported).
  - Each evaluation evaluates only the case's expected lines, or the whole return where a case expects a line it
    does not name.
  - **Yes, each mutant re-evaluates fixtures: a killed one stops at the first killing case, and a survivor
    evaluates all of them.**
- **Sampled check** [checked: `mutate.ts:2937-3048`]. Each keyed argument that explains a survivor, plus one
  fixture-killed control per site, is evaluated on all sets. A second "closure self-test" pass runs on the controls
  against every line of the return on the first 200 sets. A new generation of workers is used, each loading the
  data, the judging cases, the generated returns and the mutant list again. Sites are assigned statically by
  `i += count`.
- **Serial tail on the main thread** [checked: `mutate.ts:3085-3104`, `3233-3247`]. `equivalenceReason` per
  survivor, `staleEquivalences`, `staleEquivalenceSelfTest` (which rebuilds `mutations(baseline)` again),
  `premiseDigestSelfTest` (1,603 edits per the lane record), and the whole-dollar, guard, figure and choose
  self-tests. Some of these run after the sampled check, and none of them overlap with the workers.
- **Short-circuits already present.** First-kill stops the search, targets-only evaluation is used, and in the
  sampled check, where a watched line's value is exactly the same under the mutant, its readers are not evaluated.
  There is **no reuse of unaffected sub-values across evaluations**: every evaluation starts with an empty memo
  [checked: `eval.ts:88-97`].
- **Evaluator hot paths that every evaluator step pays** [checked, cost inferred]:
  - a linear `doc.lines.find` per line evaluation (`eval.ts:220`, `226`);
  - `tables.find` per table lookup (`eval.ts:587`, `616`, `647`);
  - `register.entries.find` per line with an ambiguity (`eval.ts:306`);
  - `validateInputs` rebuilds the map of legal inputs on every `evaluate` call (`eval.ts:843-873`).

## 2. Proposals for mutate, ranked

Savings are given as shares of mutate's 2,491 s on the nx-b1 run unless stated. The phase split is assumed at
about 35% phase 1, 55-60% sampled check, and 5-10% serial setup and tail. That split is **[inferred]** from the
g1-t3 note and the pre-T-280 run times, and measurement M1 settles it.

### R1. Sampled check set-major, with shared per-set baseline work (rank 1)

- **Change.** In `sampledShare`, loop sets outermost and sites inside.
  - Per set: compute `every = allTargets(baseline, inputs)` once, index its keys by `lineOfKey` once (a
    `Map<line, key[]>`), and evaluate the baseline once on the union of all sites' targets, or the whole return.
    Then, per site, `own` and the closure targets are lookups, and `ownBase` and `base` are read from that one
    baseline result.
  - This relies on the invariant that a line's memoized value does not depend on which other targets were asked
    for. The code already relies on it [checked: comment at `mutate.ts:2595-2600`].
  - Keep per-site result objects across sets. To keep the witness text identical (`contradicted ??=` takes the
    first set in set order), process sets in order within a worker. If sets are split across workers, merge by the
    lowest set index.
  - Split work by **set ranges** (for example 9,360 sets in chunks of 100 on a dynamic queue) instead of by sites.
    This removes the per-site straggler and spreads the baseline work once over the machine. `exercised`,
    `reached` and `sets` are sums, and `contradicted`, `partial` and `closureMiss` take the minimum set index:
    a mergeable reduction.
- **Expected saving** [inferred]. Per site-set, today's work is: `allTargets` (about 3,100 top-level line ids plus
  collection keys), a filter of about 5,600 keys through `lineOfKey`, one baseline cone evaluation, about 2.2
  mutant cone evaluations (claimed plus control), and the closure evaluations where the result is not exact. The
  first three become roughly 1/92 of their present cost, which is perhaps 35-50% of sampled-check CPU. Removing
  the per-site straggler adds more. Estimate: the sampled check falls by 40-60%, about 500-900 s of mutate's wall
  time.
- **Risk to what the check proves.** None, if the reduction reproduces today's results. Verify by running old and
  new on the same tree and diffing `mutation.md` and the per-argument rows byte for byte.
- **Memory.** One set's baseline derivations at a time per worker. That is small.
- **Effort.** Medium: about a day of Opus work in `mutate.ts` (`sampleSite`, `sampledShare`, `sampledResults`) and
  `mutate-worker.ts`.
- **Files.** `engine/src/mutate.ts`, `engine/src/mutate-worker.ts`, and possibly `engine/src/pool.ts` (TaskWorkers
  for the chunk queue).

### R2. Kill-witness cache (rank 2)

- **Change.** At the end of a run, write `{mutant id: outcome, killing case id}` to a cache outside the tree, for
  example `<git common dir>/mutate-cache/<year>-<us|ny>.json`. It is not committed and is keyed by nothing. In
  `outcome()`, put the cached killing case first. All non-class-M cases still come before class M ones, and the
  class M order stays fixed.
- **Why it is sound** [checked: `mutate.ts:2624-2626` says "any order gives the same outcome, the first kill only
  ends the search sooner"]. The hint changes only the search order, and the kill is **re-evaluated on the current
  data**. A stale hint costs one wasted evaluation. Survivors still search everything, as they must. So, unlike a
  scope-incremental mutate, a run with the cache still proves exactly the full claim, and the green record needs
  no new caveat.
- **Expected saving** [inferred]. The saving is the evaluations a killed mutant now spends before its first kill,
  beyond one. Its size is unknown, because the fixed order already puts `mutation.json` and the mutant's own form
  first. Measurement M3 gives the number of cases evaluated per killed mutant. If it averages 10 or more, this is
  a large share of phase 1. If it is about 2, it is small. Plausible range: 0-25% of phase 1, about 0-200 s.
- **Effort.** Small: about 40 lines.
- **Risk.** None to verdicts. A corrupt cache file must fall back to the default order, never fail the run.
- **Files.** `engine/src/mutate.ts` and `tools/check_all_steps.sh` (to state where the cache lives). The cache is
  also a natural home for per-mutant timings, used for LPT scheduling (R3).

### R3. Dynamic scheduling and worker count (rank 3)

- **Change.**
  - Replace the static `i += count` shares in both phases with a queue: `TaskWorkers` in `pool.ts` already serves
    tasks one at a time [checked: `pool.ts` class TaskWorkers, `run(task)`]. Use chunks of about 25 mutants, or
    one site or set chunk for the sampled check. Workers load once and serve both phases, so the second
    generation of loads disappears.
  - Order the sampled-check sites by expected cost, largest first (LPT), using the last run's
    `MUTATE_SAMPLE_TIMES` figures from the R2 cache.
  - Size the pool to the machine: when mutate is the only long step left, as it is for about 1,600 s of every full
    run today, 8 workers leave about 10 cores idle. Either start `cores-2` workers and let the queue absorb the
    oversubscription early in wave 2, or grow the pool when `os.loadavg()[0]` falls below the core count.
- **Why it matters** [inferred]. 18 cores is 6 performance plus 12 efficiency
  (`docs/2026-11-11_check_all_timing.md:28`). A static equal share that lands on efficiency cores finishes late
  even on a quiet machine. Under load, any worker that is descheduled holds back the whole run.
- **Expected saving.**
  - Balance alone: about 10-30% of each phase's wall time, mainly in the sampled check, where 92 uneven sites
    over 8 workers give about 11.5 sites per worker.
  - Growing to about 14-16 workers after wave 2's other steps finish: up to about 40% of the remaining time on a
    run with no second check-all.
  - With two runs at once the gain shrinks, and `defaultWorkers` already shares cores between slots.
- **Risk.** None to verdicts: outcomes are indexed and the mutant-list digest check stays. More workers add
  memory, about a canonical copy (tens of MB) per worker [inferred].
- **Effort.** Small to medium.
- **Files.** `engine/src/mutate.ts`, `engine/src/mutate-worker.ts`, `engine/src/pool.ts`.

### R4. Copy-on-write mutant data, with a frozen baseline (rank 4)

- **Change.** Every mutation changes exactly one of three things [checked: `mutate.ts:148-293`]:
  - one line of one document (its `expr`, or its `refuses` list or an entry of it, located by document id and
    line index);
  - one parameter entry;
  - one rate table's bands.

  Build the mutant's data as a shallow copy:
  - the `forms` / `defs` arrays are copied with only the touched document deep-cloned (its `lines` array copied
    and only the touched line deep-cloned);
  - or `params.values` is shallow-copied with only the touched entry cloned;
  - or `tables` is copied with only the touched table cloned.

  Deep-freeze the baseline in each worker, so that any `apply` writing outside its declared atom throws (ES
  modules are strict mode) instead of silently corrupting later mutants.
- **Expected saving** [inferred]. A JSON round trip of several MB is plausibly 30-80 ms. Over 7,758 mutants that is
  about 230-620 CPU-seconds, or 30-80 s of wall time on 8 workers. It also makes R6's mutant-major-to-case-major
  inversion affordable in memory.
- **Risk.** An `apply` that touches something else. The freeze turns that into a crash, not a wrong verdict. The
  evaluator must not write to `data` either; the freeze checks that too. Add a self-test that runs a sample of
  mutants both ways and compares outcomes.
- **Effort.** Small to medium: a `site` descriptor per Mutation, which `siteOf()` already almost is, plus a
  `mutantData(baseline, m)` function.
- **Files.** `engine/src/mutate.ts`.

### R5. Main-thread work overlapped with the workers (rank 5)

- **Change.**
  - Start the phase-1 workers before `retargetSelfTest`, and run `retargetSelfTest`, `premiseDigestSelfTest`,
    `wholeParamSelfTest`, `unknownGuardSelfTest`, `guardedFigureSelfTest` and `scalarChooseSelfTest` on the main
    thread while the workers run. They depend only on the baseline [checked: their signatures at
    `mutate.ts:2108,2256` and the self-tests at `3233-3247`].
  - Have the workers return a digest so they do not have to rebuild `mutations(baseline)`. They need the list
    anyway to apply mutants, so instead cache `mutations()` per thread.
- **Expected saving** [inferred]. Whatever these take serially, unmeasured (M1 shows it). The timing doc saw mutate
  "at a third of one core for its first 100 s" (`docs/2026-11-11_check_all_timing.md:133-134`). That was partly
  this and partly starvation. Estimate 30-120 s.
- **Risk.** None. **Effort.** Small. **Files.** `engine/src/mutate.ts`.

### R6. Coverage filter: skip cases that never read the mutated atom (rank 6; larger saving, needs care)

- **Change.**
  - Instrument `evaluate` with an optional `touched` recorder: every `(document id, line index)` that `evalLine`
    enters, including lines whose memo entries are later rolled back (`eval.ts:258-263`, `chooseUnresolved` at
    `720-740`), every parameter read (`eval.ts:328`), and every table read (`eval.ts:587/616/647`).
  - Per worker, evaluate each case once on the baseline with the recorder and keep a bitset of about 6,000 lines
    plus the parameters and tables. That is under 1 KB a case, about 2-3 MB for 2,383 cases.
  - In `outcome()`, skip any case whose baseline evaluation never touched the mutant's atom.
  - For targets-null cases (whole-return evaluation), `allTargets` depends only on documents, collections and
    rosters, which no mutant changes [checked: comment `mutate.ts:2601-2602`, `eval.ts:156-180`].
- **Why it is sound** [inferred, but a short argument]. Evaluation is a deterministic function of (data, inputs,
  targets). A mutant differs from the baseline only inside one line's `expr` or `refuses`, one parameter, or one
  table. If the baseline evaluation never entered that line, never read that parameter and never read that table,
  the mutant's evaluation takes identical steps and gives identical values.
  - The one static read of other lines' structure, `guardsCover`, reads only line **types** and enum values
    [checked: `eval.ts:750-775`], and no mutation changes a type [checked: `mutate.ts:148-293`].
  - `validateInputs` reads types only.
  - This assumes `evaluate` has no other read of `data` that a mutation can change. A grep finds only those listed
    above [checked: `eval.ts` matches for `ctx.data.`, `.find(`], but the implementer must re-audit.
  - Self-test: for a random 2% of mutants, also run the unfiltered search and require the same outcome. Also plant
    a mutation in an untouched line and require that the filter skips it while a forced evaluation shows no change.
- **Expected saving** [inferred]. Mostly on survivors: about 330 survivors × 2,383 cases is about 786,000 case
  evaluations. A survivor on a line that only rental, Form 8582 or Form 1116 cases reach would evaluate tens of
  cases instead of 2,383. Lines that every return reaches (f1040 totals) gain nothing. Plausibly 40-70% of phase 1's
  evaluation CPU if survivors dominate it, as they do if per-case evaluation costs about 1.5 ms (M3 settles this).
- **Effort.** Medium: an evaluator hook plus the bookkeeping. Hooks in `eval.ts` touch a file every evaluator step
  uses, so the hook must cost nothing when it is off.
- **Files.** `engine/src/eval.ts` (an optional recorder in `EvalOptions`) and `engine/src/mutate.ts`.

### R7. Seeded (incremental) evaluation of mutants (rank 7; largest potential saving, most work)

- **Change.** Add `EvalOptions.seed: Map<string, Derivation>`, a memo pre-filled with the **baseline's** derivations
  for every key whose line (`lineOfKey`) is outside the downstream closure of the mutant's site (`downstreamOf` /
  `siteLines` exist already [checked: `mutate.ts:2865-2907`]). The mutant's evaluation then recomputes only the
  mutated line and its readers.
  - In the sampled check, the "own" evaluation becomes one line instead of a cone.
  - In phase 1 (combined with R4, and a case-major loop so that one baseline memo per case is live at a time),
    each case evaluation recomputes only the closure.
- **Why it is sound.** It is exactly as sound as the closure. The closure is already self-tested on the controls
  against every line of the return (`closureMiss`) [checked: `mutate.ts:3027-3030`, `3119-3120`]. Add a stronger
  self-test: for a sample of mutants and sets, seeded and unseeded evaluation must give identical derivation maps.
  - Seeded entries must never be in `memoLog`, so `chooseUnresolved`'s rollback cannot delete them. Lines the
    baseline rolled back are simply absent from the seed and are recomputed.
- **Expected saving** [inferred]. Cone evaluations become closure evaluations, possibly 3-10× less evaluation CPU in
  both phases. Not estimable without M2/M5 profiles.
- **Risk.** Medium. The value of a memo key must be context-free across two different evaluations (the evaluator
  assumes it within one). A wrong closure would let a real difference through, turning a killable mutant into a
  survivor (a false "equivalent" in the sampled check, or a lost kill in phase 1). Adopt only behind an A/B run
  (old and new on the same tree, identical outcomes array and report) and keep the unseeded path as a release
  option (`MUTATE_SEED=off`).
- **Effort.** High: about 2-3 days of Opus work. **Files.** `engine/src/eval.ts`, `engine/src/mutate.ts`.

### R8. Evaluator micro-optimizations (rank 8; helps every evaluator step)

- **Change.** Per-document `Map` indexes (line id to line) cached in a `WeakMap` keyed by the document, replacing
  `doc.lines.find` at `eval.ts:220`, `226`, `770`, `772`. Also a table index and an ambiguity-register index, and
  `validateInputs`' legal-input map cached per `data` (`WeakMap`) and reused across calls.
- **Expected saving** [inferred]. Unknown until profiled. Documents average about 70 lines (5,887 lines over 87
  documents), and some have hundreds, so `find` per line evaluation is plausibly a few to 20% of evaluator CPU.
  This would speed mutate, compare's TypeScript side, test_fixtures, properties, interview walks and the build's
  path walks (94% of the build, `docs/2026-11-11_check_all_timing.md:144-147`).
- **Risk.** Low: same semantics, with the caveat that cached indexes must be keyed by the data object, since
  mutants are different objects (with R4, a cloned document is a new key). **Effort.** Small.
- **Files.** `engine/src/eval.ts`.

### R9. Fewer sampled sets (owner decision; reduces what is checked)

- **Dedupe.** Many fixture cases may share inputs after withholding. Dedupe sets by a hash of their inputs and
  keep the first label. This is a zero-risk saving of unknown size; M5 counts the duplicates.
- **`MUTATE_SAMPLE`.** It lowers the 300 generated returns, but the fixture sets are the larger share
  (2,040 × 4 versus 300 × 4) [checked: `mutate.ts:2803-2849`]. Sampling the withheld-rate copies of fixture cases
  (for example rates 0.1/0.3/0.6 on a fixed half of the cases) would roughly halve the sampled check, but it
  weakens the claim "checked on every fixture case at every rate". That is the owner's decision, and
  `mutation.md` must state the sample actually used.

### Not recommended now: a scope-incremental mutate (only mutants of changed lines)

- **Why it is unsound as stated** [inferred]. A mutant's outcome depends on the whole mutated data, every fixture
  and the evaluator. A change to line Y can change the outcome of a mutant on any line X connected to Y through
  the graph, upstream or downstream, and a fixture change can change any mutant. "Mutants of changed lines" would
  miss these.
- **What it would need.** A mutant must be rerun when its site's closure or a killing case's cone meets the change
  set. Computing that is about as hard as R6/R7 and gives less.
- **If adopted anyway, the green record must say so.**
  - Record `mutate_scope=full|incremental:<base tree>` beside `tier` in the green record (`tools/green.sh`,
    `check_all.sh`).
  - `pre-push` must refuse an `r*` tag whose record lacks `mutate_scope=full`.
  - An incremental run must not write `reports/<year>/mutation.md`, whose score and survivor list claim the whole
    population; it would write a separate scoped report.
  - The README's guarantee sentence for releases stays as it is.
- **Recommendation.** R2 gives most of the incremental benefit for killed mutants while still proving the full
  claim, and R6/R7 cut the survivor cost without changing scope. Prefer them.

### Not recommended now: reusing survivor or sampled verdicts by a content digest

Reusing verdicts across runs when a digest of the computational data, fixtures and engine is unchanged (option G
in the timing doc) helps only wording-only trees, which the fast tier already serves. A field wrongly treated as
wording would turn a real change into a reused green. If ever done, it needs a `use|verify|off` mode like
`ENGINE_CACHE`, with `off` forced at release.

### Expected combined effect on mutate

[inferred, to be replaced by measurement]

| Proposals | Mutate wall time on a quiet machine | With mutate as the only remaining long step |
|---|---|---|
| R1 + R3 + R5 | about 2,491 → 1,200-1,500 s | lower still |
| plus R4 and R2 | a further 100-300 s off | |
| R6 and R7 | could bring mutate to the 300-600 s range | |

At 300-600 s, compare (828 s, already parallelisable) would be the long pole again. ny_mutate (647 s) shares all
the code and benefits equally.

## 3. The other slow steps

### compare / ny_compare (828 s / 452 s on nx-b1)

- **Now** [checked]. Lean runs in batches of 50 cases per process (`compare.ts:48-51`), but the batches run
  serially with `spawnSync` in a `for` loop (`compare.ts:452-454`, `161`), and the TypeScript evaluation and the
  comparison of each case run on the main thread between batches.
- **C1.** Run the batches through `mapPool` with an async spawn. `pool.ts` `run()` ignores stdin, so a variant
  that writes the case lines to stdin is needed. Do the TypeScript side per batch in a worker, or keep it on the
  main thread overlapped with the running Lean children.
  - Saving [inferred]: on free cores, about 1/k of the Lean time with k processes, plus the overlap. Estimate
    828 → 150-250 s, and ny_compare 452 → 100-150 s.
  - Risk: none to content (same binary, same inputs, same comparison). The time-limit and `runner.stopped`
    semantics need care: one stopped batch must still stop every later one, which in a pool means "no new batch
    starts".
  - Effort: small to medium. Files: `engine/src/compare.ts`, `engine/src/pool.ts`.
- **C2.** R8 speeds `tsEvaluate` (whole-return evaluation per case, `compare.ts:252-261`).
- **Measure first** (M6): the split between Lean and TypeScript time.

### engine_differential (568 s on nx-b1; 937 s on nx-speed)

- **Now** [checked]. `tools/engines/run.sh` runs these serially: generate cases (python), `node … eval --batch`
  over all cases in one process, the UsTaxes adapter self-test, `run_engines.py` with the engine-record cache
  (`ENGINE_CACHE`, `run_engines.py:621-626`), then `compare.py`.
- **Unknown.** Whether the cache hit on those runs, and where the 568 s goes. The step log is kept only on
  failure [checked: `tools/check_all_steps.sh:114,149`].
- **E1.** Measure (M7). If the cache missed, find which key component changed.
- **E2.** If `node eval --batch` is large, split the cases over N processes, as `mapPool` does elsewhere.
  - Risk: none to content. Effort: small. File: `tools/engines/run.sh`, or a small node driver.
- **E3.** If `compare.py` or case generation dominates, profile it (`python -X importtime`, cProfile).

### test_fixtures (231 s; 276 s on batchB2)

- **Now** [checked: `fixtures.ts:55-58`]. Each of 2,383 cases spawns `node main.js eval --inputs … --json`, which
  starts Node and parses about 10 MB of canonical JSON each time (`canonical.ts:10-25`).
- **F1.** Run the cases through `eval --batch` (`main.ts:124-137`) in about 16 chunks on the pool. Keep the
  per-case CLI path for a fixed sample (say 50 cases, chosen by a seed, plus every case of one small file), so
  that `--inputs/--json` stays exercised end to end.
- **Check before adopting.** Whether the `--json` single-case output and the batch output are serialized by the
  same `resultToJson`; batch mode calls `resultToJson(…, false)` at `main.ts:134`.
- **Saving** [inferred]: most of the step, 231 → 30-60 s.
- **Risk.** The step's claim "passed through the command-line program" stays true (it is still the CLI), but most
  cases would go through `--batch`, not `--inputs`. Say so in the step output.
- **Effort.** Small. **Files.** `engine/src/fixtures.ts`.

### ny_mutate (647 s)

Same code as mutate. Every R-proposal applies. Its sampled check includes 22 New York band-edge arguments that no
sample reaches by design (`mutate.ts:2785-2802`). Those are still evaluated on every set, and could be skipped once
`UNEXERCISED_IF` holds. That would be a small change in what is reported, so it is the owner's decision.

## 4. Measurements to take first (once the machine is free; nothing here was run)

Run from the xint worktree after its check completes, on a quiet machine, one measurement at a time. The worktree
is called `$WT`. No paid calls.

**M1. Mutate phase timeline and resource use.**

```sh
cd $WT && MUTATE_SAMPLE_TIMES=1 /usr/bin/time -l node engine/dist/main.js mutate --year 2025 2>&1 \
  | while IFS= read -r l; do printf '%s %s\n' "$(date +%s)" "$l"; done > /tmp/m1.log
```

- The first `sampled check:` line marks the end of phase 1 plus the respawn. The last one marks the end of the
  sampled check, and the final summary lines mark the end of the tail.
- `time -l` gives user+sys CPU and peak RSS.
- Repeat with `--ny`.
- From the per-site times, compute the maximum and mean per-worker sum, which gives the straggler cost.

**M2. Phase-1 CPU profile on one slice, single-threaded.**

```sh
cd $WT && node --cpu-prof --cpu-prof-dir=/tmp/mprof --input-type=module -e \
  "process.argv.push('--year','2025'); const m = await import('./engine/dist/mutate.js'); \
   const t = Date.now(); const r = m.mutantShare(0, 50); console.log(Date.now() - t, r.outcomes.length)"
```

This covers about 155 mutants. Open the `.cpuprofile` in Chrome DevTools and read the self and total time of
`cloneData` (JSON.parse/stringify), `runChecks`, `evaluate`, `evalLine`, `Array.prototype.find`, `validateInputs`,
`allTargets`, and setup (`loadCanonical`, `mutations`, `judgingCases`).

**M3. Per-mutant search counts.** Write a read-only `/tmp` script that reproduces `outcome()` from the exported
pieces (`mutations`, `runChecks`, `evaluate`, `allTargets`, `loadFixtureCases`) on the same slice and records, per
mutant:

- the clone time;
- the checker time;
- the number of cases evaluated before the first kill;
- the evaluation time.

From these, read the survivors' share of phase-1 evaluation CPU (which sizes R6) and the mean number of cases per
killed mutant (which sizes R2).

**M4. A coverage estimate for R6, before building it.**

- In the M3 script, for each survivor, count the cases whose baseline derivation keys include the mutated line,
  using `lineOfKey` on `evaluate(...).derivations` keys as a lower bound on what is touched.
- The ratio to 2,383 estimates R6's saving.

**M5. Sampled-check profile and set duplicates.**

- `node --cpu-prof` on the whole `mutate` run. Check that the worker profiles appear (Node 24 writes one per
  thread, to be confirmed). If they do not, run with `MUTATE_WORKERS=1 MUTATE_SAMPLE=30`.
- Read the share of `allTargets`, `lineOfKey`, the baseline `evaluate` in `sampleSite`, the mutant `evaluate`, and
  `valuesOf`.
- In a `/tmp` script, count the distinct input sets among the 9,360 (a hash of `stableStringify(inputs)`); this
  sizes R9's dedupe.

**M6. compare split.**

- `node --cpu-prof engine/dist/main.js compare --year 2025` gives the main-thread TypeScript time.
- Separately, time one Lean batch:

```sh
/usr/bin/time -l lean/.lake/build/bin/taxeval --canonical canonical/2025 < /tmp/batch50.jsonl > /dev/null
```

  Build `/tmp/batch50.jsonl` from 50 fixture inputs. Multiply by 48 batches. The difference from the step time is
  the TypeScript side and waiting.

**M7. engine_differential breakdown.**

```sh
cd $WT && PS4='+ $(date +%s) ' bash -x tools/engines/run.sh --year 2025 2>&1 | tee /tmp/m7.log
```

Read the time per stage and whether each engine logged "stored record reused".

**M8. test_fixtures, batch against per case.**

- `time node engine/dist/main.js eval --year 2025 --batch /tmp/all_cases.json > /dev/null`, against the step's own
  time.
- Diff the batch output of five cases against their `--inputs … --json` output.

**M9. Load context.** Record `uptime` (load average) and the slots held (`tools/check_all_bg.sh --status`) beside
every measurement. Run-to-run spread is mostly contention (`docs/2026-11-11_check_all_timing.md:102-107`).

## 5. Suggested order

1. **Measure:** M1, M2, M3 and M5, about an hour of machine time.
2. **The verdict-neutral cheap ones:** R3 (queue and worker count), R5 (overlap) and R2 (kill witness). Verify
   each with an A/B diff of `mutation.md` and the outcomes on the same tree.
3. **R1 (set-major sampled check),** with the same A/B. In parallel lanes: C1 (compare pool) and F1
   (test_fixtures batching), since they touch other files.
4. **R4 and R8,** guided by M2.
5. **R6, then R7,** only if M3/M4/M5 show evaluation dominates after steps 2-4. Each lands behind an A/B equality
   run and its own self-test. R7 keeps an off switch for release runs until it has a record.

All of these are mechanical-to-judgment code work on Opus (R1, R6 and R7 are judgment because of the soundness
arguments). None needs a paid review call. Each change to `mutate.ts` needs a full-tier run at commit time under
the release-gating rules (`docs/2026-11-05_release_gating_design.md`, "When to release").
