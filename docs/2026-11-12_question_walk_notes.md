# Question walk with the owner, 2026-11-12: toward a theory of how to restructure the interview

The owner reads the interview's questions one at a time, in asking order, on the vetting page (`/vet`), and says what
is wrong with each. This file keeps his words and the theory as it develops. Nothing is rewritten from it until he says
the theory is ready. It follows docs/2026-11-11_owner_walkthrough_notes.md (his first walk) and
docs/2026-11-11_interview_redesign_intent.md (the intent and decisions of the first slice).

A rule below is a **candidate** until it has held on several questions; each says how many it rests on.

## The theory so far

**Rule 1 (candidate; rests on question 3; the owner agreed it holds there).** Each item of a catch-all goes where its
subject already lives, and only an item with no home becomes a question of its own. A catch-all is therefore not
redesigned alone: taking it apart moves its items into other topics.

- A fact about the person goes with who the return is for.
- An item about a paper the filer already enters goes beneath that paper's questions.
- An item about a life event goes beneath the question on that event.
- An item with no home gets its own plain question, with a gloss where the term needs one.

Why not one question per item: the credits part of the first slice was first built that way (14 flat questions asked of
everyone) and the owner rejected the count.

**Symptom noted.** A question that opens by listing what it is not about has no subject of its own.

## The questions

### 3. `scope.other_income` (188 words, Yes or No)

"Any nonresident alien status, or other income or return treatment outside the kinds listed below?", then a list of
kinds it is not about, nonresident alien status, and nine items of "other income or return treatment".

The owner:

> This question groups together a bunch of unrelated concepts that do not belong together:
> 1. non-resident alien status
> 2. hodgepodge of unsupported income varieties
>
> it would be better to ask each of these individually, e.g.
>
> "Did you receive adoption benefits?"
> "Did you receive income or loss from a passive activity?" (this one needs a gloss)
>
> etc.
>
> This question by itself covers such a massive and detailed array of stuff

Where each item could live, under rule 1 (the owner: "Yes that holds"):

| Item | Where it could live |
|---|---|
| Nonresident alien status; chapter 11 debtor | Facts about the person, asked with who the return is for |
| Wages or tips not on a Form W-2; Medicaid waiver payments; dependent care benefits beyond box 10 | Beneath the Form W-2 questions |
| Adoption benefits | Beneath the adoption question (`s3.adoption_any`) |
| Disaster recovery distribution; reservist IRA repayment | Beneath the retirement distribution and IRA questions |
| Passive activity income or loss; other earned income | No home: each its own plain question, with a gloss |

## The frame: the interview as a graph with costs on its answers

The owner, 2026-11-12, after the first questions of the walk:

> We need to think about the interview as a directed graph. Each question is a node. Each way of answering is an edge.
> Every edge has a cost, which represents how mentally taxing it is to correctly answer that way.
>
> Our goal is to minimize the average person's cost of traversing the graph. We do this by structuring the graph so
> that people prefer questions that are easy to answer and a graph with a larger number of cheap edges than a smaller
> graph with much more expensive edges.
>
> The typical answer should always be the least cognitively difficult to produce for any given question. And questions
> should be layered.

His three examples, with the costs he gave:

| Question | Yes | No | Why |
|---|---|---|---|
| "Are you now or have you ever been married?" | 1 | 1 | Either answer is known at once. |
| "Did you have additional income of unsupported varieties, 1040 lines 14e, 14f, 14j?" | 20 | 20 | The filer must find out what is being asked, and look up a form and its lines, to answer either way. |
| "Are you a veteran with one of the following:" and three unrelated long items | 5 | 1 to 15 | A non-veteran says no at once; a veteran who says no must read all of it. The items do not belong together, which unsettles the context the interview has built. |

On splitting ("Do you have a brown cat with blue eyes which was inherited from a great aunt between 1995-7 and is
currently FIV positive?"): asked as separate easy questions, the whole costs about the same to someone who answers
them all, but each easy question is an off-ramp. A person without a cat leaves at "Do you have a cat?"; in the one
long question even that person tends to read to the end. The separate questions can then be put in the order that
makes the average cost of the walk least.

**The criterion (owner, 2026-11-12).** The least mental effort to answer correctly. An edge's cost is the cost of
giving that answer and being right, so a design that lowers effort by making a wrong answer easy is not cheaper; it is
unacceptable. A vague parent whose "no" feels easy but takes thought to give correctly is an expensive edge.

### What follows from the frame (stated by the agent; the owner has seen these and not objected, none yet tried on a question)

For a yes or no question answered yes by a share p of the filers who reach it, with costs y and n, the expected cost
is e = p·y + (1 − p)·n.

- **Order within a chain.** Where a no ends a chain of questions, ask them in rising order of e divided by the share
  who leave at that question. This is the least expected cost when the answers are independent; where they are not,
  it is a heuristic. It applies only among questions that can change places: "Is it brown?" cannot come before "Do
  you have a cat?".
- **When a parent pays.** A parent costing g, answered no by a share q of those asked, in front of children costing C
  in total, lowers the expected cost only when g is less than q·C. This is why fourteen flat questions asked of
  everyone failed: splitting without layering gives no off-ramp.
- **A catch-all is not a chain.** Where any yes refuses, the typical filer answers no to every item and never leaves
  early, so order cannot help them. Only a parent, or rule 1 (the item moved beneath a question that already gates
  it), does.
- **Cost depends on what came before.** The third example's incoherence is a cost carried into the next question, so
  order is chosen within a topic and then among topics, not across the whole interview at once.

### What the frame needs that the project does not have

Shares exist for 88 situations (`interview/2025/gate_frequencies.yaml`, many of them judgments). Costs do not exist:
the words report counts words, and the second example above is short and costs 20. The owner's decision, 2026-11-12:
he rates each answer's cost as he walks the questions on the vetting page, and those ratings seed a formula from
features that can be counted (words, the number of "or" items, terms that need a gloss, whether a document must be
fetched). The measurement is not yet designed.
