# 2026 archive refresh, 2026-11-04

TY2026 preparation, step 1 (`docs/ty2026/2026-11-04_ty2026_cloud_brief.md`). The rehearsal of commit 713a566
archived 57 IRS drafts on 2026-10-27. This refresh checked every document in `tools/sources-2025.json` against
irs.gov/draft-tax-forms (all pages, read 2026-11-04), the current final PDFs at `irs.gov/pub/irs-pdf/`, and IRS
guidance that sets 2026 amounts. `python3 tools/fetch_sources.py --year 2026` verifies the archive: 88 documents,
52 of them IRS drafts. `years.json` is unchanged (`[2025]`); drafts cannot back a release (spec 7).

How a final 2026 edition was recognised: the PDF now at `irs.gov/pub/irs-pdf/<name>.pdf` prints 2026 (or a
revision current for 2026) as its year, inspected in the extracted text; the revision fields in
`sources/2026/manifest.json` quote where.

## 1. Rehearsal drafts re-checked

All 57 rehearsal drafts were downloaded again and compared by SHA-256 with the manifest: all 57 are unchanged,
and the posted dates on the draft page equal the catalogued `draft_posted` dates. No draft has been reposted since
2026-10-27.

## 2. Drafts replaced by the final 2026 edition (8)

The draft entry and its files were removed and the final archived under the same id; the catalog row's
`description` names the draft it supersedes.

| id | final edition | superseded draft |
|---|---|---|
| f1040sc | Schedule C (Form 1040) 2026, created 5/15/26 | 2026 draft posted 2026-05-28 |
| f1040sse | Schedule SE (Form 1040) 2026, created 4/27/26 | 2026 draft posted 2026-05-21 |
| i1040sse | Instructions for Schedule SE (2026), Aug 5, 2026 | 2026 draft posted 2026-08-14 |
| f4952 | Form 4952 (2026), created 5/28/26 | 2026 draft posted 2026-05-29 |
| f1095a | Form 1095-A (2026), created 5/12/26 | 2026 draft posted 2026-07-08 |
| i1099r | Instructions for Forms 1099-R and 5498 (2026), Jun 17, 2026 | 2026 draft posted 2026-06-18 |
| iw2w3 | General Instructions for Forms W-2 and W-3 (2026) | 2026 draft posted 2026-01-30 |
| f1099g | Form 1099-G (Rev. December 2026) | Dec 2026 draft posted 2025-10-15 |

## 3. New 2026 drafts (3)

| id | edition | posted |
|---|---|---|
| p503 | Publication 503 (2026) | 2026-10-29 (after the rehearsal) |
| p590b | Publication 590-B (2026) | 2026-11-03 (after the rehearsal) |
| p575 | Publication 575 (2026) | 2026-10-02 (before the rehearsal, which did not archive it) |

## 4. New final 2026 editions (6)

`fw2` (2026 Form W-2), `f1099r` (2026 Form 1099-R), `f1098t` (2026 Form 1098-T), `i1098et` (Instructions for
Forms 1098-E and 1098-T, 2026), `p15` (Publication 15 (2026)), `p505-2026` (Publication 505 (2026)).

## 5. Continuous-use revisions current for 2026 (13)

These forms carry a revision date, not a year. Each revision below is the one at `irs.gov/pub/irs-pdf/` on
2026-11-04, and no later draft for 2026 is posted (a posted draft of `f1099div` and `i1099div` is a December 2027
revision). Each applies to 2026 unless the IRS supersedes it before filing season; recheck at adoption.

`f1099int`, `f1099div`, `i1099div` (Rev. January 2024); `f1099c`, `i1099ac`, `f1099sa` (Rev. April 2025);
`f8283`, `i8283` (Rev. December 2025); `f6198`, `i6198` (Rev. November 2025); `p529` (Rev. December 2020);
`p538` (Rev. January 2022); `i982` (Rev. December 2021).

`i1099int` stays the 2026 draft (Dec 2026 revision, posted 2026-10-22): the final at `irs-pdf/` is still Rev.
January 2024, which the draft will replace.

## 6. Final guidance that sets 2026 amounts (9)

| id | document | what it sets |
|---|---|---|
| rp-25-32 | Rev. Proc. 2025-32 | the 2026 inflation-adjusted items (the counterpart of `rp-2024-40`) |
| rp-25-19 | Rev. Proc. 2025-19 | the 2026 HSA amounts under section 223 |
| n-25-67 | Notice 2025-67 | the 2026 retirement plan and IRA limits |
| rp-25-25 | Rev. Proc. 2025-25 | the 2026 applicable percentage table (section 36B) |
| rp-26-15 | Rev. Proc. 2026-15 | the depreciation limits for passenger automobiles placed in service in 2026 |
| n-26-10 | Notice 2026-10 | the 2026 standard mileage rates (the counterpart of `n-25-05`) |
| irb26-29 | Internal Revenue Bulletin 2026-29 | prints Announcement 2026-11, which modifies Notice 2026-10's rates for travel on or after July 1, 2026; there is no separate PDF at `irs-drop/a-26-11.pdf` (404) |
| fr-2025-01377 | 90 FR 5917, the 2025 HHS poverty guidelines | the counterpart of `fr-2024-00796`; that the 2026 Form 8962 uses them rests on the 2025 pattern and must be confirmed from the 2026 Instructions for Form 8962, not yet posted |
| plaw-119-21 | Public Law 119-21 as printed | the statute behind amounts it fixes for 2026; the same document the 2025 catalog holds |

The search for this guidance used a web search restricted to irs.gov and govinfo.gov; every document above was
then fetched and its identification read in the extracted text. Search summaries were not used as sources.

## 7. Still missing (78 ids of the 2025 catalog)

**No 2026 edition posted, draft or final** (the latest edition on the draft page or at `irs-pdf/` is the 2025
or an earlier one):

- Instructions: `i1040gi` (the Form 1040 instructions, cited by 130 of the 2025 parameters), `i1040sca`,
  `i1040sd`, `i8949`, `i8995a`, `i4562`, `i8582`, `i1065sk1`, `i8962`.
- Publications: `p501`, `p502`, `p526`, `p561`, `p550`, `p334`, `p946`, `p463`, `p587`, `p560`, `p525`,
  `p590a`, `p527`, `p925`, `p974`, `p970`, `p969`, `p504`.
- HTML instruction and publication pages (`*-html`), posted with the final editions: `i1040gi-html`,
  `i1040sca-html`, `i1040sd-html`, `i8949-html`, `i8283-html`, `i8959-html`, `i8960-html`, `i8995-html`,
  `i8995a-html`, `i1116-html`, `p946-html`, `p463-html`.

**Year-specific 2025 guidance with no 2026 counterpart identified**: `n-25-69` (Notice 2025-69, overtime
methods), `n-25-62` (2025 penalty relief, tips and overtime reporting), `n-25-57` (2025 transitional guidance,
car loan interest returns), `fr-2025-24154` (proposed car loan interest regulations; final regulations not
looked for beyond this search), `fs-2025-01`, `fs-2025-05` (energy credit fact sheets), `i8995-correction`,
`about-8995`, and the newsroom pages (`obbb-provisions`, `wftc-notices`, `tips-deduction`,
`overtime-deduction`, `overtime-qa`, `senior-deduction`, `tipped-occupations`). Whether 2026 needs any of them
depends on whether a 2026 definition still cites them (step 3).

**Renamed in 2026** (a 2026 counterpart exists under another id; definitions re-cite at adoption):
`rp-2024-40` → `rp-25-32`; `n-25-05` → `n-26-10` (with `irb26-29`); `fr-2024-00796` → `fr-2025-01377`;
`i4562-2024` (the 2024 printing, a second reading of the auto limits) → none yet.

**Statutes and regulations**: `usc-26-36b`, `usc-26-25a`, `usc-26-72`, `usc-26-4973`, `usc-26-179` are the 2024
edition of the U.S. Code, which predates Public Law 119-21; the 2025 edition is not on GovInfo
(`USCODE-2025-title26/...sec36B.pdf` redirects to the error page, 2026-11-04). `cfr-26-1-179-2`,
`cfr-26-1-179-3`: not refetched (the "most recent" link would be a 2026 edition only after April 2026; not
needed by any 2026 amount found so far).

**Not year sources**: the Statistics of Income pages and tables (`soi-*`) feed the coverage estimate, not the
encoding.

`tools/fetch_sources.py --year 2026` (verify) therefore reports the archive complete for the 2026 catalog; the
missing documents are outside the catalog until they post.

## Addendum (step 3): three new 2026 drafts named by the 2026 Form 1040

Reading the 2026 Form 1040 draft in step 3 found two forms that are not in the 2025 catalog: Schedule 3-A (Form
1040), Federal Public Benefit (line 32b), and Form 1062 (line 24b). Their drafts were archived with the draft flags:
`f1040s3a` (2026 edition, posted 2026-08-20), `f1062` (Dec 2026 edition, posted 2026-08-04), `i1062` (Dec 2026
edition, posted 2026-04-14). The archive now holds 91 documents, 55 of them IRS drafts.
