# 2026-11-16: Adversarial Review — Verifiable Integrity and Annual Rollover Foundation

This document records an adversarial audit of the `us-tax-model` (`tax-formalization`) codebase at `r2026.11.16.1`,
conducted with two goals in mind:
1. **Verifiable integrity:** finding places where the mechanical, formal, or epistemic guarantees have code-level holes,
   silent fallbacks, or feedback loops beyond the limitations already disclosed in `README.md` and `docs/TRUST.md`.
2. **Annual rollover foundation:** finding structural, tooling, and architectural failure modes that will block or
   degrade tax year 2026 adoption and multi-year maintenance (TY2026, TY2027, TY2028+).

Each finding below includes the exact files and line numbers, the failure mechanism, and an actionable specification for
an agent or lane to fix and self-test it.

---

## Part I: Verifiable Integrity Findings

### 1. Silent Section Truncation and Draft-Watermark Bypass in `tools/transcription/year_carry.py` (P0 — Soundness Bug)

- **Where:** `tools/transcription/year_carry.py`, lines 138–162 (`Tree.pages`, `Tree.anchors`) and lines 256–269
  (`anchor_section`).
- **What `year_carry.py` claims:** A line's review verdict carries to the next tax year only when its cited source text
  at *anchor-section granularity* is unchanged after lockstep year normalization:
  > *"for each cited page segment, the text from the cited anchor heading to the next anchor any citation of the same
  > document names on those pages, else the cited pages whole ... Never only the quoted words, so a paragraph added
  > under the same heading changes the key."* (lines 19–23)
- **What actually happens:**
  1. **In-sentence cross-reference truncation (false carry / soundness hole):**
     ```python
     def anchor_section(text, anchor, known):
         flat = _norm_space(text)
         if not anchor:
             return flat
         at = flat.find(_norm_space(anchor))
         if at < 0:
             return flat
         start = at + len(_norm_space(anchor))
         ends = [flat.find(_norm_space(k), start) for k in known if k and _norm_space(k) != _norm_space(anchor)]
         ends = [e for e in ends if e >= 0]
         return flat[at:min(ends)] if ends else flat[at:]
     ```
     `known` (`tree.anchors(seg_doc)`) is the set of **all** anchors cited anywhere in that document across the year's
     forms (e.g., `"Line 1"`, `"Line 2"`, `"Line 4"`, `"Part I"`, `"Step 1"`). `flat.find(_norm_space(k), start)`
     performs a raw substring search anywhere after `start` without checking whether `k` is a section heading or a
     subsequent line. If the instructions under `"Line 5"` say *"Subtract Line 4 from Line 1..."* or *"Enter the amount
     from Part I..."*, `flat.find("Line 4", start)` or `flat.find("Part I", start)` matches inside the prose of Line 5
     and **slices off the remainder of Line 5's section**. Any new paragraph, exception, or limit added by the IRS after
     that cross-reference is excluded from `anchor_section`, allowing `year_carry.py` to falsely report the cited text
     as unchanged and carry a stale review verdict into the new year.
  2. **Unnormalized anchor matching (false invalidation):** Unlike `tools/citations.py` (`norm()`), `anchor_section`
     only normalizes whitespace (`_norm_space`). When an anchor in a locator differs from raw PDF extraction in case,
     soft hyphens, line-end hyphenation, leader dots, or dash spacing (e.g. `"Chart — Line 18a"`), `flat.find` returns
     `-1` and falls back to the entire page range (`flat`), causing unrelated changes elsewhere on the page to block the
     carry.
  3. **Bypass of `tools/archive_text.py` draft watermark stripping:** `Tree.pages` (lines 138–147) reads `cols_file` or
     `text_file` directly via `self.read(*self.dir("sources", doc), name)` (`open()`) instead of calling
     `archive_text.read()`. It escaped `archive_text.py --self-test` because the filename lookup (`cols_file` /
     `text_file`) and the `open()` call are on separate lines (`archive_text.py` line 92 notes: *"A line scan: a layer
     path built in one place and read in another escapes it"*). Consequently, on any IRS draft document, `year_carry.py`
     reads raw draft watermarks and cover pages.
- **How to fix:**
  1. Route `Tree.pages` in `tools/transcription/year_carry.py` through `archive_text.read(sources_dir, d, key)` and
     tighten `archive_text.py`'s `direct_reads` check to catch helper methods that open paths under `sources`.
  2. Fix `anchor_section` so section boundaries only match actual headings (e.g., line-initial headings in the
     page text before flattening newlines, or headings that appear after `at` and are not preceded on the same line by
     prose words like `"from"`, `"see"`, `"add"`, `"subtract"`, `"on"`), and match using `citations.norm` (or span
     offsets over normalized text).
  3. Add a near-miss test case to `year_carry.py --self-test` where `"Line 5"`'s body mentions `"Line 4"` in prose
     (`"Subtract Line 4 from Line 3."`) followed by a second sentence that changes in the new year, verifying that
     `compare_parts` returns `carries = False`.

---

### 2. Gaps Between the TypeScript Evaluator (`engine/src/eval.ts`) and the Lean Reference Evaluator (`lean/TaxFormalization/Eval.lean`) (P1)

- **Where:** `engine/src/eval.ts`, `engine/src/compare.ts`, `engine/src/interview.ts`, and
  `lean/TaxFormalization/Eval.lean`.
- **What actually happens:**
  1. **Two incompatible memo-rollback mechanisms in `engine/src/eval.ts`:**
     - In `evalLine` (`engine/src/eval.ts:258-265`), a refusal gate marked `when_known: true` snapshots
       `const before = refusal.when_known ? new Map(ctx.memo) : null` and restores `ctx.memo = before` when the gate
       evaluates to `unknown`—**without rolling back `ctx.memoLog`**.
     - In `chooseUnresolved` (`engine/src/eval.ts:720-740`), speculative evaluation of alternatives after an unknown
       guard records `const mark = ctx.memoLog.length` and rolls back via
       `for (const key of ctx.memoLog.splice(mark)) ctx.memo.delete(key)`. If a `when_known` gate was rolled back via
       `ctx.memo = before`, stale keys remain in `ctx.memoLog` and can be deleted later if a subsequent evaluation memoizes
       them and an enclosing `chooseUnresolved` splices `memoLog`.
     - Furthermore, when `chooseUnresolved` finds that all possible paths refuse (`engine/src/eval.ts:735-739`), it
       returns early **without** rolling back `ctx.memo` (`memoLog.splice(mark)` is only reached on line 740). All
       speculatively evaluated derivations from untaken branches remain in `result.derivations`.
  2. **`multiply_count` in TypeScript omits `BigInt` and `safeNumber`:**
     - In `engine/src/eval.ts:531`, `multiply_count` computes `amount.cents * count.value` directly as a JavaScript
       `number` without `BigInt` or `safeNumber()`, whereas every other money atom (`sum`, `sum_over`, `subtract`,
       `round`, `multiply_rate`, `percent_floor`) uses `BigInt` and `safeNumber()`.
     - Similarly, in `engine/src/eval.ts:558`, `multiply_rate` with `unit` computes `rate.den * expr.unit` as a JS
       `number` before passing it to `multiplyRateHalfUp`.
  3. **`unknown` metadata and `inputsAhead` are not verified by `compare.ts` / `Eval.lean`:**
     - In `engine/src/compare.ts:114`, `normalize` reduces every `unknown` value to the bare string `"unknown"`,
       discarding `input`, `lowerBound`, and `GATE_PENDING` (`gatePending`).
     - Yet the interview engine (`engine/src/interview.ts:347-386`) relies directly on `der.value.input`, `der.awaits`
       (from `evaluate(..., { ahead: true })`), `lowerBound`, and `GATE_PENDING` to decide which questions are
       reachable and when a return is complete. `Eval.lean` does not implement `ahead` mode (`inputsAhead`) or track
       `input` on `unknown` values, and `compare.ts` never checks `lowerBound` or `gatePending` on `unknown` outputs.
- **How to fix:**
  1. In `engine/src/eval.ts`, replace `const before = refusal.when_known ? new Map(ctx.memo) : null` with the same
     `const mark = ctx.memoLog.length` rollback used by `chooseUnresolved`, and roll back speculative `memoLog` entries
     in `chooseUnresolved` before returning on line 738 (matching `Eval.lean:770-772` or keeping `Eval.lean` and
     `eval.ts` identical).
  2. In `engine/src/eval.ts:531`, compute `safeNumber(BigInt(amount.cents) * BigInt(count.value))`.
  3. In `lean/TaxFormalization/Eval.lean` and `engine/src/compare.ts`, include `lowerBound`, `gatePending`, and `input`
     (for missing-input unknowns) in `normalize()` so that both evaluators are checked for agreement on unknown-input
     provenance.

---

### 3. Single-Family Auto-Ruling Loops in `tools/transcription/carry.py` and `tools/transcription/subjects.py` (P2)

- **Where:** `tools/transcription/carry.py` (lines 465–581) and `tools/transcription/subjects.py` (lines 147–202).
- **What actually happens:**
  1. **Unreached branches in `triage_equivalence` (`carry.py:465-505`):**
     With reviews now Claude-only (`CLAUDE.md`), `carry.py` automatically rules 9 out of 10 open transcription
     disagreements (`AUDIT_EVERY = 10`) as `"Ruling: representation; equivalent on executable triage, ruled
     mechanically"` whenever the project's line and the candidate's line agree on the fixtures and `MIN_GENERATED = 500`
     generated returns. However, `triage_equivalence` only checks `line.get("triage") == "agrees on sample"` and
     `sources.get("generated")`—it does **not** verify that the specific branch, guard, or floor where the two
     expressions syntactically differ was actually reached by the sample (`reports/2025/properties.md` shows the
     generator leaves many branches unreached). An edge-case bug in a rarely reached branch can therefore be
     mechanically ruled "equivalent" without any agent reading the source text.
  2. **In-document `boundary` lines in `subjects.py` omit semantic changes (`subjects.py:147-202`):**
     For line-scoped transcription reviews, `reach(doc, line_id)` stops at other printed computed lines in the same
     document (`boundary`), and `transcription_line_subjects` hashes only:
     ```python
     [{"boundary": i, "printed": str(by_id[i]["printed"]), "type": by_id[i]["type"]} for i in sorted(boundary)]
     ```
     It strips `label` (via `WORDING`) and does not include `i`'s expression. If printed line `X` is edited to change
     what `X` computes (or its label is updated to reflect a different concept) while keeping its `printed` number and
     `type` (`NonNegDollars`), another printed line `Y` in the same form that reads `X` has an unchanged `subject` hash
     and is skipped by `--lines auto`.
- **How to fix:**
  1. In `tools/transcription/subjects.py`, include `by_id[i].get("label")` (or `by_id[i]`'s own line-subject hash) in
     the `boundary` entry of `transcription_line_subjects` so that changing a printed line's meaning or expression
     invalidates downstream printed lines in the same form, or include its `label` in the boundary interface just as
     `foreign_interfaces` includes `source` for foreign inputs.
  2. In `tools/transcription/carry.py` (`triage_equivalence`), require that any guard or branch present in the candidate
     or project expression for that line was exercised at least once in the triage run (or require `compared` to cover
     both `true` and `false` for a Bool line / guard difference) before auto-ruling without source reading.

---

### 4. Release Gate (`tools/release_reviews.sh`) Passes When Sampled Reviews Confirm Unfixed Medium/High Bugs (P2)

- **Where:** `tools/release_reviews.sh`, `tools/transcription/check_completeness.py`,
  `tools/transcription/check_screens.py`, `tools/transcription/check_false_no.py`.
- **What actually happens:**
  The release gate checks that every sampled completeness, screen, and false-no review is current and has no unruled
  finding. However, a ruling in `rulings.json` that confirms a real defect and cites an open `BUG_INVENTORY.md` entry
  is counted as "ruled" just like a dismissed false positive. In `r2026.11.15.1` (`HANDOFF-NEXT-SESSION.md`), 42 open
  medium findings (including ~25 narrow interview questions that cause filers to answer No and drop items) passed the
  release gate because they were ruled as open bugs.
- **How to fix:**
  In `check_completeness.py --release`, `check_screens.py --release`, and `check_false_no.py --release`, cross-check
  any ruling that cites a `BUG-XXXX` entry against `tools/bug_status.py`. If the cited bug is still open (and is high
  or medium severity), fail the `--release` check unless an explicit flag (e.g. `--allow-open-bugs`) is passed and
  recorded in the release notes.

---

## Part II: Annual Rollover & Multi-Year Foundation Findings

### 5. `tools/transcription/check_logs.py` Will Fail Every Carried Review Log at TY2026 Adoption (P0 — Rollover Blocker)

- **Where:** `tools/transcription/check_logs.py` (lines 142–147) and `docs/ty2026/ADOPTION.md` (step 7, lines 67–71).
- **What actually happens:**
  `ADOPTION.md` step 7 notes: *"Before that, check_logs must read a carried record's source snapshot rows against the
  2025 manifest (not yet built)."*
  Currently, `check_logs.py` runs:
  ```python
  for row in re.findall(r"^\| (\S+) \| [^|]* \| [^|]* \| [^|]* \| ([0-9a-f]{64}) \|(?: [^|]* \| ([0-9a-f]{64}|-) \|)?$", text, flags=re.M):
      doc_id, sha, cols_sha = row
      if doc_id in docs and docs[doc_id]["text_sha256"] != sha:
          stale.append(f"{kind} log was made against a different snapshot of {doc_id}")
  ```
  Because `review_store.py` stores immutable pass records under `reviews/store/<kind>/<sha>.md`, any 2025 review record
  carried into `reviews/2026/<kind>/<form>.index.json` by `year_carry.py --write` still has the **2025**
  `text_sha256` and `cols_sha256` in its `## Source pages` table. When `check_logs.py --year 2026` runs, it compares
  those 2025 hashes against `sources/2026/manifest.json` (`docs`) and fails every carried form. Even if a 2026 form has
  line-scoped passes for changed lines, `review_store.view()` renders the header's `## Source pages` table from the
  `base` (2025) record and the pass blocks' `## Source pages` tables from the 2026 passes, so `re.findall` over the
  rendered `text` sees both years' hashes and fails on the 2025 ones.
- **How to fix:**
  1. In `check_logs.py` (and `review_store.py`), check source snapshots per record (or per index entry) rather than with
     an unanchored regex over the assembled view text:
     - A record carried from year `F` (`carried.from == F` or `year_carried.from == F` on the index lines it backs)
       must have its source hashes checked against `sources/<F>/manifest.json`, **and** `check_logs.py` must verify
       that each carried line's `year_key` in the index matches `year_carry.py`'s current key for `F -> Y` (so a carried
       line cannot stay green if the `Y` source text or parameters later change).
     - Any non-carried record (a `Y` whole-form or line-scoped pass) checks its source hashes against
       `sources/<Y>/manifest.json`.
  2. Add a self-test in `tools/transcription/test_review_tools.py` (or `year_carry.py --self-test`) that carries a
     review across a synthetic year with a new source manifest hash and runs `check_logs.py` on the target year.

---

### 6. `tools/year_changes.py --check` Does Not Run Type, Cycle, or Guard Exhaustiveness Checks on the Applied Tree (P1)

- **Where:** `tools/year_changes.py` and `engine/src/check.ts` (noted in `docs/2026-11-14_year_change_operations.md`
  section 7).
- **What actually happens:**
  `changes/2026/` already holds 130 entries and 1,256 operations across 54 files. `year_changes.py --check` verifies
  that operations apply cleanly, references resolve, gated inputs are read only by their gates, new inputs have
  questions/defaults, and cited quotes exist in `sources/2026/`. However, it does **not** run `engine/src/check.ts` on
  the resulting tree. Any type error (`Dollars` vs `NonNegDollars`, `Count` vs `Dollars`), cycle across `def`
  instances, non-disjoint or non-exhaustive `choose` guard interval tiling, or `interview-rules` violation introduced
  by those 1,256 operations is currently invisible until adoption day.
- **How to fix:**
  1. In `tools/year_changes.py`, add an option (enabled in `check-all`) that exports the in-memory applied 2026 state
     (combining the applied 2025 forms/interview/register with the staged parameters in
     `research/ty2026/params-2026.proposed.yaml` and tables in `research/ty2026/tables-2026/`, falling back to 2025
     values for unsourced parameters) and runs `engine/src/check.ts` (with a flag skipping citation snapshot-hash
     checks for unarchived 2026 documents).
  2. This turns `year_changes` from a syntax/patch-applicability check into a full static semantics check of TY2026 on
     every commit.

---

### 7. Multi-Year Repository Scaling and Multi-Year `check-all` Execution Model (P2 — Architectural)

- **Where:** `tools/check_all_steps.sh`, `tools/year_diff.py`, `years.json`, `tools/baseline_check.py`.
- **What actually happens:**
  1. **Single-year `check-all` vs. multi-year `years.json`:** `check_all_steps.sh` resolves a single `year`
     (`python3 ... import taxyear; print(taxyear.Y)`), which defaults to `max(adopted)` in `years.json`. Once `2026` is
     added to `years.json` (`"adopted": [2025, 2026]`), `check-all` will stop checking `2025` by default. Any change to
     shared engine code (`engine/src/`), Lean (`lean/`), or shared tools (`tools/`) could silently break `2025` builds,
     fixtures, or evaluator agreement. Conversely, running the full suite (including mutation testing and Lean/engine
     differentials) serially for every adopted year on every commit will scale wall-clock time linearly with `N` years.
  2. **Two-year cliff in `tools/baseline_check.py`:** `baseline_check.py` (lines 11–15, 93–98) accepts a carried
     baseline hash by moving `tax_year` and `(YYYY)` back **one** year (`year_back(text, year)`). As its docstring notes:
     *"The match reaches back one year only: an entry still recorded with the hash of two years before comes due."*
     Unless `year_diff.py --adopt` re-hashes carried baseline entries to the new year's subject hash at adoption time,
     every surviving 2025 baseline entry carried into 2026 will simultaneously fail at the 2027 rollover even if its
     line never changed.
- **How to fix:**
  1. In `tools/year_diff.py --adopt` (`carry_reviews`), when copying ` COVERAGE` baseline files (`operands.json`,
     `consumers.json`, `limits.json`, `instruction_cites.json`, `signs.json`), either re-compute the baseline hashes
     for `to_year`'s `tax_year` mark on unchanged subjects, or have `baseline_check.py` normalize `tax_year` and
     `(YYYY)` to `{Y}` before hashing so baseline hashes are year-invariant.
  2. Define the multi-year `check-all` policy before `2026` enters `years.json`:
     - Changes to `forms/<Y>/`, `params/<Y>.yaml`, `tables/<Y>/`, `fixtures/<Y>/`, `interview/<Y>/`, `reviews/<Y>/`
       need only run `check-all --year <Y>` (plus `year_changes` for `<Y+1>`).
     - Changes to shared code (`engine/`, `lean/`, `tools/`) should run fast build + fixture + compare checks across all
       adopted years in `years.json`.

---

### 8. Line ID Drift Across Renumberings (`f1040.line13b` Printed as `13a`) and Missing Cross-Year Carryover Schema (P3)

- **Where:** `changes/2026/` (`f1040.yaml`, `sa.yaml`, `s2.yaml`, `f5695.yaml`) and cross-year carryover forms
  (`clcw.yaml`, `clcw26.yaml`, `f8606.yaml`, `f8582.yaml`, `f4952.yaml`, `f5695.yaml`, `asset.yaml`).
- **What actually happens:**
  1. **Line ID vs. printed line number drift:** Because spec 4.3 keeps line IDs stable across renumberings by mutating
     `printed` (`set: {line: f1040.line13b, field: printed, from: 13b, to: 13a}`), in 2026 `f1040.line13b` is printed
     line `13a` and `f1040.line13a` is printed line `13b`. Across multiple annual rollovers, line IDs named `.line<N>`
     that no longer match their printed line numbers create severe confusion for both human readers and LLM agents, and
     cause ID collisions when a later year introduces a new line at the old number.
  2. **No formal cross-year carryover mapping:** Prior-year return outputs that feed current-year inputs (capital loss
     carryovers, passive loss carryovers, IRA basis, energy credit carryforwards, prior-year depreciation, state tax
     refund recovery) are currently standalone manual inputs with no machine-checked mapping from Year `N` output line
     IDs to Year `N+1` input line IDs. (Also note `forms/2025/clcw26.yaml` has a year-specific filename in the 2025
     forms directory.)
- **How to fix:**
  1. When a printed line changes its printed number or swaps places, prefer renaming its ID to a **semantic,
     number-free ID** (e.g., `f1040.s1a_deduction`, `f1040.qbi_deduction`) using `tools/rename_ids.py` and
     `tools/transcription/rename_carry.py` so no `.line<N>` ID ever lies about its printed number.
  2. Rename `forms/2025/clcw26.yaml` to a year-free form ID (e.g. `clcw_next.yaml` or `clcw_out.yaml`) using
     `rename_ids.py` and `rename_carry.py`.
  3. Add a declarative `carryover/<year>.yaml` map linking Year `N-1` computed/output lines to Year `N` input lines,
     checked by the build so that a user's prior-year log/values sheet can pre-populate next year's carryover inputs
     mechanically.

---

## Summary Checklist for Handoff

| ID | Priority | Target Files | Short Description |
| :--- | :--- | :--- | :--- |
| **AR-01** | **P0** | `tools/transcription/year_carry.py`, `tools/archive_text.py` | Fix `anchor_section` cross-reference truncation, normalize anchors, and route `Tree.pages` through `archive_text.read`. |
| **AR-02** | **P0** | `tools/transcription/check_logs.py`, `tools/transcription/review_store.py` | Support carried review records in `check_logs.py` by checking `from_year` manifest hashes and current `year_carry` keys. |
| **AR-03** | **P1** | `engine/src/eval.ts`, `engine/src/compare.ts`, `lean/TaxFormalization/Eval.lean` | Unify `memoLog` rollback in `eval.ts`, use `BigInt`/`safeNumber` in `multiply_count`, and compare `unknown` metadata (`input`, `lowerBound`, `gatePending`) against Lean. |
| **AR-04** | **P1** | `tools/year_changes.py`, `engine/src/check.ts` | Run static type, cycle, and guard-exhaustiveness checks on the in-memory applied `changes/<year+1>/` tree during `year_changes.py --check`. |
| **AR-05** | **P2** | `tools/transcription/subjects.py`, `tools/transcription/carry.py` | Include boundary-line labels/semantics in `transcription_line_subjects` and require branch reachability before auto-ruling via `triage_equivalence`. |
| **AR-06** | **P2** | `tools/release_reviews.sh`, `tools/transcription/check_*.py` | Fail `--release` review gates when a ruling confirms an open high/medium `BUG_INVENTORY.md` defect unless explicitly overridden. |
| **AR-07** | **P2** | `tools/baseline_check.py`, `tools/year_diff.py`, `tools/check_all_steps.sh` | Make source-coverage baseline hashes year-invariant across >1 rollover and define multi-year `check-all` execution for shared code changes. |
| **AR-08** | **P3** | `forms/2025/clcw26.yaml`, `changes/2026/`, `tools/rename_ids.py` | Replace mismatched `.lineN` IDs on renumbered lines with semantic IDs, rename `clcw26`, and add a cross-year carryover schema. |
