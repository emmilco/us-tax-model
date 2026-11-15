# 2026 archive refresh, 2026-11-14

Lane S1 of the TY2026 preparation (plan decision D13; `docs/ty2026/ADOPTION.md` step 1). Previous refresh:
`reports/2026/archive_refresh_2026-11-04.md`. Sources: the public irs.gov draft-forms listing
(`irs.gov/draft-tax-forms`, all 50 pages, read 2026-11-14) and the PDFs at `irs.gov/pub/irs-pdf/` and
`irs.gov/pub/irs-dft/`. No personal data was sent. `python3 tools/fetch_sources.py --year 2026` verifies 96 documents
(57 IRS drafts); `python3 tools/check_extraction.py --year 2026` reports 96 PDFs, 0 failing checks. `years.json`
is unchanged (`[2025]`).

## 1. What was checked

- Every one of the 91 catalog documents was downloaded again from its catalog address and compared by SHA-256 with
  the manifest. 89 are byte-identical. Two drafts differ (section 3).
- Every catalog draft's posted date and edition on the draft listing was compared with the catalog. Two differ
  (the same two).
- For each of the 55 catalog drafts, the current final at `irs.gov/pub/irs-pdf/<name>.pdf` was downloaded and its
  printed year read. Three now print 2026 (section 2); the rest still print 2025 (the 2025 form, not a 2026
  final); `f1040s3a` has no final (404); `i1099int` is still the Rev. January 2024 final.
- For each id of the 2025 catalog that has no 2026 entry (section 4), the final at `irs-pdf/` (printed year,
  Last-Modified) and the draft listing were read.

## 2. New finals (3), replacing drafts

| id | final edition | superseded draft | content change |
|---|---|---|---|
| f1040s8812 | Schedule 8812 (Form 1040) 2026, Cat. No. 59761M, created 8/18/26 (PDF dated 2026-11-09) | draft posted 2026-05-19 (created 4/24/26) | text equal to the archived draft apart from draft marks and the creation date |
| f8606 | Form 8606 (2026), created 4/21/26 (PDF dated 2026-11-10) | draft posted 2026-07-16 | text equal apart from the draft cover and marks |
| i1095a | Instructions for Form 1095-A (2026), Oct 29, 2026 (PDF dated 2026-11-02) | draft posted 2026-10-13 (dated Aug 21, 2026) | wording and link-case changes only ("other than" to "that isn't", quotation marks removed from two date examples); no change to a rule that the reading found |

The draft entries and files were deleted and the finals archived under the same ids; the catalog rows carry the
superseded draft in `description`. Changes were read by word-level comparison of the archived text, not
adjudicated; the draft-sourced entries of `changes/2026/` that cite these three documents (see
`python3 tools/year_changes.py --check`: 16 of 17 entries still rest on drafts) are F2's to flip.

## 3. Drafts reposted by the IRS on 2026-11-09 (2)

| id | catalog date before | now | what changed (word comparison of the reading-order text; not adjudicated) |
|---|---|---|---|
| i5329 | 2026-09-08 (document dated Sep 4) | 2026-11-09 (document dated Nov 6) | Trump-account excess-contribution passage rewritten: the earlier "no tax on a contribution in excess of the limit if withdrawn before the beneficiary reaches age 18" is replaced by text on the 6% additional tax, excess contributions distributed by the beneficiary's tax filing deadline, and a 100% rate for the year of the distribution; a "line 5 or line 18, as appropriate" reference added; one page reference changed (57 to 59). About 15 changed spans |
| p590b | 2026-11-03 (document dated Nov 2) | 2026-11-09 (document dated Nov 6) | the "qualified long-term care distribution" exception (and its definition) removed from the early-distribution passages; a "Repayment of certain early distributions" passage added. About 58 changed spans, most of them page-break movement |

Neither was a catalog change of id: the old draft files were replaced (the manifest's hashes changed), as the
procedure requires for a reposted draft.

## 4. New 2026 drafts (5), all in the plan's gating list or the 2025-catalog list of missing documents

| id | document | posted | note |
|---|---|---|---|
| i8962 | Instructions for Form 8962 (2026), Oct 20, 2026 | 2026-11-05 | gates P3 and the C-PEOP-13 items; the 2026 poverty-guideline pattern (catalog row `fr-2025-01377`) can now be confirmed from it |
| i8582 | Instructions for Form 8582 (2026), Nov 5, 2026 | 2026-11-05 | |
| p525 | Publication 525 (2026), Nov 6, 2026 | 2026-11-06 | |
| p925 | Publication 925 (2026), Nov 6, 2026 | 2026-11-06 | |
| p590a | Publication 590-A (2026), Nov 9, 2026 | 2026-11-10 | the draft listing prints edition "2025"; the document prints "What's New for 2026" and "Publication 590-A (2026)" (IRA limit $7,500 for 2026). Catalogued as edition 2026 with that noted in `description` |

Their finals at `irs-pdf/` still print 2025 (i8962 2025 edition dated 2026-01-29, i8582 2025-12-04, p525
2026-02-26, p925 2026-02-24, p590a 2026-01-15).

## 5. Gating documents of the plan (sections 0 and 4)

| id | status 2026-11-14 | detail |
|---|---|---|
| i1040gi (+ -html) | not posted | listing shows only the 2025 edition (posted 2026-02-26); `irs-pdf` prints 2025 |
| i1040sca | not posted | 2025 only |
| i1040sd | not posted | 2025 only |
| i8949 | not posted | 2025 only |
| i8995a | not posted | 2025 only |
| i4562 | not posted | 2025 only (2025 instructions, PDF dated 2026-03-30) |
| i8962 | **draft posted 2026-11-05** | archived (section 4) |
| i8582 | **draft posted 2026-11-05** | archived |
| p946 (+ -html) | not posted | 2025 only (listing 2026-03-10) |
| p463 (+ -html) | not posted | 2025 only (listing 2026-02-27) |
| p970 | not posted | 2025 only (listing 2026-02-05) |
| p590a | **draft posted 2026-11-10** | archived (section 4) |
| p501, p526, p560 | not posted | 2025 only |
| p502, p504, p527, p550, p561, p587, p334, p969, p974, i1065sk1 | not posted | 2025 or earlier only |
| p525, p925 | **draft posted 2026-11-06** | archived |

No gating final is posted. The HTML pages (`i8959-html`, `i8960-html`, `i8995-html`, `i1116-html`, `i8283-html`,
`i8995a-html` and the others of the 2025 catalog) were not fetched: they are posted with finals, and none has a
final.

## 6. Observed but not archived (outside the 2026 catalog and outside the earlier list of missing documents)

Documents of the 2025 catalog that show a 2026 draft or a newer final on the listing, and that no 2026 catalog
row or lane scope names. Archive them if a definition comes to cite one:

- 2026 drafts: `f3800` (2026-05-06), `i3800` (2026-11-13), `f8396`, `f8801`, `i8801`, `f8839` (2026-06-08), `i8839`
  (2026-11-10), `f8859`, `f8936`, `f8936sa`, `i8936`, `f8938` and `i8938` (Dec 2026), `f8994` and `i8994` (Dec 2026),
  `f7205` (Dec 2026).
- A final newer than the 2025 catalog: `i8804` (Instructions for Forms 8804, 8805 and 8813, Rev. December 2026;
  `irs-pdf` file dated 2026-11-10).

## 7. Continuous-use revisions and guidance

The 13 continuous-use revisions of the 2026-11-04 report, `i1099int`'s final address, the nine guidance documents
(`rp-25-32`, `rp-25-19`, `n-25-67`, `rp-25-25`, `rp-26-15`, `n-26-10`, `irb26-29`, `fr-2025-01377`, `plaw-119-21`)
and the other finals are byte-identical to the archive. Not rechecked in this run: whether a new notice or revenue
procedure setting 2026 amounts was published after 2026-11-04 (no search of irs.gov news; the catalog's own
addresses were all that was compared).

## 8. Catalog after this run (96 documents, 57 drafts)

| id | state | revision | change this run |
|---|---|---|---|
| f1040 | draft | 2026 DRAFT, posted 2026-09-17 (irs.gov/draft-tax-forms) | unchanged |
| f1040s1 | draft | 2026 DRAFT, posted 2026-06-08 (irs.gov/draft-tax-forms) | unchanged |
| f1040s1a | draft | 2026 DRAFT, posted 2026-09-04 (irs.gov/draft-tax-forms) | unchanged |
| f1040s2 | draft | 2026 DRAFT, posted 2026-06-04 (irs.gov/draft-tax-forms) | unchanged |
| f1040s3 | draft | 2026 DRAFT, posted 2026-06-08 (irs.gov/draft-tax-forms) | unchanged |
| f1040s3a | draft | 2026 DRAFT, posted 2026-08-20 (irs.gov/draft-tax-forms) | unchanged |
| f1040s8812 | final | 2026; created 2026-08-18 | NEW FINAL (replaces draft) |
| f1040sa | draft | 2026 DRAFT, posted 2026-06-08 (irs.gov/draft-tax-forms) | unchanged |
| f1040sb | draft | 2026 DRAFT, posted 2026-05-20 (irs.gov/draft-tax-forms) | unchanged |
| f1040sc | final | 2026; created 2026-05-15 | unchanged |
| f1040sd | draft | 2026 DRAFT, posted 2026-05-15 (irs.gov/draft-tax-forms) | unchanged |
| f1040se | draft | 2026 DRAFT, posted 2026-05-19 (irs.gov/draft-tax-forms) | unchanged |
| f1040sse | final | 2026; created 2026-04-27 | unchanged |
| f1041sk1 | draft | 2026 DRAFT, posted 2026-06-01 (irs.gov/draft-tax-forms) | unchanged |
| f1062 | draft | Dec 2026 DRAFT, posted 2026-08-04 (irs.gov/draft-tax-forms) | unchanged |
| f1065sk1 | draft | 2026 DRAFT, posted 2026-05-21 (irs.gov/draft-tax-forms) | unchanged |
| f1095a | final | 2026; created 2026-05-12 | unchanged |
| f1098t | final | 2026 (PDF title "2026 Form 1098-T"); created 2025-10-08 | unchanged |
| f1099c | final | April 2025 (continuous-use form) | unchanged |
| f1099div | final | January 2024 (continuous-use form) | unchanged |
| f1099g | final | Rev. December 2026; created 2025-10-09 | unchanged |
| f1099int | final | January 2024 (continuous-use form) | unchanged |
| f1099r | final | 2026; created 2026-04-02 | unchanged |
| f1099sa | final | April 2025 (continuous-use form) | unchanged |
| f1120ssk | draft | 2026 DRAFT, posted 2026-04-29 (irs.gov/draft-tax-forms) | unchanged |
| f2441 | draft | 2026 DRAFT, posted 2026-05-06 (irs.gov/draft-tax-forms) | unchanged |
| f4562 | draft | 2026 DRAFT, posted 2026-06-01 (irs.gov/draft-tax-forms) | unchanged |
| f4952 | final | 2026; created 2026-05-28 | unchanged |
| f5329 | draft | 2026 DRAFT, posted 2026-08-06 (irs.gov/draft-tax-forms) | unchanged |
| f5695 | draft | 2026 DRAFT, posted 2026-05-26 (irs.gov/draft-tax-forms) | unchanged |
| f6198 | final | November 2025 (continuous-use form) | unchanged |
| f7206 | draft | 2026 DRAFT, posted 2026-05-19 (irs.gov/draft-tax-forms) | unchanged |
| f8283 | final | December 2025 (continuous-use form) | unchanged |
| f8582 | draft | 2026 DRAFT, posted 2026-09-18 (irs.gov/draft-tax-forms) | unchanged |
| f8606 | final | 2026; created 2026-04-21 | NEW FINAL (replaces draft) |
| f8863 | draft | 2026 DRAFT, posted 2026-05-26 (irs.gov/draft-tax-forms) | unchanged |
| f8880 | draft | 2026 DRAFT, posted 2026-05-14 (irs.gov/draft-tax-forms) | unchanged |
| f8889 | draft | 2026 DRAFT, posted 2026-05-07 (irs.gov/draft-tax-forms) | unchanged |
| f8949 | draft | 2026 DRAFT, posted 2026-05-26 (irs.gov/draft-tax-forms) | unchanged |
| f8959 | draft | 2026 DRAFT, posted 2026-05-29 (irs.gov/draft-tax-forms) | unchanged |
| f8960 | draft | 2026 DRAFT, posted 2026-06-01 (irs.gov/draft-tax-forms) | unchanged |
| f8962 | draft | 2026 DRAFT, posted 2026-05-11 (irs.gov/draft-tax-forms) | unchanged |
| f8995 | draft | 2026 DRAFT, posted 2026-05-29 (irs.gov/draft-tax-forms) | unchanged |
| f8995a | draft | 2026 DRAFT, posted 2026-05-29 (irs.gov/draft-tax-forms) | unchanged |
| fr-2025-01377 | final | 90 FR 5917, January 17, 2025 (FR Doc. 2025-01377), Annual Update of the HHS Poverty Guidelines | unchanged |
| fw2 | final | 2026; created 2026-01-07 | unchanged |
| i1040s8812 | draft | 2026 DRAFT, posted 2026-08-21 (irs.gov/draft-tax-forms) | unchanged |
| i1040sb | draft | 2026 DRAFT, posted 2026-08-12 (irs.gov/draft-tax-forms) | unchanged |
| i1040sc | draft | 2026 DRAFT, posted 2026-10-08 (irs.gov/draft-tax-forms) | unchanged |
| i1040se | draft | 2026 DRAFT, posted 2026-09-24 (irs.gov/draft-tax-forms) | unchanged |
| i1040sse | final | 2026; dated Aug 5, 2026 | unchanged |
| i1041sk1 | draft | 2026 DRAFT, posted 2026-08-25 (irs.gov/draft-tax-forms) | unchanged |
| i1062 | draft | Dec 2026 DRAFT, posted 2026-04-14 (irs.gov/draft-tax-forms) | unchanged |
| i1095a | final | 2026; dated Oct 29, 2026 | NEW FINAL (replaces draft) |
| i1098et | final | 2026; dated Sep 30, 2025 | unchanged |
| i1099ac | final | April 2025 (continuous use) | unchanged |
| i1099div | final | January 2024 (continuous use) | unchanged |
| i1099int | draft | Dec 2026 DRAFT, posted 2026-10-22 (irs.gov/draft-tax-forms) | unchanged |
| i1099r | final | 2026; dated Jun 17, 2026 | unchanged |
| i1116 | draft | 2026 DRAFT, posted 2026-09-30 (irs.gov/draft-tax-forms) | unchanged |
| i1120ssk | draft | 2026 DRAFT, posted 2026-09-18 (irs.gov/draft-tax-forms) | unchanged |
| i2441 | draft | 2026 DRAFT, posted 2026-08-24 (irs.gov/draft-tax-forms) | unchanged |
| i5329 | draft | 2026 DRAFT, posted 2026-11-09 (irs.gov/draft-tax-forms) | DRAFT REPOSTED 2026-11-09 (was 2026-09-08) |
| i5695 | draft | 2026 DRAFT, posted 2026-09-01 (irs.gov/draft-tax-forms) | unchanged |
| i6198 | final | November 2025 (continuous use) | unchanged |
| i7206 | draft | 2026 DRAFT, posted 2026-07-14 (irs.gov/draft-tax-forms) | unchanged |
| i8283 | final | December 2025 (continuous use) | unchanged |
| i8582 | draft | 2026 DRAFT, posted 2026-11-05 (irs.gov/draft-tax-forms) | NEW DRAFT |
| i8606 | draft | 2026 DRAFT, posted 2026-09-23 (irs.gov/draft-tax-forms) | unchanged |
| i8863 | draft | 2026 DRAFT, posted 2026-09-11 (irs.gov/draft-tax-forms) | unchanged |
| i8889 | draft | 2026 DRAFT, posted 2026-07-27 (irs.gov/draft-tax-forms) | unchanged |
| i8959 | draft | 2026 DRAFT, posted 2026-08-31 (irs.gov/draft-tax-forms) | unchanged |
| i8960 | draft | 2026 DRAFT, posted 2026-10-16 (irs.gov/draft-tax-forms) | unchanged |
| i8962 | draft | 2026 DRAFT, posted 2026-11-05 (irs.gov/draft-tax-forms) | NEW DRAFT |
| i8995 | draft | 2026 DRAFT, posted 2026-09-10 (irs.gov/draft-tax-forms) | unchanged |
| i982 | final | December 2021 (continuous use; Form 982 Rev. March 2018) | unchanged |
| irb26-29 | final | Internal Revenue Bulletin 2026-29 (July 13, 2026), Announcement 2026-11 at page 49 | unchanged |
| iw2w3 | final | 2026 (Rev. 1-2026 references inside) | unchanged |
| n-25-67 | final | Notice 2025-67; 2026 retirement limits | unchanged |
| n-26-10 | final | Notice 2026-10; 2026 standard mileage rates | unchanged |
| p15 | final | 2026; dated Dec 15, 2025 | unchanged |
| p4681 | draft | 2026 DRAFT, posted 2026-10-22 (irs.gov/draft-tax-forms) | unchanged |
| p503 | draft | 2026 DRAFT, posted 2026-10-29 (irs.gov/draft-tax-forms) | unchanged |
| p505-2026 | final | 2026; dated Mar 31, 2026 | unchanged |
| p525 | draft | 2026 DRAFT, posted 2026-11-06 (irs.gov/draft-tax-forms) | NEW DRAFT |
| p529 | final | December 2020 (continuous use) | unchanged |
| p538 | final | January 2022 (continuous use) | unchanged |
| p575 | draft | 2026 DRAFT, posted 2026-10-02 (irs.gov/draft-tax-forms); dated Oct 2, 2026 | unchanged |
| p590a | draft | 2026 DRAFT, posted 2026-11-10 (irs.gov/draft-tax-forms) | NEW DRAFT |
| p590b | draft | 2026 DRAFT, posted 2026-11-09 (irs.gov/draft-tax-forms) | DRAFT REPOSTED 2026-11-09 (was 2026-11-03) |
| p925 | draft | 2026 DRAFT, posted 2026-11-06 (irs.gov/draft-tax-forms) | NEW DRAFT |
| plaw-119-21 | final | Public Law 119-21, July 4, 2025, 139 Stat. 72 (GovInfo, GPO) | unchanged |
| rp-25-19 | final | Rev. Proc. 2025-19; 2026 HSA amounts | unchanged |
| rp-25-25 | final | Rev. Proc. 2025-25; 2026 applicable percentage table | unchanged |
| rp-25-32 | final | Rev. Proc. 2025-32; 2026 adjusted items | unchanged |
| rp-26-15 | final | Rev. Proc. 2026-15; 2026 automobile depreciation limits | unchanged |
