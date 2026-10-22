> Adversarial verification of `stage21-form-5329.md` by an independent read-only agent after Stage 15 (commit 1c465c2): 8 errors and 4 items out of date. Read it with the map; where they differ, the verification has checked the source.

# Verification: research/premises/stage21-form-5329.md

Read-only check against `sources/2025/` (page N = N-th form-feed chunk of `<doc>.cols.txt`) and the repository at
1c465c2 (working tree). Nothing in the repository was changed. Page checks were done with a per-page matcher
(`/tmp/premises/verify/s21tools/pg.py`) and `check_quotes.py`.

## Errors

1. **D12 rests on a misreading of how the estimator retires a category.** Map section 9, D12 (and section 5, the
   `categories.json` row): it recommends replacing the `form5329` gates with the residual gates
   (`f5329.unsupported`, the narrowed `s2.other`) and keeping the IRS count; the alternative is to "drop the
   category as retired". What the source says: `tools/coverage/estimate.py` treats a category as refused by its
   `refused` field alone (`refused = [c for c in cats if c.get("refused", True)]`). Gates are only checked to exist
   in the forms (`categories.json names gates not in the forms`). So D12 as recommended leaves the 3.2% counted
   as refused permanently, and the stage's +3.0 never shows. The convention already in the file (Schedule C
   entry, `"refused": false`; and the Stage 15 commit for `cdcc`, `savers`, `energy`) is `"gates": []`,
   `"refused": false` and a label "(supported since Stage 15; its remaining refusals are unmeasured gates)". That
   keeps the IRS count and is neither of D12's two options. Also, `s2.other` stays the gate of `ptc` and
   `schedule2_other`, so listing it under `form5329` too would count it twice. Affects D12.

2. **The caps in D4 are applied per entry, but the text sets them per person or per year.** Map D4 (and section 6,
   "Cap the fixed dollar amounts"): "the per-entry amount is capped by ... 19 by $5,000 times a count of children;
   22 at $10,300 and 23 at $1,000". What the source says: p590b p. 28, "A qualified birth or adoption distribution
   must not exceed $5,000 per taxpayer"; "You are limited to taking one emergency personal expense distribution per
   calendar year and the amount ... must not exceed the lesser of $1,000 or your total interest in the IRA minus
   $1,000"; the domestic abuse limit "must not exceed the lesser of $10,300 for 2025 or 50% of the present value of
   the IRA". A per-entry cap lets two Forms 1099-R claiming 23 exclude $2,000, or two claiming 22 exclude $20,600.
   The map does treat 09 per person; 19, 22 and 23 need the same per-person total. Affects D4.

3. **The s2.other rewording removes a phrase that `s2.other` does not contain.** Map section 5, row `s2.other`:
   "remove ... 'excess contributions to an HSA'". What the source says: forms/2025/s2.yaml `s2.other` asks only "the
   additional tax on early retirement or HSA distributions (often called a penalty)", among the other items. It
   names no excess-contribution item. Today HSA excess is refused by `f8889.excess`, not by name in `s2.other`.
   Section 1.2's description is right; the section 5 row is not. Affects how D2 and D7 are worded only.

4. **The Form 1040 line ids in section 5 are wrong.** Map section 5: "`f1040.line4a`, `.line4b`, `.line4c`,
   `.line5a`, `.line5b`, `.line5c` ... become `sum_over person`". What the source says: forms/2025/f1040.yaml has
   `f1040.line4c_rollover` and `f1040.line5c_rollover`; neither is a `sum_over`. The six `sum_over retirement`
   lines are `f1040.line4a`, `.line4b`, `f1040.ira_rollovers` (Count of `retirement.one`), `.line5a`, `.line5b` and
   `f1040.plan_rollovers`. A seventh is `f8880.dist_2025` (f8880.yaml l. 134, field `retirement.sav_amount`). The
   map calls that one "Form 8880 line 4"; it is a helper that feeds line 4. Affects the cost estimate behind D1.

5. **`s2.line8` as written cannot be expressed under spec 4.4.** Map section 3.4: "`s2.line8` = `sum_over person` of
   (`f5329.line4` + Part VII line 49)", with line 49 "On the person's `f8889` entry" (3.3). What the source says:
   spec.md section 4.4, "A line of an entry may read a line of the entry that encloses it ... no other reference
   into a collection is allowed". check.ts also allows a `sum_over` only over a child collection. Line 49 sits on
   an `f8889` entry, a child of `person`. If Form 5329 is the implicit child collection the map offers, `f5329.line4`
   is a child line too. So `person` needs its own total lines (`sum_over f8889`, and `sum_over f5329` or
   `sum_over retirement`) before s2 can `sum_over person`. This is a change in shape, not a cycle. Affects how D1
   and D2 are built.

6. **D1 leaves out an interview text that a re-parented `retirement` contradicts.** In interview/questions-2025.yaml,
   the help text of `$person` says "Amounts that are not asked person by person (interest, dividends, sales, pensions
   and annuities, ...) are entered once, for you and your spouse combined." D1's recommended answer makes
   pensions and annuities per person. Section 5 lists `interview/questions-2025.yaml` only for new questions, not
   for this sentence. Affects D1.

7. **The exception 05 cap can exceed the medical expenses when AGI is negative.** Map D5 / section 6: "Compute cap
   from `sa.line4`". What the source says: forms/2025/sa.yaml has `sa.line3` typed `Dollars` (7.5% of `sa.agi`,
   which copies `f1040.line11b` and can be negative) and `sa.line4 = subtract_floor0(sa.line1, sa.line3)`. When
   AGI is negative, `sa.line4` is larger than `sa.line1`. Then the exception 05 amount can be more than "the amount
   you paid for unreimbursed medical expenses" (i5329 p. 5). This is an edge case; a floor or a `smaller_of` with
   `sa.line1` closes it. Affects D5 (minor).

8. **Several page locators are wrong.** The quotes are all genuine.
   - p590b, higher education "generally the amount that isn't more than the qualified higher education expenses"
     and the K-12 sentence "Additional qualified education expenses in connection with elementary and secondary
     tuition" (map 4.4 and Q4, "p. 26"): both are on **p. 27**. Affects D11 (Q4) citations.
   - p590b, the repayment sentence "repaid, in whole or part, ... If you have, file Form 8606." (map 4.4, "p. 2"):
     it is on **p. 4**.
   - f1099r, exception 18 row, "these go on line 1h (f1099r p. 7, Box 1)": the Box 1 recipient text is on
     **p. 5**. It says to report "permissible withdrawals from eligible automatic contribution arrangements" on "the
     line for 'Wages, salaries, tips, etc.'"; it does not name line 1h.
   - Minor: the f5329 line 2 quote misses only because of leader dots in the extraction (f5329.txt l. 26-27); the
     text is genuine.

## Out of date after Stage 15

1. **The roadmap position and target.** Map header: "Roadmap item 7 of spec 2.4 ('... Form 5329 (95%, the target)')".
   The assumption paragraph says "roadmap items 1 to 6 (Stage 15 credits, ...)"; 1.3 and D7 refer to "roadmap item
   2" (Schedule 1) and "item 5" (education). Now, spec.md 2.4 item 6 reads "The additional tax on qualified
   retirement plans, Form 5329 (94%)", and the target is item 7, "Married filing separately (97%, the target)".
   Stage 15 is listed as done. The items before this stage are 1 to 5: Schedule 1 is item 1, education is item 4.
   No decision's answer changes, but the stage no longer reaches the 95% target.
2. **The coverage step.** Map 1.1: "Step 7 of the gain order: '95.1% (+3.0)', '+1.9' if covered alone now".
   reports/2025/filer_coverage.md now reads "| 6 | Additional tax on retirement plans (Form 5329) | 94.3% (+3.0) |
   +2.1 |", with overall coverage 64.7%. The share (3.2%) and the count (5,092,999) are unchanged.
3. **New lines on the collection D1 would move.** Stage 15 added `retirement.sav_military`, `.sav_404k`,
   `.sav_inherited`, `.sav_excluded`, `.sav_gross` and `.sav_amount` to retirement.yaml, read by `f8880.dist_2025`.
   D1's re-parenting moves these lines too, and `f8880.dist_2025` must become a `sum_over person` of a person-level
   sum. The map foresaw the f8880 reader but not the six entry lines or their fixtures (Stage 15 fixtures as well as
   Stage 10).
4. **Line numbers.** Map section 5: "the only readers of `f1040.line24` are within f1040.yaml, lines 851 and 881".
   They are now lines 876 and 906 (still the only readers in forms/; engine/src/properties.ts also reads line 24 in
   tests). The Stage 15 credit-limit readers of `f1040.line18` (f2441.yaml l. 787, f8880.yaml l. 517, f5695.yaml
   l. 333 and 2054, s8812.yaml l. 238) do not read Schedule 2 Part II, so the map's no-cycle claim still holds.

## Unverifiable

- Anything in the documents the map lists as not archived (Pub. 575, Pub. 721, Form 8915-F, Notices 2024-55,
  2024-02, 2020-68, i1099sa, Form 8853, Pub. 907). I confirmed that none is in sources/2025/manifest.json. One
  consequence: the caps for exceptions 22 and 23 are archived only in IRA terms (p590b, "present value of the
  IRA", "interest in the IRA"). Their form for plan distributions, which the map marks "both", is not archived.
- The joint-return medical reading (Q5/D5) and the per-child reading of the $5,000 cap (Q3). The archived text is
  silent on the first. On the second, i5329 p. 5 says "a distribution of up to $5,000 if made during the 1-year
  period beginning on the date your child was born or adopted", which does not say "per child"; p590b p. 28 says
  "per taxpayer".
- Whether the evaluator, and not only the checker, accepts a re-parented `retirement` with no further changes.
- The 2026 Form 1099-R "code P problem" and the "research brief" phrase: neither has an archived source.
- That most of the 5.1 million returns are code 1 (the SOI cell does not split the parts of the form).
- The Part III line 10 no-cycle inference (maximum allowable contribution versus AGI). Not checked.

## Confirmed

About 140 premises confirmed: about 110 IRS quotes with their page locators, and about 30 project facts. The
decision-critical ones:

- SOI soi-23in33ar row "All returns, total": column 76 = 5,092,999, column 77 = 6,380,591. Row 1 reads "money
  amounts are in thousands of dollars", so the map's unchecked unit is now confirmed and the average is about $1,253.
- categories.json `form5329`: group `retirement_penalty`, gates `retirement.special` and `s2.other`, column 76.
  `s2.other` also gates `ptc` and `schedule2_other`. No category gates on `retirement.bad_code`.
- `retirement` has no `collection.parent` (D1). check.ts l. 311 gives "collection parent binding mismatch".
  `w2`, `f8889`, `sc`, `tipjob` and `otjob` have parent `person`; `f4562` is `implicit: form` under `sc`.
- `sum_over` with a `where` on `person.role` exists (f8880.yaml), so D1's alternative is expressible.
- `enums.retirement_code` = {normal_7, death_4, early_exception_2, direct_rollover_G, qualified_roth_Q, other}, so
  codes 1, 3, S, U and B are `other`. `retirement.bad_code` refuses `other` and Roth non-Q. Its remedy says "other
  than 7, 4, 2, G or Q".
- The `retirement.special` question includes "an early distribution with no known exception (code 1, J or S)". It
  does not mention disaster distributions, though its refusal names 8915-F (D3's gap holds).
- `s2.line21` sums only lines 4, 11 and 12, and its only reader is `f1040.line23`. The f1040s2 line 21 printed text
  is "Add lines 4, 7 through 16, 18, and 19".
- f8889: lines 2, 8, 9, 11 (= 9 + 10, with 10 fixed at 0), 12 (`subtract_floor0` 8 − 11), `line13_figured` =
  `smaller_of`(2, 12). `f8889.excess` tests line 2 > line 12 or line 11 > line 8. So line 2 − line 13 = line 2 −
  line 12 when positive, as the map says.
- `sa.line4` = line 1 − 7.5% × AGI (`sa.medical_rate` 75/1000). Q7 is largely moot: engine/src/interview.ts asks
  reachable missing inputs ("missing reachable inputs determine the questions"), so `sa.line1` would be asked when
  an exception 05 branch needs it.
- i1040gi p. 112, the line 8 exception: "If only item (1) applies and distribution code 1 is correctly shown in box
  7 of all your Forms 1099-R ... multiply the taxable amount ... by 10% (0.10)" and "check the box".
- i5329 p. 2, Joint returns: "complete a separate form for each of you. Include the combined tax on Schedule 2".
- i5329 p. 5: the exceptions table 01 to 23 and 99 with the quoted texts; "(01–23) ... enter 99"; the Line 4 25%
  SIMPLE rule. f5329 p. 1, lines 1 to 4; f5329 p. 2, lines 42 to 49 (6%).
- i5329 p. 3: Roth IRA line 1 uses Form 8606 line 25c. i5329 p. 8: lines 43 and 47. i5329 pp. 9-10: Part IX 25%,
  10%, the correction window and "RC".
- i1099r p. 18: codes 1 (the nine excepted kinds under 72(t)(2)(B) to (L), and the SEPP-modification sentence), 2
  and 4. Code 7 on p. 19, code S on p. 20, two codes on p. 15. f1099r p. 7 has code 1 and p. 9 has code S.
- p590b p. 26: the SEPP recapture goes on line 4. p590b p. 25: the medical exception (no need to itemize, AGI line
  11a). p590b p. 27: the $10,000 first-home limit and the per-spouse TIP.
- p969 p. 8 and i8889 p. 8: excess HSA contributions and withdrawals. i1040gi p. 65 excludes "5329 (Parts III
  through IX only)".
- p590a p. 35: the $7,000/$8,000 limit. i5329 p. 7: Roth limits of $236,000/$150,000. p590a p. 43, Worksheet 2-2:
  starts of $236,000/$0/$150,000 and widths of $10,000/$15,000 ("rounded to at least three places", round up to
  $10 with a $200 floor). The atoms `prorate` and `round` exist.
- Not archived as stated: p575, p721, f8915f/i8915f, n-24-55, n-24-02, n-20-68, i1099sa, f8853, p907.
