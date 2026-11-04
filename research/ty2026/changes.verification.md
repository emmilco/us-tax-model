# Verification of the 2026 change map (`research/ty2026/changes.md`)

> **Applied 2026-11-04 (main session).** Every row of the corrections table below is applied in `changes.md`: each affected entry carries a "Correction (verification)" line; C-SCHED-17, C-SCHED-18 and C-CRED-17 are reclassified as wording only (cross-reference); C-PEOP-26 is retitled; C-PEOP-27 is new (section 71304); three What's New rows are added. Both high findings were confirmed against `plaw-119-21` pp. 252 and 254 before applying. The verifier's suggestion to read every 2026-effective section of Public Law 119-21 is carried to `docs/ty2026/ADOPTION.md`.

Independent check, 2026-11-04. Sources used: `sources/2026/*.txt|.cols.txt`, `sources/2025/*.txt|.cols.txt`,
`sources/2026/manifest.json`, `forms/2025/*.yaml`, `params/2025.yaml`, `ambiguities/2025.yaml`, `tables/2025/` (names
only) and the map. Pages are PDF pages (text split on form feeds; a draft's page 1 is the IRS cover). Nothing here is
from memory. Nothing under `tools/transcription/` was run.

## Summary

The map has 132 entries: 29 C-PRI, 39 C-SCHED, 20 C-CRED, 26 C-PEOP and 18 C-BUS.

What I checked:

1. **All 29 C-PRI entries in full.** I compared Form 1040 (2026 pp. 2–3 against 2025 pp. 1–2), Schedule 1 (2026
   pp. 2–3 against 2025 pp. 1–2) and Schedule A (2026 pp. 2–3 against 2025 p. 1) line by line. I also ran a
   word-level, year-shifted diff of Schedule B, Schedule D, Form 8949, Form 8889, Form W-2 and the Schedule B
   instructions. I read Schedule 3-A, Form 1062, the i1062 What's New, the i8889 What's New and Reminders, the
   iw2w3 What's New and Reminders, and the Public Law and Rev. Proc. passages each entry cites.
2. **All 44 "rule (definition change)" and "new line or form" entries in the other sections.** I read the 2026
   pages behind each one: Schedules 1-A, 2 and 3, Form 8959, Form 8995, Form 5695, the i2441 phaseout table,
   Form 8880, i8863, i5329, i1099r, the f8962 claims, the PTC sections of P.L. 119-21, i1040sc and rp-26-15.
3. **All 20 "amount (parameter)" entries.** I checked each against its source and against the final Rev. Proc. or
   Notice where one is archived (rp-25-32, rp-25-19, rp-25-25, n-25-67, rp-26-15, p15, iw2w3, fr-2025-01377).
4. **31 of the 38 "wording only" entries outside C-PRI, read closely against both editions.** I checked the other 7
   only for quotes and ids; they are listed below. All 7 C-PRI wording entries were checked in full under item 1.
5. **What's New completeness** for i8889, iw2w3, i1040s8812, i2441, i8863, i5329, i8606, i1040sc, i8960 and i8995.
   I also checked i1040sb, i1099int and i1040se.
6. **Every "no 2026 source" claim** against `manifest.json`. All are true: i1040gi, i1040sca/i1040sa, i1040sd,
   i8949, i8962, i4562, i8995a, p946, i8582, p970, p590a, p560, p501, p463 and a Schedule 3-A instruction are
   absent. The byte-identical claims also hold: f1099int, f1099div, f8283, i1099div, i8283, f6198, i6198,
   f1099c, i1099ac, f1099sa, i982, p529 and p538 have identical PDFs in both archives.

I checked every quote with my own script. All 672 quotes are printed on the cited page (in one of the two text
layers). Every dotted id and enum or table name in the Touches and Worklist lines exists in the 2025 encoding,
except the ones the map itself marks as new (`f1040.line12f`, `sa.line8d`, `e24`).

**Result.**
- 116 entries confirmed with no correction (103 checked in full, 13 checked for quotes and ids only).
- 16 entries need a correction (C-PRI-03 only through the C-PRI-04 row).
- 19 correction rows in all.
- 2 corrections are not tied to an entry: a missing 2026 statutory change and missing iw2w3 What's New rows.
- By severity: 2 high, 11 medium, 7 low.

## Corrections

| entry id | what the map says | what the source says (doc, page) | severity | proposed correction |
|---|---|---|---|---|
| C-PEOP-26 | Title: "PTC limited to certain lawfully present aliens". Notes: "Sec. 71301 (p. 251) also limits the credit to "eligible aliens"". Presented as a 2026 change. | `plaw-119-21` p. 252, sec. 71301(e): "The amendments made by this section (other than the amendments made by subsection (c)) shall apply to taxable years beginning after December 31, 2026." Sec. 71301 does not apply to 2026. Only sec. 71302 (p. 253, "taxable years beginning after December 31, 2025") applies. | high | Retitle to "Below-100% lawfully present alien branch repealed (sec. 71302)". State that sec. 71301 (eligible aliens) first applies to taxable years beginning in 2027, so it is out of scope for 2026. |
| (missing; PEOP section, Form 8962) | Nothing. The map cites sec. 71302 and 71305 but not sec. 71304. | `plaw-119-21` p. 254, sec. 71304: a qualified health plan "shall not include any plan enrolled in during a special enrollment period provided for by an Exchange— (I) on the basis of the relationship of the individual's expected household income to such a percentage of the poverty line ... and (II) not in connection with the occurrence of an event or change in circumstances". Its effective date: "shall apply with respect to plan years beginning after December 31, 2025." | high | Add a PEOP entry, kind "rule (definition change)". Touches: the coverage months behind `f8962.line7` and `ptc.months` (Form 1095-A inputs); a new refusal question (was any month's coverage enrolled in through an income-based special enrollment period?). The rule rests on the statute (final). The 2026 i8962 is not archived. Sec. 71303 (pp. 253–254) applies only after December 31, 2027; note it as out of scope. |
| C-PRI-17 | Notes: "Whether the 90% applies before the limit to winnings ... is for the 2026 instructions (not posted)". The Touches line's "90% of losses, limited to gains" is right. | `i1040se` p. 2 (draft): "You must apply the 90% limitation first then apply the gambling winnings limitation." `i1040sc` p. 2 (draft): "your gambling losses are limited to the lesser of (i) 90% of your gambling losses or (ii) gambling winnings". The BUS table sends both What's New items to the Schedule A rule, but C-PRI does not account for them. | medium | Cite both 2026 drafts in C-PRI-17 and settle the order: smaller of 90% of losses and winnings. Keep open only how winnings reported on Schedule C or E enter (the new 17a box). Add both What's New items to the C-PRI What's New table, pointing to C-PRI-17. |
| C-PRI-04 (and C-PRI-03) | Touches: "a new refusal gate (no 2025 id)" only. Notes: line 15 is "25% of the net tax". | `f1040s3` p. 2 (draft): "13e Total section 1062 applicable net tax liability. Enter amount from Form 1062, line 14". `f1062` p. 2 (draft), line 15: "Enter 25% (0.25) of line 14", where line 14 is the "Total section 1062 applicable net tax liability" (Part III). | medium (touch); low (wording) | Add Schedule 3 line 13e and its readers (`s3.line14`, `s3.line15`, `f1040.line31`, then line 32a) to C-PRI-04 and C-PRI-03, cross-referenced to C-SCHED-39. The election puts line 14 into payments and line 15 into tax. Reword the note to "25% of line 14 (the section 1062 applicable net tax liability)". |
| C-PRI-11 | Kind: wording only. Line 14 reworded. | `f1040s1` p. 3 (draft): "14 Moving expenses for members of the Armed Forces and the intelligence community". `plaw-119-21` p. 95: "(2) MEMBERS OF THE INTELLIGENCE COMMUNITY.—An employee or new appointee of the intelligence community ... who moves". This widens who may take the deduction. | medium | Split line 14 into its own entry, kind "rule (definition change); not encoded (refused through `scope.schedule1`)". The `scope.schedule1` question and refusal text need no change in substance; record the wider class. |
| C-PRI-11 | Touches: "labels of `s1.line1` ... `s1.line11`, `s1.line18` ... `s1.line20`". | These labels are printed the same in both years (`f1040s1` 2025 p. 1–2, 2026 p. 2–3). Only sub-line letters (2b, 8a–8z, 19b–c, 24a–z) gained their number. | low | Say these ids are listed only because the worklist flagged them, not because their labels change. |
| C-PRI-25 | Touches: `w2.over` and "the excess social security credit parameters". Notes: the 2026 maximum is quoted "only if a 2026 source prints it". | `params/2025.yaml` holds `ss.base` (17610000) and `ss.limit` (1091820). `forms/2025/person.yaml` `person.excess` has the label "Withholding above $10,918.20" and a remedy with the same figure. `iw2w3` p. 19 (final): "For 2026, the amount should not exceed $11,439 ($184,500 × 6.2%)". | medium | Name `ss.base`, `ss.limit`, `person.excess` and `w2.over` in Touches. Give 2026 values $184,500 and $11,439, cited to `iw2w3` p. 19 and `p15` p. 2 (both final). |
| C-PRI-28 | `retirement_account` is "(figures near the citation in `f1099r`; wording)". | `f1099r` p. 9 (final): "Box 7b. If the IRA/SEP/SIMPLE box is checked, you've received a traditional IRA (other than a Trump account), SEP, or SIMPLE distribution." `i1099r` p. 1: "we added boxes 7c (Trump account) and 7d". The enum's cite rests on "the IRA/SEP/SIMPLE box", which now excludes Trump accounts. | medium | Change the kind for `retirement_account` to "rule (definition change)". Cross-reference C-PEOP-04 and C-PEOP-11 (a Trump-account distribution needs a refusal or a value). |
| C-SCHED-17 | Kind: rule (definition change). | `f1040s2` 2026 pp. 2–3 (draft): "16c Total additional social security and Medicare tax. Add lines 16a and 16b" is 2025 lines 5+6, and 17c is 2025 line 13 (`f1040s2` 2025 p. 1). The entry's own notes: "Only the labels, citations and refusal text change." | medium | Change the kind to "wording only (cross-reference)". |
| C-SCHED-18 | Kind: rule (definition change). | `f8959` p. 2 (draft): line 18 "Additional Medicare Tax on self-employment income" and line 11 "Additional Medicare Tax on RRTA compensation" are 2025 lines 13 and 17 renumbered (`f8959` 2025 p. 1). The amounts are the same. | medium | Change the kind to "wording only (cross-reference)". The re-pointing of `s8812.amt_ws7` is bookkeeping that follows C-SCHED-13. |
| C-CRED-17 | Kind: rule (definition change). Notes: "No numeric effect". | `f1040` p. 3 (draft): "11b Amount from line 11a (adjusted gross income)". Line 11a and line 11b are the same amount. | medium | Change the kind to "wording only (cross-reference)". |
| (C-PRI What's New table, `iw2w3`) | Lists PFML, wage threshold, box 14a/14b split, TP, TT, TA, penalties, and Reminders. | `iw2w3` p. 1 (final), What's New: "The Form W-2c was released in January 2026 and has a revision date (Rev. 1-2026)" and "Changes to boxes 9 and 14a on the 2026 Forms W-2 ... Box 9 was reduced in size so that an additional entry can be input into box 14a." Neither is in the table. | medium | Add two rows, both "not encoded: employer form layout (W-2c revision; box 9 / 14a sizes)". |
| C-CRED-14 | Touches: "parameter `qr.gross_income_limit` holds the same 2025 figure for the dependent tests (another group)". | `rp-25-32` p. 20 (final), § .23: "the exemption amount referred to in § 152(d)(1)(B) is $5,300." No entry in any section updates `qr.gross_income_limit` (`params/2025.yaml`: 520000). | medium | Add `qr.gross_income_limit` = 530000, cited to `rp-25-32` p. 20, either to C-CRED-14 or as a PEOP amount entry. Have `f2441.nondependent` read it. |
| C-CRED-11 | Touches: `dc.exclusion_max`, `f2441.exclusion_max`, `f2441.plan_max`, `f2441.line21`. | `forms/2025/w2.yaml`: `w2.box10_wages` prompts "it is often the amount of box 10 over $5,000", and the `w2.box10` cite quotes "the $5,000 exclusion". The 2026 final `iw2w3` p. 19 still prints "including those in excess of the $5,000 exclusion". That disagrees with `i2441` p. 7 (draft), "The maximum amount is increased to $7,500". | medium | Add `w2.box10` and `w2.box10_wages` to Touches. Record the iw2w3 (final) and i2441 (draft) disagreement for the adoption; the $7,500 applies only if the plan was amended. |
| C-PRI-22 | The What's New table maps "1. Telehealth and Remote Care Services" to C-PRI-22. | C-PRI-22 does not mention telehealth. `i8889` p. 2 (draft): "effective for plan years beginning after 2024". `plaw-119-21` p. 255, sec. 71306: "shall apply to plan years beginning after December 31, 2024". This is no change from 2025. | low | Map the telehealth row to "not encoded: unchanged from 2025 (already effective for 2025 plan years)", or mention it in C-PRI-22. |
| C-PRI-21 | Worklist items: `f8889.rollover`. | The C-PRI coverage table maps `f8889.rollover` to C-PRI-23 only, and C-PRI-23 also lists it. | low | List `f8889.rollover` under one entry only (C-PRI-23), or add C-PRI-21 to the coverage row. |
| (C-PRI What's New table, `rp-25-32`) | Section 2 is listed as .01–.12 and .14–.16. | `rp-25-32` p. 7: "13 Section 70115 of the OBBBA amended § 529A(b)(2)(B)(i) ... the inflation adjustment to the amount under § 529A(b)(2)(B)(i) is separately added". | low | Add a row for .13 (ABLE contribution limit): "not encoded: ABLE contributions are not computed". |
| C-SCHED-30 | "Possible draft error" for the MFS $201,775. "Values to use: the values above, all from the draft." | `rp-25-32` p. 22 (final), § .26 table: "Married Individuals Filing Separate Returns $201,775 $276,775"; "All Other Returns $201,750 $276,750"; joint "$403,500 $553,500". | low | Cite `rp-25-32` p. 22 (final) and drop the draft-error caution. The values are confirmed. |
| C-BUS-16 | "(from a draft; confirm against the final Form 7206 when posted)". | `rp-25-32` p. 22 (final), § .27: "40 or less $500 ... More than 40 but not more than 50 $930 ... More than 50 but not more than 60 $1,860 ... More than 60 but not more than 70 $4,960 ... More than 70 $6,200". | low | Cite `rp-25-32` p. 22 (final). The values are confirmed. |

## Entries confirmed without correction

- **Quote, kind, touched ids and claims checked against the sources (103).**
  - Priority: C-PRI-01, C-PRI-02, C-PRI-05, C-PRI-06, C-PRI-07, C-PRI-08, C-PRI-09, C-PRI-10, C-PRI-12, C-PRI-13,
    C-PRI-14, C-PRI-15, C-PRI-16, C-PRI-18, C-PRI-19, C-PRI-20, C-PRI-23, C-PRI-24, C-PRI-26, C-PRI-27, C-PRI-29.
    C-PRI-03 is confirmed apart from the cross-reference in the C-PRI-04 row.
  - Schedules: C-SCHED-01, C-SCHED-02, C-SCHED-03, C-SCHED-04, C-SCHED-05, C-SCHED-06, C-SCHED-07, C-SCHED-10,
    C-SCHED-11, C-SCHED-12, C-SCHED-13, C-SCHED-14, C-SCHED-16, C-SCHED-19, C-SCHED-20, C-SCHED-21, C-SCHED-22,
    C-SCHED-23, C-SCHED-24, C-SCHED-25, C-SCHED-26, C-SCHED-27, C-SCHED-28, C-SCHED-29, C-SCHED-31, C-SCHED-32,
    C-SCHED-33, C-SCHED-36, C-SCHED-39.
  - Credits: C-CRED-01, C-CRED-02, C-CRED-03, C-CRED-04, C-CRED-05, C-CRED-06, C-CRED-07, C-CRED-08, C-CRED-09,
    C-CRED-10, C-CRED-12, C-CRED-15, C-CRED-16, C-CRED-18, C-CRED-19, C-CRED-20.
  - People: C-PEOP-01, C-PEOP-02, C-PEOP-03, C-PEOP-04, C-PEOP-05, C-PEOP-06, C-PEOP-07, C-PEOP-08, C-PEOP-09,
    C-PEOP-10, C-PEOP-11, C-PEOP-12, C-PEOP-13, C-PEOP-14, C-PEOP-15, C-PEOP-16, C-PEOP-17, C-PEOP-18, C-PEOP-19,
    C-PEOP-20, C-PEOP-21, C-PEOP-22.
  - Business: C-BUS-01, C-BUS-02, C-BUS-03, C-BUS-04, C-BUS-05, C-BUS-06, C-BUS-07, C-BUS-08, C-BUS-09, C-BUS-10,
    C-BUS-11, C-BUS-12, C-BUS-13, C-BUS-14, C-BUS-17.
- **Quotes and ids checked and text read, but no further independent comparison (13):** C-SCHED-08, C-SCHED-09,
  C-SCHED-15, C-SCHED-34, C-SCHED-35, C-SCHED-37, C-SCHED-38, C-PEOP-23, C-PEOP-24, C-PEOP-25, C-BUS-15, C-BUS-18,
  C-CRED-13.

The What's New checks found nothing missing beyond the rows above. i1040s8812, i2441, i8863, i5329, i8606, i8960 and
i8995 are each fully accounted for. i8889 (apart from the telehealth mapping) and i1040sc (apart from the gambling
item) are too.

## What I could not check, and why

- **The 2025 line instructions behind the "waits on i1040gi" entries** (C-PEOP-23, C-PEOP-24, parts of C-SCHED-01,
  -03, -05, -08 and C-BUS-17). The 2026 i1040gi, i1040sca, i1040sd, i8949, i8962, i4562, i8995a, p946, p970,
  p590a, p560, p501 and p463 are not archived, so there is no 2026 text to compare.
- **The worklist itself** (`reports/2026/worklist_split.md`) is outside the allowed sources. I did not check that
  every kind-(a) item is covered. I checked only that the coverage tables name existing ids and entries.
- **The 2025 Rev. Proc. 2024-40 (`rp-2024-40`) section numbers** cited in C-PRI-12, C-PRI-27 and C-PEOP-12. I
  checked only that the quotes are printed; the map proposes no 2026 values in C-PRI-12 or C-PRI-27 (it defers
  them to step 4).
- **Whether other 2026-effective sections of P.L. 119-21 touch encoded lines** beyond those the map cites. I read
  the PTC and HSA sections (71301–71308) and the itemized-deduction sections (70108–70116, 70424–70425). A full
  sweep of the statute was not done; the sec. 71304 omission suggests the other sections deserve the same pass.
