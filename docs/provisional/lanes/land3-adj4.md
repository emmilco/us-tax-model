# land3-adj4: adjudication of dependent, asset, clcw_next_year, f8889 (Claude transcription)

Judgment lane (claude-opus-5-5, class judgment, tax year 2025, jurisdiction us). Worktree `landing`, not committed.
Every open line (`Ruling: open`) of the Claude transcription logs of the four forms was ruled with
`tools/transcription/rule.py --kind transcription` (rulings files in `/tmp/land3-adj4/<form>.json`). A section
"Landing round (2026-11-14)" was added to each form's `reviews/2025/transcription/adjudication/<form>.md`. Evidence: the
log sections, the triage records `.transcription/triage/2025/<form>.json` (log sha256 matches the triage record for
all four forms), `triage.py --explain` on chosen witnesses, the fixtures, the form YAML, the ambiguity register and the
archived sources.

## Counts

| form | lines | model error | representation | ambiguity | scope | finding |
| --- | --- | --- | --- | --- | --- | --- |
| dependent | 21 | 15 | 6 | 0 | 0 | 0 |
| asset | 16 | 1 | 14 | 0 | 1 | 0 |
| clcw_next_year | 13 | 11 | 2 | 0 | 0 | 0 |
| f8889 | 10 | 1 | 7 | 2 | 0 | 0 |

No findings, so no pending bugs. No line was left open.

## Main patterns

- **clcw_next_year.** Lines 1-7 and 9-12: the reply drops the worksheet's applicability test (i1040sd p. 10, "Otherwise,
  you don't have any carryovers"; p. 14, Line 21) and shows the lines when there is no carryover. The values are the
  project's wherever both show. Ruled model error, as the deepseek reply was ruled in Stage 20 round 2. Lines 8 and 13: the reply's zero on a
  decedent's final return is the project's hidden line and notice (p550 p. 103). The reply reads the gated input
  `final_return` raw. Ruled representation.
- **f8889.** Line 3, model error: for a married filer aged 55 or older with family coverage in part of the year, the reply
  puts the $1,000 for the self-only months on line 3. The instructions forbid this (i8889 p. 5, Note; p. 4, rule 6).
  Line 6, ambiguity: the reply takes the alternative that amb.2025.hsa_step4_other_limits records. Line 7, ambiguity: the reply takes
  the alternatives that amb.2025.hsa_line7_months and amb.2025.hsa_last_month_all_year record. Step 1, the share, split,
  excess_amt, and lines 13, 15 and 17b: representation. Their values are equivalent, or differ only where the line is not read or through
  upstream lines.
- **dependent.** The reply's dependent test is built into most lines. It exempts a joint return from the dependent
  taxpayer test, although i1040gi pp. 18-19 says "Yes. STOP You can't claim any dependents" with no such exception. It also tests residency by
  months > 6 only, with no born-or-died, adoption or placement rule (p501 p. 9; i1040gi p. 15; p503 p. 3). These two
  errors make 15 lines model errors. On 7 of those lines the triage shows no value witness, because the reply reads gated inputs raw and so stays
  unknown; those 7 were ruled on the expression. Line 27 is also a model error: the reply denies the American opportunity credit when the student's
  ATIN or ITIN was applied for by the due date (p970 p. 11). Lines 28 to 30, hoh_test1 and the two EIC lines: representation.
- **asset.** cost179, model error: the reply counts property used 50% or less as section 179 property (i4562 p. 3, "used
  predominantly (more than 50%)"). (c), representation: the reply's (c) is i4562's column (c) after the reductions,
  which the project carries as 19(c). (screen), scope: the two screens refuse different property, and no amount differs. The other 13 lines:
  representation, with differences only as unknowns or refusals.

## Observations, not ruled (no bug filed)

- `fixtures/2025/defaults.json` gives `asset.bonus_same` the closed default `false` with the reason "the circumstance
  ... does not apply". But `false` is the circumstance (a mixed choice within a class). This default causes the (screen)
  value witnesses: single 2025 properties with an election out.
- `asset.screen` does not refuse an election out (`bonus_choice` none) when `bonus_same` is false. The other property in the
  class is refused on its 100% or 40% path, so the return is still refused unless that property is not entered in this tool.

## Verification

`python3 tools/transcription/check_logs.py 2>&1 | grep -E '^\[claude\] (dependent|asset|clcw_next_year|f8889):'` no
longer lists "open ruling(s) in the transcription log" for these forms. It still lists open rulings in the render logs
of clcw_next_year and f8889, a stale render log for dependent, and stale class M logs for asset, dependent and f8889.
These are outside this lane.
