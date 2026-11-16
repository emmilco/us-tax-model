# Lane plan-tooling (claude-opus-5-5, judgment, 2025, us)

Read-only lane. Nothing in the repository was edited; no builds, checks or model calls were run.
"Checked" means read in the file at path:line, or measured by a read-only command. "Inferred" means not checked directly.

## Summary

**A. Release-tooling audit. No blocker found.** Under the conditions below, the new skip path cannot tag a tree that
lacks a green full release-mode run. The release list is written in one place only, check_all.sh:64-67. That code
runs after the full-tier record and after the outside-change and default-year guards. It requires `tier=full` and both
variables set exactly. release.sh takes the skip path only if HEAD's committed tree is in both the release list and the
full list (release.sh:51). `release_reviews.sh` is still reached on the skip path, because it runs at release.sh:44,
before the branch at :51. pre-push still requires full-green plus release-ready, and release.sh writes release-ready on
both paths (:86).

The new path is weaker than the old one in one way: the old release always ran in the exclusive background snapshot
worktree, while the new path accepts a direct run in any worktree. The findings, ranked:

1. **MEDIUM-HIGH: a direct run in a shared worktree can record report files that the run did not produce.**
   check_all.sh ignores changes under reports/ and rendered/ made during the run (:51). Nothing stops two
   check_all.sh runs in the same worktree; slots are counted per machine, not per worktree. For example, a concurrent
   fast run rewrites evidence with its fast-run note while the release-mode run is in progress, or an agent writes
   into reports/. The release-mode record then covers those files. Before this change this could not happen to a
   release, because a release always ran in `.git/check-all-worktree` under the per-clone lock.
   **Tonight's mitigation:** run the xint release-mode check with nothing else running in or writing to xint, or run
   it through `tools/check_all_bg.sh --wait`, which uses the isolated snapshot. A fix diff is in A.3.
2. **MEDIUM: a direct run can drop outside engines without failing.** run_engines.py:628-634 prints `SKIPPED` and
   continues when OpenTaxSolver or UsTaxes is not installed in the worktree. The run is still green and is still
   recorded as release. The background path borrows the primary worktree's .engines (check_all_bg.sh:52, 109-117).
   xint has a full .engines (checked with `ls`), so tonight is not affected.
3. **MEDIUM (owner policy): release-list entries carry no time.** A tree verified days ago, with older engine
   installs or older ignored review data, can be tagged later without a rerun. Before, "release" meant the engines
   were verified at tag time.
4. **LOW-MEDIUM: a run in a linked worktree uses that worktree's ignored data** (.transcription, .classm,
   .extraction-review, .direct-file, node_modules). The tag is then made in main, whose copies may differ. Carry the
   data back to main before releasing; the project rules require this anyway.
5. **LOW: `marker_of` and `trees_of` now accept `release` as if it were a tier.** So `check_all.sh --tier release` is
   accepted until check_all_steps.sh:72-74 rejects it. That happens after a slot wait, and nothing is recorded.
   `in_record release` also reads a per-worktree marker file `check-all-green-release` that nothing writes. This is
   not a hole.
6. **LOW: environment-variable leakage is safe.** If both variables are exported, every full run records release,
   but those runs really are release-mode runs. `CHECK_ALL_RELEASE=1` alone only makes full runs rewrite
   interview_length.md. Fast and docs tiers are excluded (:64), and so is `--year N` (:57-60, which exits before
   recording).
7. **LOW: test gap.** test_pre_push.sh never exercises the skip path. A one-block test is sketched in A.3.
8. **Operational note for tonight (not a defect):**
   - The skip fires only if main's release commit has exactly the recorded after-tree. That tree is the
     post-run tree, with reports rewritten (check_all.sh:49, 61-66).
   - main (acde74b5) is not an ancestor of xint's HEAD (0c8cd21d) (checked with `git merge-base --is-ancestor`). Any
     landing that produces a different tree falls back to the ordinary 60-minute release run. That fallback is safe.
   - Any edit outside reports/ and rendered/ in xint during the run voids the green record (check_all.sh:51-56).
     The tooling files' modification times are 23:08-23:11, so make sure the run started after them.
   - Do **not** land the change proposed in B before tonight's release; it makes screens due (see B).

**B. Screen and false-no prompts.** The open item is only partly accurate.
- **Screen reviews:** the defect is real. screen_review.py:142 shows the YAML `expr.source` as the question. Measured
  on xint's canonical/2025: 134 of 149 screens have YAML text that differs from the interview prompt, and the screen
  subject (screen_subject, :258-265) does not track the interview wording at all.
- **Gate and false-no reviews:** these already show the interview wording (gates.wording, gates.py:93-98, used by
  describe :127-150).
- **Leftovers in those prompts:** enum answers are shown with YAML labels (else_text :115-124), the interview's
  `choices` are dropped, and the fallback to `expr.source` is silent.

The design is to use `gates.wording()` in the screen prompt and subject. Doing so makes 134 screen subjects due, and
`check_screens --release` would then refuse a release. A rerun costs about $14.50 (134 × the $0.108 mean sample cost).
The alternative is a $0 one-time subject migration. That decision is the owner's.

**C. The 71.48 MB store record.**
- **What writes it:** transcribe.py's log writer (`_sections`, :2184-2199). It prints the full `Project:` and
  `Second:` expressions of each DISAGREE line, as expanded by `Expander` (transcribe.py:1368ff.). The expander
  inlines every helper line, which turns a shared graph into a tree.
- **Measured on 43fe6dd0…:** the f8889 record is 74.9 MB. Its JSON blocks hold only **250 distinct subtrees
  (28.6 KB once shared subtrees are stored once)**. gzip gives 767 KB.
- **Growth:** f8889 records were 57.0 MB on 2026-11-12 (commit 168a49d9) and 74.9 MB on 2026-11-15. Each new f8889
  pass writes a new immutable file. One more level of helper sharing could double the size.
- **Other large files in main:**
  - Over 30 MB: only this one.
  - Over 5 MB: eic at 24.7 MB and 17.7 MB; household at 12.0 MB and 10.8 MB; dependent at 8.8 MB; s2 at 6.1 MB.
  - xint has an uncommitted new f8889 record, e3b28879…, at 74.9 MB.
- **Fix:** write expressions with shared subtrees stored once (a subtree table plus `{"$": sha}` references), decode
  on read, and keep rulings keys computed on the expanded text. Add a size guard in pre-push or pre-commit now.

---

## A. Adversarial audit of the release skip path

Diff read: `git -C .claude/worktrees/xint diff HEAD -- tools/green.sh tools/check_all.sh tools/release.sh
tools/hooks/test_green.sh`. Also read: check_all_steps.sh (uncommitted in xint; release_steps), check_all_bg.sh,
commit_tested.sh, hooks/pre-push, hooks/test_pre_push.sh, check_slot.py (env handling), engines/run_engines.py,
engines/engine_cache.py.

### A.1 What holds (checked)

- **Single writer of the release list:** check_all.sh:64-67, after `record_green "$after" "$tier"` (:62). It is
  reached only if:
  - the suite passed (`set -e`, :48);
  - nothing outside reports/ and rendered/ changed (:51-56);
  - the year is the default (:57-60 exits 0 before recording);
  - `tier=full` and `release_mode` hold: green.sh:91 requires exactly `CHECK_ALL_RELEASE=1` and
    `ENGINE_CACHE=verify`.

  grep found no other `record_green ... release`.
- **Variables reach check_all.sh through the background path:** environment → `nohup "$0" --run` → check_slot.py
  `os.execvp` with `os.environ` (check_slot.py:180-182). The snapshot runs the snapshot's own check_all.sh and
  green.sh (check_all_bg.sh:150), so uncommitted tooling edits are what get tested and what record.
- **Fast or docs runs with the variables set** do not record release (:64). In those tiers interview_length is
  excluded anyway (check_all_steps.sh:69-81).
- **`--year`:** no record (:57-60). release.sh passes no `--year`.
- **Skip condition, release.sh:50-53:** `is_release_green && is_green` on `HEAD^{tree}`. The clean-tree check (:41,
  :45) makes HEAD's tree equal to the worktree's tree. Line :76 requires the tagged commit's tree to equal `tested`.
  commit_tested.sh is not called on the skip path, because `tested == HEAD tree`.
- **release_reviews.sh:** still reached. It runs at :44, before the branch at :51, and :45 rechecks the tree.
- **Concurrent recording:** `record_green` serializes with a lock directory (green.sh:60-75), so concurrent runs lose
  no entries.
- **pre-push** (hooks/pre-push:20-36) requires `is_green(tree)` and `release-ready/<tree>`. Both paths write
  release-ready (release.sh:86). pre-push does not read the release list.
- **After-tree versus HEAD tree:** the list holds the after-tree, meaning reports rewritten by the run, including
  interview_length.md, which only release-mode runs write. A later normal full run on that tree records it as
  full-green only. A merge on main that changes the tree is not in the list, so release.sh runs the suite. Both cases
  fail safe.

### A.2 Findings, ranked

**1. MEDIUM-HIGH: a direct run in a shared, editable worktree.**
- *Checked:*
  - check_all.sh:51 excludes reports/ and rendered/ from the outside-change test.
  - Slots are counted per machine (check_slot.py; CHECK_ALL_MAX_RUNS=2), so two check_all.sh runs in the same
    worktree can overlap.
  - The old release path always ran in `$common/check-all-worktree` under the per-clone lock (check_all_bg.sh:79-89,
    94-119).
- *Inferred, not reproduced:* a concurrent fast run in the same worktree rewrites reports/ (evidence with its fast-run
  note and its E column taken from the last release; check_all_steps.sh:38-41) between the release run's
  `before` and `after`. The release list then certifies a tree whose reports came from the other run. The same
  happens if an agent or tool writes reports/ mid-run.

This exposure already existed for the full-green record, which is the commit gate. It is new for releases.

Minimal fix: record release only from the isolated background snapshot. This restores the old isolation exactly. The
coordinator would then run `CHECK_ALL_RELEASE=1 ENGINE_CACHE=verify tools/check_all_bg.sh --wait --tier full` in xint
instead of a direct check_all.sh.
```diff
--- a/tools/check_all.sh
+++ b/tools/check_all.sh
@@
-if [ "$tier" = full ] && release_mode; then
+# Only the background snapshot worktree (tools/check_all_bg.sh) is free of concurrent writes to reports/ and rendered/.
+if [ "$tier" = full ] && release_mode \
+   && [ "$(pwd -P)" = "$(cd "$(git rev-parse --git-common-dir)" && pwd -P)/check-all-worktree" ]; then
   record_green "$after" release
   echo "check-all green in release mode: tree $after (tools/release.sh tags it without another run)"
+elif [ "$tier" = full ] && release_mode; then
+  echo "check-all: release mode outside tools/check_all_bg.sh; not added to the release list"
 fi
```
The README line 193, release.sh:20-22 and green.sh:12-14 would then say "through tools/check_all_bg.sh".

Alternative that keeps direct runs: a per-worktree exclusive lock taken by every check_all.sh, using `mkdir` on
`$(git rev-parse --git-path check-all-run.lock)` with a stale-pid check. That is a larger change, and it also changes
the normal path.

**2. MEDIUM: outside engines are silently skipped in a direct run.**
- *Checked:*
  - run_engines.py:628-634 prints `SKIPPED` and continues when OpenTaxSolver or UsTaxes is missing.
  - check_all_bg.sh:50-55 and 109-117 fall back to the primary worktree's .engines.
  - xint/.engines contains opentaxsolver-src, ustaxes-src, ustaxes-deps, venv, cache and work (`ls`).

Sketch:
```diff
--- a/tools/engines/run_engines.py
+++ b/tools/engines/run_engines.py
@@ def main():
+    release = os.environ.get("CHECK_ALL_RELEASE") == "1"
     if ots is None:
+        if release and ots_adapter.package_dir() is None:
+            sys.exit("OpenTaxSolver is not installed; a release run needs every outside engine (tools/engines/README.md)")
         print("OpenTaxSolver: SKIPPED - ...")
@@
     if ust is None:
+        if release and not os.path.isdir(ustaxes_adapter.USTAXES_SRC):
+            sys.exit("UsTaxes is not installed; a release run needs every outside engine")
         print("UsTaxes: SKIPPED - ...")
```
*Inferred:* `ustaxes_adapter.available(YEAR)` can be false because the year is unsupported rather than because the
engine is missing, so the guard tests whether the package is installed, not whether it is available. Check
`os`/`sys` imports and the adapter attribute names before applying.

**3. MEDIUM (policy): release-list entries have no age limit.**
- *Checked:* green.sh:73 stores the bare tree; nothing bounds age except the 50-entry cap.
- Sketch:
  - record `tree epoch` for the release list only;
  - `is_release_green` greps `^TREE ` and compares the epoch with `RELEASE_LIST_MAX_AGE_H`, default 24 for example;
  - `in_record` stays unchanged for the tiers.

Owner decision: whether "release" means verified at run time or at tag time.

**4. LOW-MEDIUM: the data source is the worktree the run started in.**
- *Checked:* check_all_bg.sh:30-35 and 45 copy ignored review data from the starting worktree.
  worktree_data.py checks presence, not equality with main.
- Mitigation: `tools/worktree_data.py carry-back` from xint before release.sh in main. This is the project rule
  already.

**5. LOW: `release` in marker_of and trees_of.**
- *Checked:* green.sh:46 and :54. check_all.sh:33 then accepts `--tier release`. check_all_steps.sh:72-74 rejects it
  and nothing is recorded.
- Cleaner fix: keep `marker_of` to tiers only; add `release_list()` (echo `${GREEN_TREES%-trees}-release-trees`);
  make `is_release_green` do `[ -f "$(release_list)" ] && grep -qx "$1" "$(release_list)"`; make check_all.sh call a
  `record_release` that locks that list. Cosmetic; not needed tonight.

**6. LOW: environment leakage** (checked, see A.1). The only side effect is that `CHECK_ALL_RELEASE=1` exported alone
makes interview_length.md churn on every full run.

**7. LOW: test gap.** test_pre_push.sh:109-160 stubs check_all_bg.sh and never records release. Proposed block, after
the `STUB=reports` case:
```bash
# A tip whose tree is release-listed (and full-green) is tagged without running the suite: the red stub would fail it.
record_green "$(git rev-parse 'HEAD^{tree}')" release
STUB=red tools/release.sh >/dev/null || fail "release.sh ran the suite on a release-listed tree"
[ "$(git rev-parse "r$day.3^{commit}")" = "$(git rev-parse HEAD)" ] || fail "release.sh did not tag the release-listed tip"
```
The negative case, a full-green tree that is not release-listed still running the suite, is covered by the existing
`STUB=red` test at :141, because the stub records no release entry.

**8. Not found:** a way to reach the skip path with a tree that never had a green full release-mode run. Snapshot
worktree markers are per worktree and cannot leak into main's `MARKER-release`, because nothing writes that file.

**Minor documentation point:** release.sh:2-16 still opens with "Makes a release: a full check-all run on the clean
tip". Lines 20-22 qualify it. Low.

## B. Interview wording in the screen and false-no prompts (design and diff sketch)

### B.1 Where the prompts are built (checked)

- **screen_review.py**
  - `build_prompt` :122-174. The question is `Input {screen}: {sline['expr']['source']}` (:142), the YAML text.
  - The help comes from `gates.wording(sline)["help"]` (:254-255) and is left out of the subject.
  - The subject is `screen_subject` (:258-265), a hash of the prompt without help and gate, so it hashes the YAML
    source.
  - The stored record's `question` field is also `expr.source` (:302).
- **Gate prompts** (screen_review `build_gate_prompt` :177-228) and **false-no prompts** (false_no_review
  `build_prompt` :88ff.) both use `gates.describe` (gates.py:127-150). That function shows `wording()`: the
  interview prompt and help from canonical/<Y>/interview-full.json and interview-ny.json (gates.py:77-98).
  `gates.subject` hashes `wording()` (:101-112).
- **Remaining YAML text in gate and false-no prompts:**
  - (a) `else_text` names enum alternatives by YAML `label` (gates.py:115-124);
  - (b) `questions()` keeps only prompt and help and drops the interview's `choices`, which hold the answer labels
    the filer picks from (interview JSON has `choices[].label`, checked);
  - (c) `wording()` falls back to `expr.source` silently for an input that neither profile asks;
  - (d) computed conditions and gate lines show line labels, which is correct because they are not questions.
- **Freshness:** both tools call `build_fresh.require(rendered=True)` (screen_review.py:377, false_no_review.py:289),
  so the canonical interview is current when they run.

**Measured on xint, read-only, against canonical/2025/interview-full.json** (1147 questions; that build's freshness
is not verified): 149 screens; 15 have prompt equal to `expr.source`, 134 differ, and none are missing from the
interview. Examples:
- `dependent.married`: YAML "a person legally separated under a decree…" versus interview "or is this person on a
  joint tax return for 2025…".
- `f1116.foreign_gain`: the interview adds "(or, on a joint return, your spouse)".

So since the redraft, **a change to interview wording never makes a screen due**. That is the more serious half of the
open item.

### B.2 Design

1. **Screen prompt and subject use the interview wording.** `prompt_for` passes `gates.wording(sline)["prompt"]`
   with or without the gate, so the wording is in the subject. Help stays out of the subject (current rule,
   :258-263).
2. **Choices.** `questions()` keeps `choices` (their `label`s) **only when non-empty**. The wording dict of a Bool
   question then keeps its current shape, and `gates.subject` changes only for units with an enum question.
   `describe` prints "Answers offered: …". `else_text` maps an enum value to the interview label when a choice has
   that value, and keeps the YAML label otherwise.
3. **Fallback made visible.** When `wording()` falls back, the prompt says "(this input is not asked in the
   interview; the form's own question text)". Use a separate flag function, so the wording dict and therefore
   `gates.subject` do not change.

### B.3 Diff sketch
```diff
--- a/tools/transcription/screen_review.py
+++ b/tools/transcription/screen_review.py
@@
-def build_prompt(screen, sline, gated, excerpt, gate="", help_text=""):
+def build_prompt(screen, sline, gated, excerpt, question, gate="", help_text=""):
@@
-Input `{screen}`: {sline['expr']['source']}
+Input `{screen}`: {indent_rest(question, "  ")}{gates.fallback_note(sline)}
@@ def prompt_for(screen, gated, lines, mani, with_gate=True):
-    return build_prompt(screen, sline, gated, excerpt, screen_gate(screen, lines) if with_gate else "",
-                        gates.wording(sline)["help"] if with_gate else ""), used
+    w = gates.wording(sline)
+    return build_prompt(screen, sline, gated, excerpt, w["prompt"], screen_gate(screen, lines) if with_gate else "",
+                        w["help"] if with_gate else ""), used
@@ def run_one(...):
-    return {"screen": screen, "question": sline["expr"]["source"], ...
+    return {"screen": screen, "question": gates.wording(sline)["prompt"], ...
--- a/tools/transcription/gates.py
+++ b/tools/transcription/gates.py
@@ def questions():
-                    _QUESTIONS[q["input"]] = {"prompt": q["prompt"], "help": q.get("help", "")}
+                    w = {"prompt": q["prompt"], "help": q.get("help", "")}
+                    if q.get("choices"):
+                        w["choices"] = [{"value": c.get("value"), "label": c["label"]} for c in q["choices"]]
+                    _QUESTIONS[q["input"]] = w
+def fallback_note(line):
+    return "" if line["id"] in questions() else "\n  (Not asked in the interview: the form's own question text.)"
@@ def describe(...):
+    # after each "Gated question" / condition prompt:
+    + ("\n  Answers offered: " + "; ".join(c["label"] for c in w["choices"]) if w.get("choices") else "")
@@ def else_text(gate, inp, lines):
-        return " or ".join(f"`{o}` ({lines[o][1]['label']})" ...
+        # an alternative whose value an interview choice carries is named by the choice label the filer sees
```
*Inferred:* the exact mapping from a `choose` alternative (`then: <line id>`) to a choice `value` needs checking
against one enum gate before writing `else_text`. The choice `value` can be a list (the role example), so the mapping
may not be one-to-one.

### B.4 What it makes stale under the project's rules

- **Screen subjects (screen_subject):** 134 of 149 change (measured). `check_screens.py --release`
  (check_screens.py:20, 92-99) fails on due units, so `release_reviews.sh` would **refuse a release** until they are
  reviewed or migrated. **Do not land this before tonight's release.**
  - Option (a), rerun: about 134 × $0.108 ≈ $14.50. The mean is over the 471 samples in xint's
    reviews/2025/screens/screen_review.json, gates included, so it is approximate. The run needs `--approve-cost`
    because it is above $3.
  - Option (b), a $0 one-time migration: rewrite `subject_sha` from the legacy hash to the new hash for records whose
    legacy subject still matches, and mark them with something like `grandfathered: "yaml-source"`. samples.py:13 and
    :31-37 already have a `grandfathered` concept. This keeps the "prompt changes apply prospectively" rule
    (CLAUDE.md, inference cost), but 134 screens stay unjudged against the wording the filer sees until their next
    change.
  - Option (c): a pilot of about 10 screens (about $1.10) to measure whether verdicts change, then choose (a) or (b).

  The project rule allows a global re-review only "if a measured defect calls for it". The 134/149 mismatch is
  measured; whether verdicts are wrong is not. That is why (c) is suggested. Owner decision.
- **gates.subject:** unchanged for Bool-only units. Units whose condition or gated input is an Enum question change,
  because `choices` is added to the wording dict, and become due for both the screen(gate) and false-no reviews
  (check_false_no.py --release). The number of such units is not measured.
- **rename_carry.py:333** calls `S.screen_subject`. Carry across renames uses the new subject automatically.
  *Inferred:* no change needed.
- **Tests:**
  - test_review_tools.py:3526-3545 (subject invariant under help and gate) should still pass. Their fake inputs are
    not in canonical, so `wording()` falls back to `source`.
  - Fixtures that assert prompt text containing `source` would need updating (e.g. around :881-907).
  - Add a test that changing interview wording changes the screen subject.
- **Docs:** tools/README.md (screen review section), the screen_review.py docstring :17-28, and
  docs/2026-11-10_question_review_design.md:40 and :81. The last is dated testimony; leave it as it is and note the
  change in the decision record.
- The raw prompts in .transcription/screens/ are historical, and nothing needs to change there.

## C. The 71.48 MB review-store record

### C.1 What writes it (checked)

- `review_store.write_record` (review_store.py:226-250) stores one pass's log, split into parts, at
  `reviews/store/<kind>/<sha>.md`. The file is immutable and content-addressed (design doc :43).
- The bulk is DISAGREE sections written by `transcribe._sections` (transcribe.py:2184-2199). Each prints
  `Project:` and `Second:` as full JSON. Both sides are produced by `Expander` (transcribe.py:1368-1440): it expands
  helper lines and definitions in place, "so helper naming on either side does not matter", recursing to depth 40.
  f8889 reuses guard helpers heavily (coverage changed, family or self-only, months), so the shared graph becomes an
  exponential tree.
- **Section sizes in 43fe6dd0…** (main, f8889, 74,955,497 bytes; parsed read-only):
  - the "Source-based partial-input checks" heading begins a span of 74.9 MB, but the table itself is small;
  - the span is the per-line part sections that follow;
  - the largest single expressions are 39.8 MB, 23.7 MB, 4.5 MB, 3.1 MB, 1.9 MB and 1.9 MB.

### C.2 How compressible it is (measured)

- Hash-consing the 25 JSON blocks, storing every subtree of at least 80 characters once: **250 distinct subtrees,
  28,578 bytes in total**, against 74,906,342 bytes raw. The size is pure duplication.
- `gzip -c`: 766,944 bytes.

### C.3 Growth (checked)

- f8889 transcription records:
  - 4136f37d…: 57.0 MB on 2026-11-12, commit 168a49d9;
  - 43fe6dd0…: 74.9 MB in main, commit acde74b5 of 2026-11-15;
  - e007c1c7…: 74.9 MB in many lane worktrees;
  - e3b28879…: 74.9 MB, a new uncommitted record in xint.
- Every f8889 transcription pass adds about 75 MB as a new blob. Adding one more shared helper level doubles a tree.
- The 107 MB file rejected today was not found in commits since 2026-11-08 on any ref. It may have been in a commit
  that was rewritten. *Inferred:* it was an f8889 or eic variant.
- **Store files in main above 5 MB** (`find reviews/store -size +5M`; only one is above 30 MB):

  | Size | Form | Record |
  |---|---|---|
  | 74.9 MB | f8889 | 43fe6dd0 |
  | 24.7 MB | eic | 6b79af15 |
  | 17.7 MB | eic | 9e64b305 |
  | 12.0 MB | household | 6dafaa10 |
  | 10.8 MB | household | 681888e6 |
  | 8.8 MB | dependent | 9ebdabda |
  | 6.1 MB | s2 | 642f5afe |

  xint adds eic 789d33fd at 23.8 MB and dependent 7dcc19a4 at 8.9 MB.
- The store is 180 MB in main (`du`).

### C.4 Proposed fix

1. **Now, mechanical: a size guard.** Add a pre-push check, or pre-commit, which is cheaper and earlier, that
   refuses any blob in the pushed range or the index over 50 MB. GitHub warns at 50 MB and refuses at 100 MB. Sketch
   for pre-push, inside the commit loop:
   ```bash
   big="$(git diff-tree -r --no-commit-id -z "$commit" --diff-filter=AM | ... git cat-file --batch-check='%(objectsize) %(rest)' | awk '$1>50000000')"
   ```
   Also add a soft guard in `review_store.write_record`: warn when content exceeds 40 MB. Do not raise there; that
   would waste a paid review that has already run.
2. **The real fix: store shared subtrees once in the record.** In `_sections`, write each expression as
   `{"root": {...}, "shared": {sha12: subtree}}`, using hash-consing with a size threshold. Measured: 75 MB becomes
   about 30 KB.
   - Old records are immutable and remain readable. The decoder detects the `shared` key.
   - **Readers to port:**
     - rulings.py:352, the regex that captures `Project:` and `Second:` JSON;
     - rulings.py:97, `HASHED` (`project_expr_sha256`, `second_expr_sha256`). Keep the key computed on the
       *expanded* canonical text, or old rulings stop matching. Expansion can be streamed into hashlib without
       building the string;
     - triage.py:192-203 and :325, which evaluate the project and candidate expressions;
     - carry (T-218) and rename_carry;
     - review_store parse and view.
   - *Inferred:* the Expander's own `pa == sb` comparison could compare root hashes. That also removes the CPU and
     memory cost of building 40 MB strings for every comparison.
   - Touches transcribe.py, rulings.py, triage.py, carry and rename_carry, review_store.py and their tests.
   - Under the project rules this is a tool change. It applies prospectively and makes nothing due, provided the
     ruling keys stay on the expanded text.
3. **Alternatives considered:**
   - gzip records over N MB (767 KB here). Simple, but it loses greppability, every `_read` must handle `.gz`, and
     it only delays the limit, by about 100×.
   - Store only expression hashes plus line ids and recompute on read. That breaks triage's evaluation of historical
     records.
   - Shard by line part. That does not help, because a single expression is 40 MB.
4. **History:** blobs of 57 MB and 75 MB are already in history. No rewrite is proposed. The guard prevents new ones.
   Lane worktrees each hold copies of e007c1c7…, which is disk only.
