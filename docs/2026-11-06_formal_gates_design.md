# Formal gates: design

Status: approved by the owner 2026-11-06, with the recommendations on the survey's open questions. Written from the
applicability survey (`research/audits/2026-11-06_applicability_survey.md`).

## Why

The T-251 topic layer put tax claims ("no to this situation means these inputs are zero") in the interview layer,
outside the verification regime. The independent review of that layer found 43 problems, 16 of them high
(`research/audits/2026-11-06_t251_ladder_review.md`). The interview had become a second, unverified transformation of
the form data. This design moves every gate into the formal model and fixes the interview's role.

## Standing rules (owner, 2026-11-06)

1. **All tax logic lives in the formal model.** The interview gathers facts and presents them. It never derives one
   answer from another.
2. **The interview may only:**
   - word and format questions (headings, paragraphs, bullet lists, help);
   - choose a widget from the input's type (any input with a fixed set of answers is a selector);
   - order and group questions, including by earlier answers. Order never changes a computed value: the same answers in
     any order give the same values;
   - label values for display, where each label maps to exactly one value (roster labels, "Just me" for
     `["taxpayer"]`).
3. **Only the formal model can make a question disappear.** A question goes unasked only when the evaluator finds its
   input unreachable given the answers so far. The interview never suppresses a reachable input, never sets an input,
   and never shows a return as complete while a reachable input is unanswered.
4. **Wording that changes meaning is content.** A variant such as "you" against "you or your spouse" belongs in the
   reviewed form text, not in interview code.
5. **Gates are formal facts of two kinds:**
   - **applicability conditions** the instructions themselves state ("Who Must File", "Use this form if…"), formalized
     as `Bool` inputs in the forms they govern and cited to the passage that states them;
   - **existence facts** ("did you receive any interest?"), only where the instructions state no condition, each
     defined as exactly the set of situations in which a line it gates could be non-zero.
6. **Gate wording leans to yes.** A wrong "no" silently drops something; a wrong "yes" costs a few questions. Gate
   questions are worded inclusively and offer "Not sure", which is yes. Facts a person can check (a form received, a
   thing done) come before legal classifications, which are asked only after a broad yes or read from a document
   field.
7. **Every gate passes the full regime:** render and screen reviews against its cited source, the Lean comparison,
   mutation testing, and a required adversarial review asking who would answer "no" wrongly.

These rules are enforced, where mechanically possible, by checks in `check-all`:

- the interview data sets no input value, and replay yields only answers the user gave;
- for fixtures and generated returns, answering in a different order yields identical values;
- the interview never presents a state as complete while the evaluator reports a reachable unknown input.

## What the evaluator already does (survey §1; the three load-bearing points re-read in `eval.ts`)

- A `choose` evaluates its guards in order and only the alternative it takes. Inputs read only by an untaken
  alternative are unreachable, so they are never asked. A `choose` with no matching guard is unknown forever, so every
  gate needs an explicit else alternative.
- A refusal gate (`refuses: when`) is evaluated before its line's own expression, but a false gate does not hide the
  line's inputs. Screens are asked even when the line's amount is zero.
- `all` and `any` do not stop at an unknown operand: every undecided operand is asked at once. A conjunction cannot
  make one question wait for another.
- An empty roster sums to zero and asks nothing. Arithmetic evaluates every operand, so a zero does not hide the rest.

So a gate hides an input only when **every reader of that input sits under a `choose` on the gate**, or when the input
belongs to an empty roster.

## Three kinds of gate

| Kind | What it is | New input? | Example |
|---|---|---|---|
| **A, applicability** | A condition the instructions state about the filer ("Use this form if…") | a `Bool` in the governed form, cited to the passage | Form 4952 investment interest; Schedule B line 7a gating FinCEN 114 |
| **B, existence** | "Does this kind of amount exist?", where no instruction states a condition | a `Bool`, defined as exactly the lines it gates | dividends; charitable gifts |
| **C, computed condition** | A condition the instructions state on amounts the model already computes | none | Form 1116 election only when foreign tax is above zero; Form 8880 AGI limit; 1099-DIV boxes that are parts of box 1a or 2a |

**Filing thresholds are not gates.** The Schedule B $1,500, the Form 8283 $500 and the Schedule SE $400 decide whether a
form is filed, never whether an amount exists, so they never hide an amount input.

## Model conventions

- **One gate line per gated input.** A gated input is renamed (`div.box2b` → `div.box2b_amount`), and its old id becomes
  a `choose` on the gate with an explicit else of zero, false or empty. Every reader keeps reading the old id, so no
  reader can be missed. The rename changes input keys, the question bank and the fixtures: one mechanical migration,
  checked by `test-fixtures`. A check fails if any line other than its gate line reads a gated input.
- **Leaking conjunctions are rewritten as nested `choose`** where order matters, so the second question waits for the
  first. The evaluator's `all`/`any` semantics stay unchanged. A change there would alter reachability across the
  whole model and the Lean evaluator, and belongs with T-248.
- **"You or your spouse"** is the wording of every per-return gate.
- **Unarchived sources gate nothing.** A New York condition that rests on an unarchived source (IT-214, IT-272,
  IT-225, the inflation-check line) stays a direct question until the source is archived.

## Verification

- **Existing reviews** rerun on every changed form: transcription, render, class M and completeness, as the inference
  cost rules require (review what changed).
- **The screen review is extended to `choose`-guard gates first.** Today `screen_review.py` covers only `Bool` refusal
  gates, so new gates would go unreviewed. No gate lands before this extension.
- **An adversarial gate review** ("who would answer no wrongly?") becomes a standing review kind beside the screen
  review: logged per form, rerun when a gate's wording or gated lines change. Its first input is the 43 findings of
  the T-251 review, each either designed out by an A or C gate or turned into a test.
- **Mechanical checks** in `check-all`:
  - the interview rules of the standing rules (no input set by the interview; order independence; no early
    completion);
  - each gated input is read only by its gate line;
  - every `choose` gate has an else;
  - the fixtures and generated returns reach the same values;
  - mutation testing covers the new gate lines.
- **Lean:** the new lines use existing operations, so the Lean evaluator needs no new semantics. Form-data commits are
  fast tier (`tools/tier_paths.py`); `compare`, the engine differential and mutation run in the full tier at each release
  (`tools/release.sh`), which covers the new lines.

## Scope of the first build (survey §6; estimates)

- **C gates, no new inputs:** about 30–35 lines across 13 forms: ftc, div, f1040, qbi, s1, household, s8812, w2, f8880,
  person, sa, f4952 and ny_it201.
- **Core new `Bool` inputs:** B-1 dividends, B-3 charitable gifts, A-1 investment interest, and A-2 (Schedule B
  line 7a, which exists but is unreached).
- **Not in the first build:**
  - B-2 (Schedule 1 line 8 income): the largest saving and the largest risk. A wrong "no" drops nine lines, and the
    instructions call their own table "a general guide".
  - The optional B-4 to B-6.
  - Deriving `$ny_it2` from `$w2`.
- **Split from `sb.unsupported`:** the Form 5471 clause (review finding L-34), so the rest can be gated by interest or
  dividends.
- **Estimated effect on `ny.table.single.0`:** 165 to about 115–120 questions. Estimated, not measured.

## Branch and sequence

1. **New branch from `main`.** The two T-236 presentation commits (`f36673c`, `ae19d5f`) are cherry-picked onto it.
   The topic-layer commits (`0f84950`, `204cc77`) and the ladder proposal stay on the old branch as a record, and are
   not merged.
2. **The interview-rule checks.**
3. **The screen review extended to `choose` gates, and the adversarial gate review tool.**
4. **C gates, form by form.** Each round: full tier, then the changed forms' reviews.
5. **Core A and B gates,** each with its adversarial review.
6. **Measure the question count;** decide on B-2 and the optional gates from the measurement.
7. **Restructure the long questions** into headings and bullets (render reviews).

Paid review costs are logged per round in `.transcription/costs.jsonl`, and each round is estimated before it runs.

## Rare-situation pages (owner, 2026-11-06)

A presentation rule within the interview layer's grouping; it changes where a gate appears, never what is computed.

- Gates answered yes by fewer than about 10% of all filers are not asked one by one up front. They are gathered at the
  end under "Less common situations". The exact cut is set at the natural gap in the frequency distribution.
- Frequencies come from the coverage estimate (`tools/coverage/`: IRS Statistics of Income counts and PolicyEngine
  microdata) where it can measure them, otherwise from a recorded judgment. Each gate's estimate and its source are
  recorded beside it in the data.
- The page is a grid: one row per gate, each row answered Yes, No or Not sure (Not sure is yes). Every row must be
  answered before moving on; no row defaults to no.
- A grid has at most about 8 rows. Longer sets are split into themed grids (for example work and income; family;
  property and investments).
- A row's follow-up questions are asked after its grid.

## Question hierarchy after the first build

Each line is one question. A question indented under another is asked only when the answer above makes it matter.
Tags: **[A]** an applicability condition from the instructions (new question); **[B]** an existence fact (new
question); **[C]** asked only when an amount already computed makes it matter (no new question); untagged questions
are asked as now. Groups follow the current asking order; the walk of `ny.table.single.0` asks every untagged
top-level item. Derived from the applicability survey; the counts after the build are measured, not taken from here.

- Who is on this return (just me / me and my spouse)
  - For each person: whose entry is this (taxpayer or spouse)
  - For each person: under 16, 65 or older, blind
- Filing status
- Married at the end of 2025; spouse died in 2025; community-property state
- Scope screens (as now; restructured into headings and bullets in step 7)
  - Credits this tool does not figure
  - Income or return treatment outside what this tool handles
  - Additional line 16 taxes
  - Schedule 1 items this tool does not ask separately
- Rosters: Marketplace 1095-A forms; 1099-R distributions; dependents; employers (W-2); interest payers; HSAs; sales;
  businesses (Schedule C)
  - For each W-2: boxes 1–7
  - For each W-2: any box 12 codes [C: asked only while the saver's credit or combat pay can still use it]
  - For each interest payer: amount; early-withdrawal penalty
- Dividends: did you (or your spouse) receive any dividends or fund distributions, with or without a form [B]
  - Ordinary dividends (1099-DIV box 1a)
    - Qualified dividends (box 1b) [C: only if box 1a is above zero]
    - Section 897 ordinary dividends (box 2e) [C]
    - Section 199A dividends (box 5) [C]
  - Capital gain distributions (box 2a)
    - Unrecaptured 1250 gain, 1202 gain, collectibles gain, section 897 gain (boxes 2b, 2c, 2d, 2f) [C: only if box 2a
      is above zero]
  - Nondividend distributions (box 3)
    - Basis reconciled for the nondividend distributions [C: only if box 3 is above zero]
  - Cash and noncash liquidation distributions; exempt-interest dividends (boxes 9, 10, 12, 13)
- Schedule B
  - Foreign trust distribution or grantor (line 8)
  - Financial interest in or signature authority over a foreign account (line 7a) [A: moves to the front of Schedule B]
    - FinCEN 114 required [A: only after a yes on line 7a]
  - Form 8938 (specified foreign financial assets)
  - Form 5471 clause, split out of the Schedule B screen (review finding L-34)
  - Other Schedule B special treatment [C: only if interest or dividends are above zero]
- Schedule D: capital loss carryover; gains from other forms
- Payments: other withholding (1099, W-2G and others); estimated payments; amount applied from 2024; Schedule 3 lines
  10 and 14
- Schedule 1
  - State or local refund received; alimony; unemployment compensation
  - Educator expenses; student loan interest; Social Security benefits
  - Line 8 income items: cancelled debt, gambling winnings, 8g, 8h, 8i, 8j, 8r, other line 8 items (as now: B-2 is not
    in the first build)
    - Jury pay given to your employer [C: only if jury pay (8h) is above zero]
  - Other income (8z) roster
- Schedule 1-A: car loan interest; tips; overtime
- Schedule 2 and 3 screens: alternative minimum tax; other taxes; other person items; Schedule 3 line 12
- Schedule A
  - Charitable gifts: did you (or your spouse) give anything to a charity in 2025, or carry a charitable contribution
    forward from an earlier year [B]
    - Cash gifts (line 11)
    - Noncash gift groups (roster)
    - Gifts subject to the special limits [C: only after a yes]
  - Medical expenses; state and local income taxes; real estate and personal property taxes; mortgage interest
  - Can be claimed as a dependent; excluded income; unsupported Schedule A items
  - Elect to itemize [C: only if itemized deductions are above zero and no more than the standard deduction]
- Investment interest: did you (or your spouse) pay interest on money borrowed to buy investments, or carry
  investment interest forward from 2024 [A]
  - Investment interest paid; carryover
  - Election to include qualified dividends or gains (line 4g) [C: only if interest paid or carryover is above zero]
- Foreign tax: foreign tax paid
  - Election without Form 1116: all foreign income passive; statements received; eligible; elect [C: only if foreign
    tax is above zero]
- Credits and other screens: education expenses paid; Additional Medicare tax screen; railroad retirement; section 179
  carryover; QBI screen and carryforward; dependent care benefits and expenses; home energy parts I and II
- Saver's credit
  - Eligibility: age, student, claimed as a dependent [C: asked first]
    - AGI within the limit [C, computed]
      - Traditional IRA, Roth IRA, ABLE and voluntary contributions; excess contributions [C: only if eligible]
- EIC and child tax credit history
  - Form 8862 (credit reduced or disallowed before) [C: only if claiming the EIC, CTC, ODC or ACTC]
  - Puerto Rico residence for the child tax credit [C: only with a qualifying child]
  - Combat pay [C: only with a W-2 box 12 code]
- New York
  - Residency: state, city, spouse, special accrual, Yonkers
  - New York W-2 records (roster) and their withholding
  - Government and private pension exclusion (lines 26, 29) [C: only with federal pension income]
  - Interest on U.S. obligations (line 28) [C: only with federal interest or dividends]
  - Dependent care credit (line 64) [C: only with federal care expenses]
  - MCTMT [C: only with self-employment earnings above $50,000 per person]
  - 529 account: nonqualified withdrawal (line 22) [C: only with a 529 deduction (line 30)]
  - 529 refund; amount applied to 2026 (line 79) [C: only with an overpayment]
  - Other New York questions (about 25; as now)
