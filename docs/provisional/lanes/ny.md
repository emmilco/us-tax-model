# Lane notes: ny (the New York part of the interview)

Branch `draft/ny` (worktree `.claude/worktrees/provisional-ny`), cut from `draft/v2` at `709fee40`. Agent:
`claude-opus-5-5`, class judgment, tax year 2025, jurisdiction `ny`. No paid call and no model call was made. Lines
marked **RAN** were run and seen in this worktree; **INFERRED** were not checked.

Work in progress: this file is kept current as the lane goes. A successor reads it top to bottom, then "Not finished".

## Step 1 (done): measure

- `draft-walk` walks the `ny` profile: a persona may now say `profile: ny` and `extends: <persona>` (that persona's
  answers first, its own laid over them). The transcript's totals and `SUMMARY.md` give the New York stretch: the
  questions whose input is a line of a New York form (`ny_*`), wherever asked (`engine/src/draft-walk.ts`).
- Five New York personas in `interview/2025/personas/`: `ny01_single_nyc_w2` (extends `01_single_w2`),
  `ny02_couple_nyc_children` (the answers of `02` up to its end; see below), `ny03_retiree_gov_pension` (extends
  `04_retired_couple`), `ny04_refused_part_year` (extends `01`), `ny05_investor_nyc` (extends `06`).
- Baseline, never overwritten: `docs/provisional/walks/ny_before/` (the five transcripts and `SUMMARY.md`), walked on
  `709fee40` with only the walk tool and the personas added. **RAN.**

| Persona | NY questions | Steps | Prompt words | Help words | End |
|---|---|---|---|---|---|
| `ny01_single_nyc_w2` | 33 | 33 | 1,282 | 950 | complete |
| `ny02_couple_nyc_children` | 0 | 0 | 0 | 0 | refused at `ny_it201.gate.child_credit`, question 31 |
| `ny03_retiree_gov_pension` | 14 | 14 | 845 | 487 | refused at `ny_it201.gate.line26` |
| `ny04_refused_part_year` | 1 | 1 | 108 | 74 | refused at `ny_it201.gate.part_year_state`, question 128 |
| `ny05_investor_nyc` | 34 | 34 | 1,318 | 983 | complete |

**The first finding (RAN): a family with a child under 17 is refused by New York at question 31**, in the middle of
the federal dependents, before any New York question: the Empire State child credit (line 63, Form IT-213) is not
computed and its gate is figured from the federal dependents' ages. In the `ny` profile, which the page serves, such a
family therefore never reaches the rest of its federal return. Not a wording matter; it is in "Decisions for the owner".

## Step 2: the 44 questions redrafted

### Where the New York questions are asked, and why

The New York part stays after the federal part (orders 1000 to 1050), in six topics in the order of a life: where
you lived (1000), income as New York counts it (1010), deductions (1020), credits and other taxes (1030), things you
bought (1040), tax already paid and your refund (1050). One question stays inside the federal part:
`ny_it201.ask.dependent_care` at 155, directly after the federal care questions (N5; a federal agent put it there);
and the three 529 questions now sit at 180 (seq 40 to 42), directly after the federal account questions that open
them (N5). **RAN:** at 1010, `tick-groups` failed: ticking the federal box "A 529 plan, Coverdell or ABLE account"
(group `accounts`) opened `ny_it201.ask.ny_529`, which was then asked only after New York questions of order 1000
already waiting; a question a box opens must be asked in that box's topic. Consequence: a Yes to either 529 child
refuses in the federal part, as the child credit does (see Found).

Weighed per question, and why most cannot move into the federal topics:

- **Most New York questions now wait on a computed federal amount** (taxable interest and dividends, IRA and pension
  income, tax-exempt interest, other income, federal AGI, an overpayment or a balance due). By the order contract
  (`order.md` 1.6) such a question is asked the moment it opens, whatever its number, so placing it in a federal topic
  would not make it asked there; it would be asked late in some other topic. After the federal part every such amount
  is known, so the New York part is asked in its own order.
- **The two profiles share the federal part.** A New York item placed in a federal topic is asked only in the `ny`
  profile; the `full` profile's walk is unchanged either way. A filer who finishes the federal questions and then meets
  a short New York part knows which return each answer is for.
- **Residency opens the New York part** (N11): the city question, then (only after a No) the State question, then
  (joint only) the spouse, then the screen of facts about where you lived. Every line-1 refusal is told at its
  question. The alternative, residency as the very first question of the whole interview, would tell a part-year
  resident at question 1, but in the `ny` profile a refusal ends the walk, so such a filer would lose the federal return
  the page could otherwise give. A decision for the owner (below).

### What changed, by question (prompt words: before as shown to a single filer, now)

| Question | Now | Asked of | Model |
|---|---|---|---|
| `ask.state_resident` (108) | "Did you live in New York State for all of 2025?" (10) | only after a No to the city question | gated: `ny_it201.state_resident_if_not_city`; `gate.part_year_state` = active duty, or city No and State No |
| `ask.city_resident` (40) | asked first: "Did you live in New York City (the Bronx, ...) for all of 2025?" (19) | everyone | a Yes settles the State question (N8) |
| `ask.spouse_resident` (18) | "Did your husband or wife also live in New York City for all of 2025?" | joint returns (as before) | the city and State questions now ask about "you"; the spouse question carries the spouse, so a couple with one non-resident reaches `gate.spouse_nonresident` (before, the honest answer to the "(and your spouse)" question was No, refused at `part_year_state`) |
| (new) `ask.active_duty` | "At any time in 2025, were you (or, on a joint return, your spouse) on active duty in the U.S. armed forces?" | only when the federal `scope.armed_forces` is Yes | the old State question's "Answer No if you were in active military service"; feeds `gate.part_year_state`. The item G military codes (C7, K2, M4 to M9) are covered by it |
| `ask.special_accrual` (48) | parent tick-boxes `ask.moved_in`, `ask.moved_out`; the child "Was any of your income earned in one year but paid in the other ...?" | the child only after a move | `gate.special_accrual` chooses on `ny_it201.moved` |
| `ask.yonkers` (25) | tick-box "Lived, worked or kept a home in Yonkers in 2025" | everyone | none |
| `ask.special_code` (43) | **taken apart; the id is a derived line** (any of `bab_if_interest`, `ask.abroad`, `ask.installment`), so `gate.special_code` and its refusal are unchanged | | A6 `ask.bab` (only with interest, dividends or business income); E3/E5 `ask.abroad` and C2 `ask.installment` (tick-boxes near the end); C7, K2, M4 to M9 by active duty; D9 by `ask.decedent`; E4 by the federal nonresident refusal; Y1 by Yonkers; 56 (a Ponzi theft loss) needs itemizing, refused at `gate.itemize` |
| `ask.decedent` (14) | "Is this return for someone who has died?" (8) | everyone | the line-1 entry moved before `special_code` (which now waits for the last questions) so it is told at once |
| `ask.item_c` (25) | "You said no one can claim you ... Could a parent or someone else claim you if they filed a return ...?" | only after the federal `sa.dependent` No | `ny_it201.item_c` = federal Yes, or the New York answer (federal Yes implies New York Yes; New York's test is wider) |
| `ask.414h` (130) | parent `ask.public_job` "work for the government in New York, including a public school or college or the MTA?" (27); child "Does a Form W-2 from that job show a 414(h) retirement contribution (usually in box 14)?" (17) | parent only with a W-2 (`scope.has_w2`); child after Yes | `gate.line21` chooses on `public_job_if_w2`; the list of retirement systems moved to the child's help |
| `ask.us_obligation_interest` (37) | tick-box "U.S. Treasury or savings bonds, or a fund holding them" | as before (interest, dividends, business) | none |
| `ask.out_of_state_bond_interest` (39) | tick-box "Another state's bonds, or a fund holding them"; prompt "Did any of your tax-free interest or dividends come from bonds issued outside New York ...?" | only with tax-exempt interest (federal line 2a) | `gate.line20` chooses on `has_tax_exempt` |
| `ask.gov_pension` (103) | "Was any of your pension or retirement money from the federal government, the military, or a New York State or local government job?" (28); guard `ask.gov_pension_other` after a No: the MTA, MABSTOA, LIRR, SUNY/CUNY/SED plans (25) | as before (pension or IRA income) | gate line `gov_pension_if_income`; `gate.line26` = either question Yes |
| `ask.pension_exclusion` (64) | settled by the birth year: a recipient of taxable IRA or pension income born in 1965 or earlier is 59½ in 2025 (N8); otherwise "Did you ... turn 59½ by December 31, 2025, or receive any of that pension or IRA money as the beneficiary of someone who died?" (29) | pension income, no recipient born by 1965, after the government questions | `gate.line29` waits for the government questions (`pension_exclusion_after_gov`), so it is told in the New York part, not mid-federal; see "Found" |
| `ask.529_nonqualified` (160), `ask.529_owner` (33) | parent `ask.ny_529` "Is any 529 account you ... own part of New York's own 529 college savings program?"; children "In 2025, did you take money out of that New York 529 account for anything but college, career training or student loans? ..." (35) and "... put money into that New York 529 account, or take any out?" (16) | only when the federal `person.x_edu_account` is Yes for someone | `gate.line22`, `gate.line30` choose on `ny_529_if_account`. The beneficiary's taxable withdrawal of the old line-30 question is refused federally (`person.x_edu_taxable`) |
| `ask.inflation_check` (22) | "Was any of the other income you reported ... a New York State inflation refund check?" | only with federal other income (Schedule 1 line 9 not zero) | `gate.line25` reads `inflation_if_other_income` |
| `ask.it225` (49) | reworded, kept one question: "Does any item on New York's list of less common income changes (Form IT-225) apply ...? Most people have none." | everyone | none (see "Not finished") |
| `ask.itemize` (31) | split: the wish "Do you want to itemize deductions on your New York return instead of taking the New York standard deduction?" (19); `ask.spouse_itemizes` | wish: everyone; spouse: married filing separately only (federally refused, so never asked in the interview) | `gate.itemize` = any. See "ny_it201.ask.itemize" below |
| `ask.resident_credit`, `ask.noncustodial`, `ask.other_credits`, `ask.other_taxes`, `ask.contributions`, `ask.refund_529`, `ask.mctmt`, `ask.dependent_care` | reworded only | as before | none |
| `ask.city_credits` (30) | "Did your business pay New York City unincorporated business tax for 2025?" | only with a business (`s1.has_sc`) | the accumulation-distribution credit needs a trust K-1 (refused federally) and the part-year child care credit a part-year resident (refused at line 1): N8 |
| `ask.real_property_credit` (41) | "Was your rent $450 a month or less ..., or is all the real estate you own worth $85,000 or less?" | only with federal AGI of $18,000 or less and item C No (Form IT-214's first tests) | `gate.real_property` chooses on `low_income` |
| `ask.college_tuition` (13) | "You said college tuition was paid in 2025. Did you ... pay any of it yourselves?" | only when the federal `f8863.paid` is Yes | |
| `ask.owes_use_tax`, `ask.use_tax_st141` | reworded; the "or do you want the exact amount" half split off as `ask.use_tax_exact` | exact: after a No to the large purchase | `gate.use_tax_st141` = owes and (large or exact) |
| `ask.abode_part_year` | "Did you have a home in New York State for only part of 2025?" | as before | |
| `ask.other_withholding` (31) | "Was New York income tax taken out of any retirement, unemployment or other payment to you (not pay on a Form W-2)?" | only with IRA, pension, unemployment or other income | |
| `$ny_it2` | "List your Forms W-2 again ..." | as before | see "Not finished" (N8) |
| `ny_it201.line75` (75) | parent `ask.est_any` (35); the amount `ny_it201.line75_amount` beneath | | **line 75 is now a derived line** (the parent's choose); the input is `line75_amount` |
| `ask.prior_full_year`, `ask.prior_year_tax`, `ask.prior_agi_high` | reordered: the full-year question first (its No ends the part, sparing the other two) | balance due only (as before) | |
| `ask.late_penalty` (20) | "Will you pay the New York tax you owe after April 15, 2026, or file this return after its due date?" | only with a balance due (no penalty or interest on a refund) | `gate.late` chooses on `tax_due_positive` |
| `ny_it201.line79_amount` | parent `ask.apply_any` "Do you want any of your New York refund kept as a payment toward your 2026 New York tax ...?" | overpayment only | `line79` reads `line79_wanted` |

### The groups (tick-box screens)

| Group | Heading | Members and labels |
|---|---|---|
| `ny_where` (1000) | Did any of these apply to you (or, on a joint return, your spouse)? | `ask.yonkers` "Lived, worked or kept a home in Yonkers in 2025"; `ask.moved_in` "Moved into New York City on January 1, 2025"; `ask.moved_out` "Moved out of New York City on January 1, 2026". `ask.active_duty` follows as its own question (only after the federal armed-forces Yes): **RAN**, as a member it failed `tick-groups` ("Shown together") on the background return |
| `ny_interest` (1010) | Did any of your interest or dividends come from these? | `ask.us_obligation_interest` "U.S. Treasury or savings bonds, or a fund holding them"; `ask.bab` "Build America Bonds"; `ask.out_of_state_bond_interest` "Another state's bonds, or a fund holding them" (shown only with tax-exempt interest) |
| `ny_filing` (1050) | Do any of these apply to you (or, on a joint return, your spouse)? | `ask.abroad` "Outside the U.S. on April 15, 2026, and filing later"; `ask.installment` "Will ask to pay what you owe in installments"; `ask.contributions` "Giving to a New York State charity fund on this return" |

### `ny_it201.ask.itemize`

The coordinator's reading holds, checked against the instructions (`ny_it201i-html.txt` 523 to 531: "You may take
either the New York standard deduction or the New York itemized deduction"; "If you are married and filing separate
returns ..., both of you must take the standard deduction unless both of you choose to itemize"). The old question was
two: a comparison that needs Form IT-196 to answer, and a fact about a married-filing-separately spouse. Now:

- `ny_it201.ask.itemize` (the id kept, so every fixture's answer means the same thing to the model) asks the wish, of
  everyone. Either answer gives a correct return: No takes the standard deduction, which New York always allows; Yes
  refuses as before.
- `ny_it201.ask.spouse_itemizes` asks the spouse's choice, only married filing separately. The federal part refuses
  that status, so in the interview it is never reached; it keeps the model's case for fixtures.
- First built, the wish was asked only when the federal Schedule A held an amount New York itemizes. Taken out: the
  sum reads about twenty Schedule A questions, which the class M and mutation cases (whose inputs are complete, with
  no defaults) do not state, and the gate is a refinement, not a correctness matter.
- **Task, not done (new arithmetic):** tell a filer that itemizing would lower the tax. It needs Form IT-196 figured
  from what is already entered: the federal Schedule A amounts (mortgage interest, real estate and personal property
  taxes uncapped, gifts, medical over 7.5%, other), less state and local income taxes, with New York's own additions
  and subtractions (IT-196 lines 40 to 49) and the high-income limitation (lines 47 to 49 for New York AGI over
  $100,000), compared with the standard deduction. With that line, the question could be asked only of filers whose
  New York itemized deduction is larger, and could say so.

### Model changes (all in `forms/ny/2025/ny_it201.yaml`; no federal form edited)

- **Inputs added (14):** `ask.active_duty`, `ask.moved_in`, `ask.moved_out`, `ask.bab`, `ask.abroad`,
  `ask.installment`, `ask.public_job`, `ask.ny_529`, `ask.gov_pension_other`, `ask.spouse_itemizes`,
  `ask.use_tax_exact`, `ask.est_any`, `ask.apply_any`, `line75_amount` (the old line 75 input, renamed).
- **Inputs that became derived lines (same id, so every reader, gate and refusal is unchanged):**
  `ny_it201.ask.special_code` (any of its three items) and `ny_it201.line75` (the parent's choose over the amount).
- **Gates added or rewritten:** `state_resident_if_not_city`, `active_duty_if_armed_forces`, `gate.part_year_state`
  (active duty, or city No and State No), `moved`, `gate.special_accrual` (choose on `moved`), `bab_if_interest`,
  `item_c_if_not_federal` and `item_c` (federal Yes or the New York answer), `has_other_income`,
  `inflation_if_other_income`, `gate.line25`, `has_tax_exempt`, `gate.line20`, `public_job_if_w2`, `gate.line21`,
  `edu_people`, `has_edu_account`, `ny_529_if_account`, `gate.line22`, `gate.line30`, `gov_pension_if_income`,
  `gov_said_no`, `gov_pension_other_if_no`, `gov_pension_any`, `gate.line26`, `pension_59_people`,
  `pension_59_known`, `pension_exclusion_if_young`, `pension_exclusion_line`, `pension_exclusion_after_gov`,
  `gate.line29`, `spouse_itemizes_if_mfs`, `gate.itemize`, `gate.city_credits` (choose on `s1.has_sc`), `low_income`,
  `gate.real_property`, `gate.college_tuition` (choose on `f8863.paid`), `has_other_payments`,
  `gate.other_withholding`, `use_tax_exact_if_small`, `gate.use_tax_st141`, `apply_if_overpaid`, `line79_wanted`,
  `line79`, `gate.late` (choose on `tax_due_positive`).
- **Federal lines now read by New York:** `scope.armed_forces`, `scope.has_w2`, `sa.dependent`, `f1040.line2a`,
  `person.x_edu_account`, `person.birth_year`, `person.ira_taxable`, `person.plan_taxable`, `s1.line9`,
  `f1040.line4a`, `f1040.line5a`, `s1.line7`, `s1.has_sc`, `f8863.paid`, `f1040.status`.
- **Refusal list of line 1:** the `gate.decedent` entry moved before `gate.special_code` (nothing else of any refusal
  changed: gate, form, remedy, citation).
- **`gated_by` left off on purpose** where the question opens on the closed (No, zero) answer of its parent:
  `ask.state_resident`, `ask.item_c`, `ask.gov_pension_other`, `ask.pension_exclusion`, `ask.use_tax_exact`,
  `ask.real_property_credit`, `ask.other_withholding`, `ask.late_penalty`. The minimal return of the checks closes
  every gated input, and these open on that return's answers (interview-rules' `minimalAnswers`); the gate line still
  hides each, as for the Count inputs (`l9.md`, "Found" 2). Also left off: `ask.spouse_itemizes` and
  `ask.college_tuition`. **RAN:** with the marker, `f1040.status` and `f8863.paid` became existence gates and
  interview-rules' minimal returns failed ("f1040.status = mfj alone: ends refused", for both profiles; "f8863.paid =
  true alone: person[taxpayer].tin ... never asks it"), properties of federal forms the markers only exposed.
- **Engine:** `engine/src/generate.ts` (`NY_IN_SCOPE`: the in-scope answer of each new Bool, `special_code` removed;
  `est_any` true so the estimated payment amount is drawn as before); `engine/src/interview-rules.ts`
  (`MINIMAL_BASE.ny` answers `ny_it201.ask.city_resident` Yes: its No no longer refuses at once, so the closed answer
  left the background walk on a gated question); `engine/src/draft-walk.ts` (step 1).
- **Bank and profile:** `interview/ny/2025/questions.yaml` rewritten (prompts in the bank where the form's source is
  the old one; three groups); `interview/ny/2025/ny.yaml` lists the new inputs and drops `special_code` and `line75`.

### Fixtures (inputs only; no expected value or refusal edited)

Rewritten by `/tmp/nywork/refix.py` (kept in `docs/provisional/lanes/ny_work/refix.py`) from the files at `709fee40`:

- `ny_it201.ask.special_code: true` became `ny_it201.ask.abroad: true` (one case, `ny.refuse.special_code`; and the
  regression case `ny.reg.choose.status_unanswered_refused_income`); `false` was dropped.
- `ny_it201.line75: X` became `ask.est_any: true` and `line75_amount: X` (X > 0), else dropped (or `est_any: false`).
  `line79_amount` above zero gained `ask.apply_any: true`.
- A case answering Yes to a question now behind an earlier fact gained that fact: special accrual (`moved_out`),
  414(h) (`public_job`), the 529 questions (`person[taxpayer].x_edu_account`, `ny_529`), other states' bonds
  (`f1040.tax_exempt_interest` $500), the inflation check (a line 8z item, kind `kickbacks`, $270: the only line 8z
  kinds the federal part prepares; see "Found"), itemizing (none needed once the wish is asked of everyone; the case
  states a $600 personal property tax from an earlier build, harmless), city credits (a Schedule C), college tuition
  (`f8863.paid`), other withholding (a pension 1099-R), the real property credit (one W-2 of $15,000 in place of two
  of $78,000: the credit needs federal AGI of $18,000 or less, so the case as written described an impossible filer).
- Five cases withheld `f1040.tax_exempt_interest` (`null`); New York now reads it, so they state 0 (the default).
- Class M and mutation cases state every answer (no defaults): they gained the new questions the model now reaches,
  each No or zero (`moved_in`, `moved_out`, `abroad`, `installment`, `public_job`, `bab`, `apply_any`, `sa.dependent`,
  `person[...].x_edu_account`, `f1040.tax_exempt_interest`, and where reached `use_tax_exact`, `gov_pension_other`,
  `spouse_itemizes`). Hence the large diff of those files.
- `fixtures/ny/2025/defaults.json`: defaults for the 14 new inputs; `special_code` and `line75` removed.

### Coverage rows

`interview/2025/coverage/ny.yaml` (new, profile `ny`), 32 rows: the residency paths (city No and State Yes or No; the
State question not asked after a city Yes; active duty; a spouse elsewhere; Yonkers; a move with and without accrued
income; a decedent), item C after a federal No, the three items of `special_code`, 414(h) with and without the
contribution, Treasury interest, other states' bonds, both government pension questions, the pension exclusion by
age (not asked) and as a beneficiary, the three 529 paths, IT-225, the itemizing wish, the resident credit, the real
property question not asked above $18,000, the use tax exact and large paths, the charity fund.

Not covered by a row, and why: item C settled by a federal Yes (`sa.dependent` Yes refuses federally first); the
spouse who itemizes (married filing separately is refused federally); the real property credit asked (every filer
with federal AGI of $18,000 or less is refused first at `gate.eic`, which New York figures from the federal earned
income credit's limit, so the question is reachable only through fixtures, as before through a wrong Yes).

### Cost and share (NORMS section 3; my judgment, not measured; the owner rates costs himself)

| Question | Asked of | Share Yes | Cost Yes / No | Who could answer No wrongly; the guard |
|---|---|---|---|---|
| `city_resident` | everyone | ~95% of users | 1 / 1 | A New Yorker away at school or abroad for a stretch: the help counts time away |
| `state_resident` | city No | ~50% | 2 / 1 | Either answer refuses; it only picks the remedy |
| `ny_where` screen | everyone | ~2% | 1 / 1 | A Yonkers commuter who works there but lives in the city: "worked" is in the label |
| `special_accrual` | after a move | ~20% | 5 / 3 | |
| `decedent` | everyone | <1% | 1 / 1 | |
| `item_c` | federal No | ~3% | 5 / 3 | 31 words; a student whose parent need not file |
| `public_job` | W-2 holders | ~15% in the city | 1 / 1 | A SUNY or MTA worker who does not think "government": named in the prompt |
| `414h` | public job Yes | ~60% | 5 / 5 (a glance at box 14) | |
| `ny_interest` screen | interest, dividends or business | ~15% | 2 / 1 | A fund holding Treasuries: in the label |
| `gov_pension` | pension or IRA income | ~30% in NY | 1 / 1 | LIRR, MABSTOA, SUNY ORP: the guard `gov_pension_other` |
| `pension_exclusion` | pension income, no recipient born by 1965 | ~5% | 2 / 2 | A beneficiary: named |
| `ny_529` | someone has a 529, Coverdell or ABLE | ~50% | 2 / 2 | An owner of an account bought through an adviser that is another state's plan: help |
| `529_nonqualified` | NY 529 Yes | ~5% | 5 / 3 | K-12 tuition: named in the prompt |
| `inflation_check` | federal other income | ~5% | 1 / 1 | |
| `it225` | everyone | ~1% | 20 / 5 | A residual catch-all: see "Not finished" |
| `itemize` | everyone | ~10% | 5 / 2 | A homeowner who would gain by itemizing and says No: gets a correct, dearer return; the help gives the standard deduction amounts |
| `resident_credit` | everyone | ~5% in the city | 2 / 1 | |
| `noncustodial` | everyone | ~1% | 1 / 1 | |
| `other_credits`, `other_taxes` | everyone | ~1% | 5 / 3 | Residual catch-alls |
| `owes_use_tax` | everyone | ~20% (honest) | 3 / 2 | |
| `other_withholding` | IRA, pension, unemployment, other income | ~30% of those | 3 / 3 (a glance at the forms) | |
| `est_any` | everyone (after the W-2 records) | ~10% | 2 / 1 | A 2024 refund applied forward: named |
| `ny_filing` screen | everyone | ~1% | 1 / 1 | |

### Where I was unsure

1. **Active duty refuses at `part_year_state`.** The old State question said "Answer No ... if you were in active
   military service", so every servicemember was refused with the part-year remedy. The instructions say active
   service only takes a person out of the 184-day statutory-resident test (`ny_it201i-html.txt` 1732); a servicemember
   domiciled in New York is a resident. I kept the refusal (N9); it is wider than the law and its remedy text ("files
   Form IT-203") does not fit a domiciled New Yorker in uniform.
2. **"A college dorm does not count as a home"** is in the city question's help only. The old question refused a
   filer whose only New York residence was undergraduate housing; such a student (domiciled elsewhere) is the one
   person who could answer the city question Yes wrongly. The rule is narrower in law (it concerns the permanent
   place of abode, not domicile); I kept the old over-refusal and put it in help, not the prompt.
3. **The city question asks about "you"** and the spouse question about the spouse; before, both residency questions
   said "you (and your spouse)". A couple with one non-resident now ends at `gate.spouse_nonresident`, the refusal
   written for exactly that case, where the honest answer before ended at `part_year_state`. Both refuse.
4. **`pension_exclusion` derived from the birth year** uses "born in 1965 or earlier" (59½ by June 30, 2025 at the
   latest) and asks the rest; a 1966 recipient who turns 59½ in 2025 is asked. Its prompt asks whether "you or your
   spouse" turned 59½, which can over-refuse a couple where only the non-recipient did.
5. **`it225`, `other_credits`, `other_taxes`** are still catch-alls (reworded, examples personal). Taking them apart
   needs the IT-225 and IT-201-ATT lists read item by item.
6. **`real_property_credit`** now asks the rent or home-value tests; the old question asked "might you qualify",
   leaving them to the filer. Only filers with federal AGI of $18,000 or less are asked, and in the interview all of
   them are refused first at `gate.eic` (see Found).
7. **The itemizing wish is asked of everyone** (19 words). See "`ny_it201.ask.itemize`".
8. **The 529 parent asks "own"**: an account someone else owns for you counts as No. That matches the old line-30
   question ("as an account owner"); the old line-22 question said "you made a withdrawal", which only an owner does.

### Found, not fixed

1. **A family with a child under 17 is refused at question 31** (step 1). Unchanged.
2. **Every filer with federal AGI at or below the federal earned income credit's limit is refused by New York**
   (`gate.eic`, decision B9) as soon as AGI is known, which is mid-federal in the `ny` profile. So the real property
   credit question is never reached in the interview (its limit, $18,000, is below every EIC limit).
3. **A retiree 59½ or older with private pension or IRA income is always refused** (line 29 is not computed). With
   the birth-year derivation the refusal needs no question; I tied it to the government pension answers so it is told
   in the New York part, not in the federal retirement topic (where it would end the walk mid-federal, like 1 and 2).
4. **The inflation refund check cannot be in federal income except as one of the two line 8z kinds the federal part
   prepares** (RTAA, kickbacks); every other line 8z kind is refused federally. So the question is near-unreachable
   honestly.
5. **The New York W-2 records repeat the federal W-2 list** (`$ny_it2`, "List your Forms W-2 again"). N8 wants the New
   York boxes asked per federal W-2 entry, in the W-2 topic. That needs the IT-2 lines on the federal `w2` collection
   (or a New York collection keyed by it), and every New York fixture's `$ny_it2` entries restated onto W-2 entries.
   Not done: a model change across the federal W-2 form and about 200 fixtures.
6. **`div.box12` is now asked of a dividend holder in the `ny` profile** where the `full` profile does not ask it
   (persona `ny05`): New York reads federal line 2a for the other-states' bonds question. Correct, but a question the
   federal walk skips.
7. `household.spouse_died_2025` (federal) would settle `ask.decedent` for a widow on a joint return; not used.

### Review debt

Every reworded New York prompt and help, the three headings and ten labels, every new input and gate line of
`ny_it201.yaml` (cited to existing passages; the citation of `ask.spouse_itemizes` quotes `ny_it201i-html.txt` 531;
`low_income` cites `ny_it214i` p. 1), and the restated fixture inputs. No transcription, render, class M, screen or
question review was run; their New York logs are stale. `rendered/` and `reports/` beyond what the checks write were
not regenerated by hand.

## Before and after (RAN: `draft-walk`; before `walks/ny_before/`, after `walks/ny_after/`)

The New York stretch (questions of New York forms, wherever asked; a tick-box screen is one step):

| Persona | Before: questions / steps / prompt words / help words | After | End (unchanged) |
|---|---|---|---|
| `ny01_single_nyc_w2` | 33 / 33 / 1,282 / 950 | 27 / 23 / 519 / 713 | complete |
| `ny02_couple_nyc_children` | 0 (refused at question 31) | 0 (the same) | `gate.child_credit` |
| `ny03_retiree_gov_pension` | 14 / 14 / 845 / 487 | 10 / 7 / 164 / 314 | `gate.line26` |
| `ny04_refused_part_year` | 1 / 1 / 108 / 74 | 2 / 2 / 30 / 98 | `gate.part_year_state` |
| `ny05_investor_nyc` | 34 / 34 / 1,318 / 983 | 29 / 24 / 542 / 785 | complete |

Whole walks: `ny01` 160 questions, 92 screens, 3,057 prompt words before; 155, 83, 2,314 after. `ny05` 187, 119,
3,797 before; 184, 111, 3,057 after (it now also meets `div.box12`, Found 6). The part-year resident (`ny04`) reads 30
words where it read 108, at one more question (the State question after the city No picks the remedy).

## Not finished, in rank order

1. **The W-2 records asked twice** (Found 5): the largest N8 failure left; every W-2 filer re-lists their W-2s.
2. **The three catch-alls** `it225`, `other_credits`, `other_taxes` (about 70 words asked of everyone): take each
   apart against the IT-225 and IT-201-ATT lists, as lane 9 did for the federal screens.
3. **`noncustodial`, `resident_credit`, `owes_use_tax`** are still asked of everyone; a tick-box screen of rare
   credits is possible but these are of different kinds (child support, tax paid elsewhere, purchases); not grouped.
4. **The itemizing comparison** (new arithmetic, Form IT-196): see "`ny_it201.ask.itemize`".
5. `prior_agi_high` and `prior_year_tax` are asked in the model's order (the AGI question first) though the bank
   numbers the tax first: `safe_harbor` chooses on the AGI answer before it reads the tax. Harmless.
6. `ny01`'s withholding leaves a small balance due, so it meets the prior-year questions; a refund persona would show
   the `apply_any` and 529-deposit questions. Not added.

## Decisions for the owner

1. **Children under 17, a low income, a pension at 59½: New York refuses mid-federal in the `ny` profile** (Found 1
   to 3). Each refusal is computed from federal answers, so it fires as soon as they are given, and the page then
   offers no federal return. Options: keep (N11, told at its topic); or hold every New York refusal until the federal
   part is complete (a change to the profile or the engine: e.g. New York targets read only after a "federal part
   done" line); or compute the Empire State child credit and the New York earned income credit (new arithmetic, by far
   the most valuable New York work: they decide most families and low earners).
2. **Residency first in the whole interview?** Kept at the start of the New York part. Asking it at question 1 tells a
   part-year resident at once but costs them the federal return the page gives today (see 1).
3. **Active duty refuses as before** (Unsure 1): keep, or ask whether New York is the servicemember's home.
4. **The itemizing wish of everyone**, or only of filers with Schedule A amounts (a gate that pulls about twenty
   Schedule A questions into every New York case; tried and taken out).
5. **The 529 questions in the federal account topic** (order 180): their Yes refuses there, mid-federal.

## Checks on the final tree (RAN, tree 7663dfec1b59, before the commit of step 2)

`tools/draft_check.sh` (whole): **green**, all sixteen steps: build OK; fixtures 1854/1854; interview-rules 0
problems (177 walks, 415 random orders; baseline untouched); interview-coverage 0 problems (the 32 new rows with the
rest; 1,130 s); tick-groups passed (`ny_interest` not met by the background return, checked by personas `ny03`,
`ny05`); person wording current; spouse-wording, check, draft-walk, interview-order and tick-groups self-tests;
integration 1030 CLI invocations; properties; test-serve 506 checks (18 New York fixture paths); twins 0 problems;
render current. Then `test-fixtures --ny` 338/338; `properties --ny` 2 properties over 400 returns, 0 failing;
`draft-walk` over all 19 personas (14 federal, 5 New York), 0 problems, each at its stated end.
