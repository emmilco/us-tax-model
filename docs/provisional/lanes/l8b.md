# Lane notes: 8b (education, student loans, home energy improvements)

Branch `lane/l8b`. Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no
model call was made. Form files owned: `f8863`, `aqee`, `sli`, `f5695`. Bank only (both twins in one commit):
`person.edu*`, `dependent.edu*`.

**How to continue this work.** The changes are made by scripts in `docs/provisional/lanes/l8b_work/`, run from the
worktree root, so that a wording change is one edit and a rerun:

| Script | What it does |
|---|---|
| `bank.py <words module>...` | Rewrites this lane's entries of `interview/2025/questions.yaml` from a wording module, and the twins' declared prompt differences in `reviews/2025/twins.json`. Rerunnable |
| `words_education.py` | Wording, order and `seq` of the education and student loan questions |
| `words_energy.py` | Wording, order and `seq` of the Form 5695 questions |
| `f5695_model.py`, then `f5695_model2.py`, then `f5695_model3.py` | The model change of `forms/2025/f5695.yaml`, in three steps. Each is applied once (it refuses to run twice) |
| `fixtures.py sli` / `fixtures.py f5695` | Rewrites fixture *inputs* for the two model changes (never an expected value). Rerunnable |

Status of each step is in "Steps" below; the last section says what is not done.

## Order numbers and blocks

| Order | Block | Questions (by `seq`) |
|---|---|---|
| 230 | Home energy improvements | `f5695.any`; the 17 kinds (three tick-lists); what ends the interview; then, per part, its conditions and amounts |
| 239 | The 2024 carryforward | `f5695.carry`, `f5695.line12` (beneath `s3.prior_other_forms`; see "Requests to other lanes") |
| 240 | Education opener | `f8863.paid` |
| 241 | Each student (twins) | `edu`, `edu_1098t`, `edu_inst`, `edu_a2025`, `edu_a2026`, `edu_refunds`, `edu_over`, `edu_line23` to `edu_line26`, `edu_ein`, `dependent.edu_tin_issued`, `edu_mat` |
| 242 | Earlier trouble with the credit | `f8863.ban` |
| 243 | The filer's own age, support and schooling (the refundable part) | `person.edu_born_2007`, `edu_born_2002`, `edu_half_support`, `edu_fulltime`, `edu_parent` |
| 244 | Student loans | `sli.any`, `sli.interest`, `sli.unqualified_any`, `sli.unqualified`, `sli.assisted_any`, `sli.assisted` |

**The twins do not share a `seq`.** The map asks for the same `order` and `seq` on both sides of a twin; the order
agent's contract (`docs/provisional/lanes/order.md` on `lane/order`, section 1.5) makes the build refuse two questions
of one order number with the same `seq`. So both sides keep order 241 and run in the same sequence, a person's
questions at 10, 20, ... and a dependent's at 210, 220, ...; each pair's `interview.seq` is a declared difference in
`reviews/2025/twins.json` (written by `bank.py`). The order contract was read after the first commit; nothing on
this branch was built or checked against the order agent's engine.

245 and 246 are free. The once-per-return questions (`f8863.paid`, `f8863.ban`) have order numbers of their own
because a block that mixes per-return and per-person questions waits on the order agent's rule (MAP 4.8, 1b).

## What changed, by question

### Student loans (`forms/2025/sli.yaml`; model change)

`sli.interest` was one amount with 244 words: what a qualified loan is, and two kinds of interest not to count.
Now:

- `sli.any` (new, asked of everyone): "Did you (or, on a joint return, your spouse) pay interest on a student loan in 2025?"
- `sli.interest` (gate line `sli.interest_if_any`): the amount by the paper, Form 1098-E box 1.
- `sli.unqualified_any` (new) and `sli.unqualified` (new amount): loans that are not qualified student loans (from a
  relative or an employer plan; used partly for something else; taken out for someone else). The amount is subtracted.
- `sli.assisted_any` (new) and `sli.assisted` (new amount): interest paid from tax-free 529 earnings or by a health
  workers' loan repayment program. The amount is subtracted.
- `sli.qualified` (new derived line) = interest less the two amounts, not below zero; `sli.has` and `sli.line1` read it.

The same facts give the same return (N9): a filer who used to leave those amounts out of the one figure now enters
the lender's total and the part to leave out. Every fixture with interest above zero got `sli.any: true`; the files
that state every input (`classm*`, `mutation`) got the closed answers of the four new children. No expected value
changed. `sli.unqualified_any` holds three short items of one subject (which loans do not count) because they share
one amount; if the owner wants them apart, each needs its own amount.

Who could answer `sli.any` No wrongly: a borrower whose loan was a private or family loan who does not call it a
student loan. The help says to answer Yes when unsure; the children then sort the loan out.

### Education (`f8863.paid`, `f8863.ban`, the twins; bank only)

No model change. The twins' form lines cannot change in this redraft (MAP, "person.yaml and dependent.yaml"), so
every question here keeps its input and only its words and place change. Both twins carry the same words; the person
side begins with the per-person frame and says "this person", which the interview shows as "you" or "your spouse".
The frame makes the two stored prompts differ, so each pair's `interview.prompt` is declared in
`reviews/2025/twins.json` (written by `bank.py`).

Because no child can be added beneath a twin, three questions keep in their **help** a rule only the rare answer
needs (N10 wants a child): `edu_1098t` (when a missing form still counts as a Yes), `edu_inst` (the list of what is
left out of tuition) and `edu_a2025` (what is not tax-free help). The typical answer needs none of it. The children
I would build when the twins may change are under "Not done".

### Home energy (`forms/2025/f5695.yaml`; model change)

See "Steps", step 3, for whether this has landed. Design:

- `f5695.any` (new parent, asked of everyone) replaces `f5695.part1_any` (143 words) and `f5695.part2_any` (141
  words) as the opener. The two old ids stay as derived lines (true when a kind of their part was installed), so
  `s3.line5a`, `s3.line5b` and `s8812.clwb_complete` are not edited.
- Seventeen kinds, each a one-line yes or no beneath the parent. Fifteen are new inputs (`f5695.solar`,
  `solar_water`, `wind`, `geothermal`, `insulation`, `doors`, `windows`, `panel`, `audit`, `heat_pump`,
  `hp_water_heater`, `central_ac`, `water_heater`, `furnace`, `biomass`), each with a gate line `<kind>_if_any`; two
  are existing questions reworded (`line5a`, the battery; `line7a`, the fuel cell, which refuses).
- Each cost is asked only for a kind answered Yes (a gate line `<cost>_if_<kind>` per cost input).
- The conditions of a section are asked only when one of its kinds was installed, one after another: `line17a`,
  then `line17b`, then `line17c`, then `line17e`; `line21a`, then `line21b`, then `b_new_home`. `line25a` and
  `line26a` became the condition beneath the panel and audit kinds.
- A QMID is asked only once a cost of its category is entered (doors, windows, air conditioners and the panel now
  follow the pattern lines 23, 24 and 29 already had).
- `f5695.separate_homes` is asked only on a joint return (it was asked of single filers).
- The carryforward: `f5695.carry` (new) beneath `s3.prior_other_forms` ("does your 2024 return include any separate
  form"), then `f5695.line12`. A filer with no 2025 work but a 2024 carryforward is reached this way, not through
  `f5695.any`. Lines 6b and 11 are read only when something was installed in 2025 (`line6b_if_any`,
  `line11_if_any`), so the carryforward-only filer is not asked about business use, a home under construction or a
  fuel cell (today that filer is asked all three).
- **All seventeen kinds are asked together, directly after the parent** (`f5695.kinds_answered`). A test of `any` is
  decided by its first true operand, so after one Yes the remaining kinds were opened only later, where a cost line
  first read them (seen in the walk: solar, then the conditions, then the other kinds). `kinds_answered` is an `all`
  of one "Yes or No" test per kind: it needs every kind's answer, is true once they are given, and the two part lines
  read the kinds only through it. It is a device to control asking order with the evaluator as it is; the order
  agent may have a better one.

Refusal gates keep their ids (`f5695.business_use`, `construction_later`, `line7a`, `joint_occupancy`,
`separate_homes_joint`, `sec_a_new_home`, `sec_b_new_home`, the five `*_no_qmid`).

**The cost help.** Each of 30 cost questions carried about 224 words of help (7,059 in all). The rules now sit where
the answer that needs them is given: the timing rule and the association share in the parent's help; the home under
construction in `construction_later` and `line17e`/`b_new_home` (existing refusing questions); what to take off the
cost in the prompt itself ("after any rebate or utility subsidy") with one 45-word help shared by the cost
questions. Dropped from the interview's words, kept in the form line's label and source: "costs for more than one
home go on the same line" (Part I).

## Cost and share table (my estimates on the owner's scale, except shares marked gf)

| Question | Asked of | Share answering Yes | Cost of No | Cost of Yes | Children's cost C | g < q·C? |
|---|---|---|---|---|---|---|
| `f5695.any` (new parent) | everyone | 2.5% (gf, `home_energy`) | 1 | 1 | today 5 + 5 (two openers of 143 and 141 words) | 1 < 0.975 × 10 |
| The 17 kinds | 2.5% | one or two each | 1 each | 1 each | today about 30 amounts and 8 screens | flat; three tick-lists |
| `f5695.carry` | those with a separate form in 2024 (est. 25%) | under 1% (judgment) | 2 | 5 | 5 | sits beneath an existing parent |
| `sli.any` (new parent) | everyone | 8% (gf, `student_loan_interest`) | 1 | 1 | 5 (was 244 words, an amount) | 1 < 0.92 × 5 |
| `sli.interest` | 8% | | | 5 (a glance at Form 1098-E) | | |
| `sli.unqualified_any`, `sli.assisted_any` | 8% | under 5% (judgment) | 2 each | 5 | 5 each | guards, not parents: they carry what the long prompt said |
| `f8863.paid` | everyone | 9% (gf, `education`) | 1 (was 2) | 1 | per student about 40 | existing parent, shortened |
| `edu` per person or dependent | 9% | most | 1 | 1 | | existing |
| `edu_inst` | students | | | 5 (Form 1098-T box 1; was 20) | | |

## Candidates for one tick-list

Each member is its own yes or no question; the members of a group have consecutive `seq` numbers in order 230 and
nothing else among them. Not declared in the bank on this branch: the `groups`, `group` and `tick` fields exist only
on `lane/ltick` (its notes, `docs/provisional/lanes/tick.md`, were read after the first commit). What to declare:

| Group id | Heading | Members (`seq`): the words beside each box |
|---|---|---|
| `energy_power` | Did the work include any of these for making or storing energy? | `f5695.solar` (2): Solar panels that make electricity. `solar_water` (3): A solar water heater. `wind` (4): A wind turbine. `geothermal` (5): A geothermal (ground-source) heat pump. `line5a` (6): A battery storing at least 3 kilowatt hours. `line7a` (7): A fuel cell at your main home (a Yes refuses) |
| `energy_shell` | Did the work include any of these? | `f5695.insulation` (8): Insulation or air sealing. `doors` (9): Exterior doors. `windows` (10): Exterior windows or skylights. `panel` (11): A new or upgraded electrical panel, circuits or wiring. `audit` (12): A home energy audit paid for in 2025 |
| `energy_heating` | Did the work include any of this heating, cooling or hot-water equipment? | `f5695.heat_pump` (13): A heat pump, electric or gas (not geothermal). `hp_water_heater` (14): A heat pump water heater. `central_ac` (15): A central air conditioner. `water_heater` (16): A water heater running on natural gas, propane or oil. `furnace` (17): A furnace or hot water boiler running on gas, propane or oil. `biomass` (18): A stove or boiler burning wood, pellets or other plant fuel |

**These three groups will fail the tick lane's build rule 10 as it is written** (inferred from reading the rule; not
built). The rule wants every question a member's Yes opens to follow its group with nothing between. Here the three
groups come first and every detail after the last of them, so the cost of the solar panels (opened by a member of
the first group) has the other two groups and the refusing conditions between. The thing the rule protects does
hold: no cost or condition opens until every kind is answered (`f5695.kinds_answered`), so after the third screen
the next questions are exactly the ones the ticks opened, in `seq` order. Two ways out, for the tick lane or the
stitch to choose:

1. The tick rule accepts consecutive groups whose opened questions all follow the last of them (the runtime check
   "children next, as it happens" should already pass, since a tick opens nothing until the last group is answered).
2. This lane's order changes to group, then that group's conditions and costs, three times over. It is a renumbering
   plus one `…_answered` line per group in place of `kinds_answered`. The price: the refusing questions about
   business use and a shared home would come after the first amounts are typed (against N11), and a filer is asked
   for the solar cost before being asked whether there was also a heat pump.

Education has no tick-list group: its yes or no questions are conditions asked one after another, each opened by the
one before.

## Model changes (inputs)

| Form | Added | Removed (now derived) | Gate lines added |
|---|---|---|---|
| `sli` | `sli.any`, `sli.unqualified_any`, `sli.unqualified`, `sli.assisted_any`, `sli.assisted` | none | `sli.interest_if_any`, `sli.unqualified_any_if_any`, `sli.unqualified_if_some`, `sli.assisted_any_if_any`, `sli.assisted_if_some`; derived `sli.no`, `sli.not_counted`, `sli.qualified` |
| `f5695` | `f5695.any`, the 15 kinds, `f5695.carry` | `f5695.part1_any`, `f5695.part2_any` | one `<kind>_if_any` per kind, `line5a_if_any`, `line7a_if_any`, `carry_if_prior`, one `<cost>_if_<kind>` per cost, `line12_if_carry`, `line25a_if_panel`, `line26a_if_audit`; derived `sec_a_kinds`, `sec_b_kinds`, `sec_a_home`, `sec_a_original`, `sec_b_home`, four `<category>_costs` and `<category>_qmid_missing` |

Other files touched for these inputs: `fixtures/2025/defaults.json`; `interview/2025/stage4.yaml` and `sales.yaml`
(the profiles that list `sli.interest`); `engine/src/generate.ts` (the generated returns state the new answers).

## Review debt

Every changed or new question, gate and line is unreviewed: no transcription, render, class M, screen, false-no or
completeness review was run (NORMS section 5). In particular: the wrong-No analysis of `f5695.any`, `sli.any` and
`s3.prior_other_forms` as the gate of the carryforward is mine alone; the new `sli` arithmetic (interest less two
amounts) is not in any fixture with a nonzero subtraction; the gate lines are not covered by mutation tests.

## Unsure

- `f5695.joint_occupancy` refuses any Part II claim when the home is shared with "someone other than your spouse".
  I kept that meaning and worded it by example (a housemate, a partner, a co-owner living there). Whether a child or
  other dependent who lives in the home is a joint occupant is not something I read in the instructions; the old
  wording did not say either.
- `f8863.ban` says "you"; on a joint return a spouse's earlier disallowance presumably counts too. The form line
  says "your", so I did not add the spouse phrase.
- `f5695.line7a` asks about a fuel cell "at your main home" because the old question refused only that; a fuel cell
  at another home is answered No and gets nothing, as before.
- The help of `edu_line23` says that a student who first went to college in 2022 or later answers No (at most three
  earlier tax years). That is arithmetic on the question, not a sentence of the instructions.

## Engine files touched, and why

- `engine/src/generate.ts` (the generated returns of `interview-rules` and `properties`). The new student loan
  inputs and the Form 5695 kinds are not drawn at random: `sli.any` is set from the amount, and the two answers that
  were drawn for `f5695.part1_any` and `f5695.part2_any` are now drawn under the names `f5695.any` and `f5695.solar`
  (the first two inputs of the form, as the two screens were) and spread over the kinds of each part in
  `buildInputs`. This keeps the random stream, so the generated returns are the ones they were. My first version
  let the new yes or no inputs be drawn; `interview-rules` then failed on a business vehicle question of another
  lane (`scveh.owned` reachable before `scveh.method`, on `generated.6`), which I read as a latent problem the
  changed stream exposed, not as something this lane caused. I did not confirm that reading beyond seeing the
  failure go when the stream was restored (see "Steps" for whether it did).
- `SCREENS` in the same file lists, per kind, the amounts asked only after its Yes.
- `engine/src/umbrella-what-if.ts`: the what-if candidate `f5695.any` is removed (it is now in the model).

Not touched, and now stale: `tools/engines/generate_cases.py` and `tools/engines/compare.py` (the independent
engines' case generator still states `f5695.part1_any`, `f5695.part2_any` and one `sli.interest`);
`research/audits/credits-misc/specs/f5695_no_part2.json`; the description string of the `screens_respected` property
in `engine/src/properties.ts` (it still names "Form 5695 Parts I and II"); `interview/2025/gate_frequencies.yaml`
(its `refs` name the two old screens, which are now derived lines; the shares are unchanged).

## Requests to other lanes

- **Lane 7b / the coordinator (order of `s3.prior_other_forms`).** `f5695.carry` and `f5695.line12` are asked beneath
  `s3.prior_other_forms` ("does your 2024 return include any separate form"), which is not this lane's. I gave them
  order 239. They belong directly after `s3.prior_forms` and `s3.prior_amt`, wherever lane 7b places those (the map
  says 290): please give them the next two `seq` numbers of that block, or tell me the slot. This is MAP Part 5,
  question 9 ("From your 2024 return") done for one form.
- **Fixtures of `s3.prior_other_forms`.** Every fixture case with a 2024 carryforward now states
  `s3.prior_other_forms: true` (the same fact: its 2024 return included Form 5695). That input is not this lane's; I
  changed it only in those cases. If lane 7b renames or regates it, `f5695.carry_if_prior` reads it.
- **Lanes 4b and 2a (the twins' form lines).** Not requested now (MAP: no model change to a twin in this redraft).
  The children I would add are under "Not done".
- **Lane 1 or 4b (a person's age).** `person.edu_born_2007` and `person.edu_born_2002` ask a date of birth for the
  sixth and seventh time (walk note 10). One birth-date input read by all of them would remove five questions for a
  student filing alone.
- **The coordinator, at the merge (coverage rows of `credits.yaml`).** A row that answers `s3.prior_other_forms: true`
  and goes on to completion now meets `f5695.carry`; I added `f5695.carry: false` to the two rows that do
  (`credits.form1116_nothing_carried`, `credits.prior_forms_none`). The other ten rows with that answer end (a refusal
  or an `asks`) before order 239 is reached. If lane 7b moves `s3.prior_forms` and `s3.prior_amt` to order 290, the
  carryforward question at 239 will be asked *before* them, and those ten rows will each need `f5695.carry: false`;
  placing `f5695.carry` after them at 290 (the first request above) avoids that.

## Questions that still arrive away from their topic

Seen in the walks of the rebuilt interview (`draft-walk`, personas 01, 07 and 10):

- `f8863.ban` and `person.edu_born_2007`, `edu_born_2002` (and, for the filers who reach them, `edu_half_support`,
  `edu_fulltime`, `edu_parent`): the student met the opener at question 82 and his own questions at 85 to 97 in one
  run, but these came at 106, 108 and 109. They are waiting on income: `f8863.ban` is read only when the American
  opportunity credit is above zero after the income limit (`f8863.aoc_claimed` reads `f8863.line4`, which reads
  adjusted gross income, `f1040.line11b`), and the birth-date and support questions only when part of the credit
  would be refunded (`f8863.kid_needed`, the same dependence). They are computed gates of the kind MAP 4.8 1(c)
  describes; they cannot come earlier unless income is complete before order 240.
- Between `f8863.paid` (82) and `person.edu` (85) the student was asked two questions of other lanes
  (`person.sav_claimed`, whether someone else can claim him, and `person.tin`), which the education lines read first.
- `person.edu_inst` (the tuition amount, `seq` 90) is asked after the tax-free help, the refunds and `edu_over`
  (`seq` 110 to 140), against its number: the student's walk has the conditions at 87 to 91, help and refunds at 92
  to 95, tuition at 96 and course materials at 97. I read the cause as the refusal on the lines that read the
  tuition (`person.edu_over_refused`, which reads the help and the refunds): on this branch's engine a refusal
  screen is asked before what stands behind it. The order contract (section 1.3) says that under the order agent's
  engine a screen no longer holds back a question that states a `seq`; if so the tuition will come before the help
  after the merge, as numbered. Not tested here.
- `f5695.carry` and `f5695.line12` (order 239) come after the 230 block and not next to `s3.prior_other_forms`,
  which is still at its old order 10 on this branch (see the first request above).
- Home energy itself is asked in one run (questions 81 to 109 for the homeowner), in `seq` order.

## Steps

| # | Step | State |
|---|---|---|
| 1 | Orders and `seq` for every bank entry of the lane; the boilerplate help deleted from all of them | done |
| 2 | `sli.any` and the amount by the paper; the two exclusions as children (model) | done |
| 3 | `f8863.paid` short; the twins reworded by the paper (bank only) | done |
| 4 | Form 5695: one parent, the kinds, costs only for kinds installed, conditions in turn, the carryforward beneath the 2024 forms question (model) | done |
| 5 | Form 5695 cost help (224 words on each of 30 questions) replaced | done |
| 6 | `person.edu_born_*`, `edu_half_support`, `edu_fulltime`, `f8863.ban` reworded (bank only) | done |

Each landed with fixture inputs rewritten, defaults added, coverage rows
(`interview/2025/coverage/education_energy.yaml`, 20 rows) and persona 10 updated. Check results are in the commit
messages and in the report at the end of this file.

## Not done, in rank order

1. **Doors and windows are still asked as four and five amounts** (most expensive, second, third, the rest) because
   the form caps the credit per door and per window. A filer with one door answers three zeros. A parent "Was more
   than one door installed?" (and the same for windows) would save three and four questions for the one-item filer;
   by N3 it pays only if at least a third of door filers have one door (my guess: yes).
2. **"What did the other heat pumps cost together?"** and its five siblings (`line22b`, `23a_ii`, `23b`, `24b`,
   `29b`, `29d`, `29f`) are asked of the typical filer who installed one. A parent over one cheap child does not pay
   (N3); a count ("How many heat pumps?") would, but a Count input cannot be a gate line (formal gates design).
3. **Children beneath the twins** (needs the twins' form lines to change, lanes 4b and 2a together with this one):
   - beneath `edu_1098t` = No: "Did the school not have to send one?" and "Was it asked for after February 2, 2026
     and not received?", in place of the 55-word help;
   - beneath `edu_inst`: "Was any of the tuition paid with a tax-free withdrawal from a 529 plan or a Coverdell
     account?" with the amount, and one for courses in sports, games, hobbies or without credit, in place of the
     list in the help;
   - `person.edu` for a filer with no dependent and no spouse is settled by `f8863.paid` (N8) and should not be asked.
4. **`f8863.ban` is two subjects** (a credit denied so that Form 8862 is needed; a 2-year or 10-year bar). Both
   refuse at one gate, so splitting needs two inputs behind the one gate line.
5. **`f5695.joint_occupancy`** needs the instructions read on who is a joint occupant (see "Unsure").
6. **No persona has a dependent student, a student loan, insulation or doors.** The walks here show a student filing
   alone and a homeowner with solar panels and a heat pump only.
7. The stale files listed under "Engine files touched" (`tools/engines/*`, a research spec, one report string).

## Found and not fixed

- With the generator's random stream changed (my first version of step 2), `interview-rules` reported
  `person[taxpayer].sc[biz_a].scveh[car_1].owned` reachable before `scveh.method` was answered, on `generated.6`. It
  did not appear with the stream as it was. It concerns lane 6b's questions; I did not look further.
- `f5695.separate_homes` was asked of filers who are not married filing jointly (an `all` of the status and the
  answer asked both). Fixed in passing (it is now under a `choose` on the filing status).
- A QMID was asked for doors, windows, air conditioners and the panel even when no cost of that category was entered
  (an `all` again). Fixed in passing.
- A slip of mine to know about: `bank.py` failed on its second run (it tried to remove bank entries already
  removed) and the shell line went on to delete my draft of the coverage rows; I rewrote the rows. `bank.py` now
  skips entries already removed.

## Before and after, from the persona walks

Measured with `docs/provisional/lanes/l8b_work/topic_words.py` on the baseline transcripts
(`docs/provisional/walks/before/`) and on walks of this branch's build (`draft-walk --out /tmp/...`, not committed:
`walks/after/` is left for the merged interview). "This lane's questions" are `f5695.*`, `f8863.*`, `sli.*` and the
`edu*` questions of a person or dependent, as asked of that persona.

| Persona | This lane's questions | Prompt words | Help words | Where in the walk |
|---|---|---|---|---|
| `01_single_w2` (nothing in the topics), before | 4 | 565 | 45 | 25, 74, 85, 86 |
| after | 3 | 57 | 95 | 81, 82, 83 |
| `07_college_student`, before | 20 | 1,311 | 205 | education at 25 and 87 to 110 |
| after | 19 | 378 | 468 | opener 82, his own questions 85 to 97, three more at 106 to 109 |
| `10_homeowner_solar_heat_pump`, before | 35 | 2,213 | 3,950 | home energy at 85 to 117 |
| after | 31 | 453 | 514 | home energy at 81 to 109 |

Whole walks: `01` 86 to 85 questions, 6,777 to 6,269 prompt words, 2,376 to 2,426 help words; `07` 110 to 109, 7,747
to 6,814, 2,681 to 2,944; `10` 117 to 113, 8,425 to 6,665, 6,281 to 2,845. All twelve personas end where they did
(ten complete, two refused at the same gates), with no stale or unanswered answer.

Two things these figures should not hide:

- **The student's help more than doubled (205 to 468 words).** That is the pattern N10 warns of. The cause is named
  above: three twin questions keep a rare-case rule in help because no child can be added beneath a twin in this
  redraft. `edu_inst` alone has 95 words of help. The typical student needs none of it to answer.
- **The homeowner still answers 29 questions**, 17 of them the one-line kinds. On the tick-list page they are three
  screens; as single questions they are 17 answers of No or Yes at a few words each.
- The plain filer's help rose from 45 to 95 words: the old help was the ten-word boilerplate; each of the three
  parents now has about 30 words for the filer who is unsure.

## What was run and seen, and what is inferred

Ran and saw, on the tree of the last commit of this branch:

- `tools/draft_check.sh` (full): green. build OK; fixtures 1854/1854; interview-rules 0 problems; interview-coverage
  0 problems (99 rows, 20 of them new); person wording report current; spouse-wording, check and draft-walk
  self-tests passed; integration 694 invocations; properties; serve 337 checks; twins 0 problems (40 declared
  differences); render check current. An earlier full run of the same content, before the twins' `seq` numbers were
  made distinct, was red at `render_check` only (the rendered forms had not been regenerated; `render` fixed it).
- `draft-walk` over the twelve personas: 0 problems, the same ends as the baseline; the figures in "Before and
  after" and the question numbers in "Questions that still arrive away from their topic" are read from those
  transcripts (personas 01, 07 and 10).
- `reports/2025/person_wording.md` for the framed education questions: read for `person.edu`, `edu_1098t`,
  `edu_inst`, `edu_line24`, `edu_line25` and `edu_half_support`, and searched whole for broken agreement ("was you"),
  which found two questions I then reworded. The other framed questions were not read one by one.

Inferred, not checked:

- That nothing here conflicts with the order agent's engine or the tick lane's build: neither was merged or built.
  The duplicate-`seq` rule and tick rule 10 were read in their notes, not run.
- That each fixture's new answers describe the same facts as its old ones: the rule is in `fixtures.py`, the proof
  is that all 1854 expected results still hold, and I looked at the 53 cases of `fixtures/2025/f5695.json` as a
  list of which kinds each got, not at every file.
- The wrong-No analyses, the shares marked as judgment, and every statement about what a filer would find easy.
- Tax content of the new wording was taken from the form lines' own text (labels, sources, the old prompts and
  help); I did not reread the Form 5695, Form 8863 or Form 1040 instructions.
