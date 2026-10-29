# Stage 21 (Form 5329): decision batch for the owner

> **Owner's answer (2026-10-29): all recommended.** D1 to D10 are accepted as recommended, with the items under
> "Settled by the evidence".

Prepared on 2026-10-29 from `stage21-form-5329.md` (the premise map, 2026-10-22, at 6051ec0) and
`stage21-form-5329.verification.md` (its adversarial check, at 1c465c2). Both were checked again against the tree at
2d971ad with the Stage 19 build in the working tree, not yet committed. Where the map and the verification differ, the
verification's checked facts are used. Where the tree has moved since (Stages 16, 20, 18 and 19), the current state is
used and the change is noted.

This is the fourth and last stage of the route in `docs/2026-10-26_plan_revision.md` section E. Category `form5329`:
3.2% of returns (5,092,999, the 2023 count of returns with "Penalty tax on qualified retirement plans", soi-23in33ar
column 76, read again from the spreadsheet; column 77 is $6,380,591 thousand, about $1,253 a return). The gain if
covered alone is +2.6 from 79.6% (`reports/2025/filer_coverage.json`, `gain_if_covered_alone.retirement_penalty`
0.0261, with Stage 19 retired), so 82.2% after it. That reaches the first goal. The figure is the least certain of the
route's four. The category is IRS-only ("—" for microdata) and is combined as independent of every other category.
The SOI cell is the whole of Schedule 2 line 8 and does not split Form 5329's nine parts, so the +2.6 counts as
retired every return with any line 8 tax, including the parts this stage refuses. That most of the count is Part I
rests only on the averages: $118 to $249 a return between $1 and $10,000 of AGI, about $1,565 between $100,000 and $200,000.
That fits 10% of early distributions, but the cell cannot show it.

## What the stage is

Form 5329 (`f5329`, i5329 2025). Part I is the 10% additional tax on early distributions from qualified plans and IRAs
(lines 1 to 4: early distributions included in income, the excepted part with an exception number, the rest, and 10%
of it, or 25% for a SIMPLE IRA in its first two years). Parts II to IX are the 10% tax on taxable Coverdell, QTP and
ABLE distributions, and the 6% taxes on excess contributions to traditional IRAs, Roth IRAs, Coverdell ESAs, Archer
MSAs, HSAs and ABLE accounts. Part IX is the 25% (or 10%) tax on a required minimum distribution not taken. On a joint
return each spouse files a separate form ("complete a separate form for each of you. Include the combined tax on
Schedule 2 (Form 1040), line 8", i5329 p. 2). There is also a no-form path: when only early distributions are involved
and code 1 is correct on every Form 1099-R, the filer enters 10% of the taxable amount on Schedule 2 line 8 and
checks its box (i1040gi p. 112, "If only item (1) applies and distribution code 1 is correctly shown in box 7 of all
your Forms 1099-R, you don't have to file Form 5329").

Today every Form 5329 tax is refused, and the project has no `s2.line8`. Three routes refuse it. Code 1 and code S are
`other` in `enums.retirement_code` (`params/2025.yaml`: normal_7, death_4, early_exception_2, direct_rollover_G,
qualified_roth_Q, other), so `retirement.bad_code` refuses them. `retirement.special` names "an early distribution with
no known exception (code 1, J or S)". `s2.other` asks for any other Schedule 2 amount, including "the additional tax on
early retirement distributions (often called a penalty)". The parts also have gates of their own. `f8889.excess`
refuses HSA excess, and `f8889.unsupported` refuses prior-year HSA excess and withdrawals of excess. For IRA excess
(Stage 16, below) there are `person.ira_excess_gate`, `person.ira_over_limit` and `ira.over_comp`. Taxable Coverdell and
QTP distributions are refused by `oi8z.additional_tax`. Nothing gates Part V (Coverdell excess), Part VIII (ABLE
excess) or Part IX (a missed required distribution) except `s2.other`. That matters once `s2.other` is narrowed (D3).

New since the map was written, or corrected by the verification:

- **`retirement` still has no owner.** `forms/2025/retirement.yaml` `collection:` has no `parent`, and `check.ts`
  still rejects a `sum_over` whose collection's parent is not the evaluating document ("collection parent binding
  mismatch"). The readers are the same six Form 1040 lines the verification found (`f1040.line4a`, `line4b`,
  `ira_rollovers`, `line5a`, `line5b`, `plan_rollovers`) plus `f8880.dist_2025`, reading the six Stage 15 `sav_*`
  entry lines. The fixtures hold 115 entries in 83 cases across five files (classm 40 cases, classm.deepseek 15,
  stage10 24, stage15 2, stage16 2). Twelve of those cases are joint, with 18 entries. `engine/src/generate.ts` draws
  the codes (l. 339) and keys `retirement[rN]` (l. 592).
- **Stage 16 added per-person IRA facts.** `person.ira_trad`, `ira_contrib`, `sav_roth`, `ira_own_total` and
  `ira_limit` exist, as do the IRA Deduction Worksheet (`ira.*`) and Form 8606 Part I as an implicit per-person form
  (`f8606.yaml`, `collection: parent: person, implicit: form`). Excess IRA contributions are refused by the screen
  `person.ira_excess` (through `person.ira_excess_gate`, which fires only when the person made 2025 contributions), by
  the computed `person.ira_over_limit` and by `ira.over_comp`. *Gap:* an earlier IRA excess still in the account, with
  no 2025 contribution, reaches no IRA gate. Only `s2.other` catches it today. Stage 16 also added `person.ira_dist`,
  a per-person Yes/No on a 2025 traditional IRA distribution. It exists because the Forms 1099-R have no owner.
- **Stage 16 also added Form 8889 Part II and other income.** Lines 14a to 17b are computed, and
  `person.hsa_addtax = sum_over f8889` feeds `s2.line17c = sum_over person`. That is the person-total pattern the
  verification (error 5) said line 8 needs, and it is now in use. `oi8z` is a return-level line 8z collection with no
  owner. Its kinds are rtaa, kickbacks and seven refused kinds, `other` among them.
- **The negative-AGI edge is closed.** `sa.line2` now copies `sa.agi_floor`, which is AGI floored at zero
  (`amb.2025.sa_medical_negative_agi`), so `sa.line4` ≤ `sa.line1`. The verification's error 7 no longer holds, and
  exception 05 can be capped by `sa.line4` as it stands.
- **`s2.other` gates one other category now, not two.** `ptc` is `"refused": false` with no gates (Stage 18), so
  `s2.other` is the gate of `form5329` and `schedule2_other` only. Its wording (Stage 18) no longer names the PTC
  repayment. It does name "the additional tax on early retirement distributions (often called a penalty)" and no HSA
  excess item, which confirms the verification's error 3.
- **No atom is needed.** Part I is `test`, `choose`, `smaller_of`, `subtract_floor0`, `sum_over` and `multiply_rate`.
  Part VII is `smaller_of` then `multiply_rate`.
- **Outside engines.** None computes Form 5329 as printed. UsTaxes' `F5329.ts` (read in full) does Part I only, for
  IRA records only. It takes a user-supplied `earlyWithdrawalAmount` ("amounts with exception codes should be excluded
  by the user"), combines both spouses, applies a flat 10% rounded to dollars, and has no 25% rate and no Part VII.
  Its Schedule 2 `l8box` is always false. Tax-Calculator takes Schedule 2 line 8 as the input `e09900`, and
  OpenTaxSolver reads `S2_8` as an entered amount. PolicyEngine-US has no Form 5329 variable: its
  `early_withdrawal_penalty` is the Schedule 1 savings penalty. No adapter maps Form 1099-R distributions today
  (`tools/engines/generate_cases.py` l. 216, "no Form 1099-R distributions").
- **The 2026 drafts are archived**: `sources/2026/f5329` (posted 2026-08-06), `i5329` (2026-09-08), `f1040s2`
  (2026-06-04) and `i1099r`. The draft Schedule 2 splits today's line 8 in two. Line 5 ("Additional tax on IRAs or
  other tax-favored accounts", Section A) takes Form 5329 Parts I and II and the new Part XI. Line 18 ("Additional tax
  on excess contributions or accumulations in IRAs or other tax-favored accounts", Section B) takes Parts III to X.
  Both lines stay in Part II, so Form 1040 line 18 still does not see them. The draft form adds Parts X and XI
  (Trump accounts, sec. 530A). The draft instructions add exception 24, qualified long-term care distributions
  ("Beginning with distributions made after December 29, 2025"), which the 2025 table (01 to 23) does not list.
- P.L. 119-21 (archived) does not amend 72(t) or 4974. Sec. 70204 creates Trump accounts and a 4973 excess rule for
  them, for taxable years after 2025. Sec. 70413(a) widens 529 qualified expenses for "distributions made after the
  date of the enactment" (July 4, 2025), which touches only Part II, refused here. The HSA sections touch HDHP
  eligibility, not Form 5329: sec. 71306 (telehealth) applies to plan years after 2024, and secs. 71307 and 71308
  apply to months after 2025.

## Decisions for you

**D1. Who owns a Form 1099-R.** Give `retirement` the parent `person`, as Form W-2 has. Each person gets totals
(`sum_over retirement`), and the six Form 1040 lines and `f8880.dist_2025` become `sum_over person` of them, as
`f1040.line1a` is over the W-2 totals. The 115 fixture entries are re-keyed under their person. The 18 entries on
joint returns are assigned to a spouse; no value changes, because nothing reads them per person today. The interview
moves `$retirement` under `$person`. Its `$person` help, "pensions and annuities ... are entered once, for you and your
spouse combined", is rewritten (verification error 6). The generator re-keys too. *Noted, not this stage's:*
`person.ira_dist` could then be derived from the person's traditional IRA entries. / (a) An owner Enum on each entry,
with Form 5329 at return level in two columns filtered by owner, the Form 8880 pattern (`where` on `person.role`).
That leaves the collection in place, but every Form 5329 line is written twice, and the values sheet shows one form
where the IRS wants one per spouse. (b) A single return-level Form 5329 that refuses joint returns where both spouses
have early distributions. It is cheapest, but it refuses the joint cases the per-person caps (D4) are about.

**D2. Scope.** Compute Part I for codes 1 and S, with exceptions per Form 1099-R entry and the 25% SIMPLE rate. Also
compute the no-form path with the Schedule 2 line 8 box (D5), Part VII for the current year's HSA excess (D6), and
Schedule 2 line 8. Also accept code 3 (disability) on an IRA entry: fully on line 4b, exception 03 shown by the code,
no tax. Code 3 from a plan stays refused, because under minimum retirement age it is wages on line 1h, which
`retirement.special` names. Refuse, each by a cited screen (D3): Part II, Parts III and IV (D7), Part V, Part VI
(already `f8889.unsupported` for Archer MSAs), Part VIII and Part IX. Roth IRA distributions other than code Q (code
J, T; Form 8606) stay refused by `retirement.bad_code`. / Part I only, leaving HSA excess with `f8889.excess`. Or also
Parts III and IV (D7).

**D3. Screens.** Two new screens.
(a) **Per Form 1099-R entry, asked for code 1 or S.** It asks whether the distribution is any of these: a qualified
disaster recovery distribution (Form 8915-F; today's `retirement.special` does not name it, so computing code 1
without this screen would overstate tax); a modified series of substantially equal payments (the recapture on line 4,
p590b p. 26); a distribution from an annuity contract or modified endowment contract; a repayment of an exception 19,
20, 22 or 23 distribution (Form 8606, p590b p. 4); a qualified long-term care distribution made December 30 or 31,
2025 (exception 24 of the 2026 draft, absent from the 2025 table); or a distribution with more than one exception
(D4).
(b) **Per person, the parts not built.** A taxable Coverdell, QTP or ABLE distribution (Part II;
`oi8z.additional_tax` keeps refusing the Coverdell and QTP item). An IRA excess from an earlier year still in the IRA,
asked whether or not there were 2025 contributions (this closes the gap above). Excess Coverdell, Archer MSA or ABLE
contributions. An HSA excess from an earlier year when there is no Form 8889 entry. A required minimum distribution not
taken (Part IX). These are worded from the part headings, because narrowing `s2.other` uncovers them.
Today's `retirement.special` loses its code 1, J or S clause. A code 2 entry whose exception covers only part, and a
code 7 or 4 that is wrong (the filer was under 59½, or was not a beneficiary), go into screen (a)'s list for code 2,
4 and 7 entries. / Fold everything into `retirement.special` and one longer `s2.other`. That means fewer questions,
but a filer with only a code 7 pension answers a long question about early-distribution special cases.

**D4. Exceptions and their caps.** Each early entry gets one exception (an Enum: 01 to 23, or none) and the amount it
covers. The amount is capped by the entry's taxable amount (`retirement.taxable`). Exceptions 01 and 06 are refused on
an IRA entry, and 07, 08 and 09 on a plan entry, as i5329 p. 5 limits them. The fixed caps are per person, totalled
over the person's entries (verification error 2):
- 09: $10,000 less a per-person input of earlier first-home distributions (p590b p. 27, "can't be more than
  $10,000", with each spouse having their own $10,000).
- 19: $5,000 per birth or adoption (a Count; reading D8(c)).
- 22: $10,300.
- 23: $1,000, one per year (p590b p. 28).
- 05 (medical): `sa.line4`, the medical expenses above 7.5% of AGI, which can be asked whether or not the filer
  itemizes (p590b p. 25, "You don't have to itemize"). On a joint return, the combined 05 amounts of both spouses are
  limited to `sa.line4` by refusal (reading D8(d)).
For 07 and 08, the filer enters the premiums or adjusted qualified education expenses (p970 chapter 8), with
help text. The account-value limbs of 22 and 23 (50% of the IRA's value; the interest in the IRA less $1,000) are
attested in the question's wording. / No computed caps: take the filer's amount, capped only by the taxable amount,
with a notice. Simpler, but the caps are printed amounts that a filer can overstate.

**D5. The no-form path on a joint return.** Prepare a Form 5329 for every person with an early distribution whenever
any person must file one. Check the line 8 box only when no one must, that is: every early entry is code 1, none claims
an exception, there is no code S and no Part VII tax (map Q2/D10). The tax is the same either way. / Per person: the
second spouse's 10% goes on line 8 directly beside the first spouse's form. The instructions do not say how to mark
that, so the box could not be shown correctly.

**D6. HSA excess (Part VII).** Line 47 is the person's own excess, `f8889.line2` − `f8889.line13`, which equals line 2
− line 12 when positive (i5329 p. 8 says line 12, i8889 p. 8 says line 13; the verification checked that they agree).
Line 49 is 6% of the smaller of line 48 and a new input, the value of the person's HSAs on December 31, 2025, asked
only when line 48 is above zero. Lines 42 to 46 are zero: a prior-year excess stays refused by `f8889.unsupported`,
or by D3(b) without a Form 8889. An excess withdrawn by the due date stays refused, because i5329 p. 8 puts the
withdrawal on Form 8889 lines 14a and 14b and its earnings in income. `f8889.unsupported`'s "a 2025 distribution that
withdrew excess contributions" is reworded to cover a withdrawal made in 2026 by the due date. Excess employer
contributions are computed when the filer says the excess is included in Form W-2 box 1. Otherwise they are refused,
because p969 p. 8 makes them "Other income" and line 8z's `other` kind is refused. / Keep `f8889.excess` refusing
all HSA excess. That does not change the coverage figure, but it leaves a computable case refused.

**D7. Parts III and IV (excess IRA contributions).** Keep them refused by the Stage 16 gates and D3(b). The current
year's traditional excess is now nearly computable (`person.ira_own_total` − `person.ira_limit`). But the Roth limit by
modified AGI (Pub. 590-A Worksheets 2-1 and 2-2) is not computed, since `person.ira_excess` asks it. The traditional
and Roth split of an excess, the year-end values, and the carry-in from the 2024 Form 5329 (lines 9 to 14, 18 to 22,
which feed the IRA deduction back through line 10) are also missing. / Compute the current year's traditional IRA
excess only (line 15, with a year-end value input), and refuse Roth excess and every carry-in.

**D8. Readings** (each an ambiguity-register entry).
(a) Line 1 holds only code 1 and S entries. i5329 p. 3's "early distributions includible in income" would on its
face take code 2 amounts too, with the same amount on line 2. That changes no tax.
(b) Line 4 is figured per person at the cent, as the form does. i1040gi p. 112 says per distribution ("multiply the
taxable amount of the distribution by 10%"), which can differ by a cent on the no-form path.
(c) The $5,000 for exception 19 is per person per birth or adoption. i5329 p. 5 says "a distribution of up to $5,000
if made during the 1-year period beginning on the date your child was born or adopted". p590b p. 28 says "must not
exceed $5,000 per taxpayer". The statute (72(t)(2)(H)) is not archived (D10).
(d) On a joint return the medical exception's excess over 7.5% of joint AGI is one amount, shared by both spouses'
forms. The archived text is silent.
(e) Exception 08 takes the filer's adjusted qualified education expenses as entered, including the K-12 tuition that
p590b p. 27 lists ("Additional qualified education expenses in connection with elementary and secondary tuition")
and i5329's "qualified higher education expenses" does not.
/ Any reading the other way. For (c), per taxpayer only. For (d), each spouse uses the whole excess.

**D9. Evidence.** UsTaxes is compared where its model is the form: IRA code 1 entries with no exception, its
`earlyWithdrawalAmount` set to the taxable amount, and whole-dollar amounts. That needs Form 1099-R distributions
mapped into its adapter for the first time. Tax-Calculator and OpenTaxSolver can only echo line 8, so they are not
counted. Ten blind returns cover: the no-form path with the box checked; code S at 25% beside code 1; one person with
several exceptions across entries (99 printed); the 09, 19, 22 and 23 caps across two entries; exception 05 binding,
alone and on a joint return; exception 12; both spouses with early distributions; code 3 on an IRA; and Part VII with
a year-end value below the excess. The official examples are added: Tom Jones (p590b p. 29, $3,000, $300) and the
teacher (p970 p. 56, Example 1). / Blind returns and examples only, with no adapter work. That is cheaper, but no outside
family then sees line 8 flow to the total tax.

**D10. Second printings.** Archive 26 U.S.C. 72 (for 72(t), the exceptions and D8(c)) and 4973 (for the HSA excess
definition and the year-end value limit), as `usc-26-36b` and `usc-26-25a` were archived for Stages 18 and 19. Leave
4974, 529, 530, Pub. 575, Pub. 721, Form 8915-F, i1099sa, Form 8853, Pub. 907 and Notices 2020-68, 2024-02 and
2024-55 unarchived, since what they cover stays refused. The caps of exceptions 22 and 23 then rest on p590b, in IRA
terms, for plan distributions too. / Rest Part I on i5329 and p590b alone.

Structure-changing: D1, D2 and D3. D1 decides who owns a Form 1099-R. It moves a collection that six Form 1040 lines,
Form 8880 and 115 fixture entries read, and it is the main decision. As in Stage 19, the atom vocabulary does not
change.

## Settled by the evidence (done this way unless you object)

1. **Form shape.** `f5329` is an implicit per-person form under `person`, as `f8606` is. `person` gains the totals it
   needs: `sum_over retirement` for lines 1 to 3 and the SIMPLE part, and `sum_over f8889` for line 47. That is the
   `person.hsa_addtax` pattern (verification error 5). `f5329` reads them. It gets two person-level tax totals: one
   for Part I, and one for the excess-contribution parts (Part VII now). That way TY2026's split of line 8 into lines 5
   and 18 is a relabelling.
2. **Downstream lines.** New `s2.line8` (`sum_over person` of the person's Form 5329 tax; "Additional tax on IRAs or
   other tax-favored accounts. Attach Form 5329 if required", f1040s2 p. 1) and a display Bool `s2.line8_box` (D5).
   `s2.line21` adds `s2.line8` (printed "Add lines 4, 7 through 16, 18, and 19", f1040s2 p. 2). Its only reader is
   `f1040.line23`, then `f1040.line24`, whose readers are two lines in f1040.yaml. Nothing reaches Form 1040 line 18,
   so no credit limit moves. Form 5329 reads AGI (through `sa.line4`) and the taxable amounts, so there is no cycle.
3. **Codes.** `retirement_code` gains `early_1`, `simple_S` and `disability_3` (D2). Code S is accepted only with
   `account = traditional_ira` (the IRA/SEP/SIMPLE box), and code 3 only on an IRA entry. `retirement.bad_code` keeps
   its Roth rule, so code J stays refused, and its remedy text lists the new codes. Two-code combinations stay
   `other`.
4. **`s2.other`.** It drops "the additional tax on early retirement distributions (often called a penalty)" and adds
   that Form 5329 Part I and the current year's HSA excess are figured, as it already does for Form 8889 line 17b. It
   keeps "or on an HSA you did not keep as an eligible individual (Form 8889 Part III)" and the rest. `f8889.excess`
   narrows to the employer excess not in box 1 (D6).
5. **Parameters**: `f5329.early_rate` 10/100 (f5329 line 4), `f5329.simple_rate` 25/100 (i5329 p. 5, "you must multiply
   that amount by 25% instead of 10%"), `f5329.excess_rate` 6/100 (f5329 line 49), and the caps $10,000, $5,000,
   $10,300 and $1,000 (i5329 p. 5; p590b pp. 27 to 28). `sa.medical_rate` is reused.
6. **Coverage bookkeeping.** `form5329` gets `"refused": false`, `"gates": []` and the label "(supported since Stage
   21; its remaining refusals are unmeasured gates)" (verification error 1). The new screens are unmeasured gates.
   `retirement.special` stays a gate in the forms.
7. **Fixtures.** The re-keying of D1. The 10 entries with `retirement.special` true and the 6 with code `other` are
   checked against the narrowed question and the new codes. So are the 9 cases with `s2.other` true (classm 3,
   stage12 2, stage4 2, stage18 1, stage8 1).
8. **Reviews.** The new `f5329` and every changed document (`retirement`, `person`, `f8889`, `s2`, `f1040`, `f8880`,
   `params`, the interview) are reviewed under Claude and deepseek-flash and adjudicated.
9. **Estimated tax penalty.** i1040gi p. 65 leaves "5329 (Parts III through IX only)" out of the tax shown on the
   return. The project does not compute the penalty (spec 2.2), so nothing changes.
10. **TY2026.** It is built on the final 2025 text and carried forward by year adoption. Part I and Part II taxes go
    to Schedule 2 line 5, and Parts III to X to line 18 (settled item 1). Exception 24 joins the Enum, and D3(a)'s
    December clause goes. Parts X and XI (Trump accounts) are refused by D3(b). The final 2026 text is checked when
    it posts.

## Verified and inferred

Checked against the tree at 2d971ad with the uncommitted Stage 19 build:
- `retirement.yaml`: the line list, no `collection.parent`, `retirement.special` (wording), `bad_code`, `taxable`,
  `show_a` (code-agnostic), and the `sav_*` lines.
- `params` `retirement_code` and `retirement_account`.
- The six Form 1040 readers and `f8880.dist_2025`.
- The `check.ts` `sum_over` rule.
- `s2.yaml`: all ids, the `s2.other` wording, `s2.line17c`, `s2.line18` and `s2.line21`.
- The readers of `s2.other`, `s2.line21` and `f1040.line24`.
- `f8889`: lines 2, 9, 12 and 13, `excess`, `unsupported`, `parent: person`.
- `person`: `hsa_addtax`, `ira_*` (excess, gate, limit, own total, dist), `sav_able`, `role`.
- `f8606` (implicit form under person), `oi8z` (kinds, `additional_tax`, no parent), `sa.agi_floor` through `sa.line4`.
- The `form5329`, `schedule2_other`, `ptc` and `education` entries in `categories.json`, and the report's coverage,
  share and gains.
- The SOI cells (rows by AGI).
- The fixture counts.
- The archive: present are f5329, i5329, p590a, p590b, p969, p970, f8889, i8889, f8606, i8606, f1099r, i1099r,
  f1099sa, f1040s2, i1040gi and plaw-119-21, and the 2026 drafts of f5329, i5329, f1040s2 and i1099r. Absent are 26
  U.S.C. 72, 4973, 4974, 529 and 530, i1099sa, p575, p721, f8915f, f8853, p907 and the three notices.
- UsTaxes `F5329.ts` (in full) and its Schedule 2 wiring; Tax-Calculator `e09900`; OpenTaxSolver `S2_8`; the
  PolicyEngine-US search.

In the sources: i5329 pp. 1, 2, 5 and 8 (who must file, joint returns, the disaster TIP, the exception table, 99, the 25%
rule, line 47); f5329 lines 4 and 49; f1040s2 lines 8 and 21; i1040gi pp. 65 and 112; i1099r pp. 18 and 20; p590b
pp. 4, 25, 27, 28 and 29; i8889 p. 8; p969 p. 8; p970 pp. 54 to 56; the 2025-to-2026 word diff of f5329, the 2026
Schedule 2 lines 5 and 18, and the 2026 i5329 What's New and exception 24; P.L. 119-21 secs. 70204, 70413, 71306 to 71308.

Taken from the verification without checking again: the other quotations and locators; that i5329 p. 8's line 12 and
i8889's line 13 agree.

Inferred:
- That most of the 5.1 million returns are Part I (from averages only), and that the +2.6 survives the refused parts.
- That the evaluator accepts `retirement` under `person` as it does `w2` (not run).
- That the codes' taxable-amount logic, never reached for code 1 or S, needs no change (read, not run).
- That December 30 to 31, 2025 long-term care distributions are rare enough to screen.
- The statutory reading of D8(c).
- The shares of every refused sub-situation (none measured).
- The coverage figure itself (read from the report; the estimator was not run, since it rewrites the report).
- The final 2026 text.
