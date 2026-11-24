# TY2026 archive refresh and adoption rehearsal (2026-11-24)

Lane ty26 of the 2026-11-24 wave (claude-opus-5-5, judgment class; year 2026, jurisdiction us). 2026 is not adopted:
`years.json` is unchanged. No paid review, no model call. A record: the state it describes is that of this date.

**Labels.** [M] measured today, with the command or file. [I] inferred, not run.

## 1. Archive refresh (ADOPTION.md step 1; T-322)

What was checked [M], from public irs.gov addresses only:

- For each of the 68 catalog drafts, `irs.gov/pub/irs-pdf/<name>.pdf` (the final) and the draft address, by HTTP HEAD
  (status and Last-Modified). No final is newer than early 2026 (each is the 2025 edition) except `f1040s3a`, which
  still answers 404 (no final Schedule 3-A). Two drafts show a newer Last-Modified than their catalog date, `i8960`
  (2026-11-18) and `i1062` (2026-11-23); both were downloaded and are byte-identical (SHA-256) to the archived files,
  so neither was reposted.
- The 53 final documents of the catalog: every Last-Modified is older than its `fetched_at`; none changed.
- The twelve gating documents (`i1040gi`, `i1040sca`, `i1040sd`, `i8949`, `i8995a`, `i4562`, Publications 463, 501,
  526, 560, 946, 970) and the other 2025 catalog ids with no 2026 entry (Publications 334, 502, 504, 527, 550, 561, 587,
  974, `i1065sk1` and others): each shows only an edition dated December 2025 to March 2026 at `irs-pdf/` and
  `irs-dft/`.

**Drafts that went final since the refresh of 2026-11-22: none.** No catalog entry can therefore be set to
`verified: final`: `year_changes.py --check` names no entry whose documents are all final; 129 of its 164 entries
rest on drafts.

Added to the catalog and archived (`fetch_sources.py --year 2026 --fetch --only ...`; manifest revision fields
written):

| id | document | why |
|---|---|---|
| `f6251` | Form 6251 (2026), IRS draft, posted 2026-05-28 (draft listing), "Created 5/26/26" | the 2026 counterpart of the 2025 catalog's `f6251`, cited by the Schedule 2 AMT screen and `amt.rate_25`; it had been posted since May but was not in the catalog |
| `fr-2026-18219` | Car Loan Interest Deduction, final regulations, T.D. 10054, 91 FR 57214 (2026-09-08), GovInfo | the final counterpart of the proposed regulations `fr-2025-24154` cited by `forms/2025/carloan.yaml` |

The archive holds 123 documents, 69 of them IRS drafts (`fetch_sources.py --year 2026`).

Seen, not archived (no 2026 definition cites them): the final 2026 Form 8829 (irs-pdf, 2026-11-20); drafts of
Pub. 936 (2026-10-07), Pub. 926 (2027 edition, 2026-10-16) and the Schedule H instructions (2026-11-19).

## 2. Parameters (T-320)

No new final, so no staged value was promoted or re-derived from one. Changes [M]:

- `amt.rate_25` (Form 6251 line 37, read by `s2.amt_l37_rate` alone after C-LAW-02): 25%, from the Form 6251 draft,
  p. 3 ("Multiply line 36 by 25% (0.25)"); `source: draft`. Set in `build_params.py` and regenerated. The same draft
  prints the 2026 AMT bracket ($244,500; $122,250), the 28% subtraction ($4,890; $2,445) and the 26% and 28% rates,
  as staged from the i6251 draft.
- `propose_params.py --write --compare` and `build_params.py` rerun: four parameters added to 2025 since the last run
  now appear: `age.over59h_all_year` and `age.under59h_all_year` (derived, moved with the year) and
  `sa.gift_total_limit_rate` and `sa.gift_property_limit_rate` (no 2026 source until Pub. 526). The mechanical
  proposal's one difference is `amt.rate_25` (it reads the 2025 i6251 quote, which in 2026 is the 50% phase-out).
- Totals: 349 staged values: 168 final, 82 draft, 16 derived, 83 with no 2026 source; 15 retired.
  `check_params.py` and `check_quotes.py` pass (827 change-map quotes, 0 not printed).

**The 2026 lease inclusion threshold.** Rev. Proc. 2026-15 (final, archived since 2026-11-04 as `rp-26-15`) prints
Table 3, "DOLLAR AMOUNTS FOR PASSENGER AUTOMOBILES WITH A LEASE TERM BEGINNING IN CALENDAR YEAR 2026", whose first
row is a fair market value over $62,000 (p. 8 of the archived text). The $62,000 in the 2026 `sc.special` prompt is
therefore correct for 2026; the entry's note in `changes/2026/sc.wording.yaml` claimed no 2026 table was archived and
now cites the table (two evidence quotes added; no operation changed).

## 3. Year-change entries waiting on documents (T-328)

- None of the documents the waiting entries name has posted (section 1).
- `p590a` items: already written. The `person.sav_line1` refusal quote prints on p. 35 of the 2026 draft, the page
  the 2025 citation names; the stale note in `changes/2026/person.sav.yaml` and C-PEOP-24 in `changes.md` say so now.
- `i8962` items (C-PEOP-13 and the i8962 quotes of the f8962 lines): the draft prints Line 24 on p. 18 and Line 25 on
  p. 19 (with its cover page); at the final they should fall back to pp. 17 and 18. Not written as operations: a
  page written on a draft with a cover moves back at the final, and the relocation of `--adopt` reads the quotes then.
  The rehearsal (section 4) counts 377 citation findings on i8962 after relocation; they are the adoption's to rule.
- New items found today: the Schedule 2 AMT citations that quote the 2025 Form 6251 (20 findings once the 2026 draft
  is archived: Schedule 1-A line 37 is line 43 in 2026, and the 2026 amounts on lines 4, 7, 18, 19, 25 and 39); and
  the 20 citations of `forms/2025/carloan.yaml` on the proposed car loan regulations, 8 of whose quoted passages
  (refinancing, negative equity, the pro rata allocation) are not printed as quoted in the final regulations.

## 4. Adoption rehearsal (T-317)

`tools/year_rehearse.sh --dest /tmp/ty26-2026-11-24-reh --stand-in-sources` under `nice -n 10`, logs in
`/tmp/ty26-2026-11-24-reh/out/` (`summary.tsv`). The first run stopped at adoption (BUG-1407). The run
that reached the end was made from a scratch copy of the lane tree (`/tmp/ty26-src`, outside the repository) carrying
three stand-ins, none of them in the repository: the label rule of `year_diff.py` accepting a non-year enum member
(BUG-1407); a `remove_line` of `person.edu_tin_missing` in `changes/2026/person.edu.yaml`
(BUG-1408); a `display` reason on the three person lines read only by the New York forms
(BUG-1409); with `--reuse-build` (the 2025 build of the first run, 190 s). Results [M]:

| # | Step | rc | Outcome |
|---|---|---|---|
| 3 | `year_diff.py --adopt` | 0 (with stand-in 1; 1 without) | 3,586 of 6,316 items on the worklist; all 164 entries and 1,349 operations apply (1,348 in the repository plus the stand-in); relocation: 4,324 segments, 459 in place, 2,351 moved, 1,514 not placed |
| 4-5 | stage parameters and tables | 0 | as staged (section 2); 4 tables |
| 6 | `citations.py --strict --year 2026` | 1 | 1,203 findings (i8962 377, i8889 95, p525 79, i8863 74, i8582 74, i1116 66, i1116sb 60, i2441 53, ...; f6251 21, of which 20 are the s2 citations of section 3 and 1 was `amt.rate_25`'s anchor, since corrected); input quotes 439 checked, 86 unmatched, 3 stale |
| 7 | build 2026 | 1 | without stand-ins: the snapshot errors of the 37 cited documents not archived for 2026 and the four lines with no reader (BUG-1408, -03) |
| 9 | build 2026, sources stood in | 0 | build OK (37 documents copied from 2025, so everything after is a lower bound for the forms that cite them) |
| 10 | rebuild 2025 | 1 | only the `display` stand-in itself (the three lines are read in 2025); not a finding |
| 12 | `fixtures_year.py --no-hand-work` | 0 | 309 kept, 2,044 re-recorded, 369 marked not evaluated (363 stating a removed input, 6 rejected: `bonus_choice: forty`); 3,635 new-input answers given to 547 cases that take no defaults; 86 expectations re-recorded from known to unknown |
| 13 | `test-fixtures --year 2026` | 1 | 2,350 of 2,353 evaluated cases pass; the 369 marked cases are named and not run (rc 1 by design); 3 fail: classm.tcw.9, .11, .15 ("not evaluated") |
| 14-15 | `year_carry.py` (dry, then `--write`) | 0 | transcription 268 lines carry, 1,510 to review; render 336 carry, 1,688 to review; class M 285 carry, 7,190 to review (29 and 26 minutes) |
| 16 | `review_store.py check` | 0 | 79 indexes, 151 records |
| 17 | `check_logs.py` | 1 | as designed before reviews: transcription 3 of 82 forms satisfied, render 4 of 82, class M 6 of 73 |
| 18 | `rerun_all.py --dry-run` | 0 | transcription 76 jobs and render 77 priced, total $142.48 for 153 jobs; not priced: 68 class M jobs (classm-jobs exits on `f5695.any: input is not declared`, `engine/src/generate.ts`, the year-shared code of BUG-0644, as in R7), 2 transcription jobs (dependent, f8889: "stale input-contract source snapshot", not traced) and the jobs whose logs already answer |
| 19 | reports | 0 | year literals 4,488 lines; shared references 438 (generate_cases.py 144, generate.ts 138, mutate.ts 88, ...) |

**BUG-1275 (BUG-1040's fix) end to end.** Its regression predictions were: no class M or mutation expectation left
unknown for want of `sa.mortgage_insurance`, `person.work_ssn` or `f8962.sep_income`, and the known-to-unknown list
empty or naming other causes; `test-fixtures --year 2026` passes the 12 classm.tcw cases or lists them as marked.
Measured: the new inputs now carry. `sa.mortgage_insurance` and `f8962.sep_income` cause no unknown (BUG-1040
counted 211 and 40), and neither do `s3a.wants_benefit` or `sales.special` (8 and 10); the report lists the 3,635
default answers given. **The prediction fails for `person.work_ssn`**: the 86 known-to-unknown expectations, all in
class M files, are 61 for `person.work_ssn`, 11 `dependent.work_ssn`, 9 `person.age55_at_year_end`, 2
`person.born_jan1` and 3 with no reason. These are 2025 inputs that the 2026 operations newly read, not new inputs, so
the fix does not reach them. The report lists them, as the fix intended. Of the classm.tcw cases, 13 pass and 3 fail
"not evaluated"; BUG-1040 counted 12 failing. Filed as BUG-1410. Verdict: fixed for new inputs, not for
from-year inputs a year newly reads.

[I] The review estimate rose from R7's $88.45 (179 jobs, 2026-11-15) to $142.48 for 153 priced jobs. The forms added
by the coverage expansion since then are the likely cause; this was not broken down.

## 5. What remains blocked on the IRS

Every gating document: the 2026 Form 1040 instructions above all (most of the 83 unsourced parameters, C-PEOP-23,
the Tax Table, EIC tables and refund worksheet), then the Schedule A, Schedule D, Form 8949, Form 8995-A and Form 4562
instructions and Publications 463, 501, 526, 560, 946 and 970; the finals of the 69 drafts (129 operation entries and
82 parameters rest on them); the final Schedule 3-A and Form 1062 instructions. Not blocked on the IRS, and to do
before adoption: BUG-1407 to -04, BUG-0644 (class M pricing), the s2 and carloan re-citations (section 3).
