# Screen and false-no adjudication, xrel family inc (2026-11-15)

Brief: `/tmp/xrel/brief.inc.md` (lane xrel, sampled release reviews, B1 plus expansion tree `.claude/worktrees/xint`).
Family `inc`: forms `s1`, `sa`, `oi8z`, `w2`, `tipjob`, `otjob`, `f4137`, `f4137row`, `f8919`, `f8919firm`. The rulings are in
`/tmp/xrel/frag/inc.screens.json` and `/tmp/xrel/frag/inc.false_no.json` (keys `unruled:<unit>#1`, each with the item's
current `subject_sha`); the lead merges them. `xrel.py merge` (no `--write`) refuses none. `w2.box12_userra#1` already
carried a ruling and is not repeated. The work was split into four judgment lanes (claude-opus-5-5) by gate; each finding
was checked against the interview wording (`interview/2025/questions.yaml`), the lines (`forms/2025/*.yaml`) and the
archived source (`sources/2025/*.cols.txt`); earlier rulings were leads only.

A general point: the review prompts show the form YAML source or helper label, not the interview prompt the filer
reads. Where those differ, the findings were ruled against the interview wording; several "model error" and
"covered" rulings rest on that difference, and some defects (BUG-0810, -09) are in the interview wording only.

## Counts

Screens: 28 samples, 86 findings: defect 24, covered 24, accepted WIDE 20, model error 8, out of scope 7, presentation 3.

False-no: 28 samples, 149 findings: presentation 50, defect 47, covered 28, model error 11, out of scope 11, accepted WIDE 1, open residual 1.

## Defects (pending entries in `bug_pending/`)

| id | severity | title |
| --- | --- | --- |
| BUG-0802 | low | Schedule A: the generation-skipping tax deduction on line 6 is neither asked nor refused |
| BUG-0804 | low | Line 8z damages: medical care for non-physical emotional distress and pre-September-14-1995 agreements are neither asked nor refused |
| BUG-0805 | medium | Schedule A: the other-use question asks 'improving' where the rule is 'substantially improve' |
| BUG-0806 | medium | Tips deduction: tipjob.listed reads as 'is all of the work on the list', so a mixed-occupation employee answers No |
| BUG-0807 | low | Schedule A: a home bought on a land contract is not named as owned, so line 5b and the seller-financed interest refusal can be skipped |
| BUG-0808 | medium | The winnings gate asks what was won in 2025, not what was received: lottery installments, sales of lottery rights and late-paid prizes are missed |
| BUG-0809 | low | The professional-gambler screen asks whether gambling is 'the way a living is made', narrower than a trade or business |
| BUG-0810 | medium | The canceled-debt screen as asked drops student loans, gifts, seller price reductions, stockholder debts and most Form 982 exclusions |
| BUG-0811 | low | Alimony wording: the gate leaves out payments for the spouse and unallocated support, and the amount questions lost 'cash payments only' and the non-alimony parts |
| BUG-0812 | low | Net operating loss questions miss a joint carryback year, and scope.nol does not name an excess business loss carried forward |
| BUG-0813 | low | The unemployment gate's help points to the form, not the payment |
| BUG-0814 | low | The Alaska dividend gate has no help: a garnished or redirected dividend reads as not received |
| BUG-0815 | medium | Schedule A: the other-state-tax gate does not name a prior-year refund applied to 2025, or withholding from income other than a pension, unemployment or winnings |
| BUG-0816 | low | Schedule A: the personal property tax gate's help says a weight-based fee does not count, missing the value-based part of a mixed fee |
| BUG-0817 | medium | Schedule A: a filer with 2025 gifts and an earlier year's carryover is led to answer sa.charity_limited No |
| BUG-0818 | low | Charitable property: gift.deduction's wording omits the reductions for capital gain property and the rule on the right to use property |
| BUG-0819 | low | Schedule A: medical costs an estate pays after death for the decedent's final return are not reached by the medical gate |
| BUG-0820 | low | Schedule A: sa.spouse_extra's wording omits the definition of blind and a spouse who died after 65, in a three-part conjunction |
| BUG-0821 | low | s2.lookback asks only about a long-term contract finished in 2025; look-back interest for a contract adjusted in 2025 is missed |
| BUG-0822 | medium | s1.hobby_any asks whether the filer 'made money' from a hobby; a hobby that lost money, or paid in kind, reads as No and its receipts are dropped from line 8j |
| BUG-0823 | low | s1.inmate_wages asks about work done 'while in a jail or prison'; an inmate on work release or in another correctional facility can answer No |
| BUG-0824 | low | s1.jury_any asks whether the filer was 'paid for serving on a jury'; a juror paid for days in the jury pool but never seated can answer No |
| BUG-0825 | low | s1.scholarship_any asks about 'a scholarship, a fellowship or a grant for study'; a research fellowship or a stipend paid to the filer can read as No |
| BUG-0826 | low | s2.options_any asks only about stock options 'from an employer'; options exercised by a director, contractor, heir or former spouse never reach line 8k |

PROPOSED-L3-1 (GST on Schedule A line 6) is BUG-0802, and PROPOSED-L4-3 (taxable damages) is BUG-0804,
both filed from the completeness review (`reviews/2025/completeness/r9-xrel-inc.findings.md`).
`gate:s1.digital_income_if_assets` findings 0 and 2 cite the existing BUG-0896.

## s1, part A (alimony, cancelled debt, gambling, NOL, unemployment, Alaska, digital assets)

Screens, findings 26: accepted WIDE 7, covered 4, model error 6, presentation 1, defect 8.
False-no, findings 41: defect 22, presentation 9, model error 6, covered 3, out of scope 1.

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| `s1.alimony_unsupported` | 0: accepted WIDE; 1: accepted WIDE; 2: defect (L1-4) | The redraft's amount questions lost 'cash payments only' and the p504 p. 13 non-alimony parts. Low. |
| `s1.cod_unsupported` | 0: covered; 1: presentation; 2: model error | Findings answered by the asked wording. A gap outside the findings: the asked prompt drops student loans, gifts, price reductions, stockholder debts and most Form 982 exclusions (L1-3, medium). |
| `s1.gambling_pro` | 0: covered; 1: defect (L1-2) | Asked as 'the way a living is made', narrower than a trade or business. Low. |
| `s1.nol_pre2018` | 0: covered; 1: covered | The 80% limit is refused at f1040.line15 by s1.nol_limit. No defect. |
| `s1.uc_unsupported` | 0: model error; 1: accepted WIDE | Reached only when unemployment benefits were paid (s1.line7 guard s1.has_uc). No defect. |
| `gate:s1.alimony_any` | 0: defect (L1-4); 1: accepted WIDE; 2: accepted WIDE | 'support paid to a husband or wife' leaves out payments made for the spouse. Low. |
| `gate:s1.has_gambling` | 0: model error; 1: model error; 2: model error; 3: defect (L1-2) | The asked s1.gambling_winnings has no business exclusion and names the spouse; finding 3 is the gambling_pro wording. |
| `gate:s1.nol_separate` | 0: model error; 1: accepted WIDE | The remarried joint filer is caught by s1.nol_joint and s1.nol_not_married. No defect. |
| `gate:s1.winnings_any` | 0 to 3: defect (L1-1); 4: accepted WIDE | Gate keyed to winning in 2025, not receipt. Medium. |

False-no, findings 41.

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| `gate:s1.alaska_any` | 0: presentation; 1: defect (L1-7); 2: defect (L1-7); 3: covered | No help; a garnished or redirected dividend reads as not received. Low. |
| `gate:s1.alimony_any` | 0: defect (L1-4); 1: defect (L1-4); 2: presentation; 3: presentation | Third-party payments and unallocated support. Low. |
| `gate:s1.digital_income_if_assets` | 0: defect (BUG-0896); 1: model error; 2: defect (BUG-0896); 3: model error; 4: presentation; 5: presentation | Airdrops and the closed list already pending as BUG-0896. |
| `gate:s1.has_gambling` | 0: model error; 1: model error; 2: covered; 3: covered; 4: defect (L1-1) | No gate defect; finding 4 rides with the winnings gate. |
| `gate:s1.nol_joint` | 0: model error; 1: defect (L1-5); 2: presentation; 3: out of scope (scope.k1); 4: presentation | Non-joint filers are caught by s1.nol_separate / s1.nol_was_joint. |
| `gate:s1.nol_separate` | 0: defect (L1-5); 1: model error; 2: defect (L1-5); 3: presentation | A joint carryback year is not named. Low. |
| `gate:s1.uc_any` | 0: defect (L1-6); 1: presentation; 2: defect (L1-6); 3: defect (L1-6); 4: defect (L1-6) | Help points to the form, not the payment. Low. |
| `gate:s1.winnings_any` | 0 to 7: defect (L1-1) | Won vs received; plus losing year, recognition awards, prize points, sweepstakes. Medium. |

Proposed defects:
- BUG-0808 (medium): s1.winnings_any keyed to winning, not receipt (lottery installments, sale of lottery rights, late-paid prizes).
- BUG-0809 (low): s1.gambling_pro asked as 'the way a living is made'.
- BUG-0810 (medium): s1.cod_unsupported asked wording drops student loans and other exceptions/exclusions.
- BUG-0811 (low): alimony gate and amount wording.
- BUG-0812 (low): NOL marital questions miss carryback years; scope.nol help omits excess business loss.
- BUG-0813 (low): s1.uc_any help.
- BUG-0814 (low): s1.alaska_any help.
- Cited existing: BUG-0896 (digital asset airdrops).

Systemic note: the screen review prompts show the form-line `source` wording, not the interview prompt in
`interview/2025/questions.yaml`. For s1.cod_unsupported and s1.gambling_pro the asked wording differs materially, so
the screen review did not test what the filer reads.

## s1, part B (self-employment, hobby, inmate, jury, scholarship, stock options)

Screens: 6 samples, 20 findings. False-no: 7 samples, 39 findings.

### Screens

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| `gate:s1.has_sc` | 0: out of scope; 1: out of scope; 2: out of scope; 3: out of scope; 4: out of scope; 5: out of scope; 6: defect | Low defect BUG-0821 (look-back interest for a contract adjusted, not finished, in 2025). Every no-Schedule-C case is refused earlier: scope.k1, scope.farm, scope.rent_personal, royalty.business (working interest, own writing), sche.qbi_business (a rental never carries QBI). |
| `gate:s1.hobby_any` | 0: defect; 1: out of scope; 2: covered; 3: defect | Medium defect BUG-0822 ('make money' reads as net profit; a loss-making or in-kind hobby drops its receipts). Recreational farm refused by scope.farm; a hobby run as a business reaches sc.special. |
| `gate:s1.inmate_wages` | 0: defect; 1: defect | Low defect BUG-0823 (place wording 'in a jail or prison' against the status test 'an inmate in a penal institution'). |
| `gate:s1.jury_any` | 0: defect | Low defect BUG-0824 (jury-pool fees, 'serving on a jury'). |
| `gate:s1.scholarship_any` | 0: defect; 1: accepted WIDE; 2: accepted WIDE | Low defect BUG-0825 ('a grant for study', Pell-only help). |
| `gate:s1.stock_options_if_options` | 0: defect; 1: covered; 2: model error | Low defect BUG-0826 ('from an employer'). The interview prompt of s2.options_any covers a 2025 sale of shares bought earlier ('or sell shares bought that way'; ESPP help); the reviewer saw the narrower form label. |

### False-no

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| `gate:s1.has_sc` | 0: out of scope; 1: out of scope; 2: out of scope; 3: presentation; 4: out of scope; 5: out of scope; 6: out of scope; 7: defect; 8: out of scope; 9: accepted WIDE; 10: out of scope | Low defect BUG-0821. Rental car costs refused by rental.vehicle; K-1, farm, vessel rental, working interest refused; Schedule J is an election (a No gives a correct return). |
| `gate:s1.has_jury_pay` | 0: out of scope; 1: covered; 2: presentation | No gate defect, as the earlier ruling (owner-approved C gate on line 8h; a 2024 inclusion repaid in 2025 is p525 p. 36 Repayments, the owner's open question). |
| `gate:s1.hobby_any` | 0: defect; 1: defect; 2: out of scope; 3: covered | Medium defect BUG-0822. |
| `gate:s1.inmate_wages` | 0: defect; 1: defect; 2: presentation; 3: defect; 4: model error | Low defect BUG-0823 (W-2 pay of a work-release inmate stays on line 1a as EIC earned income; 1099 pay is dropped). Related: BUG-0893 (W-2 box 1 counted twice). |
| `gate:s1.jury_any` | 0: defect; 1: presentation; 2: presentation; 3: presentation; 4: presentation | Low defect BUG-0824. |
| `gate:s1.scholarship_any` | 0: defect; 1: defect; 2: presentation; 3: presentation; 4: presentation | Low defect BUG-0825. |
| `gate:s1.stock_options_if_options` | 0: covered; 1: defect; 2: defect; 3: defect; 4: covered; 5: presentation | Low defect BUG-0826 (heir, former spouse; a director's income is normally Schedule C). |

### Proposed defects (in L2.bugs.json)

- BUG-0821 (low): s2.lookback asks only about a contract finished in 2025; add "or have the price or costs changed in 2025 on".
- BUG-0822 (medium): s1.hobby_any "make money" reads as net profit; ask "receive any money, goods or other payment ... even if it cost you more than it brought in".
- BUG-0823 (low): s1.inmate_wages "while in a jail or prison"; ask "while serving time as an inmate, in a jail, prison or other correctional facility, including work release"; help on credited or withheld pay.
- BUG-0824 (low): s1.jury_any "paid for serving on a jury"; ask "any pay for jury duty, including days you reported for jury selection and were not chosen, and pay you gave to your employer".
- BUG-0825 (low): s1.scholarship_any "a grant for study"; ask "for study or research, that is not on a W-2" and name stipends and living allowances in the help.
- BUG-0826 (low): s2.options_any "from an employer"; name options given for work by a company the filer served, and options inherited or received in a divorce.

## sa, part A (charity, medical, state and local taxes, MFS)

Read against the interview prompts in `interview/2025/questions.yaml`. A computed gate's review prompt shows the members' helper labels, and a screen's review prompt shows the form's `source`, so several findings were made against wording the filer never sees (for example "money already taxed" and "as a bona fide resident").

### Screens

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| `sa.charity_limited` | 0: defect (GST part; foreign tax covered); 1: covered; 2: covered; 3: covered; 4: presentation | GST on line 6 is no longer screened: when `sa.unsupported` was split into separate questions, the GST item named by BUG-0005 was dropped (BUG-0802). Mortgage interest not on Form 1098 and the line 16 items are screened by `sa.unsupported`. |
| `sa.excluded_income` | 0: covered | The interview prompt has no bona fide residence condition, so the year-of-move filer answers Yes. BUG-0458 remains open for the form source text. |
| `sa.spouse_extra` | 0: accepted WIDE | Over-refusal only, for a spouse born in 1960 who died before 65. |
| `gate:sa.gifts` | 0: covered | A carryover with no 2025 gifts is asked by `sa.gift_carryover`, and a Yes refuses line 13. |
| `gate:sa.medical_asked` | 0: presentation; 1: covered; 2: covered; 3: accepted WIDE; 4: accepted WIDE | `sa.medical_premiums` asks about self-paid insurance, names Medicare, and has no "already taxed" condition. |
| `gate:sa.personal_property_tax_any` | 0: defect; 1: covered; 2: accepted WIDE; 3: accepted WIDE | The gate's help excludes a fee based partly on weight (BUG-0816). A safe-harbor credit reaches line 5a through `sa.state_tax_other`. |
| `gate:sa.state_tax_other_any` | 0: defect; 1: defect | The gate does not name a credited prior-year refund or withholding on a 1099-NEC, 1099-MISC or IRA distribution (BUG-0815). |

### False-no

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| `gate:sa.gifts` | 0: covered; 1: defect; 2: defect; 3: covered | A carryover read through `sa.charity_limited`'s "any of them" and its 20% parenthetical (BUG-0817). Capital-gain-property reductions are missing from `gift.deduction` (BUG-0818). K-1 contributions are refused by `k1p.r_b13` and the k1s box 12 question. |
| `gate:sa.medical_asked` | 0: covered; 1: presentation; 2: defect; 3: presentation; 4: presentation; 5: presentation; 6: covered; 7: model error | Estate payments for a decedent's final return (BUG-0819). |
| `gate:sa.mfs_spouse_not_itemizing` | 0: presentation; 1: defect; 2: defect; 3: defect | `sa.spouse_extra` wording: the definition of blind, the double negative, a spouse who died after 65 (BUG-0820). |
| `gate:sa.personal_property_tax_any` | 0: covered; 1: defect; 2-5: presentation | BUG-0816. |
| `gate:sa.state_tax_any` | 0: covered; 1: covered; 2: presentation | No gate defect. Other withholding and state fund contributions are asked by the sibling `sa.state_tax_other_any` and summed in `sa.line5a_total`. |
| `gate:sa.state_tax_other_any` | 0: defect; 1: presentation; 2: presentation; 3: defect; 4: presentation; 5: presentation; 6: presentation | BUG-0815. |

### Proposed defects (in L3.bugs.json)
- BUG-0802 (low): GST deduction on line 6 neither asked nor refused. This is a regression of BUG-0005 from the landing-tree split of `sa.unsupported`, and it overlaps completeness sa#1.2.
- BUG-0815 (medium): the `sa.state_tax_other_any` gate omits a credited prior-year refund and non-pension withholding.
- BUG-0816 (low): the `sa.personal_property_tax_any` help says a weight-based fee does not count, so the value-based part of a mixed fee is dropped.
- BUG-0817 (medium): a carryover alongside 2025 gifts is asked only inside `sa.charity_limited`, whose wording invites a No.
- BUG-0818 (low): `gift.deduction` omits the capital-gain-property reductions (private nonoperating foundation, unrelated use) and the right-to-use rule.
- BUG-0819 (low): the medical gate does not reach estate payments for a final return.
- BUG-0820 (low): `sa.spouse_extra` wording.

## sa, part B (mortgage, property tax), oi8z, tipjob

Screens: 6 samples, 21 findings: covered 10, accepted WIDE 6, defect 4, model error 1.
False-no: 7 samples, 37 findings: presentation 15, covered 14, defect 4, model error 3, open residual 1.

Common ground for the mortgage gates: lines 8b and 8c are fixed at zero; `sa.mortgage_unreported` (interest or points no
Form 1098 in the filer's name shows, seller-financed or a co-borrower's Form 1098) is asked of every filer with
`sa.home_asked`, independent of line 8a, and a Yes refuses through `sa.unsupported` (checked by eval on a copy of an
eic.json case: the "Schedule A unsupported item" refusal). So gating the limit questions on line 8a drops nothing.

| unit | findings (n: class) | disposition |
| --- | --- | --- |
| screens `gate:sa.has_mortgage_interest` | 0: covered; 1: model error; 2: defect BUG-0805; 3: accepted WIDE | Defect: the other-use prompt says "improving", not "substantially improving". Line 8a holds the Form 1098 amount, not the limited one. |
| screens `gate:sa.mortgage_interest_mfs` | 0: covered; 1: covered; 2: accepted WIDE | No gate defect; line 8b interest refused by sa.mortgage_unreported. |
| screens `gate:sa.mortgage_interest_not_mfs` | 0: covered; 1: accepted WIDE | No gate defect. |
| screens `gate:sa.property_tax_other_if_home` | 0: covered; 1: covered; 2: covered; 3: covered; 4: accepted WIDE | No gate defect; the line 5b amount question excludes business real estate, tax not paid in 2025 and unremitted escrow; the list names a special tax on some properties. |
| screens `oi8z.injury` | 0: covered; 1: defect BUG-0804; 2: defect BUG-0804; 3: covered; 4: accepted WIDE | Low defect: medical care for non-physical emotional distress and pre-September-1995 agreements neither asked nor refused (overlaps completeness oi8z#1.1). Property-damage recoveries screened by sd.other_forms. |
| screens `gate:tipjob.listed` | 0: defect BUG-0806; 1: accepted WIDE | Medium defect: the question reads as "all of the work". |
| false-no `gate:sa.has_mortgage_interest` | 0: covered; 1: covered; 2: defect BUG-0805; 3: presentation; 4: covered | As the screen. |
| false-no `gate:sa.home_asked` | 0: model error; 1: covered; 2: open residual BUG-0807; 3: presentation | sa.home_other does name the spouse (reviewer saw the label); co-op is in the help; land-contract buyer is a low residual. |
| false-no `gate:sa.mortgage_interest_mfs` | 0: covered; 1: presentation; 2: presentation; 3: presentation | No gate defect. |
| false-no `gate:sa.mortgage_interest_not_mfs` | 0: model error; 1: covered; 2: presentation; 3: presentation; 4: presentation; 5: covered | No gate defect; a separate return is asked sa.mortgage_over_limit_mfs through the MFS sibling gate. |
| false-no `gate:sa.property_tax_other_if_home` | 0: covered; 1: covered; 2: covered; 3: covered; 4: model error; 5: presentation; 6: presentation | No gate defect. |
| false-no `gate:oi8z.damages` | 0: presentation; 1: presentation; 2: covered; 3: defect BUG-0804; 4: defect BUG-0804; 5: covered | As the screen. |
| false-no `gate:tipjob.listed` | 0: defect BUG-0806; 1: presentation; 2: presentation; 3: presentation; 4: covered | As the screen; the roster is under the person frame. |

Proposed defects (`/tmp/xrel/inc/work/L4.bugs.json`):
- BUG-0805 (medium): `sa.mortgage_other_use` interview prompt drops "substantially"; fix the prompt and help to "substantially improving (not repairs or furniture)".
- BUG-0806 (medium): `tipjob.listed` reads as all of the work; ask "Did you get any of these tips for work on the IRS list", so `tipjob.other_work` catches the mixed case.
- BUG-0804 (low; overlaps completeness oi8z#1.1): widen `oi8z.injury` to medical care for emotional distress and agreements in effect on or before September 13, 1995 (Yes refuses).
- BUG-0807 (low): `sa.home_owner` help to count a home bought on a land contract or contract for deed.

Note for the parent: `tipjob.tips` help now offers the Form 4070 total ("You may instead take the total of the tips you
reported to this employer on Form 4070 ..."), relevant to completeness tipjob#1.1.

