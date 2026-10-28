# Stage 20 (the capital loss carryover): decision batch for the owner

> **Owner's answer (2026-10-27): all recommended.** D1 to D6 are accepted as recommended, with the items under
> "Settled by the evidence".

Prepared on 2026-10-27 from `stage20-capital-loss-carryover.md` (the premise map, 2026-10-22) and
`stage20-capital-loss-carryover.verification.md` (its adversarial check, at 1c465c2), and checked again against
the tree at 671826a. Where the map and the verification differ, the verification's checked facts are used; where
the tree has moved since either, the current state is used and the change is noted. Each decision gives the
recommendation first, then the alternative.

This is the first stage of the route in `docs/2026-10-26_plan_revision.md` section E. Category
`capital_loss_carryover`: 3.5% of returns (5,622,923, the larger of the 2023 short- and long-term carryover
counts, a lower bound); +2.5 if covered alone from 68.6%. It is an IRS-only category, combined as independent of
the rest, so the gain is the least certain of the route's four.

## What the stage is

The Capital Loss Carryover Worksheet (i1040sd p. 10): 13 lines, no rates or constants, from figures on the 2024
return. Its results go on Schedule D lines 6 and 14, which today are zero behind the `sd.carryover` refusal. Every
reader downstream (Form 1040 line 7a and AGI, the tax worksheets, Form 4952, Form 8960, the EIC, QBI, the social
security worksheet) already reads Schedule D, so the stage mostly fills two zeros, fixes their sign and makes
Schedule D required when they are nonzero. Lines 8 and 13 come out zero whenever the worksheet's applicability test
fails, so the test needs no gate line (checked by brute force by both the map and the verification, 500,000 random
cases, no violation; to become a class D property).

New since the map was written:

- **OpenTaxSolver computes this worksheet itself**, line for line, from last year's return file
  (`CapitalLossCarryOverWorksheet`, `taxsolve_US_1040_2025.c` lines 540 to 600). So the worksheet lines, not only the
  downstream totals, can get an outside-engine check. One difference is expected: its line 1 reads last year's
  Form 1040 line 15 as recorded, which is floored at zero, where the worksheet asks for the amount before the floor.
  Not yet run.
- **UsTaxes takes the two carryovers as inputs** (`priorYearCapitalLossCarryover`) and the Form 4952 carryover
  (`priorYearInvestmentInterestCarryover`). It enters the carryovers on Schedule D lines 4 and 11, not 6 and 14; the
  part totals are the same.
- The 2024 Schedule D instructions are archived (`sources/2024/i1040sd`, p. 11 holds the 2023-to-2024 worksheet), as
  are the 2024 Form 1040, Schedule D, Form 4952, i8960 and Pub. 550. Inputs are cited, as Stage 16's refund worksheet
  does, to the 2025 instruction that names the 2024 line.

## Decisions for you

**D1. Inputs.** Compute the worksheet from five figures on the 2024 return (Form 1040 lines 11 and 14; Schedule D
lines 7, 15 and 21), asked only behind the gate. / Ask for the two carryover amounts (worksheet lines 8 and 13)
directly: fewer questions, but the filer does the worksheet by hand and nothing checks it. The figures are on the
2024 return a filer has in hand, and for TY2026 they are figures this tool will itself have shown on the 2025
values sheet (D4).

**D2. Two readings of the worksheet** (each an ambiguity-register entry).
(a) Line 1, "the amount from your 2024 Form 1040, line 15", with a negative amount "enclosed in parentheses" when
line 15 would have been a loss: take 2024 lines 11 and 14 and hold their signed difference, so no one computes a
negative number by hand. / One signed input with help text.
(b) Line 2, "the loss from your 2024 Schedule D, line 21": take the figure as printed, and refuse figures that cannot
be right (more than $3,000, more than the loss on 2024 lines 7 plus 15, or a loss when lines 7 plus 15 are not a
loss), with "check your 2024 Schedule D" as the remedy. *Correction:* the bound is $3,000 for any 2024 status; a 2024
married-filing-separately return followed by a 2025 single return is possible, so $1,500 cannot be assumed or
excluded. / Recompute line 2 as the allowable loss from the 2024 status (Pub. 550's "whether or not you claimed it"),
which adds a question.

**D3. Situations to refuse** (new gates, none measured): both spouses' separate 2024 returns carrying a loss into a
2025 joint return (one carrying a loss is computed); a 2024 joint return with someone other than the 2025 joint
spouse (divorce, separation, death in 2024), where only the share of "the spouse who actually had the loss" carries;
canceled debt excluded in 2025 (Form 982 and Pub. 4681, not archived); and a nonzero 2024 Form 8960 Net Gains and
Losses Worksheet line 2(i), by its own question asked only when Form 8960 is required and a carryover exists (the
present `f8960.unsupported` wording, "another net investment income adjustment", would not lead a filer to a
prior-year worksheet line). / Compute the two-return case with a two-entry collection of 2024 returns, summed (p550
p. 103, "combine your separate capital loss carryovers").

**D4. Carryover to 2026.** Compute and show both carryovers to 2026, using the same 13 lines on the 2025 return with
each "2024" read as "2025", recorded in the ambiguity register. *Correction:* the reading is supported by the archive:
the 2024 and 2025 editions of the worksheet differ only in their years (verification, error 1). Where a spouse died in
2025, show a standing caveat that the decedent's share does not carry (p550 p. 103), rather than add a question
(`f2441.spouse_died` exists but is asked only on the Form 2441 path). / Omit the display and point to the 2026
instructions. The display is the input to the TY2026 return, which is the project's target year.

**D5. The Form 4952 investment interest carryover.** Fold it in: one input, 2024 Form 4952 line 7, replaces the
`f4952.carryover` refusal on line 2, and a carryover makes Form 4952 required (f4952 p. 3, "You don't have any
carryover of disallowed investment interest expense from 2024."). UsTaxes checks it. The gate is unmeasured, so the
estimate does not move. / Leave it refused for later.

**D6. The interview.** Gate question: "Did line 21 of your 2024 Schedule D show a loss?", which can be checked
against a document and is exact (the worksheet applies only then), in place of "Is there a capital loss carried into
2025 from any earlier year?". For a filer who did not file in 2024, or whose 2024 Schedule D left out a carryover,
accept reconstructed figures with a notice that they must be the figures the 2024 return should have shown. / Keep the
present wording; refuse the reconstructed case.

Structure-changing: D1, D3 and D4. The rest are readings or small screens.

## Settled by the evidence (done this way unless you object)

1. **Sign (T-004).** Schedule D lines 6 and 14, `g28.line5` and `u1250.line16` are held negative (Dollars), so lines 7
   and 15 and the worksheets' sums stay sums. Both second transcriptions chose this, and `sd.line21` and `g28.line6`
   already work this way.
2. **When Schedule D is required.** `sd.filed` also tests a nonzero line 6 or 14 (i1040gi p. 31, Exception 1, "You
   have no capital losses"). This meets T-003's carryover trigger but not its text, so T-003 is amended: the raw-box
   test stays open with the digital-asset half (verification, error 4). Testing the line values, not the gate, keeps
   a zero carryover from forcing Schedule D.
3. **Coverage bookkeeping.** `capital_loss_carryover` gets `"refused": false` as well as empty gates; empty gates alone
   leave it counted as refused (verification, error 6).
4. **Mutation.** The five Schedule D equivalences the map named are no longer prose entries: they are accepted
   mechanically (`aliasEquivalence`; `reports/2025/equivalence_review.md` rows 83 to 89). Once lines 6 and 14 carry
   values, the rule should stop accepting them, as it should for `sd.line7.line4`, `sd.line7.line5` and
   `sd.line11.zero` (verification, error 2). The mutants then need killing fixtures; this is checked when the stage
   is built.
5. **Fixtures.** `stage3` `sales.refuse.carryover` becomes a compute case or is replaced. Four class M cases set the
   gate incidentally (`classm.asset.3`, `classm.carloan.3`, `classm.f8889.5` and its deepseek twin; the map's
   `classm.person.4` and `classm.s1.3` no longer do). Each is re-answered under the new gate or shown unaffected. The
   worksheet gets cases on both sides of every floor and `smaller_of` (line 3 at zero, line 4 both ways, lines 8, 11
   and 13 at zero), the Pub. 550 $4,000 example, and short-term-only and long-term-only carryovers (the
   verification's error 5: a short-term carryover alone moves `g28.line6`).
6. **Engines.** The OpenTaxSolver adapter writes a prior-year return file so its worksheet runs; UsTaxes gets the two
   carryovers and the Form 4952 carryover; PolicyEngine gets net gains including the carryover (its
   `long_term_capital_loss_carryover` is a memo for the 28% and section 1250 worksheets); Tax-Calculator gets the nets.
   Every difference is explained or fixed, including the line 1 floor and the UsTaxes line placement above.
7. **Reviews.** Every changed form is reviewed again under Claude and deepseek-flash (transcription, render, class M)
   and adjudicated: the new worksheet and its 2026 copy, `sd`, `g28`, `u1250`, `f1040` (a signed taxable-income helper
   for the 2026 display), and `f4952` and `f8960` if D5 and D3 stand. For `sd`, `f1040` and `f8960` the reruns also
   discharge T-057's render reruns.
8. **Left for other stages.** Schedule K-1 (Form 1041) box 11 codes C and D stay refused by `sd.other_forms` until
   Schedule E; the AMT carryover stays refused by `s2.amt`; married filing separately is unchanged. The map's backlog
   section (farm, Form 4797, the other credits and the rest) is outside this stage; the route in section E of the plan
   revision supersedes its order.

## Verified and inferred

Checked against the tree at 671826a: `sd.carryover` (Bool input, present wording) and its refusals on `sd.count` and
lines 4, 5, 6, 11, 12 and 14; `sd.line6` and `sd.line14` (Dollars copies of `sd.zero`); `sd.line7` (sum including
line 6); `sd.filed` (count, line 18, line 19); `sd.line21`; `g28.line5` and `u1250.line16` (NonNegDollars copies of
`div.screen`); `f4952.carryover` and `f4952.line2`; the `f8960.unsupported` wording; the fixtures that set the gate;
the `capital_loss_carryover` and `schedule_c` entries in `categories.json`; T-003, T-004 and T-012; the 2024 archive
manifest; the equivalence-review rows; the OpenTaxSolver worksheet code and the UsTaxes Schedule D and data model;
the citation precedent in `forms/2025/refund.yaml`; `f2441.spouse_died`.

Taken from the verification without checking again: the worksheet text and every quotation; the brute-force
property; the PolicyEngine and Tax-Calculator findings.

Inferred: that the mechanized equivalence rule stops accepting the Schedule D mutants by itself once lines 6 and 14
change; that OpenTaxSolver's line 1 differs when 2024 taxable income would have been negative (read from the code,
not run); that the gain is understated by the independence assumption (the map's inference, unmeasured).
