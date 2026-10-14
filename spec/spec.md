# Specification

An open, verifiable formalization of the IRS individual income tax forms-and-instructions layer, and a guided self-preparation tool built on it.

Status: agreed scope and requirements for the proof of concept. Architecture and build order are in `design.md`. The evidence behind these choices is in `../research/report.md`.

## 1. Purpose

The durable asset is the formalization: a public, machine-readable encoding of IRS forms, worksheets and instructions in which every line can be checked by a non-programmer against the official text, and in which computations are built from a small set of primitive operations with proved properties.

The interview tool is the first client. It asks a person questions, decides which forms apply, computes them, and explains every value. The person files the return themselves.

What is formalized is the IRS's published procedure. It is not the Internal Revenue Code, and the IRS's forms can embed judgments about the law that are not announced. The project says so wherever it describes itself.

## 2. Scope of the proof of concept

One return: a US resident individual with wage income from two employers, interest, dividends and stock sales.

Development targets the tax year 2025 final forms and instructions. Tax year 2026 follows as a reviewed diff when its instructions are published. All filing statuses are carried in the parameter data; fixtures cover at least Single and Head of Household.

### 2.1 Computed

| Item | Notes |
|---|---|
| Form 1040 | Lines needed by the items below; standard deduction or itemized deductions, with the comparison shown |
| Schedule A | Medical and dental expenses, state and local taxes, home mortgage interest reported on Form 1098, investment interest, gifts to charity by cash and other than by cash, and the total; sub-cases in 2.2 are refused |
| Form 4952 | Investment interest expense deduction, including the election to treat qualified dividends and net capital gain as investment income and its effect on the tax worksheets |
| Form 8283 | Non-cash charitable contributions, Section A only (items and groups not requiring an appraisal, and publicly traded securities) |
| Tax Table and Tax Computation Worksheet | Both; the method switches at $100,000 of taxable income |
| Qualified Dividends and Capital Gain Tax Worksheet | |
| Schedule D Tax Worksheet | With the 28% Rate Gain Worksheet and Unrecaptured Section 1250 Gain Worksheet, fed only by Form 1099-DIV boxes 2b, 2c and 2d |
| Schedule B | Including the Part III foreign account and trust questions |
| Schedule D | Including the line 21 loss limit |
| Form 8949 | Securities boxes A to F, manual entry, adjustment codes limited to those in 2.2 |
| Schedule D lines 1a and 8a aggregate path | Broker totals where basis was reported and no adjustments apply |
| Schedule 3, excess Social Security tax withheld | Per person, across employers |
| Schedule 3, foreign tax credit without Form 1116 | Simple path only: the election for small amounts of passive foreign tax |
| Schedule 2 | Lines fed by Forms 8959 and 8960 |
| Form 8959 | Additional Medicare Tax |
| Form 8960 | Net Investment Income Tax, for the income types in scope |
| Form 8995 | Section 199A dividends from Form 1099-DIV box 5 only |

### 2.2 Refused with a cited explanation

The tool detects each of these from an interview answer or an input box and stops, naming the form it cannot prepare and the instruction that requires it. It never proceeds silently.

- Foreign tax above the limit for the simple path, or any other condition requiring Form 1116. **Deferred, not dropped: Form 1116 must be returned to after the proof of concept.**
- Qualified business income other than section 199A dividends.
- A capital loss carryover from the prior year.
- Digital asset transactions (Form 8949 boxes G to L).
- Form 8949 adjustments beyond: none, basis correction (code B), and wash sale (code W). Other codes are refused.
- Collectibles, section 1202 stock and section 1250 property sold directly.
- Form 6251, Schedule 1 income or adjustments, Schedule 1-A deductions.
- Schedule A items outside the lines computed: casualty and theft losses, non-cash gifts requiring an appraisal (Form 8283 Section B), charitable contributions limited by income or carried over, an investment interest carryover from a prior year, mortgage interest not reported on Form 1098 or subject to the debt limits, and the election to deduct sales tax in place of income tax.
- Credits for dependents and any other credit not listed in 2.1.
- Any condition in Schedule B requiring treatment not covered (nominee income, original issue discount, bond premium, seller-financed mortgage interest, savings bond exclusion).
- Married filing statuses where a rule in scope is figured per spouse and the interview cannot yet represent two people.

The estimated tax penalty is not computed. The tool states that the IRS will figure it and cites the instruction.

### 2.3 Non-goals

- Filing, signing or transmitting a return, or producing electronic filing data.
- Automating entry into any IRS system.
- Any hosted service, account, telemetry, analytics or network call carrying return data.
- State returns.
- Importing broker files.
- Filling official PDFs. Deferred until the PDF field structure has been inspected.
- A language model anywhere in the runtime path.
- Formalizing the statute.

## 3. Evidentiary requirements

These are the acceptance criteria for the formalization. Each is checkable by a third party from the repository alone.

1. **Provenance on every assertion.** Every line definition, parameter, guard, refusal and interview question carries a structured citation (section 5). The build fails if one is missing.
2. **Inspectable transcription.** Every encoded line can be rendered back as English in IRS worksheet phrasing, and the rendering is published beside the IRS text for line-against-line comparison.
3. **A closed atom vocabulary.** Every computed line is one application of an atom from a fixed list (section 4.2), or a declared exception. The number of exceptions is published.
4. **Proved atom properties.** The properties in section 6.3 are machine-checked over the integers.
5. **Structural checks.** Every reference resolves; the line graph has no cycles; units type-check; guards are exhaustive and disjoint; every interview path ends in either a complete set of forms or a cited refusal.
6. **Tests labelled by evidence class.** Every fixture states where its expected values came from (section 6.1). Official examples are all included, and are never the only evidence for a line.
7. **Visible ambiguity.** Where the instructions are ambiguous, silent, or internally in tension, the reading chosen is recorded with its reason and shown to the user whenever it affects their return.
8. **Year and revision pinning.** Every definition, parameter, example and source snapshot is pinned to a tax year and a document revision.
9. **Third-party reproducibility.** One documented command rebuilds everything and runs every check with no network access and no trust in the authors.
10. **No floating point.** Money is integer cents; rates are integer pairs; rounding happens only where an explicit, cited rounding step says so.

## 4. Data model for forms

### 4.1 Values and types

| Type | Representation |
|---|---|
| `Dollars` | Integer cents, signed |
| `NonNegDollars` | `Dollars` known to be zero or more |
| `Rate` | Pair of integers, numerator and denominator |
| `Count` | Non-negative integer |
| `Bool` | True or false |
| `Enum` | A named finite set, such as filing status or Form 8949 box |
| `Date` | Calendar date, for holding period only |

Every value also has a completeness state: unknown, placeholder, or known. A return can be produced only when every reachable line is known.

### 4.2 Atoms

| Atom | Meaning |
|---|---|
| `input` | A value the taxpayer supplies, tied to a source document box or an interview question |
| `copy` | The value of another line, on this or another form |
| `param` | A year-pinned constant, optionally keyed by filing status |
| `sum` | Add a list of lines |
| `subtract` | Signed subtraction |
| `subtract_floor0` | Subtract; if zero or less, zero |
| `smaller_of`, `larger_of` | Minimum or maximum of two lines |
| `multiply_rate` | Amount times a rate |
| `round` | Round to a stated unit by a stated rule |
| `table_lookup` | Banded lookup in a pinned table |
| `bracket_schedule` | Tax from a rate schedule |
| `sum_over` | Total of one column over a collection, with an optional filter |
| `test` | A comparison yielding `Bool`, with `all`, `any`, `not` |
| `choose` | Guarded alternatives; the guards must be exhaustive and disjoint |
| `opaque` | A named host-language function with its own citation and tests |

There are no user-defined functions, loops, local variables, strings or recursion. Adding an atom requires a written justification, a rendering template, a Lean definition and its lemmas. The vocabulary is cross-checked against the IRS Fact Graph operator list before it is frozen.

### 4.3 Lines

Each line of a form or worksheet is one record:

| Field | Content |
|---|---|
| `id` | Stable identifier that survives renumbering between years |
| `printed` | The line number or letter as printed in this revision |
| `label` | The IRS wording for the line |
| `type` | One of the types in 4.1 |
| `expr` | One atom application |
| `cite` | Citation (section 5) |
| `ambiguity` | Optional reference into the ambiguity register |

A form definition is a list of lines in printed order, plus the form's identity, tax year and revision.

### 4.4 Collections and instances

Forms that occur in multiples (Form W-2, Form 1099-INT, Form 1099-DIV, Form 8949 rows) are keyed collections. Aggregation across them is always an explicit `sum_over`. Pagination is a presentation matter and is not modelled.

A form evaluated more than once under different inputs is a parameterized instance, not a cycle.

### 4.5 Parameters and tables

Thresholds, rates, the Social Security wage base and standard deduction amounts live in one file per tax year. Each entry has its own citation. The Tax Table is stored as pinned data, cell by cell.

### 4.6 Gates

A gate is a `Bool` line with a citation whose truth either selects a path (which worksheet computes the tax) or triggers a refusal. Refusals are data: each names the unsupported form and cites the instruction requiring it.

## 5. Provenance model

A citation is a record:

| Field | Content |
|---|---|
| `doc` | Document identifier, for example the Form 1040 instructions |
| `tax_year` | Tax year |
| `revision` | The revision or posted date of the document |
| `locator` | Form line, worksheet step, or section and paragraph anchor |
| `snapshot` | Content hash of the archived source the locator was read from |
| `quote` | Optional short verbatim text |

Source documents are archived in the repository with their hashes and fetch dates, because IRS current-year addresses change content when a new year is released.

Every evaluation returns, for every line, a derivation: the atom applied, the operand lines with their values, the citation, and any rounding performed. Guards not taken are recorded with the reason.

The ambiguity register is one file per tax year. Each entry records the text at issue, the candidate readings, the reading chosen, the reason, and citations.

## 6. Test strategy

### 6.1 Evidence classes

Every expected value in the test suite is labelled with one class.

| Class | Source of the expected value |
|---|---|
| A | An official IRS worked example, cited |
| B | A human working the official form or worksheet by hand, recorded with the worker and the document revision |
| C | Agreement with an independent calculator, named with its version |
| D | A property that must hold for all inputs |

Research found official examples for single rules only: none for the Qualified Dividends and Capital Gain Tax Worksheet and none for a whole return in scope. Class A therefore cannot carry worksheet arithmetic. The project's public claims say this plainly.

### 6.2 Required coverage

- Every official example found for a form in scope is a class A fixture.
- Every worksheet has class B fixtures that together take both sides of every `smaller_of`, `larger_of`, `subtract_floor0`, `choose` and gate. The inputs are generated from the encoded worksheet; the expected values are worked by hand on the official document.
- Whole returns are compared (class C) against at least two independent calculators for the development tax year. Differences are investigated to a cited cause, never tolerated by a margin.
- A mutation score is computed and published per worksheet: the share of single-atom mutations that some fixture detects.
- A report shows, per line, which evidence classes cover it.

### 6.3 Properties and proofs

Proved in Lean 4 over the integers, once, for the atoms:

- `subtract_floor0`, `sum` of non-negatives, `smaller_of` of non-negatives and `multiply_rate` by a non-negative rate are non-negative.
- `round` matches its stated rule, is idempotent, and moves a value by less than one unit.
- Each atom is monotone or antitone in each argument, as tabulated.
- Evaluation of a well-formed, acyclic form terminates and is deterministic.
- The acyclicity and reference checker is sound.

Checked per worksheet by property test, and by proof where practical:

- Tax is non-negative and does not exceed the top rate times taxable income.
- Tax does not decrease as ordinary taxable income rises, other inputs fixed, within one computation method.
- The Tax Table agrees with the rate schedule applied at each band's midpoint, tested against every cell. This is a conjecture to test, not an assumption.

The Lean reference evaluator and the TypeScript evaluator read the same data files and must agree on every fixture and on generated inputs.

Not claimed: that the transcription matches the IRS text. No proof addresses that. The renderer, hand-worked fixtures and independent calculators do.

### 6.4 Interview checks

- Every combination of enumerated and yes/no answers leads to a complete form set or a cited refusal.
- The same answers always give the same return, regardless of the order in which they were given.
- No question is asked whose answer cannot affect a reachable line.

## 7. Versioning

- One definition file per form per revision; one parameter file per tax year.
- Draft IRS documents are marked as drafts and cannot back a release.
- Moving to a new year is a reviewed diff of the definition files and of the rendered English. Line renumbering shows as a change to `printed` with `id` unchanged.
- Fixtures are pinned to a revision and are never carried forward without re-derivation.
- The atom vocabulary and the data schema are versioned separately from the form data.

## 8. User-facing explanation model

- The primary output is a values sheet: each form in scope, line by line, in printed order, with its value and citation.
- Each value opens to its derivation: the instruction sentence, the operand lines and their values, and the arithmetic.
- Path choices are explained, including the paths not taken and why. The standard deduction and the itemized total are both shown, with the one used.
- A refusal names the form the tool cannot prepare, the answer or box that triggered it, and the instruction that requires it.
- Any ambiguity entry that affected the return is shown with the reading chosen.
- "I don't know" is an allowed answer. It leads to help naming the document box that holds the answer, or stops. It never becomes a default.
- Rounding is a return-wide setting, whole dollars by default, with cents available. The setting and its instruction are shown.
- Standing notices, at first run and on every output: this is not tax or legal advice; the user is responsible for the return; the tool implements published IRS forms and instructions, which are not the law itself; it is not affiliated with or endorsed by the IRS; and the list of what it covers and does not cover.

## 9. Operating constraints

These follow the research reading of the legal position, which has not been reviewed by a lawyer.

- Free of charge, with no payment, sponsorship or donation mechanism attached to the tool.
- Runs locally. No return data leaves the machine.
- No IRS or Treasury insignia, and no project name containing "IRS".
- No claims of accuracy, approval or certification.
- No personal tax documents or figures taken from them are stored in the repository.

Licences: Apache-2.0 for code; CC0 for form definitions, parameters, tables and fixtures.

## 10. Premises to check before encoding

These come from the research pass, which read sources through a summarising tool. Each must be confirmed against the archived IRS text before any line that depends on it is encoded.

- The conditions selecting the Schedule D Tax Worksheet over the Qualified Dividends and Capital Gain Tax Worksheet.
- The $100,000 switch between the Tax Table and the Tax Computation Worksheet.
- The wording of the rounding rules, and how row rounding on Form 8949 reconciles with total rounding on Schedule D.
- The conditions for reporting on Schedule D lines 1a and 8a without Form 8949.
- The limit and conditions for claiming foreign tax without Form 1116.
- The Form 8959 and Form 8960 thresholds by filing status.
- The excess Social Security rule, including the single-employer exception.
- The Form 8949 box set and adjustment codes.
- Whether Form 8995 suffices for section 199A dividends alone.
- The Schedule A line structure, the medical expense floor, and the state and local tax limit with any income-based reduction, for each tax year.
- The Form 4952 line structure, how its election changes the Qualified Dividends and Capital Gain Tax Worksheet and selects the Schedule D Tax Worksheet, and whether the form can be skipped in simple cases.
- The Form 8283 Section A and Section B thresholds, and the income limits on charitable deductions that would trigger a refusal.
- How itemized deductions, including investment interest, enter Form 8960, and whether a state tax refund from an itemized prior year brings Schedule 1 into scope.
- The tax year 2026 changes to itemized deductions reported by the research pass: a floor on charitable gifts and a cap on the value of itemized deductions.

## 11. Open items

- Form 1116, deferred by decision.
- Filling official PDFs.
- Capital loss carryover in and out.
- Married filing statuses for per-person rules.
- Credits for dependents, which a Head of Household filer will commonly need.
- A count of official single-line answers in the IRS volunteer test (Form 6744) that touch the slice.
- The questions for a lawyer listed in `../research/04_legal_liability.md`.
