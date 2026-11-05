> Adversarial verification of `ny-it201-nyc-resident.md` by an independent Claude subagent that did not write the map, 2026-11-04: 14 errors (1 medium, 13 low), 8 omissions (1 medium). No number in the tables is wrong. Read this file with the map; where the two differ, this file has re-read the source.

> **Integrator's note (2026-11-04, the writing session):** while this verification ran, the map's §4.3 sentence that E6
> quotes was replaced by a computed consistency note that reaches E6's conclusion independently (the printed bases are
> roundings of the exact running total; head of household at $5,000,000 is the one place the two methods differ), and a
> recapture-amount consistency note was added to §4.4. The map is otherwise unchanged; every other finding below
> stands, and the owner's decision batch (`docs/ny/DECISIONS.md`) takes in E7, E8, E9, E10, E13 and M1.

# Verification: research/premises/ny-it201-nyc-resident.md

Checked read-only against `sources/ny/2025/` on branch `ny/2025-foundation`. Sources used:
- `ny_it201` (layout text, pp. 1–4) for line numbers and labels;
- `ny_it201i` (reading-order text pp. 2–41, with layout text for pp. 13, 14, 33 and 40, and a rendered image of p. 36);
- `ny_it201i-html` for every table and every filing-status digit;
- `ny_it201_tax_tables`, parsed by a script outside `sources/` into rows, with spot checks;
- `ny_it201att`, and `ny_it270i` (text plus a rendered image);
- `forms/2025/*.yaml` for the federal ids.

The map holds 234 double-quoted strings. I read the source pages behind all of the rule quotes in sections 2 to 6 by hand. The errors below concern locators, context and inference. No quote was missing from the archive. Personal data was neither used nor sought. No network or model calls were made.

## Errors

E1. **Wrong page for the MCTMT text** (§3.7, row 54a–54e). The map cites `ny_it201i p. 14`, Lines 54a through 54e, "If an individual’s net earnings from self-employment allocated to either zone exceed $50,000 for the tax year, then you are subject to the MCTMT.", and gives the Zone 1 counties at "(`p. 14`)". Both are on p. 15: the heading "Lines 54a through 54e: Metropolitan Commuter Transportation Mobility Tax (MCTMT)" and the Zone 1 list ("Zone 1 includes the counties of: – Bronx – Kings (Brooklyn) – New York (Manhattan) – Queens – Richmond (Staten Island)"). Page 14 ends inside Line 51. Severity: low. Correction: change both locators to `ny_it201i p. 15`.

E2. **Wrong page for Line 70** (§3.9, row 70). The map cites `ny_it201i p. 20`, Line 70. The heading "Line 70: New York City earned income credit (New York City residents only)" and "Did you claim the federal earned income credit for 2025 on your federal return, or could you have claimed it based on your federal adjusted gross income?" are on p. 21, after the rate-reduction tables. Severity: low. Correction: `ny_it201i p. 21`.

E3. **Line 28 locator** (§3.4). The map cites "`ny_it201i p. 8–9`, Line 28". The whole of Line 28 is on p. 9, including "the 50% asset requirement each quarter". Page 8 ends with Line 25. Severity: low. Correction: `p. 9`.

E4. **Wrong cross-reference for line 47a** (§3.7, row 47a, "Section 4.4"). Section 4.4 is the State recapture worksheets. The City tax is in Section 4.5. Severity: low. Correction: 'Section 4.5'.

E5. **Line 20: what the interest-date and bond-premium rules do** (§3.3, row 20: 'bond premium and purchase between interest dates (same page) send amounts to IT-225 or IT-196').
- `ny_it201i p. 7`, Line 20: for a bond bought or sold between interest dates you "include the amount of interest you received during the year, after subtracting the seller’s accrued interest" (or "plus the accrued interest amount" on a sale). That adjusts the line 20 amount itself. Nothing goes to IT-225 or IT-196.
- Bond premium "is not allowed as a direct offset to interest income". It goes on IT-225 only "if the bond premium is attributable to a trade or business". Otherwise it goes on "Form IT-196, line 44 ... but only if you itemize".
- So for the standard-deduction target, non-business premium is never deducted. A line 20 computed under D5 must not net premium against interest.

Severity: medium (it bears on D5). Correction: state the two rules as above.

E6. **The proposed rate-schedule consistency check fails on one printed base** (§4.3, 'Each base can be checked against the band below it (for example 686 = 4% of 17,150)', inferred).
- The head of household row reads "5,000,000   25,000,000   434,163 plus 10.3%" (`ny_it201i p. 33`; the web edition prints the same).
- From the printed base below it, 107,651 + 9.65% × 3,383,550 = 434,163.575, which rounds to 434,164.
- The printed 434,163 comes from the unrounded chain (434,163.475).
- Every other base in the State and City schedules passes both ways.

A Phase 3 check built on printed bases would report a false defect. Severity: low. Correction: 'check each base against the unrounded cumulative tax, or allow $1'.

E7. **The proposed State residency question misstates the test** (§6, residency (State), 'domiciled in New York, or keeping a permanent place of abode there and spending 184 days or more there').
- `ny_it201i p. 30`, Resident: "You maintain a permanent place of abode in New York State for substantially all of the tax year and spend 184 days or more in New York State during the tax year*".
- The domicile limb has exceptions: "even if your domicile is New York, you are not a resident if you meet all three of the conditions in either Group A or Group B".
- The proposed wording drops "for substantially all of the tax year" and the Group A/B exceptions.

Severity: low (the wording is proposed). Correction: add both, or ask the filer to confirm full-year resident status with a pointer to p. 30.

E8. **Checklist thresholds are incomplete** (§7 item 9, 'federal AGI was under $32,000 or $22,500'). Those are the table 2 and table 5 limits. For a single filer the limits are $28,000 for the State credit (table 1, "28,000 ... No credit is allowed") and $12,500 for the City credit (table 4, "12,500 ... No credit is allowed"). The tables also use "but not over", not "under". Severity: low. Correction: 'not over $28,000 / $12,500 (single) or $32,000 / $22,500 (statuses ②④⑤)'.

E9. **The line 81 safe harbor is understated** (§3.10, row 81, '110% above $150,000 of 2024 New York AGI'). `ny_it201i p. 23`: "if your 2024 New York adjusted gross income was more than $150,000 (or $75,000 if you are married filing separately for 2025) and you are not a farmer or a fisherman, your 2025 prepayments must equal at least 110% of your 2024 New York income tax based on a 12-month return." Severity: low. Correction: add the MFS $75,000, the farmer/fisherman exception and "based on a 12-month return" to D12.

E10. **The 69a ambiguity leaves out the definition's own scope words** (§5.3, Ambiguity (69a), 'the definition of "income" is printed above, under line 69').
- The definition is printed after Table 2, immediately before the Line 69a heading.
- It reads "Income, for purposes of determining your New York City school tax credit, means your federal adjusted gross income from Form IT-201, line 19, minus distributions ..." (`ny_it201i p. 20`; web edition, same).
- Its scope is the school tax credit without qualification. Both lines carry that name ("New York City school tax credit (fixed amount)", "New York City school tax credit (rate reduction amount)").

This supports reading (a). The "(see below)" in 69a still points forward to "New York City taxable income (see below)", so registering the ambiguity remains reasonable. Severity: low. Correction: quote the scope words in D14 and say that they favour (a).

E11. **"Halved and rounded" is an inference presented as fact** (§5.1 Table 3, §5.2 Table 6). The source says only "Note 5 The credit amounts have been rounded." (`ny_it201i pp. 13, 14`). Every cell of tables 3 and 6, including the "over 7" column, does equal half the table 2 or table 5 cell rounded half-up (checked: 105/2 = 52.5 → 53, 15/2 = 7.5 → 8, 25/2 = 12.5 → 13, 5/2 = 2.5 → 3). The encoding should still use the printed cells. Severity: low. Correction: mark it 'inferred; matches every printed cell'.

E12. **An unmarked inference about the first worksheet of each group** (§4.4, 'phases the whole of taxable income into the flat rate of the bracket that contains the start of the phase-in'). For head of household the phase-in starts at $107,650, which is the top of the 5.5% bracket ("20,900   107,650   901 plus 5.5%", `ny_it201i p. 33`). Worksheet 12 uses "Multiply line 2 by 6% (0.06)", the rate of the next bracket. Severity: low. Correction: 'the rate of the bracket just above $107,650', marked inferred.

E13. **Item A: one exception has a joint option the map does not mention** (§3.1 row A, 'Exceptions only for married couples filing jointly federally ... "you may file a separate New York return using filing status"').
- For a resident spouse married to a nonresident or part-year resident, `ny_it201i p. 4` gives two choices (digits from `ny_it201i-html`, Item A): "file separate New York returns using filing status ③; or" and "file jointly, as if you both were New York State residents, using filing status ②."
- `p. 3` adds: "if you both choose to file a joint New York State return, use Form IT-201 and both spouses’ income will be taxed as full-year residents".
- The "you may file a separate" quote belongs to the other two exceptions (whereabouts unknown; refusal to sign), on p. 5.

Refusing all of these cases is still a valid scope choice, but the premise as written is incomplete. Severity: low. Correction: state the joint-as-residents option and note that it brings in the line 51 separate-sheet City rule (p. 15).

E14. **The §9 claim "Verified ... every double-quoted string above, at its locator" is overstated.** E1 to E3 are quotes at the wrong locator. The script that checked page presence evidently did not catch them. Severity: low. Correction: qualify the claim, or re-run the check with page-exact matching.

## Omissions

M1. **The arithmetic of lines 77 to 80 and how line 81 and line 82 interact** (§3.10). The printed labels of lines 77 and 80 do not show what the instructions require, and the map gives line 80 no formula:
- line 77 is net of the estimated tax penalty only (`p. 22`, "subtract the penalty from the overpayment and enter the net overpayment on line 77");
- "If your estimated tax penalty on line 81 is greater than your overpayment on line 77, enter the difference on line 80";
- line 80 is "the amount of tax you owe plus any estimated tax penalty you owe ... and any other penalties and interest you owe" (`p. 23`);
- `p. 24`: "Do not include any other penalty or interest amounts on line 77";
- `p. 23`: "The total of lines 78a through 79 should equal the amount on line 77."

The encoding needs these as rows, or a statement that lines 81 and 82 are fixed at zero (D12, D13). Severity: medium.

M2. **Who must file** (`ny_it201i p. 3`): "your federal adjusted gross income for 2025 plus New York additions was more than $4,000 ($3,100 if you are single and can be claimed as a dependent on another taxpayer’s federal return)", and the refund-claim condition. These are needed if the tool ever says no return is required. Low.

M3. **Line 59 details** (`p. 18`; web edition):
- The chart's middle bands (all verified: $3, 6, 10, 15, 18, 26, 34) are elided in the map.
- Its footnote "*This may be any amount up to $15,000, including 0 or a negative amount." is missing.
- So is "If the amount reported on line 59 is $1,700 or more, you must complete Form IT-135".
- So is the part-year abode proration, which is moot for the target.

Low.

M4. **Form items not listed separately** (§3.10, "83, 84 account and withdrawal information"):
- line 83's account-outside-the-U.S. box, and lines 83a, 83b and 83c (`ny_it201 p. 4`);
- line 84 "Date Amount";
- the line 80 electronic funds withdrawal box and the line 78b refund choice;
- item H's "If more than 7 dependents, mark an X in the box" (p. 1);
- the fiscal-year header (p. 1), and the third-party designee.

None is computed, but the completeness claim should name them. Low.

M5. **NOL** (`ny_it201i pp. 31–32`, "your NOL deduction is limited to the lesser of: • your federal NOL deduction, or • your federal taxable income calculated without the NOL deduction"). This is moot because `scope.schedule1` refuses "a net operating loss deduction" and `s1.line9` has no line 8a. A one-line note would close it. Low.

M6. **Form IT-2 as an attachment.** `p. 21`: "You must complete a W-2 record for each W-2 you receive, even if it does not show any New York State, New York City (NYC), or Yonkers wages or tax withheld." The map treats IT-2 only as a source of totals for lines 72 to 74. Low.

M7. **Line 70a's zero rule could use more of IT-270-I.**
- Other conditions in `ny_it270i p. 1` also make the credit zero: "you did not claim NYC or New York State pass-through entity tax (PTET) credit", and Line D, "You cannot claim this credit if your investment income is more than $10,000".
- The threshold depends on the number of dependents, so a zero test can use the count's own threshold plus $5,000 rather than the highest one.

The map's rule is sound but refuses more often than it needs to. Low.

M8. **Line 69 special rules for joint filers with different City residency** (`p. 20`, "Special rules for married filing joint return (filing status ②)"). These are covered by the spouse-residency refusal, but that screen's cite should include them. Low.

## Unverifiable

- **Line 25 against line 4** (D6). Both texts are confirmed as the map quotes them (form p. 2 "(from line 4)"; IT-201-I p. 8 and the web edition speak only of the inflation refund check). The archive cannot settle which governs.
- **The 69a "income" reading** (D14). See E10. The NYC Administrative Code is not archived.
- **Direction of "round the result to the fourth decimal place"** (worksheets 1 to 16). It is not printed.
- **Eligibility tests in unarchived credit forms**: IT-213, IT-214, IT-215, IT-216, IT-209, IT-272 and IT-270 itself. Line 67's test (real property tax credit for renters) in particular cannot be stated from the archive.
- **Whether the July 2026 web edition changed wording** relative to the PDF beyond what the README's word and number checks cover. Every number in every table I compared is identical in both.
- **The asterisks on "17,500*", "20,000*" and "22,500*"** in PDF tables 5 and 6 (p. 14). Confirmed present with no footnote on the page; the web edition prints none. Their meaning cannot be found in the archive.

## Confirmed

- **Form completeness** (`ny_it201` pp. 1–4): lines 1–84 are present in the map in printed order, with 47a, 54a–54e, 69a, 70a, 78a and 78b, and items A–H. Labels quoted for lines 1–34, 37, 38, 43, 44, 46, 49, 54, 58, 59, 61, 62, 76, 77 and 78b match the form. There is no misnumbered line. The only gap is the sub-items in M4.
- **Standard deduction** (6 amounts, web edition and PDF p. 11): $3,100 / $8,000 / $16,050 / $8,000 / $11,200 / $16,050, all correct.
- **State rate schedule** (27 rows over 3 status groups, web edition and PDF p. 33): every bound, base and rate is correct. Base consistency holds except E6.
- **Recapture worksheets** (web edition and PDF pp. 34–39; page 36 image-checked):
  - for all 16 worksheets, the NY AGI and taxable-income conditions, the $25,000,000 cap and the $157,650 stop on worksheets 1, 7 and 12 are correct, as are the 5.5% / 6% / 6% rates and 10.9% on 6, 11 and 16;
  - all 20 Recapture Base and Incremental Benefit amounts on worksheets 2–5, 8–10 and 13–15 are correct;
  - the coverage inference holds: within each group the taxable-income bands are contiguous, and taxable income cannot exceed NY AGI when NY AGI is positive.
- **City rate schedule** (12 rows, web edition and PDF p. 40): correct, and the bases are consistent.
- **Tax tables** (web): the State and City tables each have 1,302 contiguous rows. The State table's first bands are 0–13, 13–25 and 25–50, and the City table's are 0–18, 18–25 and 25–50; both then run in $50 bands to 64,950–65,000. The columns, the qualifying-surviving-spouse footnote, the $107,650 rule and both examples are as quoted. $1,773 and $1,292 equal the rate schedule at the $38,275 midpoint. The last State single cell (3,409) also matches the schedule.
- **Household credit tables 1–6** (all 126 cells, web edition and PDF pp. 12, 14), together with Notes 1–5 and the status-to-table assignment from the web edition digits.
- **School tax credit**: Table 1 ($63 / $125, "$250,000 or less"), the income definition, the $500,000 limit for 69a, and all six cells of the rate-reduction tables (bases 37, 21 and 25 equal 0.171% of 21,600, 12,000 and 14,400).
- **Sales and use tax chart**: all 8 bands and the top-band formula.
- **IT-270-I**: all 15 thresholds (MFJ/QSS 1–6 and "7 or more" $91,902; others 1–7 and "8 or more" $88,361, read from the page image), the "$5,000 above" and "$10,000 or less" conditions, and the line 70a transfer.
- **MCTMT**: rates 0.60% and 0.34%, the individual $50,000 threshold, and Schedule SE Part I line 6.
- **IT-201-ATT line references** (lines 7, 10, 18, 30 and 34 to IT-201 lines 42, 53, 71, 45 and 51); Part 3 is the IT-230 lump-sum taxes.
- **Rules re-read with no discrepancy**: items A–H, special accruals (the City test covers the State test for this target), line 37/38 blank rule, line 39 method choice, line 47 (Charitable Gifts Trust Fund worksheet needs itemizing), lines 63–68, 71–75 and 78–79, and the p. 2 credit-form reminder.
- **Federal ids**: all 27 ids named in §9 exist in `forms/2025/`. `sa.dependent` is refused federally (`sa.yaml` and `eic.yaml`) and carries the quoted "Answer no if ..." text. `f8962.deps` counts `dependent.claimed`.
- **Federal state withholding**: no federal entry holds state or local withholding (no W-2 box 15–20 fields), which supports D2.
- **The line 2–18 mapping**: plausible and complete. `s1.line10` = lines 1 + 2a + 3 + 7 + 9, and these map to IT-201 lines 4, 5, 6, 14 and 16. Schedule 1 lines 4, 5 and 6 (and the 8a NOL) are refused federally. `f1040.line9` sums 1z, 2b, 3b, 4b, 5b, 6b, 7a and 8, so IT-201 line 17 equals it before rounding. No federal AGI component lacks an IT-201 home. Item D1 to `sb.line7a` is sound, because `sb.line8` (foreign trust, the other Part III question) is refused federally.
