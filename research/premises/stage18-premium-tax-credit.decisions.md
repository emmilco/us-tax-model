# Stage 18 (the premium tax credit): decision batch for the owner

> **Owner's answer (2026-10-28): all recommended.** D1 to D9 are accepted as recommended, with the items under
> "Settled by the evidence".

Prepared on 2026-10-28 from `stage18-premium-tax-credit.md` (the premise map, 2026-10-22) and
`stage18-premium-tax-credit.verification.md` (its adversarial check, at 1c465c2), and checked again against the tree
at 4d24cbc. Where the map and the verification differ, the verification's checked facts are used; where the tree has
moved since, the current state is used and the change is noted. Each decision gives the recommendation first, then the
alternative.

This is the second stage of the route in `docs/2026-10-26_plan_revision.md` section E. Category `ptc`: 6.0% of returns
(9,604,913, the 2023 count of returns with advance payments, the larger of the two cells); +4.6 if covered alone from
71.0% (75.6% after it, by the estimator run per category from the post-Stage 20 base). It is placed by the
microdata, so its gain is the best measured of the route's four. Of the 2023 Form 8962 filers, about three in five repaid
excess advance payments (5,577,776 on Schedule 2 line 1a) and 2,410,248 claimed a net credit (Schedule 3 line 9).

## What the stage is

Form 8962 (`f8962`, i8962 2025) reconciles the advance payments a Marketplace made with the credit the filer is allowed:
Part I figures household income against the 2024 federal poverty line and an applicable figure from Table 2; Part II
compares, annually or month by month, the enrollment premiums, the second lowest cost silver plan (SLCSP) premium less
the contribution amount, and the advance payments; Part III limits a repayment by Table 5. Its inputs are one or more
Forms 1095-A. The net credit goes to Schedule 3 line 9, the repayment to Schedule 2 line 1a.

New since the map was written, or corrected by the verification:

- `scope.credits` already lists "the net premium tax credit you enter from Form 8962" (Stage 16, part of T-050), so a
  filer typing a net credit is not refused today; the verification's E1 is fixed. `s3.line9` is still a typed input, and
  Schedule 2 still has no line 1a: every repayment is refused through `s2.other`.
- Table 5 has an authoritative printing in the archive, Rev. Proc. 2024-40 §3.07 (verification E4), besides i8962 p. 18
  and p974 p. 52. Tables 1-1 to 1-3 (the poverty lines) and Table 2 are printed only in i8962.
- **No outside engine computes Form 8962 as printed.** UsTaxes' `F8962.ts` is a stub: a flat 8.5% of AGI, no poverty
  line, no Table 2, no Table 5, no monthly calculation. It agrees with the form only above 400% of the poverty line, on
  the annual calculation, where modified AGI equals AGI. OpenTaxSolver has no Form 8962 program. PolicyEngine-US models
  the credit (`gov/aca/ptc`) from its own rating-area SLCSP data; whether it accepts a supplied SLCSP and reconciles
  advance payments is not checked. Tax-Calculator was not checked.
- P.L. 119-21 (archived) changes nothing for 2025; for 2026 it removes the Table 5 limitation (sec. 71305) and the
  lawfully present alien rule below 100% (sec. 71302). The 2026 applicable figures are not archived.

## Decisions for you

**D1. Scope.** Compute Form 8962 Parts I to III for single, head of household, qualifying surviving spouse and joint
returns with any number of Forms 1095-A: household income (with claimed dependents required to file), the poverty
line, the applicable figure, the annual and monthly calculations, both branches below 100% of the poverty line, and the
Table 5 limitation. Refuse, each by a cited screen: Part IV allocations (a policy shared with another tax family, a
divorce or separation in 2025); Part V and the year-of-marriage column B rule (D5); anyone enrolled who is not lawfully
present; a QSEHRA or individual coverage HRA; a month whose premium was not paid by the due date; advance payments for
someone in no tax family. Married filing separately, a claimable filer, Form 2555 or 8814, and the self-employed health
insurance deduction with a Marketplace plan stay refused as today. / Also compute Part IV situations 1, 2 and 4 with
entered percentages and month ranges (about 36 more lines per Form 1095-A).

**D2. Three changes to the atom vocabulary** (spec 4.2; each needs a checker rule, a rendering template and the Lean
definition, as `rate_lookup` did in Stage 15).
(a) **Line 5.** A new atom `percent_floor` (part, whole, cap): cap + 1 when the part is more than whole × cap ÷ 100,
otherwise 100 × part ÷ whole with the decimals dropped, as Worksheet 2 prints (i8962 p. 9: "Enter 401", "drop any
numbers after the decimal point"). No existing atom divides money by money. / Refuse every Form 8962; there is no
route without it.
(b) **Line 1.** Let `sum` add Count operands when all are Counts: tax family size is the people on the return plus the
dependents claimed. / A pinned table from (people, dependents) to size.
(c) **Line 8a.** Let `multiply_rate` round once, to a named unit, so "Multiply line 3 by line 7. Round to nearest whole
dollar amount" is one rounding. *Correction:* the map recommended accepting the double rounding (to the cent, then to
the dollar) because it "bites only with cents"; the verification found it wrong by $1 on about 0.5% of whole-dollar
household incomes too (for example $60,347 × 0.0850 = $5,129.495: the form gives $5,129, double rounding $5,130). /
Accept the double rounding and register it.

**D3. How Forms 1095-A are entered.** For each form, ask first whether it shows coverage in all 12 months with the same
column A (premium) and the same column B (SLCSP) every month. If yes, ask only its line 33 annual totals (three
amounts); if no, ask the 36 monthly amounts. Line 10 is Yes when every form is answered yes (i8962 p. 14, "if all of
the following apply for each qualified health plan"; *correction:* every form, not only the one whose column B is
counted, verification E3). / Always ask the 36 monthly amounts and derive line 10 from them (more checking, three times
the questions for the common full-year filer).

**D4. A column B that is blank, zero or wrong.** The filer enters the correct applicable SLCSP premium (from the
Marketplace's tool, which p974 p. 27 says is the only source) in place of column B, with a notice; it is common when no
advance payments were made, or after a change the Marketplace did not hear of. / Refuse whenever column B needs
correcting (simpler, but it refuses most claims without advance payments).

**D5. Year of marriage.** Refuse a joint return when the spouses married in 2025 and anyone was enrolled before the first
full month of marriage (Part V and its column B rule, Pub. 974 Worksheets I to V). / Compute without the optional
election, with a notice that it might lower the repayment, refusing only the column B rule.

**D6. Below 100% of the poverty line.** Compute both branches: not an applicable taxpayer (no credit; advance payments
repaid up to the Table 5 limit), and the exception where the Marketplace estimated at least 100% and advance payments
were made (one question; i8962 p. 9). The lawfully present alien branch is refused with D1's screen. / Refuse every
return below 100%.

**D7. Four readings** (each an ambiguity-register entry).
(a) Not an applicable taxpayer: line 24 is zero and line 25 the advance payments; the text says "not eligible to take
the PTC" but, unlike for married filing separately, not "enter -0- on line 24".
(b) Dependents' income: count a claimed dependent "required to file an income tax return because their income meets
the income tax return filing threshold" by Chart B only (i1040gi p. 10, including its gross income test, verification
E5), not by Chart C's self-employment or advance-payment rules, with one modified AGI amount per such dependent.
(c) Form 1095-A amounts: keep exact cents (as `amb.2025.sales_rounding` does), though i8962 p. 22 says "You should
round the amounts on Form 1095-A to the nearest whole dollar".
(d) Line 10 Yes uses the annual line 11 even where twelve times the monthly figure would differ by rounding (up to $6);
the instructions make line 10 a test, not a choice.
/ Any reading the other way; for (b), refuse any dependent required to file.

**D8. Evidence for a form no outside engine computes.** Double the blind predictions to twenty returns (two predictors
each, from the archived text), covering both branches below 100%, the Table 5 bands, the annual and monthly routes, two
Forms 1095-A in one and in two states, and the corrected column B; compare UsTaxes only where its stub is the form
(above 400%, annual, modified AGI equal to AGI); and check whether PolicyEngine-US can take a supplied SLCSP, adding it
for the annual credit if it can. / The usual ten blind returns and no engine comparison.

**D9. Second printings.** Archive 26 U.S.C. 36B and the HHS 2024 poverty guidelines (89 FR 2961), so the poverty lines
rest on two printings and Q7's reading on the statute. Table 5 already has three. / Leave Tables 1-1 to 1-3 on i8962
alone.

Structure-changing: D1, D2 and D3. D2 changes the atom vocabulary, the project's trust base; it is the main decision.

## Settled by the evidence (done this way unless you object)

1. **Downstream lines.** Schedule 3 line 9 becomes a copy of Form 8962 line 26 (its question goes); new Schedule 2
   lines 1a (Form 8962 line 29) and 1z; line 3 adds 1z and 2. `s2.other` drops "repayment of excess advance premium tax
   credit"; `scope.credits` names the premium tax credit as figured from Form 1095-A. The repayment raises Form 1040 line
   18, which every Credit Limit Worksheet starts from, as the forms say.
2. **T-049.** `amb.2025.dc_rate_nonpositive_agi`'s reason (line 18 is zero when AGI is not positive) stops holding, since
   a Table 5 repayment can be owed then; the reason is rewritten and the readings re-examined.
3. **Table 5** parameters cite Rev. Proc. 2024-40 §3.07, the source of the amounts (verification E4).
4. **Poverty tables** are pinned from i8962 pp. 8 to 9, extended by the printed footnotes to a family size of 20 and
   refused above (the size-11 examples check the extension). The table question asks about you and your spouse only
   (verification E6: the higher-table rule names you and your spouse, not dependents).
5. **Table 2** is a keyed table of 402 rows on line 5 (0 to 401), extracted from i8962 p. 11 and checked against the
   map's derivation; line 5 is capped at 401, so the table is never asked for a key it lacks (verification E7).
6. **Several forms in one state.** One question per form, whether its column B is the one counted (one form per state);
   a screen refuses two counted forms in one state (the model cannot see states).
7. **Coverage bookkeeping.** `ptc` gets `"refused": false` and empty gates; the new screens are unmeasured gates.
8. **Fixtures.** The `s3.line9` input leaves every case (1,022 keys); the two cases that supply a nonzero amount
   (stage2 `ss.other.components` and one other) get a Form 1095-A or are replaced. The eight cases with `s2.other` true
   are checked against the narrowed question.
9. **Reviews.** New documents `f8962` and the Form 1095-A collection, and every changed form (`s2`, `s3`, `scope`,
   `dependent` for the dependent questions), reviewed under Claude and deepseek-flash and adjudicated.
10. **TY2026.** Built on the final 2025 text and carried forward by year adoption: Table 5 goes for 2026 (P.L. 119-21
    sec. 71305) and Table 2 will be replaced from the 2026 instructions. The line 5 cap keeps any table above 400%
    expressible.

## Verified and inferred

Checked against the tree at 4d24cbc: `s3.line9` (a NonNegDollars input with the map's wording); no `s2.line1a` or
`s2.line1z`; `s2.line3` (copy of zero, refused on `s2.amt`, `s2.other`); the `s2.other` and `scope.credits` wording;
`household.persons`, `dependent.claimed`, `sa.dependent`, `sa.excluded_income`, `sc.hi_screen`; `sum` takes money only
(`engine/src/check.ts`); the atom list (no division of money by money); the archive holds f8962, i8962, p974, f1095a,
i1095a, rp-2024-40 and plaw-119-21, not 26 U.S.C. 36B or the HHS guidelines; UsTaxes `F8962.ts` (read in full);
OpenTaxSolver's programs (no Form 8962); the fixture counts; T-049 and T-050 open.

Taken from the verification without checking again: every quotation and table value; the 0.5% double-rounding rate.

Inferred: that PolicyEngine-US can or cannot take a supplied SLCSP; that the monthly route is the minority (D3's burden
argument); the shares of every refused sub-situation (none measured); the 2026 Table 2 (not archived).
