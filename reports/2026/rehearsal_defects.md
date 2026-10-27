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

## Open (not fixed)

**O1. Relocation places some segments one page too far** (`citations.place`, `local_shift`).
A segment is moved by the shift its neighbours' quotes suggest. It is accepted when its heading is "in force", which
means printed up to two pages earlier.
Reproduction: `rm -rf forms/2026 …; year_diff.py --from 2025 --to 2026 --adopt`. Then `sc.yaml:113` "p. 10, Lines 26
and 27a" goes to p. 12, although the heading is printed on 2025 p. 10 and 2026 p. 11.
A heuristic count over the 77 single-page moves of +2 finds 15 probable cases (i1040sc 6, i8995 6, p4681 3). Examples:
`sc.yaml` Line 25, Line 26, Line 27a and Line 30; `qbi.yaml:88` "Who Can Take the Deduction" 1 to 3; `s1.yaml:630`
"General Rules" 3 to 5.
`citations.py` (check) passes them, because the heading is in force, and the self-test's uniform shifts cannot show
it. Proposed: when the anchor was printed on the old page itself, require it on the new page.

**O2. `--relocate` is not idempotent.**
A second run moves `f8880.yaml:608` "Caution" from p. 2 to p. 3; the heading is printed on both pages.
`citations.py --self-test --year 2026` reports this as WRONG, one of that run's failures.

**O3. No shift is learnt for a document without single-page quotes.**
The draft cover moves every page by exactly 1, but Form 4952's 39 segments "p. 1, 3, 4" are left for review.
Proposed: for a draft with a cover page, try +1 and keep it where every anchor and quote fits.

**O4. Year-specific checkers crash when a source is missing.**
`check_macrs_tables.py` and `check_auto_limits.py` fail with a FileNotFoundError traceback (`sources/2026/i4562.txt`,
`p946.txt`) where they should say "no 2026 edition archived". By owner ruling these take the year for paths only.

**O5. Other readers of archived text do not strip draft marks.**
`check_macrs_tables.py`, `check_auto_limits.py`, `extract_*.py`, `transcription/transcribe.py`,
`transcription/transcribe_tables.py`, `human_review/*`, `ocr_audit.py` and `coverage/estimate.py` read
`sources/<year>/` directly. This matters only if drafts are reviewed or extracted; reading through `Archive.read`
fixes it.

**O6. The value check matches small amounts as bare numbers.**
`sc.ho_rate` ($5) is looked for as "5", which makes noisy value findings.

**O7. Extraction conservation fails on two drafts (data, not code).**
PDFKit reads words that poppler lacks on 22 pages of `p4681` and 2 of `i1120ssk` (`reports/2026/extraction.md`).
This needs checking before those drafts are relied on.

## Design limits seen (not defects)

- The worklist is dominated by documents with no 2026 edition: 1,611 of 1,851 items, mostly `i1040gi` with 929
  citations. In the fixtures plan, 307 of the 1,062 cases that would be re-recorded rest only on such items.
- The engine cannot build 2026: 1,600 citations name documents that are not in the 2026 archive. So the normal
  `fixtures_year.py`, the 2026 build and every check downstream of it cannot run until those documents are posted.
- `check-all --year 2026` fails as intended: build, citations (452 findings), check_logs, check_table_logs (no 2026
  reviews) and check_extraction (O7). It also fails for defects O1 and O2 (citations_self_test) and O4.
- In a git worktree, the git-ignored `.transcription/` request contexts are absent, so `compare_families.py` shows
  `ltc`, `qdcg` and `sales` as pending. That regenerated `reports/2025/second_family.md` was restored.
