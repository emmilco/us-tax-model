# Research report: path forward for an open IRS forms-layer formalization

Synthesis of six workstream files in this directory, researched on 2026-10-13. Each workstream was a web-only agent; nearly every page was read through a summarising fetch tool and no PDF could be opened. Treat specific quotations and figures as needing a check against the original before they are published or built on. Per-claim sources and confidence levels are in the workstream files.

## Recommendation

**Build fresh and small. Do not build on Catala or on Direct File's code.**

1. **Formalization format: forms as data in a closed atom language.** One entry per IRS line. Each entry is one application of an atom from a frozen vocabulary of about a dozen (sum, subtract, subtract-floored-at-zero, smaller-of, larger-of, multiply-by-rate, parameter, table lookup, sum-over-collection, guard, round, copy-from-line, input), plus a mandatory structured citation (document, revision, line). No user-defined functions, no loops, no variables other than lines. Anything that does not fit is a named `opaque` function with its own citation and tests, and the count of those is published.
2. **Arithmetic: integer cents and integer-pair rates.** Rounding is an explicit, cited atom applied where the form says to round. This removes the decimal-library question and can be stated identically in every tool.
3. **Evidence, in the order it actually buys trust:**
   - A renderer that prints each encoded line back as English in IRS worksheet phrasing, to be laid beside the official text. This is the main defence against the dominant risk, which is mistranscription.
   - Static checks on the data: every reference resolves, the line graph is acyclic, units type-check, every line has a citation, guards are exhaustive and disjoint.
   - Atom properties proved once in Lean 4 over integers (non-negativity of floored subtraction, correctness and idempotence of half-up rounding, per-atom monotonicity with sign tracking), with a Lean reference evaluator reading the same data files and compared against the shipping engine in CI.
   - Tests: official examples where they exist, hand-worked branch-covering cases, differential runs against independent calculators, and a published mutation score per worksheet.
4. **Engine: a lazy, memoized evaluator over the line-level graph** that returns each value with its derivation tree, with three-valued completeness (unknown, placeholder, known). No fixed-point machinery; the slice has no true cycles. Shipping implementation in TypeScript so it runs in a browser or as a CLI with nothing to install.
5. **Interview: derive what must be asked, hand-author the order.** The needed inputs are the backward slice from the target lines under current answers. Out-of-scope detectors are ordinary cited gating facts whose result is a refusal. Answers are an append-only log recomputed from scratch.
6. **Output: a line-by-line values sheet first, a filled official IRS PDF second.** Never render look-alike forms, never produce e-file XML.
7. **Development year: TY2025 final forms and instructions now**, with parameters separated per year and every citation pinned to a revision. Re-diff to TY2026 when its instructions appear.

What to borrow and not adopt: the Fact Graph's completeness model and its operator list as a cross-check on the atom vocabulary; Catala's literate layout and per-run traces; py1040's one-cell-per-line shape.

## Why this and not the alternatives

- **Catala** (v1.3.0, Apache-2.0, actively released) is the runner-up. Its distinguishing machinery is prioritized default logic for statute text. A worksheet is already a linear order of steps with the exceptions resolved by the IRS, so that machinery has little to do, and Catala's idiom of out-of-order definitions works against line-against-line comparison. Its US coverage is two Code sections. It gives nothing toward the atoms goal.
- **Direct File / Fact Graph.** The Direct File repository is archived. Its TY2024 fact dictionary shows no dividends, capital gains, Schedule D or Form 8949 content, so reuse would mean inheriting a Scala engine and XML format without any of the slice's tax content. The Fact Graph engine itself is live and CC0, but its own design record calls the XML verbose and lists engine complexity as a risk, and its spec has no structured citations and no explanation trace.
- **Lean 4 for everything.** Best for proofs, worst for lay legibility and contributors, and its browser target is second-tier. Use it for what it is good at.
- **Plain typed code in any language.** Buries the dependency graph and makes traces, citations and year diffs bolt-ons.

## Findings that cut against the plan as briefed

1. **Official worked examples are too scarce to be the first tests.** The source-material pass found no filled-in Qualified Dividends and Capital Gain Tax Worksheet and no whole-return example matching the slice in the 2025 Form 1040 instructions, Schedule D instructions, or the parts of Publication 550 it read; Publication 17 has dropped the relevant chapters. It estimates 40 to 60 official numeric examples relevant to the slice, nearly all single-rule (an 8949 row, a wash sale, a holding period). Unread and possibly better: VITA Publications 4491 and 6744, and the IRS e-file test scenarios. Design principle 2 survives as "every official example is a test", but it cannot carry the worksheet arithmetic. This weakens the public-verifiability claim more than any other finding.
2. **The slice is larger than the form list in the brief.** Excess Social Security withholding implies one person's combined wages above $184,500 for 2026. That means taxable income over $100,000, so the Tax Computation Worksheet and not the Tax Table; and it sits close to the unindexed $200,000 single-filer threshold for Additional Medicare Tax (Form 8959, Schedule 2) and Net Investment Income Tax (Form 8960). A 1099-DIV can also force the Schedule D Tax Worksheet (boxes 2b to 2d), a foreign tax credit decision (box 7) and Form 8995 (box 5). Each must be either implemented or refused with a cited gate.
3. **"Faithful transcription is mostly mechanical" is true of worksheet arithmetic and little else.** The hard content is routing prose, per-sale classification on Form 8949 (twelve boxes as of 2025), conditions quantified over all transactions, rounding conventions, and judgment facts such as whether broker-reported basis is right.
4. **The Qualified Dividends worksheet is a weak architecture test.** It has no collections, no exceptions and one routing condition. The excess Social Security credit and the Form 8949 to Schedule D flow exercise far more of the design.
5. **The novelty is narrower than the brief assumes.** A Stanford preprint from 2 October 2026 (arXiv 2610.02792) formalizes IRS forms and instructions in Lean 4, one function per cell, for 2024 and 2025; it uses floats, its evidence is test agreement against other software, and its code is unreleased. OpenTax (September 2026, AGPL with a reservation) is a TY2025 node-graph engine that claims IRS-publication-sourced tests. What still appears unpublished is the combination of a small atom vocabulary with proved properties, structured provenance on every line, and a lay-readable rendering.
6. **Machine-readable official structure is not available.** IRS e-file schemas and business rules go only to registered software developers through a restricted mailbox. The HTML instructions, which include worksheets as tables, are the best source. Current-year IRS URLs change content silently when a new year is released, so sources must be snapshotted and hashed.
7. **"The user files it themselves" is not what keeps the project outside the preparer rules.** On the legal pass's reading, the absence of compensation is. An interview that decides which forms apply is not "mechanical assistance", and the section 7216 regulation names software developers regardless of fee. A locally run, free tool that sends nothing back has little exposure; a hosted version, telemetry, a paid tier, or possibly a donation button changes that. The holding of Rev. Rul. 85-189, the key authority, was not read in full.

## Follow-up check on test material (local PDF pass, 2026-10-13)

Done in the main session by downloading the PDFs and extracting text, with four pages viewed as images. It tightens finding 1.

- **IRS e-file test scenarios (TY2025) look like inputs, not answers.** Of the nine Form 1040 scenarios, only Scenario 3 lists Schedule D. On the four pages viewed (Form 1040 pages 1 and 2, Schedule D pages 1 and 2), the given entries are filled in (Schedule D line 1a proceeds 14,222 and cost 12,234; line 8a proceeds 14,211 and cost 4,486; lines 18 and 19 zero; the line 17 and line 20 boxes ticked) and every computed line is blank, including Schedule D lines 7, 15 and 16 and all Form 1040 amounts. That is one scenario and four pages, so it suggests, and does not establish, that these scenarios leave computed values for the software to produce. None of the nine lists Form 8949.
- **VITA materials contain no worked Qualified Dividends worksheet.** The worksheet's name does not occur in the extracted text of Publication 4491 (356 pages), Publication 4012 (408 pages) or Form 6744 (210 pages), and neither does "Schedule D Tax Worksheet".
- **Form 6744 does give a few single-line answers.** It is the volunteer test, with questions and an answer key, for example a net short-term capital gain of $400 on Schedule D. These are usable as single-line oracles once the scenario inputs are transcribed; how many touch the slice was not counted.

Consequence: no official source found so far supplies expected values for the Qualified Dividends worksheet or for a whole return in the slice. The worksheet arithmetic will rest on hand-worked branch-covering cases, differential runs and mutation scores, with official examples covering single rules only.

## Top risks

1. **Unsound scope gating.** A confident, well-cited, wrong return because an unsupported form was not detected.
2. **Thin oracles.** One or two independent checks per worksheet line, fewer on rare branches; open calculators are weakest on Form 8949; none yet covers TY2026.
3. **Form 8949 inputs.** Broker data, adjustments, and facts no tool can verify.
4. **Yearly churn for one maintainer.** 2025 added a schedule, a 1040 line and six 8949 boxes; the 2026 draft 1040 renumbers lines again.
5. **Atom-language growth.** The Fact Graph's operator list already includes payroll-month and date verbs.

## Unresolved between workstreams

- PolicyEngine-US version is reported as 1.824.7 in one file and 2.41.4 in another. It affects nothing here.
- Whether proofs should arrive with the first slice or after it. The tooling pass says after; the owner's stated weight on structural evidence argues for at least fixing the atom semantics in Lean alongside the first worksheet.
- TypeScript as host is the tooling pass's pick on browser delivery and contributor reach. Nothing in the evidence makes it clearly better than Python for a locally run tool.

## Open items needing a pass that can read PDFs

- A count of Form 6744 questions whose answers are slice lines, and a look at the remaining e-file scenarios' computed lines.
- The 2026 draft forms, and the 2026 instructions when drafted.
- The real field structure of the fillable PDFs across years.
- Rev. Rul. 85-187 to 85-189 and Publication 1167 in full.

## Sources

Detailed findings, with per-claim URLs and confidence:

- `01_prior_art_formalization.md`
- `02_prior_art_tax_software.md`
- `03_source_material.md`
- `04_legal_liability.md`
- `05_tooling_language.md`
- `06_architecture.md`

Sources carrying the most weight in this synthesis:

- IRS, Instructions for Form 1040, Schedule D and Form 8949 (2025): https://www.irs.gov/instructions/i1040gi, https://www.irs.gov/instructions/i1040sd, https://www.irs.gov/instructions/i8949
- IRS, Instructions for Forms 8959 and 8960: https://www.irs.gov/instructions/i8959, https://www.irs.gov/instructions/i8960
- Rev. Proc. 2025-32 (2026 inflation adjustments): https://www.irs.gov/irb/2025-45_IRB
- Rev. Proc. 2025-27 (substitute forms): https://www.irs.gov/irb/2025-44_IRB
- IRS draft forms listing: https://www.irs.gov/draft-tax-forms
- IRS e-file schema distribution policy: https://www.irs.gov/e-file-providers/modernized-e-file-mef-schemas-and-business-rules
- IRS Free File Fillable Forms limitations: https://www.irs.gov/e-file-providers/free-file-fillable-forms-program-limitations-and-available-forms
- IRS Direct File (archived) and Fact Graph: https://github.com/IRS-Public/direct-file, https://github.com/IRS-Public/fact-graph
- Catala: https://github.com/CatalaLang/catala, https://arxiv.org/abs/2103.03198
- Law and Order: Tax Law Autoformalization: https://arxiv.org/html/2610.02792
- TaxCalcBench: https://arxiv.org/html/2507.16126v1
- Lawsky, Tax Law and Flexible Formalizations: https://lawreview.uchicago.edu/online-archive/tax-law-and-flexible-formalizations
- OpenTax, UsTaxes, OpenTaxSolver: https://github.com/filedcom/opentax, https://github.com/ustaxes/UsTaxes, https://opentaxsolver.sourceforge.net/
- IRC 7701(a)(36) and Reg. 301.7216-1: https://www.law.cornell.edu/uscode/text/26/7701, https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol20/xml/CFR-2025-title26-vol20-sec301-7216-1.xml
- Lean platform support: https://lean-lang.org/doc/reference/latest/platforms/
