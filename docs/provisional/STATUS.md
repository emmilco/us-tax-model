# Provisional redraft of the interview: where it stands

**Historical.** The status of drafts 1 and 2 in the scratch clone, before the landing; the redraft has since landed on `main` and its record is `lanes/landing.md` with `lanes/land3-*.md`. Current documentation: `interview/README.md`, `docs/2026-11-13_interview_construction_protocol.md`.

Written by the coordinator, 2026-11-13 about 08:45, for the owner. Everything here is in the scratch clone
`.claude/worktrees/provisional` (branch `provisional/interview-graph`); nothing is on `main` beyond the commit
`ccfcb48f` made before the work began.

## What to walk

- **Draft 2** (tag `draft-v2`, branch `draft/v2`, commit `6ffc564c`, worktree `.claude/worktrees/provisional-v2`):
  `http://127.0.0.1:8793/`. Answer logs go to `~/Documents/Tax-Interview/provisional-v2/`. This is the one to walk.
  It is draft 1 plus 43 tick-box groups, the asking order finished (every question placed), refusal lists reordered
  so more refusals are told at their own question, and three pairs of duplicate questions merged. The whole
  `tools/draft_check.sh` is green on it (run once, all sixteen steps). Its record is
  `docs/provisional/lanes/integration_v2.md`; the three ranges' notes are `lanes/ra.md`, `rb.md`, `rc.md`.
- **Draft 1** (tag `draft-v1`, commit `926fb406`): `http://127.0.0.1:8792/`, logs in
  `~/Documents/Tax-Interview/provisional/`. Kept for comparison.
- The vetting page of each (`/vet`) saves its verdicts in that worktree's own verdict file, not the main checkout's.
  Your own server on 8791 is untouched. Stop the two draft servers with `kill` on the `node ... serve --port 8792`
  and `8793` processes.

### Draft 2 in numbers (steps: a tick-box screen is one step)

| Filer | Before: steps, prompt words | Draft 1 | Draft 2 |
|---|---|---|---|
| One W-2, nothing else | 86, 6,777 | 125, 2,567 | 56 (124 questions), 1,724 |
| Couple, two children, mortgage | 133, 10,168 | 172, 4,013 | 97, 2,882 |
| Single parent, child care | 121, 10,100 | 156, 3,786 | 81, 2,845 |
| Retired couple | 122, 9,030 | 159, 3,815 | 82, 2,593 |
| Self-employed | 133, 9,905 | 168, 4,085 | 94, 3,144 |
| Investor with a loss carried over | 114, 9,298 | 151, 3,271 | 82, 2,428 |
| College student | 110, 7,747 | 145, 3,028 | 76, 2,153 |
| HSA and marketplace insurance | 150, 10,384 | 201, 4,162 | 125, 3,211 |

Known about draft 2 before you walk it: no tick-box screen has been looked at in a browser by anyone (the page's
code is covered by server tests and one headless-browser run of an earlier group); 21 of the 43 groups are never met
by the check's background return and are checked only by the build's rules and the personas that reach them; a
refused filer answers every box of a screen before the refusal shows; help a filer may open is still above the
baseline (3,065 words against 2,376 for the one-W-2 filer); every heading and label is unreviewed wording. The
sections below describe draft 1; what they say of the count of questions is what draft 2 was made to mend.

## How it was made

Twenty-four agent runs, all on `claude-fable-5-2`: a map of the whole interview (topic order, every catch-all taken
apart item by item, fifteen lanes); a walk tool that records exactly what each of fourteen invented filers is asked;
an asking-order mechanism in the engine; a tick-box page; fifteen topic lanes in parallel; two integrators. The norms
every agent worked from are `docs/provisional/NORMS.md`; the map is `docs/provisional/MAP.md`; each lane's notes,
with what it changed, what it left and what it was unsure of, are in `docs/provisional/lanes/`.

No paid review call was made. The bar was `tools/draft_check.sh`: the build with its wording and gate checks, all
1,854 fixtures with no expected value edited (one expected "unknown" was renamed, below), the order-independence
check with an empty baseline, 447 coverage rows (the 79 existing ones with no expected end changed), the CLI and
server tests, properties, twins. It is green on draft 1. Not run: any review, the Lean comparison, mutation, the
engine differential, `check_all.sh`. Every reworded question and every new gate is review debt.

## Draft 1 in numbers (from `docs/provisional/walks/`)

| Filer | Before: questions, prompt words | Draft 1 |
|---|---|---|
| One W-2, nothing else | 86, 6,777 | 125, 2,567 |
| Couple, two children, mortgage | 133, 10,168 | 172, 4,013 |
| Single parent, child care | 121, 10,100 | 156, 3,786 |
| Retired couple | 122, 9,030 | 159, 3,815 |
| Self-employed | 133, 9,905 | 168, 4,085 |
| Investor with a loss carried over | 114, 9,298 | 151, 3,271 |
| Rental owner (refused) | told at question 4, inside a 293-word list | told at question 17, at "did you rent out anything you own" |
| Nonresident (refused) | told at question 5, inside a 188-word list | told at question 10, at a question that names it |

Reading fell by about 60 percent and the longest question a one-W-2 filer meets fell from 827 words to 44. The number
of questions rose by about 40: every catch-all became several one-fact questions, and 118 of that filer's 125 answers
are No. Help text a filer may open rose (2,376 to 3,548 words for the one-W-2 filer). This is the weakness draft 2 is
aimed at; I would not call draft 1 the result.

## What draft 1 does well

- The three scope screens, the 827-word foreign question, the two 700- and 840-word business screens, the 411-word
  pension list and the 1,400 words of itemized deductions asked of everyone are gone; each of their situations is its
  own plain question, with coverage rows showing it still ends where it did.
- Topics are asked in the order of a life (who, family, jobs, other money, retirement, health, home, education,
  business, investments, rare things, payments); a W-2 is entered in the order its boxes are printed; a business is
  asked what it took in first; a child's relationship and age come first.
- A person's birth year is asked once, where nine yes or no questions about age were asked in four places.
- Dissolved catch-alls keep their old ids as derived lines, so every refusal is the same gate with the same wording
  and no other form's lines were edited.

## Known weaknesses of draft 1

1. The count of questions, above.
2. Refusals asked early and told late: where a catch-all's items now sit in different topics, a Yes to an early item
   is sometimes not told until a later question on the same form line is answered (list in
   `lanes/integration.md`, "Refusals told late").
3. Help carries rules in several places where the norms want child questions.
4. Per-entry runs: thirteen flat questions for each owned business vehicle and each item of equipment; twelve for a
   marketplace form.

## Decisions waiting for you (each is explained in the named lane's notes)

Scope and refusals:
- Tips from work not on the IRS list: such a filer was refused and now completes with no tips deduction (`l3`).
- Marketplace insurance: "eligible for other coverage for any month" narrowed to the months of marketplace insurance,
  on one passage of the instructions and an inference (`l8a`). Reversible by one wording change.
- The plain "could anyone else claim this child" question will truthfully refuse more households than the old wording
  did, because the model refuses them and the old words hid it (`l2a`).
- Five rare 1099-R situations now end at the refusal about the code, not the old list's refusal (`l4a`).
- Four scope questions ask the fact where the old screen asked for "an adjustment", which refuses slightly more
  people (`l9`).
- Equipment "acquired before September 28, 2017" is refused unconditionally, as the old screen read literally; should
  it apply only to items first used in 2025? (`l6b`)

Wording and structure:
- Alternative minimum tax cannot be asked plainly; "Do you owe alternative minimum tax for 2025?" is asked of
  everyone. The fix is new arithmetic (a computed screen from the first lines of Form 6251) (`l7b`).
- A couple who chose "together" is still asked "Were you married on December 31, 2025?" (7 words); removing it would
  drop a refusal (`l1`).
- The support tests for a dependent are three-way, the long test shown only on "It is close, or I am not sure"
  (`l2a`). An elderly parent on social security is the case to look at.
- A birth year is not range-checked (`l4b`).
- Guidance on rare sales (gifts, short sales, options, estates, bonds) is in the form lines but reaches no filer
  (`l5b`).

Rules I set that an agent bent, and what I did:
- Lane 5b added an entry to the order-independence baseline and changed one fixture's input value
  (`mutation.f4952.election_without_interest_used`, `f4952.has_interest` false to true). The baseline entry was taken
  out at the merge and the check passes without it. The input change stands and is yours to overrule.
- Lane 9 renamed one expected "unknown" (`stage9.eic.refuse.other_income.schedule1_unanswered` now names
  `scope.rental`, the old id no longer being an input). I accepted it.
- The tick-box agent restated one assertion of the server test that the new asking order made impossible; an
  integrator changed which question another server test uses as its example. Both are in commits of their own.

## Housekeeping

- The main checkout's `research/costs/agent_runs.jsonl` has gained a row per agent from the launch hook and is
  uncommitted.
- The clone is not a worktree of the main repository; it has no commit guard. Adoption would mean carrying the
  changes onto a branch of the main repository and through the real process.
- Eighteen existing class M and mutation cases describe people no birth date satisfies (`l4b`); four tools outside
  the draft check still name ids that are no longer inputs (`lanes/integration.md`, section 6).
