# Ambiguity register, tax year 2025

## amb.2025.multiplication_subcent

- Text at issue: Percentage calculations can produce fractional cents when exact-cents mode is used. The form instructions do not specify subcent handling.
- Candidate readings: Round the product half-up to the nearest cent at the multiplication. | Truncate the product toward zero to whole cents. | Carry the exact fraction forward until some later rounding step.
- **Chosen:** Round the product half-up to the nearest cent at the multiplication.
- Reason: Matches the half-up convention of the printed whole-dollar rounding rules. The whole-dollar default is unaffected: whole-dollar amounts multiplied by these rates produce exact cents, so the reading only matters when cents are turned on.

- Status: Applied throughout Stages 1–4; whole-dollar mode remains deferred.
- Cite: [i1040gi] QDCGT worksheet, lines 18 and 21; Rounding Off to Whole Dollars, p. 23 (2025; printed date 2026-02-25; sha256 482e9c48)

## amb.2025.ss_wages

- Text at issue: Schedule 3 line 11 says total wages without naming W-2 boxes.
- Candidate readings: Box 1 taxable compensation | Social Security wages and tips in boxes 3 plus 7
- **Chosen:** Use boxes 3 plus 7, summed across employers separately per person.
- Reason: Owner approved the Stage 2 proposal. iw2w3 p. 18 defines these boxes and their combined wage base; box 1 can exclude deferrals subject to Social Security.
- Status: Owner approved modeling interpretation; source transcription review remains open.
- Cite: [iw2w3] p. 18, boxes 3 and 7; compare i1040gi p. 117, Schedule 3 line 11 (2025; printed date 2025-02-19; sha256 bfecbc99)

## amb.2025.sales_rounding

- Text at issue: Form 8949 permits cents or rounding all amounts; Form 1040 says add cents before rounding a line total. Row versus total reconciliation is not explicit.
- Candidate readings: Preserve exact cents throughout. | Round each row before aggregation. | Round totals after aggregating exact rows.
- **Chosen:** Preserve exact cents throughout Stage 3; whole-dollar mode remains deferred.
- Reason: Avoid choosing a reconciliation policy without explicit support; cents are expressly permitted.
- Status: Stage 3 implementation choice; whole-dollar default not implemented.
- Cite: [i8949] p. 3, Rounding Off to Whole Dollars; compare i1040gi p. 23 (2025; printed date 2026-01-20; sha256 f077991c)

## amb.2025.sd4952_selection

- Text at issue: Schedule D line 20 directs Form 4952 filers to SDTW, while the worksheet applicability text specifies an amount on Form 4952 line 4g and gives exceptions.
- Candidate readings: Follow line 20 literally for every Form 4952 filer. | Apply the detailed worksheet applicability and exceptions.
- **Chosen:** Use the detailed worksheet conditions, including line 4g and exceptions.
- Reason: The worksheet explicitly limits its own use and the Form 1040 line 16 instructions repeat the line 4g condition.
- Status: Explicit Stage 3 source interpretation for review.
- Cite: [i1040sd] p. 15, Schedule D Tax Worksheet applicability; compare f1040sd line 20 and i1040gi p. 36 (2025; printed date 2025-12-11; sha256 650643a6)

## amb.2025.box2c_scope

- Text at issue: The computed-scope table includes Form 1099-DIV box 2c, but the refusal list excludes Form 8949 code Q and Form 6251.
- Candidate readings: Expand the distribution-only section 1202 exclusion path and associated AMT treatment. | Retain the explicit code Q/Form 6251 exclusions and refuse box 2c pending scope expansion.
- **Chosen:** Refuse nonzero box 2c; no exclusion or AMT amount is silently omitted.
- Reason: Archived Schedule D instructions require the exclusion on Form 8949 code Q and describe an AMT adjustment for 50/60/75-percent exclusions. The existing explicit exclusions are retained; the owner was notified and asked, then said continue without selecting an expansion.
- Status: Scope conflict disclosed; expansion remains open.
- Cite: [i1040sd] p. 8, Gain from Form 1099-DIV and Alternative Minimum Tax (2025; printed date 2025-12-11; sha256 650643a6)
