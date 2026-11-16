# Lane A6-store: store shared JSON subtrees once in review records (claude-opus-5-5, judgment, 2025, us)

Patch: `patches/v3/store-dedup.patch` (409 lines; `git apply --check` passes on xint and on the main checkout).
Scratch: `scratch/round4-store-dedup/` (a/ and b/ copies, `roundtrip_store.py`, `sanity_synthetic.py`).

## Summary

- **The deduplication is placed in the record store, not in the log.** `review_store.write_record` encodes and
  `review_store.parse_record` decodes. Every reader of review text goes through `parse_record`: the view,
  `read_log`, rulings, carry, triage, rename_carry, year_carry and check_logs. So every reader still sees the
  sections exactly as `transcribe._sections` wrote them. No reader has to be ported. This is narrower than
  tooling.md C.4, which proposed changing `_sections` and porting five readers.
- **Old records stay readable unchanged.** A record without a `shared` part is parsed by the same code as
  before. Records are not rewritten, unless the owner runs the new `review_store.py share --write`.
- **New records over 1 MiB are deduplicated.** Each JSON subtree of at least 80 characters that the record's
  sections repeat is stored once, in a `shared` part. A reference `{"$shared": "<16 hex>"}` takes its place.
- **Byte identity is checked twice when a record is written.** `_share` expands its own output and falls back
  to the plain form unless it is identical. Then `ingest` checks, as it already does, that the view reproduces
  the log byte for byte.
- **Ruling and carry keys cannot change.** Each is computed from the view text, which is identical. The record
  sha hashes the pass identity, not the file content.
- **Expected size of f8889:** 74.9 MB becomes about 70 to 110 KB (*inferred* from measured parts, see 4.3).
- **Check tier: fast** (checked).
- **The blob guard:** after this patch and the xint push, `tools/large_blobs.txt` has no foreseeable entry. I
  recommend dropping it from tooling-1 and keeping the 50 MiB guard itself (section 6).

## 1. Design

### 1.1 Where the encoding lives (checked)

- All record access goes through `review_store.parse_record`:
  - `load_record` (xint review_store.py:281) and nothing else reads `reviews/store/` files. A repo-wide grep for
    `parse_record|load_record|record_path|store_dir|reviews/store` outside review_store.py finds only
    test_review_tools.py:3662 and a prose line in rename_carry.py:52.
  - `rulings.read_log` returns `review_store.view` (rulings.py:55-64).
  - triage.py:51/73/103/152/259, rule.py:66/119/211, year_carry.py:620 and carry.py:687/724 all read the log
    through `read_log` or `review_store.view`.
- So decoding inside `parse_record` makes the change invisible above the store.
- Encoding inside `write_record` means only new records change form.

### 1.2 The record format

A shared record is an ordinary record. It has one extra part, at the end, after `raw`:

```
<!-- part shared -->
3f2a9c0d1e4b5a67 {"args": [{"line": "1"}, {"input": "f8889.coverage_changed"}], "test": "all"}
9b1c...          {"guard": {"$shared": "3f2a9c0d1e4b5a67"}, "then": {...}}
<!-- end -->
```

- Each line has the form `<id> <text>`.
  - `<text>` is the subtree's canonical JSON (`transcribe.canonical`: sorted keys, `ensure_ascii=False`,
    default separators). Its own shared children appear as `{"$shared": "<id>"}`.
  - `<id>` is the first 16 hex characters of the sha256 of `<text>`. That makes it a Merkle id: it is
    deterministic, and the same subtree gets the same id in every record.
  - Lines are in post-order: every child is listed before its parents. The decoder refuses a line that names
    an id not yet listed, a repeated id or a malformed id. A cycle is therefore impossible.
- In the sections, each eligible ```` ```json ```` line has the same rewriting.
  - A line is eligible when it is a single line that `json.loads` parses and whose canonical dump equals it.
  - `None` and `<unparseable: …>` sides, and any non-canonical block, stay exactly as written.

### 1.3 Encoder (`_share`, b/review_store.py:297)

1. It acts only when the parts total more than `SHARED_MIN_BYTES` (1 MiB) characters.
2. If any section text already contains `"$shared"`, the record is stored plain, because a reference could
   not be told apart from the text. This is checked; no current record contains it (4.3).
3. It parses one block at a time and hash-conses it into a `_Forest`. Equal subtrees get one id. Sizes are
   computed bottom-up from the children's sizes, and occurrences are counted in the expanded trees. The walk
   is iterative, because the trees are deep. Each parsed tree is dropped after it is added, so peak memory is
   the largest single block plus the distinct nodes.
4. A node is shared when it occurs at least twice and its canonical text is at least `SHARED_MIN_CHARS` (80)
   characters long. Placeholders are 31 characters, the same threshold tooling.md C.2 measured with.
5. It builds texts in id order, which is children first. A child that occurs once has its text freed after
   its parent consumes it.
6. It verifies: `_unshare(out)` must equal the input parts in name, order and text. Otherwise it prints a
   warning and returns the plain parts.

### 1.4 Decoder (`_unshare`, b/review_store.py:357)

- It splits each shared text on the reference regex once.
- It expands the section texts iteratively into a list of pieces and joins them, in time linear in the output.
- It does not build a table of fully expanded subtrees. On f8889, that table could be several times 75 MB,
  because the 39.8 MB expression's children would be materialised again.
- Only `section *` parts are expanded. `head`, `raw`, `block` and `gate` parts are untouched.

### 1.5 `write_record` and immutability

- The file content is `_compose(sha, ident, _share(parts))`.
- When a file already exists under that sha, `write_record` compares the plain composition of its decoded
  parts with the plain composition of the new parts. It is equal in three cases:
  - an old plain record and a new shared one;
  - two shared ones;
  - the record unchanged.
  In all three it returns without writing. Otherwise it raises `never rewritten`, exactly as before. The
  existing test `test_a_record_stored_with_other_content_is_refused` still holds.
- `shared` is a reserved part name. Today's part names are `head`, `raw`, `block`, `section …` and `gate …`.

### 1.6 `review_store.py share [--write]` (optional, owner decision)

- It reports, for every record over 1 MiB that is stored plain, the size its shared form would have.
- With `--write` it rewrites the record, after `parse_record(new) == parse_record(old)`.
- The identity, name and decoded parts are unchanged. Only the bytes on disk change.
- This is the one place the patch rewrites a stored file. "Records are never rewritten" has so far meant
  never rewritten with other content, and this rewrite keeps the content. It is still the owner's call.
  Without `--write` nothing is written.

### 1.7 Hunks

| File | What |
|---|---|
| tools/transcription/review_store.py | Module docstring paragraph; usage line for `share`. New block "shared subtrees": constants, `_dump`, `_Forest`, `_share`, `_unshare`, `_compose`. `write_record` uses `_compose` and `_share`, reserves `shared` and compares decoded content. `parse_record` decodes. New `share()` command and its subparser |
| tools/transcription/test_review_tools.py | 4 tests in `ReviewStore` (3723-3790 in b/), described in 3.1 |
| tools/transcription/README.md | One paragraph after "`review_store.py check` verifies every index's records." |

## 2. Why the keys cannot change (checked against code)

- **Rulings keys.**
  - `rulings.stored_key` (rulings.py:89-108) is the sha256 of each expression's text as the log section embeds
    it. That text comes from `log_sections(read_log(...))` (rulings.py:375-386), and `read_log` is the view.
  - The view is assembled from `parse_record` output (`view_of`, review_store.py:377-393), which is decoded
    and identical.
  - `_sections` (transcribe.py:2184-2199) computes the key it looks up from `r["project"]` and `r["second"]`,
    which are in memory and untouched.
- **Carry keys.**
  - carry.py:410 canonicalises `json.loads(s)` of the view's text.
  - carry.py:687 reads `review_store.view(..., read=_reader(rev))` for other revisions. `_reader` returns the
    file text, and `parse_record` decodes it. Old revisions are plain and decode as before.
- **Triage stamps.** triage.py:259 stores `log_sha256_at_triage` = sha256 of `read_log(...)`. The view is the
  same bytes, so the stamp is unchanged.
- **Index keys.** `subject_key` and the line subjects (review_store.py:114-118; subjects.py) never read record
  content.
- **Record names.** A record's name is `_sha(ident)` (review_store.py:232), the identity and not the bytes.
  `check()` verifies `_sha(ident) == name` (review_store.py:659), and `ident` is not encoded.
- **What the brief's "computed on the expanded text" amounts to here.** There is no unexpanded text above the
  store. Nothing could hash the encoded form except a tool reading `reviews/store/*.md` directly, and the grep
  in 1.1 found none.
- **The guard against a decoder bug landing silently.** `ingest` already refuses to write an index whose view
  is not the log byte for byte (review_store.py:544-547). `_share` adds its own check before that.

## 3. Test plan

### 3.1 Unit tests in the patch (run by the `review_tools` self-test, tools/self_tests.py:27)

1. **`test_a_large_record_stores_repeated_subtrees_once_and_reads_back_as_written`.** `SHARED_MIN_BYTES` is
   patched to 0, and a log is written whose two sides repeat a 140-character subtree that holds an
   89-character guard. The test asserts:
   - `read_log` is the log;
   - the record has a `shared` part and no copy of the expanded subtree;
   - there are exactly 5 references: 4 uses of BIG and 1 of its guard. I counted this with
     `scratch/round4-store-dedup/sanity_synthetic.py` on the b/ code, synthetic data only. Its output was
     "test-1 refs: 5", and 89 for the guard, 64 for the args list, which is below 80 and so not shared;
   - the rulings key from the view equals `stored_key(("2", side1, side2))`;
   - a ruling rewrites only the index;
   - `check()` is 0.
2. **`test_a_record_stored_unshared_is_read_and_kept_as_it_is`.**
   - A record is written plain. With the threshold then at 0, `write_record` of the same parts returns the sha
     and leaves the file unchanged, and altered parts still raise `never rewritten`.
   - `share()` reports 1 and writes nothing. `share(write=True)` stores the shared form, after which
     `read_log` is unchanged and `check()` is 0.
   - Shrinkage is confirmed by the sanity script: 1,188 → 950 characters for this small fixture.
3. **`test_text_that_could_be_read_as_a_reference_is_stored_unshared`.**
   - A section holding a literal `{"$shared": …}` is returned unshared (`assertIs`).
   - A non-canonical side (compact separators) is kept verbatim, while the other side's repeats are still
     shared and decode back exactly.
4. **`test_a_shared_part_naming_a_later_or_missing_subtree_is_refused`.**
   - Each of these raises ValueError: a forward reference, a self reference, a duplicate id, and a section
     naming an absent id.
   - `write_record` refuses a part named `shared`.

Not run tonight. COMMON forbids test suites. The only thing I executed is `sanity_synthetic.py`, which loads the
b/ copy with stubbed imports on in-memory synthetic data. It printed `ok`. It also showed a 16-level
exponential tree of 17,826,385 characters shrinking to 5,491, with `None`/`<unparseable>` sections unchanged.

### 3.2 Round-trip every existing record (read only): `scratch/round4-store-dedup/roundtrip_store.py`

Written, **not run**. Run it in a checkout with the patch applied:

```
python3 .claude/nightplan-2026-11-16/nightplan/scratch/round4-store-dedup/roundtrip_store.py --repo . [--all] [--views]
```

For every `reviews/store/<kind>/*.md`, it:
- parses the record as stored (the old path, since no record has a `shared` part);
- asserts the plain recomposition equals the file byte for byte;
- builds the shared form in memory, parses it back, and asserts the identity and parts are equal;
- prints the stored and shared bytes, the number of subtrees and the seconds taken.

`--all` sets the threshold to 0, so all 287 transcription records, and the render and class M records,
exercise the encoder. `--views` also compares every index's view under the patched reader with HEAD's reader,
including the ruling keys. On an unshared store that only shows the plain path is unchanged.

It writes nothing in the repository, and one temporary copy of HEAD's review_store.py under `$TMPDIR`.

**Cost:** the whole store is about 180 MB, f8889 alone 75 MB, so this is CPU-heavy (*inferred*: about 1 to 2
minutes, and a peak of 1 to 2 GB on the 39.8 MB block). Run it only when no release-gating check is running.

### 3.3 End-to-end proof on the shared path (a throwaway clone)

In a worktree made with `tools/worktree_data.py clone`, never in main:

1. Run `review_store.py render`, then copy `.transcription/logs/` to `before/`.
2. Run `review_store.py share --write`. It rewrites only the records over 1 MiB, 12 in xint.
3. Run `review_store.py render` again, then `diff -r before/ .transcription/logs/`. Expect no output.
4. `review_store.py check`, `rulings.py --check` and `check_logs.py` (both jurisdictions) must give the same
   results as before.
5. Run `carry.py` dry runs on f8889, eic and household, and expect the same output.

### 3.4 Expected sizes (measured parts; totals inferred)

Measured read-only in xint, with a string scan only and no JSON parse. "Rest" is everything outside the
```` ```json ```` lines:

| Record | Form | Now (bytes) | JSON lines | Rest | Expected shared size |
|---|---|---|---|---|---|
| e3b28879 (staged in xint) | f8889 | 74,857,551 | 24 blocks, 74,815,535 chars | 42,016 | about 70-110 KB |
| 789d33fd | eic | 23,779,355 | 34 blocks | 48,968 | under about 150 KB |
| 6dafaa10 | household | 11,968,943 | 4 blocks | 9,163 | under about 100 KB |
| 681888e6 | household | 10,811,501 | 8 | 13,761 | under about 100 KB |
| 7dcc19a4 | dependent | 8,899,204 | 46 | 50,828 | under about 150 KB |
| 642f5afe | s2 | 6,075,454 | 4 | 38,011 | under about 100 KB |

- The f8889 figure is the measured rest, plus tooling.md C.2's measured 28,578 bytes of distinct subtrees of
  at least 80 characters, plus reference overhead.
- The others assume the same pattern, helper expansion repeating guard subtrees. That is *inferred*, not
  measured. The round-trip script prints the real values.
- None of the records contains `"$shared"`, so none would fall back (checked by the same scan).
- 12 records in xint are over 1 MiB and 30 are over 256 KiB (`find -size`).

## 4. Check tier

- **fast** (checked).
- The changed paths are tools/transcription/review_store.py, test_review_tools.py and README.md.
  - None matches tools/full_paths.txt (engine/src/mutate*.ts, engine/src/compare.ts, lean/*, tools/engines/*,
    fixtures/*/differential/engine_investigations.json, tools/step_output.py).
  - None matches docs_paths.txt, whose `docs/*` is the root docs directory.
- Under the review rules it is a tool change that applies prospectively. It changes no subject, prompt or
  key, so it makes no review due (CLAUDE.md, "Inference cost").
- The steps that exercise it are `review_store` (check_all_steps.sh:216, both jurisdictions), `check_logs` and
  the `review_tools` self-test. All are in the fast tier.

## 5. Interaction with the 50 MiB blob guard (patches/v2/tooling-1.patch)

- **What tooling-1 does (checked).** It refuses, in pre-commit and pre-push, a blob over 52,428,800 bytes that
  the commit or push adds. A blob already on the remote is never read again. `tools/large_blobs.txt` is an
  allowlist by blob id, empty in the patch.
- **After store-dedup, no new record comes near 50 MiB.** The non-JSON rest of the largest records is 51 KB or
  less (measured). The JSON shrinks to the distinct content. Size is then linear in the distinct content, not
  in the exponential expansion.
  - A record could still exceed the limit only through a non-canonical or unparseable JSON side, or a
    50 MiB raw reply. Neither occurs today (inferred from the scan above).
- **The only blob that needs an allowlist entry is xint's staged e3b28879 (74.9 MB).**
  - tooling-1.md already recommends landing tooling-1 after the xint push (option a). In that order the blob
    is on the remote before the guard exists and never needs an entry.
  - The older large records are already on origin/main: 43fe6dd0, e007c1c7 and 4136f37d are in
    acde74b5's history. I checked e007c1c7 and 4136f37d with `git log --all`.
  - Alternatively, store-dedup could land first and `share --write` be run on e3b28879 before xint is
    committed. But that changes a tree the release-gating check has just verified, so it needs a new green
    run. That is not worth it, since 74.9 MB is below GitHub's 100 MiB hard limit.
- **Recommendation.**
  - Keep the guard as a backstop, because it is cheap.
  - **Drop `tools/large_blobs.txt`**, with its two test cases and the README sentence. With dedup in place it
    would only ever hold a blob that should instead be fixed at the writer. A deliberate one-off can use
    `git push --no-verify` with the owner's approval.
  - If the owner prefers to keep the escape hatch, it costs little. It is not *needed*.
  - Owner decision; see Questions.
- **Order.**
  1. Push xint (with e3b28879 as it is).
  2. Land store-dedup.
  3. Land tooling-1, with or without large_blobs.txt.
  4. Optionally run `share --write` on main's existing large records in a later commit, with the 3.3 proof.

  Step 4 shrinks the working tree and lane clones, about 140 MB less across the 12 records (*inferred*). It
  cannot shrink history.

## 6. Risks and limits

- **Write cost.** Encoding f8889 parses 75 MB of JSON, dumps it once to check that it is canonical, walks
  millions of nodes, and expands once to verify. *Inferred:* tens of seconds and 1 to 2 GB peak, about
  what transcribe.py already used to build the same strings. It is paid once per record, after a paid review.
  I did not time it on real data.
- **Read cost is unchanged.** The view is still the full 75 MB string, and so is the view written to
  `.transcription/logs/` (git-ignored). The Expander's `pa == sb` over 40 MB strings is untouched.
  - Comparing root hashes there (tooling.md C.4, *inferred* idea) is a separate change to transcribe.py.
  - Memoising `Expander.expr` per (line, bindings) is another option, outside this patch.
- **Readability of the record file.** A shared record's DISAGREE sections show references, not the
  expressions. People read the generated view (README; review_store.py docstring), not record files, and
  records under 1 MiB stay plain.
- **Placement of the shared part.** It is last, so head and sections still read at the top. The decoder does
  not depend on position.
- **Unverified.** None of the four unit tests has been run, nor the round-trip script, nor the 3.3 proof.
  Only the synthetic sanity script ran. Python compatibility: the code uses nothing newer than 3.8.

## Questions for the owner

1. **The sharing threshold.** Records over 1 MiB are shared and smaller ones stay plain, which keeps them
   readable. The largest plain record would then be about 1 MiB. Should it be 0, so every record with a
   repeat is shared, or keep 1 MiB?
2. **`share --write` on existing records.** It rewrites the bytes of records over 1 MiB, with the same
   identity and decoded parts, verified. Allowed after the 3.3 proof, or should old records stay
   byte-for-byte as committed?
3. **`tools/large_blobs.txt` in tooling-1.** Drop it (recommended: no foreseeable entry once dedup lands and
   xint is pushed first), or keep it as an empty escape hatch?

## Provenance

- **Inspected:**
  - xint tools/transcription/review_store.py (whole file);
  - transcribe.py:1360-1445 (Expander), 1580-1690 (canonical and the comparison loop), 2150-2215
    (`_sections`);
  - rulings.py:1-140 and 340-400;
  - grep of triage.py, carry.py, rule.py and year_carry.py for how they read logs;
  - test_review_tools.py:3580-3714;
  - tools/full_paths.txt, docs_paths.txt, check_all_steps.sh:69 and :216, self_tests.py:27;
  - the review store design doc;
  - tooling.md C and patches/v2/tooling-1.patch and tooling.md;
  - a string scan of the 8 largest xint records;
  - `git log --all` for e007c1c7 and 4136f37d;
  - `git apply --check` on xint and main (both pass);
  - the sanity script's output on the b/ code with synthetic data.
- **Inferred (unverified):**
  - the shared sizes of real records;
  - the write-time cost;
  - that the 4 unit tests pass (written against the code, not run);
  - that no tool outside the grep reads record files by another route;
  - the about 140 MB saving from `share --write`.
- **Plausible gap:** a reader that runs `git show <rev>:reviews/store/...` itself, without
  `review_store._reader`. The grep found no `reviews/store` path in tools/ other than the ones listed, but a
  path assembled from fragments would not be found. The round-trip and 3.3 proofs would expose it only if
  that reader is among the steps run.
