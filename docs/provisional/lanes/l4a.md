# Lane notes: 4a (retirement money received; social security)

Branch `lane/l4a`. Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no
model call was made. Form files: `forms/2025/retirement.yaml`, `forms/2025/ssb.yaml`. Bank entries: `$retirement`,
`retirement.*`, `ssb.*`. Order numbers: 170 (retirement money received), 178 (social security), 179
(`ssb.lived_apart`, reached only on a separate return), 317 (`retirement.sav_*`).

## How the work is reproduced (for a successor)

The model and data changes are made by five scripts in `docs/provisional/lanes/l4a_work/`, each run from the worktree
root. The first two refuse to run twice (they were run on the forms as they stood at `100b132c`; three question texts were
shortened afterwards in the form file and in the script's list together); the other three can be rerun.

| Script | Does |
|---|---|
| `gen_retirement.py` | rewrites `forms/2025/retirement.yaml`: the items of `retirement.special` and `retirement.code_screen` as gated questions, the old ids kept as derived lines; `rollover` beneath `rollover_any`; `annuity` beneath `cost_any`. The question texts are its `ITEMS` list |
| `gen_ssb.py` | rewrites `forms/2025/ssb.yaml`: `ssb.any`; `ssb.pub915` derived; `ssb.prior_year_pay` and `ssb.lump_elect` |
| `apply_data.py` | rewrites fixture **inputs** (never expected values), `fixtures/2025/defaults.json` and the input lists of the `sales` and `stage4` profiles |
| `bank.py` | writes every bank entry of the lane (order, `seq`, prompt, help, labels). To change a wording that lives in the bank, edit `ENTRIES` there and rerun. A question whose words are the form line's label is changed in the form YAML (label and `source`, kept identical) |
| `coverage.py` | writes `interview/2025/coverage/retirement.yaml` from the same path tables |

To change a question's words: label and `source` in the form file (most new questions), or `bank.py` (the ones with a
`prompt`). Then `npm run build --silent`, `tools/draft_check.sh --quick`, `node engine/dist/main.js draft-walk`.

## What changed, by question

### Retirement money received (order 170)

The 411-word `retirement.special` ("Does this distribution involve any of these?", 23 items, shown for every Form
1099-R) is no longer a question. It is a derived line, true when any of the questions below that refuse is answered
Yes, so the three lines that refuse on it (`retirement.rolled`, `retirement.taxable`, `retirement.amount_a`) and their
refusal text are unchanged. Each of its 23 items is now reached only from the answer that makes it possible:

| Old item of `retirement.special` | Now asked by | Asked when |
|---|---|---|
| disability pension before minimum retirement age | `disability` (parent), then `dis_early` | a plan (not an IRA) |
| pension partly excludable, terrorist attack | `dis_terror` beneath `disability` | a plan |
| military disability pension | `dis_military` beneath `disability` | a plan |
| corrective distribution of excess deferrals or contributions | **the code**: box 7 codes 8, P and E are the choice "Any other code", which `retirement.bad_code` refuses | every form |
| qualified charitable distribution or HSA funding distribution | `charity_hsa` | an IRA |
| nondeductible contributions to any traditional IRA | `ira_basis` | a traditional IRA |
| conversion (Form 8606); rollover to a Roth IRA or designated Roth account | `roth_moved` beneath `rollover_any` | some of the money went into another retirement account, or code G |
| recharacterization | **the code** (N or R, "Any other code") | every form |
| 2024 or 2025 IRA contribution returned; earlier excess returned in 2025 | `ira_returned` (and codes 8 and P by the code) | an IRA |
| lump-sum distribution reportable on Form 4972 | `born_1936` (parent), then `lump_sum` | a plan |
| employer securities, net unrealized appreciation | `box6` (the paper) | a plan |
| nonperiodic payment at or after the annuity starting date | `lump_at_start` beneath `cost_any` | a plan with after-tax cost |
| distribution wrongfully levied, returned and contributed back | `levy_returned` beneath `rollover_any` | money went into another retirement account |
| nonqualified annuity | `own_annuity` beneath `cost_any` (and code D with another code, by the code) | a plan with after-tax cost |
| retired public safety officer premium exclusion | `pso_exclusion` (a wish: "To go on without it, answer No") | a plan |
| death benefit exclusion | `death_exclusion` | a plan, code 4 |
| beneficiary of an employee who died before retiring; guaranteed payments; shared annuity | `ben_before_retire`, `ben_guaranteed`, `ben_shared` | a plan, code 4 |
| rollover of property other than cash | `rollover_property` beneath `rollover_any` | money went into another retirement account |
| rollover under a qualified domestic relations order | `rollover_qdro` beneath `rollover_any` | money went into another retirement account |
| qualified disaster recovery distribution, repayment, recontribution | `disaster` | every form |
| plan loan offset | `loan_offset` (and codes M and L by the code) | a plan |
| Form RRB-1099-R | **the code**: the form has no code in box 7; the choice reads "…or no code at all (a Form RRB-1099-R has none)", which `retirement.bad_code` refuses | every form |
| civil service alternative annuity option | `csrs_alt` beneath `cost_any` | a plan with after-tax cost |
| annuity starting date before November 19, 1996; the General Rule | `start_1996`, `general_rule` beneath `cost_any` | a plan with after-tax cost |

Other changes in the topic:

- `retirement.code_screen` (90 words, asked of every code 7, 4 and 2) is a derived line over `under59` (code 7:
  "Were you under age 59½ when you received any of this money?"), its child `sec457`, `code2_partial` (code 2) and
  `not_beneficiary` (code 4). `retirement.screen_refused` reads it as before.
- `retirement.rollover` (239 words, asked of every form) is asked only after a Yes to the new parent
  `retirement.rollover_any`; its bank prompt is one line.
- `retirement.annuity` (141 words, asked of every plan) is asked only after a Yes to the new parent
  `retirement.cost_any`; its bank prompt is one line. With no after-tax cost the Simplified Method cannot apply (its
  second condition), so a No to the parent gives the same result as a No to the old question.
- `$retirement` is worded as a question; `account` and `code` have a one-line prompt and plain labels, the common
  answer first.
- `retirement.early_screen` keeps its input; its bank prompt is a bulleted list of six items. Its seventh, a
  qualified disaster recovery distribution, is asked by `retirement.disaster` of every form (the asker refuses at the
  same lines, `retirement.taxable` and `retirement.amount_a`).
- The boilerplate help is gone from every entry of the lane.

### Social security (order 178)

- New parent `ssb.any` over the amount `ssb.benefits`.
- `ssb.pub915` (62 words, six items) is a derived line over two questions: `ssb.ira_covered` and `ssb.repaid_more`
  (by the paper: box 4 more than box 3). Its other four items are deleted as asked elsewhere (N8, map 2.7):
  Forms 2555 and 4563 and the Puerto Rico exclusion by `sa.excluded_income` (asked of everyone, refuses directly);
  employer adoption benefits by `scope.other_income` today (asked of everyone, refuses directly) and by lane 9's
  `scope.adoption_benefits` after the merge; Form 8815 by `sb.unsupported` (see "Unsure").
- The lump-sum election (`ssb.lump_sum`) is asked as a wish, `ssb.lump_elect`, only after the paper fact
  `ssb.prior_year_pay`. `ssb.lump_sum` stays as the gate line, so the refusal's gate id is unchanged.
- `ssb.terror_disability` has a one-line bank prompt (the September 11 rule is in its help).

## Ids

Added (`retirement.`): `rollover_any`, `roth_moved`, `rollover_property`, `rollover_qdro`, `levy_returned`,
`charity_hsa`, `ira_returned`, `ira_basis`, `box6`, `loan_offset`, `disability`, `dis_early`, `dis_terror`,
`dis_military`, `pso_exclusion`, `born_1936`, `lump_sum`, `death_exclusion`, `ben_before_retire`, `ben_guaranteed`,
`ben_shared`, `cost_any`, `own_annuity`, `csrs_alt`, `start_1996`, `general_rule`, `lump_at_start`, `disaster`,
`under59`, `sec457`, `code2_partial`, `not_beneficiary` (32 inputs), with a gate line `<input>_if_<condition>` for
each gated one, and the helpers `retirement.no`, `rolled_some`, `put_back`, `rollover_if_any`, `is_trad`, `is_death`,
`plan_death`, `is_code7`, `is_code2`, `code7_wrong`, `annuity_if_cost`.
Added (`ssb.`): `any`, `ira_covered`, `repaid_more`, `prior_year_pay`, `lump_elect`, and the lines `ssb.no`,
`ssb.benefits_if_any`.

No longer inputs (kept as derived lines with the same id): `retirement.special`, `retirement.code_screen`,
`ssb.pub915`, `ssb.lump_sum`. Removed from the bank: those four. Renamed: none.

Ids changed from the map: none were fixed by the map for this lane except `ssb.any`, used as written.

## Fixtures and other data

`apply_data.py` rewrote inputs only. A case that stated `special: true` now states `disaster: true` (the one refusing
question every Form 1099-R is asked; the cases do not say which of the 23 items they meant); `special: false` is
dropped. `code_screen: true` became `under59: true` (the one case has code 7). A rollover above zero gained
`rollover_any: true`; `annuity: true` gained `cost_any: true`; benefits above zero gained `ssb.any: true`;
`pub915: true` became `repaid_more: true`; `lump_sum: true` became `prior_year_pay: true` and `lump_elect: true`.
`engine/src/generate.ts` states the same for generated returns. `interview/2025/coverage/hsa.yaml` row on an HSA
funding distribution now answers `charity_hsa`. `tools/engines/generate_cases.py` and `tools/coverage/tree.json`
still name the old inputs (not run by the draft check; debt).

## Cost and share (my estimates on the owner's scale; shares from `gate_frequencies.yaml` where marked gf)

"Share" is the share of those asked who answer Yes. Costs: 1 known at once; 5 a glance at a paper or a moment's
thought; 20 must find out what is being asked.

| Question | Asked of | Share yes | Cost of the typical answer | Before | Why the parent pays (N3) or why there is none |
|---|---|---|---|---|---|
| `$retirement` | every person | 24% gf | 1 (empty list) | 3 | reworded only |
| `account` | each form | plan 60%, IRA 35%, Roth 5% (judgment) | 2 (a tick box on the paper) | 5 | gates every later question |
| `code` | each form | code 7: 75% (judgment) | 2 (one character on the paper) | 5 | labels show the code as printed |
| `under59` | code 7 | 1% (judgment) | 1 | part of 10 (`code_screen`, 90 words) | one fact replaces three; `sec457` only after a Yes |
| `rollover_any` | each form except code G | 5% (judgment) | 1 | 10 (`rollover`, 239 words, an amount) | g 1 < q·C = 0.95 × (amount 5 + four children 4) |
| `cost_any` | each plan | 25% (judgment: public and older private pensions) | 2 | 10 (`annuity`, 141 words, four tests) | g 2 < 0.75 × (five children 5 + `annuity` 3 + the worksheet figures) |
| `disability` | each plan | 5% (judgment) | 1 | part of 15 (`special`) | g 1 < 0.95 × 3 children |
| `born_1936` | each plan | 2% (judgment) | 1 | part of 15 | g 1 < 0.98 × 5 (`lump_sum` needs thought); see "Unsure" |
| `box6` | each plan | 0.5% (judgment) | 2 (paper) | part of 15 | no parent: one fact on the paper |
| `loan_offset` | each plan | 1% (judgment) | 1 | part of 15 | no parent found that is safe (see "Unsure") |
| `pso_exclusion` | each plan | 1% (judgment) | 1 | part of 15 | one question; a parent over one cheap child does not pay |
| `charity_hsa` | each IRA | 4% (judgment; charitable distributions are common after 70½) | 1 | part of 15 | no parent |
| `ira_returned` | each IRA | 0.5% (judgment) | 1 | part of 15 | no parent |
| `ira_basis` | each traditional IRA | 7% (judgment) | 2 | part of 15 | no parent; help names Form 8606 |
| `disaster` | each form | 0.5% (judgment) | 1 | part of 15 | no parent |
| `ssb.any` | everyone | 20% gf | 1 | 3 (an amount in form words) | g 1 < 0.8 × 3 |
| `ssb.repaid_more` | with benefits | 0.5% (judgment) | 2 (paper) | part of 15 (`pub915`, 62 words, one sentence) | no parent |
| `ssb.prior_year_pay` | with benefits | 3% (judgment) | 2 (paper) | 5 (`lump_sum`, an election named in tax words) | g 2 < 0.97 × 5 |
| `ssb.terror_disability` | with benefits | 0.01% (judgment) | 1 | 3 (61 words) | bank prompt shortened |
| `ssb.ira_covered` | with benefits | 2% (judgment) | 1 | part of 15 | no parent; see "Requests" (the IRA questions could settle it) |

A plan's Form 1099-R with code 7 and nothing special: 15 before (`special`) + 10 (`rollover`) + 10 (`annuity`) + 10
(`code_screen`) = 45 by my estimate; after, eight one-line questions at 1 or 2 each, about 10.

## Asking order: what the walks show, and what it waits on

The bank gives the order wanted, by `seq` within order 170: the list, the account, boxes 1, 5 and 6, the code and its
check, where the money went, the IRA's facts, the disaster question, the plan's facts, a payment after a death,
after-tax cost and the Simplified Method figures. The engine does not ask it that way yet:

- For a plan's form the walk asks `account`, `box6`, `code`, then the one-line questions (`rollover_any`, `disaster`,
  `loan_offset`, `disability`, `pso_exclusion`, `born_1936`, `cost_any`), then `under59`, and only then `box1` and
  `box5`. Cause: `retirement.special` is the first refusal entry on `retirement.taxable`, `rolled` and `amount_a`, and
  the engine asks everything a refusal entry reads before it reaches the line's own inputs (T-284, cause 2). `under59`
  waits on the third entry (`screen_refused`), the boxes on the line's expression. The order fix should let `seq`
  decide; nothing in the bank needs to change then, but `l4a_work/coverage.py` lists its paths in today's order and
  must be regenerated (it says where).
- A filer whose form has a code this tool does not take (an RRB-1099-R, a corrective distribution) is refused at
  `retirement.bad_code` only after answering the one-line questions, for the same reason (N11 debt). Putting
  `bad_code` first in the refusal list would tell them at once, but a form with both a special situation and such a
  code would then be refused at the other gate, and fixtures expect `retirement.special` there (for example
  `classm.w2.1`); not done.
- Until the other lanes' entries carry their new order numbers, questions of other topics with an old number arrive
  inside the block as they become reachable (in the retired couple's walk: `person.x_other` for each spouse between
  `code` and `rollover_any`; `div.box12` and `f1040.tax_exempt_interest` between `ssb.benefits` and
  `ssb.repaid_more`). They were waiting on income being known (the retirement amounts feed adjusted gross income).
- Two forms of one person: not walked (no persona has two). Whether one form's questions are asked through before the
  next form's is the order agent's point (b).
- `retirement.sav_military`, `sav_404k`, `sav_inherited` are at 317 with a `seq`; lane 4b's list names their words.
  I did not reword them.

## Candidates for one tick-list

Each is its own one-line yes or no question today, recorded separately; a Yes to any but `disability` and `born_1936`
ends the interview, and those two open one to three follow-ups.

1. **"Is any of these true of this pension or plan payment?"** (a plan's Form 1099-R; `seq` 5 and 23 to 30):
   `box6` (an amount in box 6), `disaster`, `loan_offset`, `disability`, `pso_exclusion`, `born_1936`. Six.
2. **"Is any of these true of this IRA withdrawal?"** (an IRA's Form 1099-R; `seq` 20 to 23): `charity_hsa`,
   `ira_returned`, `ira_basis` (traditional IRA only), `disaster`. Four.
3. **"Is any of these true of your social security benefits?"** (`seq` 3, 4, 5, 7): `ssb.repaid_more`,
   `ssb.ira_covered`, `ssb.prior_year_pay`, `ssb.terror_disability`. Four.

## Unsure, and review debt

None of the new gates has had the adversarial review the formal gates design requires (rule 7), nor any render,
transcription, class M, screen or completeness review; the logs of `retirement` and `ssb` are stale. The new lines
cite the passages of the old questions (`i1040gi` pp. 27-31, `i5329` p. 5), not a passage for each item. Places
where a wrong No seems most possible to me:

1. **`cost_any`** gates `annuity` and five refusing children. A retiree who does not know that their own
   contributions were after-tax answers No, and the payments are then taxed in full (more tax, not less; the old
   `annuity` question had the same exposure, in harder words). The question names boxes 5 and 9b and the help says
   "If you are not sure, answer Yes". A person whose annuity is one they bought themselves (nonqualified) and who
   answers No is not refused by `own_annuity`; the code (D with another code) is then the only guard.
2. **`rollover_any`** gates the amount rolled over and four refusing children. A person who moved money to a Roth
   IRA and thinks of it as a "conversion", not as putting money "into a retirement account again", could answer No
   and miss `roth_moved`. The question says "(a rollover or a conversion)" and the help "Money moved into a Roth IRA
   counts".
3. **The code as the only asker** of five old items (corrective distributions, recharacterizations, a qualified plan
   loan offset, a nonqualified annuity, Form RRB-1099-R). It rests on the payer's code being what the Form 1099-R
   instructions prescribe (8, P, E; N, R; M; D with another code) and on the filer choosing "Any other code, two
   codes together, or no code at all" when box 7 does not show one of the eight single codes. `own_annuity` and
   `loan_offset` back two of them. These five now end at `retirement.bad_code`, whose wording is about the code,
   where they ended at `retirement.special`.
4. **`disability` asked only of a plan.** The three disability items of the old question name a pension; an IRA
   payment with code 3 is not asked. A plan payment with code 3 was and is refused by `retirement.bad_code`.
5. **`death_exclusion` and the three beneficiary questions asked only with code 4 from a plan.** A beneficiary's
   payment coded otherwise by the payer would not meet them (it would meet `not_beneficiary` only with code 4).
6. **`ira_basis` asked only of a traditional, SEP or SIMPLE IRA**, and `charity_hsa` and `ira_returned` only of an
   IRA: the old question asked every form, though the items name an IRA.
7. **`born_1936` then `lump_sum`** stand for "a lump-sum distribution you may report on Form 4972". I wrote the two
   conditions from the old item and from what I recall of Form 4972 (born before January 2, 1936; the whole balance
   within one year); I did not read Form 4972's instructions, which are not among the lines' citations. A Yes to both
   refuses whether or not the filer wants the form, as the old item did ("may report").
8. **`general_rule`** asks one case (75 or older at the start with five or more years guaranteed), which is the
   condition the old `annuity` question states; other reasons the Simplified Method does not apply are covered by
   `start_1996` and `own_annuity`. Read from the old questions, not from Pub. 939.
9. **`sec457`**: a No after `under59` = Yes refuses (the code is wrong), as `code_screen` did. The exception's words
   are the old question's.
10. **Form 8815 deleted from `ssb.pub915`** as asked by `sb.unsupported`. I confirmed that `sb.yaml` refuses with
    "Schedule B special treatment / Form 8815" at three lines; I did not confirm that every filer with benefits and
    excluded savings bond interest reaches `sb.unsupported` (the map says it is asked with interest income, and such
    a filer has interest). Adoption benefits: `scope.other_income` names them today; lane 9's
    `scope.adoption_benefits` must exist after the merge or this item has no asker.
11. **`retirement.rollover`'s rules.** The old 239-word amount listed what counts and what does not. The bank prompt
    is one line and the help holds three of the exclusions (41 words); the rest (dividends on employer securities,
    the cost of life insurance, a nonspouse beneficiary's transfer, code S to another SIMPLE IRA only, the 120-day
    first-home rule, a frozen deposit) are only in the form line's label now. That is N10 debt: they should be
    children of an amount above zero, which needs a model change I did not make.
12. **`annuity`'s bank prompt** ("paid in regular payments?") equals the form line's four-part test only given the
    answers before it: `cost_any` Yes, `start_1996` No, `general_rule` No, `own_annuity` No. On any other answers the
    return is refused, so the difference cannot change a computed return; the line's label still states the full test.

## Found and not fixed

- `tools/engines/generate_cases.py` and `tools/coverage/tree.json` name `retirement.special`, `code_screen` and
  `ssb.pub915` as inputs. Not run by `tools/draft_check.sh`; they will fail or mislead when run.
- `reviews/2025/limits.json` quotes the old text of `retirement.special` on the disaster limit.
- `interview/2025/gate_frequencies.yaml` has no entry for the new parents (`ssb.any` is its `social_security`
  figure, 20%; `$retirement` 24%).
- Facts about the person are asked per form (`under59`, `born_1936`, the public safety officer's wish), so a person
  with two forms is asked twice. They belong with the person (N5), which needs inputs in `person.yaml` (lane 4b) or
  in the opening (lane 1).

## Requests to other lanes

- **Order agent:** the two points under "Asking order" (children and boxes behind refusal entries; one form's
  questions through before the next). No target is needed in `full.yaml` that I can see: the topic is reachable as
  soon as the list is given.
- **Lane 4b (`person.yaml`):** `ssb.ira_covered` asks what `person.ira_trad` above zero with `person.ira_work_plan`
  already say. If those are asked first (topic 180 comes after 178 today), `ssb.ira_covered` could be a computed line
  and the question removed (N8).
- **Lane 9:** `scope.adoption_benefits` and `sa.excluded_income` are the only askers of two items removed from
  `ssb.pub915`; `scope.disaster_distribution` (a 2023 or 2024 distribution, or a repayment with no Form 1099-R) sits
  at 175 beside `retirement.disaster`, which asks about the form in hand.
- **Lane 1 (`f1040.line25b`):** federal tax withheld is box 4 of the Form 1099-R and box 6 of the SSA-1099; asked at
  the paper it would be `seq` 3.5 here (map Part 5, question 8). Not built.
- **Coordinator:** the tick-list page for the three groups above.

## Coverage rows

`interview/2025/coverage/retirement.yaml` (written by `l4a_work/coverage.py`): 43 rows. 25 end at
`retirement.special`, one for each situation of the old question that still has a question of its own (the disaster
one twice, for a plan and for an IRA); 5 end at `retirement.bad_code`, one for each old item the code now catches; 4
are the cases of the old `code_screen` (three refuse at `retirement.screen_refused`, the section 457 one goes on); 2
show the ordinary pension and the ordinary IRA withdrawal reaching the amounts without meeting any child question; 7
are the social security rows (`ssb.pub915` twice, `ssb.lump_sum`, the election not chosen, `ssb.terror_disability`,
no benefits, the ordinary case). `hsa.yaml`'s row `hsa.ira_transfer_at_the_1099r` now answers `charity_hsa`.

Two couplings a merge will meet. (1) The rows list answers in the order the engine asks today (see "Asking order");
the order fix will make some of them stale, and `coverage.py` says which lists to reorder. (2) The social security
rows answer `f1040.tax_exempt_interest` (lane 5a's, still at an old order number), because it is asked as soon as
there are benefits; when lane 5a moves it, remove it from the list `S` in `coverage.py` and rerun.

## Before and after, from the persona walks

Before: `docs/provisional/walks/before/`. After: `draft-walk --out /tmp/l4a_walks` on this branch (not committed:
every lane's `walks/after/` would collide at the merge).

| Filer | Topic | Before: questions, prompt words | After: questions, prompt words |
|---|---|---|---|
| `01_single_w2` (nothing in the topic) | retirement | 1, 24 | 1, 31 (worded as a question) |
| | social security | 1, 18 (an amount) | 1, 23 (yes or no) |
| `04_retired_couple` (one pension, code 7; benefits) | retirement | 10, 1,035 | 15, about 300 |
| | social security | 4, 182 | 6, 141 |

The retired couple's pension: the two lists, then `account` (9 words), `box6` (16), `code` (9), `rollover_any` (24),
`disaster` (18), `loan_offset` (25), `disability` (9), `pso_exclusion` (32), `born_1936` (23), `cost_any` (29),
`under59` (12), `box1` (6), `box5` (20). None of the 23 situations of the old question is shown as a list, and no
child question is met. The count rises by five because six one-line facts have no parent (the first tick-list
candidate); with that page the pension is nine screens.

## Not finished, in rank order

1. (Rank 5 of the map.) `retirement.exception` (409 words, an enum of 24 values) and `retirement.exc_amount` (141
   words) are unchanged but for their order and `seq`. Plain labels need the table of the Form 5329 instructions
   read whole (I read exceptions 01 to 14 and 16 to 20 as printed, not all 23). `retirement.early_screen` is still
   one question of six items (a bulleted list now); its split follows the pattern of `code_screen` in
   `gen_retirement.py`. Only early distributions (codes 1 and S) meet these three.
2. (Rank 4.) The Simplified Method figures (`cost`, `used_last_year`, `last_line4`, `joint_life`, `age`,
   `combined_age`, `months`, `recovered`) keep their wording. The rollover amount's rules are in help (see "Unsure",
   11).
3. (Rank 3.) `box1` and `box5` keep the form's label as their wording ("Gross distribution, Form 1099-R box 1").
4. The facts about the person asked per form (`under59`, `born_1936`, the public safety officer) are not moved to
   the person.
5. No persona has an IRA withdrawal, a rollover, an annuity with after-tax cost or two forms; the coverage rows walk
   those paths but no transcript shows them.

## What I ran and saw, and what I infer

Ran and saw:

- `tools/draft_check.sh` (the full check) on commit `7e1620ba`: green, every step (build; 1,854 of 1,854 fixtures;
  interview-rules, 0 problems; coverage rows, 0 problems over the four files; person wording; the self-tests; 695
  CLI integration invocations; properties; the server test; twins; render check). The commit after it adds only the
  two reports that run regenerated (`reports/2025/person_wording.md`, `properties.md`) and these notes.
- `draft-walk` over the twelve personas on that build: 0 problems, the same ten complete and two refused. I read the
  one-line listing of `01_single_w2` and `04_retired_couple` for this topic, from which the before and after figures
  and the asking order above are taken; and the shown forms of `$retirement` in the person-wording report (one
  person, the taxpayer, the spouse).
- The first run of the fixtures after the model change failed 252 cases, all "no input supplied" for a new parent:
  `classm*.json` and `mutation.json` take no defaults. `apply_data.py` now states every reachable new input in those
  files. No expected value or refusal was edited at any point.
- The archived Form 1040 instructions for the death benefit exclusion ("died before August 21, 1996"), the public
  safety officer exclusion (an election; the plan; the premiums) and the General Rule passage.

Inferred, not checked:

- Every wrong-No analysis under "Unsure" (no adversarial review was run).
- That the box 7 codes named for the five items the code now catches are the ones payers use (from the old
  question's own words, the code list in `retirement.code`'s source text and my recollection of the Form 1099-R
  instructions; I did not read the instructions' code table).
- That a nonqualified annuity always has after-tax cost, and that a civil service alternative annuity always does
  (the reason `own_annuity` and `csrs_alt` sit beneath `cost_any`).
- The shares in the cost table marked judgment.
- That the reason `box1` and `under59` are asked late is the order of refusal entries (it fits the walk and the
  README's account of blocks; I did not trace the engine).
- That `sb.unsupported` and `scope.other_income` are reached by every filer who met the deleted items of
  `ssb.pub915` (see "Unsure", 10).
