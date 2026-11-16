# Completeness review, release rerun (xrr, family rcred): adjudication of 11 claims

Ruled by the rcred fork (claude-opus-5-5, judgment). These are the new samples (one per form, Claude only) of the three
family forms whose subject changed in the xint integration: f2441, f8582 and f8853c. Each quote was checked against
`sources/2025/*.txt`, the form YAML, the rendered English and the interview wording (`interview/2025/questions.yaml`);
the Form 8582 MFS case was evaluated on copies of `x1sche.f2.small_loss_exception` under `/tmp/xrr/rcred/`. The earlier
rulings of the same units (xrel, r9) were used as leads and rechecked against the current lines. Fragment:
`/tmp/xrr/frag/rcred.completeness.json`; `xrr.py merge` (validate only) prints no REFUSED line. `rulings.json` was not edited.

## Counts

| Form | Claims | Real gap | Covered | Out of scope | Presentation | Wrong |
|---|---|---|---|---|---|---|
| f2441 | 4 | 0 | 2 | 2 | 0 | 0 |
| f8582 | 5 | 2 | 0 | 3 | 0 | 0 |
| f8853c | 2 | 2 | 0 | 0 | 0 | 0 |
| total | 11 | 4 | 2 | 5 | 0 | 0 |

Real gaps: f8582#1.1 and #1.2 cite the existing BUG-0836 (unfixed); f8853c#1.2 cites the existing BUG-0916; f8853c#1.1
cites the pending BUG-0923, which fails the gate until the numbered-bug pass.

## f2441

| claim | class | line / gate / bug | evidence |
|---|---|---|---|
| f2441#1.1 | covered | dependent.dc_paid | Column (d) is dependent.dc_paid, asked per qualifying person; its prompt states every rule listed (child support, state agency reimbursement, chauffeur/gardener, food and schooling, kindergarten and up, camp/summer school/tutoring, medical expenses, the 8-hour rule, care center rules, days of work, partly work-related costs, employment taxes, housekeeper's meals); the turning-13 case is asked by dc_under13 and dc_over12_care. The reviewer saw only the f2441 lines. |
| f2441#1.2 | out of scope | f2441.student_disabled | A spouse is never a qualifying person: f2441.unable's help, "Answer Yes too if some of the care you paid for was for your husband or wife. A Yes ends the interview here", feeds the refusal on lines 4, 5, 18 and 19 ("a disabled spouse as a qualifying person"). Dependents are tested by dependent.dc_lived_half. |
| f2441#1.3 | out of scope | dependent.claimed_no_tin | A qualifying person must be a dependent (dc_qp requires dependent.claimed); a dependent with no SSN, ITIN or ATIN, including the "Died" case, is refused. Column (c) is encoded (dependent.dc_line2c). |
| f2441#1.4 | covered | dcprov.tin_kind | The enum has tin, tax_exempt ("Tax-Exempt"), lafcp ("LAFCP"), see_statement and employer. The "none" entry on line 1 column (a) is a name column the dcprov note leaves to the filer; no amount. |

## f8582

| claim | class | line / gate / bug | evidence |
|---|---|---|---|
| f8582#1.1 | real gap | BUG-0836 | The $12,500/$50,000 MFS limits are applied, but living apart is not tested. Rechecked: MFS with mfs_living together_late and with apart_all_year give the same result (exception true, line 9 $213.20, s1.line5 -$213.20), no refusal. Passive credits, limited-partner and estate or trust interests are refused (s3.prior_forms_if_forms, k1p.r_b15, k1s.box13_other, scope.k1). |
| f8582#1.2 | real gap | BUG-0836 | Part V for an MFS filer who lived with the spouse: rental.part4 is active participation alone and lines 5 to 9 ignore household.mfs_living (same witness). Less than 10% is refused (rental.under_tenth), limited partners by scope.k1. |
| f8582#1.3 | out of scope | sche.re_pro | Real estate professional (sche.re_pro), section 280A(c)(5) home (rental.ws51), stays of 7 days or less (rental.stay7_if_short), significant or extraordinary services (rental.services) are all refused; incidental rentals are rare for Schedule E Part I and not filed. |
| f8582#1.4 | out of scope | sb.unsupported_if_income | s1.line25 is line 24a only (24b to 24z refused by scope.schedule1; W-2 code H by scope.w2_marks_if_w2), so no 501(c)(18) amount reaches MAGI; Form 8815 by sb.unsupported_if_income; adoption benefits by scope.adoption_benefits; real estate professional by sche.re_pro. |
| f8582#1.5 | out of scope |  | A prior-year unallowed CRD can come only from a pre-2010 building; the f8582.line3 note says it is not asked. Not refused; extremely rare, not filed (as the xrel ruling of this unit). |

## f8853c

| claim | class | line / gate / bug | evidence |
|---|---|---|---|
| f8853c#1.1 | real gap | BUG-0923 | Line 17 follows box 1 of the Forms 1099-LTC, as its instruction says. But the entry question s1.ltc_payout asks "were you ... paid by a long-term care insurance policy", and nothing tells a policyholder that per diem payments assigned to the care provider count (i8853 p. 8, "even if payment is assigned to a third party"). Such a filer can answer No and skip Section C. Low: line 26 changes only where the per diem exceeds both $420 a day and the costs less reimbursements. |
| f8853c#1.2 | real gap | BUG-0916 | The certification is carried by the payments: a qualified contract pays only for a chronically ill insured, and nonqualified contracts are refused. What is missing is "required to treat a chronically ill individual" in the line 22 source (BUG-0916, low). The interview prompt ("What did this person's long-term care cost during those days?") leaves it out too, and BUG-0916's proposed fix covers only the form source. **Lead: extend BUG-0916 to the interview prompt of f8853c.line22.** |

## Pending bugs filed

- BUG-0923 (low): f8853c: the entry question and line 17 do not say that the policyholder reports per diem
  payments assigned to a care provider. Proposed fix: add help text to s1.ltc_payout and f8853c.line17 counting payments
  made straight to a care provider and any Form 1099-LTC sent to the policyholder.
