# New York State sources, tax year 2025

Archived 2026-11-04 by `python3 tools/fetch_sources.py --jurisdiction ny --fetch` from the catalog
`tools/sources-ny-2025.json`, for the owner's 2026 New York return (full-year New York City resident, Form IT-201,
New York standard deduction; `docs/ny/2026-11-04_ny_cloud_brief.md`). The work is built on these final tax-year 2025
editions and carried to 2026 when the 2026 editions publish. No draft is archived. The layout is the federal
archive's: each document with its SHA-256, the layout text (`<id>.txt`), and for a PDF the reading-order text
(`<id>.cols.txt`) and page classification (`<id>.pages.json`), all hashed in `manifest.json`. `python3
tools/fetch_sources.py --jurisdiction ny` verifies the archive offline.

Where this archive sits (`sources/ny/<year>/`, a separate catalog, `ny_` document ids) is provisional: how New York
documents are named and split from the federal archive is an open owner decision (`docs/ny/DECISIONS.md`).

## Documents and editions

| id | document | edition | date standing for "posted" | pages |
| --- | --- | --- | --- | --- |
| `ny_it201` | Form IT-201, Resident Income Tax Return | IT-201 (2025), final | PDF modified 2025-11-12 | 4 |
| `ny_it201i` | Form IT-201-I, Instructions for Form IT-201 (with the instructions for Forms IT-195 and IT-201-ATT, the New York State tax rate schedule and tax computation worksheets, the New York City tax rate schedule) | IT-201-I (2025), final | PDF modified 2025-11-20 | 41 |
| `ny_it201i-html` | The web edition of IT-201-I (2025) | 2025 | page "Updated: July 27, 2026" | web |
| `ny_it201_tax_tables` | Tax tables for Form IT-201: the 2025 New York State Tax Table and New York City Tax Table | 2025 | page "Updated: November 18, 2025" | web |
| `ny_it201att` | Form IT-201-ATT, Other Tax Credits and Taxes | IT-201-ATT (2025), final | PDF modified 2025-09-22 | 2 |
| `ny_it2` | Form IT-2, Summary of W-2 Statements | IT-2 (2025), final | PDF modified 2025-09-26 | 2 |
| `ny_it270i` | Form IT-270-I, Instructions for Form IT-270, New York City Income Tax Elimination Credit | tax year 2025 (no printed edition line; address `/pdf/2025/inc/`; PDF title "Tax Year 2025") | PDF modified 2025-10-27 | 1 |
| `ny_tax_law_601` | New York Tax Law § 601, Imposition of tax (the rate schedules and the tax table benefit recapture, subsections (d) to (d-7)), from the New York State Senate's laws site | the revision from 2025-07-11, the latest | Senate page "Viewing most recent revision (from 2025-07-11)", read 2026-11-04 | 58 |

New York prints no posted date on its forms. The PDF modification date (metadata) or the web page's "Updated" footer
is recorded instead; each is in `manifest.json` under `revision`.

Why each is here:
- **IT-201, IT-201-I**: the return and its instructions, the target.
- **Tax tables (web)**: IT-201-I prints no New York State or New York City tax table; it says (p. 12, Line 39) "find
  your New York State tax using the 2025 New York State Tax Table (visit www.tax.ny.gov and search: table)". The
  tables exist only as this web page. It prints one example for each table (taxable income $38,275, married filing
  jointly: State $1,773, City $1,292), the only official worked examples found for lines in scope.
- **IT-201-I web edition**: a second publication of the instructions. It carries the filing-status numbers as real
  characters (see below) and its tables are in reading order; it is the twin of `ny_it201i` in the PDF-vs-HTML
  extraction check.
- **IT-201-ATT**: IT-201 lines 42, 45, 51, 53 and 71 read it (all zero or refused for the target).
- **IT-2**: lines 72 to 74 (tax withheld) are totals from Form IT-2's W-2 records (IT-201-I p. 21).
- **IT-270-I**: the New York City income tax elimination credit (line 70a) is new for 2025 and claimed on Form IT-270;
  its instructions state the eligibility conditions a refusal screen must ask about (dependents claimed, income
  thresholds, investment income).
- **Tax Law § 601**: the statute behind the tax computation worksheets. Subsection (d-4), for taxable years 2023 to
  2025, sets the recapture of the tax table benefit; it settles which income measure selects each worksheet
  (`amb.ny.2025.recapture_selection`). The Senate's PDF is generated per request, so a fresh download has another
  hash; the archived copy's text equals the 2025-07-11 revision shown on www.nysenate.gov.

Not archived (a refusal names them by citing the IT-201-I page that requires them): IT-203, IT-225, IT-196, IT-360.1,
Y-203, IT-112-R, IT-213, IT-214, IT-215, IT-216, IT-209, IT-272, IT-227, IT-195, IT-1099-R, IT-2105.9, IT-6-SNY,
IT-203-A.

**Corrections.** The Department's "Personal income tax forms corrections and changes" page
(`/forms/income_up_to_date_info.htm`, read 2026-11-04) lists no year after 2023, so no correction to the 2025 IT-201
or IT-201-I is published there. The web edition of IT-201-I is dated July 27, 2026, eight months after the PDF; the
extraction check found every word of every PDF page in it (bar the six pages excepted below), and a comparison of the
sets of numbers printed in each (2026-11-04, by hand: every number of two or more digits, commas removed) found the
same numbers in both except the sample-check digits (PDF only) and "5217" (Form RP-5217, web only). Whether the web
edition changed any wording that the word check cannot see (a number moved between rows, a word added) is not
established.

## Extraction checks (Phase 1, item 3)

`python3 tools/check_extraction.py --jurisdiction ny` (report: `reports/ny/2025/extraction.md`): 5 PDFs, layout
text against reading order identical in characters on every page; IT-201-I against its web edition, every word of
every page found except six pages, accepted with their reasons in `tools/extraction/exceptions.json` (p. 25, the sample
check, an image in the web edition; pp. 35 to 39, the running heading "Tax computation – New York AGI of more than
$107,650 (continued)", which the web edition prints once). The PDFKit cross-reading is macOS-only and was skipped
here; it is not claimed. The one-time OCR audit (`tools/ocr_audit.py`) was not run.

### Text-layer facts every reader of the PDFs must know

1. **Filing-status numbers.** IT-201 and IT-201-I print the filing statuses as circled digits ① to ⑤ in a Wingdings
   2 font. The text layer carries them as private-use characters U+F081 to U+F085 (① to ⑤), which read as blanks
   ("using filing status ; or"); in three places on IT-201-I p. 22 (twice under Line 75, once under "Nonobligated
   spouse") ② is followed by a stray U+201A (‚), which the web edition also prints ("②‚").
   Every rule that turns on a filing-status number ("Filing status ① only (Single): Use New York State household
   credit table 1") must be read from the web edition, where the digits are real characters, or from the page image.
2. **Tables are flattened.** Neither text layer keeps table cells in rows reliably; the web edition (one cell per
   line) is the reliable reading of every table.

### Pages whose reading-order text is doubtful

IT-201-I (`ny_it201i.cols.txt`; classifications from `ny_it201i.pages.json`):

| page | class | what is doubtful | read instead |
| --- | --- | --- | --- |
| 11 | single | New York State standard deduction table: amounts follow their rows, filing-status digits are private-use characters | web edition, "New York State standard deduction table" |
| 12 | table | household credit tables 1 to 3: column heads (number of people 1 to 7, "over 7") are scattered through the header text; rows otherwise in order. Line 40's text precedes Line 39's | web edition, tables 1 to 3 |
| 13 | single | two columns interleaved: the Line 47 worksheet sits inside the Line 41 text, Line 45 inside Line 47a, Line 48 inside Line 47 | layout text `ny_it201i.txt` p. 13, or the web edition |
| 14 | table | household credit tables 4 to 6 (as p. 12); the end of Line 51's joint-return text is printed before the Line 50 heading | web edition |
| 17 | prose | Yonkers worksheet: the rate "0 . 1675" detached from line n (out of scope) | web edition |
| 18 | prose | sales and use tax chart: rows readable; its footnote and the "You must use Form ST-141" list interleave | web edition, "Sales and use tax chart" |
| 20 | prose | school tax credit Table 1 and Table 2: filing-status column heads separated from their amounts ($63, $125) | web edition, "Table 1" and "Table 2" |
| 21 | prose | school tax credit rate-reduction tables: "over / but not over" cells scattered ("$ 21,600 0.171% of taxable income $ 0") | web edition, "Calculation of NYC school tax credit (rate reduction amount)" |
| 33 | table | New York State tax rate schedule: the "but not over" column is printed again as a list after the three schedules; ditto marks for "of the excess over" | web edition, "New York State tax rate schedule" |
| 34 to 39 | prose/single | tax computation worksheets 1 to 16: each worksheet's printed Recapture Base and Incremental Benefit amounts (for example 333 and 807 on worksheet 2) are detached after the worksheet's lines | web edition, where each amount is on its line ("4. _____333______") |
| 40 | table | New York City tax rate schedule: rows split and reordered | web edition, "New York City tax rate schedule" |

IT-201 (`ny_it201.cols.txt`, all four pages classed table): the line labels of pages 2 to 4 run together in long
rows with the line numbers and ". 00" boxes interleaved; the layout text (`ny_it201.txt`) keeps each line on its own
row and is the better reading for line numbers and labels. Page 1's filing-status boxes and items A to H are in order.

Tax tables (web, `ny_it201_tax_tables.txt`): one cell per line; a few cells carry a stray space inside the number
("62, 050"), so a table extractor must remove spaces inside numbers. The State table runs from $0 to $65,000
(bands $0–13, 13–25, 25–50, then $50 bands from $50); the City table also ends at $65,000 but starts with the bands
$0–18, 18–25, 25–50 (the full structure is for the Phase 3 extractor to confirm).

IT-201-ATT and IT-2: forms, read by line; no rule in scope depends on their reading order.
IT-270-I (one page, two columns, classed table): the income-thresholds table is in the right column beside the
general information; layout text keeps the rows.
