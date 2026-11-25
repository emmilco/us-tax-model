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

## 5. What remains blocked on the IRS (as lane ty26 left it; section 6 updates it)

Every gating document: the 2026 Form 1040 instructions above all (most of the 83 unsourced parameters, C-PEOP-23,
the Tax Table, EIC tables and refund worksheet), then the Schedule A, Schedule D, Form 8949, Form 8995-A and Form 4562
instructions and Publications 463, 501, 526, 560, 946 and 970; the finals of the 69 drafts (129 operation entries and
82 parameters rest on them); the final Schedule 3-A and Form 1062 instructions. Not blocked on the IRS, and to do
before adoption: BUG-1407 to -04, BUG-0644 (class M pricing), the s2 and carloan re-citations (section 3).

## 6. Lane ty26b (batch 3): the defects fixed and the rehearsal rerun with no workaround

Lane ty26b of the same wave (claude-opus-5-5, judgment; year 2026, jurisdiction us), branch `lane-ty26b` from `next`
6b3a9a03. No paid review, no model call. Pending entries `BUG-1441` to `-07`.

**Fixed** [M]:

- BUG-1407: `year_diff.py` applies the year label rule only to the year members of an enum (`realty_year`'s
  `before1987` keeps its label); self-test case added.
- BUG-1408: `changes/2026/person.edu.yaml` removes `person.edu_tin_missing` with its reader (operation edit
  authorized by the coordinator).
- BUG-1409: the build's reader check counts as read, for a year with no `forms/ny/<year>/`, the federal lines the
  latest earlier New York year's forms read, and names them in its output (`engine/src/build.ts` `nyReadIds`).
- BUG-1410: `fixtures_year.py` answers, in the cases that take no defaults, the from-year inputs the year newly reads
  (the input an expectation known in 2025 now waits on), and names the refusing gates of an expectation the year's own
  refusals no longer reach.
- New (BUG-1446): the 2026 operations removed `person.x_tax`, and with it the two Roth IRA refusals batch 2
  added there (BUG-1154); they move to `person.x_tax_excess` with the 2026 amounts. `year_changes.py --check` now
  fails on a helper or gate line the operations leave with no reader, which found exactly these two (and would have
  found BUG-1408).
- BUG-0644's remaining effect (class M unpriced): `engine/src/generate.ts` fits a generated return to a year other
  than 2025 (answers to undeclared inputs dropped, enum answers no longer listed set to the enumeration's first value:
  `f5695.any`, `bonus_choice: forty`); 2025 is unchanged.
- Citations: the 22 Schedule 2 AMT citations of Form 6251 itself (the 20 of section 3, `s2.amt_l19` and `s2.amt_l25`)
  and `s2.amt_part3`'s Form 6251 segment are requoted from the 2026 draft (`changes/2026/s2.f6251.yaml`, C-LAW-02);
  every citation of the proposed car loan regulations (20 cites, 3 locator mentions, the form note, the `carloan_kind`
  enum, two register entries) moves to the final regulations (`changes/2026/carloan.regs.yaml`, new change-map entry
  C-SCHED-40; `build_params.py`). In a scratch adoption of the final tree, `citations.py --strict --year 2026` reports no
  finding on `f6251` or `fr-2026-18219`, and nothing in the adopted 2026 tree cites `fr-2025-24154`.
- BUG-0734: decided under the owner's delegation and registered as `amb.2026.carloan_heir_original_use` (line 28(1)
  prints Yes for a loan taken over at a death; the tax is the same either way); to recheck against the 2026 Form 1040
  instructions.

A 2025 defect found on the way (BUG-1441): the final car loan regulations apply from 2025 and count
credit insurance products and GAP as qualifying; `carloan.nonqualifying`'s question says "insurance". Not fixed here
(forms/2025 belongs to other lanes).

**Rehearsal** [M]: `tools/year_rehearse.sh --dest /tmp/ty26b-reh --stand-in-sources` under `nice -n 10` (the second
run with `--reuse-build`), with no change to the copy. The only stand-in is the script's own: the 39 cited documents
with no 2026 edition copied from 2025 (unpublished; `fr-2025-24154` among them in that run, cited only by the
`carloan_kind` enum, which the staged parameters now re-cite).

| Step | Outcome |
|---|---|
| `year_diff.py --adopt` | rc 0: no stand-in needed (BUG-1407 fixed) |
| `citations.py --strict` | 1,263 findings, as expected before adoption's review (i8962 377, i8889 95, i8863 84, p525 79, i8582 72, ...); after the last operations (scratch copy) 1,257, none on f6251 or fr-2026-18219 |
| build 2026 | fails only on the cited documents not archived for 2026; with them stood in, build OK (the three New York-read lines named) |
| `fixtures_year.py --no-hand-work` | 321 kept, 2,082 re-recorded, 371 not evaluated (365 stating a removed input, 6 rejected); 3,631 new-input answers in 549 cases; 15 answers to newly read 2025 inputs in 11 cases (`person.work_ssn` 10, `person.born_jan1` 3, `dependent.work_ssn` 2); 3 expectations known to unknown (was 86) |
| `test-fixtures --year 2026` | 2,400 of 2,403 pass; the 3 failures are classm.tcw.9, .11, .15, each refused in 2026 before line 15 (`f1040.gate.itemized_limit`, `f1040.gate.nonitemizer_gifts`), to re-derive when the Schedule A and Form 1040 instructions post |
| `year_carry.py` (dry) | transcription 272 lines carry, 1,520 to review; render 338 and 1,693; class M 285 and 7,400 |
| `year_carry.py --write` | rc 0 (25 min) |
| `check_logs.py` | rc 1 as designed before reviews (transcription 3 of 82 forms satisfied, render 4 of 82, class M 6 of 73) |
| `rerun_all.py --dry-run` | in the run: $142.64 for 153 jobs, class M not priced (the generator still drew `bonus_choice: forty`, which 2026 drops); rerun in the same copy with the final `generate.ts`: **$240.22 for 215 jobs**, class M priced (about $97.58); 13 jobs not run (their logs answer); 6 not built: transcription dependent and f8889 (their input-contract banks, carried from 2025, pin the 2025 text of i2441, p503, i8889 and f8889: to re-pin at adoption after their cases are rechecked) and class M carloan, otjob, scveh and tipjob (classm-jobs selects no case on the interview's route for them in 2026; not traced) |

[I] The estimate is a lower bound for the forms citing the 39 stood-in documents and assumes today's drafts.

## 7. What still blocks adoption

Only IRS documents: the 2026 Form 1040 instructions (most of the 83 unsourced parameters, C-PEOP-23, the Tax Table,
EIC tables, refund worksheet, line 28(1) for heirs), the Schedule A, Schedule D, Form 8949, Form 8995-A and Form 4562
instructions, Publications 463, 501, 526, 560, 946 and 970, the finals of the 69 drafts (130 operation entries and 82
parameters rest on them), the final Schedule 3-A and Form 1062 instructions. Then the adoption's own work
(ADOPTION.md steps 1 to 9): the review rounds and the citation findings above.
