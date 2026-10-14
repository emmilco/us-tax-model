# Architectural difficulties and strategies

Research date 2026-10-13. Live IRS sources read this session are the tax year 2025 revisions; the final TY2026 forms and instructions are not yet published. Anything stated about TY2026 is flagged as such.

## Summary

- **The forms layer is not closed under the proposed slice.** A filer with excess Social Security withholding has combined wages above the wage base ($184,500 for 2026; $176,100 for 2025). That is close to the $200,000 threshold for Additional Medicare Tax (Form 8959) and Net Investment Income Tax (Form 8960). A 1099-DIV can also pull in Form 8995 (box 5), Form 1116 or its election (box 7), and the Schedule D Tax Worksheet (boxes 2b and 2d). A sound engine must transcribe the gating conditions of forms it does not compute, so it can refuse instead of silently producing a wrong return.
- **"Faithful transcription is mostly mechanical" holds for worksheet arithmetic and fails for almost everything else.** The Qualified Dividends and Capital Gain Tax Worksheet is 25 lines of add, subtract-floor-zero, smaller-of, multiply and lookup. The hard content is in routing prose, per-row classification on Form 8949, rounding conventions and taxpayer judgments such as cross-account wash sales and wrong broker basis.
- **The oracle problem is severe.** A typical worksheet line gets one or two independent checks, and one example exercises only one side of each "smaller of". Open calculators are weak oracles exactly where the slice is hard. UsTaxes' Form 8949 appears to hard-code boxes C and F and leave the adjustment columns unimplemented.
- **There are no true simultaneous cycles inside the slice.** There are form-level apparent cycles (1040 → Schedule D → 1040 line 7 → worksheet → line 16) that vanish at line granularity. There is one cross-year dependency: the capital loss carryover.
- **Rounding is the main source of one-dollar mismatches.** The Tax Table (mandatory under $100,000) is a step function. TaxCalcBench attributes most of the 15–20 point gap between strict and ±$5 scoring to models using bracket arithmetic instead of the table.
- **Form 8949 now has twelve boxes.** Boxes G–L for digital assets were added for 2025. Direct entry on Schedule D lines 1a and 8a (Exception 1) is conditional on per-transaction facts.
- **LLM evidence does not support unverified use.** Frontier models get under a third of simple returns strictly right when computing directly. Auto-formalization to logic programs has 15–20% wrong answers among attempted cases without expert-written statute encodings.
- **Direct File's Fact Graph is the closest prior art** for completeness tracking and a declarative interview. It is open source, but Direct File did not run in the 2026 filing season. Its public spec does not address cycles or explanation.
- **PDF filling works but is brittle.** UsTaxes moved from positional field order to explicit field names for 2024 onward. Free File Fillable Forms does not accept attachments, which limits Form 8949 Exception 2.

## Findings

### 1. Dependency graph and cycles

**How others handle it**

- **Fact Graph (IRS Direct File).** Facts are either `Writable` or `Derived`, and derived facts name their dependencies by path. The 3.1 specification does not address circular dependencies. Reported scale is about 3,000 facts. Source: https://github.com/IRS-Public/fact-graph/blob/main/docs/fact-dictionary-specification-3.1.md and https://alexthemark.substack.com/p/direct-file-is-open-source. Confidence: High on structure. Lazy, memoized evaluation is my recollection, not re-verified: Low.
- **OpenFisca (and so PolicyEngine).** Evaluation is lazy and recursive with caching. Core separates a "cycle" (same variable, same period; aborts) from a "spiral" (same variable, different period). The older behaviour of capping loops and returning a default gave results that were inconsistent with caching. Source: https://github.com/openfisca/openfisca-core/pull/817. Confidence: Medium (search summary of the PR).
- **Tax-Calculator.** `calc_all` is a hand-written sequence of function calls with no graph. Source: https://github.com/PSLmodels/Tax-Calculator/blob/master/taxcalc/calculator.py. Confidence: Medium (the inner `_calc_one_year` body was truncated).
- **Mlang / M.** The legacy French system calls the M rules several times with particular variable values. Merigoux's 2019 post says this was initially missed. Source: https://blog.merigoux.ovh/en/2019/12/20/taxes-formal-proofs.html. Confidence: High for that. From recollection of the CC 2021 paper, not re-read: M rules are unordered and topologically sorted, and the repeated calls live in a separate orchestration layer ("M++"). Confidence: Low.
- **OpenTaxSolver.** Imperative C, one program per form, with ordering by statement sequence. Source: https://opentaxsolver.sourceforge.net/program_structure.html. Confidence: Medium on layout; ordering is from recollection.
- **Real cycles in the 1040 family.**
  - Self-employed health insurance deduction and premium tax credit is a true simultaneous system. Intuit documents cases that do not converge within $1 and alternate between two states. Source: https://accountants.intuit.com/support/en-us/help-article/review-tax-return/calculation-se-health-insurance-deduction-claiming/L3xcftxAz_US_en_US. Confidence: Medium (search summary).
  - Taxable Social Security and the IRA deduction: the IRS breaks the cycle by substitution. The 1040 instructions say "use the worksheets in Pub. 590-A to see if any of your social security benefits are taxable and to figure your IRA deduction." Source: https://www.irs.gov/instructions/i1040gi. Confidence: High.
  - AMT and foreign tax credit is re-evaluation of the same form under different inputs, not a cycle. State refund taxability is a cross-year dependency. Confidence: Medium (domain knowledge, not re-verified).

**Within the slice**

No simultaneous cycle exists. The line-level order is: Form 8949 → Schedule D lines 1–16 → line 21 loss limit → 1040 line 7 → line 15 → Schedule D lines 17–22 routing → worksheet → line 16. One cross-year input exists: the Capital Loss Carryover Worksheet for Schedule D lines 6 and 14 needs prior-year figures (https://www.irs.gov/instructions/i1040sd, High).

**Recommended strategy (opinion)**

- Use a line-level DAG, evaluated lazily with memoization.
- Check acyclicity statically at build time, and treat any cycle as a build error.
- Do not build fixed-point iteration. When a real cycle arrives, transcribe the IRS's own published cycle-breaking worksheet as ordinary lines.
- Model "same form, different inputs" as a parameterized form instance.
- Model prior-year values as explicit inputs with their own provenance.

### 2. Interview design and question minimization

**How others handle it**

- **Docassemble** is goal-directed. `mandatory` blocks run in order, and an undefined variable triggers a search for a block that defines it. Logic is re-evaluated on every screen load. The docs warn that the number of evaluations is hard to predict and blocks must be idempotent. Source: https://docassemble.org/docs/logic.html. Confidence: High.
- **Fact Graph.** A writable fact may carry a placeholder. Any fact depending on a placeholder remains "incomplete", and `IsComplete` is an operator usable in conditions. Direct File's flow is a separate declarative artifact from the facts; an "all screens" renderer shows which tests each question affects. Sources as in item 1. Confidence: High on completeness; Medium on the flow/fact split.
- **DMN decision tables.** Hit policies (Unique, Any, First, Priority, Collect) make overlap semantics explicit, and tools check tables for gaps and overlaps. Confidence: Medium (standard knowledge, not fetched).

**Recommended strategy (opinion)**

- **Derive what must be asked; hand-author the order.** The needed set of inputs is the backward slice from the target lines under current answers. Topic grouping and wording are authored. Totality and termination are then properties of the derived set.
- **Use three-valued completeness**: unknown, placeholder, known. The return is producible only when every reachable line is known.
- **Make gating questions first-class facts** with their own citations. They must include out-of-scope detectors (for example "any 1099-DIV box 2b, 2d, 5 or 7 nonzero").
- **Handle "I don't know" as a state** that either routes to a help path naming the source document box, or halts. Never use it as a default.
- **Store an append-only answer log** and recompute everything from it, so the result is independent of answer order. That gives a simple theorem: same answers, same return.
- **Be honest about the proof.** "No contradictory states" is provable only over the engine's fact vocabulary. It cannot rule out a user's answers contradicting their documents.

### 3. Default-and-exception logic

**How others handle it**

- **Catala** adopts prioritized default logic, because legal text follows a default-then-exception pattern. Source: https://arxiv.org/abs/2103.03198. Confidence: High.
- **Fact Graph** uses `Switch`, where the first true `Case` wins and `<True/>` is the default, plus `Override`. Source: fact dictionary spec. Confidence: High.

**Recommended strategy (opinion)**

- Forms-layer text is mostly procedural ("if line 3 is more than line 4, enter…; otherwise…"), not scattered across sections like a statute. Catala's main benefit, locality to dispersed statute text, matters less here.
- Use guarded alternatives with an exhaustiveness and disjointness check. Each guard carries the citation of its own sentence.
- Allow an explicit ordered `exception` wrapper only where the instruction literally says "Exception".
- First-match lists hide overlap bugs, so avoid them as the general form.
- The Form 8949 "Exception 1" is a predicate over the set of transactions, not a line rule. No option here stays close to the text without a quantifier.

### 4. Rounding

**How it is specified and handled**

- "You can round off cents to whole dollars on your return and schedules. If you do round to whole dollars, you must round all amounts." Source: https://www.irs.gov/instructions/i1040gi. Confidence: High.
- Schedule D instructions add: when adding two or more amounts, "include cents when adding the amounts and round off only the total." Source: https://www.irs.gov/instructions/i1040sd. Confidence: High.
- Form 8949 instructions use the same half-up rule ($1.50 becomes $2). Source: https://www.irs.gov/instructions/i8949. Confidence: High.
- "If your taxable income is less than $100,000, you must use the Tax Table"; at or above, the Tax Computation Worksheet. Worksheet lines 22 and 24 invoke the same rule. Source: 1040 instructions. Confidence: High.
- The table uses $50 bands ($25 under $3,000) with tax at the band midpoint. Only secondary sources say so. Confidence: Medium.
- TaxCalcBench reports the 15–20 point gap between strict and ±$5 scoring is largely from bracket arithmetic used in place of the table, with a $3 example. It also notes rounding ambiguity can allow more than one acceptable strict value. Source: https://arxiv.org/html/2507.16126v1. Confidence: High.
- Fact Graph has `Round` (half up), `Floor` and `Ceiling` over a BigDecimal `Dollar`. Confidence: High.

**Where one-dollar differences arise (opinion)**

1. Rounding each W-2 box 1 before summing, versus rounding the sum.
2. Summing rounded 8949 rows versus rounding broker totals entered on line 1a.
3. Bracket formula versus table.
4. Rounding the 15% and 20% products per line versus carrying cents.
5. Half-up versus banker's rounding in library defaults.

**Recommended strategy (opinion)**

- Hold integer cents internally.
- Make the rounding policy a named, cited, return-wide setting (`whole-dollar` or `cents`).
- Apply rounding as an explicit atom at "enter on line" points, with sums taken over unrounded operands as the instruction says.
- Store the Tax Table as pinned data. Separately test the conjecture "cell = round(tax at midpoint)" against every cell. That is a rare exhaustive oracle.
- The $100,000 boundary is a discontinuity in method; test both sides.

### 5. Cross-form flows and multi-copy forms

**How others handle it**

- **Fact Graph.** Collections with `*` paths; `CollectionSum`, `Filter`, `Count`, `Maximum`; items refer to siblings by `../`. Confidence: High.
- **UsTaxes.** One class per form per year; extra 8949 copies are spawned at 14 rows per page. Source: https://github.com/ustaxes/UsTaxes/blob/master/src/forms/Y2024/irsForms/F8949.ts. Confidence: Medium (model-summarized).

**Recommended strategy (opinion)**

- A reference is a typed value `(form, revision, instance selector, line, column)`.
- "Enter the amount from Schedule D, line 16" becomes `Copy(ref)`. The build checks that the target exists in that revision and that its type matches.
- Multi-copy forms are keyed collections: W-2 by (person, employer EIN); 8949 by (part, box). Pagination is a rendering concern, not a semantic one.
- Aggregation is an explicit `SumOver(collection, filter, column)` atom.
- The excess Social Security check needs grouping by person, then a per-employer cap, then a sum. That is three aggregation shapes in one line.

### 6. Form 8949 and Schedule D

**Verified against the live 2025 instructions (https://www.irs.gov/instructions/i8949, High)**

- **Boxes.** A/B/C short term and D/E/F long term: basis reported to the IRS; not reported; no 1099-B. G/H/I short term and J/K/L long term for digital assets, new for 2025: "Do not use box C to report digital asset transactions. Use box I."
- **Exception 1.** No Form 8949 is needed where basis was reported, there are no adjustments in 1099-B boxes 1f or 1g, the Ordinary box is not checked, no adjustment is needed, and there is no qualified opportunity fund deferral. Totals go on Schedule D line 1a or 8a. Collectibles are excluded.
- **Exception 2.** Attached statements with the combined totals on a row marked code M. Individuals cannot substitute "available upon request".
- **Column (f) codes.** B, C, D, E, H, L, M, N, O, P, Q, R, S, T, W, X, Y, Z.
- **TY2026.** An IRS 2026 draft of Form 8949 is listed (dated May 2026) but I could not read its contents. Whether the box set is unchanged for 2026 is unverified.

**Interview must establish per sale (opinion, derived from the above)**

- Is there a 1099-B or 1099-DA?
- Is basis reported to the IRS?
- What is the term: the broker's box, or dates?
- Is it a digital asset?
- Are 1f or 1g nonzero?
- Is the Ordinary box checked?
- Is it a collectible or a qualified opportunity fund transaction?
- Is the reported basis correct?
- Are there unreflected selling costs?
- Is the taxpayer a nominee?
- Is there a wash sale the broker did not report (for example across accounts)?

Also needed: the prior-year carryover, capital gain distributions, and the lines 18–19 triggers.

**Modelling difficulties (opinion)**

- Imported broker data has no standard open format. Hundreds of rows make per-row questions impossible, so classification must run on imported fields with questions asked per lot group.
- "Is the basis correct?" is not mechanical. Employee stock (RSU and ESPP) commonly carries understated basis, and this population overlaps the two-W-2 filer.
- UsTaxes appears to support only boxes C and F and no adjustments, with rows that ignore fees while totals include them. So it cannot serve as an oracle here. Confidence: Medium.

### 7. Yearly diffing and migration

**How others handle it**

- UsTaxes copies a directory per year, with a JSON schema per year for PDF fields and a `formgen` skeleton generator. Source: https://github.com/ustaxes/UsTaxes/blob/master/docs/ARCHITECTURE.md. Confidence: High.
- Fact Graph has a `TaxYear` element on facts. Confidence: High.
- Tax-Calculator and PolicyEngine separate parameters by year from formulas. Confidence: Medium (recollection).
- For scale of churn: 2025 added Schedule 1-A, Form 1040 line 13b and six 8949 boxes (1040 and 8949 instructions, High).

**Recommended strategy (opinion)**

- Keep form definitions as data, one file per form revision.
- Give each line a stable semantic ID that is separate from its printed number. Renumbering is then a one-field diff, detected by matching line text across years.
- Keep parameters (thresholds, rates, wage base) in a table per year, each with a citation. The worksheet thresholds are different printed numbers each year over identical structure.
- Pin examples to a revision and never carry them forward silently.
- Draft forms appear around May to October and finals in December or January. Build against drafts, with a mandatory re-diff when the final is released.

### 8. Output

**How others handle it**

- UsTaxes fills IRS PDFs with pdf-lib. For 2024 onward it uses explicit AcroForm names through `fillInstructions()`; the order-derived path is called a "legacy bridge" for 2020–2023. Confidence: High.
- IRS field names follow `topmostSubform[0].Page1[0].f1_02[0]` and reportedly change between revisions. Confidence: Medium (practitioner sources only).
- Free File Fillable Forms "does not allow you to attach any documents to your return, except those available through the program". It allows up to 50 W-2 copies. Source: https://www.irs.gov/e-file-providers/free-file-fillable-forms-program-limitations-and-available-forms. Confidence: High.
- Publication 1167 (Rev. Proc. 2025-27) governs substitute forms. I could not read its body.

**Recommended strategy (opinion)**

- Produce both outputs, with the values sheet as primary. It is a line-by-line list in the entry order of Free File Fillable Forms, with citations, and it survives field-name drift.
- Treat the filled official PDF as a convenience. Use an explicit per-revision field map, verified by a round-trip test: fill, re-extract, compare.
- Fill the IRS's own PDF and never redraw forms, which avoids substitute-form approval questions.
- Because attachments are not accepted, Exception 2 is effectively unavailable to a Free File Fillable Forms user. The engine should emit individual rows or line 1a/8a totals, and should say so.

### 9. Provenance and explanation

**How others handle it**

- Catala's CLI has a `--trace` option that prints the interpreter's computation. Its package also has an `Explain` module with graph output options and a base source URL. Source: https://ocaml.org/p/catala/latest/doc/Explain/index.html. Confidence: Medium (existence verified; behaviour not).
- Fact Graph facts carry descriptions with citations. The public spec has no user-facing derivation trace. Confidence: Medium.
- Jurayj et al. argue symbolic execution gives a stronger audit trail than chain-of-thought. Source: https://arxiv.org/html/2508.21051v3. Confidence: High.
- Provenance semirings (Green, Karvounarakis and Tannen, 2007) are the database-theory basis for "why" provenance. Not fetched.

**Recommended strategy (opinion)**

- Have the evaluator return `(value, derivation tree)` for every line. Each node records the atom, operands, citation and rounding applied. With a small atom set this is nearly free.
- For a lay reader, render it as the worksheet itself, filled in, with each line's instruction sentence beside it and click-through to source lines.
- Record guards not taken ("you did not use the Schedule D Tax Worksheet because lines 18 and 19 are zero"). Routing explanations matter more to trust than arithmetic.
- A semiring formalism is more than this needs. A tree is enough.

### 10. LLM-assisted transcription and verification

**Evidence**

- **TaxCalcBench (TY2024, 51 cases).** The best model had 32% of returns strictly correct and about 81% of lines correct. Results were inconsistent across runs. Confidence: High.
- **Jurayj, Holzenberger and Van Durme (SARA, 100 cases).** Zero-shot translation to Prolog: o3 had 75 correct, 15 wrong and 10 abstained; GPT-5 had 53, 13 and 34. With expert-written statute encodings and exemplars: 86–87 correct. Confidence: High.
- **Lorenzo et al. (NLLP 2025).** A benchmark for Catala generation from legal text; it reports feasibility. I could not read the numbers. Source: https://aclanthology.org/2025.nllp-1.4/.
- **CUTECat.** Concolic test generation for Catala programs (https://2024.splashcon.org/details/prolala-2024-papers/6/CUTECat-Generating-Testcases-for-Fiscal-Laws-through-Concolic-Execution), which is the relevant technique for branch coverage.

These studies test statutes and whole returns, not worksheet transcription. Worksheets are easier, but I found no measurement of that task.

**The oracle count (opinion)**

For a typical worksheet line:

1. A human line-against-line read. This is real but fatigable.
2. A second independent transcription and diff. This is strong only if truly independent; two LLM runs from the same PDF share misreadings.
3. Round-trip rendering to English. It catches structural slips but not a wrong threshold digit that is rendered back faithfully.
4. Official worked examples: often zero or one per worksheet, covering one side of each branch.
5. Differential testing against other calculators. This is useful on mainstream lines; it is weak on Form 8949, and one-dollar rounding noise masks real errors.

Realistically that is one to two genuinely independent checks per line, and fewer on rarely taken branches. Mutation testing will make this visible. For example, "smaller of line 1 or line 6" mutated to "line 6" survives any example where line 6 is the smaller.

**Recommended strategy (opinion)**

- Use an LLM as one of two transcribers; the other is a human or a structurally different extraction.
- Diff parameters separately against a second source.
- Generate branch-covering inputs by symbolic execution of the formal worksheet, and have a human work those by hand on the official PDF.
- Publish the mutation score per worksheet as the honesty metric.

### 11. Typed atoms

**A plausible set (opinion)**

- `Input(source box)` and `Copy(ref)`
- `Add`, `Subtract`, `SubtractFloorZero`
- `SmallerOf`, `LargerOf`
- `MultiplyRate`
- `Param(year, filing status)`
- `TableLookup`
- `SumOver(collection)`
- `Guard(predicate)`
- `Round(policy)`

The Qualified Dividends worksheet as fetched uses only the first nine of these. Fact Graph's operator list is almost the same set, plus dates, enums and `StepwiseMultiply`. That is independent evidence the set is roughly right.

**What composes**

- Totality and termination, trivially.
- Type and unit correctness.
- Non-negativity where it is derivable.
- Monotonicity, but only with sign tracking, since `Subtract` is antitone in its second argument.
- Exact integer arithmetic.
- Permutation invariance of `SumOver`.

**What does not compose**

- Worksheet-level monotonicity in income, across the min and subtract structure. It needs a per-worksheet proof or a property test.
- Continuity. The Tax Table is a step function, and the method switches at $100,000.
- Split invariance. Splitting one sale into two changes rounded totals.

**Where the picture breaks**

- "See instructions".
- Free-text predicates ("if you are required to file Form 4952").
- Elections.
- Yes/no routing lines (Schedule D lines 17–22).
- Write-ins and attachments.
- Quantified conditions over transactions (Exception 1).
- Judgment facts ("is the reported basis correct?").

All of these can be modelled as opaque boolean inputs with citations. That keeps the calculus clean by moving the difficulty into the interview, and it should be described that way publicly.

## Ranked risks

1. **Scope leakage and unsound gating.** The slice's own inputs trigger unsupported forms (8959, 8960, 8995, 1116, Schedule D Tax Worksheet, Schedule 1-A items, carryovers). Refusing correctly requires transcribing gating text across many forms. A wrong return that looks well evidenced does the most damage to the trust goal.
2. **Oracle scarcity.** One to two independent checks per line, common-mode LLM error, and weak open calculators on Form 8949. The "publicly verifiable" claim depends on evidence that is thin on rare branches.
3. **Form 8949 input reality.** Broker imports, per-row classification, adjustments, and judgment facts such as basis correctness and cross-account wash sales. This is where "mechanical transcription" is weakest, and where the output channel also fails (no attachments).
4. **Annual churn against a small team.** TY2026 finals arrive around the turn of the year. Recent years added a schedule, a 1040 line and six 8949 boxes. Without the diff tooling built early, each year is a re-transcription.

Rounding is a persistent irritant but not project-threatening.

## Recommended engine architecture

Opinion.

- **Layer 0, data.** Per-revision form definitions (lines with stable IDs, printed numbers, instruction-text anchors), per-year parameter tables and the Tax Table. All are pinned and cited.
- **Layer 1, atom calculus.** About a dozen total, pure functions over integer cents and typed references. Each worksheet is a list of lines, each an atom application plus citation. A build step checks references, types, guard exhaustiveness and disjointness, and line-level acyclicity.
- **Layer 2, evaluator.** Lazy and memoized over the line DAG with three-valued completeness. It returns values with derivation trees, and applies the rounding policy as an explicit atom. No fixed-point machinery.
- **Layer 3, interview.** The needed-inputs set is derived by backward slicing under current answers. Order and wording are authored. An append-only answer log is recomputed from scratch. Out-of-scope detectors are ordinary gating facts whose result is a cited halt.
- **Layer 4, output.** A values sheet first, a filled official PDF second with a per-revision field map, and a rendered explanation.

No LLM is used at runtime. At authoring time an LLM is one of two transcribers.

## First vertical slice

Opinion. The Qualified Dividends and Capital Gain Tax Worksheet is a good first worksheet and a poor first architecture test. It is 25 lines of the cleanest atoms, has no collections, no exceptions and no elections, and has one routing condition. It would validate the transcription format and the Tax Table handling, and say nothing about the hard parts.

A better shape test is a thin end-to-end thread:

1. Two W-2s → Form 1040 wages → taxable income → Tax Table → line 16.
2. Schedule 3 line 11, the excess Social Security credit. It has a multi-copy collection, grouping by person, a per-employer cap with an exception branch, a parameter that changes each year, and a neighbouring out-of-scope gate (Form 8959).
3. Then Form 8949 → Schedule D lines 1–16 with Exception 1 routing.
4. The Qualified Dividends worksheet last.

If only one worksheet may go first, do it together with the Tax Table. Do not treat success as evidence about the engine.

## Could not verify / weak spots

- **PDFs were unreadable through the fetch tool.** This covers the Mlang paper, the NLLP 2025 paper, the 2026 draft Form 8949 and instructions, and Publication 1167. Mlang ordering and M++ details are recollection (Low).
- **TY2026 form content is unverified.** The $184,500 wage base comes from secondary reports of the SSA announcement; the implied maximum withholding of $11,439.00 is my arithmetic.
- **Schedule 3 line 11 wording** ("any one employer withheld more than…") was not located in the live 2025 text; only older-year wording was seen via secondary sources.
- **Tax Table midpoint method**: secondary sources only.
- **OpenTaxSolver rounding and tax-table behaviour** was not inspected. Tax-Calculator's inner ordering was not seen.
- **UsTaxes Form 8949 details** come from a model summary of the source file, including a claimed page-count rounding bug. Re-check before citing publicly.
- **Fact Graph evaluation strategy and cycle handling** are not in the public spec.
- **DMN and provenance-semiring statements** are from background knowledge.
- **IRS MeF Assurance Testing System scenarios** are a probable source of official worked returns. I did not verify their current availability.
- **Free File Fillable Forms**: whether it enforces whole dollars or limits 8949 rows was not established.

## Open questions

1. Is a refusal ("this return needs Form 8959; out of scope") an acceptable product outcome for the first release, and how many gating conditions is the owner willing to transcribe for forms not computed?
2. Whole-dollar or cents as the default policy? Does the owner's chosen filing channel force one?
3. Is broker import (CSV or PDF 1099-B) in scope, or is manual entry of a handful of sales the slice?
4. Should the engine ask "is the reported basis correct?" at all, or take 1099-B values as given with a prominent caveat?
5. Is the capital loss carryover (a prior-year input) in or out of the first slice?
6. What counts as an "official worked example" for the public suite: IRS publications only, or also IRS e-file test scenarios and VITA training returns?
7. Who is the second transcriber?

## Sources

- IRS, Instructions for Form 8949 (2025): https://www.irs.gov/instructions/i8949
- IRS, Instructions for Form 1040 (2025): https://www.irs.gov/instructions/i1040gi
- IRS, Instructions for Schedule D (2025): https://www.irs.gov/instructions/i1040sd
- IRS, Free File Fillable Forms limitations: https://www.irs.gov/e-file-providers/free-file-fillable-forms-program-limitations-and-available-forms
- IRS draft forms: https://www.irs.gov/draft-tax-forms ; https://www.irs.gov/pub/irs-dft/f8949--dft.pdf (unreadable)
- IRS Publication 1167: https://www.irs.gov/pub/irs-pdf/p1167.pdf (unreadable)
- Fact Graph repository and docs: https://github.com/IRS-Public/fact-graph ; https://github.com/IRS-Public/fact-graph/blob/main/docs/fact-dictionary-specification-3.1.md ; https://github.com/IRS-Public/fact-graph/blob/main/docs/fact-graph-3.1-adr.md
- Direct File repository: https://github.com/IRS-Public/direct-file
- Alex Mark, "Direct File is open source": https://alexthemark.substack.com/p/direct-file-is-open-source
- Direct File not offered in 2026: https://www.cpapracticeadvisor.com/2025/11/05/irs-says-direct-file-wont-be-around-for-2026-filing-season/172448/
- UsTaxes: https://github.com/ustaxes/UsTaxes/blob/master/docs/ARCHITECTURE.md ; https://github.com/ustaxes/UsTaxes/blob/master/src/forms/Y2024/irsForms/F8949.ts
- Tax-Calculator: https://github.com/PSLmodels/Tax-Calculator/blob/master/taxcalc/calculator.py
- OpenTaxSolver: https://opentaxsolver.sourceforge.net/program_structure.html ; https://opentaxsolver.sourceforge.net/download2025.html
- OpenFisca core PR 817: https://github.com/openfisca/openfisca-core/pull/817
- Merigoux, Monat, Protzenko, "A Modern Compiler for the French Tax Code": https://arxiv.org/abs/2011.07966 ; https://blog.merigoux.ovh/en/2019/12/20/taxes-formal-proofs.html
- Merigoux, Chataing, Protzenko, "Catala: A Programming Language for the Law": https://arxiv.org/abs/2103.03198 ; https://ocaml.org/p/catala/latest/doc/Explain/index.html
- Docassemble logic: https://docassemble.org/docs/logic.html
- TaxCalcBench: https://arxiv.org/html/2507.16126v1
- Jurayj, Holzenberger, Van Durme: https://arxiv.org/html/2508.21051v3
- Lorenzo, Pietromatera, Holzenberger, NLLP 2025: https://aclanthology.org/2025.nllp-1.4/
- CUTECat: https://2024.splashcon.org/details/prolala-2024-papers/6/CUTECat-Generating-Testcases-for-Fiscal-Laws-through-Concolic-Execution
- Intuit on the self-employed health insurance and premium tax credit circularity: https://accountants.intuit.com/support/en-us/help-article/review-tax-return/calculation-se-health-insurance-deduction-claiming/L3xcftxAz_US_en_US
- 2026 wage base (secondary): https://www.dlapiper.com/insights/publications/2025/11/irs-announces-2026-retirement-and-benefit-plan-limits-ssa-announces-cola-adjustment
- Tax Table midpoint (secondary): https://ustax.tools/irs-tax-tables-2025/
