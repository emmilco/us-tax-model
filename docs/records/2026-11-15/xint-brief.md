# Expansion integrator (XINT): merge the coverage-expansion lanes onto the final goal-1 merge

Model: claude-opus-5-5. Class: judgment. Year: 2025. Jurisdiction: us.

Worktree: `/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/xint` = `refs/scratch/b1-final`
(the 18 goal-1 lanes merged; its record `docs/provisional/lanes/b1-integration.md`). Review data cloned. Never cd
elsewhere; do not commit; do not run `tools/check_all.sh`; no paid reviews or model calls from code. Read project
`CLAUDE.md` and the B1 integration log first: its merge method and tools are in `/tmp/b1/` (`tools/verify_merge.py`
checks a shared file by id three-way and into case inputs; `tools/merge_keyed_json.py` merges consumers.json by key;
`check.sh`/`quick.sh` run per-lane checks). Use them.

## Lanes to merge (each is an uncommitted worktree diff against base `825024d8` = refs/scratch/x1-base)
Get each lane's diff with `git -C <wt> add -A -N . && git -C <wt> diff --binary 825024d8 -- . ':!rendered' ':!canonical' ':!reports'`
and EXCLUDE `fixtures/2025/defaults.json` (every lane's copy is a broken-base workaround): instead run each lane's
defaults patch script on the integrated defaults.json (`/tmp/x1d/defaults_patch.py`, `/tmp/x1-f1116/defaults_patch.py`,
`/tmp/x2-k1p/defaults_patch.py` or the lane's `docs/provisional/lanes/*_work/scripts/defaults_patch.py`,
`/tmp/x2-k1s/defaults_patch.py`, `/tmp/mfs-l4/defaults_patch.py`, and later `/tmp/mfs-l1..l3`, `/tmp/x1sche`,
`/tmp/x2-k1e`, `/tmp/mfs-x2-s1o`, `/tmp/mfs-x2-paynow2`, x2-dep's — find each in its lane note).
Note x1-base was a mid-merge snapshot of B1: a lane's diff against it may include nothing of B1, but B1 changed
many of the same shared files since; merge by id, never by blind text. x1-base already contained 12 of B1's 18
lanes; the other 6 (F5, F6, F7b, F9, F11, T3) changed s2, s3, household, sb, sales, sd, ftc, gift, sc, mutation pins.

Ready now (merge in this order): x1-digital, x1-f1116 (its second pass x1-f1116b is still running until ~17:00 in
the same worktree: merge the first pass now, and its delta later), x2-k1p, x2-k1s, mfs-l4.
Coming by ~17:30 (merge each as the coordinator sends it): x1-sche, mfs-l1, mfs-l2, mfs-l3, x2-s1o, x2-paynow2,
x2-dep, x2-k1e. Each lane's note `docs/provisional/lanes/<lane>.md` in its worktree lists merge cautions, shared
lines it changed, its defaults script, and its round-2 review list. Read it before merging the lane.
Also apply the archived sources: `git -C .claude/worktrees/nx-src diff --binary HEAD -- tools/sources sources`
(merge catalog/manifest entries by key; B1 already has F6/F11 catalog entries 289–292).

## Known cross-lane cautions
- `s1.line9`'s sum: x1-digital adds 8v; x2-s1o adds 8z/8e/8u/8k operands; x2-paynow2 adds 8s. Combine.
- `questions.yaml` order 264: x2-k1p and x2-k1s both use it (k1s seq 20–83). mfs-l4 renumbers order 120 seq 17–36 to
  20–39. Check every (order, seq) is unique after merging.
- `person.yaml`: k1p (29 totals), k1s (block `# --- x2-k1s ---`), MFS L2, B1's F8/F9 lines.
- Personas: 14 (f1116), 17/18 (digital).
- `ftc.elect` retired by x1-f1116 (470 fixture facts deleted): re-apply that deletion to any case that B1 added.
- Schedule E filers must refuse on the Form 1116 path until x1-sche's s1.line5 is wired (x1-f1116 note).
- `tools/coverage/tree.json` / `categories.json`: merge topics; k1p added topic `k1_partnership`, k1s put its gates
  under `other_income`; make one K-1 topic.
- K-1 forms stay unreached (scope.k1 still refuses) unless a wiring lane runs; do NOT wire them in this lane.
- Every class M / mutation case must state each newly-asked-of-everyone input (f1040.digital_assets etc.).

## After each merge
Build, render, render --ny; `test-fixtures` and `--ny` must pass fully (the base is no longer broken: any failure is
real — fix it at its cause or report it); citations --strict; check_consumers; tick-groups; check_questions /
check_screens / check_false_no; year_changes --check; interview-rules; interview-coverage --rows on the merged
lane's row files. Keep a log `docs/provisional/lanes/xint.md` (per lane: what merged, conflicts and how resolved,
check results). At the end: new_bug.py --assign, mutate (+ --ny), and the full round-2 review list (per form:
transcription / render / class M, whole or line-scoped, and which are brand-new forms).

Report to the coordinator after the five ready lanes are merged and checked (target 17:30), then again at the end.
