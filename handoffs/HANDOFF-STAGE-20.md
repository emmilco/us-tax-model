# Handoff: Stage 20 (the capital loss carryover), built and reviewed

The first stage of the route to the first coverage goal (`docs/2026-10-26_plan_revision.md` section E). The owner's
decisions are in `research/premises/stage20-capital-loss-carryover.decisions.md` (all recommended, 2026-10-27);
`sources/2025/PREMISES.md` records them; TASKS.md T-075.

## Scope

- **Computed:** the Capital Loss Carryover Worksheet (i1040sd p. 10, `forms/2025/clcw.yaml`) from five 2024 return
  figures, to Schedule D lines 6 and 14 held negative, and through line 14 to the 28% Rate Gain Worksheet line 5 and the
  Unrecaptured Section 1250 Gain Worksheet line 16; Schedule D required on a nonzero line 6 or 14; the carryovers to
  2026 shown (`forms/2025/clcw26.yaml`, the same 13 lines on this return, `amb.2025.clcw_to_2026`); the Form 4952
  investment interest carryforward from 2024 (`f4952.prior_7`).
- **Refused:** a 2024 joint return with someone other than the 2025 joint spouse, and two separate 2024 returns that
  each carry a loss into a 2025 joint return (`clcw.spouse_screen`); a 2024 line 21 that no correct 2024 return can show
  (`clcw.bad`: above $3,000, above the line 16 loss, or below the smaller of that loss and $1,500); a prior-year Form
  8960 Net Gains and Losses Worksheet line 2(i) amount on a return over the threshold (`f8960.carryforward_adj`).
  Excluded canceled debt (Form 982) was already refused by `s1.cod_unsupported`; a regression shows it with a carryover.
- **Coverage:** `capital_loss_carryover` retired; the estimate is 71.0% (from 68.6%). It is an IRS-only category
  (independence assumed), the least certain of the route's four.

## How it was built

- Forms authored in this session; two fixture cases from stage 3 and 4 that refused a carryover became compute cases.
- **Blind predictions** (`reviews/2025/blind/stage20/`): ten returns written as facts; two Opus agents worked them from
  the archived text without the encoding. Both agreed with each other and the evaluator on every value they gave (236
  asserted values, the tax included); their only differences from the project were lines the project hides.
- **Fixtures** `fixtures/2025/stage20.json`, 26 cases: the ten blind returns, refusal regressions for every new
  refusal, controls at each bound, and mutation scenarios predicted by hand.
- **Engines:** the generator draws a carryover on about one return in seven (`carry:{i}` stream, figures by Pub. 550's
  prose rule, an independent formulation) and a Form 4952 carryforward for some itemizers. OpenTaxSolver runs the
  worksheet itself from a written prior-year return file (its `CarryOverWsN` lines are compared with `clcw.lineN`, and
  its line 8 matched the generator's rule and the project on the case examined); UsTaxes takes the carryovers natively
  (`priorYearCapitalLossCarryover`, placed on its Schedule D lines 4 and 11); PolicyEngine and Tax-Calculator take the
  nets. The project's own generator derives the figures from a hash of the other answers, so its random stream is
  unchanged.
- **Reviews:** fresh Claude and deepseek-flash transcription, render and class M reviews of every changed form (sd,
  g28, u1250, f4952, f8960, clcw, clcw26; render of f1040 and qdcg, whose English names changed lines). Three Opus
  agents drafted every ruling under `.transcription/proposed/stage20/BRIEF.md`; this session checked them and applied
  them. Earlier logs are archived in `.transcription/archive/before-stage20-2026-10-27/` and
  `stage20-clcw-before-findings-fixes-2026-10-27/`. Summaries are in `reviews/2025/transcription/adjudication/`.

## Findings (all in BUG_INVENTORY.md)

- BUG-0182 (harness): OpenTaxSolver's IRA limitation left out the student loan interest line.
- BUG-0183 (display): the 28% and section 1250 worksheets were shown when Schedule D line 17 is No; caught by the blind
  predictions.
- BUG-0185, 0187 (display): the carryover worksheets were shown when the instructions say there is no carryover.
- BUG-0186 (value, on a wrong entry): an understated 2024 line 21 was accepted.
- BUG-0184 (wording, open): Schedule D lines 4, 5, 11 and 12 still say "carryover screening"; fixed with the next change to
  `sd.yaml`, as T-074 defers the line-level link of `amb.2025.sep_loss_floor`.
- T-076: review-tool defects the adjudication found (class M prompt format, `shown_when` ignored in the agreement
  check, the interface's sign of g28 line 5, a cite's document). None yielded a wrong ruling, so under plan revision B
  they wait for the next tool change.

## Facts a fresh session needs

- The applicability test is `clcw.applies` (2024 line 21 a smaller loss than line 16, or 2024 taxable income below
  zero); it decides only what is shown: lines 8 and 13 are zero without it by the arithmetic.
- The interview asks `f8960.prior_2i` at order 11, after every order-10 question, so a No to `sd.carryover` is known
  before it could be asked (the interview sorts pending questions by order, then name).
- `refusal.f4952.f4952.required.1` is recorded in `EQUIVALENT_IF` (`engine/src/mutate.ts`) with a structural check;
  it replaces the earlier P2 kill, which `f4952.required` testing line 3 made equivalent.
- Next on the route: Stage 18, the premium tax credit, from its premise map and verification (a decision batch first).
