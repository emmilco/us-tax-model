# Handoff: T-091 done (reviews complete, committed with this file); next is T-092

## Status at commit (2026-10-31, late; Claude Opus 5.5)

Everything below "Written 2026-10-31" is the record from the start of the session; this block supersedes its state and steps.

- Two review rounds on dependent and household, both families (transcription, render, class M), plus completeness and screens;
  rulings applied (`.transcription/proposed/t091/`, `t091r2/`; brief sections "T-091 round" and "T-091 round 2" in
  `.transcription/proposed/fixr2/BRIEF.md`; completeness `r6`, `r7`; screens `group6`). Logs archived before each round in
  `.transcription/archive/before-t091-2026-10-31/` and `before-t091-r2-2026-10-31/`.
- Round 1 found one low that T-091 introduced (the absence refusal refused returns another person qualified). Owner's new
  standing rule: a regression in uncommitted work is fixed before commit whatever its severity (recorded in
  `handoffs/HANDOFF-HARDENING-1.md`). Fixed as BUG-0267: the refusal moved to the return-level gate `household.hoh_absence`.
  Round 2 found nothing of any severity.
- Owner accepted the QSS wording addition and the age-18 refusal; `CLAUDE.md` now points to `HANDOFF-NEXT-SESSION.md`.
- BUG-0264 to BUG-0267. T-092 gained: Form 2441 line 2 `shown_when`, the newborn hospital-stay clause in `dependent.months`,
  and a to-check on the considered-unmarried absence. Owner left `generate.ts` drawing `absence_no_return` false.
- Class M of dependent was regenerated (8 cases). check-all (with mutation and Lean comparison) run before the commit.
- Next: T-092 with T-094 alongside, then Schedule E (Stage 17).


Written 2026-10-31 by Claude Opus 5.5. Facts here were observed in this session unless marked otherwise.

## Current state

- Repo `/Users/elliotmilco/Documents/GitHub/tax-formalization`, branch `main`. HEAD `3ea8fa3`, equal to origin when last fetched.
- **All T-091 work is uncommitted in the working tree.** Do not reset, stash or clean. `git status` should show about 29 changed
  paths: forms, interview, fixtures, generators, the input contract, rendered output, and this file's pointer.
- Nothing is running.
- Inspected: `npm run build` OK; `npm run fixtures` 1406/1406 (1394 old, 12 new) on that build.
- **Not run on this change:** check-all, mutation testing, Lean comparison, engine differential, any model review. The old fixtures
  got neutral answers, so their passing shows only that old results did not move.

## Read first

1. This file.
2. `handoffs/HANDOFF-HARDENING-1.md`: the owner's standing decisions and operational facts.
3. `git diff forms/2025/dependent.yaml forms/2025/household.yaml`: the change itself.
4. `TASKS.md`, rows T-091, T-092, T-094.
5. `.transcription/proposed/fixr2/BRIEF.md`: the adjudication brief; append a new section for this round.
6. `reviews/2025/completeness/dependent_household.findings.md`, PENDING-4 and PENDING-7: the source findings.
7. Before any scripted `claude -p` or model run: `~/.claude/AISP.md` (QMS Annex A). The review tools are fixed-prompt with no tools.

The project `CLAUDE.md` still points to `HANDOFF-INTEGRITY.md` as current. That pointer is stale (last changed 10-25; that plan was
paused 10-26). Its inference-cost paragraph still stands: paid model calls are pre-authorized.

## Decisions by the owner (this session)

- **Order:** T-091, then T-092, with T-094 as a standing burn-down alongside, a few forms at a time paired with each form's next
  review. Schedule E (Stage 17) after.
- **Item 1, spouse's relative on a joint return:** new input, not rewording. p501 p. 19's joint-return sentence sits only under the
  qualifying-relative test, so the review's proposed rewording of `relationship` would have leaked into the qualifying-child test.
- **Item 2, temporary absence:** split inputs. The expected-return sentence (p501 p. 9) sits only under head of household, so owner
  chose option (b): leave `months`, `part_year_home` and `us_half` unchanged and put the condition on the head-of-household path only.
- **Item 3, kidnapped child, qualifying relative:** refuse, do not encode the part-year rule.

## My own choices, not explicitly ruled by the owner; tell them

- The expected-return condition was also added to the `household.qss_eligible` wording, because p501 p. 11 points QSS to the
  head-of-household temporary-absence rule.
- `dependent.qr_kidnapped` refuses at age 18 and under (`age < 19`): p501 p. 18 "until ... the year the child would have reached age
  18" is unclear about that year, and refusing is the safe side.
- `qr_all_year` treats p501 p. 19's "may be considered temporary" as counting. The owner approved that wording in the option, but no
  ambiguity register entry was written. Consider one in `ambiguities/2025.yaml`.
- `absence_no_return` also covers "did not continue to keep up the home", the second sentence of p501 p. 9.

## What changed

`forms/2025/dependent.yaml`:
- New inputs `dependent.spouse_relative`, `dependent.qr_all_year`, `dependent.absence_no_return`.
- New gates `dependent.hoh_absence` (`hoh_lived_half` and `absence_no_return`; refuses `hoh_test2`) and `dependent.qr_kidnapped`
  (refuses `qualifying_relative`).
- `qr_relationship`: new branch `f1040.status == mfj` and `spouse_relative`; `months == 12` replaced by `qr_all_year`.
- `relationship` question: says to give the relationship to you; a later question covers the spouse's relatives.

`forms/2025/household.yaml`: `qss_eligible` wording and citation.

Ripple, done: `interview/questions-2025.yaml`; profiles `2025`, `sales-2025`, `stage4-2025` (`full-2025` asks all questions);
every fixture answering `months` (771 entries: `spouse_relative` false, `qr_all_year` = months == 12, `absence_no_return` false);
`engine/src/generate.ts` (no random draw, so the stream is unchanged); `tools/engines/generate_cases.py`;
`tools/transcription/input_contracts/2025/dependent.json`. Twelve `t091.*` cases appended to `fixtures/2025/stage8.json`; each was
predicted from source before evaluation. Their `covers` lists are one generic list; tighten them if coverage asks.

Possible gap to check: `classm.json` and `classm.deepseek.json` received inserted answers too; class M fixtures have recorded
provenance, and the check for that has not been run on this change. check-all will show it.

## Next steps, in order

1. Update `TASKS.md` (T-091 status) and `BUG_INVENTORY.md`. Next number after BUG-0263, confirm with grep. One entry per defect.
2. Archive stale logs of `dependent` and `household` to `.transcription/archive/<name>/` with a MANIFEST.
3. `npm run render`, then
   `python3 tools/transcription/rerun_all.py --kinds transcription,render --forms dependent,household --model M --jobs N`, once with
   `claude-opus-5-5` and once with `deepseek-flash`. Class M: `classm.py --doc X --model M --case-jobs 4`.
4. `completeness_review.py --forms dependent,household`; `screen_review.py --screens dependent.married,dependent.multiple_support`
   (in `tools/transcription/`).
5. `triage.py --form X [--family deepseek]`, adjudicate with agents on disjoint files per the brief, apply with
   `rule.py --kind K --form F --family claude|deepseek --rulings <json>`. Expect many `shown_when` rulings (T-076 decision).
6. Coverage checks, as last run:
   - `check_consumers.py`, 5 new, to rule in `reviews/2025/consumers.json`: `dependent.lawful@p501:p19`, `f1040.status@i1040gi:p19`,
     `f1040.status@p501:p19`, `dependent.spouse_relative@i1040gi:p19`, `dependent.age@p501:p18`. Remove stale
     `consumer:dependent.months@i1040gi:p19`.
   - `check_screens.py`: remove stale `unruled:dependent.married`, `unruled:dependent.multiple_support` from `screens/rulings.json`
     (after step 4).
   - `check_completeness.py`: rule after step 4; `check_logs.py` exit 0 after step 5.
   - Clean: instruction cites, operands, signs, limits: 0 new, 0 stale.
7. Fix-and-review loop: fix medium and higher, batch lows into T-092, stop when a round finds nothing medium or higher.
8. Edit `TASKS.md` before check-all (the hook needs it green on the exact tree). `npm run check-all` takes about 15 minutes.
   `git commit -F <file>`, **pull, then push**; the owner edits the README on GitHub.

## Roadmap after that

- **T-092:** about 30 batched lows; verify Form 8962 line 11 (d)/(e) below 100% of the poverty line, and the Form 8863 ITIN verdicts
  against Pub. 970 for the lifetime learning credit.
- **T-094** alongside: baselines, form by form, each citation fix reopening the form's reviews.
- **Remainders:** T-066 printed-only class M for single documents; T-076 (3), (4); T-079 (2), (4); T-081 (3), (4), (5), (7) and the
  mutation kill attribution in `engine/src/mutate.ts`.
- **Schedule E (Stage 17).**

## Open questions for the owner

1. Fix the stale `HANDOFF-INTEGRITY.md` pointer in the project `CLAUDE.md`? It is guidance for future agents, so show the proposed text.
2. Accept the QSS wording addition and the age-18 refusal above?

## Rules that bite

- A new input must be answered in five places: fixtures (insert as text; some files do not round-trip), interview, `generate.ts`,
  `generate_cases.py`, input contracts.
- `npm run fixtures` uses the last build: a failed build still prints a stale pass. Check the build first.
- Do not run `/tmp/s19/gen.py`. Do not rebaseline to make a check pass. Do not lower deepseek's output budget. Do not pass a brief's
  illustrative examples as source. Avoid form-level baseline release.
- `eval --json` nests each result under `value`.
- QMS: status line at session start, refer choices with more than one defensible answer to the owner, provenance on completion claims.
