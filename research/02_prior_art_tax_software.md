# Prior art: tax software and computational tax models

Research date: 2026-10-13. Web sources only. "Read directly" means I fetched the primary page; all page reads were mediated by a summarising fetch tool, so verbatim wording is not guaranteed.

## Summary

- **No existing open project does all of what the owner describes** (citation on every value, literal line-by-line worksheet transcription, official IRS worked examples as the public test suite). Several do one or two parts. The closest overlap is **OpenTax** (filedcom/opentax), first seen September 2026, which uses IRS Pub 4491 / Pub 17 / MeF scenarios as a public benchmark, but it is TY2025, AI-agent-maintained, and AGPL with a reserved MeF clause.
- **Direct File is dead; the Fact Graph is not.** The `IRS-Public/direct-file` repo is archived (last commit 2026-06-11, a README update). The Fact Graph was split into `IRS-Public/fact-graph`, which is CC0, unarchived, and had commits through 2026-09-01. It powers the IRS Tax Withholding Estimator 2.0.
- **Direct File never covered the proposed slice.** TY2024 scope excluded dividends and capital gains. The released fact dictionary has no Schedule D, Form 8949, 1099-DIV, 1099-B or Qualified Dividends and Capital Gain Tax Worksheet module, and apparently no Schedule 3 line 11 (excess Social Security). Reusing it means inheriting the engine, not the tax content.
- **I could not reach an IRS.gov statement of the discontinuation.** The claim rests on news reports of an IRS email, a Treasury report I could not open, and my own observations that the Direct File pages are gone.
- **UsTaxes is the nearest functional match to the slice** (W-2, 1099-INT/DIV/B, Schedules B and D, Form 8949, Schedule 3 excess FICA, TY2020–2025, AGPL-3.0). It is imperative TypeScript per form per year, and I found no citations in its architecture doc.
- **Free File Fillable Forms is a viable e-file path.** It has no income limit, e-files for free, and lists Form 1040, Schedules B, D and 3, and Form 8949 as available. The current season closes 2026-10-15; nothing is announced yet for the TY2026 season.
- **Line-level oracles for TY2026 do not exist yet.** OpenTaxSolver, UsTaxes and OpenTax are at TY2025. Only the excel1040 "2026 Forecast" spreadsheet (in progress) and the policy microsimulation models reach 2026, and the latter give totals, not form lines.
- **Rules-as-data works but is expensive.** The Fact Graph team itself calls its XML verbose and tedious, and lists engine complexity as a risk.

## Findings

### Comparison table

| Project | Scope | Rule representation | Licence | Last activity seen | Reuse potential |
|---|---|---|---|---|---|
| IRS Direct File | TY2024; W-2, SSA-1099, 1099-G, 1099-INT, some 1099-R; no dividends or capital gains | XML fact dictionary + React flow | CC0 | Archived; 2026-06-11 | Reference only |
| IRS Fact Graph | Engine only, no tax content | Scala engine, XML facts | CC0 | 2026-09-01 | Moderate (engine) |
| IRS Form Builder / Withholding Estimator | W-4 estimation, not returns | Flow XML + fact XML + YAML locale | CC0 | Org listing 2026-10-06 / 2026-08-20 | Pattern for interview layer |
| OpenTax | TY2025 Form 1040, many schedules | TypeScript node graph, Zod schemas | AGPL-3.0 + commercial | 2026-10-12 | Competitor; oracle for TY2025 |
| UsTaxes | TY2020–2025; covers the slice | TypeScript class per form per year | AGPL-3.0 | 2026-10-13 (dependabot) | Oracle; not a base |
| OpenTaxSolver | TY2025 (v23.07); 1040, Schedules 1–3, A–D, 8949, 6251 and more; 11 states | C programs, text input files | GPL-2.0 | 2026-09-25 | Oracle |
| tenforty | 2018–2025; wraps OpenTaxSolver, plus a Rust graph backend | C via Python; Rust graph | MIT | 2026-10-08 | Oracle (not independent of OTS) |
| HabuTax | TY2023; 1040, Schedules 1, 3 (Part I), A, B; no Schedule D | Python field-level dependencies + solver | GPL-2.0 | 2024-02-24 | Design reference; stale |
| py1040 | Form 1040; years not stated | Dictionary of cells, one per form line | GPL-2.0 | Date not seen | Design reference |
| excel1040 | 1996–2025; 2026 forecast in progress | Excel formulas mirroring forms | Free, copyrighted | Site dated 2026-10-09 | Human-checkable oracle |
| PolicyEngine-US | Federal and state tax-benefit rules, multi-year | Python variables + parameter files | AGPL-3.0 | v2.41.4, 2026-10-13 | Totals oracle only |
| PSL Tax-Calculator | Federal income and payroll tax microsimulation | Python functions + parameter files | CC0 (badge) | v6.8.4, 2026-10-01 | Totals oracle only |
| NBER TAXSIM | Federal 1960–2023 (v35); test version through 2024 | FORTRAN, closed | Not stated | v35 page dated 2022-05-20 | Not usable for TY2026 |

### 1. IRS Direct File and the Fact Graph

**Discontinuation.** News outlets (November 2025) report an IRS email to states saying Direct File "will not be available in Filing Season 2026" with no future launch date. Confidence: Medium, secondary only. A Treasury "Report on the Replacement of Direct File", dated 2025-10-02, exists at home.treasury.gov, but the PDF failed to load twice; its content (about $41M cost, $138 per return) is from secondary summaries. Direct observations: `directfile.irs.gov` does not resolve, `irs.gov/filing/irs-direct-file-for-free` returns 404, and the IRS March 2026 Free File tax tip does not mention Direct File. The owner's claim is very probably true, but not verified against an IRS.gov statement.

**Code release.** Verified, High confidence, read directly. https://github.com/IRS-Public/direct-file has three commits: 2025-05-27, 2025-06-05 and 2026-06-11. The README says the repo is archived, unmaintained, and not for production use. It also says some code was withheld (PII, FTI, SBU, national security) and some functionality removed or rewritten. A fork author says the MeF submission code and the SADI/ID.me authentication were removed (secondary, HN thread).

**Licence.** CC0 1.0 plus US-government public-domain status, for both `direct-file` and `fact-graph`. High confidence; read the LICENSE files directly.

**Scope.** The README says the logic is for Tax Year 2024 and was developed with IRS Chief Counsel. A Treasury flyer lists capital gains and dividends as out of scope (secondary search summary, Medium). The fact dictionary directory (read directly) has 36 XML modules, including `interest.xml`, `formW2s.xml`, `schedule3.xml` and `taxCalculations.xml`, and none for dividends, capital gains, Schedule D or Form 8949. `taxCalculations.xml` computes tax by rounding to the tax-table row midpoint and applying bracket formulas; it has no qualified-dividends worksheet. `schedule3.xml` showed no line 11 fact. Confidence: High on the file list; Medium on file contents (tool summaries, possibly truncated).

**What the Fact Graph is.** High confidence on the outline, read directly from the README, the 3.1 ADR and `Tax-Logic.md`:
- A declarative knowledge graph in Scala, running on the JVM and in the browser via Scala.js.
- Facts are declared in XML with slash paths (`/filers/*/firstName`). Each is either Writable (user input) or Derived (an expression tree of operators such as `Add`, `Switch`, `Round`, `GreaterOf` over `<Dependency>` references).
- Collections use `*` wildcards with UUID items; aliases and relative paths (`../x`) reach sibling facts.
- Completeness is first-class: a fact is complete when it has a valid value, placeholders give defaults without marking completeness, and incomplete facts export blank.
- Facts carry `<Name>` and `<Description>`; descriptions cite form lines (for example "line 13 of Form 1040"), and one cites the Rev. Proc. rate tables. Citation is free text, not structured provenance.
- The interview flow is separate: React `<Screen>` components in categories and subcategories, with conditions that reference facts, knockout screens, and "dataview" summary pages.
- Tests are a few hundred "scenarios" (complete fact-graph JSON files), flow snapshots, and completeness tests. I saw no mention of comparison against IRS worked examples.

**Continuation inside the IRS.** `IRS-Public/fact-graph` (421 stars, 70 commits, latest 2026-09-01) describes itself as production-ready, developed in a private repo and mirrored. It added a "Fact Dictionary 3.1 informal specification" on 2026-05-13. `tax-withholding-estimator` (857 commits) says TWE 2.0 went live on 2026-02-27. `form-builder` generates a static multi-language questionnaire site from flow XML, fact XML and YAML locale files. All CC0, all read directly. Their READMEs also carry a "draft, not for production" disclaimer, which conflicts with "production-ready".

**Community forks.** `openfiletax/openfile` (186 stars, 175 commits, not archived, last commit date not seen) and `jz4396/direct-file` (0 stars, 21 commits, documentation only as of 2026-10-07, targets TY2026). Neither shows added investment-income scope. Medium confidence.

**Reuse difficulty.** The engine is reusable (CC0, standalone, JS and JVM). The costs: a Scala toolchain; XML that the ADR itself calls verbose; several 3.1 features (typed declarations, Optional, modules) still proposals; no stated resolution algorithm in the ADR; and the ADR lists "engine too complex for available resources" as a risk. The Direct File application around it (Spring backend, MeF, auth) is not practically reusable.

### 2. OpenTaxSolver
Version 23.07 dated 2026-09-25 for TY2025; C; GPL-2.0; registered 2003. Federal 1040 with Schedules 1–3 and A–D, Forms 8949, 6251, 8889 and others; 11 states. A GUI calls per-form text-based solver programs. Rules are imperative C. It is meant to be used alongside the IRS booklets. High confidence, read directly (opentaxsolver.sourceforge.net, sourceforge.net project page).

### 3. PolicyEngine-US
AGPL-3.0; v2.41.4 on PyPI dated 2026-10-13; 25,583 commits. A household-level rules engine and microsimulation model. Read directly. Its representation (Python variable classes, YAML parameters with legal references, YAML tests, an OpenFisca-derived core) is from my recollection, not verified this session; my one attempt to fetch a parameter file returned 404. `policyengine-taxsim` (MIT) emulates TAXSIM-35 using PolicyEngine for 2021 onward, with a $15 comparison tolerance.

### 4. PSL Tax-Calculator
Release 6.8.4 dated 2026-10-01; 10,391 commits; CC0 per badge. Microsimulation of federal income and payroll taxes over tax-unit records, not forms. Read directly. Rule representation (Python functions plus a JSON parameter file) is from recollection. Tax-Brain was not investigated.

### 5. Free File Fillable Forms
Read directly on IRS.gov (page updated 2026-09-24). Electronic versions of IRS forms with free federal e-file, for people who can prepare from forms and instructions. "Basic calculations" and limited error checking; no interview, no state return, no amended returns. Requires a US cell number and a new account each year. Open now, closes 2026-10-15. The limitations page (filing season 2026, TY2025) lists Form 1040, Schedules 1–3, A, B, D and Form 8949 as available, with up to 50 W-2s and only 1099-R transcribed among 1099s. A user of the owner's tool could plausibly transcribe values into it. Not verified: whether it computes the Qualified Dividends worksheet or needs line 16 typed in; identity-verification requirements; TY2026 availability.

### 6. IRS Free File generally
Active. IRS.gov page updated 2026-10-13: guided software for AGI of $89,000 or less, Fillable Forms for any income. IRS Tax Tip 2026-19 (2026-03-10) says eight partners. High confidence, read directly. Nothing announced for the 2027 season.

### 7. Others
- **OpenTax** (https://github.com/filedcom/opentax): TY2025 Form 1040, 208 nodes as pure functions with typed schemas, 133 benchmark scenarios from Pub 4491, Pub 17 and MeF test packages, exports MeF XML and PDFs, does not transmit. Built by Filed and Crimson Tree ("Open Tax Technology Alliance", announced 2026-09-22). "Built and maintained by AI agents" with human review. The right to apply for MeF authorisation using the codebase is reserved. Schedule D / 8949 / worksheet support not confirmed. Commits through 2026-10-12. Read directly; claims about per-line traceability are the project's own and unverified.
- **UsTaxes**: see table. Redux data model, one TypeScript class per form per year extending a PDF `Fill` base. Read directly.
- **HabuTax**: explicit "fail loudly" design and field-level dependency solver with prompting for missing inputs. Last commit 2024-02-24.
- **tenforty**: validation doc reports 4 "gold" IRS scenarios, 42 formula-derived, 8 OTS regression; found an unresolved $6 OTS discrepancy for 2022; README says it cross-checks against Tax-Calculator.
- **py1040**: one cell per form line with line number, label, calculation and parents; the closest structural precedent for line-by-line transcription. 338 stars.
- **excel1040** (Glenn Reeves): 2025 version available; 2026 forecast being updated against draft forms.
- **TAXSIM**: production v35 covers federal law through 2023; a test version through 2024.

## Implications for this project

**(a) Does anything already do this?** No, not as specified. But the gap is narrower than it might appear. OpenTax already claims IRS-publication-sourced tests and IRS-traceable nodes, and py1040 and HabuTax already model per-line cells. What none offers is structured provenance on every value, literal worksheet transcription as the design constraint, or a small-atom formal core. Contributing to OpenTax is a real alternative that should be evaluated before building; reasons against are its AGPL-plus-reservation terms, AI-agent authorship (which cuts against lay-verifiable trust), and unknown coverage of the slice. Contributing to Direct File is not possible (archived).

**(b) Rules as data or graph.**
- Fact Graph (XML): shipped a real IRS product and survives in the Withholding Estimator. Its own team reports verbosity, a hard Scala codebase, and complexity risk. Completeness-aware facts are its distinctive win for interview flows.
- HabuTax and py1040 (field or cell dictionaries): small, legible, and both stalled as one-person projects; yearly form updates are the stated burden.
- OpenTax (node graph): too new to judge.
- tenforty: added a graph backend beside OTS to get features (marginal rates) the C code could not give.
- PolicyEngine and Tax-Calculator: parameters as data, formulas as code. Sustained by funded teams, but organised around policy variables, not form lines.

**(c) Oracles for differential testing.**
- Line-level, covering the slice: OpenTaxSolver and UsTaxes (independent codebases); excel1040; possibly OpenTax. All are TY2025 today, so use TY2025 for differential testing now and expect TY2026 versions around early 2027.
- tenforty is not independent of OpenTaxSolver.
- Totals only: Tax-Calculator and PolicyEngine. They will not match tax-table rounding exactly.
- TAXSIM is not usable for 2025–2026.
- Free File Fillable Forms' own arithmetic is a weak but official check at entry time.

## Could not verify / weak spots

- No IRS.gov statement of Direct File's discontinuation; Treasury PDF unreadable.
- Direct File XML contents (no QDCG worksheet, no Schedule 3 line 11) rest on tool summaries of single files; `income.xml` and `interest.xml` were not opened.
- Fact Graph's evaluation algorithm, caching and how flow conditions bind to facts were not read from source.
- PolicyEngine and Tax-Calculator internals are from recollection.
- OpenTax's form coverage, test contents and citation claims were not inspected in code.
- UsTaxes' "latest activity" is dependency bumps; substantive maintenance and a QDCG worksheet were not confirmed.
- Last-commit dates not seen for py1040, openfile, form-builder and tax-withholding-estimator (org-listing dates used).
- Whether TWE 2.0 on irs.gov runs exactly the public code is unconfirmed.
- Fillable Forms details (worksheet computation, identity verification, row limits on 8949) not verified.

## Open questions

1. Does OpenTax implement Schedule D, Form 8949 and the Qualified Dividends worksheet, and how good are its per-node citations in practice?
2. Is the Fact Graph engine (without Direct File's content) a suitable substrate for the owner's "functional atoms", or does the provability aim call for a smaller purpose-built core?
3. Will the IRS publish a Fact Dictionary for any return-preparation scope again, given continued Fact Graph investment?
4. Which official worked examples exist for the slice (Pub 17, Pub 550, Pub 4491, MeF ATS scenarios), and are any published for TY2026 before filing season?
5. Does Fillable Forms compute line 16 from the worksheet, or must the user enter it?

## Sources

- https://github.com/IRS-Public — organisation listing, 10 repos with update dates
- https://github.com/IRS-Public/direct-file — README, archived status
- https://github.com/IRS-Public/direct-file/commits/main/ — three commits, latest 2026-06-11
- https://raw.githubusercontent.com/IRS-Public/direct-file/main/LICENSE — CC0
- https://github.com/IRS-Public/direct-file/tree/main/direct-file/backend/src/main/resources/tax — fact dictionary module list
- https://raw.githubusercontent.com/IRS-Public/direct-file/main/direct-file/backend/src/main/resources/tax/taxCalculations.xml — tax computation facts
- https://raw.githubusercontent.com/IRS-Public/direct-file/main/direct-file/backend/src/main/resources/tax/schedule3.xml — Schedule 3 facts
- https://raw.githubusercontent.com/IRS-Public/direct-file/main/docs/engineering/Tax-Logic.md — facts, completeness, flow, testing
- https://raw.githubusercontent.com/IRS-Public/direct-file/main/docs/engineering/tax-flow/writing-facts.md — dependency syntax
- https://github.com/IRS-Public/fact-graph — README, status
- https://github.com/IRS-Public/fact-graph/commits/main/ — commits through 2026-09-01
- https://raw.githubusercontent.com/IRS-Public/fact-graph/main/docs/fact-graph-3.1-adr.md — 3.1 design record
- https://raw.githubusercontent.com/IRS-Public/fact-graph/main/LICENSE.md — CC0
- https://github.com/IRS-Public/tax-withholding-estimator — TWE 2.0
- https://github.com/IRS-Public/form-builder — declarative presentation layer
- https://github.com/openfiletax/openfile — community fork
- https://github.com/jz4396/direct-file — community fork targeting TY2026
- https://hn.svelte.dev/item/44428438 — fork author on removed MeF and SADI code (secondary)
- https://home.treasury.gov/system/files/131/Report-Replacement-of-Direct-File-2025.pdf — Treasury report (could not open)
- https://www.fox7austin.com/news/irs-direct-file-canceled-2026-tax-changes — news on discontinuation (secondary)
- https://home.treasury.gov/system/files/8861/IRS%20DF%20FLYER%202025_ENG.pdf — Direct File scope flyer (via search summary)
- https://www.irs.gov/e-file-providers/free-file-fillable-forms — Fillable Forms status
- https://www.irs.gov/e-file-providers/free-file-fillable-forms-program-limitations-and-available-forms — forms and limits
- https://www.irs.gov/filing/free-file-do-your-federal-taxes-for-free — Free File status
- https://www.irs.gov/newsroom/irs-free-file-supports-even-more-complex-returns — Tax Tip 2026-19
- https://opentaxsolver.sourceforge.net/ and https://opentaxsolver.sourceforge.net/download2025.html — OpenTaxSolver
- https://sourceforge.net/projects/opentaxsolver/ — licence, language
- https://github.com/PolicyEngine/policyengine-us and https://pypi.org/project/policyengine-us/ — PolicyEngine-US
- https://github.com/PolicyEngine/policyengine-taxsim — TAXSIM emulator
- https://github.com/PSLmodels/Tax-Calculator and https://github.com/PSLmodels/Tax-Calculator/releases — Tax-Calculator
- https://github.com/ustaxes/UsTaxes, https://github.com/ustaxes/UsTaxes/commits/master/, https://raw.githubusercontent.com/ustaxes/UsTaxes/master/docs/ARCHITECTURE.md — UsTaxes
- https://github.com/habutax/habutax and https://github.com/habutax/habutax/commits/main/ — HabuTax
- https://github.com/mmacpherson/tenforty, https://github.com/mmacpherson/tenforty/commits/main/, https://raw.githubusercontent.com/mmacpherson/tenforty/main/docs/irs-validation.md — tenforty
- https://github.com/b-k/py1040 — py1040
- https://opentax.filed.com/, https://github.com/filedcom/opentax, https://github.com/filedcom/opentax/commits/main/ — OpenTax
- https://sites.google.com/view/incometaxspreadsheet/home — excel1040
- https://taxsim.nber.org/ and https://taxsim.nber.org/taxsim35/ — TAXSIM
