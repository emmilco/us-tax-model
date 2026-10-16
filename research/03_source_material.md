# Authoritative source material and machine-readability

Research date: 2026-10-13. Method: WebSearch and WebFetch only. IRS PDFs did not parse through the fetch tool, so everything read "directly" below was read from IRS HTML pages (instructions, Internal Revenue Bulletin, listing pages). Where I rely on a search snippet, a secondary source, or recollection, the claim says so.

## Summary

- **Worked examples for the Qualified Dividends and Capital Gain Tax Worksheet (QDCGTW) are scarce.** I found no numeric filled-in example in the 2025 Form 1040 instructions, Schedule D instructions, or the parts of Publication 550 I read. Publication 17 (2025) has removed its dividends, sale-of-property and reporting-gains chapters. The plan to use official QDCGTW examples as the first passing tests is not supported by what I found.
- **MeF schemas and business rules are not publicly downloadable.** Since 2016 they go only to the e-Services Secure Object Repository mailbox of registered Software Developers or States. The project cannot treat them as an open, citable source without becoming an e-file applicant, and redistribution status is unknown.
- **A short form list is easily incomplete for a wage earner with investment income.** Two W-2s that together exceed the 2026 wage base ($184,500) imply taxable income above $100,000, so the Tax Computation Worksheet applies, not the Tax Table. For a single filer above $200,000 of combined Medicare wages, Form 8959 and Schedule 2 are required, and Form 8960 is likely.
- **TY2026 forms exist as drafts; TY2026 instructions for the core computation do not.** Drafts exist for Form 1040 (2026-09-17), Schedules 1, 1-A, 2, 3, B, D, and Forms 8949, 8959, 8960, 2210, 1116. No 2026 draft exists yet for the 1040 instructions, Schedule D instructions, or Form 8949, 8960 and 2210 instructions.
- **TY2025 is a sound development fixture, with caveats.** The 2026 draft 1040 renumbers lines (new 12f, 13a/13b swapped, 24a–c, 32b–c). Line-number citations must be revision-pinned from day one.
- **TY2026 figures are published.** Rev. Proc. 2025-32 gives the brackets, the 0%/15% capital gain breakpoints and the standard deduction. SSA set the wage base at $184,500.
- **HTML instructions are the best machine-readable source.** They include worksheets line by line. There is no XML; ePub is for publications only.
- **Rounding rules are stated, and consistently.** Rounding is optional but all-or-nothing, at 50 cents, on the line total and not the components. The Tax Table's midpoint construction is not stated in the statute or in instruction text I could find.
- **Filling the official PDF is outside the substitute-forms regime; rendering our own form is inside it.** Publication 1167 (Rev. Proc. 2025-27) defines a substitute as any form that differs from the official version.

## Findings

### 1. Form set for the slice

**Certain (every return in the slice)**
- **Form 1040.** High.
- **Tax Computation Worksheet instead of the Tax Table**, if taxable income is $100,000 or more: "If your taxable income is less than $100,000, you must use the Tax Table." The excess-Social-Security premise makes this the normal case. Source: https://www.irs.gov/instructions/i1040gi (2025, read directly). High.
- **Schedule 3, line 11** (excess Social Security withheld), given the premise.
  - The 2026 single-employer maximum is 6.2% × $184,500 = $11,439.00 (SSA figure via search snippet; ssa.gov returned 403 to direct fetch). Medium-High.
  - The credit applies only with two or more employers. If one employer over-withheld, the remedy is that employer or Form 843. It is figured separately per spouse. I have this from prior-year IRS wording quoted by secondary sources; I could not reach the 2025 Schedule 3 line 11 text. Medium.
- **A tax worksheet for line 16**: the QDCGTW or the Schedule D Tax Worksheet, whenever there are qualified dividends or net capital gain. High.

**Conditional**
- **Schedule B.** Required if taxable interest or ordinary dividends exceed $1,500, or if any of these apply: seller-financed mortgage interest, accrued bond interest, OID or bond-premium adjustments, the EE/I bond exclusion, nominee income, a foreign account, or a foreign trust. Source: https://www.irs.gov/instructions/i1040sb (2025, read directly). High. The interview must ask the Part III foreign-account question even when amounts are small.
- **Schedule D and Form 8949.** Source for all three cases: https://www.irs.gov/instructions/i1040gi, https://www.irs.gov/instructions/i8949, https://www.irs.gov/instructions/i1040sd (read directly). High.
  - Stock sales normally require both.
  - Form 8949 can be skipped for transactions where basis was reported to the IRS and no adjustments are needed. Those go as aggregates on Schedule D lines 1a and 8a.
  - Neither form is needed (1040 Exception 1) if the only gains are capital gain distributions in 1099-DIV box 2a, with nothing in boxes 2b–2d and no losses. Then check "Schedule D not required" on line 7.
  - Form 8949 Exception 2 allows attached statements in place of line-by-line entry.
- **Schedule D Tax Worksheet replaces the QDCGTW** "only if line 18 or line 19 of Schedule D is more than zero and lines 15 and 16 of Schedule D are gains, or if you file Form 4952 and you have an amount on line 4g." Source: https://www.irs.gov/instructions/i1040sd (read directly). High.
- **28% Rate Gain Worksheet** (collectibles, section 1202) and **Unrecaptured Section 1250 Gain Worksheet.** A 1099-DIV with box 2b, 2c or 2d populated triggers these. Mutual funds and REIT funds do this routinely, so it is not exotic. High.
- **Capital Loss Carryover Worksheet.** Needed if the prior year had a net loss over the limit, or the current year produces one (Schedule D line 21). This needs prior-year return data. High.
- **Form 8949 adjustment codes** in column (f): B, C, D, E, H, L, M, N, O, P, Q, R, S, T, W (wash sale), X, Y, Z. Boxes A–F cover securities; boxes G–L were added in 2025 for digital assets (1099-DA). Source: https://www.irs.gov/instructions/i8949 (read directly). High.
- **Form 8959 and Schedule 2.** Required if any single W-2 has Medicare wages over $200,000, or combined Medicare wages exceed $250,000 (MFJ), $125,000 (MFS) or $200,000 (others). The thresholds are not indexed. Source: https://www.irs.gov/instructions/i8959 (read directly). High. Two employers each paying under $200,000 withhold no Additional Medicare Tax, so tax is due on the return.
- **Form 8960** (net investment income tax). Required if MAGI exceeds $250,000, $125,000 or $200,000 by the same statuses. Source: https://www.irs.gov/instructions/i8960 (read directly). High.
- **Foreign tax credit (1099-DIV box 7).** It goes directly on Schedule 3 line 1 without Form 1116 if all foreign income is passive, it was reported on a qualified payee statement, and creditable foreign tax is at most $300 ($600 MFJ). Otherwise Form 1116 is needed. Source: https://www.irs.gov/instructions/i1116 (read directly). High.
- **Schedule 1.** Not needed by the slice's income types. It becomes relevant only with adjustments or other income. Medium.
- **Schedule 1-A** (tips, overtime, car-loan interest, senior deduction). Conditional on those facts; the senior deduction applies at 65 or older. The 2025 instructions route it to line 13b. High.
- **Form 2210.** Usually not filed: "The IRS will generally figure your penalty for you." The penalty is still computed for line 38 if the taxpayer chooses. Safe harbours are 90% of current-year tax, or 100% of prior-year tax (110% if prior-year AGI exceeded $150,000), and the under-$1,000 exception. Source: https://www.irs.gov/instructions/i2210 (read directly). High. With unwithheld Additional Medicare Tax and capital gains, underpayment is plausible.
- **Standard deduction versus Schedule A**, and the new 2026 non-itemizer charitable line. See item 2.
- **Form 6251 (AMT).** Unlikely, but not excluded at high income. Not investigated.

### 2. Law changes, TY2025 to TY2026

Figures from Rev. Proc. 2025-32, read directly in IRB 2025-45 (https://www.irs.gov/irb/2025-45_IRB) and cross-checked against secondary summaries. High.

| Item (TY2026) | Single | MFJ | Other |
|---|---|---|---|
| Standard deduction | $16,100 | $32,200 | HOH $24,150; MFS $16,100 |
| Additional amount, aged or blind | $2,050 | $1,650 | |
| Maximum 0% capital gain amount | $49,450 | $98,900 | HOH $66,200; MFS $49,450 |
| Maximum 15% capital gain amount | $545,500 | $613,700 | HOH $579,600; MFS $306,850 |

- **Single bracket floors:** 12% at $12,400; 22% at $50,400; 24% at $105,700; 32% at $201,775; 35% at $256,225; 37% at $640,600.
- **MFJ bracket floors:** $24,800; $100,800; $211,400; $403,550; $512,450; $768,700.
- **TY2025 comparison** (2025 instructions, read directly): standard deduction $15,750 / $31,500 / $23,625; 0% breakpoints $48,350 / $96,700 / $64,750; 15% breakpoints $533,400 / $600,050 / $566,700 / MFS $300,000.
- **Social Security wage base:** $184,500 for 2026, up from $176,100; announced 2025-10-24. Source: https://www.ssa.gov/oact/cola/cbb.html (search snippet only; direct fetch returned 403). Medium-High. The 2027 base is not relevant to TY2026 and I did not verify whether it has been announced.
- **P.L. 119-21 items first effective 2026 that touch the slice:**
  - Non-itemizer charitable deduction, up to $1,000 ($2,000 MFJ), cash only. It appears as new line 12f on the 2026 draft 1040. Secondary sources (taxgirl.com on the draft; law-firm summaries). Medium.
  - For itemizers: a 0.5%-of-AGI charitable floor and a 35% cap on the value of itemized deductions. Secondary. Medium.
  - The Schedule 1-A deductions continue.
- **2026 draft Form 1040 structural changes** (secondary: https://www.taxgirl.com/2026/09/22/draft-2026-form-1040-adds-new-citizenship-and-work-authorization-question/; I could not parse the draft PDF). Medium.
  - New "Other Information" section with a citizenship and work-authorization question.
  - Line 12f added.
  - Schedule 1-A moves to line 13a and QBI to 13b, the reverse of 2025.
  - Line 24 splits into a, b, c (new Form 1062).
  - Lines 32b and 32c added, with new Schedule 3-A.
- **Not verified:** changes inside the 2026 Schedule D, 8949, 8959 and 8960 drafts; the NIIT and Additional Medicare thresholds are statutory and unindexed.

### 3. TY2026 availability and calendar

Draft listing read directly from https://www.irs.gov/draft-tax-forms. High. The listing held 1,239 drafts today.

| Product | 2026 draft posted | Notes |
|---|---|---|
| Form 1040 | 2026-09-17 | |
| Schedule 1 | 2026-06-08 | |
| Schedule 1-A | 2026-09-04 | |
| Schedule 2 | 2026-06-04 | |
| Schedule 3 | 2026-06-08 | |
| Schedule B | 2026-05-20 | Instructions 2026-08-12 |
| Schedule D | 2026-05-15 | |
| Form 8949 | 2026-05-26 | |
| Form 8959 | 2026-05-29 | Instructions 2026-08-31 |
| Form 8960 | 2026-06-01 | |
| Form 2210 | 2026-06-04 | |
| Form 1116 | 2026-07-07 | Instructions 2026-09-30 |
| Publication 1040 (Tax and EIC tables) | 2026-09-16 | |

- **No 2026 draft exists for:** Instructions for Form 1040, Schedule D, Form 8949, Form 8960, Form 2210. The newest drafts on the site for those are 2025 revisions, posted 2026-02-26, 2025-12-11, 2025-11-05, 2026-02-04 and 2026-02-19 respectively.
- **Calendar observed from TY2025** (current-products listing, https://www.irs.gov/forms-instructions-and-publications, read directly). "Posted date" is the latest posting, not necessarily the first. Medium.
  - Finals: Schedule B 2025-11-03; Form 8949 2025-12-11; Schedule D and its instructions 2025-12-17; Form 1040 and Schedules 1, 1-A, 2, 3 on 2026-01-02; Publication 1040 2026-01-15; Form 8949 instructions 2026-01-22; 1040 instructions currently dated 2026-02-27 (a re-post).
  - Draft instructions: Form 8949 early November; Schedule D mid-December.
  - Expect TY2026 Schedule D and 8949 instruction drafts in November–December 2026, finals from mid-December to late January, and at least one post-release revision of the 1040 instructions.
- **Is TY2025 a sound fixture?** Yes for the logic. Form 8949, Schedule D, the QDCGTW and the Schedule D Tax Worksheet are structurally stable. No for line numbering and dollar constants. Medium, because I could not read the 2026 Schedule D and 8949 drafts.

### 4. Programmatic acquisition

- **URL patterns.**
  - Current: `https://www.irs.gov/pub/irs-pdf/f1040.pdf`, with `f1040s1.pdf`, `f1040s1a.pdf`, `f1040s2.pdf`, `f1040s3.pdf`, `f1040sb.pdf`, `f1040sd.pdf`, `f8949.pdf`, `i1040gi.pdf`, `i1040sd.pdf`, `i1040sb.pdf`, `i8949.pdf`, `p1040.pdf` (read from the listing). High.
  - Prior year: `https://www.irs.gov/pub/irs-prior/f1040--2024.pdf`. Seen in search results. High.
  - Draft: `https://www.irs.gov/pub/irs-dft/f1040--dft.pdf`, `f1040s1a--dft.pdf`, `i8949--dft.pdf`. Fetched or seen. High.
  - HTML: `https://www.irs.gov/instructions/i1040gi`, `/i1040sd`, `/i1040sb`, `/i8949`, `/i8959`, `/i8960`, `/i1116`, `/i2210`, and `https://www.irs.gov/publications/p550`, `/p17`. Fetched. High.
  - ATS scenarios: `https://www.irs.gov/pub/irs-efile/…`.
- **Caution on URLs.** The current-year URLs are not versioned. `/pub/irs-pdf/f1040.pdf` and `/instructions/i1040gi` silently become TY2026 when finals are released. Snapshots must be content-hashed and archived at fetch time, then re-fetched from `irs-prior` to confirm.
- **Revision detection.** The listing pages expose Product Number, Title, Revision Date and Posted Date in sortable columns, with `?find=` and `items_per_page=` query parameters that work. Draft PDFs carry a watermark date. Forms print a catalog number and revision year. "Recent Developments" live on `https://www.irs.gov/forms-pubs/about-form-XXXX` pages (pattern seen, content not read). Medium-High.
- **Structured formats.** The IRS says it offers "text, e-Braille, HTML, accessible PDF, and large print," plus ePub for publications. Source: https://www.irs.gov/forms-pubs/accessible-irs-tax-products (read directly). High. No XML or structured data is offered for instructions. The HTML instructions do include worksheets as tables: the Schedule D Tax Worksheet's lines 1–47 are present, though the fetch tool reported the text as fragmented by table markup. Medium-High.
- **Copyright.** US government works are not subject to copyright in the United States (17 U.S.C. § 105). I found no IRS page stating reuse terms. Caveats I could not source: foreign copyright is not waived, and use of IRS or Treasury names and insignia in ways implying endorsement is restricted (31 U.S.C. § 333, from recollection). Medium; not verified against an IRS statement.

### 5. Fillable PDF structure

I could not inspect a PDF, so this item is weak.

- IRS fillable forms carry both an AcroForm and an XFA layer. Fields are named in the pattern `topmostSubform[0].Page1[0].f1_01[0]`, with `c1_1[0]` for checkboxes. Field tooltips (`/TU`) carry accessibility text describing the line. The name pattern is corroborated by a search-result forum quote; the rest is recollection. Low-Medium.
- Field names are positional sequence numbers and should be assumed unstable across years. The 2026 draft inserts new fields on page 1, so `f1_NN` indices almost certainly shift. Inferred, not measured. Low-Medium.
- pypdf documents that unknown field keys are silently ignored and that checkboxes need their export-state value. Source: https://pypdf.readthedocs.io/en/latest/user/forms.html (search snippet). Medium.
- Whether pdftk, pypdf, PyMuPDF, pdf-lib or qpdf fill these reliably, including dropping the XFA layer and regenerating appearances, is unverified.
- **Substitute-form rules.** Source: Rev. Proc. 2025-27, reprinted as Publication 1167 (Rev. 10-2025), read directly in https://www.irs.gov/irb/2025-44_IRB (partial). High on the quoted points.
  - A substitute form is one that "differs in any way from the official version."
  - Reproductions using an official IRS version as master need no prior approval (Sec. 2.2.1).
  - Computer-prepared substitutes must follow the layout, page count and line text, and reproduce jurats verbatim.
  - Approval submissions go to substituteforms@irs.gov, and a three-letter source code is assigned per firm.
  - It covers 2025 forms; a 2026 revision should appear in late October 2026.
  - I did not read its later parts (2D barcodes, exhibits).
- Printing data into the official PDF is within the no-approval path. Low-Medium on that conclusion, since it rests on my reading of Sec. 2.2.1 and not on explicit text about filled official PDFs.

### 6. MeF as a structured source

- **Access is restricted.** Schemas and business rules are distributed through the e-Services SOR mailbox, not the website. The requirement is "an active e-Services account" and being "listed on an e-file application with the provider option of software developer" (or State), in a principal, responsible-official or delegated role. Messages are purged after 60 days. Sources: https://www.irs.gov/e-file-providers/modernized-e-file-mef-schemas-and-business-rules, the MeF status page, and the v4.0 release memo (all read directly). High.
- **Release timing.** TY2026 1040-series packages: v1.0 on 2026-05-28 (diffed against 2025v5.3), v2.0 on 2026-07-02, v3.0 on 2026-08-13, v4.0 on 2026-09-24. I read the v4.0 memo directly; the other dates are search snippets of IRS memos. High / Medium. TY2025 reached at least v5.3. Business rules ship as PDF and CSV. Publication 1436 (Rev. 10-2025) says ATS opened 2025-10-14 for TY2025 (search snippet).
- **Contents and coverage.** From recollection, not verified: the XSDs give per-line element names and types, with documentation annotations referencing form lines; the business rules are reject criteria (cross-form consistency, required attachments). Unfiled worksheets such as the QDCGTW are not schema documents. Low-Medium.
- **Public alternatives.** The archived IRS Direct File repository (https://github.com/IRS-Public/direct-file) carries TY2024 logic and test cases in a fact graph. Its README lists excluded material, and I did not read its licence file. Its scope probably excludes capital gains, which I did not verify.

### 7. Official worked examples

| Source | What I found | Usable for the slice | Confidence |
|---|---|---|---|
| 1040 instructions (2025) | Three qualified-dividend holding-period examples; the QDCGTW as a blank worksheet; a Tax Table lookup illustration | 3 rule-level examples plus about 1 lookup | Medium-High; I did not see every section |
| Schedule D instructions (2025) | 13 labelled examples, about 10 numeric and single-transaction; three duplicate Form 8949 examples | About 10 | High |
| Form 8949 instructions (2025) | 7 numeric examples (gain, loss, adjustment, incorrect basis with code B, two digital-asset, home sale) | About 4 for stocks | High |
| Publication 550 (2025) | 54 labelled examples in the last 200,000 characters, including 6 wash-sale examples and basis and holding-period examples. No filled-in Form 8949, Schedule D, carryover worksheet or QDCGTW, and no comprehensive named-taxpayer example in the portions read | Perhaps 20–30 rule-level | Medium; characters 100,000–400,000 unread |
| Publication 17 (2025) | Dividends, Sale of Property and Reporting Gains and Losses chapters removed, pointing to Publication 550 | Little | Medium-High |
| Form 8959 instructions | 8 examples, mostly multi-employer and joint thresholds | 8, directly relevant | High |
| Form 8960 instructions | About 4, none basic | About 0 | Medium |
| Form 2210 instructions | 5, about payment timing | Few | High |
| MeF ATS scenarios, TY2025 | Ten 1040-family scenario PDFs. Scenario 3 was read directly (text extracted, pages rendered): it lists Form 1040, Form 1099-R, Schedules 1, 2, D, E, F, SE and Form 4835, and supplies inputs only — source-document figures (the 1099-R amounts, Schedule D proceeds and basis, Schedule F entries) with every computed line on Form 1040 and the schedules left blank. The IRS grades the submitted XML on its side and publishes no answer key | 0 whole-return oracles; inputs could seed a case whose expected values come from elsewhere | High for scenario 3; the other nine not opened |
| VITA/TCE Publications 4491, 4012, 6744 | They exist (Rev. 10-2025); contents not read | Unknown | Low |
| Publications 505, 544, 551 | Not examined | Unknown | — |

**Estimate.** About 40–60 official numeric examples are relevant to the slice. Nearly all are single-rule or single-line: basis, wash sale, holding period, an 8949 row, the Additional Medicare thresholds. Whole-return examples matching the slice: none found. Filled-in QDCGTW examples: none found. The best remaining candidates are Publication 4491 and the ATS scenarios, since ATS PDFs are complete filled returns whose line 16 is a QDCGTW result, though the worksheet itself is not shown.

### 8. Rounding rules

Sources read directly: 1040 instructions https://www.irs.gov/instructions/i1040gi, Schedule D instructions https://www.irs.gov/instructions/i1040sd, Form 8949 instructions https://www.irs.gov/instructions/i8949. High unless noted.

- **Form 1040:** "You can round off cents to whole dollars on your return and schedules." "If you do round to whole dollars, you must round all amounts." Drop amounts under 50 cents and raise 50–99 cents to the next dollar. For sums, "include cents when adding the amounts and round off only the total." (Assembled from short quoted fragments; the middle sentence is the tool's paraphrase.)
- **Schedule D:** identical wording.
- **Form 8949:** "You can round off cents to whole dollars on Form 8949"; all-or-nothing; cents over 49 round up.
- **Tension to resolve.** Schedule D totals are sums of 8949 rows. "Round only the total" and "round all amounts on Form 8949" can give different totals depending on whether rows are rounded before summing. I found no text settling it.
- **Tax Table.** Mandatory under $100,000. 26 U.S.C. § 3 requires only that table amounts "be computed on the basis of the rates prescribed by section 1" (read at law.cornell.edu). It does not say midpoint. That the table uses $50 bands with tax at the band midpoint, and narrower bands under $3,000, comes from secondary sources and common knowledge, not official text. Medium. The table must be transcribed or reverse-verified cell by cell, not derived.
- **Worksheet arithmetic.** I found no stated rule for rounding intermediate QDCGTW products (the 15% and 20% lines) or for the Tax Computation Worksheet. Low.

## Implications for this project

1. **Change the first-test strategy.** Official examples can seed unit tests for 8949 rows, wash sales, holding periods and the 8959 thresholds. They cannot seed the QDCGTW or a whole return. Whole-return oracles will have to come from VITA materials or cross-validation against other software, which is a different evidentiary class from "official worked example." ATS scenarios supply inputs without computed values and are not oracles.
2. **Redefine the slice honestly.** The proposed slice needs the Tax Computation Worksheet, Schedule 2, Form 8959, probably Form 8960, the Schedule D Tax Worksheet with its two feeder worksheets (driven by 1099-DIV boxes 2b–2d), the Capital Loss Carryover Worksheet, the foreign-tax election test, and a decision about the line 38 penalty. Otherwise the tool needs explicit out-of-scope refusals for each.
3. **Use HTML instructions as the primary text source**, with PDFs as the layout and citation authority. Snapshot both with hashes at fetch time, because the current-year URLs mutate.
4. **Make revision pinning line-level.** Schedule 1-A is line 13b in 2025 and 13a in the 2026 draft.
5. **Treat MeF as optional.** It requires an e-file application and cannot be assumed redistributable, so it cannot underpin a public verifiable artefact unless that is resolved.
6. **Plan the TY2026 build around December 2026 to late January 2027** for instruction text. Constants can be loaded now from Rev. Proc. 2025-32.
7. **For output, fill the official PDF** and do not render look-alike forms, to stay outside substitute-form approval.

## Could not verify / weak spots

- All IRS PDFs were unreadable through the tool: the draft 2026 Form 1040, Rev. Proc. 2025-32 as a PDF (read via the IRB HTML instead), ATS scenarios, Publication 1436, Publications 4491 and 4012.
- Item 5 is largely recollection.
- The contents of the MeF schemas and business rules are not verified.
- The 1040 HTML instructions were read in windows up to about 326,000 characters. I never reached the Schedule 2 and 3 line instructions or the line 38 text, nor the Tax Table's own introductory text.
- Publication 550 characters 100,000–400,000 are unread. That span covers chapter 1 on interest and dividends and the start of chapter 4. A filled-in example could be there, though the table of contents suggests only blank worksheets.
- ssa.gov blocked direct fetch. The $184,500 figure rests on search snippets of the SSA page plus secondary agreement.
- The 2026 draft 1040 changes come from one secondary article.
- IRS "posted dates" are last-posted dates. First-release dates for the TY2025 finals are not established.
- The MeF status page showed filing-season dates of January 2026, which looks like stale text. I did not confirm the processing-year 2027 opening date.

## Open questions

1. Is the owner willing to register as an e-file Software Developer to obtain MeF schemas, and may those files be republished?
2. Should the slice assume single or MFJ? The answer changes whether Forms 8959 and 8960 are near-certain or merely possible.
3. Are 1099-DIV boxes 2b, 2c and 2d in scope (forcing the Schedule D Tax Worksheet), or refused?
4. What counts as an acceptable test oracle where no official worked example exists?
5. Do Publications 4491, 4012 or 6744 contain filled QDCGTW or whole-return examples with keys? This needs a PDF-capable pass.
6. Do the ATS scenario PDFs give enough inputs to reproduce line 16 independently? Answered for scenario 3: the inputs are present but no computed values are, so the scenario cannot check line 16.
7. How does the IRS's own software resolve row rounding against total rounding on Form 8949 and Schedule D?
8. What is the actual AcroForm/XFA structure and year-to-year field-name stability? This needs a local dump of the 2024, 2025 and 2026-draft PDFs.
9. Has the TY2026 revision of Publication 1167 been issued, and does it change anything for filled official PDFs?

## Sources

- https://www.irs.gov/draft-tax-forms — draft listing (queried with `?find=`), posted dates for all slice products
- https://www.irs.gov/forms-instructions-and-publications — current products listing with revision and posted dates
- https://www.irs.gov/instructions/i1040gi — 2025 Form 1040 instructions (rounding, Schedule B and D triggers, line 16, QDCGTW thresholds, standard deduction)
- https://www.irs.gov/instructions/i1040sb — 2025 Schedule B instructions (filing conditions)
- https://www.irs.gov/instructions/i1040sd — 2025 Schedule D instructions (worksheets, conditions, rounding, examples)
- https://www.irs.gov/instructions/i8949 — 2025 Form 8949 instructions (exceptions, codes, boxes A–L, examples)
- https://www.irs.gov/instructions/i8959 — 2025 Form 8959 instructions (thresholds, examples)
- https://www.irs.gov/instructions/i8960 — 2025 Form 8960 instructions (thresholds)
- https://www.irs.gov/instructions/i1116 — 2025 Form 1116 instructions ($300/$600 election)
- https://www.irs.gov/instructions/i2210 — 2025 Form 2210 instructions (penalty tests, IRS figures the penalty)
- https://www.irs.gov/irb/2025-45_IRB — Rev. Proc. 2025-32, 2026 inflation adjustments
- https://www.irs.gov/irb/2025-44_IRB — Rev. Proc. 2025-27, substitute forms (Publication 1167)
- https://www.irs.gov/pub/irs-pdf/p1167.pdf — Publication 1167 (Rev. 10-2025); not parsed
- https://www.ssa.gov/oact/cola/cbb.html — SSA contribution and benefit base (via search; direct fetch 403)
- https://www.irs.gov/e-file-providers/modernized-e-file-mef-schemas-and-business-rules — MeF distribution policy
- https://www.irs.gov/e-file-providers/modernized-e-file-mef-status-page — SOR access requirements, 60-day purge
- https://www.irs.gov/e-file-providers/modernized-e-file-schemas-and-business-rules-for-individual-tax-returns-and-extensions — index of TY2025 and TY2026 individual packages
- https://www.irs.gov/e-file-providers/release-memo-for-tax-year-2026-modernized-e-file-schema-and-business-rules-for-individual-tax-returns-version-4-point-0 — v4.0 memo, 2026-09-24
- https://www.irs.gov/e-file-providers/tax-year-2025-form-1040-series-and-extensions-modernized-e-file-mef-assurance-testing-system-ats-information — TY2025 ATS scenario list
- https://www.irs.gov/pub/irs-efile/ty25-1040-mef-ats-scenario-3-10202025.pdf — ATS scenario 3; read directly (inputs only, no computed values)
- https://www.irs.gov/publications/p550 — Publication 550 (2025), partially read
- https://www.irs.gov/publications/p17 — Publication 17 (2025), removed chapters
- https://www.irs.gov/forms-pubs/accessible-irs-tax-products — available formats
- https://www.irs.gov/pub/irs-dft/f1040--dft.pdf — 2026 draft Form 1040; not parsed
- https://www.taxgirl.com/2026/09/22/draft-2026-form-1040-adds-new-citizenship-and-work-authorization-question/ — secondary description of the 2026 draft 1040
- https://www.law.cornell.edu/uscode/text/26/3 — 26 U.S.C. § 3, tax tables
- https://github.com/IRS-Public/direct-file — archived IRS Direct File source (TY2024)
- https://pypdf.readthedocs.io/en/latest/user/forms.html — pypdf form-filling behaviour
- https://kpmg.com/us/en/taxnewsflash/news/2025/10/tnf-rev-proc-2025-32-inflation-adjustments-for-2026-individual-taxpayers.html — secondary cross-check of the 2026 figures
- https://www.irs.gov/pub/irs-pdf/p4491.pdf, https://www.irs.gov/pub/irs-pdf/p4012.pdf — VITA/TCE materials; existence only
