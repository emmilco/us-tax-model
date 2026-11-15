# Lane notes: 2a (children and other dependents)

Branch `lane/l2a`. Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no
model call was made. Form file owned: `forms/2025/dependent.yaml`. Bank entries owned: `$dependent` and `dependent.*`
except `dc_*` (lane 2b), `edu*` (lane 8b) and `ptc_*` (lane 8a), which this lane did not touch.

**For a successor: read "State" first.** The two scripts in `docs/provisional/lanes/l2a_work/` are how the bank
entries and the fixture inputs were written; edit their tables and run them again, do not edit the outputs by hand.

## State

Done and committed (`e495e1f2` and what follows it): the map's items 1, 2, 3 and 6, the parents of items 4 and 5,
and a parent the map did not ask for (`citizen_ssn`). Not done: see "Not finished, in rank order". To continue: change
the wording table in `l2a_work/bank.py` and run it; for a new input also add its default to
`fixtures/2025/defaults.json`, its answer to `new_inputs` in `l2a_work/fixture_inputs.py` (run it: it adds only what a
case lacks), the two generators, and the three slice profiles; then `tools/draft_check.sh --quick`, the lane's rows
alone with `node engine/dist/main.js interview-coverage --rows interview/2025/coverage/dependents.yaml` (90 seconds
against the 4 minutes of all rows), and `draft-walk`. A build took 8 to 10 minutes on the night, with fifteen lanes
running.

## The design in one paragraph

The dependent tests are `choose` chains in the model, and a question is asked only when the evaluator reaches its
input. Before this lane a dependent's first three questions were the three refusal gates of `dependent.qualifying_child`
(tie-breaker, divorced parents, married), because a line's refusals are read before its expression; then a 297-word
relationship question, and age fifth. Now the first refusal gate reads the relationship and the age before anything
else (an equivalent rewrite, below), and each precise or refusing question sits beneath a plain parent whose No is
known at once and settles it:

| Plain parent (new input) | A No settles, without asking | Why the No is right (the entailment) |
|---|---|---|
| `dependent.lived_all_year` "Did this person live with you for all of 2025?" (Yes is the off-ramp) | `months` (178 words), `qr_all_year` (156), `kidnapped` (74) | Lived with you all year is 12 months, is all year as a member of the household, and (time missing is not time lived with you) is not a child missing in 2025 |
| `dependent.ever_married` "Has this person ever been married?" | `married` (62, refuses), `joint_return` (51) | A person never married is not married at the end of 2025 and is on no joint return |
| `dependent.own_money` "did this person have money of their own ... or own the home they lived in?" | `self_support_view`, `self_support` (240) | Pub. 501: a person's own funds are support only if spent; a person with no funds and no home provided none of their own support |
| `dependent.parents_apart` "a child whose parents are divorced, separated, or lived apart for the last 6 months of 2025?" | `divorced_rule` (107, refuses) | Condition 1 of the rule for children of divorced or separated parents |
| `dependent.self_support_view`, `dependent.supported_view` (three answers: clearly less than half, clearly more than half, close or not sure) | `self_support` (240), `supported` (559): the full tests, asked only on "close or not sure" | The plain answer is the test's answer where it is clear; the full text is kept whole for the filer who needs it |

Nothing was renamed and no refusal gate changed its id: `dependent[x].married` and `dependent[x].divorced_rule` are
still the inputs and still the gates the fixtures expect.

## Model changes (`forms/2025/dependent.yaml`, `params/2025.yaml`)

New inputs (6): `lived_all_year`, `ever_married`, `own_money`, `parents_apart` (Bool); `self_support_view`,
`supported_view` (Enum `dependent_support_view`: `under_half`, `over_half`, `unsure`; the enum is new in
`params/2025.yaml`, the one edit outside this lane's files, placed beside `dependent_relationship`).

New derived lines, and what reads them:

| Line | What it is | Replaces the direct read in |
|---|---|---|
| `lived_half_counted`, `under_7_counted` | the two tests on `months` (over 6, under 7) | `lived_half`, `under_7_months`, which now choose on `lived_all_year` first (a Count cannot be gated by a marker; the convention of the formal gates design) |
| `kidnapped_if_part_year` | gate line of `kidnapped` (marked `gated_by`) | `kidnap_residency`, `qr_kidnapped`, `kidnap_eic_kidnapped` |
| `household_all_year` | Yes when `lived_all_year`, else `qr_all_year` | `qr_household_member`, `qr_other_relation` |
| `joint_return_if_ever_married` | gate line of `joint_return` (marked `gated_by`) | `qc_from_joint`, `eic_child_from_joint` |
| `self_support_if_own_money`, `self_support_by_view`, `self_support_view_over` | No without own money; else the plain answer; else `self_support` | `qc_from_support` |
| `supported_by_view`, `supported_view_over` | the plain answer; else `supported` | `qr_from_income` |
| `divorced_rule_screen`, `divorced_rule_if_parents_apart` | see "The screen lines" | the refusal entry on `qualifying_child` |
| `married_screen_qc`, `_qr`, `_eic`; `married_if_ever_married_qc`, `_qr`, `_eic` | see "The screen lines" | the refusal entries on `qualifying_child`, `qualifying_relative`, `eic_child` |
| `qc_tiebreak_from_age`, `qc_tiebreak_claimant`, `qc_tiebreak_not_child`, `other_is_taxpayer` | see "The tie-breaker gate" | the expression of `qc_tiebreak` |

**The screen lines (how a refusing input sits beneath a parent without changing the gate id).** A refusal's gate id
is the line its `when` names, and the fixtures expect `dependent[x].married` and `dependent[x].divorced_rule`. A gate
line as the `when` would change that id. Instead each refusal entry now names a `choose` on the parent
(`married_if_ever_married_qc`): parent No gives false; parent Yes reads a screen line (`married_screen_qc`), whose value
is always false and which carries the original refusal entry (`when: dependent.married`, with the form, remedy and
citation of the line it came from). The evaluator passes a refusal met inside a `when` up unchanged (`eval.ts`, the
refusals loop: a `when` that is not a Bool blocks the line with its own value), so the refusal shown is the same gate,
form and remedy as before, and the entries keep their order on each line. The three married screens differ only in
the form and remedy text of the line they belong to.

**The tie-breaker gate (`qc_tiebreak`), an equivalent rewrite.** Before: `other_claimant` and (the other person is a
taxpayer, or this person passes your qualifying child tests). It read `other_claimant` first. Now it reads
`qc_relationship`, then `qc_age`, and only then `other_claimant`: where either is false the qualifying child tests
are false without reading anything further, so the value is `other_claimant` and the other is a taxpayer
(`qc_tiebreak_not_child`); where both are true it is the old expression unchanged (`qc_tiebreak_claimant`). Reading
the relationship and the age can refuse nothing, so the order in which refusals are met is unchanged. This is what
puts relationship and age first for a child, brother or sister. For anyone else the gate never needed the age, so
it was asked late (after `disabled`); `qc_tiebreak_other_age` is a `choose` on the age whose two alternatives are the
same line, there only so that the age is asked directly after the relationship for every person listed.

## Fixtures, defaults, generators

- `fixtures/2025/defaults.json`: six defaults, each the answer that opens the questions a case already answers
  (`ever_married`, `own_money`, `parents_apart` true; the two views `unsure`; `lived_all_year` false, so `months` is
  read). No existing default changed. A fixture that states `months: 12` and nothing else is therefore evaluated as
  "not all year, 12 months": the same values, by the old path.
- The files that take no defaults (class M and mutation, federal and New York: seven files) state the six inputs for
  every dependent entry, written by `l2a_work/fixture_inputs.py`: the same opening answers, and `lived_all_year` true
  where the case states 12 months (not for a kidnapped child, nor where an all-year household answer of No is read).
  No expected value or refusal was edited. Nothing was regenerated.
- `engine/src/generate.ts` and `tools/engines/generate_cases.py` give the new inputs, derived from the facts already
  drawn so the random stream and every value are unchanged.
- The slice profiles `sales.yaml`, `social-security.yaml`, `stage4.yaml` list the six new inputs (they list every
  dependent input). `full.yaml` was not edited.

A second step added one more plain parent and one more read through a parent:

| Plain parent (new input) | A Yes settles, without asking | Why the Yes is right |
|---|---|---|
| `dependent.citizen_ssn` "Is this person a U.S. citizen with a social security number? (If the card has a restriction printed on it ... answer No.)" | `citizen` (39 words), `tin` (54), `work_ssn` (40), and later `eic_ssn` (79) | A citizen is a citizen; a social security number issued by the due date is the number the tests ask for; a card with no restriction is valid for work and for the earned income credit |

Lines: `citizen_known`, `tin_known`, `work_ssn_known`, `eic_ssn_known` (Yes when `citizen_ssn`, else the old input), read
by `resident`, `ctc_from_citizen`, `odc_from_citizen`, `claimed_no_tin`, `ctc_from_tin`, `odc_from_tin`,
`ctc_from_work_ssn`, `eic_ssn_child`. `edu_student_tin` still reads `dependent.tin` directly: it is a twin of a
`person.edu*` line and this lane leaves the twins alone, so a dependent student is still asked `tin` after a Yes here
(see Requests). `married_known` (No without `ever_married`, else `married`) replaces the one direct read of `married`
outside the refusals, in `hoh_test2_lived`, so a head of household is not asked `married` past the parent. Default and
stated-all fixtures: `citizen_ssn` false (the old answers are read).

## The bank (`interview/2025/questions.yaml`), written by `l2a_work/bank.py`

- `order` 120 and a `seq` for `$dependent` and every dependent test of the first sitting (36 entries); `order` 314
  for `us_half` and `eic_ssn`, which are reached only when income allows the earned income credit.
- The boilerplate help ("Married filing separately and unsupported items are refused with citations.") is gone from
  all of this lane's entries.
- `seq` within 120: `$dependent`, relationship, age, lived all year (then kidnapped, months, born or died, placed,
  part-year home), younger, student, disabled, the four plain facts (`other_claimant`, `parents_apart`, `ever_married`,
  `own_money`), their children, the tests of a relative who is not a child, citizenship and the number, the parent's
  home, the absence question.
- Every prompt this lane changed is a bank `prompt`; the form line's `source` keeps the source-faithful statement.
  Untouched (the line's own text is still the question): `born_died`, `placed`, `part_year_home`, `spouse_relative`,
  `parent_home_paid` (170 words), and the two full support tests `self_support` (240) and `supported` (559), which
  are now reached only from "It is close, or I am not sure".

| Question | Words before | Words now | Note |
|---|---|---|---|
| `$dependent` | 28 | 34 | a question now: "did children live with you, or did you ... support anyone else" |
| `relationship` | 297 | 7, and eight labelled answers (about 150 words; the first is the common one) | the adopted and foster rules are in the first label; the household rules in the last two |
| `age` | 8 | 10 | |
| `lived_all_year` | new | 39 | |
| `months` | 178 | 96 | beneath a No; the born, died, adopted rule is still in it (not finished: see below) |
| `younger` | 27 | 16 | |
| `student` | 136 | 12 | definition in help (42 words) |
| `disabled` | 56 | 39 | |
| `other_claimant` | 31 | 36 | plain words for "qualifying child of any other person"; see "For the owner" |
| `other_nontaxpayer` | 89 | 33 | |
| `parents_apart` | new | 20 | |
| `divorced_rule` | 107 | 34 | beneath `parents_apart` |
| `ever_married` | new | 6 | |
| `married` | 62 | 32 | beneath `ever_married`; still two subjects in one input (not split) |
| `joint_return` | 51 | 28 | beneath `ever_married` |
| `own_money` | new | 27 | |
| `self_support_view`, `supported_view` | new | 18, 14 | three answers |
| `qr_all_year` | 156 | 65 | beneath a No to `lived_all_year`; asks whether the time away was temporary |
| `lawful` | 49 | 11 | |
| `gross_income` | 100 | 27 | detail in help |
| `multiple_support` | 37 | 30 | |
| `kidnapped` | 74 | 33 | beneath a No to `lived_all_year` |
| `citizen_ssn` | new | 28 | |
| `citizen`, `canada_mexico`, `tin`, `work_ssn` | 39, 18, 54, 40 | 24, 10, 28, 24 | beneath a No to `citizen_ssn` |
| `absence_no_return` | 65 | 36 | |
| `us_half`, `eic_ssn` (314) | 155, 79 | 41, 26 | |

## Cost and share (NORMS section 3). All figures are this lane's judgment unless marked *gf*.

29% of filers list someone (*gf* `dependents`). Costs on the owner's scale; "q" is the share who take the cheap exit.

| Parent | g (its cost) | q | C (what it spares) | g < q·C |
|---|---|---|---|---|
| `lived_all_year` | 1 | 0.9 say Yes | months 5, kidnapped 2; for a housemate also `qr_all_year` 5 | 1 < 6 |
| `ever_married` | 1 | 0.97 of children say No; about half of adult relatives | `married` 3 + `joint_return` 3 | 1 < 5.8 |
| `own_money` | 1 | 0.8 of children under 14 say No; few adults | the plain support answer 2, the full test 10 | 1 < 2.4 at least |
| `self_support_view` | 2 | 0.9 are clear | the full test (240 words) 10 | 2 < 9 |
| `supported_view` | 2 | 0.7 are clear | the full test (559 words) 15 | 2 < 10.5 |
| `parents_apart` | 1 | 0.65 say No | `divorced_rule` 3 (was 5 to 15 at 107 words) | 1 < 2 |
| `citizen_ssn` | 1 | 0.95 say Yes | `citizen` 1, `tin` 2, `work_ssn` 2, `eic_ssn` 3 | 1 < 7.6 |

Typical answer costs, before to after: `relationship` 5 to 1; `other_claimant` 20 (form words) to 3; the whole first
sitting for a young child of one's own, my estimate 30 to 9 (nine questions at 1 each).

## Candidates for one tick-list

Heading: **"About this child (or person): does any of these apply?"**, per dependent, with "None of these":

1. `dependent.other_claimant`: another relative they lived with could also claim them
2. `dependent.parents_apart`: their parents are divorced, separated or lived apart
3. `dependent.ever_married`: they have been married
4. `dependent.own_money`: they have money of their own, or own their home

They have adjacent `seq` (13 to 16 of order 120), and their children follow. For the ordinary child all four are No.
`younger` and `lived_all_year` are not in the group: their typical answer is Yes.

## Review debt this lane creates

- Every new gate is an entailment written by this lane and reviewed by no one: the five in the first table, and
  `citizen_ssn`. The formal gates design requires an adversarial review of each ("who would answer No wrongly?").
  The ones I think most worth a second look: `own_money` (a person who owns nothing but whose keep was paid from a
  loan in their name, or from benefits paid to them: the words "benefits in their name" and "a loan" are in the
  prompt for that), and `citizen_ssn` (a naturalized citizen who still holds an old restricted card: the prompt sends
  a restricted card to No).
- Transcription, render, class M, screen, false-no and question reviews of `dependent` are stale. The class M and
  mutation cases state the new inputs but none was written to exercise them; `mutation.json` has no mutant of the
  new lines.
- `tools/transcription/input_contracts/2025/dependent.json` (base inputs of a paid tool) was not updated.
- The new enum `dependent_support_view` and the six-plus-one inputs cite existing passages; the locators were copied
  from the lines they sit beside and were not checked against the archived pages by a tool.

## Ids

Added (7 inputs, all asked): `dependent.lived_all_year`, `dependent.ever_married`, `dependent.own_money`,
`dependent.parents_apart`, `dependent.self_support_view`, `dependent.supported_view`, `dependent.citizen_ssn`.
Added (derived lines, never asked): listed under "Model changes". Removed: none. Renamed: none. The map fixed no id
for this lane, so there is nothing under "Ids changed from the map".

## Where the map was wrong or was not followed

- The map's `$dependent` wording ("Did children, or anyone else you support, live with you or depend on you in 2025?")
  joins two conditions loosely; the bank has "did children live with you, or did you (or, on a joint return, your
  spouse) support anyone else, such as a parent, another relative or a partner?".
- "The adopted, foster and 'in your care' rules as children of `child`" (2.9): not built as children. A child
  question would be asked of every `child` answer (nine in ten dependents) to catch a rare foster case. The rule is in
  the first answer's label instead ("a foster child placed with me by an agency or a court"), and the unplaced child
  falls under the last two answers. Splitting the enum's `child` value would do it properly and was not attempted (it
  changes fixture inputs everywhere).
- "`married` joins two questions: split" (2.9): not split. Both halves are one refusing input and are now behind
  `ever_married`, so few filers meet it.
- "`dependent.born_died`, `placed`, `kidnapped` ... move up as the parents of these rules" (2.9): `kidnapped` now sits
  beneath `lived_all_year`. `born_died` and `placed` did not move: the born, died and adopted cases are answered by
  the second sentence of `lived_all_year` (all of their part of the year), and only a part-time newborn still reads
  the rule inside `months`.

## Places I was unsure

1. **`other_claimant` in plain words.** The form's words are "meet the conditions to be the qualifying child of any
   other person". Read literally that is true of any child who lived more than half the year with an older brother or
   sister, a grandparent, an aunt or an uncle, whether or not that relative would ever claim them, and the model then
   refuses the return (`qc_tiebreak`: the tie-breaker rules are outside the tool). In form words nobody answers Yes for
   an older sibling. The plain prompt names "a parent, grandparent, aunt, uncle, or grown brother or sister" and the
   help says "even if that relative will not claim the person": faithful to the model, and it will refuse more real
   households than the old wording did. "Grown" is narrower than the rule (a 17-year-old sibling counts). See "For
   the owner".
2. **`lived_all_year` and the newborn.** A Yes for a baby born in 2025 who lived with the filer from birth is right
   for every reader of it (the residency exception, the all-year household test, head of household, dependent care).
   I put that in the prompt's second sentence, which takes it to 39 words.
3. **`qr_all_year` reworded** to ask whether the time away was temporary, because it is now asked only after a No to
   "all of 2025". Its Yes and No mean what they meant.
4. **`gross_income`** no longer names the limit, and its definition is in help.
5. **`citizen_ssn` timing.** "Issued before the due date of your return" is in help, not the prompt. A filer preparing
   a late return for a child whose number came after the due date could answer Yes wrongly.
6. **The `parents_apart` share** (35% of children with parents apart) is a guess.

## Found and not fixed

1. **`younger` cannot be skipped for a young child, because of the fixtures.** A dependent under 14 is necessarily
   younger than a filer who is not under 16 (`household.filer_under16` refuses a younger filer), so `younger` could be
   asked only of older dependents (N8). But 16 class M cases (11 in `classm.json`, 5 in `classm.deepseek.json`, for
   example `classm.carloan.1`, `classm.f8880.4`) state a dependent under 14 as not younger than an adult filer and
   expect the result of that. The gate would change those expected values, so it was not built. The cases describe
   an impossible household.
2. **`dependent.dc_child` and `dependent.dc_disabled_qp` read `dc_under13` and `dc_incapable` before the age is
   known** (conjunctions: the D family of `docs/2026-11-11_interview_rules_catalog.md`). In this branch, where
   `f2441.care` (old order 20) is still asked before the dependents (order 120), a young child's parent is asked both
   straight after the list. With care at 155, after the dependents, the age is known first and neither is asked of a
   child under 13 (the baseline walk shows that). If they still appear after the merge, rewrite the two lines as
   nested `choose`.
3. **`claimed_no_tin` is read before the dependent tests** (it is a refusal of `dependent.claimed`), so
   `citizen_ssn` is asked of a relative who is not a child before `multiple_support` and the income and support
   questions. For a child it comes last, by `seq`. **Tried and undone:** reading `meets_tests` before the number in
   `claimed_no_tin` (the same value on complete answers). It made `hoh_test1`, which carries the same refusal entry,
   refuse for a child with a tie-breaker, divorced-parents or married refusal where it is plain false today:
   `stage8.refuse.dependent.other_claimant`, `.divorced_rule` and `.married` changed four expected values each
   (1,851 of 1,854 fixtures). Reverted; the three pass again.
4. **`multiple_support` is asked of every relative who is not a qualifying child, before the support questions**
   (first refusal of `qualifying_relative`). A clear "more than half" to `supported_view` settles it, but the refusal
   is read first. Reordering it needs a screen line like the married ones; not done.

## Requests to other lanes

- **Coordinator (`s3` has no owner):** add "Count costs your employer paid." to the help of `s3.adoption_any`
  (MAP 2.2 item 4).
- **Lane 8b or the coordinator (twins):** `dependent.edu_student_tin` reads `dependent.tin` directly. Point it at
  `dependent.tin_known` (and declare the difference in `reviews/2025/twins.json`) so a dependent student who is a
  citizen with a social security number is not asked `tin` again.
- **Lane 2b:** no request for the `dependent.dc_paid` children reached this lane (lane 2b had no notes on its branch
  when I looked); they are not built. `dependent.dc_*` entries are untouched, still at order 21.
- **Order agent:** the order within the dependent block is fixed by the model's structure, not only by `seq`: a
  line's refusal gates are read one at a time before its expression. `seq` decides only among questions open at
  the same moment. What still arrives away from the topic is under "What the walks show".
- **Whoever merges:** personas `02` and `03` answer the new questions. Persona `03` also answers
  `dependent[child].dc_incapable` and `dc_under13`, which this branch's order asks (item 2 above); once care is asked
  after the dependents those two answers go stale and should be deleted.

## Not finished, in rank order

1. (Map 4) The rules inside the two full support tests (`supported` 559 words, `self_support` 240) are not children:
   the tests are whole, behind "It is close, or I am not sure".
2. (Map 5) `parent_home_paid` (170 words) untouched; `months` (96 words) still carries the rule for a person born,
   adopted, placed or who died in 2025 and lived with the filer only part of that time; `us_half` has no parent
   (a Yes to `lived_all_year` does not settle where).
3. (Map 3) `spouse_relative` (a list of seven kinds of relative), `born_died`, `placed`, `part_year_home` untouched.
4. (Map 6) `married` not split; `multiple_support` not behind the support answer (above).
5. (Map 7) The `dependent.dc_paid` children for lane 2b.
6. `younger` for a young child (above).

## What the walks show (`docs/provisional/walks/after/`, written by `draft-walk` on this branch)

| | Before | After |
|---|---|---|
| Filer with no dependents (`01_single_w2`): the topic | 1 question, 28 prompt words (`$dependent`, a list instruction) | 1 question, 30 words (`$dependent`, now a question) |
| The same filer, whole walk | 86 questions, 6,777 words | 86 questions, 6,779 words |
| A couple's young child (`02`), each child | 12 questions (11 in the first sitting, 1,094 words; `work_ssn` later, 40 words) | 9 questions, 189 words, nothing later |
| The couple, whole walk (two children) | 133 questions, 10,168 words | 127 questions, 8,283 words |
| A single parent's child aged 4 (`03`), first sitting | 11 questions, 1,094 words; age asked fifth; then `absence_no_return`, `work_ssn`, `kidnapped`, `us_half`, `eic_ssn` in four other places | 10 questions, 223 words (the tenth is the release question, because her answer to "parents apart" is Yes); age asked second; then `absence_no_return` (36 words) and `us_half` (41) |
| The single parent, whole walk | 121 questions, 10,100 words | 119 questions, 9,012 words |

The ordinary child's nine questions, in the couple's order: relationship (7 words), age (10), younger than you (16),
another relative who could claim them (36), parents apart (20), ever married (6), money of their own (27), lived
with you all year (39), a citizen with a social security number (28). The typical answers are: first choice, a
number, Yes, No, No, No, No, Yes, Yes.

Still away from the topic, or out of the order `seq` asks for, and what I think each waits on:

- **"Lived with you all year" is asked eighth of a couple's child and third of a head of household's.** `seq` puts
  it third. For a couple it becomes reachable only when the qualifying child chain gets to the residency test, after
  the support and joint return tests (the chain's order is the form's Step 1 order; moving residency up changes which
  refusal a kidnapped, self-supporting child meets first, so I left it). For a head of household the household tests
  reach it at once. The order agent's fix (a question open only behind an earlier unanswered refusal gate) would
  not move it: it waits on the chain, not on a refusal entry.
- **`other_claimant`, `parents_apart`, `ever_married` come before `own_money` and `lived_all_year`** because they are
  the three refusal gates of `qualifying_child`, read before its expression.
- **The second child's questions are cut by `person.tin`, `person.work_ssn`, `s8812.puerto_rico`,
  `household.credit_disallowed`** in the couple's walk. Those are lane 2b's entries, still at old order numbers (2 and
  20) on this branch, which sort before 120; at 310 they will wait.
- **`dependent.dc_incapable` and `dc_under13` straight after the list, `dc_paid` later** (the single parent): lane 2b's
  entries at old order 21, and "Found and not fixed" 2.
- **`absence_no_return`** (head of household) arrives after `household.home_cost`, which is lane 1's and still at an
  old order number on this branch.
- **`us_half`** (order 314) arrives with the earned income credit questions, as the map intends.

## What I ran and saw, and what I infer

Ran and saw, on the committed tree: the build (OK, with its gate, wording and schema checks); `test-fixtures`
1,854 of 1,854; `interview-rules` 0 problems (177 walks, 415 answered in a random order; 0 templates left reachable
at completion, 0 asked and unread); `interview-coverage` 0 problems with the 18 new rows; `draft-walk` 12 personas, 0
problems, from which every figure under "What the walks show" is read; the full `tools/draft_check.sh` (result in the
last section). I read the one-line listings of personas `01`, `02` and `03` after the change, not the full transcripts
of the others.

Inferred, not checked: that a filer gives the answers the entailments assume (the wording is unreviewed); the shares
and costs in the table; that lane 2b's questions stop cutting into the dependents once they carry order 310 (I did not
build that order); that `dc_incapable` and `dc_under13` stop being asked of a young child once care is asked after the
dependents (read from the baseline walk, where care came later, not from a walk in the merged order); that the
locators I copied still quote their pages; and that the Lean evaluator agrees on the new lines (no Lean comparison,
mutation run or engine differential is in the draft check, and none was run).

## For the owner

1. **The plain tie-breaker question will refuse more households, truthfully.** "Could another relative the person
   lived with also claim them: a parent, grandparent, aunt, uncle, or grown brother or sister?" A Yes for a child who
   passes your own tests refuses the return (the tie-breaker rules are outside the tool), and that has always been
   the model: three generations in one home, unmarried parents living together, a grown sibling at home. The old
   wording ("meet the conditions to be the qualifying child of any other person") hid it. Either the refusal is
   narrowed (the tie-breaker rules built for the common cases, where a parent wins) or the question keeps refusing
   them. This is the one place where plain words change who is refused in practice, without changing the model.
2. **Nine questions per ordinary child, all answered at once.** Four of them (another relative could claim them;
   parents apart; ever married; money of their own) are the tick-list candidates: one screen with "None of these"
   would make it six screens. `younger` would go too for a young child, but for the 16 class M cases above.
3. **A parent who says "all year" for a baby born in 2025** is relying on the second sentence of that question. If
   you would rather not have a parenthesis there, the alternative is a No and the 96-word months question.
4. **The two support tests are whole, behind "It is close, or I am not sure".** Whether a filer who picks "clearly
   more than half" for an elderly parent on social security is right is exactly the risk the 559 words were written
   against; the plain question's help says what the person paid from their own income or benefits is not paid by
   you. A reviewer should look at that one first.

## The full check

`tools/draft_check.sh` on commit `e495e1f2` (tree `d80c45ba46e8`): **green**. build OK (638 s); test_fixtures
1,854 of 1,854; interview_rules 0 problems; interview_coverage 0 problems; person_wording current; spouse_self_test
passed; check_self_test 95 cases; test_integration 696 invocations; properties (report written); test_serve 337
checks; draft_walk_self_test passed; twins 0 problems; render_check current. The commit after it adds these notes and
the reports the check itself rewrote, and changes no form, bank entry, fixture or engine file.

Correction: the message of commit `e495e1f2` says the coverage check walked 107 rows. It walked 97 (79 that were
there, and this lane's 18).
