# Lane v2-tooling: five tooling patches (claude-opus-5-5, judgment, 2025, us)

Patches are drafted from copies of xint's files, under /tmp/nightplan/scratch/v2-tooling-<n>/{a,b}. Nothing in the
repository was edited. No build, test, check_all or engine run was made, and no model was called.
- **Checked** means one of: read at path:line; `git apply --check` against xint; `bash -n`; a Python `ast.parse`; or
  a read-only Python script.
- **Inferred** means none of those.

## Summary

| Patch | What | Files | Apply check | Tier | Land |
|---|---|---|---|---|---|
| tooling-1 | pre-commit and pre-push refuse a new blob over 50 MiB; `tools/large_blobs.txt` lists exceptions | tools/blob_limit.sh (new), tools/large_blobs.txt (new), hooks/pre-commit, hooks/pre-push, hooks/test_green.sh, hooks/test_pre_push.sh, tools/README.md | applies alone (checked) | fast | **after** tonight's xint push: it would refuse xint's new 74.9 MB f8889 record |
| tooling-2 | `coverage` fails on a fixture input stated with a non-default value under a closed gate, unless the case lists it in `closed_gate` | engine/src/fixtures.ts, engine/src/fixture-inputs.ts, 5 fixture files (27 acknowledgements) | applies alone (checked) | fast | after one `coverage` run settles the flagged list (below) |
| tooling-3 | in a release or verify run, a missing outside engine fails the engine differential instead of being skipped | tools/engines/run_engines.py, tools/engines/run.sh, tools/engines/README.md | applies alone (checked) | **full** (tools/engines/* is in tools/full_paths.txt, checked) | any time after tonight; the next engine run is cold |
| tooling-4 | release-list entries expire after 24 hours, by time | tools/green.sh, tools/release.sh, hooks/test_green.sh, tools/README.md | applies alone, and after 1 and 5 (checked) | fast | **after** tonight's release: entries without a time are refused, so a run recorded tonight would be rerun |
| tooling-5 | test of the release.sh skip path: positive and negative | hooks/test_pre_push.sh | applies alone, and after 1 (checked) | fast | any time |

**Combined application (checked).** Patches 1, 5 and 4 apply in that order to scratch copies of xint's files with
`git apply`. Patches 2 and 3 touch no file another patch touches.

**Two judgments the owner should see:**
1. **Patch 2: fail, with a per-case acknowledgement, rather than warn.** A static read of the 2025 fixtures found 29
   stated inputs under a closed gate. 27 are deliberate gate-isolation tests whose notes say the answer "is not read".
   Two notes do not say so (see 2.4). A plain fail would block good tests. A plain warning would print 27 known lines
   on every run, and nobody would read them.
2. **Patch 4: limit by time (24 h), not by count.** The reasons are in 4.1.

---

## tooling-1: blob size guard

### 1.1 What each hunk does
- **tools/blob_limit.sh (new).** `MAX_BLOB_BYTES=52428800` (50 MiB). Two functions:
  - `oversized_blobs` reads `<object id> <path>` lines and runs one `git cat-file --batch-check` over them. awk keeps
    blobs over the limit, and blobs listed in `tools/large_blobs.txt` (by blob id) are dropped.
  - `report_oversized WHO` prints one refusal line per blob and returns 1 if there was any. The line gives the blob
    id, the path, the size in MiB, and the exact line to add to `tools/large_blobs.txt`.
- **tools/large_blobs.txt (new).** A header comment and no entries. Format: `<blob id> <path> <reason>`.
- **hooks/pre-push.** Sources blob_limit.sh. For each ref it sets `added` to the same range the commit loop uses:
  - an update reads `local_sha ^remote_sha`;
  - a new ref reads `local_sha --not --remotes`.

  It then runs `git rev-list --objects "${added[@]}" | oversized_blobs | report_oversized`, which sets `failed=1`.
  **Only objects the push adds are read, so the 74.9 MB record already on main (43fe6dd0, store/f8889) is never
  refused again.** That record is on origin/main, so it is reachable from the remote side.
- **hooks/pre-commit.** Sources blob_limit.sh. It checks the blobs the commit adds or changes against HEAD
  (`git diff-index --cached --no-renames --diff-filter=AM`), or against the empty tree for a first commit. It runs
  before the claims and green checks.
  - Why pre-commit as well: a blob once committed leaves history only by rewriting it (today's 107 MB rejection).
    Refusing at commit is cheaper than refusing at push.
  - pre-push stays the backstop for merges (git runs no pre-commit on a merge) and for `--no-verify` commits.
- **test_green.sh.** Copies and sources blob_limit.sh. New block at the end:
  - a 50 MiB + 1 byte file of zeros on a full-green tree is refused;
  - once listed in tools/large_blobs.txt, it is accepted.
- **test_pre_push.sh.** Copies and sources blob_limit.sh. New block after the release-tag tests. Commit H adds a big
  blob:
  - the push M..H is refused;
  - with H's blob listed, the push is accepted;
  - with origin/main moved to H, the push H..I and the new ref I (`--not --remotes`) are accepted, so a blob already
    on the remote is not read.
- **tools/README.md.** One paragraph in the hooks section.

### 1.2 How to handle the existing large blobs (checked sizes from the plan-tooling lane, tooling.md C.3)
- **Already pushed** (43fe6dd0 at 74.9 MB, 4136f37d at 57.0 MB, and the eic and household records under 50 MB): no
  action. Neither hook reads them again.
- **xint's uncommitted new f8889 record e3b28879 (74.9 MB):** the new hooks would refuse it at commit and at push.
  Options:
  - (a) **Recommended:** land tooling-1 after tonight's xint commit and push.
  - (b) Before landing, add its blob id to tools/large_blobs.txt with the reason "f8889 transcription record; shrinks
    when the store writes shared subtrees once (tooling.md C.4)". The commit-time refusal prints the exact line.
- **Each later f8889 transcription pass** writes another ~75 MB record. Until the shared-subtree fix lands, each one
  needs an entry in tools/large_blobs.txt. Every entry is visible in a diff, and each is a debt.

### 1.3 Risks
- `rev-list --objects A ^B` can list a blob that is in old history but not in B's boundary trees, for example a large
  file brought back by a revert. That gives a false refusal, which the list can clear. *Inferred* from how rev-list
  marks objects.
- Paths with tabs or newlines print quoted or wrong in the message. The size test uses the blob id only, so this is
  cosmetic.
- The new tests write a 50 MiB file into the temporary repository (zeros, about 50 KB compressed in .git). Each self
-test run takes about 1 s more. *Inferred.*
- `git hash-object -t tree /dev/null` gives the empty tree's id without writing it. git treats the empty tree as
  always present. *Inferred*, not run.
- The 50 MiB limit is GitHub's warning level. GitHub refuses at 100 MiB. A lower or higher limit is a one-line change.

### 1.4 Verify (not run)
- `bash tools/hooks/test_green.sh`
- `bash tools/hooks/test_pre_push.sh`
- Then commit something small in a scratch worktree with the hooks enabled.

Tier: **fast**. tools/hooks/*, tools/*.sh and tools/large_blobs.txt are not in full_paths.txt or docs_paths.txt
(checked). Reviews made due: none (no form content).

---

## tooling-2: fixture inputs under a closed gate

### 2.1 Where, and fail rather than warn
- **Not in `validateInputs`** (eval.ts:843). It also runs in `evaluate` (eval.ts:87) and the interview
  (interview.ts:510, 537), where values on unselected branches are legitimate. Its own doc comment says "including
  values on currently unselected branches" (checked).
- **In `coverageReport` (fixtures.ts).** That function already evaluates every case in-process with `allTargets` and
  reads `takenGuardIndex` from the derivations (checked). The check therefore adds no evaluation. It runs in the
  `coverage` step (check_all_steps.sh:268, every tier that runs it; checked).
- **Fail, with an acknowledgement.** A new optional case field `closed_gate: [input keys]`. The step fails on either:
  - an unlisted input stated with a non-default value under a closed gate;
  - a listed key that is not such an input (a stale acknowledgement).

  Reasons:
  - A gate-isolation test is valuable. A case with the gate closed and the gated input at zero cannot tell a broken
    gate from a working one. So known-good hits must be allowed, and listing them documents the intent.
  - A warning would list 27 known lines on every run.
  - A stale acknowledgement is caught, so the list cannot rot.

### 2.2 What each hunk does
- **fixtures.ts**
  - `FixtureCase.closed_gate?`.
  - `gateInputs(data)`: gate line → {doc, gated input, indexes of the alternatives that take the input}.
  - `closedGateInputs(gates, stated, table, derivations)`: for each `choose` derivation of a gate line that took
    another alternative, it rebuilds the gated input's key from the gate's key. The gate and its input share one
    document, so they share the entry prefix. It then reports the input if the case states it, not null, with a value
    other than its default.
  - In `coverageReport`: the stated inputs come from `checkedCases()` with `resolveParams` (federal, or NY under
    `--ny`), and only for files that take defaults. After the report, the problems print and set
    `process.exitCode = 1`. It also prints a count of acknowledged inputs.
- **fixture-inputs.ts.** `StatedCase.closed_gate?` and its doc comment.
- **fixtures/2025/{f1040,f8889,rec,s1,s3}.json.** `closed_gate` is added before `inputs` in 15 cases, 27 keys in all.
  The files round-trip byte-identically through `json.dumps(indent=2, ensure_ascii=False)` (checked), so only the new
  lines change.

### 2.3 Predicted first run (static, read-only script /tmp/nightplan/scratch/v2-tooling/dead_gated2.py)
- The script follows gate conditions through inputs, parameters and chained `choose` lines with `eq` guards. It reads
  2707 stated non-default gated inputs and finds **29 under a closed gate**. 1337 have computed conditions it cannot
  decide.
- So the real run **may flag more than these**. That count is unknown until run.
- Acknowledged in the patch (the case's note says the answer is not asked or not read):
  - stage11.educator.not_eligible
  - stage13.educator_one_eligible
  - four f8889 `*_not_asked` / `*_unread` cases
  - rec.not_itemized
  - s1.line8v.not_asked
  - eight redesign.credits cases

### 2.4 Left unacknowledged on purpose: candidate fixture findings for the owner
The first run should fail on these two:
1. **`s1.line8v.none`** (fixtures/2025/s1.json) states `s1.digital_amount: 123456` with `s1.digital_income: false`.
   The note ("A Yes to the digital asset question with no digital asset income … line 8v is zero") does not say the
   amount is there to show the gate discards it. Either acknowledge it and add that to the note, or drop the amount.
2. **`redesign.credits.prior_not_asked`** (s3.json) states `ftc.carryover: true` and `s3.foreign_any: false`. The
   note speaks of "the two questions beneath" (prior_amt, prior_forms) only. The carryover Yes looks copied from
   foreign_not_asked. Either drop it or mention it in the note.

### 2.5 Risks
- **Not compiled.** The TypeScript is not type-checked (no builds were allowed).
  - Imports: `CanonicalData`, `Expr` and `Derivation` are types those modules export (checked). Patch 2 also imports
    `checkedCases`, `defaultTable`, `resolveParams`, `takesDefaults` and the `DefaultTable` type from
    fixture-inputs.ts (checked exported). It writes `type DefaultTable` inline in a value import, a form the file
    has not used before. *Inferred* to compile.
- **Instance keys.** The derivation key of a collection line is the instance key (e.g. `person[taxpayer].x`).
  *Inferred* from coverageReport's use of templateKey (fixtures.ts:395) and branches.ts:7-10; not observed.
- **More cases than predicted** (2.3): the patch then lands together with the resolutions from the first run.
- **Year carry.** tools/fixtures_year.py copies whole cases into the next year. If an input is renamed there,
  `closed_gate` keeps the old key and the next year's coverage run reports a stale acknowledgement. That failure is
  visible, not silent. *Inferred.*
- **NY.** NY fixtures are checked only if `coverage --ny` is run. check_all runs `coverage` federal only (checked,
  check_all_steps.sh:268).

### 2.6 Verify (not run)
1. Build.
2. `node engine/dist/main.js coverage` (2025). Expect: "coverage: 27 stated inputs under a closed gate, each listed …",
   then a failure on the two cases in 2.4, plus any the static read could not decide.
3. Resolve each, then rerun.
4. Also run `test-fixtures`, `draft-walk` and `interview-coverage` to confirm the new key is ignored there.
   *Inferred*: no reader of fixture cases rejects unknown keys. grep found no key allowlist for fixture cases in
   engine/src or tools.

Tier: **fast** (engine/src/fixtures.ts and fixtures/2025/*.json are not full-tier paths). Reviews: none made due
(*inferred*: fixtures are not the form content that review subjects hash).

---

## tooling-3: release or verify runs fail on a missing engine

### 3.1 What each hunk does
- **run_engines.py**
  - Imports `os`.
  - New `must_compare_all()`: true when `CHECK_ALL_RELEASE == "1"` **or** `ENGINE_CACHE == "verify"`.
  - At the start of `main()`, before any engine runs (so it fails in seconds, not after PolicyEngine): if OpenTaxSolver
    or UsTaxes is not `available(YEAR)`, it exits non-zero naming them.
  - The module docstring is updated.
- **run.sh.** When the venv is missing, the same condition gives exit 1 with a message instead of `SKIPPED`
  (run.sh:17-19 skipped the whole step: the same hole one level up). Header comment updated.
- **engines/README.md.** One sentence in the ENGINE_CACHE paragraph.

### 3.2 Choices
- **"Or", not "and".** green.sh's `release_mode` needs both variables (green.sh:91). Either one alone also promises a
  full comparison: verify "reruns every engine" (engine_cache.py:19-24). So either one now refuses a skip. A release
  run sets both, so it is covered either way.
- **Available for the year, not merely installed.** The plan-tooling sketch tested installation only, so that an
  unsupported year would not fail. I chose the stricter test: a release run on the default year that silently lacks an
  engine's forms is exactly the hole.
  - **Consequence (owner decision):** when the default year flips to 2026, releases fail until OpenTaxSolver 2026 is
    built and UsTaxes has Y2026 forms. xint's clone has Y2020 to Y2025 only, and its OTS package is 2025 (checked
    with `ls`).
  - If that is unwanted, change `available(YEAR)` to installation tests: `ots_adapter.package_dir() is not None` and
    `ustaxes_adapter.USTAXES_SRC.is_dir()`.

### 3.3 Risks
- **Cold cache.** The engine cache key hashes every file under tools/engines/ except NOT_READ (engine_cache.py:9-11),
  so this patch makes the next engine-differential run cold. T-273's measures: about 527 s against 228 s warm
  (TASKS-DONE.md:256).
- **`ENGINE_CACHE=verify` with `--year 2026`** now fails where it skipped before. No script sets that combination
  (grep, checked), but a person might.
- The UsTaxes self-test (run.sh:24) still prints SKIPPED before run_engines fails. The step still fails.

### 3.4 Verify (not run)
- With `.engines/ustaxes-src` temporarily moved aside in a scratch clone:
  - `ENGINE_CACHE=verify tools/engines/run.sh` must exit 1 naming UsTaxes;
  - without the variable, it must print SKIPPED and pass.
- Then one normal full run.

Tier: **full**. tools/engines/* is in tools/full_paths.txt (checked).

---

## tooling-4: age limit on release-list entries

### 4.1 Recommendation: by time, 24 hours
- **Why time.** The tree is content-addressed and cannot change. What makes a release-mode result stale is outside the
  tree:
  - the installed engines (.engines);
  - the ignored review data (.transcription and the others);
  - node_modules.

  Those drift with wall-clock time and with reinstall events, not with how many trees the clone records.
- **Why not a count.** A count of later entries measures activity in the clone. A quiet weekend would keep an entry
  valid for days, and a busy night would expire it in an hour. Only release-mode runs write the release list, so a
  count of release entries would barely move. A count over the full list would tie releases to unrelated lane work.
- **Why 24 h.** The skip path exists so that tonight-style sequences (release-mode run, then landing on main, then
  release.sh) take minutes to hours. 24 h covers an overnight gap.
- **A sharper alternative, not drafted.** Expire an entry when the engine identities change: compare the identities
  stored in the engine cache records with the current ones. That tracks the real cause, but it is a larger change.
  Owner decision whether it is worth it.

### 4.2 What each hunk does
- **green.sh**
  - `RELEASE_MAX_AGE=86400`.
  - `record_green TREE release` writes `TREE SECONDS`. Other tiers are unchanged.
  - `is_release_green` now uses awk: `NF == 2 && $1 == tree && $2 >= now - RELEASE_MAX_AGE`. An entry without a time
    (the current format) is refused, so the change fails safe.
  - Header comment updated.
- **release.sh**
  - When the tree is listed but too old, it says so before running the suite.
  - Header lines 20-22 now say "in the snapshot worktree of tools/check_all_bg.sh, at most RELEASE_MAX_AGE seconds
    ago".
  - The old text said "in any worktree of the clone", which contradicts check_all.sh:64-66. Those lines record release
    only in the bg snapshot worktree (checked).
- **tools/README.md:193-196** said "`tools/check_all.sh --tier full`, in any worktree". It now names
  `check_all_bg.sh --wait` and the snapshot, and states the 24 h limit. The same contradiction is corrected.
- **test_green.sh** adds three assertions:
  - an entry 24 h + 60 s old is refused;
  - an entry without a time is refused;
  - the recent entry is still accepted beside them.

  The awk expression was sanity-checked on a 3-line temporary file (rel1 accepted; rel2 old, rel3 bare and rel4
  absent refused).

### 4.3 Risks
- **Land after tonight's release.** A bare entry recorded tonight would no longer skip, and release.sh would rerun the
  60-minute suite. That fails safe, but it costs the hour.
- `in_record release` still exists, reached through `marker_of` and `trees_of`, and would now never match. Nothing
  calls it (grep: only `is_release_green` did). Cosmetic.
- The clock: `date +%s` on one machine. No cross-machine use.

### 4.4 Verify (not run)
- `bash tools/hooks/test_green.sh`
- `bash tools/hooks/test_pre_push.sh` (patch 5's test records release and tags at once)

Tier: **fast**.

---

## tooling-5: test of the release.sh skip path

### 5.1 Where
The brief named test_green.sh, but **release.sh is exercised only in test_pre_push.sh**:
- test_pre_push.sh copies release.sh and stubs check_all_bg.sh and release_reviews.sh at lines 22 and 109-135;
- test_green.sh copies neither.

So the test is placed after test_pre_push.sh's last release test (line 160). The audit's three-line sketch was
extended with the negative case.

### 5.2 The test
1. Commit `j` with `--no-verify`, because the hooks are active by then.
2. Record its tree in the release list only. `STUB=red tools/release.sh` must fail and make no tag r$day.3: a
   release-listed tree that is not full-green is run again.
3. `rec full HEAD`. `STUB=red tools/release.sh` must succeed: the red stub is never reached, so the suite did not run.
4. The tag r$day.3 must be on HEAD.
5. pre-push must accept that tag, which shows release.sh wrote release-ready on the skip path.

The existing `STUB=red` test (line 141) still covers "a full-green tree not release-listed runs the suite".

### 5.3 Risks
- None known. It does not depend on patch 4. With patch 4, `record_green … release` writes the time and the entry is
  fresh.
- With patch 1, origin/main is I. The tag's new-ref range (`--not --remotes`) excludes the big blob, and every commit
  since is recorded green. *Inferred* by reading the test sequence; not run.

### 5.4 Verify (not run)
`bash tools/hooks/test_pre_push.sh`. Tier: **fast**.

---

## Files
- Patches: /tmp/nightplan/patches/v2/tooling-1.patch … tooling-5.patch
- Scratch copies: /tmp/nightplan/scratch/v2-tooling-{1..5}/{a,b}; combined application: /tmp/nightplan/scratch/v2-tooling-combo
- Patch builder: /tmp/nightplan/scratch/v2-tooling-mkpatch.sh
- Static fixture scan: /tmp/nightplan/scratch/v2-tooling/dead_gated2.py (`python3 -I dead_gated2.py <repo>`)
