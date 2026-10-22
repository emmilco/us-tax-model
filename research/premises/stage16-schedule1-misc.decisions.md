# Stage 16 (the remaining Schedule 1 items): decision batch for the owner

Prepared from `stage16-schedule1-misc.md` (the premise map) and `stage16-schedule1-misc.verification.md` (its
adversarial check), after Stage 15. Where the two differ, the verification's checked facts are used; the corrections are
noted against the items they change. Each item gives the recommendation first, then the alternative.

Coverage (estimator after Stage 15, `reports/2025/filer_coverage.md`): 64.7% now; the whole Schedule 1 group would take it
to 72.4% (+7.7). By share: other income 4.85% of returns, taxable state refund 1.94%, IRA deduction 1.56%, gambling
1.44%, Form 4797 1.07%, NOL 0.63%, early withdrawal penalty 0.56%, taxable HSA distributions 0.29%, foreign earned income
exclusion 0.27%, canceled debt 0.24%, alimony paid 0.17%, received 0.11%. The map's absolute figures are about 0.6 points
high (written before Stage 15); the ranking is unchanged.

**D1. Scope.** Compute: other income (a named subset, D3), the taxable state or local refund, the IRA deduction (with
Form 8606 Part I for nondeductible contributions when there is no distribution), gambling winnings (losses on Schedule A
line 16), the early withdrawal penalty, alimony (pre-2019 agreements), taxable HSA distributions, and fully taxable
canceled nonbusiness debt. Leave refused: Form 4797 (sales of business property), the net operating loss deduction, and
the foreign earned income exclusion, each of which needs a form that is not archived and reaches the business or foreign
paths. / Compute only the four largest (other income, refund, IRA, gambling).

**D2. The four small ones** (early withdrawal penalty, alimony, HSA distributions, canceled debt): compute each, each a
few lines on existing structure. / Refuse any of them by name. *Correction:* a penalty reported on Form 1099-OID is not
caught by any existing screen (the Schedule B screen refuses only OID *not* on a Form 1099-OID), so line 18 gets its own
input or screen for it.

**D3. Which lines of Schedule 1 line 8:** 8b (gambling), 8c (canceled debt), 8f (HSA, Part II only), 8g (Alaska
Permanent Fund dividends), 8h (jury duty pay, with line 24a when given to the employer), 8i (prizes and awards), 8j
(activity not for profit), 8r (scholarships not on a W-2) and a closed list for 8z; the rest of line 8 stays refused. /
Smaller: 8b, 8g, 8h and 8i only. *Correction:* line 25 (jury duty given to the employer) then also enters the IRA
worksheet line 4, the student loan interest worksheet line 3 and the social security worksheet line 6, as all three
printed lines include it.

**D4. Line 8z "List type and amount"** (the project has no text values): a collection of 8z entries keyed by a kind from
a fixed list (the values sheet shows the kind's name). / One total with a notice that you write the type on the form.

**D5. Taxable state refund:** compute the Form 1040 instructions' worksheet only; a refund is not taxable at all when you
did not itemize in 2024 or deducted sales tax rather than income tax; refuse the nine Pub. 525 exceptions, refunds of
taxes other than income tax, and other recoveries. / Also encode Pub. 525 Worksheets 2 and 2a.

**D6. Three readings in the refund worksheet:** (a) cap line 1 at 2024 Schedule A line 5d as printed (the total of the
taxes), not at the income-tax part; (b) ask the amount reported on 2024 line 5d; (c) ask the four 2024 checkbox facts
(born before 1960, blind, for you and your 2024 spouse) as four yes/no questions, since a 2024 spouse may not be the
2025 one. / (a) cap at line 5a; (c) one count of boxes.

**D7. Social security and the IRA deduction.** A return with social security benefits, a traditional IRA contribution
and plan coverage is already refused today (`ssb.pub915`, which sends it to Pub. 590-A). Keep that refusal as it is, and
break the static line cycle (the IRA worksheet reads Form 1040 line 9, which includes taxable social security, whose
worksheet reads Schedule 1 line 20) by giving the social security worksheet its own copy of the IRA deduction's terms.
*Correction:* the map proposed a new refusal; one exists. / Derive that refusal from the new contribution and coverage
answers instead of the filer's own answer.

**D8. IRA situations to refuse:** contributions to both a traditional and a Roth IRA on a joint return by either spouse
(the broad reading); a joint return with modified compensation under the printed floors; excess contributions this year
or an earlier excess still in the IRA (see D10); W-2 box 11 or code Z amounts; recharacterizations and the other Pub.
590-A special cases; nondeductible contributions together with a 2025 distribution or conversion; a non-W-2 fellowship
counted as compensation; and nontaxable combat pay, which needs its own refusal on the IRA lines (*correction:* today it
is refused only on the Schedule 8812, EIC and Form 2441 paths). Compute the maximum deduction and refuse the election to
deduct less. / Narrow the both-kinds rule to one person's own contributions; take box 11 and code Z as W-2 inputs (now
cheap: box 12 is modelled since Stage 15); take an input for the amount you choose to deduct.

**D9. IRA readings:** (a) ask "age 50 or older at the end of 2025" directly; (b) coverage by a work plan as one question
per person, with W-2 box 13 named in the help, plus the existing SEP or SIMPLE plan answer for the self-employed;
(c) a self-employment loss of one spouse does not reduce the other's compensation (Pub. 590-A), so floor per person. /
(a) a birth-date cut; (b) a box 13 input per W-2; (c) floor the couple's total, as the worksheet prints it.

**D10. The saver's credit.** Lift Stage 15's refusal of traditional IRA contributions on Form 8880 and count them (deductible
or not) on line 1, with one excess-contribution screen shared by traditional and Roth contributions. This also answers
Stage 15 question 4 (no screen today asks about excess Roth contributions). / Leave Form 8880 as built: anyone who takes
the IRA deduction and claims the saver's credit stays refused, and the estimator would not show it.

**D11. Coverage bookkeeping.** Mark each computed category not refused (`"refused": false`, as Stage 15 did; *correction:*
emptying its gates alone leaves it counted as refused), and keep "other income" refused with a note that part of it is now
computed, since the estimate cannot measure which part. / Mark "other income" covered (overstates).

**D12. Lines with no number** (2b the agreement date, 19b the recipient's SSN, 19c the date): a notice on the values sheet
that you write them on the form; nothing asked. / Ask and show them.

**D13. HSA distributions partly subject to the 20% tax** (for example, turning 65 during the year): an input for the part
subject to the tax. / Refuse a partial exception.

**D14. Gambling:** losses on Schedule A line 16, capped at the winnings, when you itemize; professional gamblers refused. /
Compute winnings only and keep gambling losses refused.

Structure-changing items: D1, D7, D8, D10. Everything else is a reading or a small screen.
