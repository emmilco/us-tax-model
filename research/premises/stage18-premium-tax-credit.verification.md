> Adversarial verification of `stage18-premium-tax-credit.md` by an independent read-only agent after Stage 15 (commit 1c465c2): 7 errors and 5 items out of date. Read it with the map; where they differ, the verification has checked the source.

# Verification: research/premises/stage18-premium-tax-credit.md

Checked at commit 1c465c2. The working tree also has uncommitted changes to fixtures/2025/stage15.json, handoffs/HANDOFF-STAGE-15.md and TASKS.md. Page N means the N-th form-feed chunk of `<id>.cols.txt`. Every quoted source passage in the map was located page by page with a script (kept outside the repo, in /tmp/verify18_scripts/). Every quote the map attributes to a page was found on that page. The one quote not found in `.cols.txt`, the Form 8962 line 4 text, is in `f8962.txt` lines 19 and 20; the column extraction splits it.

## Errors

**E1. "Nothing refuses it" (s3.line9) leaves out `scope.credits`.** The map says this in section 0 bullet 1 ("Nothing refuses it: a filer with a net PTC can type the figure in"). Section 1.1 says the same ("the 2.4 million with a net PTC are not refused"), and section 5.2 never lists `scope.credits`.
- What the source says: forms/2025/scope.yaml line 22 asks "Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit, the earned income credit, the credit for child and dependent care expenses (Form 2441), the retirement savings contributions credit (Form 8880) and the residential energy credits (Form 5695), or do you have any other amount for Schedule 3 Part I ...?"
- The premium tax credit is not on that list. The refusal's form names "Form 1040 lines 29 to 31" (scope.yaml line 69), and line 31 carries Schedule 3 line 9.
- Read literally, a filer claiming a net PTC answers yes and is refused. The wording at fcd2c26 was the same, so this was true before Stage 15 as well.
- Effect on the stage: it must add the PTC to the `scope.credits` exception list (label, source and remedy). That change is missing from section 5.2 and decision 14.
- Decisions affected: 1 and 14.

**E2. The Q3 double rounding is not limited to cents in household income.** Q3 says "it arises only with cents in line 3". Decision 6 recommends accepting it "because it bites only with cents in household income".
- What the code does: `multiplyRateHalfUp` (engine/src/eval.ts line 299) rounds half-up to the cent, and `roundToUnit` (line 290) then rounds to the dollar.
- With a whole-dollar line 3 of D and a four-place line 7 of r/10000, the product in cents is D·r/100. When D·r mod 10000 is between 4950 and 4999, the exact dollar fraction is 0.4950 to 0.4999, which the instructions round down. The engine rounds the cents to 50, then rounds the dollar up.
- I ran the engine's two functions over D = 1 to 199,999 at r = 0.0850 and 0.0603: 2,000 mismatches, about 0.5%. Example: household income $60,347 at 0.0850 is exactly $5,129.495. i8962 p. 12 rounding gives $5,129; the engine gives $5,130.
- The premise behind recommending acceptance is false. The rounding-unit alternative, or applying `round` to the exact product, deserves a fresh look.
- Decision affected: 6.

**E3. The line 10 test is narrowed to "counted" forms.** Section 3.2, line 10 says "every counted 1095-A has 12 months of coverage, the same column A each month and the same column B each month". Q5 says "on every counted form".
- What the source says: i8962 p. 14, "Check “Yes” and continue to line 11 if all of the following apply for each qualified health plan you or a member of your tax family was enrolled in for 2025", followed by the 12-month, same-premium and same-SLCSP bullets.
- So the enrollment and column A conditions apply to every Form 1095-A, not only to forms with `b_counted`.
- With the map's test, an uncounted second policy in the same state that started mid-year or changed premium would leave line 10 at Yes, when the text requires No. Annual and monthly results can then differ by more than rounding, because line 11(e) is min(Σa, Σd) while the monthly route is Σ min(a, d).
- Decisions affected: 10 and 13.

**E4. Table 5 has a third, authoritative printing in the archive.** Section 2 lists Rev. Proc. 2024-35 among the not-archived sources and says it would give "the 2025 repayment limitation amounts" and "an independent second printing of Table 5". Section 7.1 cites only i8962 and p974. Decision 15 says "the tables otherwise rest on one printing each".
- What the archive holds: `rp-2024-40` is in the manifest. rp-2024-40.txt lines 333 to 353, §3.07 "Refundable Credit for Coverage Under a Qualified Health Plan", says "For taxable years beginning in 2025, the limitation on tax imposed under § 36B(f)(2)(B) for excess advance credit payments is determined using the following table".
- That table gives "Less than 200%" $375 / $750, "At least 200% but less than 300%" $975 / $1,950 and "At least 300% but less than 400%" $1,625 / $3,250. The columns are "unmarried individuals (other than surviving spouses and heads of household)" and "all other taxpayers".
- These match the map's values. The `ptc.repay_*` parameters should cite rp-2024-40 §3.07, which is the source of the amounts.
- The single-printing concern stands for Table 2 and Tables 1-1 to 1-3 only. Whether Rev. Proc. 2024-35 contains repayment amounts at all cannot be checked offline.
- Decision affected: 15 and the section 7.1 locators.

**E5. The Chart B summary is narrower than the chart.** Section 4.8 says "for a single dependent, "Your unearned income was over $1,350." / "Your earned income was over $15,750."".
- What the source says: i1040gi p. 10, Chart B, single dependents under 65 and not blind, also has "Your gross income was more than the larger of— • $1,350, or • Your earned income (up to $15,300) plus $450". It also has separate amounts for age 65 or older or blind, and for married dependents.
- If the per-dependent "required to file" help is drafted from section 4.8, it will miss the gross-income test.
- Decision affected: 11.

**E6. The poverty-table rule is broader than the text.** Section 4.3 says the rule reduces to "Alaska if anyone on the return lived there in 2025, else Hawaii if anyone did".
- What the source says: i8962 p. 8, Line 4, "If you moved during 2025 and you lived in Alaska and/or Hawaii, or you are filing jointly and you and your spouse lived in different states, use the table with the higher dollar amounts".
- The text refers to you and your spouse, not dependents. "Anyone on the return" over-reaches, though the reduction is correct for the filer and spouse.
- Decision affected: the R18 Enum help (no numbered decision).

**E7. The no-cap alternative in Q2 does not give "the same results" with decision 3's table.** Q2 and the decision 2 alternative say that without the cap "Tables 2 and 5 give the same results either way".
- Decision 3 recommends a `keyed_lookup` with 402 rows, keys 0 to 401.
- The spec says the lookup is unknown when no row has the key (spec 4.2, keyed_lookup), so an uncapped line 5 above 401 would leave line 7 unknown.
- The claim holds only for the printed tables or a banded lookup.
- Decisions affected: 2 and 3 (they are coupled).

## Out of date after Stage 15

**O1. Coverage report figures (section 1.1).** The map says "The group's step is 4: '84.8% (+4.9)' after Steps 1 to 3, '+3.5' if covered alone now".
- reports/2025/filer_coverage.md (64.7%) now reads "| 3 | Premium tax credit (Form 8962) | 84.0% (+4.9) | +4.2 |".
- The 84.8% / +3.5 figures were the fcd2c26 report (58.0%).
- The refused-situations row is unchanged: 6.0%, 9,604,913 and 5.0%.
- Decision affected: 1 (scope priority).

**O2. Roadmap position (title, "spec 2.4 roadmap item 4").** spec/spec.md section 2.4 now lists "3. The premium tax credit (84%, the first goal)".
- So this stage is now the one expected to cross the 80% goal. That raises the stakes of the scope refusals in decisions 1 and 8.
- At fcd2c26 it was item 4 (85%).

**O3. Fixture counts (section 0).** The map says "648 cases set "s3.line9": 0, one sets it to 123; 617 set s2.other false and 10 true".
- At 1c465c2: 801 cases set `s3.line9` to 0 and 1 sets it to 123; 768 set `s2.other` false and 12 true.
- The working tree reads 802 and 769 because of an uncommitted change to stage15.json.
- The case with 123 is still stage2.json `ss.other.components`.
- Decision affected: 14 (fixture migration size).

**O4. Interview locator (section 5.2).** The map says "interview/questions-2025.yaml line 180". It is now line 181 (`- input: s3.line9`). Profiles 2025.yaml line 18 and stage4-2025.yaml line 59 still list it.

**O5. Stage 15 assumed, now landed (sections 0 and 5.1).** Assumptions it confirms: the Credit Limit Worksheets reading `f1040.line18` exist at f2441.yaml line 787, f8880.yaml line 517 and f5695.yaml lines 333 and 2054, and `rate_lookup` is as described (money key, Rate line).
- What the map missed: Stage 15 rewrote `scope.credits` to list Forms 2441, 8880 and 5695, and the PTC is still absent from that list (see E1).
- No saver's credit or energy credit register entry repeats the dc_rate "line 18 is zero" argument. `amb.2025.dc_rate_nonpositive_agi` (ambiguities/2025.yaml line 477) is the only one, and it already appears in TASKS.md as T-049.

## Unverifiable

- 26 U.S.C. 36B: whether 36B(d)(2)(A)(ii) points to section 6012 (Q7), and the claim that 71302 strikes the below-100% lawfully present alien rule. The statute is not archived. P.L. 119-21 only says "Section 36B(c)(1) is amended by striking subparagraph (B)".
- The contents of Rev. Proc. 2024-35 (9.02% and the repayment amounts), the HHS notice at 89 FR 2961, the About Form 8962 page and the URLs: none is archived, and I made no fetches. The 9.02% figure is confirmed in i8962 p. 5.
- That the 2026 Table 2 will differ (knowledge of the expiring enhancement).
- Q7's claim that "the literal text says no" for Chart C. Self-employment earnings of $400 or more is arguably income meeting a filing threshold. Item 5 (APTC paid) is clearly not. This is an interpretation, not a check.
- Decision 2's alternative "refuse every Form 8962 (no other route exists)": I did not prove there is no route through existing atoms. For example, money tests against `multiply_rate(line 4, p/100)` are exact in cents, though they cannot yield a Count or a Rate. This is an inference, not checked.
- Q1b: whether an unknown keyed helper off the chosen `choose` branch blocks a return. Spec 4.1 says "every reachable line is known". Spec 4.4's "Every line of every entry is evaluated" is about collection entries, while line 4 is a return-level line. Engine behaviour not tested.
- Sub-situation shares (none is measured, as the map says). The manifest marks soi-23in27aca "Pending inspection of archived document; not cleared for encoding", but its counts read correctly.

## Confirmed

I confirmed about 75 premises. The decision-critical ones:

- s3.line9 is an `input` with the quoted source; s3.line15 sums 9, 10, 11, 12 and 14; f1040.line31 copies s3.line15.
- s2 has no line 1a. s2.line2 and s2.line3 copy s2.zero and are refused on s2.amt or s2.other. s2.other's label and source name "repayment of excess advance premium tax credit". f1040.line17 copies s2.line3; f1040.line18 sums lines 16 and 17; f1040.line22 is line 18 less line 21 (floored at zero).
- categories.json `ptc`: gate `s2.other`, the quoted label, soi-23in27aca columns 3 and 5 combined by max, micro `premium_tax_credit`.
- SOI "All returns" row: 8,860,422 / 9,604,913 / 2,410,248 / 5,577,776 in columns 3, 5, 7 and 9.
- sa.dependent's refusal is at sa.yaml line 842. sa.excluded_income asks about Forms 2555 and 4563 and Puerto Rico income. scope.other_line16 names Form 8814. sc.hi_screen cites i1040gi p. 95, and that page has "Use Pub. 974 instead".
- Checker typing: sum, smaller_of and larger_of take money only; sum_over takes money or Count; choose branches are money only; rate_lookup needs a money key and a Rate line; the keyed_lookup cell may be Rate, Count, enum or money; there is no Count addition. multiply_count is money × Count line.
- Two engine behaviours: multiply_rate rounds half-up to the cent (eval.ts line 299), and keyed_lookup is unknown when no row matches (spec 4.2).
- s8812.clw_a1 reads f1040.line18 (s8812.yaml line 238); the FTC limit reads f1040.line16 (ftc.yaml line 151).
- `amb.2025.dc_rate_nonpositive_agi`'s reason rests on line 18 being zero with Schedule 2 refused, as the map says.
- The Form 8962 line texts and the Worksheets 1-1, 1-2 and 2 texts are on the cited pages (f8962 p. 1; i8962 pp. 8 to 9).
- Tables 1-1 to 1-3: all 24 amounts, the increments $5,380, $6,730 and $6,190, and the size-11 examples $68,860, $86,110 and $79,210 match i8962 pp. 8 to 9. The linear pattern holds.
- Table 2: 250 numeric rows (150 to 399) plus "less than 150" and the "400 or more" 0.0850 row, 252 in all. The map's derivation (with half-up to four places) reproduces every row.
- Table 5's six amounts are at i8962 p. 18 and p974 p. 52 (and rp-2024-40, see E4). "If your entry on Form 8962, line 5, is 400 or more ... Leave line 28 blank".
- Line 8b via 1/12 then `round` is exact: the fraction of 8a/12 in cents is a multiple of 25/3, never in [49.5, 50).
- Column (b) "only one Form 1095-A" per state, columns (a) and (f) added across forms: i8962 pp. 15 to 17.
- Below 100%: the five conditions and the "No APTC was paid" caution (i8962 p. 9); "skip lines 7 and 8" (p. 10); MFS "enter -0- on line 24" (p. 16).
- P.L. 119-21: 71305 strikes 36B(f)(2)(B), effective after 2025 (pp. 254 and 255); 71301 after 2026 (p. 252); 71302 after 2025 (p. 253); 71303 after 2027 (p. 254); 71304 plan years after 2025 (p. 254). Table 5 applies for 2025.
- Not archived as the map states: 26 USC 36B, Rev. Proc. 2024-35, the HHS 2024 guidelines. Table 2 appears only in i8962 ("0.0850" occurs nowhere else). The poverty amounts appear only in i8962; the i1040gi hits for "15,060" are Tax Table cells.
- Page counts and dates: f8962 3 pages; i8962 25 pages, Oct 1, 2025; p974 69 pages, Jan 12, 2026.
- No cycle: Form 8962 reads only lines 11a, 2a, 6a and 6b, household and dependent lines, and the filing status. The self-employed health insurance feedback (p974 p. 47) is screened by sc.hi_screen.
