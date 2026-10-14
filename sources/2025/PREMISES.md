# Stage 0 premise checks — paused for scope decision

Status: **incomplete**. The Form 8995 premise is corrected below. The remaining
premises have not been verified. The specification is unchanged pending the
owner's decision, as required by `HANDOFF.md`, Stage 0 step 5.

Reviewer: Codex (agent), reading local `pdftotext -layout` extracts of the
archived PDFs. This is source inspection, not a human transcription review,
proof of correctness, or a class B fixture.

## P09 — Does Form 8995 suffice for section 199A dividends alone?

**Finding: no, not for every income level in scope. Correction required.**

Directly inspected evidence:

| Source | Revision | Locator | Finding |
| --- | --- | --- | --- |
| [i8995.pdf](i8995.pdf) | TY2025, printed January 26, 2026 | PDF p. 1, “Who Can Take the Deduction” | Eligibility includes qualified REIT dividends, but use of Form 8995 also requires taxable income before the QBI deduction no greater than $394,600 for married filing jointly or $197,300 for all other returns, and no specified cooperative patron status. Otherwise the instructions direct use of Form 8995-A. |
| [f8995.pdf](f8995.pdf) | TY2025, created September 12, 2025 | PDF p. 1, applicability statement above line 1 | The form itself repeats the income ceiling and cooperative exclusion. |
| [i8995a.pdf](i8995a.pdf) | TY2025, printed January 26, 2026 | PDF p. 1, “Who Can Take the Deduction” | The higher-income applicability conditions explicitly include qualified REIT dividends. |
| [f8995a.pdf](f8995a.pdf) | TY2025, created September 12, 2025 | PDF p. 1, applicability statement; p. 2, Part IV | The form states the higher-income condition and has a REIT/PTP component within the deduction calculation. |

Interpretation: having only section 199A dividends does not exempt the filer from
the form-selection income threshold. A high-income return with this income can
therefore exceed the agreed Form 8995-only scope. This is a form-selection
boundary, not a conclusion that the dividend deduction itself disappears above
the threshold. No conclusion is drawn about any particular filer's taxable income
or dividend boxes.

### Proposed specification change (not applied)

Recommended: keep the intended dividend coverage and expand only the necessary
form path.

1. In `spec/spec.md` section 2.1, replace the Form 8995 row with:

   > Forms 8995 and 8995-A — Section 199A dividends from Form 1099-DIV box 5
   > only; select the form using its cited applicability conditions. Form 8995-A
   > coverage is limited to the dividend-only path and the lines necessary to
   > compute and report that deduction.

2. In `spec/design.md` Stage 4, replace “Form 8995 for section 199A dividends”
   with “Forms 8995 and 8995-A for section 199A dividends, with cited form
   selection.”

The existing refusal of other qualified business income remains applicable.
Exact gates, carryover treatment, holding-period conditions, and required lines
would still need source review; this proposal does not settle them or implement
them ahead of Stage 4.

Alternative: retain Form 8995 alone, explicitly restrict section 2.1 to eligible
returns, and add a cited Form 8995-A refusal in section 2.2. This narrows the
returns the proof of concept can prepare. Either choice requires the owner's
decision before changing the specification.

## Remaining premise checklist

These identifiers follow the order of bullets in `spec/spec.md` section 10.

| ID | Premise | Status |
| --- | --- | --- |
| P01 | Schedule D versus Qualified Dividends worksheet selection | Pending |
| P02 | $100,000 Tax Table / Tax Computation Worksheet switch | Pending |
| P03 | Rounding, including Form 8949 rows versus Schedule D totals | Pending |
| P04 | Schedule D lines 1a and 8a aggregate reporting conditions | Pending |
| P05 | Foreign tax credit without Form 1116 | Pending |
| P06 | Forms 8959 and 8960 thresholds by filing status | Pending |
| P07 | Excess Social Security and the single-employer exception | Pending |
| P08 | Form 8949 box set and adjustment codes | Pending |
| P09 | Form 8995 sufficiency for section 199A dividends alone | Corrected; owner decision pending |
| P10 | Schedule A structure, medical floor, SALT limit and reduction | Pending |
| P11 | Form 4952 structure, election, worksheet routing and filing exception | Pending |
| P12 | Form 8283 sections and charitable deduction limitations | Pending |
| P13 | Form 8960 deductions and prior-year state tax refunds | Pending |
| P14 | Reported TY2026 charitable floor and itemized deduction value cap | Pending; requires suitable official evidence beyond simply assuming TY2025 rules carry forward |

Stage 0 must resume here after the scope decision. It is not complete and
Stage 1 must not begin yet.

## Snapshot identifiers for P09

- `f8995.pdf`: SHA-256 `55380ad230303e1586ce97f0f224265b8337ad18c9204f0fb7325e95a76b5cde`.
- `f8995a.pdf`: SHA-256 `3362db81b8ef60cfaa93354858c6c92bac16e63984be0805c6479d272a6ec9aa`.
- `i8995.pdf`: SHA-256 `875843baead68f6fa9aa7c3f6f27d6c1f37cb971ac334bcf414acdb4c1487684`.
- `i8995a.pdf`: SHA-256 `6df1301c1ce74ef391219094831accd22cfeac26ce510f4499c4834484f55d97`.
