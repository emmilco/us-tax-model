# Handoff: Stage 18 (the premium tax credit), built and reviewed

The second stage of the route to the first coverage goal (`docs/2026-10-26_plan_revision.md` section E). The owner's
decisions are in `research/premises/stage18-premium-tax-credit.decisions.md` (all recommended, 2026-10-28);
`sources/2025/PREMISES.md` records them; TASKS.md T-077.

## Scope

- **Computed:** Form 8962 Parts I to III (`forms/2025/f8962.yaml`) for single, head of household, qualifying surviving
  spouse and joint returns with any number of Forms 1095-A (`forms/2025/f1095a.yaml`, a collection): household income
  with Worksheets 1-1 and 1-2 (claimed dependents required to file by Chart B, D7(b)), the poverty line (Tables 1-1 to
  1-3, sizes 1 to 20), line 5 by Worksheet 2, the applicable figure (Table 2), the annual and monthly calculations, both
  branches below 100% of the poverty line (not an applicable taxpayer; the Marketplace-estimate exception), and the
  Table 5 limitation. The net credit goes to Schedule 3 line 9, the repayment to Schedule 2 line 1a (lines 1z and 3).
- **Refused:** Part IV allocations, Part V and the year-of-marriage column B rule, coverage of someone not lawfully
  present, a QSEHRA or individual coverage HRA, unpaid premiums, advance payments for someone in no tax family
  (`f8962.alloc`, `f8962.marriage`, `f8962.other`); the lawfully present alien branch below 100% (`f8962.alien_branch`,
  BUG-0188); two counted Forms 1095-A from one state that share a month (`f8962.two_counted`, BUG-0189); a family over 20.
  Married filing separately, a claimable filer, Forms 2555 and 8814 and the self-employed health insurance deduction
  with a Marketplace plan stay refused as before.
- **Atoms (D2):** `percent_floor` (part, whole, cap), `sum` over Counts, `multiply_rate` rounding once to a `unit`; each
  with a checker rule, rendering, and a Lean definition with proved lemmas.
- **Coverage:** `ptc` retired; the estimate is 75.6% (from 71.0%).

## How it was built

- **Tables** by `tools/extract_ptc_tables.py` (`--check` runs in `check-all`); sources `usc-26-36b` and `fr-2024-00796`
  archived as second printings (D9).
- **Blind predictions** (`reviews/2025/blind/stage18/`): twenty returns, two Opus predictors each from the archived text;
  both agreed with the evaluator on all 656 numeric values.
- **Fixtures** `fixtures/2025/stage18.json`: the blind returns, refusal and control cases, mutation scenarios, and the
  adjudication regressions (`refuse.alien_below_100`, `mut.sequential_policies_one_state`, `ftc_limit_with_repayment`).
  The `s3.line9` input left every case (1,022 keys).
- **Engines:** the generator draws Forms 1095-A on about one return in seven (`putPtc`, a derived stream), including two
  forms in one state that follow one another or nest. UsTaxes is compared only where its stub is the form (limitation
  `ustaxes_ptc_stub`); its Schedule 3 drop of a lone net PTC is `ustaxes_ptc_no_schedule3`. PolicyEngine-US was checked
  and not added (T-078). Engine differential: 0 unexplained in 539,048 comparisons. Lean and TypeScript agree on all
  1,828 cases.
- **Reviews:** fresh Claude and deepseek-flash transcription, render and class M reviews of every changed form
  (dependent, s2, s3, scope, f1095a, f8962, ftc), adjudicated by Opus agents under `.transcription/proposed/stage18/BRIEF.md`
  in four rounds (f8962 was re-reviewed after each round's findings were fixed); this session checked and applied the
  rulings. Archives: `.transcription/archive/before-stage18-2026-10-28/`, `stage18-before-findings-fixes-2026-10-29/`,
  `stage18-before-round3-2026-10-29/`, `stage18-before-round4-2026-10-29/`. Summaries in `reviews/2025/transcription/adjudication/`.

## Findings (all in BUG_INVENTORY.md)

- BUG-0188 (value): the lawfully present alien branch below 100% was computed as not applicable; now refused (D6).
- BUG-0189 (value): column B counted per form for the year, not per month (i8962 p. 16); sequential policies in one state
  lost months of column B.
- BUG-0190 (value, introduced by this stage): the foreign tax credit limit left out Schedule 2 line 1z (i1116 p. 25).
- BUG-0191 (display): Form 8962 lines shown on returns with no Form 1095-A, or after the line 5 STOP; completed over
  rounds 2 and 3 (R3 to R5), each found by the next round's adjudication.
- BUG-0192 (open, low, pre-existing): the local-law condition for an "other" household member; with the next
  `dependent.yaml` change.
- BUG-0193 (open, wording): four remedies say "entered from Form 8962"; with Stage 19, which rewrites them.
- T-079: review-tool defects found in adjudication (class M ignores `shown_when` for non-collections, generated answers
  the interview never asks, a prompt sentence that invites redefining collection fields, all-or-nothing candidate
  validation, triage witness sampling).

## Facts a fresh session needs

- `f8962.filing` (a form, and an applicable taxpayer or advance payments) is the class M filing flag and gates every line
  after line 5; `f8962.any` gates lines 1 to 5.
- A uniform Form 1095-A is entered by its monthly column A and B amounts and line 33C (the D3 route), not by the three
  line 33 totals: the same number of questions, exact monthly figures.
- `f8962.alien_below` and `f8962.estimate_100` are at interview order 11, after the order-10 screens.
- Next on the route: Stage 19, the education credits. Its decision batch is drafted at
  `research/premises/stage19-education-credits.decisions.md` and awaits the owner. It estimates 79.6% after the stage,
  so the 80% goal also needs Stage 21 (Form 5329).
