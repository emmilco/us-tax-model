# Interview redesign: intent

Decided by the owner on 2026-11-11, after walking the first screens of his own 2025 return in the web UI
(docs/2026-11-11_owner_walkthrough_notes.md). This document states what the redesign is for and the decisions that
bound it. It is not a plan; the plan is made from it.

## What the walk showed

The interview is written from the forms outward: it asks the forms' questions in the forms' vocabulary, protects its
scope with catch-all questions that list what the tool cannot do, and orders its screens by an internal number. The
five notes of the walk are symptoms of that one cause: a question whose answer an earlier answer had fixed, three
catch-alls no ordinary person can answer, a question that arrives for no reason a reader can see, and a 232-word
sentence.

## Intent

A person who is not a tax person sits down with the year's paperwork and gets a correct return, or is told early and
clearly that this tool cannot prepare theirs. They are never asked something they cannot answer, never asked something
an earlier answer settled, and never made to read tax law in order to say no.

The interview is to be turned around: it starts from what a person knows and works toward what the forms need, without
weakening what the tool guarantees about a completed return.

## Decisions

1. **The filer.** The interview is written for a person who knows their own life and has their documents, and has no
   tax vocabulary. They know whether they are married, have children, own a home, changed jobs or sold stock. They do
   not know what Schedule 3 is or which credits exist.

2. **Answerable at the top, airtight underneath.** Where a plain question and an airtight one conflict, the top
   question is plain and the precision lives beneath it. Every situation a catch-all covers today must be reachable
   through some plain question. A situation that no plain question leads to is not dropped: it stays as its own
   separate question, however rare.

3. **Measures of success.** Three, reported together:
   - the words a typical filer has to read to finish (reports/2025/interview_words.md);
   - a coverage check: every situation the design's coverage tables name is written as a set of answers with the end
     it must reach (a question asked, a refusal, values recorded), and a check with no model walks the built question
     tree and confirms each one. The structure of the tree is what must be right, and this walks it in the abstract;
   - the owner's own walk.
   The number of screens is not the measure. A reader test by a model (decision 6) was tried and dropped.

4. **Reach into the model.** New gating questions and regrouped catch-alls are in scope, with their fixtures and
   reviews. Removing inputs the model does not need a filer to supply (such as `person.role`, which the roster choice
   already fixes) is potentially in scope, to be decided case by case.

5. **A slice first.** The redesign is proven on a slice, taken all the way to its measures and the owner's walk, before the rest of the
   interview is touched. The slice: the opening (who is on the return, the filing status, the role question); one
   scope screen taken apart completely, `scope.credits`; and one ordinary topic end to end, health savings accounts
   (Form 8889: a roster, about 18 questions, a catch-all, per-person framing). The other three scope screens and the
   order of the interview as a whole are not in the slice.

6. **The reader test: tried, and dropped as a measure (owner, 2026-11-11).** Invented personas, each a life and the
   documents held, with the right outcome known; a model played each persona and answered one question at a time, or
   said it could not tell. On today's interview it answered 96 percent of 510 questions correctly and none wrongly:
   it passed the interview the owner found unanswerable, because it knows tax vocabulary whatever the persona says and
   does not feel length, order or repetition. The owner's judgment: pretending to be a poor reader is not a realistic
   task for a model, nor a meaningful signal. Its code, personas and results are not on main; they stay on the branch
   `worktree-agent-aba087062001bfbeb`. The coverage check of decision 3 takes its place.

7. **On hold until the slice is judged:** the remaining interview-rules rewrites (T-276) and the umbrella gates U3,
   U4 and U1 (T-265), since restructuring the catch-alls changes the gates they touch.

## Decisions on the design of the first slice

The slice is designed in docs/2026-11-11_interview_redesign_slice_design.md. The rules that design marks as unverified
were checked against the credit instructions archived afterwards; what the sources say, and where the design is not
right, is in docs/2026-11-11_interview_redesign_sources_check.md. The owner decided, on 2026-11-11:

1. **One answer may record several inputs, narrowly.** The "who is this return for" choice also records each entry's
   role and, for a couple, the joint filing status. The rule that the interview sets no input is restated to allow
   this for the inputs of the entries a roster choice creates, plus an allow-list of one (the filing status). The role
   is not derived inside the model.
2. **Adoption and a mortgage credit certificate refuse on the fact,** not on the wish to claim the credit.
3. **`s3.line12` and `s3.line14` refuse** instead of asking the filer to type a total from a form the tool does not
   prepare.
4. **The credit instructions that are not archived are archived first** (Forms 3800, 8396, 8801, 8834, 8839, 8859,
   8911, 8912, 8936, Schedule R and Form 5498-SA), before the precise credit questions are written.

The design's other five open questions stand at its recommendations unless the owner objects on reading it: marriage
is not moved ahead of the filing status in this slice; refusal questions are asked at their topic; none of the three
scope changes the sources support (a surviving spouse's inherited HSA, the elderly or disabled credit screened from
income, a dormant Archer MSA) is made in this slice; the per-person frame becomes "About you" or "About your spouse"
on a joint return and nothing on a one-person return, applied when shown; and a health FSA question is added after the
coverage check.

## Readings ruled out

- A polish pass that rewords the worst questions and keeps the structure. The objection to the catch-alls is to their
  structure, not their wording.
- An interview written for the owner. The reader is someone who is not a tax-literate filer.
- Shorter as the goal. The goal is answerable; shorter reading follows for most filers, and some will see more
  screens.

## Tensions the plan must handle

- **A plain question is easier to answer wrongly.** A filer who does not recognize their situation under a plain word
  says No. Decision 2 answers this structurally (nothing is dropped), and the coverage check verifies it for the situations the design names. When a review
  finds a way to answer a top question No wrongly, the remedy is a child question or a separate question, not a longer
  top question: the umbrella question `sb.foreign_any` grew from a short question to about 640 words by the other
  remedy.
- **The form's words.** The reviews check a question's wording against the instructions. Under decision 2 the top
  questions are deliberately not in the form's words; the source-faithful wording belongs to the questions beneath
  them. What each review checks at each level has to be restated.
- **Model changes cost evidence.** Each new question or gate brings fixtures, mutation coverage and reviews.

## The owner's idea (Idea A), in his words

"Consider the following question: Do you have an orange cat, or a cat which was once trampled by lions, or a dog, or a
dog recently deceased, or a dog which was taken into custody for aggressive behavior, or a cat pregnant with hope for
the future? We can ask a person 'do you have any pets?' and their 'no' will spare them considering all of those
different cats and dogs. We can replace that question with:

- Do you have any pets?
  - Do you own a cat?
    - Was your cat trampled by lions, or is it pregnant with hope for the future, or is it orange?
  - Do you have a dog?"

## Working principles drawn from two paper examples

Drawn by the coordinator from working `f8889.unsupported` and `scope.credits` through Idea A on paper; the owner has
seen them and decided they stay as the redesign's working principles. The examples themselves were read from the question text and the printed
Schedule 3 and were not checked against the instructions line by line.

1. Ask about what the person has, never about "anything other than". `scope.credits` lists the credits the tool
   handles and asks about the unnamed rest; what lies outside is a closed list (Schedule 3 prints 14 named credits and
   two "other" lines) that can be asked about positively, as facts of a life: a vehicle bought, a child adopted.
2. A top question names kinds in everyday words; the precise conditions live in its children. The ten items of
   `f8889.unsupported` fall into five plain kinds (a transfer from an IRA; an Archer MSA; a death or an inherited
   account; a correction of a mistake or a loan; something left over from an earlier year).
3. Put each piece where its topic comes up. Four catch-alls stand at the very start of the interview; adoption belongs
   with the dependents questions and business credits with the business questions.
4. Do not ask what an earlier answer settles.
