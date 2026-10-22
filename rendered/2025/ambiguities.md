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
- Cite: [i1040sd] p. 15, Schedule D Tax Worksheet, applicability; compare f1040sd line 20 and i1040gi p. 36 (2025; printed date 2025-12-11; sha256 650643a6)

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
- Status: Owner accepted, after Stage 14.
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
- Status: Owner accepted, after Stage 14.
- Cite: [p560] chapter 5, Rate Table for Self-Employed and Rate Worksheet for Self-Employed (For use in preparing 2025 returns; sha256 1f1f7abe)

## amb.2025.f7206_line15_person

- Text at issue: Form 7206 line 7: "Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the percentage on line 6"; the Schedule 1 line 17 worksheet, line 2, subtracts "any deductions on Schedule 1, lines 15 and 16". On a joint return Schedule 1 lines 15 and 16 combine both spouses.
- Candidate readings: Use the amounts of the spouse whose business establishes the plan (their own Schedule SE line 13 and SEP or SIMPLE deduction). | Use the whole of Schedule 1, lines 15 and 16.
- **Chosen:** The first: sc.f7206_line7 uses person.se_line13 and sc.f7206_line9 uses person.s16 of the business's owner.
- Reason: Line 5 of Form 7206 and its line 9 ("attributable to the same trade or business") look only at the businesses of the person whose insurance it is; the other spouse's self-employment tax is not attributable to this business. The readings agree when only one spouse is self-employed.
- Status: Owner accepted, after Stage 14.
- Cite: [f7206] Form 7206 (2025), lines 5 to 9; i1040gi Schedule 1 line 17 worksheet, line 2 (2025; created 2025-10-02; sha256 822203c9)

## amb.2025.f7206_ratio_places

- Text at issue: Form 7206 line 6: "Divide line 4 by line 5". No precision is given.
- Candidate readings: Six decimal places, half-up. | Exact.
- **Chosen:** Six decimal places, half-up (prorate with places 6 on sc.f7206_line7_pos and sc.f7206_line9_pos).
- Reason: Six places is the precision of the other ratios in this tool; with one business the ratio is exactly 1.
- Status: Owner accepted, after Stage 14.
- Cite: [f7206] Form 7206 (2025), line 6 (2025; created 2025-10-02; sha256 822203c9)

## amb.2025.f7206_plan_attribution

- Text at issue: Form 7206 line 9: "Enter the amount, if any, from Schedule 1 (Form 1040), line 16, ... attributable to the same trade or business in which the insurance plan is established." The instructions do not say how a contribution figured on all of a person's businesses is attributed to one.
- Candidate readings: In proportion to the business's share of the person's net profits (line 4 over line 5, as line 7 does for self-employment tax). | Wholly to the business under which the plan is established.
- **Chosen:** In proportion to the business's net profit over the total of the person's net profits (sc.f7206_line9).
- Reason: A SEP or SIMPLE plan is supported only for a person with one Schedule C (Pub. 560 p. 7, "If you have more than one business, but only one has a retirement plan, only the earned income from that business is considered for that plan"; a plan with more than one Schedule C is refused, person.plan_screened), and with one business both readings give the whole amount.
- Status: Owner accepted, after Stage 14. Reason corrected after T-044 (BUG-0078; owner ruling to refuse a plan with more than one Schedule C); the reading is unchanged.
- Cite: [f7206] Form 7206 (2025), lines 6, 7 and 9 (2025; created 2025-10-02; sha256 822203c9)

## amb.2025.qbi_attribution

- Text at issue: Form 8995 instructions, Line 1: "To figure the total amount of QBI, you must consider all items that are attributable to the trade or business. This includes, but isn't limited to, ... deductible part of self-employment tax, self-employment health insurance deduction, and contributions to qualified retirement plans." No method is given for a person with more than one business.
- Candidate readings: Self-employment tax and retirement contributions in proportion to each business's net profit; the health insurance deduction to the business of its Form 7206. | Each item in proportion to net profit.
- **Chosen:** The first (sc.qbi_se, sc.qbi_plan, sc.qbi_ded). Line 2 of Form 8995, the total, does not depend on the method.
- Reason: Form 7206 is figured for the business under which the plan is established, so its deduction is attributable to that business; self-employment tax is figured on all businesses together, as on Form 7206 line 7, and a retirement plan is supported only for a person with one Schedule C (person.plan_screened), so its contributions belong to that business.
- Status: Owner accepted, after Stage 14.
- Cite: [i8995] Line 1, Determining your qualified business income (2025; printed date 2026-01-26; sha256 875843ba)

## amb.2025.s179_carryover_no_property

- Text at issue: Form 4562 instructions, Worksheet 1: "1. Enter total cost of section 179 property ... placed in service during the tax year beginning in 2025 ... 3. Enter the smaller of line 1 or line 2 here ... 4. Enter the amount from line 3 here and on Form 4562, line 1"; Line 5: "If line 5 is zero, you cannot elect to expense any section 179 property. In this case, skip lines 6 through 11, enter zero on line 12, and enter the carryover of any disallowed deduction from 2024 ... on line 13."
- Candidate readings: As printed: with no section 179 property placed in service in 2025, line 1 and line 5 are zero and a 2024 carryover is carried again, not deducted. | Line 1 is the $2,500,000 limit whether or not property was placed in service, so a carryover can be deducted up to the income limit.
- **Chosen:** The second. s179.line1 is the $2,500,000 the line 1 instruction states, so line 5 is the dollar limitation and a carryover is deducted up to the dollar limitation less the 2025 election and up to the business income limit (line 11). On a separate return line 5 is 50% of the limitation, the instruction's allocation when the spouses elect no other.
- Reason: Research for the owner (ambiguities/research/amb.2025.s179_carryover_no_property.md) quotes the archived 26 U.S.C. 179(b)(3)(B), Treas. Reg. 1.179-2(b) and 1.179-3(b) to (d), and P.L. 119-21 sec. 70306. The carryover's room is "the limitation of paragraphs (1) and (2)", the dollar amount, which the cost of 2025 property reduces only above $4,000,000. Form 4562 computes exactly that when line 1 is the $2,500,000 the line 1 instruction states (p. 4). The optional Worksheet 1 instead takes the smaller of that and the cost of 2025 property, a cap that changes no return without a carryover and departs from the statute on a return with one.
- Status: Owner ruling after Stage 14 (T-043), on the research memo.
- Cite: [i4562] p. 4, Line 1 and Worksheet 1; p. 5, Line 5 (2025; sha256 5c1c95b7)

## amb.2025.meals_full_exceptions

- Text at issue: Schedule C instructions, Line 24b, Amount of deduction: "However, you can fully deduct meals and incidentals furnished or reimbursed to an employee if you properly treat the expense as wages subject to withholding. You can also fully deduct meals and incidentals provided to a nonemployee to the extent the expenses are includible in the gross income of that person and reported on Form 1099-NEC. See chapter 5 of Pub. 15, Employer's Tax Guide, for details and other exceptions. See also chapter 8 of Pub. 334."
- Candidate readings: Only the two cases the instruction names are deducted in full. | The two named cases and the other exceptions to the 50% limit, as Pub. 463 lists them (Exception to the 50% Limit for Meals, p. 16), each deducted in full.
- **Chosen:** The second (sc.meals_100). Of Pub. 463's six exceptions, exception 2 (an employee reimbursed under an accountable plan) concerns employees and is not a Schedule C expense; exception 1 is the instruction's first case; exceptions 3 to 6 are the client-reimbursed independent contractor, recreation for employees, food for the general public, and meals sold to the public. The question asks for none of the amounts entered elsewhere on Schedule C, such as cost of goods sold.
- Reason: The instruction says other exceptions exist and points to Pub. 15 chapter 5 and Pub. 334 chapter 8. Pub. 15 (2025) chapter 5 covers whether meals are wages and lists no exceptions to the limit; Pub. 334 (2025), Travel and Meals, repeats the 50% rule and refers to Pub. 463, which lists the exceptions. Asking for the named cases only would leave a filer whose meals fall under another exception with no correct entry.
- Status: Owner ruling after Stage 14 (T-042).
- Cite: [p463] p. 16, Exception to the 50% Limit for Meals, exceptions 1 to 6 (For use in preparing 2025 returns; sha256 ddc3bb15)

## amb.2025.vehicle_s179_claimed

- Text at issue: Pub. 946, Depreciation Worksheet for Passenger Automobiles, line 10: "Section 179 deduction claimed this year (not more than line 9)"; Form 4562 line 11: "The total cost you can deduct is limited to your taxable income from the active conduct of a trade or business."
- Candidate readings: The section 179 cost elected for the vehicle this year (Form 4562 column (i)), not more than line 9. | The part of that election deducted this year after the business income limit of Form 4562 line 11, the rest being carried over.
- **Chosen:** The first (scveh.line10 through scveh.s179_line10).
- Reason: The two differ only when the business income limit cuts the year's section 179 deduction and the vehicle carries part of it. The basis is reduced by the whole amount elected, the carryover included, since Pub. 946 says that on a disposition before the carryover is used "you must add it back to the property's basis" (p. 20); the worksheet then limits the year's depreciation by the same amount. The second reading would let the year's depreciation room grow by an amount that is still deductible later.
- Status: Agent reading, after Stage 14 (scveh render review), for the owner's review (TASKS.md T-046).
- Cite: [p946] p. 62, Depreciation Worksheet for Passenger Automobiles, line 10; p. 20, Carryover of disallowed deduction (For use in preparing 2025 returns; sha256 07fadfb2)

## amb.2025.dc_ineligible_providers

- Text at issue: i2441 p. 2, item 4: "The person who provided the care wasn't your spouse, the parent of your qualifying child, or a person whom you can claim as a dependent. If your child (including stepchild or foster child) provided the care, they must have been age 19 or older by the end of 2025 and they can't be your dependent"; p503 p. 8, Payments to Relatives or Dependents: "A person for whom you (or your spouse if filing jointly) can claim as a dependent", "Your child ... who was under age 19 at the end of the year, even if they aren't your dependent", "A person who was your spouse any time during the year" and "The parent of your qualifying person if your qualifying person is your child and under age 13".
- Candidate readings: Pub. 503's list of four (dcprov.related), which is broader for a spouse (at any time during the year) and narrower for a parent (only of your child under 13). | The instructions' list (your spouse, the parent of your qualifying child, your dependent, your child under 19).
- **Chosen:** The first (dcprov.related asks Pub. 503's list; a Yes refuses Form 2441).
- Reason: The owner's decision (Stage 15, decision 6). The publication is the more specific text, and both lists agree on a dependent and a child under 19. A provider in either list refuses, so the reading decides only which question is asked.
- Status: Owner ruling, Stage 15 (T-048).
- Cite: [p503] p. 8, Payments to Relatives or Dependents, "However, don't count any amounts you pay to" (For use in preparing 2025 returns; sha256 3a00d0c1)

## amb.2025.dc_line1e_attribution

- Text at issue: i2441 p. 4, Lines 4 and 5: "If filing jointly, figure your and your spouse's earned income separately" and earned income "generally includes ... The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z"; line 1z includes line 1e (Form 2441 line 26), a figure for the return, not for either spouse.
- Candidate readings: Line 1e is the earned income of the spouse whose Forms W-2 show box 10; when both spouses' (or neither spouse's) Forms W-2 show box 10 on a joint return, line 1e is above zero and a credit remains (line 31 above zero), the form is refused. | Line 1e is split between the spouses in proportion to each spouse's part of line 12. | Line 1e is the filer's (line 4) earned income.
- **Chosen:** The first (person.dc_1e, f2441.attrib_gate). On a return that is not joint there is one person and line 1e is theirs. When the split is undetermined but no credit remains (line 31 is zero, so line 3 and line 6 are zero whatever lines 4 and 5 hold), line 1e is shown in the taxpayer's line 4, keeping lines 4 and 5 together equal to line 1z plus self-employment earnings; the credit cannot differ.
- Reason: The owner's decision (Stage 15, decision 6). Taxable benefits arise from one spouse's plan; the instructions give no rule for dividing a joint line 26, and the case where it matters (benefits over the exclusion with a credit still left) is rare, since excluded benefits of $5,000 leave at most $1,000 of the $6,000 limit.
- Status: Owner ruling, Stage 15 (T-048); the display of line 1e on line 4 in the undetermined case with no credit is an agent reading for the owner's review.
- Cite: [i2441] p. 4, Lines 4 and 5, "If filing jointly, figure your and your spouse's earned income separately" (2025; sha256 86f0669e)

## amb.2025.dc_line30

- Text at issue: Form 2441 line 30: "Complete line 2 on page 1 of this form. Don't include in column (d) any benefits shown on line 28 above. Then, add the amounts in column (d) and enter the total here"; the instructions give no rule for dividing line 28 among the qualifying persons.
- Candidate readings: Line 30 is the total of the qualified expenses incurred and paid in 2025 for all qualifying persons less line 28, and not less than zero; column (d) shows each person's expenses before excluding benefits. | Each person's column (d) is asked net of the benefits that paid for that person's care, and line 30 is their sum.
- **Chosen:** The first (f2441.line30; dependent.dc_paid and dependent.dc_line2d ask and show each person's expenses including those paid with dependent care benefits).
- Reason: The owner's decision (Stage 15, decision 6). The total is determined by the text and verifiable; an allocation of line 28 among persons is not. In Pub. 503's example (the Paris family, p. 13) the benefits covered one child's expenses and the total less the benefits is the line 30 the example uses ($19,500 less $1,000).
- Status: Owner ruling, Stage 15 (T-048).
- Cite: [f2441] Form 2441 (2025), line 30 (2025; created 2025-03-18; sha256 6c3c2d19)

## amb.2025.dc_plan_maximum

- Text at issue: Form 2441 line 21: "However, don't enter more than the maximum amount allowed under your dependent care plan"; i2441 p. 5, Line 21: "if your dependent care plan only allows a maximum of $4,000 to be excluded, substitute $4,000". The text speaks of one plan; spouses, or one person with two employers, may have more than one.
- Candidate readings: One plan maximum for the return (f2441.plan_max), the smaller of it and $5,000; refused when the plans allow different maximums. | The $5,000 limit, reduced only if every plan's maximum is lower. | The sum of the plans' maximums, not more than $5,000.
- **Chosen:** The first (f2441.plan_max, f2441.plans_differ).
- Reason: The owner's decision (Stage 15, decision 6). Where every plan allows the same maximum the readings agree; where they differ the text does not decide, so that case is refused.
- Status: Owner ruling, Stage 15 (T-048).
- Cite: [i2441] p. 5, Line 21, "Don't enter more than the maximum amount allowed under your dependent care plan" (2025; sha256 86f0669e)

## amb.2025.dc_rate_nonpositive_agi

- Text at issue: Form 2441, line 8: "Enter on line 8 the decimal amount shown below that applies to the amount on line 7", in a table whose first band is "Over $0 But not over 15,000".
- Candidate readings: Line 7 of zero or less takes the first band's .35. | Line 7 of zero or less has no decimal amount, and the credit is not figured.
- **Chosen:** The first (tables/2025/dc_rate.yaml, the first band open below).
- Reason: The owner's ruling. In this tool the readings cannot differ in the credit. Line 7 (adjusted gross income) of zero or less gives taxable income of zero and no tax on Form 1040 line 16, and Schedule 2 Part I (line 17) is zero here, the alternative minimum tax and the repayment of excess advance premium tax credit being refused (s2.amt and the Schedule 2 screen); so line 18 is zero, and the Credit Limit Worksheet's line 3 and line 10 are zero. A rate is still needed for line 8 to be known.
- Status: Owner ruling, Stage 15 (T-048).
- Cite: [f2441] Form 2441 (2025), line 8 (2025; created 2025-03-18; sha256 6c3c2d19)

## amb.2025.f5695_17abc_section_a

- Text at issue: Form 5695, after line 17c: "If you checked the No box for line 17a, 17b, or 17c, you cannot claim the energy efficient home improvement credit. Do not complete Part II, Section A." The instructions for lines 17a to 17c say each time "If you check the No box, you can't take the energy efficient home improvement credit."
- Candidate readings: A No on line 17a, 17b or 17c zeroes Section A (lines 18b, 19h and 20d) only; Section B and the home energy audit are figured by their own tests (lines 21a, 21b and 26a). | A No on any of them disallows the whole of Part II.
- **Chosen:** The first (f5695.sec_a_claimed gates lines 18b, 19h and 20d only).
- Reason: The owner's decision. Section B has its own residence test on line 21a, "a home located in the United States that you use as a residence", which is not limited to the main home, and its own original-use test on line 21b, and the audit has its own test on line 26a; the form's direction is "Do not complete Part II, Section A". Reading the No as disallowing Section B would make line 21a's wider residence test unreachable for anyone without Section A improvements on a main home.
- Status: Owner ruling, Stage 15 (T-048).
- Cite: [f5695] Form 5695 (2025), lines 17a to 17c and 21a; i5695 p. 5, Lines 17a Through 17e (2025; created 2025-03-20; sha256 e2ac6a5c)

## amb.2025.f5695_category_cap

- Text at issue: Form 5695 lines 22d, 23d, 24d and 25e cap 30% of each category's total cost at $600 ("Multiply line 22c by 30% (0.30). Enter the results. Do not enter more than $600"); the instructions list "A credit limit of $600 for any qualified energy property item" (i5695 p. 2).
- Candidate readings: The form's cap of $600 on each category (central air conditioners, water heaters, furnaces and boilers, enabling property), whatever the number of items in it. | A cap of $600 on each item, so that two central air conditioners could give up to $1,200 before line 28.
- **Chosen:** The first (f5695.ac_capped, wh_capped, furnace_capped and enabling_capped against f5695.item_max).
- Reason: The owner's decision to encode the form as printed. The joint occupancy list of credit limits (i5695 p. 3) also gives the limit by category ("$600 for central air conditioners"). The two readings differ only for a filer with two or more items in one category whose 30% exceeds $600 together, and line 28's $1,200 limit narrows even that.
- Status: Owner ruling, Stage 15 (T-048).
- Cite: [f5695] Form 5695 (2025), lines 22d, 23d, 24d and 25e; i5695 p. 2, Energy Efficient Home Improvement Credit (Part II), "A credit limit of $600 for any qualified energy property item" (2025; created 2025-03-20; sha256 e2ac6a5c)

## amb.2025.f5695_battery_second_home

- Text at issue: i5695 p. 2: lines 1 to 4 each say "The home doesn't have to be your main home"; qualified battery storage technology costs are for technology "installed in connection with your home located in the United States", with nothing said either way about a main home. Fuel cell property, by contrast, is for "your main home".
- Candidate readings: Battery storage technology on any home in the United States you used as a residence counts, as lines 1 to 4 do. | Battery storage technology counts only on the main home, as fuel cell property does.
- **Chosen:** The first (f5695.line5a asks for battery storage technology installed in connection with your home in the United States, not your main home).
- Reason: The owner's decision. The text names the main home where it means it (fuel cell property, line 7a) and does not for the battery; the Part I general rule is that improvements to "more than one home that you used as a residence" go on one Form 5695 (i5695 p. 2).
- Status: Owner ruling, Stage 15 (T-048).
- Cite: [i5695] p. 2, Qualified battery storage technology costs, "installed in connection with your home located in the United States" (2025; sha256 55113467)

## amb.2025.f5695_section_b_residence

- Text at issue: Form 5695 line 21a: "a home located in the United States that you use as a residence"; i5695 p. 3, Section B: "a home that you used during 2025"; but the Schedule 3 line 5b instructions describe the credit as for improvements "to your main home" (i1040gi p. 116) and line 17d says "You can only claim the energy efficient home improvement credit on one main home" (i5695 p. 5).
- Candidate readings: Section B property (lines 22 to 25 and 29) counts on any home in the United States you use as a residence, a second home or a rented home included; Section A and the audit require the main home. | All of Part II requires the main home.
- **Chosen:** The first (f5695.line21a's question says the home may be a second home or a home you rent).
- Reason: The owner's decision. Line 21a and the Section B paragraph state the wider test, line 21c asks for "each home", and Fact Sheet 2025-01 says "such property may be installed in the taxpayer’s second home" and that "the taxpayer may rent the home". The main-home statements are in Section A (lines 17a and 17d) and in a summary in the Form 1040 instructions.
- Status: Owner ruling, Stage 15 (T-048).
- Cite: [fs-2025-01] p. 5, Energy Efficient Home Improvement Credit - Qualifying residence, "In this case, the taxpayer may rent the home in which such property is installed, and such property may be installed in the taxpayer’s second home" (FS-2025-01, January 2025; sha256 8565a0b8)

## amb.2025.clwb_claiming_part1

- Text at issue: i1040s8812 p. 4, Credit Limit Worksheet A: "Complete Credit Limit Worksheet B only if you meet all the following. 1. You are claiming one or more of the following credits. ... c. Residential clean energy credit, Form 5695, Part I." Whether one is claiming the credit depends on Form 5695 line 15, which is limited by a worksheet that reads Credit Limit Worksheet B line 14 when Worksheet B is completed.
- Candidate readings: Claiming the credit means completing Form 5695 Part I with line 13 (the credit before the tax limit, the 2024 carryforward included) more than zero. | Claiming the credit means Form 5695 line 15 (the credit allowed) is more than zero.
- **Chosen:** The first (f5695.claiming_part1).
- Reason: The second is circular (line 15 depends on whether Worksheet B is completed). The readings cannot differ in any amount. With Worksheet B completed, the Part I limit subtracts Worksheet B line 14, which is never more than Schedule 8812 line 12, instead of Form 1040 line 19, the smaller of line 12 and Credit Limit Worksheet A line 3; so the limit with Worksheet B is at least the limit without it. If line 13 is more than zero and line 15 is zero with Worksheet B, it is zero without it too, and Credit Limit Worksheet A line 4 (Worksheet B line 15, Schedule 3 line 5a) is zero either way; if line 15 is more than zero, both readings complete Worksheet B.
- Status: Agent reading, Stage 15 (T-048), for the owner's review.
- Cite: [i1040s8812] p. 4, Credit Limit Worksheet A, "Complete Credit Limit Worksheet B only if you meet all the following" (2025; printed date 2026-01-23; sha256 bb9788cd)

## amb.2025.savers_ineligible_column

- Text at issue: Form 8880, Caution and Who Can Take This Credit: "You cannot take this credit if either of the following applies ... The person(s) who made the qualified contribution or elective deferral (a) was born after January 1, 2008; (b) is claimed as a dependent on someone else’s 2025 tax return; or (c) was a student".
- Candidate readings: On a joint return, an ineligible spouse's own column is zero (line 6 of that column), and the other spouse's column is figured as usual. | On a joint return, one ineligible spouse bars the whole credit.
- **Chosen:** The first (f8880.line6a and f8880.line6b through f8880.elig_a and f8880.elig_b).
- Reason: The owner's decision (Stage 15 premise map, decision 4). The test is of "the person(s) who made the qualified contribution or elective deferral", so it reads as a test of each contributor, and the form keeps each spouse's contributions in their own column. Whether a person is claimed as a dependent is asked of each person (person.sav_claimed), not read from the return's "can claim" question; it is asked only when someone can claim you or your spouse (sa.dependent), since otherwise no one is claimed.
- Status: Owner decision, Stage 15 (T-048).
- Cite: [f8880] p. 2, Who Can Take This Credit, "The person(s) who made the qualified contribution or elective deferral (a) was born after January 1, 2008; (b) is claimed as a dependent on someone else’s 2025 tax return; or (c) was a student" (2025; created 2025-11-04; sha256 ba2b2877)

## amb.2025.savers_line4_gross

- Text at issue: Form 8880, Line 4: "Enter the total amount of distributions you, and your spouse if filing jointly, received after 2022 and before the due date of your 2025 return (including extensions) from any of the following types of plans", followed by a list of distributions not to include.
- Candidate readings: The gross distribution (Form 1099-R box 1) less the part rolled over, the listed kinds excluded; a nontaxable part (basis recovered, a qualified Roth distribution) counts. | The taxable amount of each distribution.
- **Chosen:** The first (retirement.sav_gross; f8880.line4a and f8880.line4b).
- Reason: The owner's decision (Stage 15 premise map, decision 4). The text says "total amount of distributions" and excludes only the kinds it lists; a rollover is excluded because it is "not taxable as the result of a rollover", and the other exclusions it lists either need a form this tool refuses (retirement.special, retirement.bad_code) or are asked for each Form 1099-R (retirement.sav_military, retirement.sav_404k, retirement.sav_inherited).
- Status: Owner decision, Stage 15 (T-048).
- Cite: [f8880] p. 2, Line 4, "Enter the total amount of distributions"; "Don’t include any of the following" (2025; created 2025-11-04; sha256 ba2b2877)

## amb.2025.savers_2026_joint

- Text at issue: Form 8880, Line 4: "Exception. Don’t include your spouse’s distributions with yours when entering an amount on line 4 if you and your spouse didn’t file a joint return for the year the distribution was received." A distribution received in 2026, before the due date of the 2025 return, is received in a year whose return is not yet filed.
- Candidate readings: A 2026 distribution counts as from a year filed jointly when the 2025 return is joint (both columns). | A 2026 distribution counts as from a year filed jointly only if the spouses expect to file jointly for 2026. | A 2026 distribution goes in the column of the spouse who received it only.
- **Chosen:** The first (person.sav_prior_joint includes 2026; f8880.prior_joint).
- Reason: The owner's decision (Stage 15 premise map, decision 4). The 2026 return cannot be known when the 2025 return is prepared, and the 2025 return's filing status is the one fact available.
- Status: Owner decision, Stage 15 (T-048).
- Cite: [f8880] p. 2, Line 4, "Exception. Don’t include your spouse’s distributions with yours when entering an amount on line 4 if you and your spouse didn’t file a joint return for the year the distribution was received" (2025; created 2025-11-04; sha256 ba2b2877)

## amb.2025.savers_inherited_plans

- Text at issue: Form 8880, Line 4, among the distributions not to include: "Distributions from an inherited IRA by a nonspousal beneficiary." The list names no inherited employer plan.
- Candidate readings: Only an inherited IRA of a nonspouse beneficiary is excluded; distributions from an inherited 401(k), 403(b) or other plan count. | Distributions to a nonspouse beneficiary from any inherited plan are excluded.
- **Chosen:** The first (retirement.sav_inherited is asked of IRA distributions only).
- Reason: The owner's decision (Stage 15 premise map, decision 4), the literal reading of the list.
- Status: Owner decision, Stage 15 (T-048).
- Cite: [f8880] p. 2, Line 4, "Distributions from an inherited IRA by a nonspousal beneficiary" (2025; created 2025-11-04; sha256 ba2b2877)

## amb.2025.savers_sep_contrib

- Text at issue: Form 8880, Line 2: "Elective deferrals (including designated Roth contributions under section 402A, if applicable) to a 401(k), 403(b), governmental 457(b), SEP, SIMPLE, or the federal TSP." A self-employed person's own SEP contribution (Pub. 560 chapter 2) is an employer contribution, not an elective deferral; the person's SIMPLE IRA salary reduction contributions (chapter 3) are.
- Candidate readings: The self-employed SIMPLE salary reduction contributions (person.simple_deferral) count on line 2; the self-employed SEP contribution (person.sep_contrib) does not. | Both count. | Neither counts.
- **Chosen:** The first (person.sav_simple_plan).
- Reason: The owner's decision (Stage 15 premise map, decision 2). Only elective deferrals to a SEP (code F, a salary reduction SEP) are named; a SEP contribution a self-employed person makes for themselves is a nonelective contribution.
- Status: Owner decision, Stage 15 (T-048).
- Cite: [f8880] p. 2, Line 2, "Elective deferrals (including designated Roth contributions under section 402A, if applicable) to a 401(k), 403(b), governmental 457(b), SEP, SIMPLE, or the federal TSP" (2025; created 2025-11-04; sha256 ba2b2877)
