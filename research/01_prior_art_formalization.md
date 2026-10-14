# Prior art: formalizations of tax law

## Summary

- **The closest prior art is a paper posted eleven days ago, and it is not Catala.** "Law and Order: Tax Law Autoformalization" (arXiv 2610.02792, 2 Oct 2026, Stanford) formalizes IRS *forms and instructions* in Lean 4, one function per form cell. Its correctness evidence is test agreement, not proof; it uses `Float`; code is not yet released.
- **Nobody has published what the owner wants for structural evidence.** I found no work that fixes a small primitive vocabulary for tax arithmetic and proves monotonicity, bounds or non-negativity of those primitives. The Mlang Coq development proves only "well-formed programs do not get stuck", and its `Round` is an identity stub marked FIXME.
- **The IRS has already published a de facto atom vocabulary.** The Direct File Fact Graph (CC0, last push 2026-09-01) has operator nodes named `Add`, `Subtract`, `Multiply`, `GreaterOf`, `LesserOf`, `Round`, `Floor`, `Ceiling`, `TruncateCents`, `StepwiseMultiply`, `Switch`, `CollectionSum`. No proofs accompany them.
- **Catala is alive and stable, but aimed at a different problem.** Version 1.3.0 was released 2026-10-01 (Apache-2.0). Its distinctive machinery (prioritized defaults, out-of-order definitions, conflict/empty errors) solves statute structure that a worksheet has already linearised away.
- **Catala's US federal coverage is two sections.** IRC §121 and §132 only. Nothing in it reaches a Form 1040 line.
- **Lawsky's own position cuts both ways.** She argues forms *are* a formalization (supporting the project's premise), but calls them a "rigid" one, says they are not law, and notes they can embed unannounced agency judgments.
- **LLM autoformalization results are test-relative and model-dependent.** Where a proof attempt was made (50 cells), 7 failed, and one failure was in the human "gold" implementation.
- **SARA is poor test material for this project.** Its statutes are hand-edited and simplified, so its numeric answers are not real-form answers. TaxCalcBench (MIT, 51 CPA-written returns) is a better external check.
- **Reuse is licence-constrained.** Mlang is GPL-3, OpenFisca and PolicyEngine-US are AGPL-3, Catala is Apache-2.0, Fact Graph is CC0, TaxCalcBench is MIT.

## Findings

### 1. Catala

- **Maturity.** Releases seen via the GitHub API: 1.0.0 (2025-11-10), 1.1.0 (2026-01-29), 1.2.0 (2026-06-02), 1.2.1 (2026-07-06), 1.3.0 (2026-10-01). Latest commit 2026-10-01 by Vincent Botbol (Inria). About 5,730 commits, Apache-2.0. The README still says "The compiler is yet unstable and lacks some of its features", which sits oddly with a 1.x version number. https://github.com/CatalaLang/catala and https://api.github.com/repos/CatalaLang/catala/releases. Confidence: High. Primary.
- **Semantics.** The core is a prioritized default calculus: a default has exceptions, a justification and a consequence. Two simultaneously valid exceptions raise a conflict error; no applicable rule yields an empty error. Definitions may be written out of order and the compiler computes the dependency order. The language is deliberately not Turing-complete. https://ar5iv.labs.arxiv.org/html/2103.03198. Confidence: High. Primary (first 100k characters of the ICFP 2021 paper).
- **Proofs.** One compilation step (default calculus to lambda calculus) was proved correct in F*, about 3,500 lines; the scope-to-default step is unproved, and the extracted F* code is not what the compiler runs. Same source. Confidence: High. Primary. This is compiler assurance, not assurance about any encoded law.
- **Verification tooling.** A `catala.verification` module encodes the default calculus into Z3 and generates conditions for absence of empty and conflict errors; it appears in package docs up to 1.1.0. https://ocaml.org/p/catala/1.1.0/src/catala.verification/solver.ml.html. Confidence: Medium. Secondary (search summary of package docs); I did not confirm it in 1.3.0.
- **Money and decimals.** Money is an integer number of cents (Zarith `Z.t`); decimals are exact rationals (`Q.t`); rounding is half away from zero. Decimal-to-money conversion truncated in 0.7.0 and rounded in 0.9.0, so behaviour has changed across releases. https://ocaml.org/p/catala/1.1.0/catala.runtime_ocaml/Catala_runtime/index.html. Confidence: Medium. Secondary.
- **Backends and tooling.** 1.3.0 notes mention Java, Python, OCaml and C targets, the `clerk` build tool, and JSON execution traces (not yet for C). https://github.com/CatalaLang/catala/releases. Confidence: High. Primary.
- **US encodings.** `us_tax_code/` contains `section_121.catala_en` and `section_132.catala_en` only. https://github.com/CatalaLang/catala-examples/tree/master/us_tax_code. Confidence: High. Primary. Repo last pushed 2026-09-25, Apache-2.0.
- **French scale.** The housing-benefits encoding is 19,655 lines including the legal text, per the CUTECat paper; the examples README calls it the largest so far. https://arxiv.org/html/2410.18212v2. Confidence: Medium (one source for the figure).

**Where Catala fits badly for worksheets.**
1. A worksheet is already a total order of steps with exceptions resolved by the IRS. Default logic has nothing to resolve; every definition would be unconditional.
2. Out-of-order definitions are idiomatic in Catala. The project's forensic claim depends on the code having the *same* order as the worksheet.
3. The literate unit is a statute paragraph. A worksheet's unit is a numbered line; "line 7 = smaller of line 5 or line 6" gains nothing from scopes and context variables.
4. IRS whole-dollar rounding of individual lines would need to be imposed on top of a cents-based money type.
5. Conflict and empty errors, Catala's main safety story, cannot arise in a straight-line worksheet, so the Z3 checks would be vacuous.
6. A lay reader must learn Catala syntax before comparing code with the form.

What Catala does offer and is worth copying: the literate layout, exact-rational arithmetic, and per-run JSON traces.

### 2. Sarah Lawsky

- **"A Logic for Statutes"** (21 Fla. Tax Rev., 2018) argues statutory reasoning is defeasible and default logic models it best, using §163(h). https://scholarship.law.ufl.edu/ftr/vol21/iss1/2/. Confidence: Medium. Secondary (search summary).
- **"Formalizing the Code"** (70 Tax L. Rev. 377, 2017) argues for formal logic in drafting, focused on definitional scope and cross-references. Confidence: Low to Medium. Secondary only.
- **"Form as Formalization"** (16 Ohio St. Tech. L.J. 114, 2020). The abstract says large parts of the Code are already formalized because forms formalize it; tax software encodes the forms, not the law; and the way form entries interact "may contain judgements about the law". https://experts.illinois.edu/en/publications/form-as-formalization/. Confidence: High for the abstract. Primary abstract; full text not read.
- **"Coding the Code"** (75 SMU L. Rev. 535, 2022). Per Grimmelmann's review: default logic is not more powerful than standard logic but tracks how lawyers read statutes; pair and literate programming help others *check* a translation rather than making it correct. https://cyber.jotwell.com/?p=2670. Confidence: Medium. Secondary; the PDF was unreadable through my tool.
- **"Tax Law and Flexible Formalizations"** (91 U. Chi. L. Rev. Online, 18 Nov 2024). She distinguishes *rigid* formalizations, built for one purpose, with IRS forms as the example, from *flexible* ones that are machine-executable and formally verifiable. She notes agencies sometimes resolve ambiguities or errors inside forms without announcing it. She does not claim formalization removes intended ambiguity or simplifies law. https://lawreview.uchicago.edu/online-archive/tax-law-and-flexible-formalizations. Confidence: High. Primary (HTML read).
- **"Reasoning with Formalized Statutes: The Case of Capital Gains and Losses"** (43 Va. Tax Rev. 361, 2024) exists and is squarely on the first slice's subject. I could not reach its text. Confidence: High that it exists; contents unverified.
- She gave a January 2026 talk titled "Computational Law, Transparency, and Accountability: The Case of Direct File". https://ischool.illinois.edu/news-events/events/2026/01/28/ai-disruption-speaker-series-sarah-lawsky. Confidence: Medium. Listing only.

### 3. LLM autoformalization

- **Law and Order** (Han, Takashima, Wei, Li, Genesereth). Targets IRS forms and instructions plus some state forms (26 listed in the appendix, 30 claimed in the conclusion), tax years 2024 and 2025, over 10,000 lines of Lean 4. Pipeline: regex extraction of cells from PDFs, one function per cell, cell-level comparison against OpenTaxSolver outputs, localized LLM repair for up to 20 rounds. Held-out test: 51 TaxCalcBench returns. Reported strict return-level accuracy for TY2025 ranges from 0% (small open model) to 100%, and for one model plain self-debugging beat the paper's method. Branch coverage was 44% on the repair set and 73% on the test set. A separate experiment tried to prove 50 sampled cells equivalent to gold implementations: 43 proved, 7 counterexamples, one of which was a gold error. Helpers seen in generated code: `notLessThanZero`, `smallerOf`, `largerOf`. Numbers are `Float`, and the repair prompt carries rounding special-cases. https://arxiv.org/html/2610.02792. Confidence: High that the paper says this; Low that the results generalise (11-day-old preprint, no released code, and the oracle is another piece of software).
- **Synedrion** (ICSE 2026, arXiv 2509.13471). Multi-agent generation of Python from IRS publications for TY2021, checked by higher-order metamorphic testing against a hand-written oracle the authors admit "may contain logical bugs". Typical failure: applying the top bracket rate to all income. https://arxiv.org/html/2509.13471v1. Confidence: High. Primary.
- **Statutory inconsistency in §121** (Yadamsuren, Platt, Diaz, arXiv 2511.11954; later in *Artificial Intelligence and Law*). LLM-drafted Prolog; a direct GPT-4o baseline found the inconsistency in one of three strategies. One section, tiny sample. https://arxiv.org/abs/2511.11954v1. Confidence: Medium. Abstract only.
- **Translating Tax Law to Code with LLMs** (Lorenzo, Pietromatera, Holzenberger, NLLP 2025): a Catala generation benchmark. A later paper attributes to it 88.8% *syntactically valid* output, which measures parsing rather than correctness. https://aclanthology.org/2025.nllp-1.4/. Confidence: Low for the figure (single secondary source).
- **Language Models and Logic Programs for Trustworthy Tax Reasoning** (AAAI 2026, arXiv 2508.21051): LLM to Prolog on SARA, treating failed executions as refusals. https://arxiv.org/abs/2508.21051. Confidence: Medium. Abstract only.
- **TaxCalcBench** (Column Tax, arXiv 2507.16126): frontier models computed under a third of returns correctly; errors centred on tax-table misuse. Repo MIT, pushed 2026-10-13. https://arxiv.org/abs/2507.16126v1, https://github.com/column-tax/tax-calc-bench. Confidence: Medium (accuracy from search summary; licence from API).

### 4. CUTECat and test generation

- Concolic execution for Catala using Z3; 3,400 lines of OCaml. On French housing benefits it generated 186,390 tests in under 7 CPU-hours; also run on §132. It detects conflicts, missing cases and division by zero. It found a rounding discrepancy between Catala's Python backend and its interpreter. Money is modelled in cents, decimals as rationals. Lists and date arithmetic are only partly symbolic. https://arxiv.org/html/2410.18212v2. Confidence: High. Primary (first 100k characters). Repo and licence not seen.

### 5. SARA

- 376 hand-written cases over nine IRC sections that were "heavily edited by hand to be much shorter and remove ambiguity"; includes entailment and numeric cases plus a Prolog encoding. https://nlp.jhu.edu/law/sara. Confidence: Medium (structure primary; size and editing from a search summary of a 2023 Tax Notes piece). Licence not found. Not usable as an oracle for real forms.

### 6. Other efforts

- **Mlang / M** (Merigoux, Monat, Protzenko, CC 2021). Reverse-engineered compiler for the DGFiP's 1990 M language. README: GPL-3, Inria copyright; passed "all the private DGFiP tests as of Sept. 2022" for 2018 to 2021 income; that test base is unpublished; "no legal guarantee of any kind"; default arithmetic is IEEE doubles because the DGFiP uses them, with MPFR and fixed-point options. Last commit 2026-01-16. https://raw.githubusercontent.com/MLanguage/mlang/master/README.md. Confidence: High. Primary. The abstract's "officially transitioning to Mlang" claim is not repeated in the README.
- **Direct File and Fact Graph.** `IRS-Public/direct-file` is archived and "no longer maintained"; it describes TY2024 logic. `IRS-Public/fact-graph` is a separate, live library (CC0, 70 commits, pushed 2026-09-01) with XML fact dictionaries of writable and derived facts. https://github.com/IRS-Public/fact-graph. Confidence: High. Primary. It models facts and derivations, not form lines.
- **OpenFisca-core**: AGPL-3, pushed 2026-10-13. **PolicyEngine-US**: AGPL-3, pushed 2026-10-14 UTC. Both are vectorised microsimulation models of policy, not line-by-line forms. Confidence: High for status. Primary (API).
- **Blawx**: MIT, last push 2024-11-01; looks stalled. https://api.github.com/repos/Lexpedite/blawx. Confidence: High.
- **L4**: `legalese/l4-ide` pushed 2026-10-14 UTC; licence not asserted by GitHub. Confidence: Medium.
- **Logical English, DMN**: not investigated beyond one search. Confidence: Low.

### 7. Functional atoms with proved properties

- **Mlang Coq semantics** (`formal_semantics/semantics.v`, Coq 8.12). Values are IEEE doubles or `Undef`. Unary built-ins: `Round`, `Inf`, `Abs`, `Gtzero`, `Gtezero`, `Null`, `Present`. Binary: `And`, `Or`, `Lt`, `Eq`, `Add`, `Sub`, `Mul`, `Div`, `Min`, `Max`. Division by zero returns zero. Proved, with no `Admitted`: `soundness_expr`, `soundness_cmd`, `soundness_prog`, meaning well-formed programs evaluate without error. `Round` and `Inf` are identity functions flagged FIXME. No monotonicity, bounds or non-negativity theorems. https://raw.githubusercontent.com/MLanguage/mlang/master/formal_semantics/semantics.v. Confidence: Medium to High. Primary file, but read through a summarising model.
- **Verifisc** (Merigoux, 2019). Z3 encoding of French tax and benefit rules used to *search for* a household whose net income falls after a raise. It found one. No universal property was proved; queries used over 100 GB of RAM and ran for days. https://blog.merigoux.ovh/en/2019/12/20/taxes-formal-proofs.html. Confidence: Medium. Author's blog.
- **Fact Graph operators** as listed in section 6 and the summary. https://github.com/IRS-Public/fact-graph/tree/main/shared/src/main/scala/gov/irs/factgraph/compnodes. Confidence: High that the files exist; their semantics were not read.

## Implications for this project

- The gap is real: forms-layer formalization with an explicit atom algebra and machine-checked atom properties appears unpublished. That is a finding about my search, not proof of absence.
- Lean 4 has one precedent for exactly this target. Catala does not.
- The atom vocabulary should be cross-checked against the Fact Graph and M built-in lists rather than invented from scratch. Mlang shows how unusual semantics creep in (division by zero equals zero; undefined is not zero).
- Rounding is where prior art is weakest: stubbed in Mlang's proof, patched by prompt in Law and Order, changed between Catala versions, and the source of CUTECat's one reported bug. A provably specified rounding atom would be novel and is the highest-risk primitive.
- Exact integers or rationals are the defensible choice; both Mlang and Law and Order use floats and inherit tolerance fudge.
- Lawsky supplies the honest framing for lay users: this formalizes the IRS's algorithm, which is not the law and may contain unannounced judgments.
- Proof attempts found errors in human reference code. Test agreement with another program is weak evidence; IRS worked examples are a stronger oracle.

## Could not verify / weak spots

- The Mlang CC 2021 paper body (HAL blocked, PDF unreadable, ar5iv conversion failed). Size of the French tax code in M and the DGFiP test count are therefore not reported.
- Full texts of Lawsky's "Formalizing the Code", "Coding the Code", "Form as Formalization" and the capital-gains article.
- Whether any French agency runs Catala in production; the catala-lang.org page returned no body.
- Whether Catala 1.3.0 still ships the Z3 proof backend.
- SARA licence and v2 differences; the NLLP 2025 metrics; Logical English and DMN.
- All pages were read through a summarising model, so fine detail (especially the Coq theorem statements and Law and Order's table figures) may be distorted. Model names in that paper ("GPT-6", "Opus 5.5") are reported as given.
- My Catala-fit critique is reasoning from its design, not from an attempted worksheet encoding.

## Open questions

1. Does Lawsky's capital-gains paper identify points where Schedule D or the Qualified Dividends worksheet diverges from §1(h)?
2. Will Law and Order's Lean code be released, and under what licence?
3. What exactly do Fact Graph's `Round`, `TruncateCents` and `StepwiseMultiply` compute, and do they match IRS form rounding instructions?
4. Is there any published proof of monotonicity for a bracket-schedule function in any proof assistant?
5. Would the Catala team regard a worksheet-transcription mode as in scope?

## Sources

- https://github.com/CatalaLang/catala : Catala repository, licence, README status
- https://api.github.com/repos/CatalaLang/catala/releases : release dates
- https://github.com/CatalaLang/catala-examples/tree/master/us_tax_code : US encodings
- https://ar5iv.labs.arxiv.org/html/2103.03198 : Catala ICFP 2021 paper
- https://ocaml.org/p/catala/1.1.0/src/catala.verification/solver.ml.html : Catala Z3 backend docs
- https://ocaml.org/p/catala/1.1.0/catala.runtime_ocaml/Catala_runtime/index.html : Catala runtime money and rounding
- https://arxiv.org/html/2410.18212v2 : CUTECat
- https://arxiv.org/abs/2011.07966v3 : Mlang paper abstract
- https://raw.githubusercontent.com/MLanguage/mlang/master/README.md : Mlang README
- https://raw.githubusercontent.com/MLanguage/mlang/master/formal_semantics/semantics.v : Mlang Coq semantics
- https://blog.merigoux.ovh/en/2019/12/20/taxes-formal-proofs.html : Verifisc and Z3 queries
- https://lawreview.uchicago.edu/online-archive/tax-law-and-flexible-formalizations : Lawsky 2024
- https://experts.illinois.edu/en/publications/form-as-formalization/ : Lawsky 2020 abstract
- https://scholar.smu.edu/smulr/vol75/iss3/4 : Lawsky 2022 landing page
- https://cyber.jotwell.com/?p=2670 : Grimmelmann review of Lawsky
- https://scholarship.law.ufl.edu/ftr/vol21/iss1/2/ : "A Logic for Statutes"
- https://arxiv.org/html/2610.02792 : Law and Order: Tax Law Autoformalization
- https://arxiv.org/html/2509.13471v1 : Synedrion
- https://arxiv.org/abs/2511.11954v1 : §121 inconsistency detection
- https://aclanthology.org/2025.nllp-1.4/ : Catala generation benchmark
- https://arxiv.org/abs/2508.21051 : LLM plus Prolog on SARA
- https://arxiv.org/abs/2507.16126v1 : TaxCalcBench paper
- https://github.com/column-tax/tax-calc-bench : TaxCalcBench data
- https://nlp.jhu.edu/law/sara : SARA dataset
- https://github.com/IRS-Public/fact-graph : IRS Fact Graph
- https://github.com/IRS-Public/fact-graph/blob/main/LICENSE.md : Fact Graph licence
- https://github.com/IRS-Public/direct-file : archived Direct File source
- https://api.github.com/repos/openfisca/openfisca-core : OpenFisca status
- https://api.github.com/repos/PolicyEngine/policyengine-us : PolicyEngine-US status
- https://api.github.com/repos/Lexpedite/blawx : Blawx status
- https://api.github.com/repos/legalese/l4-ide : L4 status
