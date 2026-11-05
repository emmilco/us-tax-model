# Release-gated check-all: design for the owner (T-238)

Status: approved by the owner on 2026-11-05, with the three recommendations below: fast commits on `main`; release at every session end plus the path triggers; the docs tier included.

## The problem, measured

A commit needs a green full check-all on its exact tree. The run on 2026-11-05 (tree `b2d7356c`) took
about 38 minutes of wall time. Per-step times are in `.git/worktrees/check-all-worktree/check-all-times`:

| Wave | Slowest steps (seconds) | Wave wall time |
|---|---|---|
| compile | compile 1 | ~1 s |
| build | build and render 153 | ~2.5 min |
| 1: sources, logs, data | review_tools 92, check_logs 87, check_extraction 58, compare_families 57 | ~1.5 min |
| 2: evaluators | **mutate 1,733**, engine_differential 539, compare (Lean) 424, test_fixtures 320, test_integration 138, human_review 109 | **~29 min** |
| 3: evidence, NY | ny_compare 136, ny_mutate 69, evidence 3 | ~2.3 min |

Five steps make up the cost: `mutate`, `engine_differential`, `compare`, `ny_compare` and `ny_mutate`.
Without them the suite is about 9.5 minutes: wave 2 is then bounded by `test_fixtures`. They write only
under `reports/`. One later step reads one of their outputs: `evidence` takes its E column (engine
assertions) from the committed `reports/<year>/engine_differential.json`. In a fast run that file is
the one from the last full run (see "What `main` guarantees between releases").

The effect is that work is held back and batched into large commits. On 2026-11-05 `main` went 6.5 hours
without a push while finished work waited for a run, and each bookkeeping edit either waits for the next
run or costs its own 38 minutes.

## What is guaranteed today

- `tools/hooks/pre-commit`: the staged tree is a tree a green full run tested (`tools/green.sh`: the
  worktree marker, or the last 50 green trees of the clone).
- `tools/hooks/pre-push`: every commit in the pushed range, not only the tip, has such a tree.
- README ("The commit guard"): "refuses any commit whose tree is not exactly the tree the last green run
  of the full suite tested". This claim is public, because the repository is public.

So today every commit on `origin/main` passed the full suite.

## Proposal

### Three tiers of check, chosen by what the commit changes

| Tier | Runs | Time | Accepted for |
|---|---|---|---|
| **docs** | `check_bug_inventory`, `coverage_tree --check`, `green_self_test` | seconds | a commit whose changes all lie in an allowlist of bookkeeping paths: `TASKS.md`, `TASKS-DONE.md`, `BUG_INVENTORY.md`, `HANDOFF-NEXT-SESSION.md`, `handoffs/`, `docs/`, `research/costs/`, `research/audits/`, `PROJECT_INDEX.md` |
| **fast** | every step except the five slow ones | ~9.5 min | any commit on `main` |
| **full** | today's check-all, unchanged | ~38 min | a release |

The docs tier is decided by the diff against the parent commit, not by the agent's judgment. A single
path outside the allowlist makes the commit need the fast tier. The allowlist lives in one file, and its
self-test checks that no path a build step reads is on it.

### What a release is

- A release is an annotated tag `r<year>.<month>.<day>.<n>` (for example `r2026.11.05.1`) on a commit of
  `main` whose tree passed a green **full** run.
- `tools/release.sh` starts a background full run on the clean tip, and when it is green, it tags the tip
  and pushes the tag. If the run is red, nothing is tagged. The failing step's log names what broke, and
  the fix is the next ordinary commit.
- `pre-push` refuses any `r*` tag whose tree is not in the full-green record.
- The README states the latest release and the fact that only releases carry the full guarantee.

### What `main` guarantees between releases

- Every commit's tree passed at least the fast tier, or the docs tier for bookkeeping-only commits. The
  hooks enforce this exactly as today: same tree identity, same range check on push, two records instead
  of one.
- The fast tier does **not** cover the following, which are checked only at a release:
  - **mutation adequacy:** whether the fixtures still kill every mutant;
  - **agreement with the independent evaluators:** `engine_differential`, and the Lean `compare` for
    both federal and New York;
  - **New York mutation.**
- `reports/<year>/mutation.md`, `evaluator_agreement.md` and `engine_differential.{md,json}` on an
  unreleased commit can be older than its tree. So can the E column of `evidence.md`, which is built from
  that JSON: a line changed since the release can show an engine assertion made on its old encoding. A
  fast run therefore stamps `evidence.md` with "engine evidence as of release r…". Release refreshes
  all of these.

### When to release

My recommendation:
- **at the end of every working session**, before the handoff;
- **before** any change to `engine/src/mutate.ts`, the mutation equivalence lists, the evaluators, or
  `tools/engines/` is built on further. A commit touching those paths needs the full tier at commit
  time: the fast tier skips exactly the steps they affect;
- **before** a paid review round or the T-236 web UI is used on the tree.

At about one release per session, the cost falls from one 38-minute run per commit to one per session,
plus about 10 minutes per code commit.

### What happens when a release run fails

The defect lies somewhere in the commits since the last release. Those commits are on `origin/main`
and passed the fast tier. The window is one session's commits; `git bisect` with the failing step alone
finds the commit. The fix is a new commit, never a rewrite of pushed history.

## Alternatives considered

1. **Work on a `dev` branch, with `main` fast-forwarded only at releases.** `main` would keep today's
   every-commit-full guarantee in its first-parent history, and `dev` would be pushed often. This is
   rejected as the default. Fast-forwarding puts the fast-only commits into `main`'s history anyway, and
   a merge commit per release adds ceremony across a two-branch workflow, so the guarantee becomes
   "first-parent only". It remains a good choice if keeping the every-commit-full claim on `main`
   matters more than simplicity.
2. **Step reuse (the original Package B, process plan item 5).** A step whose inputs are unchanged reuses
   its last result. It saves most on bookkeeping commits, which the docs tier already covers more simply,
   and little on code commits, because almost every code change is an input to `mutate`. It carries the
   most risk: a wrong input declaration silently skips a step. Deferred; per-form mutation caching is the
   version of it worth doing later.
3. **Full run on pre-push instead of pre-commit.** This was the plan's open question 2. It keeps the
   guarantee on `origin` but still costs 38 minutes per push, and the push gap seen on 2026-11-05 was a
   push gap.

## What changes (once approved)

- `tools/check_all_steps.sh`: a `--tier fast|docs` option that skips steps. The full run is the default
  and unchanged.
- `tools/check_all.sh`, `tools/check_all_bg.sh`, `tools/green.sh`: record the tier with the tree (a
  full-green list and a fast-green list, as today, with the same lock). A full-green tree is also
  fast-green.
- `tools/hooks/pre-commit` and `pre-push`: accept fast-green trees on branches, and only full-green trees
  for `r*` tags. Docs-tier acceptance is checked from the diff.
- New: `tools/release.sh`, and a `tools/docs_paths.txt` allowlist with its self-test.
- Tests: `test_green.sh` and `test_pre_push.sh` cover each tier, the tag rule, and an allowlisted commit
  that strays outside the allowlist.
- Documentation: the README's commit-guard paragraph, `PROJECT_INDEX.md`, and the commit recipe in the
  handoff. Any `CLAUDE.md` text goes to the owner first (T-241).
- Cost: one Opus agent, about half a day, with no paid review calls. It lands behind one full run, and
  its own first release follows.

## Owner decisions (2026-11-05)

1. Fast commits land on `main`. The full guarantee belongs to release tags, and the README is reworded to say so.
2. Release cadence: at every session end, plus the path triggers in "When to release".
3. The docs tier is included.
