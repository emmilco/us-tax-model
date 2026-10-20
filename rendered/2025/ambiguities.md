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

- Status: Owner accepted, after Stage 13.
- Cite: [i8889] p. 5, Line 3, Note; p. 7, Line 7 Additional Contribution Amount and the worksheet (2025; sha256 da6f2f58)

## amb.2025.auto_later_year_basis

- Text at issue: Pub. 946 chapter 5, Depreciation Worksheet for Passenger Automobiles, line 16 says of the special depreciation allowance "Enter -0- if this is not the year you placed the car in service", so for a later year line 18 (the basis for depreciation) is the business cost less the section 179 deduction only. Chapter 4, Figuring the Unadjusted Basis of Your Property, says the table rates apply to unadjusted basis, which reduces the original basis by "Any special depreciation allowance taken on the property".
- Candidate readings: Later years apply the table rate to the business cost less the section 179 deduction (the worksheet as printed). | Later years apply the table rate to the basis reduced by the special allowance taken in the first year (the general rule).
- **Chosen:** Neither is computed: a vehicle placed in service 2019 to 2024 that took a special allowance in its first year is refused (scveh.screen).
- Reason: The owner's ruling. The two passages give different amounts for the common case of a vehicle that took the 100% allowance, and the publication does not say which governs; vehicles that took no special allowance, or only section 179, are computed the same under both.
- Status: Owner ruling, Stage 14.
- Cite: [p946-html] Chapter 5, Depreciation Worksheet for Passenger Automobiles, line 16; chapter 4, Figuring the Unadjusted Basis of Your Property (2025; sha256 b5ac23e5)

## amb.2025.auto_unrecovered_basis

- Text at issue: Pub. 946 chapter 5, Deductions After the Recovery Period: "Unrecovered basis is the cost or other basis of the passenger automobile reduced by any ... depreciation, and section 179 deductions that would have been allowable if you had used the car 100% for business and investment use and the passenger automobile limits had not applied." Its example reduces the basis by the amounts allowed under the limits ($31,500 less $16,935), and in its last year allows $1,875 where the table amount is $1,814.
- Candidate readings: Reduce the basis by the deductions allowable at 100% business use under the limits, each the lesser of the table amount and the limit (the example's method). | Reduce the basis by the deductions allowable at 100% business use without the limits (the definition's last clause), which leaves no unrecovered basis. | As the first reading, but allow the limit in a year where it exceeds the table amount (the example's last row).
- **Chosen:** The first reading: each year's deduction at 100% business use is the lesser of the table amount (with the section 179 deduction in year 1) and that year's limit (scveh.d1 to scveh.d6).
- Reason: The second reading would make the section meaningless, since the limits are what create unrecovered basis; the example computes it with the limits ("At the end of 2024, you had an unrecovered basis of $14,565 ($31,500 − $16,935)") and its 60% variation confirms business use is taken as 100%. The example's last row ($1,875 allowed against $1,814) is taken as an error: the lesser of the two is the rule of every other row. The difference arises only when the unrecovered basis is below the year's limit.
- Status: Agent reading, Stage 14, for the owner's review.
- Cite: [p946-html] Chapter 5, Deductions After the Recovery Period, and its example (2025; sha256 b5ac23e5)

## amb.2025.mq_joint

- Text at issue: Pub. 946 chapter 4, Which Convention Applies?: the mid-quarter convention applies if "the total depreciable bases of MACRS property you placed in service during the last 3 months of the tax year ... are more than 40% of the total depreciable bases of all MACRS property you placed in service during the entire year." It does not say whether spouses filing a joint return are one taxpayer for the test.
- Candidate readings: Both spouses' property together, as one return. | Each spouse's property separately.
- **Chosen:** Both spouses' property together (mq.q4 and mq.total sum over every person on the return).
- Reason: The owner's ruling; section 179's limits are already figured once for a joint return (i4562 line 11, "combine the total taxable incomes for you and your spouse").
- Status: Owner ruling, Stage 14.
- Cite: [p946-html] Chapter 4, Which Convention Applies?, Mid-quarter convention (2025; sha256 b5ac23e5)

## amb.2025.vehicle_business_pct

- Text at issue: Form 4562 instructions, Column (c): "For automobiles and other vehicles, determine this percentage by dividing the number of miles the vehicle is driven for trade or business purposes ... by the total number of miles the vehicle is driven for all purposes." No precision is given.
- Candidate readings: Six decimal places, half-up. | Hundredths of a percent. | Whole percent.
- **Chosen:** Business miles over total miles to six decimal places, half-up (the prorate atom with places 6 wherever the percentage is applied).
- Reason: The owner's ruling.
- Status: Owner ruling, Stage 14.
- Cite: [i4562] p. 14, Column (c)—Business/investment use percentage (2025; sha256 5c1c95b7)

## amb.2025.sep_rate_places

- Text at issue: Pub. 560 chapter 5, Rate Worksheet for Self-Employed, line 3: "Self-employed rate as a decimal rounded to at least 3 decimal places (line 1 ÷ line 2)"; the Rate Table for Self-Employed gives six (10% is 0.090909).
- Candidate readings: Six decimal places (the Rate Table). | Three decimal places (the least the worksheet allows).
- **Chosen:** Six decimal places, half-up (person.sep_s5); only whole-percent plan rates are accepted, which the Rate Table covers.
- Reason: For whole-percent plan rates the Rate Table applies, and it prints six places; "at least 3" permits six.
- Status: Agent reading, Stage 14, for the owner's review.
- Cite: [p560] chapter 5, Rate Table for Self-Employed and Rate Worksheet for Self-Employed (For use in preparing 2025 returns; sha256 1f1f7abe)

## amb.2025.f7206_line15_person

- Text at issue: Form 7206 line 7: "Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the percentage on line 6"; the Schedule 1 line 17 worksheet, line 2, subtracts "any deductions on Schedule 1, lines 15 and 16". On a joint return Schedule 1 lines 15 and 16 combine both spouses.
- Candidate readings: Use the amounts of the spouse whose business establishes the plan (their own Schedule SE line 13 and SEP or SIMPLE deduction). | Use the whole of Schedule 1, lines 15 and 16.
- **Chosen:** The first: sc.f7206_line7 uses person.se_line13 and sc.f7206_line9 uses person.s16 of the business's owner.
- Reason: Line 5 of Form 7206 and its line 9 ("attributable to the same trade or business") look only at the businesses of the person whose insurance it is; the other spouse's self-employment tax is not attributable to this business. The readings agree when only one spouse is self-employed.
- Status: Agent reading, Stage 14, for the owner's review.
- Cite: [f7206] Form 7206 (2025), lines 5 to 9; i1040gi Schedule 1 line 17 worksheet, line 2 (2025; created 2025-10-02; sha256 822203c9)

## amb.2025.f7206_ratio_places

- Text at issue: Form 7206 line 6: "Divide line 4 by line 5". No precision is given.
- Candidate readings: Six decimal places, half-up. | Exact.
- **Chosen:** Six decimal places, half-up (prorate with places 6 on sc.f7206_line7_pos and sc.f7206_line9_pos).
- Reason: Six places is the precision of the other ratios in this tool; with one business the ratio is exactly 1.
- Status: Agent reading, Stage 14, for the owner's review.
- Cite: [f7206] Form 7206 (2025), line 6 (2025; created 2025-10-02; sha256 822203c9)

## amb.2025.f7206_plan_attribution

- Text at issue: Form 7206 line 9: "Enter the amount, if any, from Schedule 1 (Form 1040), line 16, ... attributable to the same trade or business in which the insurance plan is established." The instructions do not say how a contribution figured on all of a person's businesses is attributed to one.
- Candidate readings: In proportion to the business's share of the person's net profits (line 4 over line 5, as line 7 does for self-employment tax). | Wholly to the business under which the plan is established.
- **Chosen:** In proportion to the business's net profit over the total of the person's net profits (sc.f7206_line9).
- Reason: The SEP and SIMPLE limits are figured on the person's net earnings from all businesses; line 7 apportions self-employment tax in the same way. With one business both readings give the whole amount.
- Status: Agent reading, Stage 14, for the owner's review.
- Cite: [f7206] Form 7206 (2025), lines 6, 7 and 9 (2025; created 2025-10-02; sha256 822203c9)

## amb.2025.qbi_attribution

- Text at issue: Form 8995 instructions, Line 1: "To figure the total amount of QBI, you must consider all items that are attributable to the trade or business. This includes, but isn't limited to, ... deductible part of self-employment tax, self-employment health insurance deduction, and contributions to qualified retirement plans." No method is given for a person with more than one business.
- Candidate readings: Self-employment tax and retirement contributions in proportion to each business's net profit; the health insurance deduction to the business of its Form 7206. | Each item in proportion to net profit.
- **Chosen:** The first (sc.qbi_se, sc.qbi_plan, sc.qbi_ded). Line 2 of Form 8995, the total, does not depend on the method.
- Reason: Form 7206 is figured for the business under which the plan is established, so its deduction is attributable to that business; the other two are figured on all businesses together, as on Form 7206 line 7.
- Status: Agent reading, Stage 14, for the owner's review.
- Cite: [i8995] Line 1, Determining your qualified business income (2025; printed date 2026-01-26; sha256 875843ba)

## amb.2025.s179_carryover_no_property

- Text at issue: Form 4562 instructions, Worksheet 1: "1. Enter total cost of section 179 property ... placed in service during the tax year beginning in 2025 ... 3. Enter the smaller of line 1 or line 2 here ... 4. Enter the amount from line 3 here and on Form 4562, line 1"; Line 5: "If line 5 is zero, you cannot elect to expense any section 179 property. In this case, skip lines 6 through 11, enter zero on line 12, and enter the carryover of any disallowed deduction from 2024 ... on line 13."
- Candidate readings: As printed: with no section 179 property placed in service in 2025, line 1 and line 5 are zero and a 2024 carryover is carried again, not deducted. | Line 1 is the $2,500,000 limit whether or not property was placed in service, so a carryover can be deducted up to the income limit.
- **Chosen:** As printed (s179.line1 is the smaller of line 2 and $2,500,000).
- Reason: The worksheet and the line 5 instruction say so in terms. The agent recalls that the deduction of a carryover is not conditioned on placing new property in service, but has not verified that recollection against any archived source, so the printed instructions are followed and the question is put to the owner.
- Status: Agent reading, Stage 14, for the owner's review.
- Cite: [i4562] p. 3, Worksheet 1; p. 4, Line 5 (2025; sha256 5c1c95b7)
