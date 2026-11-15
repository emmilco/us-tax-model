# Lane notes: ra (round two, the questions with order numbers 100 to 169)

Branch `lane/ra`, cut from `provisional/interview-graph` at `926fb406`. Agent: `claude-fable-5-2`, class judgment, tax
year 2025, jurisdiction `us`. No paid call and no model call was made. Lines marked **RAN** were run and seen in this
worktree; **INFERRED** were not checked.

The range: who the return is for, about you, children and dependents, income the tool cannot prepare, jobs, tips and
overtime, care, other money received. Two other agents have 170 to 249 (`lane/rb`) and 250 to 319 (`lane/rc`).

## What whoever merges this branch must know first

1. **Two bank entries of lane rc's range were moved into this range**, because a tick-box screen of this range opens
   them: `person.work_ssn` (was 311/3, now 150/3) and `s8812.combat_pay` (was 310/2, now 158/2). If `lane/rc`
   renumbers the same two entries, take this branch's `order` and `seq` for them, or the groups `tips_overtime` and
   `care_help` fail `tick-groups` ("the answer opens ..., asked only after ..."). See "Work number and combat pay".
2. **One New York bank entry moved**: `ny_it201.ask.dependent_care` (`interview/ny/2025/questions.yaml`) from order
   1027 to 155/5, directly after the care screen that opens it (`tick-groups` asks for that).
3. **`interview/2025/full.yaml` has three more targets** (`s1.line10`, `s1a.line7`, `s1a.line15`), added as lines
   after the coordinator's relay said that file may be added to. See "Three direct targets".
4. **`scope.excess_deferral` (was 187/1, lane rb's range) is now a box of the W-2 screen (145/5)**, at lane rb's
   request relayed by the coordinator. The input is not renamed.
5. **One line of `engine/src/serve-check.ts` was changed.** The server test asserted that the only questions with a
   tick-box label are the three of `rare_credits`; with any other group in the bank it fails. It now asserts that
   of the cards of that group. The other two ranges will meet the same failure and may make the same edit.
6. `lane/tickrule` (`f009095a`) is merged here (`31064dff`): the groups are declared and checked under its rules, and
   its group `rare_credits` (290) is in the bank beside this range's thirteen.

## The tick-box groups

Thirteen groups (twelve in this table and the W-2 screen). Each member keeps its own prompt, help and answer; nothing in a form changed for a group.

| Group (order) | Heading | Boxes (member) |
|---|---|---|
| `about_you` (113) | Is any of these true of you (or, on a joint return, your spouse)? | Not a U.S. citizen at some time in 2025 (`scope.noncitizen`) · Under 24 at the end of 2025 (`scope.under24`; not on a joint return) · In the U.S. armed forces, reserves or National Guard since January 2022 (`scope.armed_forces`) · Leaving out income earned abroad, in Puerto Rico or in American Samoa (`sa.excluded_income`) · In a chapter 11 bankruptcy case at some time in 2025 (`scope.chapter11`) |
| `dependent_facts` (120, for each child or person listed) | Is any of these true of this person? | Lived over half of 2025 with another relative who could claim them (`dependent.other_claimant`) · Parents divorced, separated, or apart for the last 6 months of 2025 (`dependent.parents_apart`) · Has been married at some time (`dependent.ever_married`) · Had money of their own in 2025, or owned their home (`dependent.own_money`) |
| `child_extras` (126) | Does either of these apply to you (or, on a joint return, your spouse)? | Adopted a child, or paid adoption costs, since the start of 2024 (`s3.adoption_any`) · Reporting a child's 2025 interest or dividends on your own return (`scope.f8814`) |
| `own_income` (130) | In 2025, did you (or, on a joint return, your spouse) have any of these? | Anything you own rented out or offered for rent, or royalties (`scope.rental`) · Income or a loss from a partnership, S corporation, estate or trust (`scope.k1`) · Income or a loss from farming (`scope.farm`) |
| `work_kind` (140, for each person) | Did either of these describe your work in 2025? | Worked for a railroad (`person.rrta`) · K–12 teacher, counselor, principal or aide for 900 hours or more (`person.eligible_educator`) |
| `other_pay` (146) | In 2025, did you (or, on a joint return, your spouse) have any of these kinds of work or pay? | Wages, tips or strike benefits that are not on a W-2 (`scope.pay_no_w2`) · Medicaid pay for caring for someone who lives in your home (`scope.medicaid_waiver`) · Pay for work for a church or religious body, or as clergy (`scope.religious_work`) · A wage statement from Puerto Rico or another U.S. territory (`f8959.territory_w2`) · Employer stock options used to buy shares, or such shares sold (`s2.options_any`) |
| `tips_overtime` (150) | In 2025, did you (or, on a joint return, your spouse) get either of these at a job? | Tips (`s1a.tips`) · Overtime pay (`s1a.overtime`) |
| `tip_kinds` (151, for each employer with tips) | About the tips from this employer: is any of these true? | Some were for other work here that is not on that list (`tipjob.other_work`) · Some were service charges, negotiated amounts, or tickets, meals or goods (`tipjob.charged`) · Some of the work was against the law, or prostitution or pornography (`tipjob.unlawful`) |
| `care_help` (155) | In 2025, did you (or, on a joint return, your spouse) have any of these? | Care for a child or a dependent, so that you could work (`f2441.care`) · An employer's help with care costs, such as a dependent care account (`f2441.benefits`) · Someone you paid to work in your home: a nanny, housekeeper, gardener (`s2.household_help`) |
| `care_facts` (155, after a Yes to care) | About that care: is any of these true of you (or, on a joint return, your spouse)? | Some care was for someone other than your listed children under 13 (`f2441.care_other`) · Paid a bill in 2025 for care given in 2024 (`f2441.prior_year`) · A full-time student in each of 5 months of 2025 (`f2441.student`) · Unable to care for yourself at some time in 2025 (`f2441.unable`) · Your husband or wife died in 2025 (`f2441.spouse_died`; joint returns only) |
| `money_a` (160) | In 2025, did you (or, on a joint return, your spouse) get any of these? | Unemployment benefits (`s1.uc_any`) · Gambling or lottery winnings, or a prize or award (`s1.winnings_any`) · A scholarship, a fellowship or a grant for study (`s1.scholarship_any`) · Pay for serving on a jury (`s1.jury_any`) · An Alaska Permanent Fund dividend (`s1.alaska_any`) · Money from a hobby or pastime not run as a business (`s1.hobby_any`) |
| `money_b` (161) | Did any of these happen to you (or, on a joint return, your spouse)? | Alimony paid or received since the start of 2023 (`s1.alimony_any`) · A debt canceled or forgiven by a lender or card company (`s1.cod_any`) · A long-term care insurance payout, or life insurance paid early, in 2025 (`s1.ltc_payout`) · Pay in 2025 for work done while in a jail or prison (`s1.inmate_wages`) · Crypto received as pay, as a reward, or from mining or staking (`s1.digital_income`) · A deducted amount paid back to you (not a state tax refund) (`scope.recovery`) |

(The W-2 screen is under "Never ask twice".)

Why each is cut as it is, and what was decided against:

- **`about_you` has five of the nine facts about the person.** Left out, each for a cause seen in the build or the
  check and not for taste:
  - `sa.dependent` ("Can a parent or anyone else claim you as a dependent?") is asked alone, first (111/1).
    `person.blind` is not reachable until it is answered (`interview-order`, 75 of 79 walks), so it has to come
    before that question; and as a box it fails `tick-groups` on the New York profile (its answer opens
    `sa.sales_tax_wish`, order 201, which is then asked after a question of 200 that was waiting). **RAN**, on the
    merged rules.
  - `person.blind` is asked of each person, and a screen is all per person or all once per return.
  - `s3.disability_retired` is asked alone (118/1): as a box it fails `tick-groups` (its Yes opens
    `s3.elderly_credit`, order 318, asked after questions that were waiting). **RAN.**
  - `household.community_property` is answered Yes by everyone who lived in one of nine states, California and
    Texas among them: not a box most people pass over.
- **`refund.any` is not a box.** About four filers in ten answer Yes (`gate_frequencies.yaml`), and a Yes opens up
  to seventeen questions.
- **`scope.artist_official` is not in `other_pay`**, where it belongs by subject. It is asked only when a W-2 is
  listed, and `tick-groups` fails a group of which the background return (no W-2) is asked some members and not
  others. It is on the W-2 screen instead, whose five boxes are all asked only with a W-2.
- **Per-person screens** (`work_kind`) and per-entry screens (`dependent_facts`, `tip_kinds`): the engine and
  `draft-walk` show them; the tick lane's notes say the page and the server were tested for a per-person screen
  only on a planted group. **Not looked at in a browser here.**

## Never ask twice (N8)

- **The marks on a W-2: one screen, one look at the paper.** Lane 9's `scope.w2_marks` (box 13 "Statutory
  employee", box 12 code H) and lane 7b's `s2.w2_marks` (box 8, box 12 codes A, B, K, M, N, Z) and `s1.nqdc_pension`
  (box 11) are three different facts about the same paper, each refusing through a different old screen
  (`scope.schedule1`, `s2.other`, `s1.line8_other`). Making them one input was tried on paper and rejected: a Yes
  would then refuse at `scope.schedule1` whatever the mark was, and the rows that end at `s2.other` and
  `s1.line8_other` would change their expected end. They are now the boxes of one screen, `w2_jobs` (145), with
  `scope.artist_official` and `scope.excess_deferral`, asked only when a W-2 is listed:

  | Heading | Boxes |
  |---|---|
  | Do your (or, on a joint return, your spouse's) W-2s, or the jobs on them, show any of these? | An amount in box 8, or box 12 code A/B/K/M/N/Z (`s2.w2_marks`) · In box 11, money paid to you from a deferred pay plan (`s1.nqdc_pension`) · Box 12 code H, or box 13 “Statutory employee” ticked (`scope.w2_marks`) · Work as a performing artist, or as an official paid from fees (`scope.artist_official`) · More pay put into retirement plans at work than the yearly limit (`scope.excess_deferral`) |

  The boxes follow the paper (8, 11, 12, 13), then the two facts about the jobs. The last label leaves out the
  figure ($23,500), which is higher from age 50; the question behind the box has it.

  Model change for it (two gate lines, the technique of `s2.lookback_if_business`): `s2.w2_marks` and
  `s1.nqdc_pension` are asked only when a W-2 is listed (`s2.w2_marks_if_w2` in `forms/2025/s2.yaml`,
  `s1.nqdc_pension_if_w2` in `forms/2025/s1.yaml`, both reading lane 9's `scope.has_w2`). Their help said "With no
  W-2, answer No"; the form now gives that answer. This is lane 7b's request 1. A filer with no W-2 is asked two
  questions fewer.
  **For the owner:** the first label writes the six letters as "A/B/K/M/N/Z". Written "A, B, K, M, N or Z" the
  label is 16 words and the build allows 12. The better remedy is two inputs (box 8; the letters), which needs the
  651 fixture cases that state `s2.w2_marks` restated; not done.
- **Found, not merged** (each needs a fixture's facts restated, or a form outside this lane):
  - `scope.under24` ("Were you under 24 at the end of 2025?") is settled by `person.birth_year`, asked eight
    questions earlier. Lane 4b's derived line `person.edu_born_2002` is the same test; `scope.under24` could read
    it. Not done: the fixtures that answer `scope.under24: true` would need a birth year of 2002 or later, which
    moves their credits.
  - `f2441.spouse_died` ("Did your husband or wife die in 2025?", a box of `care_facts` on a joint return) is word
    for word `household.spouse_died_2025`. It could be derived from `household.married_dec31` and that answer.
  - `scope.pay_no_w2`'s help names "tips shown only in box 8", which is the first box of the W-2 screen.

## The ordering

| Order | Asked | Questions, in `seq` order |
|---|---|---|
| 100 | once | `$person` 1, `f1040.status` 2 |
| 101 | once | `household.ever_married` 1, `household.married_dec31` 2, `household.spouse_died_2025` 3 |
| 102, 103 | once | as lane 1 left them |
| 110 | each person | `person.birth_year` 1, `born_jan1` 2, `under16_at_year_end` 3, `died_at_64` 4 |
| 111 | once | `sa.dependent` 1 |
| 112 | each person | `person.blind` 1 |
| 113 | once | screen `about_you` 1 to 5; then what its boxes open: `scope.nonresident` 10, `scope.unearned_2700` 11, `scope.reservist_expenses` 12, `scope.military_move` 13, `scope.reservist_repaid` 14, `scope.f8615` 15 |
| 118 | once | `s3.disability_retired` 1 |
| 120 | each dependent | as lane 2a left it, with the screen `dependent_facts` at 13 to 16 |
| 126 | once | screen `child_extras` 1, 2; `s3.adoption` 3, `s3.adoption_earlier` 4, `s3.adoption_us` 5, `scope.adoption_benefits` 6 (was 127/2, away from its parent) |
| 130 | once | screen `own_income` 1 to 3 |
| 140 | each person, then each W-2 | screen `work_kind` 1, 2; `person.educator_expenses` 3; `$w2` 4; `w2.box1` to `box7` 5 to 11 |
| 145 | once | screen `w2_jobs` 1 to 5; `scope.performer_expenses` 6 |
| 146 | once | screen `other_pay` 1 to 5; `scope.clergy` 10, `scope.church_exempt_wages` 11, `s2.iso` 12, `s1.stock_options` 13 |
| 150 | once | screen `tips_overtime` 1, 2; `person.work_ssn` 3 (each person) |
| 151, 153 | each person, each employer | as lane 3 left them, with the screen `tip_kinds` at 151/3 to 5 |
| 155 | once | screen `care_help` 1 to 3; `s2.household_employee` 4; screen `care_facts` 6 to 10; `f2441.nondependent` 11; `w2.box10` 12, `w2.box10_wages` 13 (each W-2) |
| 156, 157 | | as lane 2b left them |
| 158 | once | `scope.care_benefits_other` 1, `s8812.combat_pay` 2 |
| 160 | once | screen `money_a` 1 to 6; then each box's questions in the boxes' order, 10 to 21 (`s1.uc_paid`, `uc_repaid`, `uc_unsupported`; `gambling_winnings`, `gambling_pro`, `prizes`, `olympic`; `scholarship_taxable`; `jury_pay`, `jury_to_employer`; `alaska_dividend`; `hobby_income`) |
| 161 | once | screen `money_b` 1 to 6; `s1.alimony` 10 to `alimony_unsupported` 13, `s1.cod_amount` 14, `s1.cod_unsupported` 15 |
| 165 | once | `refund.*` as lane 7a left it |

No bank entry of the range is below 100 or without a `seq`. Orders 127, 144, 148, 149, 152 and 168 are now empty.
`ftc.carryover` (order 10, no `seq`) is lane rb's (279/5 by lane 5a's notes).

Things about the order that are not as one would write them, each with its cause:

- **`sa.dependent` before `person.blind`**, and the birth year before both: `person.blind` is not reachable until
  `sa.dependent` is answered.
- **`s1.line8_other` reads its six items in one chain** (`forms/2025/s1.yaml`); the chain was reordered to the order
  of asking (`s1.nqdc_pension`, `s1.stock_options`, `s1.olympic`, `s1.ltc_payout`, `s1.inmate_wages`,
  `s1.digital_income`). The value of an `any` test does not depend on the order of its parts. At the base
  `s1.nqdc_pension` (148) was asked between two questions of 161 for that reason.

### Three direct targets (`interview/2025/full.yaml`)

`s1.line10`, `s1a.line7` and `s1a.line15` are asked for directly, as the health savings account block asks for its
three results. What each mends:

- **`s1a.line7`, `s1a.line15`: the tip and overtime employers are asked with their topic.** Before, a filer who
  ticked Tips was asked which employers gave the tips about 80 questions later (`09_tips_overtime`: 39 and 122). The
  cause is in `forms/2025/s1a.yaml`: `s1a.line13_amount` chooses between line 7 and line 7 less the phase-out on
  `s1a.line10_over`, a test of adjusted gross income, and a `choose` whose guard is not yet known does not look at
  its branches. Both branches read line 7; the engine cannot see that until every income question is answered.
  Overtime is built the same way (`s1a.line21_amount`). **RAN:** the server is now asked Tips and Overtime, her work
  number, her tip employer and its questions, her overtime employer and its questions, as questions 38 to 51.
- **`s1.line10`: the Schedule 1 questions of 145 to 165 are open in their own topics, and their refusals are told at
  once** ("Refusals", below). Before, Schedule 1 was read only through `f1040.line8`, behind the scope screens.

The condition of the order contract (1.6) is that the return reads the line whatever the answers are. `f1040.line8`
copies `s1.line10` always. `s1a.line7` and `s1a.line15` are read whenever Part II or Part III applies, and are zero
without reading a list when it does not (no Tips or Overtime, or no work number). That is my reading of the two
forms; what was **RAN** is the bar (the build's fixture walks, the fixtures, `interview-rules`, every row).

The alternative, not taken: change `s1a.line13_amount` and `s1a.line21_amount` to "line 7 less line 12" without the
choice (the same value). `engine/src/mutate.ts` and the class M fixtures name those lines.

The car loan's list (`s1a.line30_amount`, lane rb's topic) waits on adjusted gross income in the same way; a target
`s1a.line24` would be the same remedy. Not added: not this range.

## Work number and combat pay

`person.work_ssn` ("Do you have a social security number that allows you to work in the United States?") was at
311/3 and is at 150/3. A Yes to Tips or Overtime makes the return need it at once (Schedule 1-A counts tips and
overtime only for a person with such a number), and with the tip employers now asked in their topic it has to come before them (they are counted
only for a person with such a number). `tick-groups` also refuses a screen whose box opens a question that is then
asked behind questions that were waiting. For the same reason `s8812.combat_pay` was at 310/2 and is at 158/2, the end of
the care topic: Form 2441's earned income line needs it as soon as care is ticked (lane 2b's notes say the same).

What it costs: a filer who is asked the work number because of a credit, not tips, is now asked it in the jobs
topic, earlier than the return can know which of two spouses needs it. `02_couple_children_mortgage` is asked it of
both spouses (questions 64 and 65) where the base asked it of one (169): one question more. The persona's answer for
the second spouse was added (`person[taxpayer].work_ssn: true`).

## Refusals told at their question (N11)

What holds today, for this range. "At once" means on the filer's own Yes; "late" means the interview goes on and
the refusal shows at a later question.

| Refusals | Asked at | Told | Cause, and what was tried |
|---|---|---|---|
| The scope items themselves: `scope.nonresident`, `chapter11`, the armed forces children, `f8615`, `f8814`, `adoption_benefits`, `rental`, `k1`, `farm`, the W-2 marks, `performer_expenses`, `pay_no_w2`, `medicaid_waiver`, `clergy`, `church_exempt_wages`, `care_benefits_other`, `recovery` | 113 to 161 | at once | Lane 9's `scope.ready_*` lines. Unchanged |
| `sa.dependent`, `sa.excluded_income`, `person.rrta`, `household.rdp`, `household.cp_married` | 103 to 140 | at once (rows `opening.*`, `jobs.*`) | Unchanged |
| The Schedule 2 items of `s2.other`: `s2.w2_marks` (145), `s2.household_employee` (155) | 145, 155 | late, at `s2.amt_owed` (292) | **A true dependency as the form and its fixtures stand.** `s2.line2`, `s2.line3` and `s2.line21` each list the refusal `s2.amt` before `s2.other`, and `s2.amt` is not known until its last item, `s2.amt_owed`, is answered. Tried: `s2.other` first on `s2.line3` only (a refusal outranks an unknown in a sum, so one line with each order tells both at once). **RAN:** fixture `stage4.refuse.s2.amt.simultaneous` then fails, because it fixes the gate each of the three lines names when both are true (`s2.amt`). Undone. What would mend it: `s2.amt_owed` asked before 145 (it is lane rc's entry and by its nature the last question of its kind), or the engine telling a refusal that is already certain (order notes, part 6). Lane rb's new target `s2.other` opens these questions at their own numbers; it does not change when the refusal is told, since the refusal stands on the three lines and not on `s2.other` itself (**INFERRED** from the engine's rule; their branch was not run here) |
| `s2.iso` (146) | 146 | at once (row `other.iso_kept`) | `s2.amt` stands first in those lists and is true as soon as one of its items is |
| The Schedule 1 items: `s1.nqdc_pension` (145), `s1.stock_options` (146), `s1.olympic`, `s1.uc_unsupported` (160), `s1.ltc_payout`, `s1.inmate_wages`, `s1.digital_income`, `s1.alimony_unsupported`, `s1.cod_unsupported` (161), the `oi8z` items | 145 to 165 | **at once now** (were told at `scope.business_before`, 295) | The target `s1.line10`. Shown by the rows of `other.yaml`: eleven no longer answer `scope.business_before`, which they needed only to bring the refusal about |
| `s1.gambling_pro` (160) | 160 | late, at `s1.digital_income` (161) | The gambling line lists `s1.line8_other` first, and that is not known until its last item (the third box of the next screen) is answered. One screen late |
| `tipjob.other_work`, `tipjob.charged`, `tipjob.unlawful`, `otjob.special_rule` | 151, 153 | at once, and now asked in their topic | The targets `s1a.line7`, `s1a.line15` |

## What the merge of `lane/tickrule` undid

The groups were first built under the rules of `926fb406`, which named where every question a box opens must stand.
Three things done for those rules were taken back after the merge, because the merged rules leave placement to the
walk check: the marker `gated_by` on `household.credit_disallowed` is on the line again (the old rule read that
gate down to every scope item); `dependent.joint_return` is at 120/20 again, after `dependent.married`, as lane 2a
had it; and the questions the boxes of `money_a` open are in their natural order. `forms/2025/household.yaml` and
`interview/2025/coverage/dependents.yaml` (but for one added answer) are as at the base.

## Help (the questions a filer with one W-2 meets)

- The sentence that ends the help of a refusing question is cut to **"A Yes ends the interview here."** on the
  entries of this range (about fifty) that carried one of the two long forms ("A Yes ends the interview here: this tool cannot
  prepare a return with it." and "A return with this is outside what this tool prepares; a Yes ends the interview
  here."). The refusal screen itself says what the tool does not prepare. **The other two ranges still carry the
  long forms** (the map's 4.3); whoever merges should make them alike, one way or the other.
- Cut to about 40 words: `sa.dependent` (59 to 36), `sa.excluded_income` (53 to 36), `scope.pay_no_w2` (60 to 36),
  `person.rrta` (46 to 27), `s2.w2_marks` (48 to 26), `s1.nqdc_pension` (33 to 18; "With no W-2, answer No" is now the
  form's doing).
- `person.blind`: the prompt was 44 words as shown, most of it the limits an eye doctor must certify. It is now
  "Were you blind on December 31, 2025? (Partly blind counts only if an eye doctor has certified it in writing; the
  help gives the limits.)", and the help is the limits (41 words) without the two sentences on contact lenses and
  on keeping the statement. **For the owner:** this moves a rule from the prompt to the help, which N10 warns
  against. The right form is a child asked after "partly blind" (a change to `person.yaml`, not this lane's file).
- Deleted, as restating the question: the help of `refund.line5d_2024`, `refund.line5e_2024`, `refund.line17_2024`
  and `refund.mfs_spouse_itemized`. Deleted, as moot: the help of `w2.box2` (36 words on a W-2 of a U.S. territory;
  a filer with such a W-2 is refused at `f8959.territory_w2`).
- **Not touched:** `$person` (51 words of help) and `f1040.status` (115), which the owner approved as they stand.
  They are 166 of the help words this filer meets in the range.

## Model changes

All value-preserving; no expected value or refusal was edited.

| File | Change |
|---|---|
| `forms/2025/s1.yaml` | `s1.line8_other`: the six parts of the `any` test put in the order of asking. `s1.nqdc_pension`: `gated_by: s1.nqdc_pension_if_w2`, new gate line (asked only when `scope.has_w2`), and `s1.line8_other` reads the gate line |
| `forms/2025/s2.yaml` | `s2.w2_marks`: `gated_by: s2.w2_marks_if_w2`, new gate line, and `s2.other` reads the gate line |
| `interview/2025/full.yaml` | three targets (not a form; listed here because it changes what is asked when) |

Fixture inputs: none changed. (Every fixture states `s2.w2_marks` and `s1.nqdc_pension` as false; with no W-2 the
form now gives the same false.)

## Review debt

The two gate lines and every heading and label are wording and lines no review has read. The prompts and help
changed are listed above. `reports/` other than the coverage report, `gate_frequencies.yaml` and the files the
integration notes list as stale were not regenerated.

## Coverage rows and personas (answers only; no `expect` was edited)

| Row | Change | Why |
|---|---|---|
| `care.other_person_not_dependent` | adds `f2441.prior_year`, `f2441.student`, `f2441.unable`: false | the boxes of `care_facts` are asked before `f2441.nondependent`, which a box opens |
| `care.other_person_is_dependent` | drops `f2441.nondependent: false` | the row ends at `asks: f2441.prior_year`, which is now asked before that question. **This row wants a later expected end** (the question after `f2441.nondependent`) to show again what it was written to show |
| `dependents.citizen_with_number`, `saving.age_73_minimum_missed` | add `person[taxpayer].work_ssn: true` | the work number is asked at 150 |
| `saving.ira_too_much_left_in`, `saving.ira_recharacterized` | add `s8812.combat_pay: false` | combat pay is asked at 158 |
| `household.hoh_divorced`, `household.hoh_married_not_considered_unmarried`, `opening.living_apart_parent` | add `household.spouse_died_2025: false` | the three marriage questions are asked together at 101 |
| `other.w2_uncollected_tax`, `other.nqdc_pension` | use the new set `one_w2`; the first adds No to the other boxes of the W-2 screen, the second No to `s2.w2_marks` | the two questions are asked only with a W-2 |
| `other.professional_gambler` | drops `sa.gambling_losses`, `s3.foreign_any`, `s1.prizes`; adds No to `s1.ltc_payout`, `s1.inmate_wages`, `s1.digital_income` | the refusal now comes in its topic, when the last item of `s1.line8_other` (a box of the next screen) is answered |
| eleven rows of `other.yaml` (`options_income_not_on_w2`, `ltc_payout`, `nqdc_pension`, `inmate_wages`, `digital_income`, `olympic_medal`, `unemployment_fund_contributions`, `alimony_recapture`, `canceled_debt_exception`, `other_income_other_kind`, `recovery_item`) and four of `home.yaml` (`refund_other_year`, `refund_tax_paid_in_2025`, `refund_business_tax`, `refund_exception`) | drop `scope.business_before: false` (and `refund_exception` two 2024 figures) | **the refusal now comes on the row's own answer** (the target `s1.line10`); the dropped answers were there only to bring it about |
| `scope.performing_artist` | adds `scope.excess_deferral: false` | the box is on the W-2 screen |
| `scope.statutory_employee`, `scope.code_h`, `scope.performing_artist`, `scope.excess_deferral` | the set `one_w2` adds `s2.w2_marks: false` and `s1.nqdc_pension: false` | the W-2 screen |
| `jobs.no_w2_no_w2_screen` (new) | | a filer with no W-2 is not asked `s2.w2_marks`, `s1.nqdc_pension`, `scope.w2_marks` or `scope.artist_official` |

That both situations of each former pair still end where they did: `scope.statutory_employee` and `scope.code_h`
end at `scope.schedule1`; `other.w2_uncollected_tax` at `s2.other`; `other.nqdc_pension` at `s1.line8_other`. Each
passes with its `expect` as it was.

Personas: nine with a W-2 answer `s2.w2_marks: false` and `s1.nqdc_pension: false` (the questions are now opened by
their W-2); `02_couple_children_mortgage` answers `person[taxpayer].work_ssn: true`. No `who` and no `end` changed.

## Found and not fixed

- `s1.gambling_pro`'s refusal waits for the last item of `s1.line8_other` (a box of the next screen): the gambling
  line lists that screen first.
- `household.community_property` is asked of every filer not on a joint return, a never-married one included, who
  can only matter to it as a registered domestic partner. Asking `household.rdp` first would spare the list of
  nine states; a change to the lines in `household.yaml`, not made.
- `refund.any` to `refund.itemized`: a filer with a state refund who took the standard deduction in 2024 answers
  three refusal screens before the question that ends the topic. Reordering needs the form (`refund.yaml`) to read
  the 2024 choice first.

## Not finished, in rank order

1. The Schedule 2 refusals of this range (`s2.w2_marks`, `s2.household_employee`) are still told late ("Refusals").
2. `sa.dependent`, `person.blind` and `s3.disability_retired` are still three questions of their own between the
   birth year and the dependents (the causes are under "The tick-box groups"). Two screens of four and three were
   tried on the merged rules and failed the walk check for the two reasons given there.
3. The W-2 screen's first label and the split of `s2.w2_marks` in two.
4. The duplicates under "Found, not merged".
5. `walks/after/` was not rewritten (the three ranges would each rewrite all fourteen files); the figures below are
   from walks written to a scratch directory.

## Requests

1. **Coordinator:** the three targets are in this branch (above). Lane rb adds `sa.line17` and `s2.other` to the
   same list; both branches add lines, so the merge keeps all five.
2. **Tick lane or coordinator:** `tick-groups` fails a group when the background return is asked some members and a
   gate hides another (`scope.artist_official` in `other_pay`, where it belongs by subject); a member the walk will
   never ask need not be on the screen.
3. **Lane rc:** `person.work_ssn` and `s8812.combat_pay` (the head of these notes). Lane 2b's request stands:
   `s8812.combat_pay` beneath `scope.armed_forces` (a person who never served has no combat pay) needs a gate in
   `s8812.yaml`.
4. **Lane rb:** `scope.excess_deferral` is taken (145/5); delete any `order`/`seq` you set on it. `sa.gambling_losses`
   (204/7) directly after the gambling questions (lane 7a's request) was not taken up: its entry is in 200 to 249.
   The car loan's list waits on adjusted gross income as the tip list did; a target `s1a.line24` is the remedy.
5. **Owner of `person.yaml`:** a child beneath `person.blind` for the partly blind; `person.eligible_educator`
   is a box of `work_kind` whose label has to carry "900 hours", which is the one long label of the range.
6. **Whoever merges:** make the refusal sentence in help alike across the three ranges ("Help").

## Before and after, in this range

Counted by `draft-walk` on each persona's transcript, for the questions of this range only: a question counts when
its bank entry is at order 100 to 169 in the base bank or in this branch's (so `scope.excess_deferral`,
`person.work_ssn` and `s8812.combat_pay` count throughout), and, for the baseline, the old questions this range
replaced (`scope.schedule1`, `scope.other_income`, `scope.other_line16`, `household.married`, `person.under16`,
`person.age65`, `f8959.unsupported`, `s1.line8_other`, `s1.line8g` to `8r`). The three scope screens are counted
whole in the baseline though a few of their items went to later topics. A tick-box screen is one step; its prompt
words are its heading and labels; help words are all the help behind the questions asked, opened or not.

| Persona | | Steps | Questions | Prompt words | Help words |
|---|---|---|---|---|---|
| `01_single_w2` | baseline | 40 | 40 | 2,434 | 1,216 |
| | after round one | 55 | 55 | 913 | 1,360 |
| | now | 26 | 55 | 642 | 1,094 |
| `02_couple_children_mortgage` | baseline | 74 | 74 | 5,177 | 1,588 |
| | after round one | 81 | 81 | 1,550 | 1,874 |
| | now | 47 | 82 | 1,100 | 1,584 |
| `03_single_parent_child_care` | baseline | 65 | 65 | 4,848 | 1,497 |
| | after round one | 79 | 79 | 1,885 | 1,972 |
| | now | 44 | 79 | 1,548 | 1,656 |
| `09_tips_overtime` | baseline | 47 | 47 | 2,876 | 1,286 |
| | after round one | 67 | 67 | 1,186 | 1,765 |
| | now | 36 | 67 | 877 | 1,499 |
| `04_retired_couple` | baseline | 39 | 39 | 2,786 | 1,153 |
| | after round one | 50 | 50 | 1,049 | 1,341 |
| | now | 23 | 48 | 662 | 1,054 |

The 26 steps of the filer with one W-2: who the return is for; the status; ever married; the nine states; the birth
year; a dependent of someone else; blind; the screen `about_you`; retired on disability; the list of dependents;
`child_extras`; `own_income`; `work_kind`; the employer; five boxes of the W-2; `w2_jobs`; `other_pay`;
`tips_overtime`; `care_help`; `money_a`; `money_b`; the state refund. Of that filer's 1,094 help words, 166 are the
two questions the owner approved, and 422 of the single parent's 1,548 prompt words are one question,
`dependent.dc_paid` (lane 2b's notes give the children it needs, in `dependent.yaml`).

Whole walks (every range; `lane/tickrule`'s one group included): `01_single_w2` 125 questions on 94 screens, 2,287
prompt words, 3,282 help words (merged draft: 125, 125, 2,567, 3,548). `interview-order` on this branch before the
merge of `lane/tickrule` and before the targets: order numbers re-entered per walk 1.8, 1.8 and 2.0 (whole-return
fixtures, generated returns, minimal returns), where the merged draft had 4.5, 3.1 and 5.1; none of the
re-entries left is a question of this range. Its count of "gated questions not placed directly after their parent"
rises (65 to 84), because the other boxes of a screen stand between a box and what it opens.

## What I ran and saw, and what I infer

**RAN, on the tree of the last commit but for this file, the one line of `serve-check.ts` and the rendered forms:**
`tools/draft_check.sh` whole. Build OK (785 s). Fixtures 1854/1854. `interview-rules` 0 problems (177 walks, 415
random orders). Coverage rows 0 problems (448 rows). `tick-groups` passed (14 groups; 10 shown whole on the
background return, 4 not met by it: `dependent_facts`, `tip_kinds`, `care_facts`, `w2_jobs`). Person wording
current; the spouse-wording, check, draft-walk, interview-order and tick-groups self-tests passed; 1031 command-line
invocations; properties; twins 0 problems. Two steps were red in that run and were then mended and run alone:
`test-serve` (the assertion above; after the edit and a compile, 514 checks passed) and `render --check` (the
rendered Schedule 1 and Schedule 2 were stale; after `render`, current). **The whole check was not run again after
those two mends.**

`draft-walk` over the fourteen personas: 0 problems, every `end` as before.

The four groups the background return does not meet were looked at in the walks of `02`, `03` and `09` (the
screens as shown, and that what a box opens is asked next); `tick-groups` does not check them.

**INFERRED, not checked:** that the screens look right in a browser (none was opened; the per-person and per-entry
screens especially); that the three targets meet the order contract's condition for every return and not only the
fixtures, rows and generated returns the checks walk; that `lane/rb`'s targets and renumbering merge with this
branch without changing what was measured here.
