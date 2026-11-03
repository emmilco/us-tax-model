# F1 dependent/education batch — report

Branch `claude/f1-dependent`, from `main` at 5eec22f. Rows: T-104 to T-113, T-153, T-154, T-167, T-168; bugs
BUG-0282 to BUG-0285, BUG-0300, BUG-0301. Proposed inventory entries are in `PROPOSED_BUGS.md` (PENDING-1 to
PENDING-11). Nothing in `BUG_INVENTORY.md`, `TASKS.md`, `TASKS-DONE.md`, the handoffs, `tools/` (except the
`tools/coverage/tree.json` placements the brief requires) or `engine/src/mutate.ts` was edited.

Labels: **inspected** means read in the source or code, or executed; **inferred** means reasoned without execution.

## Environment

- `claude -p` works here (a one-word test call, then the transport's own flags with `--output-format json`). All
  reviews below ran on `claude-opus-5-5`. DeepSeek and GPT were not run (no key in the cloud).
- `tools/transcription/rule.py` and `triage.py` need Python 3.12 or later (an f-string with a backslash); the
  default `python3` here is 3.11, so they were run with `python3.13`. No tool was edited.
- No git hooks are installed in this clone, so no pre-commit or pre-push guard ran.

## Rows

### T-104 — `dependent.kidnapped` timing (commit 0bee817)

- **Premise:** holds (inspected). The question said "at any time during 2025, was presumed", while p501 p. 13 ties the
  rule to the year of the kidnapping and the year of return, not to when law enforcement presumed it.
- **Change:** the question now asks about a child kidnapped by a non-family member, presumed kidnapped by law
  enforcement, and missing because of it at some time in 2025 (a 2025 kidnapping, or an earlier one before the child's
  return), whenever law enforcement first presumed it. The row's suggested wording ("a child kidnapped in 2025") would
  drop a child kidnapped earlier and returned in 2025, whose year of return still applies the rule, so the question
  keeps that case (inferred from p501 p. 13, statements 2 and 3).
- **Regression:** shares T-105's.

### T-105 — over-refusal of a returned kidnapped child (commits 0bee817, bec56d7)

- **Premise:** holds (inspected: both refusals were on `dependent.kidnapped` alone; `stage21.d3.kidnapped_child_refused`
  with 12 months was refused).
- **Change:** gates `dependent.kidnap_residency` (kidnapped and fewer than 7 months) on `lived_half` and
  `dependent.kidnap_eic` (kidnapped, EIC relationship yes, `us_half` no) on `eic_child`. `months` and `us_half` now say
  the time a kidnapped child was missing does not count, so a child who needs the treatment still reaches the refusal.
  The Claude transcription built the same gate independently (`h_kidnap_issue`: kidnapped and months under 7).
- **Regression:** `f1.kidnapped.returned_11` (11 months): qualifying child, EIC child, EIC $3,261 (i1040gi p. 53
  rows $25,000 and $30,000). `stage21.d3` moved to 4 months and not in the U.S. half-year: refused at line 16
  (`kidnap_residency`) and 27a (`kidnap_eic`). The two `stage21.f1.where_kidnapped_withheld_*` evaluator regressions
  lost their unanswered gate at 12 months; their withheld child moved to 4 months (and the EIC case out of the U.S.
  half-year) so the gate stays unanswered; expectations unchanged. All predictions written before evaluation and met.
- **Over-refusal:** a child presumed kidnapped who lived with you fewer than 7 months is still refused even where the
  treatment would not help; accepted (it was refused before too).

### T-106 — newborn's required hospital stay (0bee817)

- **Premise:** holds (inspected: `months` did not mention it; p501 p. 13 "except for any required hospital stay
  following birth").
- **Change:** wording in `dependent.months`. No regression (wording only; the existing month count rule is unchanged).

### T-107, T-108, T-109 — support definitions (c7fd54c)

- **Premise:** holds (inspected against p501 pp. 15, 20, 21).
- **Change:** `dependent.supported` and `dependent.self_support` state total support, the Don't-Include list (items 1
  to 6), premiums and insurance benefits, GI Bill, tax-exempt income and savings, property at fair market value,
  capital items, own home and rent-free living, foster-care business and charitable expenses, the home-for-the-aged
  lump sum, quarters allowances, year of support; T-108's state-support sentence now says "this person as a needy
  person". Wording only, no regression. The dependent completeness rerun found five remaining rules (PENDING-11).
- **Over-refusal:** none added (no refusal). A filer who now counts differently can move between a computed dependent
  and none; that is the intended correction.

### T-110 — revoked release timing (c7fd54c)

- **Premise:** holds. The quote is on p501 p. 22 in the archived text (the row says pp. 14-15; p. 14 starts the same
  sentence and the citation checker places the full sentence on p. 22).
- **Change:** `dependent.divorced_rule` says a release revoked without notice in 2024 or earlier still applies for
  2025. The screen review of this question was rerun (below).

### T-111 — TANF for a parent's home (c7fd54c)

- **Premise:** holds for `dependent.parent_home_paid` (inspected). Its sibling T-115 on `household` is already done:
  `household.home_cost` and the QSS question carry the TANF sentence (inspected), so no household edit was needed.
- **Change:** one sentence in `parent_home_paid`. Wording only.

### T-112 — Form 2441 line 2 visibility (4475893)

- **Premise:** holds (inspected: no `shown_when`).
- **Change:** `shown_when: dependent.dc_qp` on `dc_line2c` and `dc_line2d`.
- **Regression:** `f1.dc.line2_shown_qualifying_only` asserts the condition; fixtures cannot assert visibility, so the
  values sheet was checked by hand (`eval --html` on the facts of `stage15.regress.f2441.nonqualifying_dependent`:
  4 line 2 entries before, 2 after).

### T-113 — lifetime learning credit with an applied-for ITIN/ATIN (de5a15b; owner decision)

- **Premise:** holds (inspected: `dependent.tin` and `person.edu_student` accepted an applied-for number for both
  credits; i8863 p. 3 item 5 and Table 1 say "issued"; p970 p. 11's deeming is in the American opportunity chapter).
- **Change:** person side, gate `person.edu_llc_tin_refused` (`edu_llc` and `person.tin` No, so only `itin_applied`);
  dependent side, new input `dependent.edu_tin_issued` and gate `dependent.edu_llc_tin_refused`; both refuse line 31.
  The American opportunity credit is unchanged. "Or filer" in the decision is read as the filer who is the student,
  because Table 1's lifetime learning column requires only the student's TIN (inferred; owner question 2).
- **Ripple:** interview bank entry; `engine/src/generate.ts` answers Yes for dependents (constant, no draw); four
  fixtures with a dependent lifetime learning student answer Yes (annotated context repair, values unchanged);
  `tools/engines/generate_cases.py` needs the same answer, supplied as `generate_cases.patch` here because `tools/` is
  out of bounds for this branch (`git apply --check` passes). `siblings.py --input` finds no other place.
- **Regression:** `f1.t113.dep_llc_applied` and `f1.t113.person_llc_itin_applied` refuse at line 31 and line 10;
  `f1.t113.dep_aoc_applied` and `f1.t113.person_aoc_itin_applied` keep their American opportunity values.
- **Over-refusal:** the return is refused rather than prepared without the lifetime learning credit for that student,
  as decided.

### T-153 — non-taxpayer other claimant (8c93c99)

- **Premise:** holds, with a correction. The row asks to define the other taxpayer inside `other_claimant`; but that
  input also drives the tie-breaker refusal, and p501 pp. 15-17's tiebreaker rules have no non-taxpayer exception
  (they compare the parents "who can claim the child"). Folding the definition into the question would lift the
  tie-breaker refusal for your own qualifying child whose other parent does not file (inspected source; the effect is
  inferred). So the fix splits the two uses.
- **Change:** new input `dependent.other_nontaxpayer`; gate `dependent.qc_tiebreak` (other claimant and either your
  own qualifying child or a taxpayer other person) on `qualifying_child`; gate `dependent.eic_tiebreak` (other
  claimant and your EIC qualifying child) on `eic_child`. The EIC refusal had also fired for persons who are not your
  EIC qualifying child (inspected by reading; folded into PENDING-2).
- **Regression:** `f1.t153.friend_child_nontaxpayer` (p501 p. 18 Example 1): qualifying relative, line 19 $500;
  `friend_child_taxpayer` (Example 3) and `own_child_nontaxpayer_other` refused at `qc_tiebreak`. Two older fixtures
  follow the new gate ids and still refuse without answering the new input (executed).
- **Over-refusal accepted:** `other_claimant` still includes the EIC rules, so a person who is another taxpayer's
  qualifying child only under the EIC rules is refused rather than computed.

### T-154 — care-expense allocation (e9d7acb)

- **Premise:** holds (inspected i2441 p. 2, p503 pp. 6 and 8).
- **Change:** child support, day-by-day allocation with the temporary-absence and part-time exceptions, and the
  mixed-purpose division in `dependent.dc_paid`. Wording only. The completeness rerun found further omissions
  (household services, transportation, agency fees, volunteer work): PENDING-10.

### T-167 — stillborn child (c7fd54c)

- **Premise:** holds. **Change:** `dependent.born_died` states the live-birth requirement and excludes a stillborn
  child; two consumer pairs ruled `same`. Wording only.

### T-168 — student definition (c7fd54c)

- **Premise:** holds. **Change:** `dependent.student` adds the school definition, the school's full-time standard,
  non-consecutive months and the co-op rule. Wording only.

## Reviews (all Claude `claude-opus-5-5`; receipts committed)

Pre-rerun logs, rulings and the class M fixtures are archived in
`.transcription/archive/before-f1-dependent-reruns-2026-11-03/` (with MANIFEST).

| review | result | receipts |
| --- | --- | --- |
| dependent transcription | 3 agree / 19 disagree, all ruled; triage `triage/dependent.json` | `.transcription/dependent.{prompt,response}.txt`, `.meta.json` |
| person transcription | 53 / 46, all ruled; triage `triage/person.json` | `.transcription/person.*` |
| dependent render | 1 match / 10 mismatch, all ambiguities with owner decisions | `.transcription/dependent.render.*` |
| person render | 32 / 0 | `.transcription/person.render.*` |
| completeness dependent, household | 6 claims ruled (2 real gaps PENDING-10/11, 3 out of scope executed, 1 presentation) | `.transcription/completeness/{dependent,household}.*` |
| screen `dependent.divorced_rule` | WIDE, 4 findings accepted (refusal executed) | `.transcription/screens/dependent.divorced_rule.*` |
| class M dependent | 4 cases, 12 agree, 0 disagree (8 earlier cases replaced) | `.classm/classm.dependent.{1..4}.*` |
| class M person | 1 case, 15 agree, 0 disagree | `.classm/classm.person.1.*` |

Triage: every completed-return difference was enumerated with the witness cap lifted (the triage function called
with an unbounded witness count, output to scratch; the recorded triage files are the standard runs), and value groups
were spot-checked with derivation trees. Protections claimed in rulings were executed: the ban refusal for a dependent
American opportunity student, `scope.other_income` on a joint return, `kidnap_residency` on a head of household
return, the `divorced_rule` refusal, and the T-153 and T-113 refusals.

### Rulings that deserve a second look

- **dependent `claimed`, `ctc_*`, `hoh_test2`:** the Claude reply lifts the tie-breaker refusal when the other person
  is not a taxpayer, even for your own qualifying child; ruled scope (project refuses on a cited gate). This is owner
  question 1.
- **person `ira_line2`, `ira_line6`:** far more completed-record differences than the previous round (586 and 526,
  against 131 and 114). Every group checked is the `amb.2025.ira_covered` reading (the reply reads a SEP/SIMPLE answer
  without a Schedule C) and none reaches the IRA deduction (no completed value difference on `ira_deduction`), but
  only representative witnesses were derived.
- **person `x_must`:** model error on 19 records (the reply omits the HSA excess from the must-file count); one reverse
  witness (generated 259, project 0 and candidate 1) was not explained.
- **person `s179_listed`/`s179_nonlisted`:** ruled model error (the reply puts all section 179 amounts in the
  non-listed total); last round the same lines were representation with no difference.
- **person `hsa_*`:** reused the previous round's representation reasoning after one derivation check.
- Several person rulings reuse the previous round's class with fresh counts and an enumerated cause list; the old
  rulings' quotes were partly truncated, so the quotes were rewritten and checked against the archive by script.

## Owner questions

1. **Tie-breaker and non-taxpayers.** i1040gi p. 19 / p501 p. 18 exclude a non-filer (or refund-only filer, or a
   non-citizen with no U.S. gross income) from "taxpayer" for the qualifying-relative test. Should that exclusion also
   lift the tie-breaker refusal when the child is your own qualifying child and the other person is such a
   non-taxpayer? The project keeps the refusal (p501 pp. 15-17 have no such exception); the Claude transcription
   reads the other way. The same question applies to the EIC tie-breaker.
2. **T-113 "or filer".** Read as the filer who is the student. A filer whose own ITIN was only applied for, claiming
   the lifetime learning credit for a dependent student with an issued number, is not refused (Table 1 requires only
   the student's TIN for that credit). Confirm.
3. **T-104 wording.** The question covers a child kidnapped before 2025 and still missing at some time in 2025, not
   only a 2025 kidnapping as the row suggested. Confirm.

## Rows not done

None of the listed rows is left undone. Not done and out of scope: the PENDING-10 and PENDING-11 gaps found by the
completeness rerun; the DeepSeek reruns.

## Checks

Run on the branch (inspected outputs):

- `npm ci`, `npm run build`, `npm run render`: pass.
- `node engine/dist/main.js test-fixtures`: 1,446/1,446 after T-153; 1,442/1,442 at the tip after the class M rerun
  replaced dependent's 8 class M cases with 4 (baseline 1,437 at 5eec22f).
- `tools/citations.py --strict`: 0 findings. `tools/check_instruction_cites.py`: 0 new (148 baseline; one stale
  baseline entry removed because the touched line now cites its i8863 page). `tools/check_consumers.py`: 0 new, 0
  stale (11 pairs ruled `same`, 3 stale entries removed). `check_screens.py`: 0 new, 0 stale.
  `tools/coverage/tree.py --check`: current (195 gates). `tools/siblings.py --check`: passes.
- `check_completeness.py`: fails only on the two pending ids `PENDING-10`, `PENDING-11` (by design; the integrator
  files the bugs and puts the ids in `reviews/2025/completeness/rulings.json`). Person's completeness review cannot
  run: its prompt is 609,038 characters, over the tool's 400,000 limit.
- `check_logs.py` (Python 3.13): Claude transcription, render and class M logs current with no open rulings. DeepSeek
  transcription, render and class M logs of `dependent` and `person` are stale; DeepSeek is listed without
  "optional" for transcription and render, so `check_logs.py` fails until the integrator reruns them.
  Under the default Python 3.11 the script stops in its human-review step with a syntax error in an imported
  module; under Python 3.13 that step passes ("human log integrity OK").

Not run: the mutation step the class M tool asks for after replacing cases ("keep any case a mutant needs in a stage
fixture"), the full `check-all` (mutation, engine differentials with ignored data, Lean), `npm run compare`,
`test-integration`, the DeepSeek reviews, `tools/engines/generate_cases.py` (needs the patch first).
