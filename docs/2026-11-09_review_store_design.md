# Review evidence store: content-addressed records and carry across years

**Status: approved by the owner, 2026-11-09, all three stages (charter section 3 and section 7, item 3; phase 1, item 2).**

## 1. What the measurement says

Measured on main `ce07280f`, over the git history since 10-13.

| Part of `reviews/` | Lines churned (added + deleted) | Size now | What it is |
|---|---|---|---|
| `transcription/triage/*.json` | **5,452,800** | 42 MB | Derived: triage records (evaluations of project vs candidate lines). Regenerable from the log, the reply and the engine |
| review logs `*.md` (all kinds) | 791,775 | about 9 MB | The review record: header, source hashes, line sections, embedded raw reply |
| `*.rulings.json` | 108,155 | 45 MB (transcription) | Rulings. Each entry also embeds a full copy of the project-side expression (about 28 KB per entry in `eic`) |
| everything else | 46,426 | | |

Total `reviews/` churn is about 6.4M lines; triage is 85% of it. The retrospective's "88% of churn is regenerated
review output" is mostly **triage evidence, not the review logs**.

The year-rollover measurement adds a second problem. `check_logs` keys staleness to the source text sha256 and the
line subjects. A new year changes every source snapshot, so every form is re-reviewed, roughly $140 to $400 a year.
Only 27 forms have real changes.

## 2. Design

Scope: transcription, render and class M reviews, which are 99% of the churn. Completeness, screen and false-no keep
their current small rulings files.

### 2.1 Derived evidence leaves git (most of the churn)
- **Triage is regenerated on demand, not committed.** Its output goes to the git-ignored `.transcription/triage/`.
  No check-all step reads the committed triage files.
- **Prerequisite:** `triage.py` reads the candidate reply from the committed review record (`rulings.section_reply()`
  already extracts it), not from `.transcription/<stem>.response.txt`. Otherwise triage fails in a fresh clone or a
  worktree without review data. It falls back to `.transcription/` only to verify a receipt.
- **Rulings keep a compact triage stamp:** verdict, kinds, witness ids and triage policy, under 200 bytes. So a ruling
  still records what evidence it relied on.
- **`*.rulings.json` stops embedding expressions.** Each entry stores `project_expr_sha256` and the `second`
  expression's hash in place of the full text, plus the line's cross-document `subject_key`. `carry.py`'s key
  comparison works on the hashes. Argon measured 47.4 MB → about 2.5 MB for transcription rulings.

### 2.2 Review records are content-addressed
- **A record is one pass:** a whole-form pass, or a line-scoped pass over `scope_keys`. A class M pass and a pass on
  a partial-input form (dependent, f8889) are whole-form.
- **Records are stored once and never rewritten,** at `reviews/store/<kind>/<record-sha>.md`, where `record-sha`
  hashes: kind, form, scope, each scoped line's subject key, prompt sha, response sha, and the policy versions. The
  record holds the pass metadata (receipt, prompt, system and policy hashes, source page hashes), the raw reply, and
  each scoped line's subject key and comparison result.
- **A per-form index,** `reviews/<year>/<kind>/<form>.index.json`, maps each compared line to `{record, subject_key,
  status, ruling}`. It also holds a `__rest__` entry: the subject of the document outside every compared line
  (today's `REST_KEY`). A rerun writes one record and updates only the index entries of its scope.
- **Subject keys fold in foreign interfaces** for transcription: the id, document, marker, type and input question of
  every foreign line the line reaches. A changed foreign question changes the prompt, so it must change the key.
- **check_logs:** a line is current when its index entry's subject key equals the line's current key, and `__rest__`
  matches.
- **triage** groups disagreeing lines by `index[line].record` and evaluates each line against its record's reply,
  splicing in support lines for scoped records. This replaces the parsing of pass tags.
- **The per-form `<form>.md` log becomes a generated view** (a render command), not committed. Decided (owner, 2026-11-09): generated. Every tool that reads logs is ported to index plus records: `check_logs`, `rulings`, `rule`, `carry`,
  `triage`, `rerun_all`, the audit scripts. `compare_families` retires with the second family.

### 2.3 Subject keys that survive a year change (carry across years)
A line's year-carry key hashes four things:
1. **The line's subject** as its review kind sees it, with foreign interfaces.
2. **The values of every parameter and table the line's closure reads.** A changed value blocks the carry.
   - Parameters are referenced by id in the YAML, but the prompt and the compared expression show the year's value.
     Without this, a 2025 ruling such as "equivalent; the model inlined $15,000" could carry into a year where the
     amount changed.
   - So inflation updates alone **do** trigger a review of the lines that read the changed parameter. That is fewer
     than all forms, and it is sound.
3. **Cited source text, at section granularity.** For every citation of every line in the line's closure, including
   foreign lines it reaches, hash the normalized text of the cited **anchor section**: from the cited heading to the
   next sibling heading, or the whole page when no heading boundary is parsed. **Never hash only the quoted words.**
   A new paragraph added under the same heading would not change a quote. Of 2,328 computed lines, 1,871 cite a page
   with an anchor heading and 1,684 carry quotes; only 2 cite a bare page (Argon's count).
4. **The policy versions.**

**Year normalization is lockstep, not blind.** A year literal is normalized to `{Y}`, `{Y-1}`, … only where it shifted
by exactly +1 between the two years' texts, aligned by diff. Fixed statutory dates stay literal, for example
`asset.after_jan19` ("placed in service after January 19, 2025" is still 2025 in TY2026). So a wrongly incremented
fixed date shows up as a change. Birth-year cutoffs (1961 → 1962) are not ±1 of the tax year in the same sense; they
change, so their lines are reviewed, which is correct.

**What carries.** Records and rulings carry only when all four parts are equal after normalization. Every carried line
is listed in the rollover report for spot review.

### 2.4 Migration and proof
1. A mechanical converter turns every current log and pass into records plus indexes.
2. Proof before commit:
   - `check_logs` gives the same per-form and per-line verdicts, including `__rest__` and foreign-interface staleness;
   - every ruling maps to the same line and verdict, by expression hash;
   - `carry.py` dry runs agree;
   - `transcribe.py` and `render_compare.py` with `--lines auto --dry-run` plan the same scopes on every form, and
     after a planted one-line change;
   - regenerated triage on forms with line-scoped passes (f8962, f1040, sa) gives the same verdicts, kinds and witness
     ids as the committed triage files, before those are deleted;
   - `review_yield.py` output and `reports/2025/evidence.md` are byte-identical.
3. The old files are removed in the same commit. History stays in git.

## 3. What it buys (estimates, to be measured after the build)
- Triage churn (85%) goes away with 2.1. Review-log churn drops to the new records plus small index diffs.
- A year rollover re-reviews only lines with real changes: by the rollover measurement, about 27 of 62 federal forms
  had any change. Estimated saving: $70 to $200 a year.
- Carry within a year improves too. Records are keyed per line subject, so a rerun of one line never disturbs the
  rest.

## 4. Risks
- **A false carry,** where normalization makes two different subjects look equal. Mitigations:
  - normalize years only at first;
  - a self-test suite of near-miss pairs;
  - each carried line is listed in the rollover report for spot review.
- **Migration error.** Mitigated by the verdict-identity proof.
- **Human readability.** The generated per-form view keeps today's reading experience.

## 5. Build plan (after approval)
One Opus agent, in stages, each with the full tier:
1. triage reads replies from committed records; triage regenerated on demand; rulings with hashes and a triage
   stamp in place of embedded expressions (2.1). This stage alone removes about 85% of the churn.
2. The record store and indexes, with the migration proof (2.2, 2.4).
3. Year-normalized subject keys and the carry across years, tested on the TY2026 preparation copy (2.3).

Critiqued by Argon (docs/ARGON_CLAUDE_DISCUSSION.md MSG-026); its corrections are folded in above.
