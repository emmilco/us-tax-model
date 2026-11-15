# Lane notes: 8a (Marketplace health insurance)

Branch `lane/l8a`. Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no
model call was made. Files: `forms/2025/f1095a.yaml`, `forms/2025/f8962.yaml`; the bank entries of those forms,
`dependent.ptc_files`, `dependent.ptc_magi`; the order number (only) of the 32 health savings account entries;
`engine/src/generate.ts` (the generated returns' answers for the new inputs); fixture inputs; persona `08`.

**State of the work is in "Steps" at the end; a successor continues from the first step not marked done.**

## Order numbers and blocks

| Order | What | `seq` |
|---|---|---|
| 190 | The 32 health savings account entries (was 9); their `seq` unchanged | as before |
| 195 | `$f1095a`, the opening question | 1 |
| 196 | Once per return: the facts that end the interview (other coverage, who the plan covered, premiums) | 1 to 23 |
| 197 | Per Form 1095-A: the paper | 1 to 60 |
| 198 | Once per return, after the forms: `f8962.same_state_counted`, `f8962.fpl_table` | 1, 2 |
| 199 | Reached only when income allows: `f8962.estimate_100`, `f8962.alien_below`, `dependent.ptc_files`, `dependent.ptc_magi` | 1 to 4 |

The once-per-return facts (196) come before the paper (197) so that a filer the tool cannot serve is told before
typing any amount (N11), and because they are the questions on which a filer leaves (N7).

Inside 197 the months are asked in calendar order, one month at a time across the paper's row: January column A,
B, C, then February. To ask a whole column first, renumber the `seq` of the 36 `f1095a.in_*` entries; nothing else
depends on it.

## What changed, by question

### `$f1095a` (was a 45-word instruction to list forms)

Now: "In 2025, did you (or, on a joint return, your spouse), or anyone you claim as a dependent, have health
insurance bought through HealthCare.gov or a state Marketplace?" with the answers No; Yes, with one Form 1095-A; two;
... six. No model change: the question is still the roster, with fixed answers (`choices`), as `$f8889` is.

- A Bool parent in front of the roster was rejected: 42 lines of `f8962.yaml` sum over the roster and each would
  need a `choose` on the parent.
- **Limit, for the owner:** the page offers at most six forms. Seven or more Forms 1095-A in one year cannot be
  entered. Adding a choice is one bank line each.
- The interview accepts only the offered entry keys (`form_1` ... `form_6`), so every fixture's Form 1095-A keys were
  renamed (`m`, `m1`, `m2`, `mkt_a`, `mkt_b` to `form_1`, `form_2`, by position), in inputs and in the keys of
  expected values. No expected value changed. `generate.ts` names its forms the same way.
- Who could answer No wrongly: a person covered by a plan someone else signed up for, who got no Form 1095-A of
  their own. Today's interview does not catch that person either (with no form listed, no Form 8962 question is
  asked). Not fixed; see "Found and not fixed".
- The words on VOID and CORRECTED forms and on catastrophic and dental plans went to the help; `f1095a.void` is
  the guard for a void or replaced form (it refuses, as today).

### `f1095a.uniform` (198 words) taken apart

`f1095a.uniform` is now a derived line with the meaning it had; every reader is unchanged. New inputs, per form:

| Input | Question | Asked |
|---|---|---|
| `f1095a.same_months` | "Does Part III show the same amount in column A for every month, January to December, and the same amount in column B for every month?" | every form |
| `f1095a.b_blank` | "Is column B blank or zero in any month that has an amount in column A?" | every form, after it |
| `f1095a.b_changed` | "During 2025, did your address, the people in your household or on this plan, or anyone's access to other health coverage change without the Marketplace being told?" | every form whose column B is not blank (a Yes to `b_blank` already settles that column B needs correcting) |
| `f1095a.b_fixed_same` | "Once column B is corrected, is the correct column B amount the same for every month, January to December, and the column A amount the same for every month too?" | only when column B is blank or a change was not reported |

`uniform` = `same_months` when column B needs no correcting; `b_fixed_same` when it does. This is exactly today's
rule ("use the corrected column B ... answer no if the correct amount is not the same every month"; i8962 p. 14,
line 10), so the same paper takes the same route (annual line 11, or monthly lines 12 to 23) as today. The route
matters to the result (rounding), which is why `b_fixed_same` is also asked of a form whose printed months differ.

Helper lines: `f1095a.no`; `f1095a.b_wrong` (either column B fact); `f1095a.b_wrong_asked` (the same value, read
through a `choose` on `same_months` whose two alternatives are the same line, so that the column B questions wait
for the months question: the formal gates design's "nested choose where order matters");
`f1095a.b_fixed_same_if_b_wrong` (the gate line of `b_fixed_same`, which is marked `gated_by`).

Who could answer wrongly, and the guard:
- Yes to `same_months` with a column B that is uniform on paper but wrong (a move not reported): `b_changed`.
- Yes to `same_months` with column B blank all year (no advance payments): `b_blank`.
- `b_changed` is the six examples of i8962 p. 15 put as one sentence, with the examples in the help. The
  instructions call them examples and add "or if you have reason to believe the Marketplace reported the wrong
  applicable SLCSP premium"; the help ends "Answer Yes also if the Marketplace has told you column B is wrong."

The monthly prompts were 61 words (A), 109 (B), 22 (C) each; now about 15, 26 and 16 with the frame. Dropped from
them: what to enter when column A is zero although the premium was paid, and when a premium was unpaid. Both
situations refuse (`f8962.a_zero_paid`, `f8962.unpaid`, below), as they did inside `f8962.other`, so the
instruction was never reachable by a filer who answered truthfully. The form lines keep the full `source` text;
the bank `prompt` overrides it.

### `f8962.other` (357 words), `f8962.alloc` (65), `f8962.premium_adjust` (108) taken apart

Each old id is now a derived line, true when any of its items is true (MAP 4.1). The `refuses:` entries on
`f8962.line24` and `f8962.line25` are untouched, so the refusal gates, forms and remedies are the same.

| Old | New input | Kind | Question |
|---|---|---|---|
| `other` | `f8962.other_coverage` | parent, refuses nothing | "While on Marketplace insurance, could anyone on this return have had other health coverage, such as a job's plan, Medicare, Medicaid, CHIP, TRICARE or veterans' care?" |
| `other` | `f8962.mec_job_enrolled` | child | "In one of those months, was anyone on this return enrolled in a health plan from a job, counting COBRA and retiree plans?" |
| `other` | `f8962.job_offer` | child, refuses nothing | "In one of those months, was anyone on this return offered a health plan by an employer and did not take it?" |
| `other` | `f8962.mec_job_affordable` | child of `job_offer` | The affordability test (9.02% of household income) and minimum value. 56 words: the legal test itself; reached only after two Yes answers |
| `other` | `f8962.mec_government` | child | Medicare Part A or C, Medicaid, CHIP, TRICARE, veterans' care, Peace Corps |
| `other` | `f8962.mec_other` | child | Any other coverage that is not insurance bought on your own (the two examples are from Pub. 974, "Other Coverage Designated by the Department of Health and Human Services", items 1 and 2) |
| `other` | `f8962.hra` | own question | QSEHRA or individual coverage HRA offered |
| `other` | `f8962.not_lawful`, `incarcerated`, `no_family`, `medicaid_reversed` | own questions | one fact each |
| `other` | `f8962.unpaid`, `a_zero_paid` | own questions | a premium unpaid; column A zero for a month that was paid |
| `alloc` | `f8962.shared_policy`, `divorced_enrolled` | own questions | a plan covering someone on the return and someone not on it; a divorce while on one plan |
| `premium_adjust` | `f8962.midmonth_start`, `premium_refunded` | own questions | coverage starting after the first of a month; a premium refunded |

Gate lines: `f8962.mec_job_enrolled_if_other_coverage`, `job_offer_if_other_coverage`,
`mec_job_affordable_if_job_offer`, `mec_government_if_other_coverage`, `mec_other_if_other_coverage`.

**One narrowing, for the owner to accept or reverse.** Today's words are "for any month, anyone in your tax family
was eligible for minimum essential coverage". Read literally that refuses a person who had Marketplace insurance
from January to April and a job's plan from May (persona `08`, whom the baseline walk completes). The parent now
asks about the months of Marketplace insurance only ("While on Marketplace insurance ..."), as the map proposed.
Ground: i8962 p. 5, "An individual in your tax family who is eligible for MEC ... for a month is not in your coverage
family for that month": the rule works month by month, and a month with no Marketplace enrollment has no credit
and no advance payment, so other coverage in that month changes no line. The set of people is not narrowed: it is
still anyone on the return. To go back to the literal reading, change "While on Marketplace insurance" to "At any
time in 2025" in the `source` of `f8962.other_coverage` and "In one of those months" to "In any month of 2025" in
its children; persona `08` is then refused.

Wrong No to `other_coverage`, and the guard: a person with coverage of a kind the parent's examples do not name.
The parent says "such as" and its help says "If you are not sure, answer Yes; the next questions settle it."; the
last child (`mec_other`) is the open one. A wrong Yes costs up to four short questions and refuses nothing.

`f8962.married_in_2025` is unchanged in the model (asked on a joint return only) and reworded in the bank.

## Cost and share table (my estimates on the owner's scale; shares are judgments unless marked gf)

| Question | Asked of | Share answering yes | Cost of yes | Cost of no | Note |
|---|---|---|---|---|---|
| `$f1095a` | everyone | 8.5% (gf `marketplace`) | 2 (count the forms) | 1 | was 5 either way |
| `f8962.other_coverage` | with a form | 25% | 3 | 2 | parent: g = 2, q = 0.75, children C = 12; 2 < 9 (N3) |
| `f8962.job_offer` | `other_coverage` = Yes | 40% | 2 | 2 | parent over the 56-word test: 2 < 0.6 x 15 |
| `f8962.mec_job_affordable` | `job_offer` = Yes | 30% | 15 | 15 | needs the employer's figures; not made cheaper |
| each flat fact of 196 | with a form | under 2% each | 2 | 1 to 2 | was 20 to read `f8962.other` whatever the answer |
| `f1095a.same_months` | each form | 60% | 2 | 2 | a glance at the paper; was 20 (198 words) |
| `f1095a.b_blank` | each form | 8% | 2 | 1 | a glance |
| `f1095a.b_changed` | each form | 5% | 5 | 3 | the one question of the form block that needs thought |
| `f1095a.b_fixed_same` | column B to correct | 70% | 10 | 10 | needs the Marketplace's tool, as today |

## Candidates for one tick-list

All are asked of every filer with a Form 1095-A, once per return, order 196. Any tick refuses, as today.

**"About the people your Marketplace plan covered"** (`seq` 10 to 15):
`f8962.shared_policy`, `f8962.divorced_enrolled`, `f8962.married_in_2025` (joint returns only), `f8962.no_family`,
`f8962.not_lawful`, `f8962.incarcerated`.

**"About the premiums"** (`seq` 20 to 23):
`f8962.unpaid`, `f8962.a_zero_paid`, `f8962.premium_refunded`, `f8962.midmonth_start`.

Not in a group: `f8962.hra` (`seq` 7, after the other-coverage questions, same theme but its own subject) and
`f8962.medicaid_reversed` (`seq` 16; no theme in common with the others).

Per form, `f1095a.b_blank` and `f1095a.b_changed` could share a screen with `f1095a.same_months`, but they are
not ticks of one list (the first is asked before the other two can be).

## Model changes (review debt)

Inputs added: `f1095a.same_months`, `b_blank`, `b_changed`, `b_fixed_same`; `f8962.other_coverage`,
`mec_job_enrolled`, `job_offer`, `mec_job_affordable`, `mec_government`, `mec_other`, `hra`, `not_lawful`,
`incarcerated`, `no_family`, `medicaid_reversed`, `unpaid`, `a_zero_paid`, `shared_policy`, `divorced_enrolled`,
`midmonth_start`, `premium_refunded`. Inputs removed (now derived lines with the same id): `f1095a.uniform`,
`f8962.other`, `f8962.alloc`, `f8962.premium_adjust`. Gates added: the gate lines named above.

Debt: transcription, render, class M and completeness reviews of `f1095a` and `f8962` are stale; every new gate
needs the screen review and the false-no review (formal gates design, rule 7); `reviews/2025/**` and
`tools/coverage/tree.json` still describe the old questions; `engine/src/mutate.ts` pins mutants of `f8962` lines
by hash and was not rerun; the Lean comparison was not run; `tools/engines/generate_cases.py` was not looked at.
The fixtures `classm*.json` and `mutation.json` had inputs renamed and explicit `false` answers to the three old
ids dropped (the default is false); none was regenerated.

## Before and after (the topic's own questions: `$f1095a`, `f1095a.*`, `f8962.*`)

| Filer | Before | After | How measured |
|---|---|---|---|
| No Marketplace insurance (persona `01`, and every persona but `08`) | 1 question, 45 words | 1 question, 21 words (28 as stored, with the spouse phrase) | walks |
| Same plan all twelve months, one form | 10 questions, 1,040 words | 21 questions, 481 words | before: counted from the baseline prompts, not walked (no such persona); after: a walk of a persona written for the measure and not committed |
| Marketplace January to April, then a job's plan (persona `08`) | 43 questions, 3,169 words | 54 questions, 1,105 words | walks (`docs/provisional/walks/before/`; after: `draft-walk` on this branch) |

The count of questions rises by eleven: the three screens of 530 words (`alloc`, `other`, `premium_adjust`) are now
twelve one-line facts (thirteen on a joint return), ten of which are the two tick-list groups below, and the
198-word `uniform` is three one-line questions about the paper. No filer reads more words than before. `f1040.tax_exempt_interest`
(52 words, lane 5a's) is asked inside the topic and is not counted.

## Asking order: what the walks show on this branch, and the order lane's contract

Read in the walk of persona `08` on this branch's build, which does not have the order lane's engine change. The
contract (`docs/provisional/lanes/order.md` on `lane/order`, section 1) was published while this lane was being
checked; I read it after the work and changed nothing for it. `interview-order` is not on this branch, so the
measurement of its section 1.7 was not run: **run it after the merge.**

1. **Inside order 196 the questions arrive gate by gate.** The refusals on `f8962.line24` are read in the order they
   are listed (`alloc`, `marriage`, `other`, `premium_adjust`), and on this branch the questions of one are not
   reachable until the one before is settled. I numbered `seq` in that same order: the people group
   (`shared_policy`, `divorced_enrolled`, `married_in_2025`, then from `other`: `no_family`, `not_lawful`,
   `incarcerated`), `medicaid_reversed`, the other-coverage questions, `hra`, then the premiums group. The contract
   (1.4) asks for exactly this where a refusal must show at once ("Number the screens of one line in the form's
   order"), so the numbering should stand after the merge. By N7 the other-coverage parent would come first (it is
   where most filers who leave, leave); to do that, move the `other` entry to the head of the `refuses` list of
   `f8962.line24` (one list, shared with `line25` by a YAML anchor) and renumber; the people group then cannot stay
   together, since two of its questions belong to `alloc` and three to `other`.
2. **The 36 monthly amounts arrive in pieces on this branch**: January to April A and B, then May to December A,
   then C, then the remaining B, as the Form 8962 arithmetic reaches them; and `f8962.fpl_table` (order 198) arrives
   before the paper (197). The contract says a question that states a `seq` is open as soon as the return needs it,
   which should cure this without a target. If it does not: I tried `f8962.line11a`, `f8962.line11b` and
   `f8962.aptc_total` as direct targets on the built profile (edited by hand, not committed) and persona `08` was
   then asked every question of the form in `seq` order with `fpl_table` after it. **Caution:** that was one
   persona. The contract (1.6) allows a target only where the return reads the result in every case; a filer below
   the poverty line with no Marketplace estimate may never be asked columns A and B today, and these targets would
   ask them. I did not test that case.
3. **`f1040.tax_exempt_interest`** (lane 5a's, 52 words) is asked directly after `$f1095a`, because Form 8962's
   household income is the first thing to need it. Its topic (interest, 270) comes after this one (195).
4. `$f1095a` itself (195) is asked late on this branch only because every other lane's questions still carry
   order numbers below 100.
5. The contract says one `order` number per topic. This topic uses five (195 to 199), as the map allowed for
   sub-blocks; each is asked through before the next. One number with one run of `seq` would do the same; the
   per-form questions (197) are a consecutive stretch either way.

## Ids changed from the map

None of the map's fixed ids is in this lane. The map proposed nine kinds of other coverage as nine children; I
built four (`mec_job_enrolled`, `mec_job_affordable` beneath `job_offer`, `mec_government`, `mec_other`): the six
government programs are one subject on one line ("Medicare (Part A or Part C), Medicaid, CHIP, TRICARE, veterans'
health care or Peace Corps health coverage") and any of them refuses, so six questions would be six flat refusals.

## Requests to other lanes

- **Order agent / coordinator:** after the merge, run `interview-order` and look at orders 196 to 199 (notes 1 and
  2 above). No target is requested unless the monthly amounts still arrive in pieces.
- **Lane 5a (`f1040.tax_exempt_interest`):** ask it in the interest topic of every filer, or accept that a
  Marketplace filer meets it at 195.
- **Lane 2a (`dependent.yaml`):** `dependent.ptc_files` is 47 words because the filing thresholds are in it. A
  parent in `dependent.yaml`, "Did this dependent have any income of their own in 2025?" (suggested id
  `dependent.ptc_income_any`, gate line `dependent.ptc_files_if_income`), would spare most parents the thresholds.
  I reworded the question in the bank only.
- **Lane 6a (`sc.hi_screen`):** the map says Marketplace insurance is known from `$f1095a`; the roster's entry keys
  are now `form_1` to `form_6`, and "no Marketplace insurance" is the empty list, as before.
- **Tick-list lane:** the two groups under "Candidates for one tick-list".
- **Walk lane / coordinator:** persona `08_hsa_marketplace` now names its form `form_1` and answers the new
  questions; its `who` and `end` are unchanged.

## Found and not fixed

- **A person covered by someone else's Marketplace plan who has no Form 1095-A of their own** (a child enrolled
  by the other parent, an adult on a former spouse's plan) answers `$f1095a` No, or today lists nothing, and is
  asked nothing about Form 8962, though advance payments may have to be allocated to them. Today's interview has
  the same gap. A guard would be a second question after a No ("Were you, or anyone on this return, covered by a
  Marketplace plan that someone else signed up for?"), refusing as `f8962.alloc` does; it is a scope change, so I
  did not build it.
- **The page offers at most six Forms 1095-A** (above).
- **`f8962.other`'s refusal remedy** still says "Eligibility for other minimum essential coverage for any month";
  with the parent narrowed to the months of Marketplace insurance the remedy reads wider than the questions. Not
  edited (expected refusals quote it).
- **The monthly column A lines' `source`** (in the form) still tells a filer what to enter when column A is zero
  although the premium was paid, a situation `f8962.a_zero_paid` refuses. The bank prompt no longer shows it.
- **A part-year form still costs 36 amounts**, 24 of them zero for persona `08`. The plain remedy is a question
  for the first and the last month of coverage, with the months outside it taken as zero; that needs 36 gate
  lines in `f1095a.yaml` and I did not start it. A page that shows Part III as the table it is would do more.
- **`f1095a.b_counted`** (only with two or more forms) is reworded but still asks the filer to apply the rule. A
  parent "Do the months on this form overlap the months on another of your forms from the same state?" with
  `b_counted` beneath it is a small model change in `f1095a.b_used`; not done.
- **`f8962.estimate_100`** holds two facts (the Marketplace's estimate; no reckless misinformation) in one input.
  Not split: the second fact would need a negated child.
- **`f8962.married_in_2025`** refuses on the fact, though the alternative calculation for the year of marriage is
  a choice (Form 8962 line 9, "do you want to use"). Left as it is.

## Where I was unsure

- The narrowing of other coverage to the months of Marketplace insurance (above): the tax reasoning is mine, from
  one passage of the instructions; the map proposed the same wording and the persona depends on it.
- `f8962.no_family` in plain words ("on no one's 2025 tax return, neither filing one nor claimed as a dependent")
  is my reading of "not included in any tax family".
- `f8962.mec_government` keeps the bare list of programs, as today. The instructions soften it (a person the
  Marketplace found not eligible for Medicaid is treated as not eligible); I did not add that, since it would
  accept returns today's question refuses.
- Shares in the table are my judgments; only the 8.5% is from `gate_frequencies.yaml`.
- The spouse phrase: the once-per-return questions say "anyone on this return" where the subject is every person
  on it, and use the phrase where the subject is the filer (`$f1095a`, `divorced_enrolled`, `fpl_table`).

## Steps

1. **Done** (commit 94a7bb20). Order numbers; `$f1095a` as a plain question; months in calendar order.
2. **Done.** `f1095a.uniform` taken apart.
3. **Done.** `f8962.other`, `alloc`, `premium_adjust` taken apart.
4. **Done.** Reworded in the bank: `f1095a.void`, `f1095a.b_counted`, `f8962.same_state_counted`,
   `f8962.fpl_table` (now "did you live in Alaska or Hawaii?" with No first), `f8962.estimate_100`,
   `f8962.alien_below`, `dependent.ptc_files`, `dependent.ptc_magi`.
5. **Done.** Coverage rows (`interview/2025/coverage/marketplace.yaml`, 25 rows): the off-ramp; one row per refusing
   item of the three old screens; the parent's No sparing its children; an unaffordable offer going on; a void form;
   the year of marriage; the five routes of `uniform`, each walked to completion (so the rows do not depend on the asking order).
   `hsa.testing_period_no_account_left` in `coverage/hsa.yaml` lost its answer `$f8889: []`: with the health savings
   block at 190 the row is refused at `s2.other` (still order 10 here) before that question is asked; the background
   gives the same answer when it is.
6. **Done.** The full `tools/draft_check.sh` on the final sources: build, fixtures (1854/1854), interview-rules
   (0 problems), coverage rows (0 problems), person wording, the self-tests, integration (695), properties, the
   server test (337) and twins all ok; `render --check` failed because `rendered/2025/` was stale, so I ran
   `render` (the local renderer, no model) and `render --check` then passed. The script as a whole was not run
   again after that, so it never printed "green" for this tree.

Not started, in rank order: the first-and-last-month question for a part-year form; the overlap parent of
`f1095a.b_counted`; the guard after a No to `$f1095a` (a scope change); splitting `f8962.estimate_100`.
