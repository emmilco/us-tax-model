# Screen and false-no adjudication, xrel people family (2026-11-15, sampled release reviews)

Family `people`: forms `person`, `household`, `dependent` and `s3`, tax year 2025, us. The samples are the sampled
release reviews at the B1 plus expansion tree (`.claude/worktrees/xint`). Rulings are in the fragments
`/tmp/xrel/frag/people.screens.json` (34 samples) and `/tmp/xrel/frag/people.false_no.json` (33 samples), each with its
unit's current `subject_sha`. The lead merges them into the `rulings.json` files. `xrel.py merge` (no `--write`) refuses
none of them. Samples already ruled at the current subject (4 screens and 7 false-no, all `s3`) were not ruled again.

The work was split three ways: `s3` (lead), `person` (fork) and `dependent` and `household` (fork). All three ran on
claude-opus-5-5, judgment. Each finding was checked against the form YAML, the interview wording and the cited source.
Earlier rulings of the same units were leads only. Where a ruling rests on what an amount comes to, it rests on a recorded
fixture or on an evaluation, both named in the evidence:
- `redesign.credits.refuse.adoption_earlier_us`;
- `b1mutB.s3.adoption_not_final`;
- the evaluation of `mfsl4.other_relative_too` under `/tmp/xrel/people/dep/`.

Separate returns are supported now, and no ruling relies on the removed gate `s3.mfs`.

## Counts

| Tool | Samples | Findings | covered | accepted WIDE | model error | presentation | out of scope | open residual | defect |
|---|---|---|---|---|---|---|---|---|---|
| screens | 34 | 101 | 39 | 25 | 7 | 9 | 2 | 16 | 3 |
| false-no | 33 | 137 | 35 | 0 | 24 | 29 | 2 | 41 | 6 |

The defects are:
- three wording defects (BUG-0861, -02 and -04);
- one citation defect (BUG-0865).

No gate computes a wrong condition.

## s3 (lead)

The s3 open residuals are wording residuals of the credit questions, cited to BUG-0620 (items 4, 8 and 9), as earlier
rulings did. Several s3 NARROW findings name a sibling situation of the same Schedule 3 line. The reviewer saw one
screen at a time. Lines 7, 12 and 14 each carry one refusal per situation, and each situation has its own question.

### Screens

| Unit | Findings (n: class) | Disposition |
|---|---|---|
| `s3.farmland_deferral#1` | 0: covered; 1: covered; 2: covered; 3: open residual [BUG-0620] | no gate defect; every other line 13 situation has its own question or refusal; one low wording residual |
| `s3.repaid_income#1` | 0: covered; 1: covered; 2: covered; 3: accepted WIDE | no gate defect; the other line 13 entries have their own questions; one over-refusal |
| `s3.section960c#1` | 0: covered; 1: covered; 2: covered; 3: accepted WIDE | no gate defect; each other line 13 situation has its own question or refusal; one over-refusal |
| `s3.section965#1` | 0: covered; 1: covered; 2: covered; 3: covered | no gate defect; each other line 13 situation has its own question or refusal |
| `s3.virgin_islands#1` | 0: open residual [BUG-0620]; 1: open residual [BUG-0620]; 2: covered | no gate defect; the other line 13z entries have their own questions; two low wording residuals of the help |
| `s3.kerosene_credit#1` | 0: covered | no gate defect; a business's fuel claim is asked of each business |
| `s3.mcc#1` | 0: covered; 1: accepted WIDE; 2: covered | no gate defect; the carried credit is asked by the 2024 forms question; one over-refusal, one residual answered by the help |
| `s3.elderly_credit#1` | 0: accepted WIDE; 1: accepted WIDE; 2: accepted WIDE | no gate defect; wide by design, the question refuses on the wish to claim |
| `s3.ev_credit#1` | 0: covered | no gate defect; the dealer transfer is asked first by its own question |
| `s3.ev_dealer#1` | 0: covered; 1: accepted WIDE; 2: accepted WIDE | no gate defect; the direct claim has its own question; one rare over-refusal and one safe reading |
| `s3.credit_bond#1` | 0: covered; 1: open residual [BUG-0620] | no gate defect; the carried credit is asked by the 2024 forms question; one low wording residual |
| `s3.adoption_us#1` | 0: covered; 1: covered | no gate defect; both readings are answered by the question and its help |
| `s3.prior_forms#1` | 0: covered; 1: open residual [BUG-0620]; 2: covered; 3: accepted WIDE; 4: open residual [BUG-0620] | no gate defect; a first minimum tax credit and 2025 credits are asked by their own questions; two known residuals and one over-refusal |
| `gate:s3.adoption_any#1` | 0: open residual [BUG-0620]; 1: open residual [BUG-0620]; 2: accepted WIDE | no gate defect; two medium wording residuals on 'adopt' read by the date the child came home, as ruled before |
| `gate:s3.adoption_asked_if_any#1` | 0: covered; 1: covered; 2: covered | no gate defect; 2024 payments and employer payments are asked by sibling questions under the same outer gate |
| `gate:s3.adoption_final_if_adoption#1` | 0: model error; 1: covered; 2: covered; 3: open residual [BUG-0620] | no gate defect; a not-final adoption gives no 2025 credit that the stepchild question could change; one low residual |
| `gate:s3.prior_other_forms#1` | 0: open residual [BUG-0620]; 1: open residual [BUG-0620]; 2: accepted WIDE | no gate defect; the design's accepted residuals; one wide |

### False-no

| Unit | Findings (n: class) | Disposition |
|---|---|---|
| `gate:s3.adoption_any#1` | 0: open residual [BUG-0620]; 1: open residual [BUG-0620]; 2: covered; 3: covered | no gate defect; the two 'adopt by placement date' readings stand as medium wording residuals; employer reimbursement and the special-needs exclusion are reached |
| `gate:s3.adoption_asked_if_any#1` | 0: model error; 1: model error; 2: open residual [BUG-0620] | no gate defect; both false-no cases are asked by sibling questions under the same outer gate; one medium residual on foreign finality |
| `gate:s3.adoption_earlier_if_any#1` | 0: covered; 1: open residual [BUG-0620]; 2: open residual [BUG-0620]; 3: covered | no gate defect; two findings answered by the help; the U.S. territories wording stands as a medium residual, as ruled before |
| `gate:s3.adoption_final_if_adoption#1` | 0: model error; 1: model error; 2: model error; 3: open residual [BUG-0620] | no gate defect; a not-final adoption gives no 2025 credit that the stepchild question could change; one low residual |
| `gate:s3.prior_amt_if_other_forms#1` | 0: open residual [BUG-0620]; 1: open residual [BUG-0620]; 2: open residual [BUG-0620]; 3: open residual [BUG-0620] | no gate defect; four wording residuals of the 2024-return questions, recorded under BUG-0620 |
| `gate:s3.prior_other_forms#1` | 0: open residual [BUG-0620]; 1: open residual [BUG-0620]; 2: open residual [BUG-0620]; 3: open residual [BUG-0620]; 4: open residual [BUG-0620] | no gate defect; the false-no findings are the residual the design named and the owner accepted with the tree; two wording residuals |

Three medium residuals recur from earlier rounds and are worth a help sentence each when the credit questions are next
changed:
- `s3.adoption_any`: count an adoption in the year a court made it final, even if the child came home earlier.
- `s3.adoption_us`: say "including U.S. territories".
- `s3.prior_other_forms`: name Form 6251 as a form that counts.

## person (fork)

### Screens

| Unit | Disposition | Findings (n: class [bug]) |
|---|---|---|
| unruled:person.mw_business#1 | no gate defect; the Schedule C clause changes where the payments appear, not the tax | 0: presentation; 1: presentation |
| unruled:person.sav_able#1 | no gate defect; two accepted WIDE; the present-tense opening is a low residual | 0: accepted WIDE; 1: accepted WIDE; 2: open residual [BUG-0866] |
| unruled:person.tips_gov#1 | no gate defect; WIDE and a minor UNCLEAR that errs toward Yes | 0: accepted WIDE; 1: presentation |
| unruled:gate:person.eligible_educator#1 | no gate defect; the calendar-year reading of '900 hours' is a low wording residual | 0: open residual [BUG-0868]; 1: open residual [BUG-0868] |
| unruled:gate:person.has_hsa#1 | no gate defect; the narrow case is covered by the HSA listing question; the citation is filed | 0: covered; 1: defect [BUG-0865]; 2: presentation |
| unruled:gate:person.ira_files_8606#1 | no gate defect; prior-year basis with a 2025 distribution or conversion is refused on the Form 1099-R | 0: covered; 1: covered; 2: covered; 3: presentation |
| unruled:gate:person.mw_has_1099#1 | no gate defect; a home-care business without a Form 1099 gets the same tax through lines 1d and 8s | 0: presentation; 1: presentation |
| unruled:gate:person.sav_trad_if_ira_owner#1 | no gate defect; a contribution not yet made is not entered, and SEP/SIMPLE cases are WIDE | 0: presentation; 1: accepted WIDE |
| unruled:gate:person.simple_open_year#1 | no gate defect; the 1963 to 1965 band is set by birth year, and the open years are the January 1 births | 0: model error; 1: model error; 2: accepted WIDE |
| unruled:gate:person.under16_open_year#1 | no gate defect; a filer born 2011 or later is under 16 by birth year and refused | 0: model error; 1: presentation; 2: accepted WIDE |
| unruled:gate:person.x_edu_account#1 | no gate defect for the earlier Coverdell excess (the question asks whether an account was held at any time in 2025); the ABLE contributor case is a residual; citation filed | 0: covered; 1: open residual [BUG-0866]; 2: defect [BUG-0865]; 3: accepted WIDE |

### False-no

| Unit | Disposition | Findings (n: class [bug]) |
|---|---|---|
| unruled:gate:person.age50_open_year#1 | no gate defect; born before 1976 is age 50 by birth year; the January 1, 1976 wording is a low residual | 0: open residual [BUG-0867]; 1: covered |
| unruled:gate:person.age55_open_year#1 | no gate defect; f8889.age55 treats anyone born before 1971 as 55 without asking | 0: model error; 1: model error; 2: open residual [BUG-0867] |
| unruled:gate:person.birth_cut_year#1 | no gate defect for filers; dependents' ages have no January 1 rule (filed) | 0: open residual [BUG-0867]; 1: presentation; 2: open residual [BUG-0867] |
| unruled:gate:person.edu_has_adj#1 | no gate defect; the term question's materials and term-year wording is a low residual | 0: covered; 1: open residual [BUG-0869]; 2: open residual [BUG-0869]; 3: covered; 4: model error |
| unruled:gate:person.eligible_educator#1 | no gate defect; the school-year wording is a low residual; the other readings are presentation | 0: open residual [BUG-0868]; 1: open residual [BUG-0868]; 2: presentation; 3: presentation; 4: presentation |
| unruled:gate:person.has_hsa#1 | no gate defect; the HSA listing question asks about any HSA held in 2025 | 0: covered; 1: presentation; 2: defect [BUG-0865] |
| unruled:gate:person.ira_files_8606#1 | no gate defect; earlier basis with a 2025 distribution is refused on the Form 1099-R; basis from a rollover, divorce or decedent is a low residual | 0: covered; 1: covered; 2: open residual [BUG-0871]; 3: open residual [BUG-0871]; 4: open residual [BUG-0871]; 5: covered; 6: covered; 7: covered; 8: model error |
| unruled:gate:person.ira_owner#1 | no gate defect; minor UNCLEARs answered by 'If you are not sure, answer Yes' | 0: presentation; 1: presentation; 2: presentation |
| unruled:gate:person.mw_has_1099#1 | no gate defect; without a Form 1099 the payments are treated the same way the Schedule C route would | 0: presentation; 1: presentation; 2: presentation |
| unruled:gate:person.mw_has_not_box1#1 | no gate defect; the not-in-box-1 question names Forms 1099 and no form | 0: covered; 1: covered; 2: presentation |
| unruled:gate:person.mw_paid#1 | no gate defect; the total includes 1099 and no-form payments, and the earned-income choice follows i1040gi Step 5 | 0: covered; 1: presentation; 2: presentation; 3: model error |
| unruled:gate:person.rmd_possible#1 | no gate defect in the birth-year/inherited gate for yearly RMDs; the question's 'yearly minimum' wording misses deadline-type requirements (filed) | 0: open residual [BUG-0870]; 1: open residual [BUG-0870]; 2: presentation; 3: presentation; 4: presentation; 5: open residual [BUG-0870]; 6: presentation; 7: presentation |
| unruled:gate:person.sav_trad_if_ira_owner#1 | no gate defect; the questions count 2026 contributions for 2025; a contribution not yet made is not recorded | 0: presentation; 1: covered; 2: presentation; 3: presentation; 4: covered; 5: presentation |
| unruled:gate:person.simple_open_year#1 | no gate defect; 1963 to 1965 is the 60 to 63 band by birth year; the January 1, 1966 wording is the low residual | 0: model error; 1: model error; 2: open residual [BUG-0867] |
| unruled:gate:person.turned_65_this_year#1 | no gate defect; the MFS spouse's boxes are refused elsewhere; the 'final return' wording is a low residual | 0: model error; 1: open residual [BUG-0872]; 2: presentation |
| unruled:gate:person.under16_open_year#1 | no gate defect; a filer born 2011 or later is under 16 by birth year and refused | 0: model error |
| unruled:gate:person.x_edu_account#1 | no gate defect for dormant accounts or owners; four rare residuals filed together; citation filed | 0: open residual [BUG-0866]; 1: covered; 2: open residual [BUG-0866]; 3: open residual [BUG-0866]; 4: covered; 5: defect [BUG-0865] |

## dependent and household (fork)

### Screens

| Unit | Disposition | Findings |
|---|---|---|
| dependent.divorced_rule#1 | no gate defect; Yes refuses | 0-2 accepted WIDE; 3, 4 model error |
| dependent.multiple_support#1 | no gate defect; Yes refuses | 0, 1 accepted WIDE |
| gate:dependent.other_only_spouse_if_mfs#1 | no gate defect; false gate -> tie-breaker refusal (executed) | 0-2 covered |
| gate:dependent.ptc_files#1 | defect | 0 out of scope (married dependent refused); 1 covered (help); 2 out of scope (8814 refused); 3 defect BUG-0861 |
| gate:household.married#1 | no gate defect; low wording residual | 0 covered; 1 open residual BUG-0863; 2 accepted WIDE |
| gate:household.mfs#1 | no gate defect | 0 model error (HOH lived-apart test is household.considered_unmarried); 1 accepted WIDE |

### False-no

| Unit | Disposition | Findings |
|---|---|---|
| gate:dependent.edu_has_adj#1 | no gate defect (gate is worksheet line 3, verified) | 0 model error; 1 covered; 2, 3 model error; 4 presentation |
| gate:dependent.ever_married#1 | low wording residual | 0, 2 open residual BUG-0863; 1 model error |
| gate:dependent.other_only_spouse_if_mfs#1 | no gate defect; No refuses | 0-3 covered |
| gate:dependent.ptc_files#1 | defect | 0 out of scope; 1 covered; 2 defect BUG-0861; 3 out of scope; 4 open residual BUG-0861 |
| gate:dependent.relationship#1 | no gate defect (filer_parent read only on MFS) | 0 model error; 1 covered; 2, 3 presentation |
| gate:household.all_tin#1 | no gate defect | 0 presentation; 1 model error; 2 covered; 3 model error |
| gate:household.claims_8862_credit#1 | defect in the gated question's wording | 0 defect, 1 open residual, 2 defect (all BUG-0862); 3 covered |
| gate:household.marriage_possible#1 | no gate defect | 0 model error; 1 covered (household.rdp asked apart, refuses); 2 presentation |
| gate:household.married#1 | no gate defect; widow refused by household.widowed_this_year | 0 covered; 1, 2, 5 open residual BUG-0863; 3, 4 covered |
| gate:household.mfs#1 | no gate defect; low help residual | 0 model error; 1 covered; 2 defect BUG-0864; 3 covered (executed); 4 model error |

## Pending bugs (`bug_pending/xrelpeople-NN.md`)

| Id | Severity | Subject | Proposed fix |
|---|---|---|---|
| BUG-0861 | medium | `dependent.ptc_files` states only the single, under-65, non-blind limits. A taxable scholarship is not named as pay, and the 65-or-older or blind limits are missing. | Name scholarships as pay; state the 65+/blind limits, or compute Chart B; settle the $400 self-employment rule from the source. |
| BUG-0862 | medium | `household.credit_disallowed` omits the additional child tax credit. It also omits credits taken back after an IRS letter or audit, including those agreed and repaid. | Name the ACTC; restore the letter, audit, court and repaid wording; define the math-error exclusion. |
| BUG-0863 | low | The help of `household.married_dec31` and `dependent.ever_married` dropped three federal marriage definitions: common-law, foreign or tribal, and that living apart does not end a marriage. | Add those sentences. |
| BUG-0864 | low | The `dependent.other_only_spouse` help says to answer No if "another parent of the child" lived with the child. That parent is usually the spouse, so a filer following it over-refuses the Pub. 501 Example 6 case. | Say "a parent of the child other than you and your husband or wife". |
| BUG-0865 | low | The `person.x_*` Form 5329 lines cite only Parts II and IX, and the label and source of `person.x_edu_account` disagree with its question. | Give each line its own Part's locator; make the label and source match the question. |
| BUG-0866 | low | The education and ABLE account questions miss five cases: a Coverdell contribution for 2025 made in 2026; a deemed distribution; 529 costs also used for a credit; the contributor of a returned ABLE excess; a former ABLE beneficiary. | Reword `x_edu_account`, `x_edu_taxable` and `sav_able`. |
| BUG-0867 | low | No day-before-the-birthday rule for a January 1 birth in `dependent.age` and the open-year age questions. | Add the sentence `person.born_jan1` already uses. |
| BUG-0868 | low | The eligible educator question does not say which school year's 900 hours count. | Add help naming the 2024-25 and 2025-26 school years. |
| BUG-0869 | low | `person.edu_over` says "course materials" without the lifetime learning credit limit, and "one term in the year" can exclude a 2026 term. | Reword the prompt and help. |
| BUG-0870 | medium | The missed-RMD question names only a "yearly minimum". It misses the 5-year and 10-year deadlines and the first-year April 1 distribution, and the gate misses a QDRO share. | Reword the question; widen the inherited-account help. |
| BUG-0871 | low | `retirement.ira_basis` asks only about the filer's own undeducted contributions, so it misses basis from an after-tax plan rollover, a divorce transfer or an inherited IRA. | Reword the question. |
| BUG-0872 | low | `person.died_at_64` asks about "the final return", which a surviving spouse on a joint return may answer No. | Ask whether the person died in 2025 before reaching 65. |

Outside these units, not ruled: the refusal of `f1040.line12e` on `household.widowed_this_year` still says a separate
return is something "this tool does not support". Separate returns are supported now, so that remedy text is stale.
