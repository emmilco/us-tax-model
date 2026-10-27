# TY2026 adoption rehearsal: tool defects

Integrity plan item 2.1 (plan revision C3). This rehearsal adopted TY2026 on the IRS's posted drafts, as of 2026-10-27:
`tools/sources-2026.json` lists 57 drafts, archived in `sources/2026/` with the draft flag. It then ran
`year_diff.py --from 2025 --to 2026 --adopt` and `fixtures_year.py`, and checked the suite on both years. 2026 is not in
`years.json`.

Draft selection: every PDF in `tools/sources-2025.json` whose current entry on irs.gov/draft-tax-forms is labelled
"2026" or "Dec 2026". Left out: `p505-2026`, whose 2026 edition is already final and archived in `sources/2025`; drafts
labelled for an earlier year (for example `i1040gi`, `i1040sca`, `i1040sd`, `i8949`, `i4562` and `p946`, whose only
drafts are 2025); and drafts labelled for 2027 (`fw2`, `f1099div`, `i1099div`, `f1099r`, `i1098et`, `p15`). There is
no 2026 draft of the Form 1040 instructions or the Schedule A instructions. Each archived draft's revision records its
posted date and the 2026 printed after the IRS cover page. The drafts print no "draft as of" date.

Reports: `year_diff_from_2025.md` (after `--adopt`, the 2026 citations), `year_literals_from_2025.json`,
`fixtures_from_2025.md` (a plan; see F6).

## Fixed in this rehearsal

**F1. No way to mark a draft; spec 7 not enforced** (`tools/fetch_sources.py`).
Before: a catalog row has only `id` and `url`, the fetcher records every document the same way, and nothing stops an
adopted year from resting on drafts.
Fix: draft rows carry `"draft": true`, `draft_edition` and `draft_posted`, and these are copied into the manifest. A
`/pub/irs-dft/` address without the flag, or the flag without that address, is refused. The offline check fails when
an adopted year's archive holds a draft, and `revision_status` names the draft.
Test: `fetch_sources.py --self-test` (added to check-all). Gate reproduction: run `fetch_sources.main()` with
`adopted_years` patched to `[2025, 2026]`; it exits naming the 57 drafts.

**F2. Draft cover page and watermarks read as IRS text** (`tools/citations.py` `Archive`, `tools/year_diff.py`).
Every draft has a cover notice on page 1 ("Caution: DRAFT—NOT FOR FILING") and watermarks on every page ("TREASURY/IRS
AND OMB USE ONLY DRAFT", "DRAFT — DO NOT FILE") that join the neighbouring sentence.
Reproduction (before the fix): run the 2025 to 2026 year diff and strip the watermark from each 2026 counterpart
sentence. 500 sentences of 2025 text were marked changed only because of the watermark, across 44 documents
(i1116 47, iw2w3 50, i1099r 36, ...). A quote that spans a watermark also fails to match after `--adopt`.
Fix: `Archive.read` removes the watermarks of a manifest entry flagged as a draft and empties its cover page, keeping
the PDF's page numbers. `year_diff` reads through it.
Test: year-diff self-test "as an IRS draft with watermarks" (3 items flagged without the fix, none with it).

**F3. `citations.py --relocate` rewrote the wrong page list** (`_rewrite`).
When one locator had several segments folded over several rows, each edit replaced the first matching number on a
row, with no context.
Reproduction (before the fix): `--adopt` turned `forms/2026/f8880.yaml:608` "p. 1, Caution; p. 2, Credit Limit
Worksheet" into "p. 3, Caution; p. 2, …", because the second edit (2 to 3) hit the "2" the first edit had just
written. The correct result is p. 2 and p. 3. It also left `s1.yaml:652` and `sc.yaml:694` as "could not rewrite;
edit by hand". In the new test case it changed "Lines 1 and 2", inside an anchor, to "Lines 1 and 3".
Fix: the scalar is found by its YAML marks, the parsed locator is walked against the text as written (folds, doubled
quotes), and each page list is replaced at its own offset, last to first.
Test: citations self-test "rewriting folded multi-segment locators" (fails on the old function).

**F4. After `--adopt`, a changed dollar parameter could drop off the worklist** (`year_diff.run`).
The value check fires only when the data year's text prints the value in a changed sentence. After adopting, the data
year is 2026 and the value is still the 2025 one. A value that changed is then not printed at all, so nothing fires.
Reproduction (before the fix): of the 36 parameters with a value finding before adopting, 16 lost it after adopting.
Four of those (`dc.exclusion_max`, `qbi.threshold`, `hsa.self_only_55`, `hsa.family_55`) left the worklist altogether,
and `fixtures_year.py` reads that worklist.
Fix: a value finding is also made when the value is printed on the other year's counterpart pages and nowhere on the
cited pages.

**F5. A quote naming the from-year matched neither year after `--adopt`** (`year_diff.run`).
A quote such as "If you were age 55 or older at the end of 2025, enter $5,300" was compared unshifted with the 2026
text, and with the 2025 text after its years had been moved to 2026. It matched neither side, so no finding was made
in either direction.
Fix: each quote is compared as written and with its years moved to the data year's.
Test (F4 and F5): year-diff self-test "as after --adopt" (value and quote both MISSED without the fixes). The quote
case is skipped, with a message, for a carried year whose quotes name the earlier year.
After both fixes: the pre-adopt and post-adopt worklists agree (1,845 and 1,851 items), and no pre-adopt value finding
is lost.

**F6. `fixtures_year.py` crashed on a year that does not build, and hid why.**
Before: `CalledProcessError` traceback, with the build output sent to DEVNULL.
Fix: it exits with the build's error count and first errors (4,511 for 2026). New `--plan` mode: it evaluates each
case on the from-year's data, lists the cases whose derivation rests on the to-year worklist as "would be
re-recorded", and writes no fixtures. The tool has no self-test; the change was checked by running it.

## Fixed after the rehearsal (O1 to O7)

All counts below were taken in a worktree, by regenerating the 2026 tree with `year_diff.py --from 2025 --to 2026
--adopt` once with the old tools and once with the new ones. The tree was not committed.

**O1. Relocation put some segments one page too far, and the check passed them** (`citations.place`, `plan`).
Before: a segment moved by the most common shift among the five nearest quotes. The move was accepted when the heading
was "in force", meaning printed up to two pages before the new page. Near a page the 2026 draft inserted, i1040sc's
evidence mixes +1 and +2, so `sc.yaml` Lines 25, 26, 27a and 30 went to p. 12. The heading is printed on 2025 p. 10 and
2026 p. 11.
Measure: a segment that passes the 2026 check, but whose heading stands weaker there than on its 2025 page (printed
there, only in force on the new page). The old tools left 15 (i1040sc 11, p4681 3, i8995 1). The new tools leave 0.
Fix, in relocation, not in the check. The check sees one year. It cannot tell a misplaced segment from the 32 2025
segments that rightly cite a page with only a heading in force. Relocation knows the old page. Now:
(a) A move may not weaken how the anchor stood on the from-year page: printed on the first page, printed on another
cited page, or only in force. `--relocate --from <year>` reads that from the from-year archive, and `--adopt` passes
`--from`.
(b) Every shift among the nearest evidence is tried, plus the shift of the nearest evidence on each side. Exactly one
distinct fitting placement is accepted. Two or more are left for review.
(c) A segment with only a heading, beyond the evidence on one side, also tries the neighbouring shifts, so a heading
printed on several pages (`box 1`) is not placed by extrapolation.
(d) Segments still unplaced are tried again with the shifts of the other unplaced segments.
Result: 623 moved, 379 left for review (before: 544 and 461). Citation findings are 534 (the old tree under the same
check: 540). 14 segments left for review still pass the check on their 2025 page numbers, for example i1040sc
"Line 17" on p. 8, printed on 2026 pp. 8 and 9. The check cannot report these, so relocation now writes
`reports/<year>/relocation_from_<from>.md` and marks each one "the check passes it unmoved".
Test: citations self-test "a page inserted mid-document (+1, then +2)". The old logic places 31 segments elsewhere; the
new logic places none.

**O2. `--relocate` was not idempotent.**
Cause: on a second run, the segments left for review still carry 2025 pages. Their quotes taught a +1 shift that the
in-force rule let a correct segment take (f8880 "Caution", p. 2 to p. 3).
Fix: without `--from`, a segment the check passes stays where it is. Shifts are learnt only from the segments that do
not pass. The in-run retry (O1 (d)) makes one run reach that fixed point.
Result: a second `--relocate --year 2026` moves nothing (648 in place, 0 moved). `f8880.yaml:608` stays on p. 2.
Test: citations self-test "relocated again, half the evidence a page early". The old logic places 572 segments
elsewhere; the new logic places none. The self-test now takes as its answers only the segments the check passes where
they stand, so `--self-test --year 2026` passes.

**O3. No shift was learnt for a document without single-page quotes.**
Fix: a document with no quote evidence takes the cover-page shift: +1 when the to-year archive is a draft with a cover
page and the from-year archive is not (`Archive.has_cover`). The shift is used only where every quote fits and the
anchor keeps its standing. f4952's 39 segments now go to "pp. 2, 4, 5". So do i1040sb, i1116, i8960, f8995a and i7206
segments that were left for review before.
Test: citations self-test "a draft cover page added to f4952". f4952 is archived again with a cover page. The old
logic moves 0 of 39 segments by one page; the new logic moves all 39.

**O4. Year-specific checkers crashed when a source was missing.**
Fix: `check_macrs_tables.py` and `check_auto_limits.py` take the year for paths only. A year without the table has
nothing to check (exit 0). A year whose table exists, but whose source edition is not archived, fails naming the
missing files, for example "no 2026 edition of the Instructions for Form 4562 is archived (sources/2026/i4562.txt)". An
unverifiable table should not pass `check-all` silently, so this fails rather than skips.
Test: `--self-test` in each, added to check-all, runs the check against an empty archive. Before, it raised
FileNotFoundError.

**O5. Other readers of archived text did not strip draft marks.**
Fix: new `tools/archive_text.py` holds the single implementation (`drop_draft_marks`, `read`, `read_file`,
`has_cover`). `citations.Archive` uses it, and so does `year_diff` through it. These now read through it:
`check_macrs_tables.py`, `check_auto_limits.py`, `extract_macrs_tables.py`, `extract_class_lives.py`,
`transcription/transcribe.py` (`doc_pages`), `transcription/transcribe_tables.py` and `human_review/pages.py`.
Three readers keep the layers as extracted on purpose, because they compare the extraction with the printed page or
another extractor, and the watermark is printed: `ocr_audit.py`, `check_extraction.py` and `extraction/page_review.py`.
Not applicable: `extract_eic_table.py` and `extract_tax_table.py` read PDF word boxes, not the archived text (i1040gi
has no 2026 draft); `coverage/estimate.py` reads SOI spreadsheets. For a final edition the text read is unchanged.
Test: `archive_text.py --self-test`, in check-all, reads a planted draft without its marks. It also scans `tools/` for a
line that opens an archived text layer directly; there were 7 such reads before the change and there are 0 now. The
scan is line-based, so a path built in one place and read in another escapes it.

**O6. The value check made noisy findings for small or unchanged amounts** (`year_diff.printed`, `run`).
There were two causes. A small amount was matched as a bare number ("5" in "line 5"). And a value finding fired
whenever the sentence printing the amount changed for any reason: `sc.ho_rate` "$5 3b." against "$5 b.", or `se.floor`
"$400" in both years.
Fix: an amount under $1,000 is matched only with its dollar sign. A value finding needs the counterpart sentence not to
print the same amount.
Result: after `--adopt`, value findings drop from 17 parameters to 4. Each dropped finding had the same amount in both
years' aligned sentences (statutory amounts such as the NIIT and Medicare thresholds, `ctc.per_child` and the s1a caps).
`ftc.limit` dropped because i1116 is now relocated rather than left on 2025 pages.
Test: year-diff self-test. "The sentence printing the cited amount reworded, the amount kept" finds no value finding,
and small amounts are read only with their dollar sign. Both fail on the old code.

**O7. Extraction conservation failed on two drafts: a tool defect, not data.**
Cause: the drafts break words at line ends with a soft hyphen (U+00AD; 317 in p4681, 28 in i1120ssk, none in their
2025 editions). PDFKit reads "abandon", soft hyphen, "ments" as "abandonments". The check's tokenizer split poppler's
text into "abandon" and "ments", so PDFKit seemed to read words poppler lacked. The archived reading-order text rejoins
hard hyphens only, so it holds "can", soft hyphen, " celed". `citations.norm` deleted the soft hyphen but left the space, so quotes and the year diff saw
"can celed".
Fix: `check_extraction.py` matches a PDFKit word against a poppler head before a soft hyphen plus a tail.
`citations.norm` joins a word across a soft hyphen.
Result: 2026 extraction 0 failing (was 2). In 2025, i5329 and p561 (finals that also use soft hyphens) go from 1 and 3
PDFKit-only words to 0, so `reports/2025/extraction.md` changes. The archived text was not re-extracted. A later
`extract_text.py` change could rejoin soft hyphens at extraction, but that would change archived files and their
hashes.
Test: `check_extraction.py --self-test`, in check-all, joins soft-hyphen breaks and still finds a word only PDFKit
reads.

## Design limits seen (not defects)

- The worklist is dominated by documents with no 2026 edition: 1,611 of 1,851 items, mostly `i1040gi` with 929
  citations. In the fixtures plan, 307 of the 1,062 cases that would be re-recorded rest only on such items.
- The engine cannot build 2026: 1,600 citations name documents that are not in the 2026 archive. So the normal
  `fixtures_year.py`, the 2026 build and every check downstream of it cannot run until those documents are posted.
- `check-all --year 2026` fails as intended: build (4,511 errors, documents with no 2026 edition), citations (452
  findings in the rehearsal; 534 after the O1 to O7 fixes, 540 for the old relocation under the same check),
  check_logs and check_table_logs (no 2026 reviews), and check_macrs_tables and check_auto_limits (no 2026 i4562,
  p946, p946-html or p463, now reported by name, O4). citations_self_test and check_extraction pass.
- In a git worktree, the git-ignored `.transcription/` request contexts are absent, so `compare_families.py` shows
  `ltc`, `qdcg` and `sales` as pending. That regenerated `reports/2025/second_family.md` was restored.
