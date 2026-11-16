# Lane v2-mutate: two verdict-preserving speed-ups for `mutate` (UNTESTED drafts)

Model claude-opus-5-5, judgment class; tax year 2025, jurisdiction us (the code is shared, so `--ny` is affected too).
Nothing here was compiled, type-checked or run. A release-gating check had the CPU. Both patches are **untested**.
Each claim is marked **[checked: path:line]** (read in xint's `engine/src`, line numbers as of tonight) or **[inferred]**.

## Summary

- **Files.**
  - `/tmp/nightplan/patches/v2/mutate-1.patch` is change 1, the sampled check run set by set. It applies to xint as of
    tonight (`git apply --check` passed). It touches `engine/src/mutate.ts`.
  - `/tmp/nightplan/patches/v2/mutate-2.patch` is change 2, one work queue on `TaskWorkers`. It applies **on top of
    patch 1**: `git apply --check` passed on a copy of xint's files with patch 1 applied, and the result matched my
    edited copies byte for byte. It touches `engine/src/mutate.ts` and `engine/src/mutate-worker.ts`.
  - Scratch copies are in `/tmp/nightplan/scratch/v2-mutate/{a,b1,b2}`. xint was not written to; its `mutate.ts`
    still matches `a/`.
- **Change 1 is narrower than plan R1, on purpose.** The plan said to evaluate the baseline once per set on the union
  of all sites' targets, and read each site's `ownBase` and `base` from that one result. That would **not** keep the
  output byte-identical. The comparison reads the baseline map's key set, not only its values:
  - `exact = ownMutant.size === ownBase.size`;
  - a key missing from `ownBase` sets `infected`;
  - `b === undefined` in the readers' loop still sets `infected`
  
  [checked: `mutate.ts:2960-2964`, `2977-2983`]. A union evaluation memoizes more keys, so `reached` and `exercised`
  could change.

  Patch 1 shares only what is provably the same:
  - `allTargets` once per set;
  - `lineOfKey` once per key per set;
  - a fast "no watched line in this set" skip;
  - the baseline evaluations shared exactly where two sites ask for the **identical** target list (same watched set);
  - the closure self-test's whole-return baseline evaluation shared by every control in a block.

  The per-site baseline cone evaluation (`ownBase`) remains per site unless sites share a watched set.
- **Memory forced a block design** [inferred]. Running set by set holds every mutant's copy of the data for the whole
  loop, and a copy is a full canonical clone (`cloneData` is a JSON round trip, `mutate.ts:34-36`). The plan's
  "memory is small" left these copies out. With about 260 plan mutants (76 sites in xint's report,
  `reports/2025/mutation.md:1783`), a worker's static share would hold about 34 clones at once. Patch 1 therefore runs
  set by set within **blocks** of consecutive sites capped at `MUTATE_SAMPLE_BLOCK` mutants (default 8). The block
  composition cannot change any result (see below), so the default is a pure speed/memory knob for the A/B to tune.
- **Change 2** replaces the static `i += count` shares of both phases with one `TaskWorkers` pool:
  - phase 1 runs as chunks of 16 mutants;
  - the sampled check runs as patch 1's blocks;
  - workers load once and serve both phases, so the second generation of loads disappears;
  - workers start before the main thread's baseline checks, so their loading overlaps it.
- **Verdicts, `mutation.md` and stdout should be byte-identical by design.** The argument is per-mutant purity plus an
  unchanged per-mutant order of sets (section 2.3 and section 3.3). The A/B protocol (section 4) is the test. stderr
  changes only under `MUTATE_SAMPLE_TIMES`, which now prints one line per block instead of per site.
- **Expected saving: unknown, and probably smaller than the plan's R1 estimate** [inferred].
  - Patch 1 removes most of the per-site, per-set `allTargets` and 5,600-key filter cost, which today is paid
    76 × about 9,000 times. It also shares the 200-set whole-return baseline evaluations.
  - It leaves the cone evaluations, which may dominate.
  - Patch 2 removes stragglers and one load generation.
  - The A/B timing (section 4) is the first measurement of either.
- **Not addressed, listed for later:**
  - splitting the sampled check by set ranges (the merge rule is derived in section 2.5);
  - LPT ordering of blocks;
  - an exit listener in `TaskWorkers` (section 3.4).

## 1. Files and how they were checked

| File | Applies to | Check done |
|---|---|---|
| `mutate-1.patch` | xint working tree (`engine/src/mutate.ts` at 3,255 lines) | `git apply --check -v` in xint: clean; xint unchanged afterwards (`cmp`) |
| `mutate-2.patch` | xint + patch 1 | `git apply` of patch 1, then `--check` and apply of patch 2, on a copy in `/tmp/nightplan/scratch/v2-mutate/check`; `diff -r` equal to `b2/` |

What was **not** done:
- `tsc` was not run.
- Type risks to watch at the first compile:
  - `new Map(sites.flatMap(fresh))` with `readonly [string, SampledResult]` tuples (the ES2015 Map constructor
    accepts readonly tuples) [inferred];
  - the `(from): MutateTask =>` and `(block): MutateTask =>` annotations, which keep the `kind` literals from
    widening;
  - `replies.flatMap((r) => (r.kind === "mutants" ? r.outcomes : []))`.
- `noUnusedLocals` is off (`engine/tsconfig.json`), so the kept `mutantShare` export and the `SampledSite.site`
  field are not errors.

Reading the diff: patch 1 de-indents the per-mutant loop by one level (it moved out of a `for (const set of sets)`).
`git diff -w` shows the substantive change in about 146 changed lines.

## 2. Change 1: the sampled check, set by set, in blocks (`mutate-1.patch`)

### 2.1 What each hunk does

- **`sampleSite` is removed** (it was at `mutate.ts:2931-2994`). Its per-set body becomes `sampleSiteSet`, unchanged
  statement for statement except where it gets its inputs:
  - `own` is `sb.every.filter((_, j) => s.watched.has(sb.lines[j]))`, cached in `sb.own` under the site's `group`
    (its watched lines, sorted and joined);
  - `ownBase` is that cache entry's `derivations`;
  - `targets` and `base` come from `readers()`, cached in `sb.readers` under `group`, or under `EVERY_LINE` when
    `full`;
  - `if (own.length === 0) continue;` becomes `if (!watch.some((l) => sb.present.has(l))) return;`.
- **New type `SampledSite`** and function `sampledSite(baseline, site, muts)`. These are the per-site constants that
  `sampleSite` used to compute at its top (`siteLines`, `watched`, `closure`, the mutant clones), plus `group`.
- **New type `SetBaseline`** and function `setBaseline(baseline, set)`:
  - `every = allTargets(baseline, set.inputs)`, `lines = every.map(lineOfKey)` and `present = new Set(lines)`;
  - empty caches `own` and `readers`, discarded after the set.
- **New `sampledBlock(baseline, sets, byId, block)`.**
  - It builds the block's sites. The controls reuse the main pass's clones (`slice(p.claimed.length)`), and sites
    without controls are dropped from the self-test.
  - It then loops over the sets in order. Per set it builds one `SetBaseline`, runs every site's main pass
    (`ANSWERED_ONLY`, `full=false`), and, for set index < `CLOSURE_TEST_SETS`, runs the controls' closure self-test
    (`new Set()` as answered-only, `full=true`) into a separate `whole` map.
  - Finally it copies `closureMiss` from `whole` into `results`, exactly as `sampledShare` did
    [checked: old `mutate.ts:3029-3030`].
- **New `sampledBlocks(plan)` and `SAMPLE_BLOCK`** (env `MUTATE_SAMPLE_BLOCK`, default 8). These cut the plan into
  blocks of consecutive sites with at most that many mutants; a larger site is a block alone.
- **`sampledShare(index, count, plan)` keeps its signature.** Its share is `plan.filter((_, i) => i % count === index)`,
  the same sites in the same order as `for (i = index; i < n; i += count)`. It runs its share block by block.
  `sampledResults` and `mutate-worker.ts` are untouched by patch 1.
- **`MUTATE_SAMPLE_TIMES` (stderr)** now prints `sampled check: <site>, <site>, …: N ms` per block.

### 2.2 Where the time goes and what this saves [inferred, unmeasured]

Per site and per set, the old code did all of the following [checked: old `mutate.ts:2944-2948`]:
- `allTargets` (about 3,100 top-level ids plus collection keys);
- `lineOfKey` on every key (a regex for collection keys) to filter `own`;
- on about 9,000 sets per site, even where `own` came out empty;
- then one baseline cone evaluation.

Patch 1 changes this as follows:
- The first two now happen once per set per block.
- A site with no watched line in the set costs `|watch|` set lookups.
- The `own` and `readers` filters are index lookups.
- The closure self-test's whole-return baseline evaluation (`valuesOf(baseline, …, every)`), which was computed per
  control per set on 200 sets, is now once per set per block.

What is not saved:
- the baseline cone evaluation `evaluate(baseline, inputs, own)` for each site with a distinct watched set;
- the mutant evaluations.

How much this saves depends on how the sampled check's CPU splits between target building and evaluation, which
nobody has profiled (plan M5). With the default block of 8 mutants (about 2.3 sites per block), the shared part
shrinks about 2.3-fold. A bigger block shares more but holds more clones; the A/B sweeps it (section 4, step 6).

### 2.3 Why it cannot change a verdict or a byte of the report

A mutant's `SampledResult` is a fold over the sets, in order. Each step reads only the following: the set
(`label`, `rate`, `inputs`), `answeredOnly`, `full`, `own`, `ownBase`, the mutant's data, the readers' targets and
baseline values, `exclude`, `closure`, `watch`, and `isHelper(baseline, ·)`. It writes only the mutant's own `r`
[checked: old `mutate.ts:2951-2991`, unchanged in `sampleSiteSet`]. So the result is unchanged if each of those
inputs is equal and the sets are met in the same order.

1. **Skip test.** Old: skip where `own` is empty, with `own = every.filter((k) => watched.has(lineOfKey(k)))`. New:
   skip where no `l` in `watch` is in `present = {lineOfKey(k) : k ∈ every}`. These are equivalent:
   `∃k: lineOfKey(k) ∈ watched` ⇔ `watched ∩ present ≠ ∅`, and `watch` and `watched` have the same elements.
2. **`own` is the same array.**
   - It is the same filter over the same `every`, with `lines[j] = lineOfKey(every[j])` precomputed.
   - `allTargets` reads only `data.forms`, `data.defs` and the inputs' rosters [checked: `eval.ts:156-180`].
   - `lineOfKey` is a pure string function [checked: `mutate.ts:2854-2861`].
3. **`ownBase` is the same map.** It is `evaluate(baseline, set.inputs, own)` with identical arguments. For a cache
   hit, another site with the same `group` asked first, and the same group means the same watched set, so the same
   `own` by point 2.
   - `evaluate` builds a fresh context per call (`memo`, `memoLog`, `byId`) [checked: `eval.ts:81-127`].
   - `eval.ts` has no module-level mutable state [checked: grep for top-level `let`, `var`, and
     `const … = new Map/Set/WeakMap` finds none in `eval.ts`].
   - The readers of the shared map only call `get`, `size` and iterate [checked: `sampleSiteSet` body].
4. **The readers' targets and values are the same.**
   - Old: `targets = full ? every : every.filter((k) => closure.has(lineOfKey(k)))` and
     `base = valuesOf(baseline, inputs, targets)`.
   - `closure` is the union of `downstreamOf(baseline, w)` over the watched lines, a function of the watched set. So
     the same group gives the same targets, and `EVERY_LINE` gives `every` for all sites.
   - `valuesOf` returns a fresh map that is only read.
   - The cache key cannot collide: a group is newline-joined line ids, and `EVERY_LINE` starts with NUL.
5. **The mutant data is the same.**
   - Each mutant has its own clone, made as before (`cloneData` + `apply`).
   - The closure self-test now reuses the control's main-pass clone instead of making a second one. That is equal as
     long as `evaluate` never writes to `data`. The old code relies on the same thing: it evaluated one `baseline`
     object about 9,000 × 76 times per worker [inferred from the structure; grep finds no `ctx.data.… =` write in
     `eval.ts`].
   - The `apply` bodies write only into the object passed in [checked: `mutate.ts:158-290`].
6. **Order.** Within a block, every mutant meets the sets in index order. Interleaving other sites' calls only
   reorders pure calls. The first-witness fields (`contradicted ??=`, `partial`, `closureMiss ??=`) and the
   early-return after a contradiction therefore behave as before.
7. **Self-test scope.**
   - The controls are run with `full=true` on exactly the first `CLOSURE_TEST_SETS` sets (`j < 200` ⇔
     `sets.slice(0, 200)`).
   - The answered-only set is empty, and results go to a separate map.
   - Only `closureMiss` is copied back, as before.
   - Dropping control-less sites from the self-test drops only work whose result was discarded (an empty `whole`).
8. **Assembly.**
   - Blocks partition the share, and the share is the same set of sites. So every mutant gets exactly one result,
     computed as above.
   - The main thread uses `sampled` only through `.get(id)` [checked: `mutate.ts:3111-3121`], and the report and
     stdout are built from `plan` order and those values [checked: `mutate.ts:3109-3253`].
   - Mutant ids are unique within a block: a claimed mutant survives and a control is fixture-killed, and each mutant
     belongs to one site (`siteOf`).
9. **Caches elsewhere.** The `WeakMap` caches in `mutate.ts` (`lineIdSets`, `readerIndexes`, `neverRefusesMemo`,
   at lines 346, 658 and 1192) are keyed by the data object and computed from it. The order in which they are filled
   cannot change their contents [inferred].

### 2.4 Behaviour that does change

- **Memory.** A worker holds one block's clones (at most `MUTATE_SAMPLE_BLOCK` mutants, or one larger site) plus one
  set's shared baseline work. Before, it held one site's clones plus a second copy of its controls' clones for the
  self-test. With the default of 8, peak memory should be about the same or lower [inferred].
- **`MUTATE_SAMPLE_TIMES` lines** are per block, not per site. The old per-site figures are no longer printed.

### 2.5 Not in the patch: splitting by set ranges (derived here for later)

To split one block's sets across workers (balance without small blocks), a result per (mutant, range) must be merged
in range order:
- Take the first range's `sets`, `reached`, `exercised` and `contradicted`. A later range's values are discarded once
  an earlier range has `contradicted` (the old loop stops counting a mutant at its first contradiction).
- Otherwise add the counts and take that range's `contradicted`.
- `partial` and `closureMiss`: take the first defined, by range order. `partial`-rate sets never touch the counts.

This is sound because a step reads the prior state only through `r.contradicted !== undefined` and
`r.partial !== undefined` [checked: old `mutate.ts:2956`, `2989`]. It is left out to keep tonight's patches small
and auditable.

## 3. Change 2: one work queue for both phases (`mutate-2.patch`, on top of patch 1)

### 3.1 What each hunk does

- **`mutate.ts` imports `TaskWorkers`** from `pool.js` and drops the `Worker` import, whose only uses were the two
  removed spawns [checked: old `mutate.ts:8`, `2682`, `3042`].
- **New `MutateTask` / `MutateResult` types and `mutateTasks()`** (the worker's side).
  - The worker builds `baseline = loadCanonical()`, `cases = judgingCases(baseline)` and
    `muts = selectMutants(mutations(baseline))`, as `mutantShare` did. Its hello is `mutantsDigest(muts)`.
  - It answers `{kind:"mutants", from, to}` with `muts.slice(from, to).map(outcome)`.
  - It answers `{kind:"sampled", block}` with `sampledBlock(…)`, building `sampleSets(baseline, cases)` and `byId`
    on the first sampled task.
- **New `startPool()`.** If `workerCount()` is 1 there is no pool, and the main thread does the work as before.
  Otherwise it creates `TaskWorkers` with `workerCount()` workers and `{year, ny}`, and attaches a no-op `catch` to
  `ready`, so that a load failure is reported where `ready` is awaited rather than as an unhandled rejection.
- **`outcomesOf(…, pool)`.**
  - It awaits `ready` and compares every hello with the main thread's digest (the same error text as before).
  - It maps chunks of `MUTANT_CHUNK = 16` index ranges over the pool, then concatenates the replies, which
    `mapPool` returns in task order, so the outcomes are in mutant order.
  - It checks the length and that no outcome is undefined (the same error text as before).
- **`sampledResults(plan, pool)`** maps `sampledBlocks(plan)` over the pool, then builds the map from the pairs.
  Without a pool it runs `sampledShare(0, 1, plan)` on the main thread, as before.
- **`runMutation()`** now starts the pool, runs the old body (renamed `runMutationOn(pool)`), and closes the pool in
  `finally`. Its signature is unchanged for `main.ts:194` [checked].
- **`mutate-worker.ts`** now:
  - pushes `--year` and `--ny` onto `argv` before importing `mutate.js`, as before;
  - imports `serveTasks` statically (`pool.ts` imports only `node:` modules [checked: `pool.ts:4-6`]);
  - calls `serveTasks(tasks.hello, tasks.run)`.

  This follows `interview-length-worker.ts`.
- **`mutantShare` stays exported but is unused by the run.** The plan's measurement M2 calls it. `sampledShare` stays
  for the single-thread path.

### 3.2 What it saves [inferred, unmeasured]

- **Balance.**
  - Phase 1: 485 small tasks instead of 8 fixed round-robin shares.
  - Sampled check: about 30 blocks taken as workers come free, instead of a fixed `i % count` share of sites with
    uneven cost.
  - The machine has performance and efficiency cores (`docs/2026-11-11_check_all_timing.md:28`), so static shares
    finish at the slowest worker's pace.
- **One load generation, not two.** Sampled-check workers no longer reload `loadCanonical`, `judgingCases` and
  `mutations` [checked: old `mutate.ts:3018-3020`].
- **Overlap.** Worker loading overlaps the main thread's baseline checks and `retargetSelfTest`
  [checked: `mutate.ts:3050-3068`]. The workers idle between the phases while the main thread runs
  `equivalenceReason` and the stale-argument self-test.
- **Not done:** LPT ordering (the blocks run in plan order), and growing the pool when other steps finish (plan R3).

### 3.3 Why it cannot change a verdict or a byte of the report

- **Phase 1.**
  - Each mutant's outcome is `outcome(baseline_w, cases_w, m)` on a worker whose state is built by the same
    functions as before. The digest check guarantees the same mutant list.
  - `outcome` clones before applying and does not write to `baseline` or `cases` [checked: `mutate.ts:2627-2644`].
    So which worker evaluates which mutant, and in what order, cannot matter.
  - The old code already evaluated about 970 mutants in sequence on one worker's state, so reusing that state across
    many mutants is not new. What is new is reuse **across phases**: the sampled check runs on the same `baseline`,
    `cases` and `muts` that phase 1 used. That is sound by the same argument: nothing in phase 1 writes to them.
  - The sampled sets read `cases[*].inputs`. Rate-0 sets share those objects [checked: `mutate.ts:2824`]. Phase-1
    evaluations read the same objects, and `evaluate` does not write inputs; the old phase 1 already depended on that
    across mutants [inferred].
- **The order of outcomes.** `mapPool` returns results in item order [checked: `pool.ts:28-39`]. The chunks are in
  ascending index order and cover `[0, n)` exactly. So `all[i]` is mutant `i`'s outcome, and the counts, the
  survivor list and the class-M list are built from it in mutant order as before.
- **Sampled check.**
  - The blocks partition the plan, and each block's results equal the per-site results by section 2.3.
  - `sampleSets` is deterministic (fixed seeds), as when each old sampled worker built its own.
  - The map is read only by `.get`.
- **The single-thread path** (`MUTATE_WORKERS=1`) is unchanged apart from patch 1.

### 3.4 Behaviour that does change (none of it touches a verdict)

- **Failure handling.**
  - A task that throws is reported only after every queued task has settled: `mapPool` waits for all of them before
    throwing the earliest rejection [checked: `pool.ts:28-39`]. Before, `Promise.all` rejected at the first error.
    So a crashing run fails later.
  - Gap: `TaskWorkers` listens for `error` but not `exit` [checked: `pool.ts:96-110`]. A worker that ended by
    `process.exit` without an `error` event would hang the run, where the old code failed on a non-zero exit.
  - The only `process.exit` on the worker's path is `year.ts:13` for a bad year, which the main thread's year rules
    out [checked: grep]. Out-of-memory in a worker raises `error` [inferred].
  - Suggested follow-up, outside these patches: add an `exit` listener with a non-zero code in `TaskWorkers.run` and
    on `ready`. Other steps share that class.
- **Workers start before the baseline checks.** If the baseline fails its checks or mismatches, the workers are
  started and then closed: a few seconds of wasted load on a run that fails anyway.
- **Pool size in the sampled phase** is `workerCount()`, not `min(workerCount(), plan.length)`. It is the same
  whenever the plan has more sites than workers (76 in xint).
- **Memory.** Workers now live through both phases. A sampled-phase worker holds phase 1's `cases` and `muts` as well
  (the old sampled workers also loaded both) plus the sets. Peak memory is about the same [inferred].

## 4. A/B protocol for tomorrow (quiet machine, after the release-gating check)

The aim is to show that old and new produce byte-identical `mutation.md` and stdout for `mutate` and `mutate --ny` on
the same tree, and to time each phase. No paid calls.

- **Note on the brief.** It names `reports/2025/mutation*.json`, but no such file exists. The mutate step writes only
  `reports/2025/mutation.md`, or `reports/ny/2025/mutation.md` with `--ny` [checked: `ls reports/2025`, `year.ts:48-55`,
  `mutate.ts:3227`]. The protocol diffs those `.md` files and stdout.
- **Machine time** is about three to six hours [inferred]. Today's federal mutate is about 41 minutes under load
  (2,491 s) and the New York one about 11 minutes, so a run of each per build is about 50 minutes. The minimum is two
  builds (old, and patches 1+2); the full protocol is three (adding patch 1 alone, to attribute the saving). Run one
  thing at a time.

**Step 0. A throwaway tree** at the candidate commit, so that xint stays untouched:

```sh
TREE=<the commit holding the xint candidate>   # xint is uncommitted tonight; use the commit it lands as
AB=/tmp/ab-mutate/tree
mkdir -p /tmp/ab-mutate/old /tmp/ab-mutate/p1 /tmp/ab-mutate/new
git -C ~/Documents/GitHub/tax-formalization worktree add --detach "$AB" "$TREE"
ln -s ~/Documents/GitHub/tax-formalization/node_modules "$AB/node_modules"
uptime; tools/check_all_bg.sh --status        # record the load (plan M9); expect no slot held
```

`mutate` reads only `canonical/2025`, the fixtures and `BUG_INVENTORY.md`, and writes `reports/…/mutation.md`
[checked: `mutate.ts:3051-3094`, `3225-3227`]. It needs no `.transcription` data, so `tools/worktree_data.py` is not
needed [inferred].

**Step 1. The phase-marker preload** (stderr only; it changes nothing the run computes). Write it once:

```sh
cat > /tmp/ab-mutate/phases.mjs <<'EOF'
// Marks, on stderr, when each worker starts, each task posted (by kind), each reply (by kind) and each exit.
import { Worker, isMainThread } from "node:worker_threads";
if (isMainThread) {
  const say = (s) => process.stderr.write(`PHASE ${(performance.now() / 1000).toFixed(2)} ${s}\n`);
  const kind = (m) => (typeof m !== "object" || m === null ? "hello"
    : m.result?.kind ?? (Array.isArray(m) ? "sampled" : "outcomes" in m ? "mutants" : "other"));
  const seen = new WeakSet();
  const once = Worker.prototype.once;
  Worker.prototype.once = function (ev, fn) { if (!seen.has(this)) { seen.add(this); say("worker-start"); } return once.call(this, ev, fn); };
  const post = Worker.prototype.postMessage;
  Worker.prototype.postMessage = function (m, ...r) { say(`post ${m === null ? "close" : m?.kind ?? "other"}`); return post.call(this, m, ...r); };
  const emit = Worker.prototype.emit;
  Worker.prototype.emit = function (ev, ...a) {
    if (ev === "message") say(`reply ${kind(a[0])}`); else if (ev === "exit") say("worker-exit");
    return emit.call(this, ev, ...a);
  };
}
EOF
```

- **Untested.** It assumes that `Worker` dispatches `message` and `exit` through `this.emit` [inferred].
- If no `PHASE … reply` lines appear, fall back to the timestamps on the `sampled check:` lines
  (`MUTATE_SAMPLE_TIMES`) and the total from `time -l`.

**Step 2. Build and run OLD.** Use the same fixed worker count for every run, so that the timings compare:

```sh
cd "$AB" && npx tsc -p engine
cd "$AB" && MUTATE_WORKERS=8 MUTATE_SAMPLE_TIMES=1 /usr/bin/time -l node --import /tmp/ab-mutate/phases.mjs \
  engine/dist/main.js mutate --year 2025 2>&1 >/tmp/ab-mutate/old/us.stdout \
  | perl -MTime::HiRes=time -ne '$|=1; printf "%.3f %s", time, $_' >/tmp/ab-mutate/old/us.stderr; \
  echo "exit ${PIPESTATUS[0]}" >/tmp/ab-mutate/old/us.exit
cp "$AB/reports/2025/mutation.md" /tmp/ab-mutate/old/us.mutation.md
cd "$AB" && MUTATE_WORKERS=8 MUTATE_SAMPLE_TIMES=1 /usr/bin/time -l node --import /tmp/ab-mutate/phases.mjs \
  engine/dist/main.js mutate --ny --year 2025 2>&1 >/tmp/ab-mutate/old/ny.stdout \
  | perl -MTime::HiRes=time -ne '$|=1; printf "%.3f %s", time, $_' >/tmp/ab-mutate/old/ny.stderr; \
  echo "exit ${PIPESTATUS[0]}" >/tmp/ab-mutate/old/ny.exit
cp "$AB/reports/ny/2025/mutation.md" /tmp/ab-mutate/old/ny.mutation.md
git -C "$AB" diff --stat -- reports/   # sanity: OLD should reproduce the committed reports if they are current
```

**Step 3 (optional: attributes the saving). Patch 1 alone.**

```sh
cd "$AB" && git checkout -- reports/ && git apply /tmp/nightplan/patches/v2/mutate-1.patch && npx tsc -p engine
```

Then rerun step 2's two commands with `old` replaced by `p1` in every output path.

**Step 4. Patches 1 and 2 (NEW).** Either from step 3's tree, or from a clean one with both patches:

```sh
cd "$AB" && git checkout -- reports/ engine/src/ && git apply /tmp/nightplan/patches/v2/mutate-1.patch \
  && git apply /tmp/nightplan/patches/v2/mutate-2.patch && npx tsc -p engine
```

Then rerun step 2's two commands with `old` replaced by `new` in every output path. The `tsc -p engine` above is the
first compile of the patches. Also run the check-all compile step, `npm run compile --silent` (`package.json:9`,
`tools/check_all_steps.sh:183`).

**Step 5. The equality test** (the acceptance criterion):

```sh
cd /tmp/ab-mutate && for v in p1 new; do [ -d $v ] && [ -s $v/us.stdout ] || continue
  for j in us ny; do
    cmp old/$j.mutation.md $v/$j.mutation.md && cmp old/$j.stdout $v/$j.stdout && cmp old/$j.exit $v/$j.exit \
      && echo "$v $j IDENTICAL" || { echo "$v $j DIFFERS"; diff old/$j.mutation.md $v/$j.mutation.md | head -40; diff old/$j.stdout $v/$j.stdout | head -40; }
  done; done
```

Any difference fails the change: revert it and examine. Before blaming the patch, rule out run-to-run
nondeterminism: rerun OLD once and `cmp` it with the first OLD. The design says OLD is deterministic, since every
sample is seeded, but nothing has tested that.

**Step 6 (optional). The block-size sweep.** Block composition must not change the output, which makes this a
second equality test as well as a timing one:

```sh
cd "$AB" && MUTATE_WORKERS=8 MUTATE_SAMPLE_BLOCK=1 MUTATE_SAMPLE_TIMES=1 /usr/bin/time -l node --import /tmp/ab-mutate/phases.mjs \
  engine/dist/main.js mutate --year 2025 2>&1 >/tmp/ab-mutate/new/us.b1.stdout \
  | perl -MTime::HiRes=time -ne '$|=1; printf "%.3f %s", time, $_' >/tmp/ab-mutate/new/us.b1.stderr
cp "$AB/reports/2025/mutation.md" /tmp/ab-mutate/new/us.b1.mutation.md
```

Repeat with `MUTATE_SAMPLE_BLOCK=32` (`.b32.` in the paths). Then `cmp` each against `old/us.*`, and compare the
`maximum resident set size` lines of `time -l`. Pick the default from the time/RSS trade-off. Also run once with the
default `MUTATE_WORKERS` (unset) to see the production count.

**Step 7. The per-phase times:**

```sh
cat > /tmp/ab-mutate/phases.py <<'EOF'
import re, sys
# usage: phases.py <stderr file>   (lines: "<epoch> PHASE <seconds since start> <event>", and time -l's "real")
ev, real, block_ms = [], None, 0
for line in open(sys.argv[1]):
    m = re.search(r"PHASE ([0-9.]+) (.*)$", line)
    if m: ev.append((float(m.group(1)), m.group(2).strip()))
    m = re.search(r"([0-9.]+) real", line)
    if m: real = float(m.group(1))
    m = re.search(r"sampled check: .*: ([0-9]+) ms$", line)
    if m: block_ms += int(m.group(1))
def first(name, after=-1.0): return next((t for t, e in ev if e == name and t > after), None)
def last(name): return max((t for t, e in ev if e == name), default=None)
new = any(e.startswith("post mutants") for _, e in ev)
p1_start = first("post mutants") if new else first("worker-start")
p1_end = last("reply mutants")
s_start = first("post sampled") if new else first("worker-start", after=p1_end or 0)
s_end = last("reply sampled")
fmt = lambda a, b: "?" if a is None or b is None else f"{b - a:8.1f} s"
print("setup (to first phase-1 work)  ", fmt(0.0, p1_start))
print("phase 1 (judge the mutants)    ", fmt(p1_start, p1_end))
print("main thread between the phases ", fmt(p1_end, s_start))
print("sampled check                  ", fmt(s_start, s_end))
print("tail (self-tests, report)      ", fmt(s_end, real))
print("total (time -l real)           ", "?" if real is None else f"{real:8.1f} s")
print("sum of sampled-check block/site times (CPU-ish)", f"{block_ms / 1000:.1f} s")
EOF
for v in old p1 new; do for j in us ny; do f=/tmp/ab-mutate/$v/$j.stderr; [ -f $f ] && { echo "== $v $j"; ~/.pyenv/versions/3.13.6/bin/python3 /tmp/ab-mutate/phases.py $f; grep -E "maximum resident|real" $f; }; done; done
```

- For OLD, "setup" ends when the first phase-1 worker is constructed, and the sampled check starts when the second
  generation is constructed. The second generation's load time is therefore counted in the sampled check, which is
  part of what patch 2 removes.
- For NEW, workers start at about t=0. "Setup" ends at the first task posted, and worker loading overlaps it.

**Step 8. Clean up:**

```sh
git -C ~/Documents/GitHub/tax-formalization worktree remove --force /tmp/ab-mutate/tree
```

Keep `/tmp/ab-mutate/{old,p1,new}` until the numbers are written up.

## 5. Landing: what each patch makes due

- **No fixture, coverage-row, interview or help changes,** so none of the interview protocol's checks apply. No
  pending bug entry.
- **Tier.** `engine/src/mutate.ts` and `engine/src/mutate-worker.ts` are full-tier paths
  [checked: `tools/full_paths.txt:7`, `engine/src/mutate*.ts`]. Landing needs
  the full-tier `check_all` at commit (the release-gating rules), with `mutate` and `ny_mutate` green.
- **The section 4 A/B equality (step 5) is the acceptance test.** A green full run alone does not prove the output
  unchanged.
- **No paid review calls are due:** this is engine tooling, not form content.
- **Commit-message material:** the section 2.3 and 3.3 arguments, plus the A/B result with the load average
  (`uptime`) recorded.
