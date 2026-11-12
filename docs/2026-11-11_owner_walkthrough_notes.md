# Owner's walk of the interview: notes

The owner is walking his own 2025 return in the web UI (T-236), on main at `b88e5ce4`, profile `ny`. Each note
records what he saw and said, the question's id, and the facts checked against the built data at the time. Notes are
observations, not decisions: no fix is proposed here. The plan is made from this file after the walk.

Question numbers are the order in which the interview asked them on his return.

## Note 1. Questions 1 to 3: the third is already answered by the first

- **Questions:** 1 `$person`, 2 `f1040.status`, 3 `person.role` (asked once for each person on the return).
- **What the owner saw:** question 1 asks whether he is filing for himself or jointly; question 2 asks his filing
  status; question 3 asks whether the entry is his own or his spouse's.
- **In his words:** "isn't question 3 answerable from both previous question's answers?"
- **Checked:**
  - `$person` reads "Who is on this return: just you, or you and your spouse on a joint return?" and offers two fixed
    choices. "Just me" creates one entry keyed `taxpayer` and labelled "You"; "Me and my spouse (joint return)"
    creates two, keyed `taxpayer` and `spouse`, labelled "You" and "Your spouse".
  - `person.role` reads "For this person (you, or your spouse on a joint return) - Whose entry is this, yours (the
    taxpayer) or your spouse's?". It is asked of an entry the interview has just created and labelled, so its answer
    is fixed by question 1 alone. On a joint return it is asked twice.
  - `person.role` is an input in the model, read by 33 lines (34 references; an earlier count of 35 here was a text
    match, corrected from the slice design); a roster entry's key carries no meaning to the model.
  - Questions 1 and 2 overlap: "Me and my spouse (joint return)" already says the status is married filing jointly,
    and "Just me" says it is not; the status is asked anyway, and the two can be answered inconsistently.
  - `f1040.status` is not worded as a question. Its prompt is "Form 1040, Filing Status checkboxes", it has no help
    text, and its options have no labels, so the page shows the model's codes (`mfj`, `mfs`, `hoh`, `qss`). The
    question review left the three enum questions out, so this wording has not been reviewed.

## Note 2. Question 4: not answerable by a normal person

- **Question:** 4 `scope.credits`.
- **What the owner saw:** "Do you want to claim any credit other than the following, or do you have any other amount
  for Schedule 3 Part I (for example a Form 8978 adjustment)?", followed by a list of 11 items, some very obscure.
- **In his words:** "this is not answerable by a normal person."
- **Checked:**
  - The 11 items are the credits the tool figures: the foreign tax credit claimed without Form 1116; the excess
    social security credit; the child tax credit; the credit for other dependents; the additional child tax credit;
    the earned income credit; the credit for child and dependent care expenses (Form 2441); the retirement savings
    contributions credit (Form 8880); the residential energy credits (Form 5695); the net premium tax credit figured
    on Form 8962 (Schedule 3 line 9); the education credits figured on Form 8863.
  - The question asks about everything NOT on that list: the filer must know what other credits exist to answer it.
  - Its help reads: "Yes if you want any credit not in the question's list of credits this tool figures, or have any
    other amount for Schedule 3 Part I; Yes refuses the return."
  - A Yes refuses the return. The answer is read by the scope line `scope.ready` and by seven other lines, each as a
    refusal (Form 1040 line 30, Schedule 3 line 8, two credit limit worksheet lines of Schedule 8812, the Form 8863
    worksheet line 5, and two Form 5695 worksheet lines).
  - It is one of four scope screens asked at the start, with `scope.other_income`, `scope.other_line16` and
    `scope.schedule1`.

## Note 3. Question 5: similarly unanswerable

- **Question:** 5 `scope.other_income`.
- **In his words:** "question 5 is similarly unanswerable".
- **Checked:**
  - It reads "Any nonresident alien status, or other income or return treatment outside the kinds listed below?" and
    runs to 204 words: a list of six kinds it is NOT about (wages, interest, dividends, supported securities sales,
    Form 1099-R distributions, social security benefits), then nonresident alien status, then nine named examples of
    "other income or return treatment" (among them Medicaid waiver payments, passive activity income or loss, Form
    8915-F disaster distributions, a reservist repayment on Form 8606 line 1, and being a chapter 11 debtor).
  - Like question 4 it asks about everything outside a list: the nine examples are introduced by "including", so they
    do not bound the question, and a filer must know what other income or treatment exists to answer No with
    confidence.
  - It joins unrelated matters in one yes/no: residency status, kinds of income, a bankruptcy case.
  - A Yes refuses the return; the help ends "Yes refuses the return". Four lines read the answer.
  - The two scope screens that follow have the same shape: `scope.other_line16` (196 words: "Any additional Form
    1040 line 16 tax or filing, including any of the following?") and `scope.schedule1` (322 words: "Any income or
    adjustment requiring Schedule 1 other than the ones this tool asks about separately, including any of the
    following?", read by 11 lines). Together the four scope screens are 851 words (129, 204, 196 and 322) before
    the first question about the filer's own figures.

## Note 4. Question 8: suddenly about Form 1095-A

- **Question:** 8 `$f1095a` (the roster of Forms 1095-A).
- **In his words:** "why is question 8 suddenly about form 1095-A???"
- **Checked:**
  - It reads "List each Form 1095-A (Health Insurance Marketplace Statement) you received, one entry per form. Do not
    list a VOID form, or the form a CORRECTED one replaces, or a form for a catastrophic or stand-alone dental plan.
    Leave the list empty if you received none."
  - Nothing topical puts it here. Questions are asked by a hand-assigned `order` number in the bank
    (`interview/2025/questions.yaml`), and within one number by the input's id in alphabetical order
    (`interview/README.md`: "asked in bank order, then by key"). Order 0 holds the seven questions already met: the
    roster of persons, the filing status, the role, and the four scope screens. Order 1 holds six rosters:
    `$carloan`, `$f1095a`, `$otjob`, `$retirement`, `$sales`, `$tipjob`. `$carloan` did not come first for him, which fits it being asked only
    after a Yes to the car loan interest deduction (inferred from the Schedule 1-A gate; not traced in the engine), so
    the first of the six he met is the next in the alphabet, `$f1095a`.
  - So the eighth question is the Marketplace statement because its id sorts first among the rosters given order 1,
    not because the interview has reached health coverage. The wage roster `$w2` has order 5, interest `$interest`
    order 8, dependents `$dependent` order 2: the first thing asked about the filer's own figures is not wages.
  - The order values are sparse and reused: 109 questions share order 2, 144 share order 10 and 100 share order 12,
    so within those groups the sequence is alphabetical by id.
  - Its help is the boilerplate "Married filing separately and unsupported items are refused with citations.", which
    says nothing about the question. 213 questions carry that same help text (T-266).
  - Phase 3 measured that reordering cannot shorten the interview (reports/2025/interview_length.md), and T-251, an
    information-based order, was closed on that measurement. That measurement was about the number of questions, not
    about whether the sequence makes sense to a reader.

## Note 5. The HSA "any of these" question: unreadable

- **Question:** `f8889.unsupported` (asked for each person with a Form 8889; the owner did not give its number).
- **What the owner saw:** one sentence beginning "For this person (you, or your spouse on a joint return) - Any of
  these: a qualified HSA funding distribution from an IRA in 2025; contributions by you or your employer to an
  Archer MSA for 2025 (Form 8853), or, if you or your spouse had family coverage under an HDHP at any time during
  2025, any contribution by anyone to your spouse's Archer MSA; excess HSA contributions from an earlier year that
  remain in your HSA; ..." and ending "... since the last month of a decedent's tax year is the month of death, not
  December?"
- **In his word:** "Unreadable".
- **Checked:**
  - It is one sentence of 232 words with ten items separated by nine semicolons and no line break. It is the longest
    prompt in the interview that is a single paragraph; the next are `sb.line8` (218 words), `f8889.medical` (179),
    `sc.meals_100` and `carloan.requirements` (174 each).
  - Other long questions use the interview's structured text (a lead sentence, then a bulleted list), as the scope
    screens do; this one does not.
  - 116 of the 626 questions have a prompt over 100 words, and 218 over 60.
  - A Yes refuses: the answer is read by `f8889.line13` and `f8889.line16`, each as a refusal ("Form 8889 Part III,
    Form 8853, a Form 8889 for a p..."). It is the form's catch-all for the situations the tool does not prepare.
  - Its help adds only what the question is not about: "HSA distributions that were not used for qualified medical
    expenses are not among these; Form 8889 Part II asks about them separately."
  - The question review has never looked at it: `reports/2025/question_currency.md` lists it as "never reviewed".
    The first full pass covered questions no review had judged, and skipped those a screen or gate review had
    judged; this is one of the questions listed as due.
  - It mixes the per-person frame ("For this person (you, or your spouse on a joint return)") with "you or your
    spouse", "your spouse's Archer MSA" and "this person died in 2025" inside the sentence, so who "you" is changes
    within it.

## Ideas from the owner, for the plan

These are the owner's proposals, recorded as he gave them. They are inputs to the plan, not decisions.

### Idea A. Replace a catch-all with a short question and narrower ones beneath it

In his words: "Consider the following question: Do you have an orange cat, or a cat which was once trampled by lions,
or a dog, or a dog recently deceased, or a dog which was taken into custody for aggressive behavior, or a cat pregnant
with hope for the future? We can ask a person 'do you have any pets?' and their 'no' will spare them considering all of
those different cats and dogs. We can replace that question with:

- Do you have any pets?
  - Do you own a cat?
    - Was your cat trampled by lions, or is it pregnant with hope for the future, or is it orange?
  - Do you have a dog?"

Given after notes 2, 3 and 5, each of which is a catch-all question whose Yes refuses the return and which lists
everything the tool does not handle.

## Corrections from the slice design

The design of the first slice (docs/2026-11-11_interview_redesign_slice_design.md) checked these notes and the intent
document's paper examples against the form data and the archived instructions. Where it differs, it is the better
source:

- `person.role` has 33 reading lines, and `scope.credits` seven besides `scope.ready` (corrected above).
- Schedule 3 Part I has twelve named credits beyond lines 1 to 5, one reserved line, and line 6z, which the 2025
  instructions say to leave blank: the list of other credits is closed, and shorter than "14 named credits and two
  other lines".
- Four of the situations `scope.credits` covers are already refused by other questions (Form 1116, a business's
  employment credits, Form 2439, a Form 8978 amount).
- `scope.credits`, read literally, refuses a filer with a fuel credit or another Schedule 3 Part II credit, and two
  later questions (`s3.line12`, `s3.line14`) then ask every filer to type those amounts in.
- The "five plain kinds" proposed for the HSA catch-all do not hold: two of them join things a filer would not put
  together. The design uses nine short questions.
- About half the credits the tool does not handle are not facts of a life: five are carryovers that only last year's
  return shows, two are papers received, four are arrangements a person has only if told.
- The HSA catch-all overlaps other questions (prior-year excess is asked of every person by `person.x_other`; the IRA
  transfer is asked again at the Form 1099-R), refuses a surviving spouse's inherited HSA that the instructions treat
  as the spouse's own, and misses money paid out of an Archer MSA.
- The HSA questions are not asked together: on a walked return they came in four places, separated by 27 unrelated
  questions.
- A death in 2025 is asked in six places, each for one form.
