# Stage 19 (the education credits): decision batch for the owner

> **Owner's answer (2026-10-29): all recommended.** D1 to D9 are accepted as recommended, with the items under
> "Settled by the evidence".

Prepared on 2026-10-29 from `stage19-education-credits.md` (the premise map, 2026-10-22, at 6051ec0) and
`stage19-education-credits.verification.md` (its adversarial check, at 1c465c2), and checked again against the tree at
31bbd60 with the Stage 18 build in the working tree, not yet committed. Where the map and the verification differ, the
verification's checked facts are used; where the tree has moved since (Stages 16, 20 and 18), the current state is used
and the change is noted. Each decision gives the recommendation first, then the alternative.

This is the third stage of the route in `docs/2026-10-26_plan_revision.md` section E. Category `education`: 4.5% of
returns (7,211,349, the 2023 count of returns with a nonrefundable education credit, soi-23in33ar column 8, the larger
of the two cells; column 40, the refundable American opportunity credit, is 5,821,688). The gain if covered alone is
+4.0 from 75.6% (`reports/2025/filer_coverage.json`, `gain_if_covered_alone.education` 0.0397, with Stage 18 retired),
so 79.6% after it. That is short of 80%: spec 2.4 rounds it to "80%", and the plan says the route reaches 79.6% without
Form 5329, so the first goal now rests on Stage 21. The count is the IRS's, but the overlap is thin. PolicyEngine flags
education on 0.53% of returns before raking, against the IRS's 4.49%, so the overlap with the other categories rests on
about an eighth of the sample.

## What the stage is

Form 8863 (`f8863`, i8863 2025): Part III for each student (lines 20 to 31: four AOC eligibility questions and the
expenses), Part I the American opportunity credit (AOC) with its MAGI phase-out and the 40% refundable part to Form
1040 line 29, Part II the lifetime learning credit (LLC) with its own phase-out, and the Credit Limit Worksheet (i8863
p. 8) that limits the nonrefundable AOC and the LLC together to the tax left after Schedule 3 lines 1, 2, 6d and 6l. Line
19 goes to Schedule 3 line 3. The Adjusted Qualified Education Expenses Worksheet (i8863 p. 9) reduces each student's
expenses by tax-free assistance and refunds. Today the whole form is refused through `scope.credits`. `f1040.line29` is
`param sales.zero` behind it (`forms/2025/f1040.yaml`, `f1040.line29`), there is no `s3.line3`, and no line, input or
interview question names Form 8863, Form 1098-T or tuition except the refusal texts and `scope.other_line16`'s
"recapture of an education credit" (`forms/2025/scope.yaml`).

New since the map was written, or corrected by the verification:

- **The Stage 15 ids are resolved.** `s3.line8` is `sum(s3.line1, s3.line2, s3.line4, s3.line5a, s3.line5b, s3.zero)`.
  Four worksheets would add `s3.line3`: `s8812.clw_a2` (sum of lines 1, 2, 4, 5b), `f8880.clw2` (lines 1 and 2; line 3
  is left out by a note in its locator, with no `refuses` clause), `f5695.rce_ws2` (lines 1, 2, 4, 5b and `f5695.ctc`)
  and `f5695.eehi_ws2` (lines 1, 2, 4). `f2441.clw2` is `copy s3.line1` and does not change. The Form 8863 worksheet
  reads only `f1040.line18`, `s3.line1` and `s3.line2`, so there is no cycle.
- **Stage 16 brought Schedule 1 line 8r in.** `s1.line8r` is now an input ("Scholarship and fellowship grants ... not
  reported on a Form W-2; if you were a degree candidate, only the part used for expenses other than tuition"), so a
  filer who is the student and includes a scholarship in income is no longer refused by `scope.schedule1`. This settles
  the map's D8 condition and the verification's error 2 (D6 below). Taxable Coverdell and qualified tuition program
  distributions are still refused, now by `oi8z.additional_tax`.
- **Stage 18 changed line 18.** `s2.line1a` (the excess advance PTC repayment) now reaches Form 1040 line 17 and so line
  18, which Credit Limit Worksheet line 4 reads, as the forms say. `scope.credits`' label now names "the net premium tax
  credit this tool figures on Form 8962". *Noted, not this stage's:* the four refusal remedies that list the supported
  credits (`scope.yaml` on `scope.ready`, `f1040.line29`, `f1040.line30`, `s3.line8`) still say "entered from Form 8962".
- **No atom is needed.** Spec 4.2 now also has `percent_floor`, `sum` over counts and `multiply_rate` with a unit (Stage
  18). Form 8863 needs none of them. `prorate` gives lines 6 and 7 and lines 17 and 18 (the ratio rounded half-up to
  three places and kept between 0 and 1, so "enter 1.000" and the line 4 and 15 stops come out of it).
  `multiply_rate` gives 40%, 20% and 25%, and `choose`, `test`, `smaller_of`, `subtract_floor0` and `sum_over` do
  the rest.
- **Outside engines.** UsTaxes computes Form 8863 (`.engines/ustaxes-src/src/forms/Y2025/irsForms/F8863.ts`, read in
  full). It takes per-student adjusted expenses and an `aotcEligible` flag as inputs and uses an unrounded phase-out
  fraction. It has no line 7 test (40% is always refundable), no Credit Limit Worksheet (line 19 is not limited by tax)
  and rounds to dollars. Its Schedule 3 line 3 and Schedule 8812 read the result. PolicyEngine-US models both credits
  per person, with eligibility variables for each AOC requirement and an unrounded phase-out; its refundable part is a
  flat 40% of the credit (read from `refundable_american_opportunity_credit.py`, not run). Tax-Calculator takes the
  tentative AOC (line 1) and LLC expenses (line 10) as inputs and applies the phase-out rounded to three places and a
  tax limit (`AmOppCreditParts`, `EducationTaxCredit`). OpenTaxSolver does not compute the form: it reads line 29 and
  Schedule 3 line 3 as entered amounts. None of the four adapters maps education today.
- **The 2026 drafts are archived** (`sources/2026/f8863`, posted 2026-05-26; `i8863`, posted 2026-09-11). Compared word
  by word with the 2025 form, the draft differs only in pointing lines 3 and 14 to Form 1040 line 11a and in numbering
  lines 22a and 22b. The amounts and the Credit Limit Worksheet line 5 list are unchanged. The draft instructions add
  the identification rule of P.L. 119-21 sec. 70606 (below).
- P.L. 119-21 (archived) changes nothing for 2025. For 2026, sec. 70606 rewrites 25A(g)(1) ("taxable years beginning
  after December 31, 2025", plaw-119-21 p. 219): the claimant needs a social security number in the sense of section
  24(h)(7), so an ITIN no longer suffices. A dependent student needs one too, and the AOC still needs the institution's
  EIN. The 2026 draft i8863 reads it as "a valid SSN ... valid for employment", and on a joint return "only one spouse
  must have a valid SSN". Secs. 70413 and 70414 widen 529 qualified expenses, which touches only the 529 help text.

## Decisions for you

**D1. Scope.** Compute Form 8863 Parts I to III, the Adjusted Qualified Education Expenses Worksheet, the Credit Limit
Worksheet, Form 1040 line 29 and Schedule 3 line 3 for every student the return may claim: you, your spouse on a joint
return, and each dependent you claim. Refuse, each by a cited screen: an AOC that needs Form 8862 or is barred for 2 or
10 years (one question, i1040gi p. 61 and i8863 p. 3); an academic period whose tax-free assistance exceeds its own
expenses (D3). Lines 3 and 14 refuse on the existing `sa.excluded_income` (Form 2555, 4563 or Puerto Rico income;
Pub. 970 Worksheet 2-1). Recapture (`scope.other_line16`), married filing separately (`s3.mfs`) and nonresident alien
status (`scope.other_income`) stay refused as today. / The LLC only now, the AOC later. That saves lines 1 to 8, 23 to
30 and the line 7 test, but the AOC is the larger part (5.8 million returns with a refundable part) and the category
would stay refused.

**D2. Where the students live.** Put Part III and the expenses worksheet inputs on the `person` and `dependent` entries.
They are reached only when "Did anyone pay qualified education expenses for this person in 2025?" is yes, and only
for a claimed dependent. The arithmetic of lines 27 to 31 goes in one `def`, bound from each entry, so it is written
and reviewed once. Lines 23 to 31 are printed lines of the entry with `shown_when` that answer, so the values sheet shows
each student's Part III in that person's or dependent's section. `output.ts` prints collection entries and their nested
entries, not def instances, which settles the verification's open question against a def alone. Return lines 1 and 10
are `sum_over person` plus `sum_over dependent`. The student's TIN and `dependent.claimed` are read in their own
entry, as spec 4.4 requires. / (a) A `student` collection nested under `person` and another under `dependent`: a
cleaner Part III section, but two copies of every line to transcribe and review. (b) One return-level `student`
collection: one copy, but it cannot read the dependent entry's TIN or claimed status (spec 4.4), so it would ask them
again unchecked.

**D3. Academic periods.** One total per student. A per-student screen refuses when any one academic period's tax-free
assistance exceeds that period's expenses. Only then does the per-period floor of the worksheet ("for each student for
each academic period", i8863 p. 9) differ from the total. / A nested academic-period collection under each student: exact
for every case, at three more inputs a period.

**D4. Requirements with no line.** Form 1098-T: one Bool per student, "received a 2025 Form 1098-T, or an exception in
the instructions applies" (i8863 p. 1). No means no credit for that student, and there is no 1098-T collection: box 1
is not the line value (i8863 p. 4, "use only the amounts you actually paid"), so boxes 1, 5, 7, 8 and 9 are help text.
The student has no TIN by the due date: no credit (`person.tin` with `person.itin_applied`, or `dependent.tin`). The
filer has no TIN, or the institution's EIN is not available: an eligible AOC student goes to line 31 (the i8863 p. 4
Tip, "You may be able to claim the lifetime learning credit ... instead"). Ban or Form 8862: refuse (D1). / Refuse in
every one of these cases. Simpler, but it refuses filers the form allows an LLC.

**D5. The refundable part (line 7).** On a return that is not joint and has line 7 above zero, ask: three birth-date
questions in the pattern of `person.born_before_2001` (born before January 2, 2008, which is `person.sav_born` reused;
before January 2, 2007; before January 2, 2002), so under 18, exactly 18 and under 24 at the end of 2025 come from
dates. Also ask: full-time student under the i8863 p. 7 definition (5 calendar months at an eligible educational
institution); earned income less than half of support (a Bool, with the i8863 p. 7 definitions as help); and at least
one parent alive. `person.sav_student` is not reused, because Form 8880's "school" includes on-farm training courses
and i8863 says "eligible educational institution". On a joint return the test is false without asking (item 3). / Ask
one age Count, as `dependent.age` does, and leave the birthday edge to the filer. Or refuse non-joint AOC filers under
24.

**D6. A scholarship the student includes in income.** *Changed by Stage 16:* compute it. When the student is a
dependent, the dependent's return carries the inclusion and this return takes only the tax-free part as entered. When
the student is you or your spouse, the included amount is in `s1.line8r` (now an input), and the student's "tax-free
educational assistance" leaves it out. Help text on both inputs says so (p970 pp. 15 to 16; i8863 p. 5), but nothing
links the two, because line 8r is one amount for both spouses. Pub. 970's Jane variants (p970 p. 16, Example 5)
become usable fixtures. / A screen refusing a filer-student who includes any scholarship in income (the map's
fallback, now needless).

**D7. Four readings** (each an ambiguity-register entry).
(a) The AOC's "Filers and students must have been issued a TIN" (i8863 p. 3, item 5): on a joint return both spouses
(`household.all_tin`), since both are filers. The 2026 draft says one spouse suffices, but under the new SSN rule,
which is not the 2025 text.
(b) Age at the end of 2025 by the day-before-the-birthday rule (D5's dates), which i8863 does not state. Pub. 501
states it for age 65, and the project's other birth-date questions apply it.
(c) "Full-time student (defined later)" in line 7 item 1c is the 5-month definition, though i8863 p. 7 heads it "Solely
for purposes of determining whether a scholarship is considered support".
(d) The Form 1098-T exception for a late-requested form: help text cites p970 p. 2 ("After February 2, 2026"), the later
revision (Jan 27, 2026), over i8863 p. 1 ("After January 31, 2026").
/ Any reading the other way; for (a), one spouse.

**D8. Evidence.** UsTaxes is the only engine that computes the form from expenses. It is compared where its model is
the form's: joint filers or filers 24 and over, phase-out fractions exact at three places, and a tax large enough that
the Credit Limit Worksheet does not bind. Tax-Calculator is compared on the phase-out and the tax limit from line 1 and
line 10 amounts. PolicyEngine-US gets per-person expenses and the eligibility flags. Every difference is explained,
including UsTaxes's missing line 7 test and tax limit. Ten blind returns cover both phase-outs on a non-exact decimal,
an under-24 filer in each line 7 branch, mixed AOC and LLC students, the LLC $10,000 cap shared across students, a
binding Credit Limit Worksheet with Schedule 8812 after it, and the line 31 fallback. The official examples are added:
Jack and Kay, Bruce and Toni, the two phase-out examples, the Pell examples, Bill, and Jane (now computable, D6). / The
blind returns and examples only, with no engine mapping: cheaper, but no outside family sees the form's arithmetic.

**D9. Second printings.** Archive 26 U.S.C. 25A (the 2024 edition, as `usc-26-36b` was for Stage 18) for D7(a) and
the line 7 rule (25A(i)), and the 2025 Form 1098-T (`f1098t`) for the box captions in the help text. Leave Form 8862,
i1099q and Pub. 519 unarchived, since what they cover stays refused. / Rest D7(a) on i8863 alone.

Structure-changing: D1, D2 and D4. D2 decides where per-student data lives and how it is shown; it is the main
decision. Unlike Stages 15 and 18, the atom vocabulary does not change.

## Settled by the evidence (done this way unless you object)

1. **Downstream lines.** New `s3.line3` is a copy of Form 8863 line 19 ("Education credits from Form 8863, line 19",
   f1040s3 p. 1), and `s3.line8` adds it. `f1040.line29` becomes a copy of Form 8863 line 8 without its refusal, and
   `f1040.line30`'s refusal form text drops line 29. `s8812.clw_a2`, `f8880.clw2`, `f5695.rce_ws2` and
   `f5695.eehi_ws2` add `s3.line3` and drop "3" from their labels, locator notes and refusal texts (i1040s8812 p. 4;
   f8880 p. 2; i5695 pp. 5, 7). The four `scope.credits` remedies and the label name the education credits, and the
   "entered from Form 8962" wording is corrected with them.
2. **Credit order** (checked in the code): Form 2441 → Form 8863 → Form 8880 → Form 5695 Part II → Schedule 8812 →
   Form 5695 Part I. Schedule 8812 Credit Limit Worksheet B reads neither line 3 nor line 29, so it does not change.
3. **Credit Limit Worksheet line 6** is `subtract` as printed, with a class D property that it is never negative.
   `ftc.credit` and the Form 2441 credit are each limited by line 18, so lines 1 + 2 ≤ line 18 (the verification).
4. **Decimal places.** Lines 6 and 17 use `prorate` at three places, half-up. That is a new register entry citing
   f8863 lines 6 and 17, read as `amb.2025.sli_ratio_places` (the owner's Stage 11 ruling) reads the same words.
5. **AOC or LLC.** Follow the form: a student who passes lines 23 to 26 and D4 is an AOC student, with no election.
   Per student the AOC is at least the LLC (i8863 p. 3 Tip; checked by arithmetic in both the map and the
   verification).
6. **Expenses by credit.** Two inputs per student: amounts required to be paid to the institution (tuition, fees and
   required materials) and other course materials (AOC only), as i8863 p. 4 splits them.
7. **Claimed as a dependent.** Reuse `sli.claimed`. Its wording is i1040gi p. 115's for Schedule 3 line 3 ("You, or
   your spouse if filing jointly, are claimed as a dependent"). `person.sav_claimed` is per person and asked only when
   `sa.dependent` is true, so it cannot serve a return-level bar.
8. **529 and Coverdell.** Help text only: enter expenses not used for a tax-free distribution. Taxable distributions
   stay refused by `oi8z.additional_tax` until Form 5329 (Stage 21).
9. **Parameters.** Status-keyed, with `mfs` given the single amount and recorded as never reached, following
   `savers.agi_limit` (the verification's error 1; `sli.line5` is not the precedent). The second printings are i8863
   pp. 2 and 3.
10. **Coverage bookkeeping.** `education` gets `"refused": false` and empty gates. The new screens (D1, D3) are
    unmeasured gates.
11. **Fixtures.** Ten cases set `scope.credits` true (classm 4, stage15 2, stage16, stage4, stage5, stage8 one each).
    Each is checked against the narrowed question.
12. **Reviews.** The new `f8863` and every changed form (`s3`, `f1040`, `s8812`, `f8880`, `f5695`, `scope`, `person`,
    `dependent`) are reviewed under Claude and deepseek-flash and adjudicated.
13. **TY2026.** Built on the final 2025 text and carried forward by year adoption. Lines 3 and 14 read Form 1040 line
    11a. The identification rule becomes a valid-SSN test on `person.work_ssn` (one spouse, per the 2026 draft) and
    `dependent.work_ssn`. The amounts are unchanged in the draft; the final 2026 text is checked when it posts.

## Verified and inferred

Checked against the tree at 31bbd60 with the uncommitted Stage 18 build: `scope.credits` (label) and every refusal
clause that names it (`scope.yaml`, `f1040.yaml` lines 29 and 30, `s3.yaml`, `s8812.yaml`, `f5695.yaml`) and the
`f8880.clw2` and `f2441.clw2` notes. Also checked: `f1040.line29` (`param sales.zero`), lines 11b, 18 to 22 and 32;
`s3.line8`, no `s3.line3`; the four worksheet sums; `s2.line1a` and `s2.line3`; `s1.line8r` (input) and the
`oi8z.additional_tax` wording; `sli.claimed` and `sli.eligible`; `person.sav_claimed`, `sav_student`, `sav_born`,
`born_before_2001`, `tin`, `itin_applied`, `work_ssn`; `dependent.age`, `tin`, `claimed`, `work_ssn`;
`household.all_tin`; `sa.excluded_income`; the spec 4.2 atom list; `savers.agi_limit`; `amb.2025.sli_ratio_places`;
collection parents and `output.ts`'s values-sheet sections; the `education` entry in `tools/coverage/categories.json`
and its figures in `reports/2025/filer_coverage.json`; the fixture counts; the archive (f8863, i8863, p970, i1098et,
plaw-119-21 and the 2026 f8863 and i8863 drafts present; 26 U.S.C. 25A, Form 1098-T, Form 8862, i8862, i1099q and Pub.
519 absent). Also read: UsTaxes `F8863.ts` (in full) and its Schedule 3 wiring; the PolicyEngine AOC, phase-out and
limit formulas; Tax-Calculator's two functions; OpenTaxSolver's two input lines. In the sources: Credit Limit
Worksheet line 5, the line 7 conditions, "rounded to at least three places", the per-period worksheet heading, the
Form 8862 rule, i1040gi p. 115, i8863 p. 3 item 5; P.L. 119-21 sec. 70606 in full; the 2025-to-2026 form diff and the
2026 draft identification text.

Taken from the verification without checking again: the other quotations and every parameter value; the official
examples' arithmetic; lines 1 + 2 ≤ line 18; the SOI column values.

Inferred: that `shown_when` lines on the person and dependent entries give a readable Part III (D2; read from
`output.ts`, not run); PolicyEngine's flat 40% (read, not run); that the Bill and Jane examples reproduce under the
project's Tax Table and EIC Table (not run); the shares of every refused sub-situation (none measured); the effect of
the thin microdata on the +4.0; the coverage figure itself (read from the report; the estimator was not run, since it
rewrites the report); the final 2026 text.
