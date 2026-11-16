# int-n10.patch and int-n10-ticks.patch: N10 rewrites (plan-interview item 2)

Lane patch-interview, claude-opus-5-5, judgment, 2025, us. Bank only (`interview/2025/questions.yaml`). Nothing run.
**[C]** checked; **[I]** inferred.

## Summary

- **Two patch files, not one.** The tick-member prompts depend on the owner's answer to plan item 5 (does N10's
  25-word limit apply to a member's full prompt?). They are in `int-n10-ticks.patch` so that `int-n10.patch` can be
  applied alone. The two touch different bank entries and apply in either order [I: disjoint hunks; each was
  dry-run against the untouched bank, not one on top of the other].
- **The wording is the plan's verbatim** (/tmp/nightplan/interview.md section 2), with one deviation, below.
- **Form `source` texts are not edited.** Each rewrite is a bank `prompt:` override, written with its frame, as the
  bank's per-entry prompts already are (e.g. `person.rrta` [C questions.yaml]). That keeps the forms' transcription
  and render reviews out of it. The alternative, editing the form `source`, makes those reviews due as well.
- `rprop.screen` is left out, as briefed. `int-rprop.patch` was **not drafted** (time).
- The script that builds both patches parses the bank before and after. It asserts that nothing but the stated
  `prompt`, `help` and `value_labels.residential` fields changed
  (/tmp/nightplan/scratch/patch-interview/tools/mk_n10.py).

## Deviation from the plan

The plan's `rental.personal_any` help drops the condition "(or trying to) for 12 months or more". Without it, a
filer who lived in the place for a few months before renting it could take those days as not personal use and
answer the parent No wrongly; the child `rental.days_personal` (which carries the rule) would then be skipped.
- I keep the condition. Help, 43 words: "Family: spouse, parent, grandparent, child, grandchild, brother or sister. Not
  personal use: family paying a fair rent to make it their main home, or days it was your main home before or after
  renting it (or trying to) for 12 months or more."
- Source: p527 [C as quoted by the plan at p527.cols.txt:870-875; not re-read here].

## int-n10.patch: children and help (word counts by the walk's rule, frame included; before → after)

| id | before | after | note |
|---|---|---|---|
| `rprop.kind` | 64 | 8 | prompt "For this building or improvement — What is it?"; the 80% rule moves into the `residential` choice: "A building whose rent comes mostly (80% or more) from homes, or an improvement to one" |
| `rental.days_personal` | 67 | **40** | at the limit, not under it; relies on the parent asked just before (N8); "in 2025" comes from the parent |
| `rprop.basis` | 46 | 34 | |
| `rental.not_at_risk` | 46 | 39 | adds "a government" as a qualified lender (i1040se); the guarantee/stop-loss gap is **not** fixed here (see below) |
| `rental.days_fair` | 44 | 35 | its help repeats the empty-day rule; left as it is |
| `rental.personal_any` help | 50 | 43 | deviation above |
| `person.f4137_under20` | 48 | **40** | new help 30 words |
| `person.mw_not_box1` | 47 | 28 | new help 20 words (box 12 code II, 1099-MISC/NEC, no form; until now in the prompt) |
| `person.mw_box1` | 43 | 37 | |
| `s2.amt_business` | 42 | 39 | outside the seven areas |
| `k1s.not_at_risk` | 54 | 34 | help 32 words |
| `k1s.past_years` | 50 | 37 | help 68 → 40 |
| `k1p.not_at_risk` | 49 | **40** | |
| `k1p.basis_short` | 45 | **40** | same words, new sentence break |

Four prompts land at exactly 40. N10 says "under 40". They are the plan's; whether the owner wants them trimmed by
a word is a style call.

**Who could answer wrongly** (protocol 2.3), per row:
- `rprop.kind`: the owner of a mixed shop-and-flat building; the 80% now sits on the option they read.
- `k1s.not_at_risk`: a shareholder with a nonrecourse loan who does not see it as "terms that protect you from
  loss". The help names that case first.
- `person.f4137_under20`: "at that job" relies on the per-employer questions just before it (order 148, seq 1-3
  [C bank]). In the CLI or a reopened answer that reference is weaker [I].
- The rest restate the same rule in fewer words; no new false No is expected [I].

## int-n10-ticks.patch: tick-member full prompts (only if the owner adopts item 5)

- Thirteen members, each now under 25 words.
- The labels and group membership are unchanged; only "What this asks", the CLI and the reopened question read
  these prompts.
- The examples removed from the prompts are already in each member's help, except `sche.qbi_business`. Its help
  gains "For example, 250 hours or more a year of rental services, with separate books."

| id | before | after |
|---|---|---|
| `rental.part_home` | 31 | 20 |
| `sche.qbi_business` | 28 | 14 (help 20) |
| `royalty.business` | 27 | 24 |
| `f1116sb.changed` | 36 | 15 |
| `f1116sb.split` | 29 | 21 |
| `f1116.reduction` | 27 | 22 |
| `rec.has_other` | 41 | 23 |
| `s1.nol_not_married` | 26 | 21 |
| `scope.tips_unreported` | 42 | 24 |
| `scope.household_pay` | 34 | 23 |
| `scope.contractor_pay` | 33 | 24 |
| `scope.wages_no_form` | 30 | 22 |
| `sd.qof` | 35 | 24 |

Owner judgment, as the plan says:
- `scope.contractor_pay`: the "no social security or Medicare taken out" condition now lives only in the help.
- `rec.has_other`: the excluded kinds now rely on the sibling boxes of `rec_kinds`.

## Not done

- `rprop.screen` (`int-rprop.patch`): a model change (six new inputs, a derived screen, a gated child, fixture
  restatements and coverage rows). Not drafted for lack of time; the plan's section 2.1 is the design.
- The `rental.not_at_risk` correctness gap (guarantees, stop-loss agreements, loans from a person with an interest
  in the activity, i1040se.cols.txt:48 per the plan) needs a new question.
  - Pending bug-entry text: "`rental.not_at_risk` asks only about nonrecourse loans from non-qualified lenders. It
    omits amounts protected by a guarantee or stop-loss agreement and amounts borrowed from a person with an
    interest in the activity (i1040se, at-risk rules). Possible false No; add a child or a second box and put it
    in the false-no sample."
- The six K-1 members the plan did not draft (`k1p.t6`, `k1p.t4`, `k1s.disposed`, `k1s.box16ef`, `k1p.r_b14bc`,
  `k1s.basis_carry`), and the help over 40 in the MFS, HSA and AMT rows.

## What to run

1. Build. It checks that a bank `prompt` does not repeat the line's, the spouse phrase and the per-person frame.
2. The person-wording report.
3. `draft-walk`: personas 09 (tips), 19 (rental house), 11 (refused rental), and any with Medicaid pay or K-1s.
   Check the words.
4. `interview-coverage --write`: the report quotes the wording.
5. `tick-groups` (ticks patch).

## Reviews due

- The questions review (`reviews/2025/questions/`) for every entry changed, scoped to those entries.
- The false-no sample for `rental.not_at_risk`, `k1s.not_at_risk`, `k1p.not_at_risk` and `rental.personal_any`:
  each parent's wording changed.
- No form is touched, so no transcription, render or class M review [I: those read the forms, not the bank].
