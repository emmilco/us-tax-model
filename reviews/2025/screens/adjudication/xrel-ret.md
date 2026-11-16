# Screen and false-no adjudication, xrel lane, family ret (2026-11-15)

Brief: `/tmp/xrel/brief.ret.md` (claude-opus-5-5, judgment, 2025, us). Sampled release reviews of the ret family (forms retirement, ira, f8606, f5329, ssb, sli, f8889, f8853c, f8959) at the B1 plus expansion tree. Rulings are in the fragments `/tmp/xrel/frag/ret.screens.json` (31 samples) and `/tmp/xrel/frag/ret.false_no.json` (32 samples), keys `unruled:<unit>#<k>` with the current `subject_sha`; the lead merges them. `xrel.py merge` (no `--write`) refuses none of them. Earlier rulings were leads only and were checked against the current lines.

Pending bugs cited: BUG-0873 to BUG-0876 (filed by this family's screen and false-no adjudication) and BUG-0878 (filed with the completeness adjudication, `reviews/2025/completeness/r9-xrel-ret.findings.md`).

Pending entries -07 to -09 were filed by the false-no adjudication. BUG-0880 (retirement.ira_basis) duplicates BUG-0871 and should be merged into it at numbering.

One open point for the lead: the screen ruling of `f8853c.others_paid#1` finding 0 reads the current set-rate prompt as matching the Multiple Payees condition (i8853 p. 9), which argues against the part of BUG-0873's proposed fix that would name an accelerated death benefit paid to another person.

## Screens (ret family, xrel lane)

Samples ruled: 31 (all unruled screen samples of the ret family). Findings: 77. Classes: accepted WIDE 31, covered 26, defect 9, model error 6, presentation 3, out of scope 2.
Defects: BUG-0875 (low) and BUG-0876 (low) filed here; BUG-0873 (medium) and BUG-0874 (low), filed by the false-no fork, are cited where a screen finding repeats them.

| sample | findings (n: class) | disposition |
| --- | --- | --- |
| `f8853c.nonqualified#1` | 0: accepted WIDE | no gate defect; the box 4 test is the issuer's report of the status. The question asks about box 4 of Form 1099-LTC; a box that contradicts the contract is an issuer error, and a Yes on a qualified contract only refuses. |
| `f8853c.others_paid#1` | 0: covered; 1: accepted WIDE | no gate defect. The interview asks only about others paid at a set rate, which is the Multiple Payees condition; an assignee reading refuses, safe. |
| `f8853c.pre1996#1` | 0: accepted WIDE; 1: accepted WIDE | no gate defect; WIDE by design. A modified pre-1996 contract is refused though line 24 would be right; the refusal remedy names that case. The scope of 'that' errs safe either way. |
| `f8853c.rate_changed#1` | 0: covered; 1: accepted WIDE; 2: accepted WIDE | no gate defect. The interview asks whether a policy started or stopped paying partway through, which catches the stop-and-restart case; the other two readings refuse, safe. |
| `f8889.archer#1` | 0: accepted WIDE; 1: accepted WIDE | no gate defect; WIDE by design. Any Archer MSA distribution or inherited interest refuses, as the earlier ruling of this unit and BUG-0614 record. |
| `f8889.excess_withdrawn#1` | 0: covered; 1: accepted WIDE; 2: accepted WIDE | no gate defect. The 6-month window after a timely filed return is reached by an amended return, on which the withdrawal is before filing; the two WIDE findings refuse, safe, as the earlier ruling. |
| `f8889.former_spouse_family#1` | 0: accepted WIDE; 1: defect (BUG-0874) | defect (wording): legal separation not named; one WIDE. The spouse-not-eligible case refuses, safe. A marriage ended by a decree of separate maintenance is not named; filed with the false-no lane's entry. |
| `f8889.ira_transfer#1` | 0: covered; 1: covered; 2: accepted WIDE | no gate defect. The prompt asks about any money moved straight from an IRA, with no type or 'qualified' test; the third finding refuses, safe. |
| `ira.deduct_less#1` | 0: accepted WIDE; 1: covered | no gate defect. The prompt compares with the most the rules allow, so a capped deduction is not a smaller one; a zero deduction is deducting less. |
| `ssb.lump_elect#1` | 0: accepted WIDE | no gate defect; WIDE. Wanting the election with nothing taxable refuses a case the worksheet computes. Safe. |
| `ssb.terror_disability#1` | 0: accepted WIDE; 1: accepted WIDE | no gate defect. Both readings either refuse or follow the text's own words; as the earlier ruling (T-008). |
| `gate:f8853c.has_line24#1` | 0: defect (BUG-0873); 1: accepted WIDE | defect (wording) recorded; one WIDE. The 'paid back' wording of the line 24 and pre-1996 questions is the false-no lane's BUG-0873; the modified-contract case refuses, safe. |
| `gate:f8853c.has_periodic#1` | 0: presentation; 1: accepted WIDE | no amount defect; line 15 box presentation. With line 20 zero line 26 is zero whatever line 15 says; the gated questions confirming No cost only questions. |
| `gate:f8853c.periodic#1` | 0: defect (BUG-0873); 1: covered; 2: out of scope | defect (wording) recorded for weekly or other periods; the rest covered or outside the tool. 'Per day or month' omits other periods (BUG-0873); accelerated death benefits are named in the opening tick; a wrong box 3 is an issuer error. |
| `gate:f8889.ask_former_spouse_family#1` | 0: defect (BUG-0874); 1: defect (BUG-0874); 2: accepted WIDE | defect (wording) recorded; one WIDE. The 'while' and divorce-or-death wording is the false-no lane's BUG-0874; the not-eligible spouse refuses, safe. |
| `gate:f8889.ask_last_month_prior#1` | 0: covered; 1: covered | no gate defect. A failed 2024 transfer testing period sets f8889.testing_if_asked, so any month of 2025 without eligibility refuses at f8889.testing_failed; as the earlier ruling. |
| `gate:f8889.inherited_any#1` | 0: covered; 1: accepted WIDE | no gate defect. The account beneficiary's own final return is asked at f8889.owner_died; the earlier-year non-spouse case costs a question. |
| `gate:f8889.medical_all_if_dist#1` | 0: covered; 1: covered; 2: accepted WIDE | no gate defect. The help names the excluded costs; a deemed distribution and an excess withdrawal are asked and refused elsewhere; as the earlier ruling. |
| `gate:f8889.mfs_ask#1` | 0: covered; 1: defect (BUG-0874); 2: presentation | defect (wording) recorded for the present tense; the rest covered or presentation. Joint returns split the family limit through the allocation lines; the present-tense spouse-HSA question is the false-no lane's BUG-0874. |
| `gate:f8889.testing_failed_figured#1` | 0: covered; 1: covered; 2: accepted WIDE; 3: accepted WIDE; 4: accepted WIDE | no gate defect. A 2025 transfer refuses at f8889.ira_transfer; the filer-facing questions carry no timing ambiguity; the wrong disability No and the WIDE cases refuse, safe. |
| `gate:retirement.cost_any_if_plan#1` | 0: covered; 1: accepted WIDE | no gate defect. The death benefit exclusion is asked of a plan beneficiary at retirement.death_exclusion and refused; full recovery costs questions. |
| `gate:retirement.disability_if_plan#1` | 0: covered; 1: accepted WIDE | no gate defect. Forms 1099-R are listed per person, so 'you' is the recipient; the plan-without-disability-provision case asks extra questions here (its amount effect is completeness item retirement#1.1). |
| `gate:retirement.is_code7#1` | 0: covered; 1: presentation; 2: covered; 3: accepted WIDE | no gate defect. Codes 1, J and S over 59 1/2 are handled by exception 12 in retirement.exception; the code-7 gate looks for a code that does not fit; the recipient is the listed person. |
| `gate:retirement.is_ira#1` | 0: model error; 1: model error; 2: model error; 3: model error; 4: model error; 5: model error | no gate defect; model error. The model read the gate's polarity backwards: each plan-only line asks its question when retirement.is_ira is false. |
| `gate:retirement.is_trad#1` | 0: covered; 1: covered; 2: accepted WIDE | no gate defect. IRA basis is asked of the person who lists the form; 2025 nondeductible contributions with a distribution refuse at f8606.line14; any earlier Form 8606 refusing is safe. |
| `gate:retirement.plan_death#1` | 0: defect (BUG-0875); 1: defect (BUG-0875) | defect (wording): the beneficiary questions name only an employee who died before retiring. retirement.ben_before_retire's '(before retiring)' and retirement.death_exclusion's 'the employee' are narrower than i1040gi; filed low. |
| `gate:retirement.put_back#1` | 0: covered; 1: covered; 2: accepted WIDE | no gate defect. retirement.rollover_any names conversions and does not say 'another' account; the WIDE finding costs questions. |
| `gate:retirement.under59_if_code7#1` | 0: covered; 1: covered | no gate defect. A section 457 distribution coded 1 takes exception 13 in retirement.exception; the recipient is the listed person. |
| `gate:sli.any_if_not_mfs#1` | 0: defect (BUG-0876); 1: accepted WIDE | defect (wording): a loan not named a student loan; one WIDE. The tick turns on the loan's name; the help covers doubt but not a filer sure a personal loan is not a student loan. Filed low. |
| `gate:ssb.any#1` | 0: covered | no gate defect. A repayment-only filer is asked at s3.repaid_income, whose help names social security repayments, and refused. |
| `gate:ssb.prior_year_pay#1` | 0: out of scope; 1: accepted WIDE | no gate defect. A missed Yes only skips an election this tool refuses; the return without the election is a correct return. The WIDE finding costs a question. |

### Defects

- BUG-0873 (medium, false-no fork): f8853c line 24 / pre-1996 'paid back' wording and the set-rate question's 'per day or month'. Cited by `gate:f8853c.has_line24#1` 0 and `gate:f8853c.periodic#1` 0. Note: `f8853c.others_paid#1` finding 0 argues that the current set-rate limit in f8853c.others_paid follows Multiple Payees (i8853 p. 9), against the part of that entry's fix that would name any accelerated death benefit to another person.
- BUG-0874 (low, false-no fork): f8889 then-spouse question ('while', divorce or death only) and the present-tense separate-return spouse-HSA question. Cited by `f8889.former_spouse_family#1` 1, `gate:f8889.ask_former_spouse_family#1` 0 and 1, `gate:f8889.mfs_ask#1` 1.
- BUG-0875 (low): retirement.death_exclusion names only 'the employee' (i1040gi p. 29 says employee or former employee) and retirement.ben_before_retire's '(before retiring)' conflicts with the annuity-starting-date line. Fix: reword both questions. `gate:retirement.plan_death#1` 0 and 1.
- BUG-0876 (low): sli.any's tick turns on the loan's name; a personal loan used only for school costs may be answered No. Fix: help sentence that a loan counts by what it paid for. `gate:sli.any_if_not_mfs#1` 0.

Model error: `gate:retirement.is_ira#1` read the gate's polarity backwards (each plan-only line asks its question when retirement.is_ira is false).

## False-no samples (ret family, 32 samples, 153 findings)

Model claude-opus-5-5, judgment. Each sample ruled against the archived source, forms/2025, rendered/2025 and interview/2025/questions.yaml; one interview-coverage probe row (ssb.any false) walked, no model calls.

Findings by class: covered 78, presentation 39, defect 22, model error 7, accepted WIDE 3, open residual 2, out of scope 2.
Samples by disposition: no gate defect 19, defect 12, open residual 1.

| Gate | Disposition | Findings (n: class, bug) |
|---|---|---|
| f8853c.has_line17#1 | no gate defect; the box 4 and box 3 readings follow the payee statement the line instructions name; low wording points | 0: presentation; 1: covered; 2: covered; 3: accepted WIDE; 4: presentation |
| f8853c.has_line24#1 | defect (medium, wording): the pre-1996 question is in the past tense against an expected reimbursement; the general-rule reading is a model error | 0: model error; 1: defect BUG-0873; 2: open residual BUG-0873; 3: presentation |
| f8853c.has_periodic#1 | defect (medium, wording): line 24 asks only what was 'paid back to you'; others-paid omits a lump-sum accelerated death benefit to another person | 0: defect BUG-0873; 1: presentation; 2: defect BUG-0873; 3: defect BUG-0873; 4: defect BUG-0873; 5: covered |
| f8853c.periodic#1 | no gate defect for the set-rate test; one wording residual: 'per day or month' omits a weekly or other period | 0: defect BUG-0873; 1: covered; 2: covered; 3: covered; 4: model error; 5: covered |
| f8889.ask_former_spouse_family#1 | defect (low, wording and reach): the then-spouse question reads as coverage at the end of the marriage and skips a person remarried by year end | 0: defect BUG-0874; 1: covered; 2: defect BUG-0874; 3: defect BUG-0874; 4: covered; 5: presentation |
| f8889.ask_last_month_prior#1 | no gate defect; the failed funding-distribution case still reaches the testing-period refusal | 0: covered; 1: model error; 2: covered |
| f8889.coverage_year#1 | no gate defect; a No sends the filer to the month questions, which give the same line 3; wording points low | 0: covered; 1: covered; 2: covered; 3: presentation |
| f8889.inherited_any#1 | no gate defect; the estate case is refused by f8889.owner_died and the help names the beneficiary cases | 0: covered; 1: covered; 2: covered; 3: covered |
| f8889.ira_prior_if_asked#1 | no gate defect; each named disqualifier is asked in the month or FSA questions | 0: covered; 1: covered; 2: covered; 3: covered |
| f8889.medical_all_if_dist#1 | no gate defect; the inherited cases are refused before the distributions; one low wording point on reimbursement | 0: covered; 1: covered; 2: covered; 3: presentation; 4: out of scope |
| f8889.mfs_ask#1 | defect (low, wording): the separate-return spouse-HSA question is in the present tense; the other findings are covered | 0: defect BUG-0874; 1: covered; 2: presentation; 3: covered |
| f8889.testing_failed_figured#1 | no gate defect; a 2025 funding distribution is refused, and a wrong No to the disability question refuses | 0: covered; 1: model error; 2: accepted WIDE; 3: accepted WIDE |
| ira.has_deduction#1 | no gate defect; the help states what a No does; one presentation low on 'Almost everyone answers No' | 0: covered; 1: presentation; 2: covered |
| ira.mfs_cov_matters#1 | defect (low, wording): 'covered by a retirement plan at work' may leave out a self-employed spouse's plan | 0: defect BUG-0881; 1: covered; 2: presentation |
| retirement.born_before_averaging_date_if_plan#1 | no gate defect; the question asks about the person who earned the balance | 0: presentation; 1: covered; 2: covered |
| retirement.cost_any_if_plan#1 | no gate defect; the question asks about any taxed money paid in, with 'If you are not sure, answer Yes' | 0: covered BUG-0875; 1: covered; 2: covered; 3: covered; 4: covered; 5: covered |
| retirement.dis_early_if_disability#1 | defect (low, wording): the disability tick is in the present tense; the joint-return reading is covered | 0: covered; 1: defect BUG-0881; 2: presentation |
| retirement.disability_if_plan#1 | defect (low, wording): the disability tick is in the present tense; code 3 from a plan is refused; the plan-provision point is BUG-0878 | 0: covered; 1: defect BUG-0881; 2: presentation; 3: presentation; 4: covered |
| retirement.is_code2#1 | no gate defect; combined codes are refused, a modified series is screened; wording lows | 0: covered; 1: covered; 2: presentation; 3: presentation; 4: presentation |
| retirement.is_code7#1 | no gate defect; combined codes are refused and the age question is per person | 0: covered; 1: covered; 2: presentation; 3: covered |
| retirement.is_death#1 | open residual: a surviving spouse treating an inherited IRA as their own (BUG-0878); combined codes refused | 0: open residual BUG-0878; 1: covered; 2: covered |
| retirement.is_ira#1 | no gate defect; the account kind is chosen by the IRA/SEP/SIMPLE box and has only three values | 0: covered; 1: covered; 2: covered; 3: model error; 4: model error; 5: covered |
| retirement.is_trad#1 | defect (medium): an inherited IRA's basis, and basis from rolled-in after-tax money, are not asked; other findings covered | 0: covered; 1: defect BUG-0880; 2: defect BUG-0880; 3: covered; 4: covered; 5: covered; 6: presentation |
| retirement.plan_death#1 | no gate defect; combined codes refused; the beneficiary wording is BUG-0875 | 0: presentation; 1: covered; 2: out of scope; 3: defect BUG-0875; 4: defect BUG-0875; 5: presentation; 6: presentation |
| retirement.put_back#1 | no gate defect; conversions, direct Roth rollovers and same-account redeposits are reached | 0: covered; 1: covered; 2: covered; 3: covered; 4: presentation; 5: presentation; 6: presentation; 7: covered |
| retirement.rollover_any#1 | defect (low, wording): the rollover question's 60 days omits the encoded 120-day first-home recontribution; other findings covered or low | 0: presentation; 1: presentation; 2: covered; 3: covered; 4: presentation; 5: defect BUG-0881 |
| retirement.under59_if_code7#1 | no gate defect; per person, and other codes take the exception list | 0: covered; 1: presentation; 2: presentation; 3: covered |
| sli.any_if_not_mfs#1 | defect (low, wording): a loan not called a student loan (BUG-0876); other findings covered or low | 0: defect BUG-0876; 1: covered; 2: defect BUG-0876; 3: covered; 4: presentation |
| sli.assisted_any_if_any#1 | no gate defect; the question asks whether interest was paid by a program or a 529 plan, for the filer or spouse | 0: presentation; 1: model error; 2: covered; 3: presentation; 4: presentation; 5: covered |
| sli.unqualified_any_if_any#1 | defect (low, wording): the list does not name a school or program that is not eligible; the other findings are covered | 0: presentation; 1: covered; 2: covered; 3: covered; 4: defect BUG-0881; 5: covered |
| ssb.any#1 | defect (low): a person who only repaid benefits answers No and the repayment refusal is not asked | 0: defect BUG-0879; 1: covered; 2: covered; 3: presentation; 4: covered |
| ssb.prior_year_pay#1 | no gate defect; the lump-sum election is optional and a No yields a correct return without it | 0: presentation; 1: presentation; 2: presentation |

### Pending defects cited

- BUG-0873 (medium): f8853c line 24 asks what was 'paid back to you' (misses expected and provider-paid reimbursements); pre-1996 question past tense; others-paid omits accelerated death benefits; set-rate question names only day or month.
- BUG-0874 (low): f8889.former_spouse_family reads as coverage at the end of the marriage and skips a person remarried by year end; f8889.mfs_spouse_hsa in the present tense.
- BUG-0875 (low, filed by the screens fork): retirement beneficiary questions name only an employee who died before retiring.
- BUG-0876 (low, filed by the screens fork): sli.any turns on the loan's name.
- BUG-0878 (filed by the completeness adjudicator): code 4 surviving spouse treating an inherited IRA as own.
- BUG-0879 (low): ssb.any misses a person who only repaid benefits; ssb.repaid_more is then not asked (probe walk).
- BUG-0880 (medium): retirement.ira_basis misses an inherited IRA's basis and rolled-in after-tax basis (same point as completeness claim retirement#1.2).
- BUG-0881 (low): disability tick present tense; rollover question omits the encoded 120-day first-home recontribution; ira.mfs_spouse_covered says 'at work'; sli.unqualified_any does not name an ineligible school or program.
