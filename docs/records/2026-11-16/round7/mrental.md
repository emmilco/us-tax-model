# Round 7, lane M-rental: report

Model claude-opus-5-5, class judgment, tax year 2025, jurisdiction us. Worktree `.claude/worktrees/mrental`, detached
at `6649c637`. No commits, no check_all, no paid reviews, no full mutate run. Patch: `round7/mrental.patch`. Lane tools
and logs: `round7/mrental-tools/` (`cases.py` holds the hand predictions; `kills.txt` and `sampled.txt` hold the
verification output).

## Outcome

Family: 89 unexplained survivors (forms rental, rec, f8582, sche, royalty, rprop).

| Result | Count |
| --- | --- |
| Killed by a new fixture case | 77 |
| Keyed argument (all inputs), lane block in EQUIVALENT_IF | 10 |
| Open: equivalent on answered inputs only, not registered | 2 |
| Defect (pending bug) | 0 |

## What was done

- **32 new fixture cases** (ids `mrental.*`). 7 are in rental.json and 10 in rec.json, both appended. The new files are
  f8582.json (8), sche.json (4), royalty.json (2) and rprop.json (1). Every number was predicted by hand from the
  archived sources before the evaluator ran. Each evidence_note cites the document and page.
  - **Numbers.** The first evaluation matched every predicted number, with no corrections.
  - **Refusals.** Each refusal was predicted by its gate. `fill_refusals.mjs` completed the form, remedy and cite from
    the evaluator only where the evaluator refused at the predicted gate, and all 19 did.
- **Lane block.** `engine/src/mutate.ts` has one contiguous block between `// ---- lane mrental begin ----` and
  `// ---- lane mrental end ----`. It holds 10 arguments built with `pinned` or `pinnedRefusal`, with digests from
  `premiseDigest`.
- **Q1 (advertising and commissions divided by days).** No expected value depends on it.
  - The div5, div8 and div11 kills use rentals where the rental part is exactly 1: every personal-use day was also a
    fair rental day (Pub. 527 p. 26).
  - Other cases use rentals with no personal use, or no rental-only costs (lines 5, 8 and 11 are $0).
  - Under either reading, the expected values are the same.

## Per mutant

Verified (V) means: `round7/mrental-tools/verify.mjs`, niced and single-threaded, applied each mutant and evaluated
the 32 cases, comparing only their expected keys, as `outcome()` in mutate.ts does. For the arguments it means
mutate.ts's own `sampledShare`, run on just these 10 (`sampled.txt`): no contradiction, and exercised on 4 to 4,099
sets each.

### Killed (77, all V)

| Mutant | Killed by (case : line) |
| --- | --- |
| filter.f8582.f8582.line1c_rental | mrental.f8582.part5_prior_loss : f8582.line1c |
| operand.f8582.f8582.loss1d.zero | mrental.f8582.part5_income_and_loss : f8582.line4 |
| operand.f8582.f8582.line8.max8 | mrental.f8582.part5_prior_loss : f8582.line8 |
| operand.f8582.f8582.line11.line9 | mrental.f8582.part5_prior_loss : f8582.line11 |
| param.f8582.special_max.$1 | mrental.f8582.part5_prior_loss : f8582.line8 |
| filter.f8582.f8582.p6_total_rental | mrental.rental.excluded_home_beside_a_loss : f8582.p6_total |
| filter.f8582.f8582.p7_total_rental | mrental.rental.excluded_home_beside_a_loss : f8582.p7_total |
| operand.f8582.f8582.exception.p5b.all.0.le.0 | mrental.f8582.part5_loss_net_gain : f8582.exception |
| operand.f8582.f8582.exception.p5c.all.1.le.0 | mrental.f8582.part5_prior_loss : f8582.required |
| operand.f8582.f8582.exception.p4c.all.2.le.0 | mrental.f8582.part4_prior_loss_net_gain : f8582.exception |
| operand.f8582.f8582.exception.p4b.all.3.le.0 | mrental.f8582.loss_over_25000 : f8582.exception |
| operand.f8582.f8582.deductions.p4c.any.1.gt.0 | mrental.f8582.part4_prior_loss_net_gain : f8582.required |
| operand.f8582.f8582.deductions.p5b.any.2.gt.0 | mrental.f8582.part5_loss_net_gain : f8582.required |
| operand.f8582.f8582.deductions.p5c.any.3.gt.0 | mrental.f8582.part5_prior_loss_net_gain : f8582.required |
| param.f8582.exception_loss.$1 | mrental.f8582.loss_one_cent_over_25000 : f8582.exception |
| param.f8582.exception_magi.$1 | mrental.f8582.magi_one_cent_over : f8582.exception |
| operand.rec.rec.w2a_line4.w2a_line3.then1 | mrental.rec.w2a_refunds_over_5d : rec.w2a_line4 (printed 2a:4) |
| operand.rec.rec.w2a_line5.w2a_line3 | mrental.rec.w2a_refunds_over_5d : rec.w2a_line5 |
| operand.rec.rec.w2a_line7.w2a_line7_capped.then1 | mrental.rec.salt_limited_no_tax_refunds : rec.w2a_line7 |
| operand.rec.rec.w2a_line8.w2a_line8_capped.then1 | mrental.rec.salt_limited_no_tax_refunds : rec.w2a_line8 |
| operand.rec.rec.line7_mfs.zero.then0 | mrental.rec.prior_mfs_spouse_itemized : rec.line7 |
| operand.rec.rec.line7.line7_mfs.then0 | mrental.rec.prior_mfs_spouse_standard : rec.line7 |
| operand.rec.rec.line11_negative.line9 | mrental.rec.negative_ti_line9_is_line3 : rec.line11 |
| operand.rec.rec.nol_negative.ti_positive.all.0.eq.0 | mrental.rec.nol_negative_ti_prior_mfs : rec.line11 |
| refusal.rec.rec.line11.1 | mrental.rec.prior_dependent_refused : rec.line11 |
| operand.rec.rec.line11_is_line3.line11.eq.0 | mrental.rec.amt_2024_split_refused : rec.line_b |
| operand.rec.rec.line_b_share.line11 | mrental.rec.split_line11_less_than_line3 : rec.line_b |
| operand.rec.rec.line_c.line_b | mrental.rec.line11_equals_line3 : rec.line_c |
| operand.rental.rental.overlap_raw.day_cents | mrental.rental.shared_costs_divided : rental[a].line7 |
| operand.rental.rental.reported.excluded.eq.0 | mrental.rental.home_15_days_totals_refused : sche.line24 |
| operand.rental.rental.div5.fair_c | mrental.rental.rental_only_costs_full : rental[a].line5 |
| operand.rental.rental.div5.total_c.whole | mrental.rental.rental_only_costs_full : rental[b].line5 |
| operand.rental.rental.line5.amt5_if_any.then0 | mrental.rental.rental_only_costs_full : rental[c].line5 |
| operand.rental.rental.div7.amt7_if_any | mrental.rental.shared_costs_divided : rental[a].line7 |
| operand.rental.rental.div7.fair_c | mrental.rental.shared_costs_divided : rental[a].line7 |
| operand.rental.rental.line7.amt7_if_any.then0 | mrental.rental.rental_only_costs_full : rental[c].line7 |
| operand.rental.rental.line7.div7.then1 | mrental.rental.shared_costs_divided : rental[a].line7 |
| operand.rental.rental.div8.amt8_if_any | mrental.rental.shared_costs_divided : rental[a].line8 |
| operand.rental.rental.div8.fair_c | mrental.rental.rental_only_costs_full : rental[a].line8 |
| operand.rental.rental.line8.amt8_if_any.then0 | mrental.rental.rental_only_costs_full : rental[c].line8 |
| operand.rental.rental.line8.div8.then1 | mrental.rental.shared_costs_divided : rental[a].line8 |
| operand.rental.rental.div10.fair_c | mrental.rental.shared_costs_divided : rental[a].line10 |
| operand.rental.rental.div11.amt11_if_any | mrental.rental.shared_costs_divided : rental[a].line11 |
| operand.rental.rental.div11.fair_c | mrental.rental.rental_only_costs_full : rental[a].line11 |
| operand.rental.rental.line11.amt11_if_any.then0 | mrental.rental.rental_only_costs_full : rental[c].line11 |
| operand.rental.rental.line11.div11.then1 | mrental.rental.shared_costs_divided : rental[a].line11 |
| operand.rental.rental.div13.fair_c | mrental.rental.shared_costs_divided : rental[a].line13 |
| operand.rental.rental.div14.amt14_if_any | mrental.rental.shared_costs_divided : rental[a].line14 |
| operand.rental.rental.div14.fair_c | mrental.rental.shared_costs_divided : rental[a].line14 |
| operand.rental.rental.line14.div14.then1 | mrental.rental.shared_costs_divided : rental[a].line14 |
| operand.rental.rental.div15.amt15_if_any | mrental.rental.shared_costs_divided : rental[a].line15 |
| operand.rental.rental.div15.fair_c | mrental.rental.shared_costs_divided : rental[a].line15 |
| operand.rental.rental.line15.div15.then1 | mrental.rental.shared_costs_divided : rental[a].line15 |
| operand.rental.rental.div19.fair_c | mrental.rental.shared_costs_divided : rental[a].line19 |
| refusal.rental.rental.line21_full.3 | mrental.rental.refusals_tenth_profit_depletion : rental[a].line21 |
| refusal.rental.rental.line21_full.4 | mrental.rental.refusals_tenth_profit_depletion : rental[b].line21 |
| refusal.rental.rental.line21_full.5 | mrental.rental.refusals_tenth_profit_depletion : rental[c].line21 |
| operand.rental.rental.line3.zero.then0 | mrental.rental.excluded_home_with_costs : rental[a].line3 |
| refusal.rental.rental.prior_loss.0 | mrental.rental.prior_loss_inactive_year : rental[a].prior_loss |
| operand.rental.rental.loss_sum.prior_loss | mrental.rental.prior_loss_inactive_year : rental[a].overall_loss |
| operand.rental.rental.has_loss.line21.lt.0 | mrental.rental.excluded_home_with_costs : rental[a].line22 |
| boundary.rental.rental.needs_4562 | mrental.rprop.form4562_needed : rental[a].needs_4562 |
| operand.rental.rental.needs_4562.count25.gt.0 | mrental.rprop.form4562_needed : rental[b].needs_4562 |
| operand.rprop.rprop.placed_this_year_cent.cent.then0 | mrental.rprop.form4562_needed : rental[c].needs_4562 |
| operand.rprop.rprop.placed_this_year_cent.zero.then1 | mrental.rprop.form4562_needed : rental[a].needs_4562 |
| operand.royalty.royalty.line20.line10 | mrental.royalty.expenses_and_loss : royalty[r].line20 |
| operand.royalty.royalty.line20.line16 | mrental.royalty.expenses_and_loss : royalty[r].line20 |
| operand.royalty.royalty.line20.line19 | mrental.royalty.expenses_and_loss : royalty[r].line20 |
| operand.royalty.royalty.income.zero | mrental.royalty.expenses_and_loss : sche.line24 |
| operand.royalty.royalty.loss_abs.line21 | mrental.royalty.expenses_and_loss : sche.line25 |
| refusal.royalty.royalty.line21.0 | mrental.royalty.refusals : royalty[r].line21 |
| refusal.royalty.royalty.line21.1 | mrental.royalty.refusals : royalty[s].line21 |
| filter.sche.sche.line23d | mrental.rental.excluded_home_with_costs : sche.line23d |
| refusal.sche.sche.line26.1 | mrental.sche.refused_grouped : sche.line26 |
| refusal.sche.sche.line26.2 | mrental.sche.refused_qbi_business : sche.line26 |
| operand.sche.sche.loss_prelimit.rent_netloss | mrental.sche.ebl_counts_rental_loss : s1.line3 |
| operand.sche.sche.loss_prelimit.roy_lossabs | mrental.sche.ebl_counts_royalty_loss : s1.line3 |

Notes on particular kills:

- **Witness worklist.** For about 40 mutants the MW worklist had marked "reaches but no reader differs" or had cut the
  search. Most of them were killable by ordinary inputs that the one-input perturbations do not reach: personal use
  together with several expense lines, an excluded home with costs, a Part V rental with a prior loss, and similar.
- **Form 4562 kills (needs_4562, placed_this_year_cent).** These assert the helper `rental[x].needs_4562`, beside
  `rf4562[form].needed`. Its only effect is whether Form 4562 is shown (i1040se p. 7, line 18). One witness is a $1.00
  improvement placed December 2025: 0.152% of $1.00 is $0.00, and Form 4562 is still needed. It is a valid input, but
  an odd one.
- **EBL kills (loss_prelimit).** These pin the recorded reading `amb.2025.s1_ebl_rental` (DECISIONS.md D15): rental and
  royalty losses count toward the excess business loss screen. They hold only while that reading stands.
- **Withheld inputs.** Two kills rely on inputs the interview leaves unanswered:
  - `has_loss` withholds `rental[a].not_at_risk`, which is unreachable when line 21 is $0.
  - `line_b_share` withholds `rec.agi_prior` and `rec.ded_prior` when 2024 taxable income was positive. The evaluator
    gives line 11 $1,500 with them withheld, so they are not reached there.

### Keyed arguments (10, V by sampled check; lane block)

| Mutant | Argument, in brief | Sets exercised |
| --- | --- | --- |
| operand.royalty.royalty.loss_abs.zero | max(max(l21,0) - l21, 0) = max(-l21, 0); unknowns and refusals pass through identically | 20 |
| operand.rental.rental.net_loss.zero | same identity on rental line 21 | 232 |
| filter.sche.sche.rents | an excluded rental's line 3 is $0; with excluded unknown both sums are unknown; no refusal path | 57 |
| filter.sche.sche.rent_income | an excluded rental's line 21 is $0 (first alternative), so its net income is $0 | 56 |
| filter.sche.sche.rent_netloss | same, for net loss | 56 |
| operand.rental.rental.home_pers10_if_any.zero.then1 | with no personal use the home test's first conjunct (0 gt 14) is false, so the all-test stops before the mutated operand | 151 |
| boundary.rec.rec.w2a_line5_more | lines 3 and 4 known and equal means 2a line 5 is $0 and line 6 is positive, so the share is $0 | 4,091 |
| operand.rec.rec.w2a_line5_more.w2a_line3.gt.0 | where line 6 > line 4 >= line 3, line 5 is $0, so the share is $0 | 4 |
| operand.rec.rec.w2a_line7_capped.zero.then1 | the alternative is taken only when line 3 <= line 4, where line 5 is $0 | 4,099 |
| operand.rec.rec.w2a_line8_capped.zero.then1 | with the cap applying and line5_more false, line 7 is also $0 | 4,099 |

Readers were checked against the data (`digests.mjs`). For example: w2a_line5_more is read only by the two capped
lines; capped7 and capped8 are read only by w2a_line7 and w2a_line8; home_pers10_if_any and home_rent_c are read only
by rental.home.

**Withdrawn argument.** I drafted an argument for w2a_line4 (then1), but it was wrong to argue it, because 2a:4 is a
printed line whose own value changes. That mutant is killed instead.

### Open: equivalent on answered inputs only (2, inferred, not verified)

- **operand.rental.rental.home.home_pers10_if_any.all.1.gt.0** (reads home_pers10).
  - The routes differ only where rental.personal_any is unanswered but days_personal is answered, and the fair days
    are under 15.
  - The interview reaches days_personal only after personal_any is Yes, so no interview-produced return tells the two
    apart.
  - It needs an ANSWERED_ONLY entry plus a keyed argument. ANSWERED_ONLY sits outside my block, so I did not add it.
- **operand.rec.rec.to_line1.zero.then1** (reads line_c).
  - rec.to_line1's only reader, refund.taxable, takes it only when rec.path is true.
  - With rec.path unknown and line 11 refused (e.g. refund.exc_tax), the mutant's to_line1 can refuse on every way where
    the data's is unknown. This needs scope.recovery or refund.itemized unanswered together with an answered exception.
  - It is an answered-only candidate on that reasoning. Not checked by execution.

### Defects

None pinned wrong; no pending bug drafted. One lead for the owner, not drafted:

- **What I saw.** In `mrental.rec.w2a_refunds_over_5d` the inputs are:
  - an income tax refund of 3,000 and a real estate tax refund of 2,000;
  - 2024 5d = 5e = 4,000.

  The model puts 3,000 on Schedule 1 line 1 and 2,000 on line 8z.
- **Why it may be wrong.** That is 5,000 taxable, more than the 4,000 deducted. Pub. 525 p. 27, Worksheet 2,
  footnote 1, says "Don't enter more than the amount deducted for the prior year" for lines 1a and 1b.
- **Why I did not draft a bug.** I did not check whether the input wording or another line is meant to enforce the cap.
- **Effect on the fixture.** The fixture asserts only 2a lines 3, 4 and 5, which do not depend on the question.

Observation, not a defect: an excluded rental with a held-back loss from a non-active year refuses its own prior_loss,
line22 and carryforward, while the return totals compute (`mrental.rental.excluded_home_beside_a_loss`).

## Verified vs inferred

- **Inspected.**
  - All 32 cases evaluate to their expected values on the data (verify.mjs baseline: 0 mismatches).
  - 77 listed mutants change an expected key of at least one case (verify.mjs, comparing as outcome() does).
  - The 10 arguments hold on the data, name the mutants' replacement lines, and pass sampledShare.
  - The worktree compiled, and `node engine/dist/main.js build` passed (build OK).
- **Inferred (unverified).**
  - **Build validation of the new fixtures.** The fixture files were written while that build was running. I have
    not shown the build validated them: the defaults consistency rules and interview path checks over the new cases.
  - **Integrator's run.** The full mutate run, with its check-step self-tests and stale-argument checks over the
    merged table, is left to the integrator.
  - **New fixture files.** I did not check whether the new per-form fixture files need registering anywhere beyond
    `caseFiles()`.
  - **Answered-only candidates.** The reasoning for the two open mutants is not checked by execution.
- **Not done.**
  - The witness addendum (`rental.addendum.md`) had not appeared when I finished. All 16 time-cut mutants are covered
    above either way.
  - No `agent_runs.jsonl` row was written by this lane; the coordinator logs the run.
