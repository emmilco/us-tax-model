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

## amb.2025.eic_below_table

- Text at issue: Worksheet A, line 2 says to look up the earned income in the EIC Table, whose first row is "At least 1 But less than 50". An earned income below $1 (for example, no wages) has no row.
- Candidate readings: The credit on line 2 is zero, so "If line 2 is zero, STOP. You can't take the credit" applies. | The return is refused because the table gives no value.
- **Chosen:** The credit on line 2 is zero.
- Reason: Every column of the table is zero at the far end and rises from $2 to $11 in the first row, so the credit is built up from earned income; with no row for less than $1 the table grants nothing there, and the worksheet's own instruction for a zero line 2 ends the computation. Rev. Proc. 2024-40 section 3.06(1) describes the credit as a percentage of earned income up to the earned income amount, which is zero at zero earned income.

- Status: Owner approved ($0) after the check that it cannot err; below $1 every column's credit, figured at the steepest build-up rate (45%), is under $0.45 and rounds to $0, and earned income is never negative in scope (self-employment is refused).
- Cite: [i1040gi] p. 46, Worksheet A, line 2; p. 49, EIC Table, first row (2025; printed date 2026-02-25; sha256 482e9c48)

## amb.2025.hsa_last_month_change

- Text at issue: Form 8889 line 3 instructions, rule 2, "If the last-month rule ... applies, you are considered an eligible individual for the entire year. You are treated as having the same HDHP coverage for the entire year as you had on the first day of the last month", and rule 4, "If you were, or were considered, an eligible individual for the entire year and you changed your type of coverage during the year, enter on line 3 ... the greater of" the Line 3 Limitation Chart and Worksheet or the maximum for the December 1 coverage.
- Candidate readings: Under the last-month rule, line 3 is the maximum for the December 1 coverage (rule 2's same coverage for the year). | Under the last-month rule with a change of coverage type, line 3 is the greater of the chart and the December 1 maximum (rule 4 names a filer who "were considered" eligible all year).
- **Chosen:** The greater of the chart and the December 1 maximum when the coverage type changed among the eligible months; the December 1 maximum otherwise (f8889.line3_last_month).
- Reason: Rule 4 names the filer considered eligible all year, which is the last-month rule's filer, so it reads as the stricter fit to the text; the result is never less than rule 2's amount. Found by the Stage 11 class M hand-work (the model applied rule 4; the second transcription read rule 2); the owner chose rule 4.

- Status: Owner ruling after Stage 11 (keep rule 4).
- Cite: [i8889] p. 4, Line 3, rules 2, 3 and 4 (2025; sha256 da6f2f58)

## amb.2025.sli_ratio_places

- Text at issue: The Student Loan Interest Deduction Worksheet, line 7, says "Enter the result as a decimal (rounded to at least three places)".
- Candidate readings: Round the ratio to exactly three decimal places (half-up), the least precision the text allows. | Keep the ratio at full precision, which also satisfies "at least three places".
- **Chosen:** Round the ratio half-up to three decimal places (the prorate atom with places 3 on sli.line8_figured).
- Reason: The owner's ruling. Three places is the least precision the text allows and the usual hand computation; the readings differ by at most a few cents of deduction (for example $167.50 against $166.67 on line 8 when line 6 is $1,000 and line 1 is $2,500).

- Status: Owner ruling, Stage 11.
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 7 (2025; printed date 2026-02-25; sha256 482e9c48)

## amb.2025.qbi_cooperative_patron

- Text at issue: Form 8995 says to use the form if "you aren't a patron of an agricultural or horticultural cooperative"; the Instructions for Form 8995 and the Form 1040 instructions for line 13a say "you aren't a patron in a specified agricultural or horticultural cooperative".
- Candidate readings: Only a patron of a specified agricultural or horticultural cooperative is outside Form 8995 (the instructions). | Any patron of an agricultural or horticultural cooperative is outside Form 8995 (the form).
- **Chosen:** Refuse any patron of an agricultural or horticultural cooperative, specified or not (qbi.unsupported).
- Reason: The owner asked for the strictly accurate reading. Refusing every patron satisfies both texts: a filer the form excludes is never computed on it, and a filer the instructions exclude is a patron the form also excludes. The cost is a refusal for a patron of a cooperative that is not specified, which the instructions would allow.

- Status: Owner ruling (choose the strictly accurate reading), after Stage 10.
- Cite: [f8995] Form 8995 (2025), note above line 1; i8995, Who Can Use Form 8995; i1040gi line 13a (2025; created 2025-09-12; sha256 55380ad2)

## amb.2025.eic_valid_ssn

- Text at issue: For the EIC a child's valid SSN is "a number issued by the Social Security Administration unless 'Not Valid for Employment' is printed on the social security card and the number was issued solely to allow the recipient ... to apply for or receive a federally funded benefit", issued on or before the due date of the return. The child tax credit asks for "an SSN valid for employment" issued before the due date.
- Candidate readings: Reuse the child tax credit question for the EIC count. | Ask a separate per-person question in the EIC's own words.
- **Chosen:** Ask a separate per-person question in the EIC's own words (dependent.eic_ssn).
- Reason: The two definitions differ for a number issued on the due date itself and for a card marked "Not Valid for Employment" for a reason other than federally funded benefits. The owner preferred the separate question as the safer reading; it is asked only for a person who is already a qualifying child for the EIC.

- Status: Owner ruling, Stage 9 follow-up.
- Cite: [i1040gi] pp. 44-45, Social security number (SSN) (EIC); p. 18, Step 3, question 4 (child tax credit) (2025; printed date 2026-02-25; sha256 482e9c48)

## amb.2025.carloan_ratio_places

- Text at issue: Proposed § 1.163-16(d)(2)(iii)(A) and (d)(4) allocate a loan's interest "on a pro rata basis" between the part that is a specified passenger vehicle loan and the rest, without saying how the ratio is figured or rounded.
- Candidate readings: Round the ratio (qualifying debt divided by the loan) half-up to six decimal places, then the interest to the cent. | Keep the ratio exact and round only the allocated interest to the cent. | Round the ratio to three places, as the Student Loan Interest Deduction Worksheet does.
- **Chosen:** Round the ratio half-up to six decimal places (the prorate atom with places 6 on carloan.mixed_prorated and carloan.refi_interest), the product half-up to the cent.
- Reason: The owner's ruling. Six places keeps the existing prorate atom unchanged; at the $10,000 cap on line 24 the result differs from an exact ratio by less than one cent, while three places could differ by about $5.

- Status: Owner ruling, Stage 12.
- Cite: [fr-2025-24154] pp. 20–22, Proposed § 1.163-16(d)(2)(iii)(A) and (d)(4) (Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154; sha256 4d243f55)

## amb.2025.hsa_line7_months

- Text at issue: The Additional Contribution Amount Worksheet for Form 8889 line 7 says "$1,000 × number of months eligible", for a married filer age 55 or older when "You or your spouse had family coverage under an HDHP and were, or were considered to be, an eligible individual on the first day of the month" and "You were not enrolled in Medicare for the month". It does not say whether a month of self-only coverage, in a year with family coverage in other months, counts.
- Candidate readings: Count every month you were, or were considered to be, an eligible individual (an eligible individual is never enrolled in Medicare). | Count only the months treated as having family coverage.
- **Chosen:** Count every month treated as eligible (f8889.elig_months, all twelve under the last-month rule).
- Reason: Line 3 leaves out the additional contribution amount for every month once a married filer had family coverage at any time (p. 5, Note), so counting only family months would drop it for the self-only months altogether, which nothing in the instructions says. The worksheet's own words are "number of months eligible", and "If items (1) and (2) apply to all months during 2025, enter $1,000". Both readings agree when every eligible month has family coverage.

- Status: Agent reading, Stage 13, for the owner's review.
- Cite: [i8889] p. 5, Line 3, Note; p. 7, Line 7 Additional Contribution Amount and the worksheet (2025; sha256 da6f2f58)
