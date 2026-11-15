# Lane notes: 2b (care for a child or dependent; the credits for a family)

Branch `lane/l2b`. Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no
model call was made. Form files owned: `f2441`, `dcprov`, `s8812`, `eic`. Bank entries owned: those files', and bank
only `dependent.dc_*` (4), `w2.box10`, `w2.box10_wages`, `household.credit_disallowed`, `person.tin`, `work_ssn`,
`itin_applied`, `eic_ssn`, `born_after_1960`, `born_before_2001`.

A successor continues from "Not finished, in rank order". The scripts that made the edits are not in the tree (they
were one-off text edits); every change they made is in the commits and listed here.

## Order numbers and seq (as set)

| Order | What | Questions, in `seq` order |
|---|---|---|
| 155 | Care: the two opening questions, the care screens, then box 10 of each W-2 | `f2441.care` 1, `f2441.benefits` 2, `f2441.care_other` 3, `f2441.nondependent` 4, `f2441.prior_year` 5, `f2441.student` 6, `f2441.unable` 7, `f2441.spouse_died` 8, `w2.box10` 11, `w2.box10_wages` 12 |
| 156 | The employer's help in figures | `f2441.line13` 1, `f2441.line14` 2, `f2441.plans_differ` 3, `f2441.plan_max` 4, `f2441.employer_care` 5, `f2441.paid_2026` 6 |
| 157 | Who provided the care, then what it cost, person by person | `$dcprov` 1, `dcprov.paid` 2, `dcprov.household` 3, `dcprov.tin_kind` 4, `dcprov.related` 5, `dependent.dc_under13` 6, `dependent.dc_incapable` 7, `dependent.dc_over12_care` 8, `dependent.dc_paid` 9 |
| 310 | Last checks for the credits for a family (once per return) | `household.credit_disallowed` 1, `s8812.combat_pay` 2, `s8812.puerto_rico` 3 |
| 311 | Each person's number and age | `person.tin` 1, `person.itin_applied` 2, `person.work_ssn` 3, `person.eic_ssn` 4, `person.born_after_1960` 5, `person.born_before_2001` 6 |
| 312 | Not used | |
| 313 | The earned income credit's own questions | `eic.same_home` 1, `eic.legally_separated` 2, `eic.died_2025` 3, `eic.us_home` 4, `eic.lived_with_relative` 5, `eic.qc_of_another` 6 |

`f2441.benefits` is second, before the children of `f2441.care`, for a reason of the engine and not of the topic: see
"Questions that still arrive away from their topic", item 1.

The three numbers are cut where they are because of two things seen in the walks (of the single parent, and of a
temporary persona with employer benefits; not read in the engine):

- In a block that mixes kinds of question, the once-per-return questions are asked first, whatever their `seq`, then
  the questions asked per W-2, per provider or per person cared for. So box 10 (per W-2) closes 155 and the amounts
  that refer to it open 156.
- `dependent.dc_paid` is not reachable until every provider's `dcprov.related` is answered (the refusal for a
  provider who may not be listed stands before the sum of the amounts). With the amounts numbered before the
  providers, the amount was asked in the middle of a provider's questions, as in the baseline. So the providers come
  first in 157 with `dcprov.related` as each one's last question, and the amounts follow.

`f2441.paid_2026` cannot be placed after the per-person amounts with the numbers I have (a once-per-return question
goes first in its block), so it is worded to be right before them: "that is not in the amounts you give for each
person cared for".

`dependent.us_half` and `dependent.eic_ssn` are lane 2a's bank entries (Part 3 of the map; slot 314), though Part 1
and my ranked list name them under 2b. I did not edit them; the wording I would give `dependent.eic_ssn` is under
"Requests to other lanes".

The boilerplate help "Married filing separately and unsupported items are refused with citations." is deleted from
every entry of mine. The frame of the care provider questions is "For this care provider — " (it named Form 2441,
Part I).

## The full check is red at one stage: `interview-rules`, 2 problems

Every other stage of `tools/draft_check.sh` passes on the final tree. `interview-rules` reports, both in the
generated return `generated.10`:

- `person[taxpayer].tin`, "until `person[taxpayer].edu` was answered: `person.tin` is reachable before the answer that
  hides it, and the walk in bank order never asks it";
- `dependent[dep_a].edu_tin_issued`, in a random order, the same.

Both are of the kind the check calls order-dependent reach: a question that some order of answering reaches although
the complete return never needs it. The check passes such a template only when it is held, with a reason, in
`tools/interview_rules_baseline.json`. That file is not mine, and I did not edit it.

What I tried, and saw: I returned `person.tin` and `person.itin_applied` to their numbers of today (2 and 3), on the
thought that numbering them after the education questions caused it, and ran the check again. It did not help:
`dependent.edu_tin_issued` was reported as before, and `person.tin` was then reported the other way round ("asked in
bank order and unread by the complete return"). So `generated.10` shows a defect whichever side of the education
questions `person.tin` is numbered. I put the two questions back at 311, where the map has them; the tree committed
is the one the full check ran on.

What I infer, and did not check: that the defect is in the model and was there before this lane (a conjunction in
the education lines of `person.yaml` and `dependent.yaml` that reads `person.tin`, through `household.all_tin`, and
`dependent.edu_tin_issued` without waiting for the answer that decides whether they matter), and that it shows now
because the random returns the check generates are drawn from the model's inputs, which my three new inputs changed.
For it: the same check passed after my bank-only step (92 generated returns classed, 0 problems), which had
`person.tin` at 311 already, and reports 95 returns classed now; and neither question, nor any line that reads them,
is in a file I changed. Against it: I did not run the check on the tree before my model step with these same
returns, so I cannot rule out that my change has a part in it.

**For the coordinator**, either: hold the two templates in `tools/interview_rules_baseline.json` under
`order_dependent_reach` with this reason; or have lanes 4b and 2a rewrite the two conjunctions as nested chooses
(formal gates design, "Leaking conjunctions"). Other lanes that add inputs will change the generated returns again,
so the list seen after the merge may differ.

## What changed, by question

### Model changes (three; all in `f2441.yaml` and `eic.yaml`)

| Change | Inputs added | Input removed | Gate or derived line | Readers edited |
|---|---|---|---|---|
| A. A plain parent in front of `f2441.nondependent` (114 words, a refusal) | `f2441.care_other` | none | `f2441.nondependent` is `gated_by: f2441.nondependent_if_other`, a choose on the helper `f2441.care_other_or_claimable` (true when `f2441.care_other` is Yes or `sa.dependent` is Yes) | `f2441.nondependent_gate` reads the gate line. Its id, and the refusal recorded at it, are unchanged |
| B. A plain parent in front of `eic.qc_of_another` (the term of art "qualifying child of another person") | `eic.lived_with_relative` | none | `eic.qc_of_another` is `gated_by: eic.qc_of_another_if_lived` | Its five readers (`eic.not_qc_of_another`, `eic.step4_dependent`, `eic.check_27c` twice, `eic.separated_box`) read the gate line |
| C. `f2441.student_disabled` (two subjects) split | `f2441.student`, `f2441.unable` | `f2441.student_disabled` as an input | `f2441.student_disabled` stays, as a derived line true when either is true (the map's rule 4.1, item 2: it worked here) | None: the four refusal entries `when: f2441.student_disabled` are untouched, so the refusal and its gate id are the same |

Fixtures: inputs only. Every case that stated `f2441.nondependent` also states `f2441.care_other` with the same value
(153 places); every case that stated `eic.qc_of_another` also states `eic.lived_with_relative` with the same value
(276 places); every `f2441.student_disabled` became `f2441.student` with that value and `f2441.unable: false` (154
places; the cases that had it true do not say which of the two facts they mean, so they are students).
`fixtures/2025/defaults.json` has the three new defaults (false) and no longer `f2441.student_disabled`. No expected
value and no expected refusal was edited; the fixtures passed 1854 of 1854 after the change. The two case
generators (`tools/ny_fixtures.py`, `tools/engines/generate_cases.py`) name the new inputs; I did not run them.

**Why the parent of A is safe (who could answer No wrongly).** `f2441.care_other` asks: "Was any of that care for
anyone other than your children under age 13 whom you listed on this return as dependents?" The narrow question
describes two kinds of person. A child the filer cannot claim (the other parent claims the child) is either not listed
(Yes to the parent) or listed, and then the dependents topic meets it first (`dependent.divorced_rule` refuses). A
person not able to care for themselves who is not a dependent because of income, a joint return, or the filer's own
status is an adult, an older child, someone else's child or not listed (Yes to the parent), with two exceptions I
found: (1) the filer can be claimed as a dependent, so none of the listed children is a dependent: the gate asks the
narrow question whenever `sa.dependent` is Yes, whatever the parent's answer; (2) a listed child under 13 of the
filer's own who is not their qualifying child (the child pays over half of their own support) and is disabled with
income of $5,200 or more: not guarded, and I think it does not occur. Coverage rows: `care.other_person_not_dependent`,
`care.other_person_is_dependent`, `care.own_children_only`. (A row for exception (1) cannot be written: today a Yes
to `sa.dependent` refuses the return before the care topic, so the guard is a second line of defence only.)

**Why the parent of B is safe.** A person is the qualifying child of another only if that other is their parent,
stepparent, foster parent, brother or sister (step and half included) or an ancestor of one of those, and the two
lived together in the United States for more than half of 2025 (read in `sources/2025/i1040gi-html.txt`, Step 3,
"A qualifying child for the EIC is your..."). `eic.lived_with_relative` asks that necessary condition as a fact of
life: "did you live for more than half the year in the same home as your parent, grandparent, brother, sister, aunt
or uncle, or a foster parent? Count time you were temporarily away, for example at school." The wrong No I see is a
student who lives at college and does not think of that as living at home: the second sentence is for them. The help
names the rarer relatives (stepparents, half brothers and sisters, great-grandparents, great-aunts and great-uncles).
The narrow question then states the three age tests and the exception for a relative who need not file, as a list.
Rows: `eic.lived_with_no_relative`, `eic.lived_with_relative_not_their_child`, `eic.qualifying_child_of_another`.

### Bank changes (wording, help, labels; no model change)

Words are of the stored text (frame and spouse phrase included; a filer not filing jointly is shown about seven fewer
where the phrase stands), counted from the bank and the form sources before (commit `100b132c`) and now.

| Question | Prompt words before → now | What was done |
|---|---|---|
| `f2441.care` | 134 → 42 | One plain question. "Use or pay for" keeps the cases the long text named (2025 care not yet paid; a 2024 bill paid in 2025) and care an employer paid for. The third kind of person (not your dependent) is the child `f2441.nondependent` |
| `f2441.benefits` | 41 → 35 | Widened to "your employer, or your own business, help pay", as the map's 2.2 item 5 requires for lane 9's `scope.care_benefits_other` |
| `f2441.nondependent` | 128 → 110 | Still long: two situations as two bullets. Reached only after a Yes to `f2441.care_other` (29 words) |
| `f2441.student_disabled` → `f2441.student`, `f2441.unable` | 55 → 26 + 27 | See change C. `unable` has a bank prompt in a person's words; the form line keeps the source's |
| `f2441.prior_year` | 20 → 24 | "a bill for care of this kind that was given in 2024" |
| `f2441.spouse_died` | 6 → 8 | "Did your husband or wife die in 2025?" (the map's question 4 wording) |
| `f2441.line13`, `line14`, `plans_differ`, `plan_max`, `employer_care` | 45, 60, 26, 49, 36 → 38, 59, 24, 42, 31 | Questions that say where the amount is read |
| `f2441.paid_2026` | 86 → 59 | "that is not in the amounts you give for each person cared for": worded to be right before or after those amounts |
| `w2.box10_wages` | 43 → 38 | A question. `w2.box10` is unchanged (lane 3 sets the register of the box questions) |
| `$dcprov` | 21 → 14 | "Who provided the care in 2025?" |
| `dcprov.paid`, `household`, `tin_kind`, `related` | 48, 54, 107, 78 → 45, 21, 12, 67 | `tin_kind` has a plain label for each of its five values; `related` is a four-item list and is each provider's last question |
| `dependent.dc_under13`, `dc_incapable`, `dc_over12_care` | 67, 50, 52 → 16, 35, 24 | Short; the rule only the rare answer needs is help |
| `dependent.dc_paid` | 529 → 422 | **Interim, and still far over the norm.** A plain first line and the same items as lists. Nothing was dropped. The fix is children, in `dependent.yaml` (lane 2a): see "Requests to other lanes" |
| `household.credit_disallowed` | 85 → 41 (help 127 → 39) | The clause on a 2- or 10-year ban is gone from the prompt: a ban follows a claim the IRS refused, which the question already asks |
| `s8812.combat_pay` | 27 → 36 | The fact first ("paid for military service in a combat zone"), then the box. Longer |
| `s8812.puerto_rico` | 18 → 24 (help 91 → 46) | "a resident of Puerto Rico (in the tax term, a 'bona fide resident')" |
| `person.tin`, `itin_applied`, `work_ssn`, `eic_ssn` | 54, 71, 50, 89 → 36, 37, 27, 51 | By what the card says; the dates and the rarer card wordings are help. `eic_ssn` says in the prompt that nearly every number counts and sends the two rare cards to the help by their wording. "The 2025 return", not "your 2025 return", so that the spouse's entry does not read "your spouse's 2025 return" |
| `eic.died_2025`, `eic.us_home` | 18, 53 → 19, 22 | `us_home`: the definition of the United States and the military rule are help |
| `eic.qc_of_another` | 47 → 80 | Longer, on purpose: it now states the three tests it used to leave to the term "qualifying child", and is reached only after a Yes to `eic.lived_with_relative` (38 words) |

All 40 questions of the lane together: 2,346 prompt words before (37 questions), 1,758 now. Help: 697 words before (of
which about 300 were the boilerplate sentence), 895 now. The help grew: 23 questions that had only the boilerplate now
have real help of 12 to 52 words. Four are over the 40 the map allows: `person.eic_ssn` and `s8812.puerto_rico` (52
each), `f2441.benefits` and `f2441.care_other` (42 each).

### Coverage rows

`interview/2025/coverage/care.yaml`: nine rows. Care: `care.other_person_not_dependent`,
`care.other_person_is_dependent`, `care.own_children_only`, `care.bill_for_2024`, `care.student`,
`care.unable_to_care_for_self`. The earned income credit: `eic.lived_with_no_relative`,
`eic.lived_with_relative_not_their_child`, `eic.qualifying_child_of_another`. `credits.yaml`: the row
`credits.elderly_65` no longer answers `person[taxpayer].work_ssn`, which is now asked after that row's refusal.

## Cost and share (my estimates, for the owner to overrule)

Shares marked *gf* are from `interview/2025/gate_frequencies.yaml`; the others are my judgment. Costs are on the
owner's scale (1 known at once, 5 a moment's thought, 20 must find out what is asked).

| Question | Asked of | Share who say Yes | Cost of the typical answer, before → now | N3 for a new parent |
|---|---|---|---|---|
| `f2441.care` | everyone | 4.5% *gf* | 5 → 1 | |
| `f2441.benefits` | everyone | 1.2% *gf* | 3 → 1 | |
| `f2441.care_other` (new parent) | filers with care, 4.5% | 3% est. | 10 (the 114 words) → 1 | g = 1, q = 0.97, C = 10: 1 < 9.7 |
| `f2441.student`, `f2441.unable` | filers with care or benefits | 2% each est. | 3 → 1 + 1 | not a parent: one question with two subjects became two |
| `f2441.prior_year`, `f2441.spouse_died` | filers with care (the second on a joint return) | 3%, 0.3% est. | 1 → 1 | |
| `dcprov.*` (4 per provider) | filers with care | | 3 each → 1 each | |
| `dependent.dc_paid` | per person cared for | | 15 → 10 | the children would make it 3 |
| `eic.lived_with_relative` (new parent) | a filer not filing jointly who reaches the credit's last steps: about 8% est. | 15% est. | 20 (a term of art, answered blind) → 2 | g = 2, q = 0.85, C = 20: 2 < 17 |
| `eic.qc_of_another` | those who say Yes above | 30% est. | 20 → 5 | |
| `household.credit_disallowed` | returns with a child credit or the earned income credit, about 30% | 1% est. | 5 → 2 | |
| `s8812.combat_pay` | the same, and filers with care | 0.1% | 2 → 1 | |
| `s8812.puerto_rico` | returns with a child for the child tax credit | 0.2% *gf* | 2 → 1 | |
| `person.tin`, `work_ssn`, `eic_ssn` | each person, where a credit or deduction needs it | 97% or more say Yes | 5 → 1 each | |

## Before and after, from the persona walks

(Counts are of this lane's questions only: `f2441.*`, `$dcprov`, `dcprov.*`, `dependent.dc_*`, `w2.box10*`,
`s8812.*`, `eic.*`, `household.credit_disallowed`, `person.tin`, `work_ssn`, `itin_applied`, `eic_ssn`, `born_*`.)

| Persona | This lane's questions, before | Prompt words | Now | Prompt words | Whole walk before → now (questions, prompt words) |
|---|---|---|---|---|---|
| `01_single_w2` (nothing in the topic) | 2 | 161 | 2 | 63 | 86, 6,777 → 86, 6,679 |
| `03_single_parent_child_care` (the ordinary case: one child, one day care, no employer help) | 18 | 1,489 | 19 | 914 | 121, 10,100 → 122, 9,525 |
| `02_couple_children_mortgage` (children, no care) | 8 | 437 | 7 | 203 | 133, 10,168 → 132, 9,934 |
| `07_college_student` (low earner, the earned income credit's checks) | 7 | 314 | 7 | 161 | 110, 7,747 → 110, 7,594 |
| `09_tips_overtime` | 3 | 200 | 3 | 79 | 95, 7,363 → 95, 7,242 |

The filer with nothing is asked the same two questions, in 63 words where there were 161. The single parent is asked
one question more (the new parent `f2441.care_other` in place of the 114-word `f2441.nondependent`, and the student
question as two) and reads 575 fewer words; 422 of her 914 are the one amount `dependent.dc_paid`. The couple lose
one question: `person[taxpayer].work_ssn` is no longer asked once the spouse's answer has settled what it was needed
for (an effect of the new order, not of a model change; I removed that answer from the persona, as the walk lane's
notes direct for an answer no longer reached).

Sittings for care (the single parent): three before (question 98; 100 to 102; 109 to 114, with the amount asked in
the middle of the provider's questions); two now (98 and 99, the two opening questions; then 105 to 114 in a row:
the screens, the provider, the amount). A filer with employer benefits (a temporary persona, not committed: the
single parent with $3,000 in box 10) is asked the whole topic in one sitting of 20 questions, 98 to 117.

The walks were written to a temporary directory, not to `docs/provisional/walks/after/` (every lane would write the
same twelve files there).

## Questions that still arrive away from their topic

1. **Five questions of other topics stand between the two opening care questions and the rest of the topic** for a
   filer with care and no employer benefits (`03`, questions 100 to 104: `dependent.kidnapped`, `qbi.unsupported`,
   `qbi.carryforward`, `dependent.us_half`, `dependent.eic_ssn`). They carry lower order numbers and become
   reachable at that moment. What I think they were waiting on (inferred from the walks, not traced in the engine):
   the answer to `f2441.benefits`, because taxable care benefits are part of total income (Form 1040 line 1e), and
   the deduction for business income and the credits read income. For the filer with benefits they come after the
   whole care topic, when the last benefit amount is in. The rest of the care topic cannot be asked before
   `f2441.benefits` either: the refusals behind `f2441.care_other` stand on lines that `f2441.line3` reaches only
   through a choose on `f2441.benefits`. That is why `f2441.benefits` has `seq` 2. **Wanted from the order agent:** a
   block once begun is finished before a question of an earlier topic that has just become reachable is asked; and
   (the map's 4.8 item 1a) a child asked directly after its parent, which would let `f2441.care_other` and the other
   screens follow `f2441.care` at once and `f2441.benefits` come after them.
2. **The last checks (310 to 313) arrive one or two at a time**, in the order the model comes to need them, not in
   number order (`03`, 115 to 122): `s8812.combat_pay` first (the care form's earned income line refuses on it, so it
   closes the care topic), then `person.tin` and `work_ssn`, then `household.credit_disallowed` and
   `s8812.puerto_rico` (once a child credit is claimed), then `person.eic_ssn`, `f1040.tax_exempt_interest` (lane
   5a's), then the earned income credit's own questions. Each waits on a computed condition, as the map said they
   would; no numbering of mine changes it. They do come after every other topic on this branch, since everything
   else still carries a number below 100.
3. `person.work_ssn` is asked wherever a deduction or credit first needs it (for the server, `09`, straight after the
   care questions at 85). After the merge I expect it to become reachable while lane 3's overtime and tips topic
   (150) is asked and to wait until 311, far from the question that needed it; the same for `person.tin`. Not seen:
   it depends on the merged order.
4. `dependent.dc_paid` (per person cared for) is asked after all the providers, not provider by provider or person by
   person with its provider. That is the order I chose given what is reachable when; it reads well in the walks.

## Not finished, in rank order

1. **`dependent.dc_paid` is 422 words.** The children are a model change in `dependent.yaml` (lane 2a). Specification
   under "Requests to other lanes". When they exist, the bank prompt becomes its first line only.
2. **`f2441.nondependent` is two subjects** (a person not able to care for themselves who is not a dependent; a child
   another parent claims). Split it as C was split: two inputs, `f2441.nondependent` kept as the derived line. Both
   stay beneath `f2441.care_other`.
3. **`eic.died_2025` is two subjects** (your husband or wife died; the return is for a person who died). Left as one
   input because the map's question 4 leaves the death questions to the coordinator.
4. **`household.credit_disallowed`**: the map wants the years and the ban as children. `household.yaml` is lane 1's;
   I reworded the bank entry only (34 words), with the years in the help.
5. **The benefit amounts** `f2441.line13` and `f2441.line14` are asked of every filer with benefits and are zero for
   most. A yes or no parent over each would pay (g = 1, q = 0.9, C = 3). Two gates in `f2441.yaml`; not built (1.2%
   of filers).
6. **`dcprov.related`** is asked of a day care center, for which it makes no sense. A first question "Is this
   provider a person or a business?" would spare it; not built.
7. `tools/coverage/tree.json`, `tools/coverage/categories.json` and `docs/COVERAGE.md` do not know the two new gate
   lines or the split (they are not in the draft check).

## Requests to other lanes

- **Lane 2a (`dependent.yaml`): the children of `dependent.dc_paid`.** Parent, one line: "How much did you pay in
  2025 for this person's care in 2025, so that you could work or look for work?" Then, each a yes or no about the
  amount just entered, a Yes asking the part to leave out (or showing the rule and asking the figure again):
  (a) "Does that include care given in 2024 or 2026, or 2025 care you had not paid for by December 31, 2025?";
  (b) "Does it include school from kindergarten up, summer school, tutoring or an overnight camp?";
  (c) "Does it include food, lodging, clothing or lessons billed apart from the care?";
  (d) "Was any of it paid back to you by a state social services agency, or do you claim any of it as a medical expense?";
  (e) "Did you work, or look for work, on only some of the days the bills cover?" (the part-time rules beneath);
  (f) for a person who is not the filer's dependent child under 13: "Was the care outside your home?" (the 8-hour rule beneath);
  (g) "Does it include a housekeeper, cook or cleaner?" (what counts beneath).
  The payments to relatives are already asked per provider (`dcprov.related`) and need no child. The items to add
  (employment taxes, a provider's trips, agency fees, a prepayment in 2024) are help.
- **Lane 2a: `dependent.eic_ssn`** in the words of `person.eic_ssn`: "Does this person have a social security number,
  on a card that does not say 'Not Valid for Employment'?", with the same help.
- **Lane 4b (`person.yaml`): one fact, asked three times.** `person.tin`, `person.work_ssn` and `person.eic_ssn` are
  one card. A person who answers Yes to `work_ssn` is asked `eic_ssn` a few questions later, which reads as the same
  question (N8). Wanted: "Do you have a social security number?", and beneath a Yes one question on what the card
  says (nothing; "Not Valid for Employment"; "Valid for Work Only With DHS Authorization"), from which the three
  inputs follow; the date of issue as a child of its own. The two dates of birth (`born_after_1960`,
  `born_before_2001`) are pieces of one date of birth (the walk lane's observation 10).
- **Lane 9 (`scope.yaml`):** `f2441.benefits` is widened as the map asked, so `scope.care_benefits_other` can sit
  beneath it. `s8812.combat_pay` belongs beneath `scope.armed_forces` (a person who never served has no combat pay):
  after the merge, gate it there; today it is asked of every return with a child credit, the earned income credit or
  care.
- **Lane 7b:** `s2.household_employee` (159) and my `dcprov.household` ask a nanny's employer about the same nanny;
  the second is per provider and is only a notice. Worth one look after the merge.
- **The order agent:** the two items under "Questions that still arrive away from their topic".
- **The coordinator:** a death in 2025 is asked in my lane as `f2441.spouse_died` and `eic.died_2025`, both now
  worded "Did your husband or wife die in 2025" (the second adds "or is this return for a person who died in 2025").

## Candidates for one tick-list

One group, all short facts about the same year, each asked of every filer who answered Yes to care, each recorded as
its own answer; they have adjacent `seq` (155: 3, 5, 6, 7, 8). Heading: **"About that care. Do any of these apply?"**

- Some of it was for someone other than your children under 13 whom you listed (`f2441.care_other`)
- You paid a bill in 2025 for care given in 2024 (`f2441.prior_year`)
- You (or your spouse) were a full-time student during five months of 2025 (`f2441.student`)
- You (or your spouse) could not care for yourself at some time in 2025 (`f2441.unable`)
- Your husband or wife died in 2025 (`f2441.spouse_died`; joint returns only)

Not candidates: `household.credit_disallowed`, `s8812.combat_pay` and `s8812.puerto_rico` are short and asked
together, but they are three unrelated subjects.

## Ids changed from the map

None of the ids fixed in the map is mine. New ids: `f2441.care_other`, `f2441.care_other_or_claimable` (helper),
`f2441.nondependent_if_other` (gate line), `f2441.student`, `f2441.unable`, `eic.lived_with_relative`,
`eic.qc_of_another_if_lived` (gate line). `f2441.student_disabled` is no longer a question.

## Review debt

- Every reworded question's transcription, render, screen and question review logs are stale.
- The two new gates (`f2441.nondependent_if_other`, `eic.qc_of_another_if_lived`) have had no adversarial review of
  who answers No wrongly (formal gates design, rule 7); my own analysis is above. No Lean comparison, no mutation
  run.
- Class M and mutation fixture inputs were edited as text, not regenerated.
- `reports/2025/interview_words.md` and the other reports the draft check does not rewrite are not current.

## Where I was unsure

- **`f2441.care` at 35 words** is over the 25 aimed at for a parent. Each clause guards a wrong No I could name:
  "use or pay for" (care an employer paid; a bill not yet paid; a 2024 bill paid in 2025, which must still reach its
  refusal), "someone living with you who could not care for themselves" (an elderly parent, whom "disabled person"
  might not bring to mind), "or look for work".
- **`f2441.prior_year` refuses on the fact** (a 2024 bill paid in 2025), though the extra credit it leads to is
  optional and the return is right without it. By the map's 4.3 it could ask the wish and end "To go on without it,
  answer No". That would change who is refused, so I left it: a decision for the owner.
- **The map's ownership of `dependent.us_half` and `dependent.eic_ssn`** is stated two ways; I followed Part 3.
- **`s8812.puerto_rico`'s help** keeps the three tests by their terms (presence test, tax home, closer connection), as
  it had them; I did not find plain words for them that I could ground. It ends "If you are not sure, answer Yes".
- **`person.eic_ssn`**: the prompt tells a filer whose card carries one of two wordings to open the help, where the
  rule is. That is help the rare answer needs, which the norms put in a child (the request to lane 4b).
- **`eic.qc_of_another`** decides the credit itself, so its help does not say "if you are not sure, answer Yes" (a
  wrong Yes loses the credit); the parent `eic.lived_with_relative` does say it (a wrong Yes there costs one question).

## Found and not fixed

- **The two leaks `interview-rules` reports** (the section near the top), in `person.yaml` and `dependent.yaml`.

- **A filer with no income is asked the earned income credit's questions** (`person.eic_ssn`, then the age and home
  questions), because the steps are modelled in the instructions' order and earned income is the fifth. The credit is
  zero whatever they answer. Asking the earned income test first would spare them; it is a model reordering in
  `eic.yaml` with the same result, not done here.
- `dependent.dc_incapable` is asked for every listed person who is not a young child once care is answered Yes (a
  healthy 15-year-old included). It could sit beneath `f2441.care_other`, which already asks whether any of the care
  was for someone else; that is a change in `dependent.yaml`.

## What I ran and saw, and what I infer

Ran and saw:

- `npm run build --silent` at the start (OK), and the build inside each check.
- After the bank-only step (commit `a5967985`): the build, `test-fixtures` (1854 of 1854), `interview-rules` (0
  problems), the coverage rows (79 walked, 0 problems after I dropped the one stale answer in `credits.elderly_65`).
  These ran as the stages of `tools/draft_check.sh --quick`, the coverage stage a second time by itself.
- After the model step: the build (OK; gated inputs 67 → 69), `test-fixtures` (1854 of 1854, no expected value or
  refusal edited), the nine rows of `coverage/care.yaml` by `interview-coverage --rows` (0 problems; a tenth row, a
  filer who can be claimed as a dependent, was removed because the walk refuses at `sa.dependent` before it reaches
  care, so the extra guard on `sa.dependent` in the gate of `f2441.nondependent` is never the deciding one today).
- The twelve persona walks on the final build (0 problems), the single parent's read in full for this lane's
  questions as shown; a temporary thirteenth persona with employer benefits, for the order inside the care blocks.
- `reports/2025/person_wording.md` for the four per-person questions, in each shown form.
- The full `tools/draft_check.sh` on the final tree (the tree of commit `aabc3c0f`): **RED, one stage**. build OK;
  fixtures 1854 of 1854; `interview-rules` FAIL, 2 problems (the section near the top); coverage rows 0 problems (88
  rows in 4 files); person wording report current; spouse-wording self-test, check self-test passed; integration 696
  invocations passed; properties passed; server test 337 checks passed; draft-walk self-test passed; twins 0
  problems; `render --check` passed.
- A second full run with `person.tin` and `person.itin_applied` at their old numbers, stopped after its third
  stage: build OK, fixtures 1854 of 1854, `interview-rules` FAIL with 2 problems again.
- Read in the archived instructions (`sources/2025/i1040gi-html.txt`): the earned income credit's Step 3 and Step 4
  questions, the table "A qualifying child for the EIC is your...", and the definition of a full-time student.

Inferred, not checked:

- That the wording of each reworded question means what its form line's source means. I worked from the form YAML's
  `source` text (itself reviewed against the instructions), not from the instructions, except for the passages
  named above. No review of any kind was run on the new wording.
- The two rules of block order stated under "Order numbers and seq" (seen in two walks each, not read in
  `askOrder`), and what the interrupting questions were waiting on.
- The shares and costs in the table.
- That nothing outside the draft check breaks: `tools/coverage/`, the Lean comparison, the case generators and the
  New York profile's own checks were not run (the New York fixtures are among the 1854).
