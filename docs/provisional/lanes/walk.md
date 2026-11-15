# Lane notes: walk (what a given filer is asked)

Branch `lane/walk`. Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no
model call was made. This lane changes no question, no form and no fixture: it adds a tool, twelve personas and the
baseline walks.

## What is here

| Path | What |
|---|---|
| `engine/src/draft-walk.ts` | the command `draft-walk` and its self-test |
| `interview/2025/personas/<name>.yaml` | twelve personas |
| `docs/provisional/walks/before/` | the baseline: each persona's walk of the interview before the redraft, and `SUMMARY.md`. Never overwritten (the tool refuses) |
| `docs/provisional/walks/after/` | where the tool writes by default; not created yet |
| `tools/draft_check.sh` | runs `draft-walk --self-test` (the self-test only, not the walks) |

Other changes: `closedAnswer` in `engine/src/interview-rules.ts` is now exported (one word); `engine/src/main.ts` has
the command; `interview/README.md` has a section "What a given filer is asked"; `PROJECT_INDEX.md` has a row.

## How to run it

After a build (`npm run build --silent`):

```sh
node engine/dist/main.js draft-walk                      # every persona; transcripts and SUMMARY.md in docs/provisional/walks/after/
node engine/dist/main.js draft-walk --only 03_single_parent_child_care   # one persona (no SUMMARY.md)
node engine/dist/main.js draft-walk --summary            # the table only, printed and written to SUMMARY.md
node engine/dist/main.js draft-walk --out /tmp/walks     # another directory
node engine/dist/main.js draft-walk --self-test
```

It takes about 12 seconds for the twelve. It exits 1 when any persona has a problem, and prints each problem naming
the persona; the transcript is written all the same, with the problems under "PROBLEMS WITH THIS PERSONA" at its head.
To compare before and after: `diff docs/provisional/walks/before/SUMMARY.md docs/provisional/walks/after/SUMMARY.md`,
and for one filer, the section "The whole walk, one line per question" at the foot of each transcript.

What a transcript's figures mean:

- **Topic** is the form the question's input belongs to (a list question's, its list's form). **Topic switch**: the
  topic differs from the question before. **Returns**: a switch to a topic the walk had already left.
- **Prompt words** and **help words** are counted as `interview-words` counts them, on the text as shown to this
  filer. Help is not printed, only its length and first sentence.
- **Answered no, zero or none** counts answers of No, 0 and an empty list, whoever gave them.

Two limits of the topic measure, so the counts are not over-read. The form `person` holds unrelated subjects (age,
blindness, educator expenses, railroad pay, the saver's credit, education, the earned income credit, a self-employed
retirement plan), so a run of `person` questions counts as one topic though it is several; and a form's questions
asked for two people or two entries in turn count as no switch. The count of returns is therefore the more telling
figure: every return is a place where a form's questions were left and come back to.

## How to update a persona after a question is renamed or split

Run the tool. It tells you what to do, in two kinds of line:

- `STALE ANSWER: <id> names no question of the interview`: the question was renamed, split or removed. Give the same
  fact under the new id (or ids), with the value the new question takes, and delete the old line.
- `STALE ANSWER: <id> is never asked on this walk`: the question exists but this filer no longer reaches it (an
  earlier answer no longer opens it, a new parent was answered no by the background, or the walk ended first). If the
  filer should still reach it, look for the unanswered parent in the next kind of line; if not, delete the answer.
- `OPENED AND UNANSWERED: question N, <id> … It was opened by question M, <id> = <value>`: the persona's answers lead
  to a question it does not answer. The walk gave it no, zero, none or the first option, so everything beneath it may
  be wrong. Add the line the message ends with (`"<id>": …`), with the answer this persona's filer gives.

Work from the top: fix the first problem, run again. A closed answer to an unanswered question changes the path, so
later problems often vanish or change once an earlier one is answered (answering a child's age made five other
questions about the child go away). An id is the question's exact id as the answer log has it, with its entries:
`person[taxpayer].w2[acme].box1`, `$w2@person[taxpayer]`, `dependent[child].age`. Amounts are integer cents.

A new plain parent (N2) that the background return is asked and answers no will silently close a topic a persona
used to reach: the persona's answers beneath it then come up as stale ("never asked"), which is the signal to add
`<parent>: true`. A new parent that only this persona meets comes up as opened and unanswered.

Keep the persona the same person. The sentence in `who` is the specification: answers change only to say the same
facts through the new questions. `end` (`complete`, or `{ refused: <gate> }`) must still hold; if it does not after
your change, N9 is at stake (the same facts must end where they ended), so stop and look before editing `end`.

The answers are synthetic and none is copied from a fixture. `fixtures/2025/returns.json` was read for the shape of
an answer (the ids, cents, the roster keys); its eleven cases are each one single person with no dependent (the one I read whole has wages, interest,
dividends, a sale and itemized deductions), so there is no couple, child or head of household to draw on, and the
personas were written by walking: answering each opened question as the person in `who` would, until nothing was unanswered. Where a truthful answer could plausibly
be zero (state income tax paid, for a filer in a state without one), the persona leaves the background's zero.

## What the baseline walks show (observations; nothing was changed)

Figures are from `docs/provisional/walks/before/`. Question numbers are those of the named persona's walk.

| Persona | Questions | Prompt words | Help words | No, zero, none | Switches | Returns | End |
|---|---|---|---|---|---|---|---|
| `01_single_w2` | 86 | 6,777 | 2,376 | 78 | 43 | 12 | complete |
| `02_couple_children_mortgage` | 133 | 10,168 | 3,286 | 95 | 50 | 17 | complete |
| `03_single_parent_child_care` | 121 | 10,100 | 2,969 | 93 | 58 | 24 | complete |
| `04_retired_couple` | 122 | 9,030 | 2,970 | 105 | 50 | 19 | complete |
| `05_self_employed` | 133 | 9,905 | 2,360 | 108 | 49 | 16 | complete |
| `06_investor_loss_carryover` | 114 | 9,298 | 2,787 | 86 | 49 | 17 | complete |
| `07_college_student` | 110 | 7,747 | 2,681 | 88 | 49 | 17 | complete |
| `08_hsa_marketplace` | 150 | 10,384 | 4,105 | 121 | 48 | 16 | complete |
| `09_tips_overtime` | 95 | 7,363 | 2,466 | 77 | 49 | 16 | complete |
| `10_homeowner_solar_heat_pump` | 117 | 8,425 | 6,281 | 102 | 43 | 12 | complete |
| `11_refused_rental` | 4 | 490 | 231 | 1 | 2 | 0 | refused at `scope.schedule1` |
| `12_refused_nonresident` | 5 | 678 | 281 | 2 | 2 | 0 | refused at `scope.other_income` |

### The floor everyone pays

1. **A person with one W-2 and nothing else answers 86 questions and reads 6,777 prompt words; 78 of the 86 answers
   are no, zero or none.** The eight that are not: who the return is for, the status, the employer list and five W-2
   boxes. (A filer with no income at all, the background return, is asked 82.)
2. **Ten prompts are nearly half of that reading** (3,192 of 6,777 words), each answered no or zero by this filer:
   `sb.foreign_any` 827, `sa.line1` 429, `scope.schedule1` 293, `sa.gifts` 292, `sli.interest` 244, `sa.line5a` 237,
   `sa.line5b` 232, `household.married` 217, `div.any` 217, `f4952.has_interest` 204.
3. **The three scope questions come third to fifth for everyone** (`scope.other_line16`, `scope.schedule1`,
   `scope.other_income`: 663 words together), before the filer has said anything about their year.
4. **The order after the opening is close to alphabetical by question id**, not a life: `div`, `f1040`, `f4952`,
   `f8863`, `f8959`, `ftc`, `person…`, `refund`, `s1`, `s1a`, `s2`, `s3`, `sa`, `sb`, `sd`, `$sales`, `sli`, `ssb`,
   `$sc`, then the questions that become reachable late. Alimony, gambling, Alaska dividends, jury pay, an electric
   car, farmland and kerosene all come before the filer is asked about social security or a business.

### Refusals

5. **Both refused filers are told early in count (question 4 and 5) but only by finding their item inside a
   catch-all.** Rental property is one bullet in the middle of `scope.schedule1` (293 words, which opens "Any income or adjustment
   requiring Schedule 1 other than the ones this tool asks about separately");
   nonresident alien status leads `scope.other_income`, whose first line is about "other income or return treatment
   outside the kinds listed below".
6. **The wording shown at the refusal does not name what the filer said.** Rental: one long sentence listing what the
   tool *does* compute on Schedule 1, with no mention of rental. Nonresident: "Form 1040 additional income/return
   forms. Prepare the required unsupported income or return treatment."

### Questions that settle what was already said (N8)

7. **A couple who chose "Me and my husband or wife, together on one return" is then asked `household.married`** (217
   words; question 31 for `02`, 9 for `04`). Answering it no stops the return as conflicting answers
   (`household.filing_status_conflict`). The first drafts of both couple personas hit this.
8. **A filer who chose "None of these: I was not married (single)" is asked `household.married` and
   `household.spouse_died_2025`** (questions 9 and 10 of `01`).
9. **The head of household filer answers `household.unmarried` (318 words) yes at question 20 and is asked
   `household.married` at question 26.**
10. **One person's age is asked in pieces, as separate yes/no questions at separate places.** The student (`07`) is
    asked `person.under16` (11), `person.age65` (28), `person.sav_born` (born before January 2, 2008; 108),
    `person.edu_born_2007` (109), `person.edu_born_2002` (110), `person.born_after_1960` (102) and
    `person.born_before_2001` (103): seven questions for one date of birth. The HSA asks `f8889.age55` as well.

### Topics that are split or interleaved

11. **The W-2 is asked in two sittings.** Boxes 1 and 2 follow the employer list (questions 15 and 16 of `01`); boxes
    4, 5 and 6 come fifteen questions later (31 to 33), after interest, the HSA, dividends, other withholding,
    investment interest, education, the foreign tax credit, and the person's age, educator expenses and railroad pay.
    For a couple the two W-2s are interleaved with each person's age, educator and railroad questions (`02`, 53 to 64).
12. **Dividends are asked in six places across five forms.** The investor (`06`): `div.any` (19),
    `sb.ordinary_dividends` and `f1040.line3a` (70, 71), `sd.distributions` (75), the `div.box…` amounts (102 to 106),
    `qbi.dividends` (107). The retired couple (`04`) is asked nine `div.box…` amounts in no printed order (box 2c, 13,
    10, 2e, 2f, 3, 9, 2b, 2d; 103 to 111) and `div.box12` eight questions after them (119).
13. **Sales are asked question by question across the sales, not sale by sale** (`06`, 78 to 95): the box of sale A,
    the box of sale B, special A, special B, code A, code B, route A, route B; then the six questions of the capital
    loss carryover worksheet (`clcw.*`); then proceeds and basis of A, of B. `sales.box` is 689 words and is shown
    once per sale (1,378 words for two sales). `sd.carryover` (74) and its figures (86 to 91) are twelve questions
    apart, with the sales between.
14. **Schedule C's amounts come in id order, so gross receipts are asked last.** `05`: the home office (76 to 78),
    then expenses `line10`, `line11`, `line14` … `line2`, `line20b` … `line8`, the three meals questions, then the
    vehicle (112 to 115) in the middle of the business's yes/no screens, and `sc.line1`, gross receipts, at 121. The
    cost of goods sold lines (inventory, purchases, labor, materials, other costs: six amounts) are asked of a
    designer with no inventory.
15. **A dependent's questions are in four places.** `03`: the list and eleven questions per child (9 to 19), then
    `absence_no_return` (25), `work_ssn` (74), `kidnapped` (105), `dc_paid` (113, between two questions about the
    care provider), `us_half` and `eic_ssn` (117, 118). Each young child costs 1,094 prompt words in the first
    sitting alone; the age is the fifth question, after whether the child is married (62 words) and the divorced
    parents rule (107), and a 3-year-old's parent reads `dependent.relationship` (297) and `dependent.self_support`
    (240).
16. **Child care is asked in three sittings** (`03`): `f2441.care` (98), then `s8812.puerto_rico`, then three more
    `f2441` questions (100 to 102), then combat pay, the saver's credit, kidnapping, the QBI questions and
    `household.credit_disallowed`, then the provider (109 to 114) with `dependent.dc_paid` (529 words) inside it.
17. **Education** (`07`): `f8863.paid` is question 25; the student's own questions begin at 87, sixty-two questions
    later, and are interleaved with the saver's credit (`sav_claimed`, `sav_born`), the earned income credit
    (`eic_ssn`, `eic.died_2025`, two birth questions) and `f1040.tax_exempt_interest`. The amounts paid (`edu_inst`,
    `edu_mat`; 105, 106) come after the questions about the fourth year, a felony conviction and the school's EIN.
18. **Tips and overtime** (`09`): the W-2 is at 14; `s1a.overtime` and `s1a.tips` are at 77 and 79 with
    `person.work_ssn` between them; the two employer lists at 84 and 85, after section 179, dependent care, the
    saver's credit and QBI; then the entries. The server names the same employer three times (`$w2`, `$otjob`,
    `$tipjob`), and `tipjob.amount` asks for W-2 box 7, which the W-2's own questions did not ask her.
19. **The Marketplace form** (`08`): listed at question 6; its first questions at 48 to 52 (`f8962.alloc`,
    `f8962.other` 357 words, `premium_adjust`, the form's `void`, the poverty table); then `f1040.tax_exempt_interest` (113) and
    the rest of the form at 114 to 150, the end of the walk. The 36 month amounts are asked column by column with the months in id order (April,
    August, December, February …), 61, 109 and 22 words each: 2,304 words for a form with four months on it.
    By contrast the HSA block (18 to 39) is asked in one sitting, in a sensible order; it is the one topic in these
    walks that reads as a topic.
20. **The pension** (`04`): the list at 7; `account`, `special` (411 words), `code` at 11 to 13; then each spouse's
    `person.under16` and `s3.adoption_any` (asked of a couple aged 71 and 69); then the rest of the pension (16 to
    20). Social security, this couple's main income, is question 94. Interest: the payer at 23, its amount at 35.
21. **Home energy** (`10`): the two openers are the last two questions of the plain filer's walk (143 and 141 words). The
    heat pump owner, after `f5695.line21a` yes, is asked seven amounts for air conditioners, water heaters, furnaces
    and boilers and the panelboard question before the heat pump's own line (`line29a`), then five more amounts. Her
    help is 6,281 words against 2,376 for the plain filer: the Form 5695 amount questions each carry long help.

### Questions that arrive for no reason the filer can see

22. Asked of the wage earner with nothing else (`01`): `f4952.line4g` (83 words, an election about investment income)
    directly after answering no to having investment interest; `f8959.unsupported` (church employee income); `s179.line10`
    (77 words, a section 179 carryover, asked after the business list was answered none); `qbi.unsupported` and `qbi.carryforward`; `person.rrta` (railroad); `person.x_other`
    (136 words); `sa.dependent`; the five Schedule A amounts (`sa.line8a`, `sa.line1`, `sa.line5a`, `sa.line5b`,
    `sa.line5c`: 970 words), which the tool needs to compare itemizing with the standard deduction but which follow
    `sa.elect_itemize` ("Elect to itemize even if the standard deduction is larger?") answered no, with nothing telling
    the filer why they are still asked.
23. `f1040.tax_exempt_interest` (52 words) appears near the end for the Marketplace filer (113), the single parent
    (120), the student (100) and the retired couple (120), far from interest, wherever a credit needs a modified AGI.
24. `person.eic_ssn` (78 words on what makes a social security number valid for the earned income credit) is asked
    of the low earners (`03`, `07`) and of the filer with no income, as one of the last questions; `s8812.puerto_rico`
    and `household.credit_disallowed` reach the parents the same way, apart from each other and from the children.
25. `person.work_ssn` and `person.tin` are asked where a credit or deduction needs them: between the Schedule A
    questions for the couple (94 to 97), between overtime and tips for the server (78), with age 65 for the retired
    couple (38, 43).

### About the measure itself

26. A persona's count moves when a truthful answer replaces the background's. Giving the single parent and the
    student `person.eic_ssn: true` added two and four questions. The baseline has the truthful answer wherever I saw
    the question was one a real filer of that kind would answer otherwise; a persona still takes the background's
    answer to every question it does not name, and that answer is "no, zero, none", which for a few questions
    (state income tax paid, medical expenses) is a simplification of the person rather than a fact about them.

## What I ran and saw, and what I infer

Ran and saw: the build; `draft-walk --self-test` (passes); `draft-walk` over the twelve personas (0 problems; ten
complete, two refused at the gates named); `tools/draft_check.sh` (result in the commit message and the lane report);
the one-line listings of all twelve baseline walks, from which every question number above is read; the full
transcript of `01` at its first five and last questions, and the refusal sections of `11` and `12`.

Inferred, not checked: that the near-alphabetical order (4) is the bank's `order` number followed by key order (the
README says so; I did not trace `askOrder` against these walks question by question); that the late arrival of a
form's remaining questions (11, 15, 19) is the reachability effect the README describes under "Blocks" (I did not
confirm it for any one question); that the personas' amounts give the tax results a preparer would expect (no
persona's computed values were inspected: the tool reads the path, not the return); and observation 22's reading of
*why* a question is asked. I did not open the help texts, so 21's "long help" is the word count only.

## Not done

- No persona with two W-2s for one person, a nonworking spouse, an older dependent, an IRA, unemployment, student
  loan interest or a state refund. These are common and each would exercise a part the twelve do not.
- The transcript does not print the wording a couple is shown for the spouse's entry separately; it prints each
  question as shown when asked, which includes it.
- `draft-walk` is not in `tools/self_tests.py` or `check-all`, by the brief (the self-test is in `draft_check.sh`).
