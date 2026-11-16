# Patch older-credits: BUG-0797, 0862, 0870, 0793, 0861 (wording), 0796

Lane patch-older, claude-opus-5-5, judgment, 2026-11-16. Year 2025, jurisdiction us. Base: the frozen xint
worktree (copies in `/tmp/nightplan/scratch/older-credits/a/`). Patch: `/tmp/nightplan/patches/older-credits.patch`
(4 files: `interview/2025/questions.yaml`, `forms/2025/eic.yaml`, `forms/2025/dependent.yaml`,
`forms/2025/f5695.yaml`). `git apply --check` passes, and it applies in sequence with the other older-* patches.
All four YAML files parse after the change [V]. **[V]** = checked against the file named; **[I]** = inferred.

## Summary
These are wording-only changes (prompts, help, a tick, and four form `source` fields). No expression, gate, id
or default changes, so no fixture changes value. Every input keeps its meaning or widens it in the safe
direction. Defaults taken where the plan left an owner decision open:
- BUG-0797: keep "you" (decision 5 is open).
- BUG-0861: wording, not a computed Chart B (decision 4 is open).
- BUG-0862: the year detail (1997 and 2016) is dropped from help. The form source keeps it.

Word counts are whitespace-split, counted by script on the parsed YAML:

| Input | Field | Before | After | Note |
|---|---|---|---|---|
| f8863.ban | help | 62 | 51 | |
| household.credit_disallowed | prompt | 41 | 46 | |
| household.credit_disallowed | help | 39 | 43 | |
| person.rmd_missed | prompt | 37 | 42 | includes the fixed 9-word frame |
| person.rmd_missed | help | 36 | 42 | |
| eic.lived_with_relative | help | 18 | 29 | prompt (form source): 31 to 30 |
| dependent.ptc_files | prompt | 47 | 53 | over the aim, see 0861 |
| dependent.ptc_files | help | 40 | 46 | over the aim, see 0861 |
| f5695.any | help | 34 | 45 | the plan accepted 45 |
| f5695.panel | tick | 9 | 12 | at the 12-word tick limit |
| f5695.line21a | prompt | 20 | 22 | |

## Hunks, in the plan's order

### BUG-0797: `f8863.ban` help (questions.yaml, order 242)
New: "Answer No only if, after the denial or bar, you filed Form 8862 for this credit with a later year's return and
the credit was allowed. The end of a bar alone does not make the answer No. A Yes is outside what this tool
prepares and ends the interview here."
- Source: i8862 exceptions, "(a) you filed Form 8862 (or other documents) and your credit was then allowed, and
  (b) your credit has not been reduced or disallowed again..." Its "Do not file Form 8862 for the: 2 years ... 10
  years" means those years refuse the credit outright. The end of a ban is not listed as an exception
  [V: sources/2025/i8862.txt:60-92].
- The form source `f8863.ban` (forms/2025/f8863.yaml:256-259) already states the rule correctly. It is unchanged.
- Spouse: kept as "you" (owner decision 5). The entry should note that i8862 is silent on a spouse's earlier
  denial on a joint return.

### BUG-0862: `household.credit_disallowed` prompt and help (questions.yaml, order 310)
- Prompt: "Has the IRS ever reduced or refused a child tax credit (including the additional child tax credit), a
  credit for other dependents or an earned income credit that you (or, on a joint return, your spouse) claimed,
  other than to fix a math or clerical error?"
- Help: "Count any earlier return, including a joint return with someone else, and a credit taken back after an IRS
  request for proof or an audit, even one you agreed to. If you are not sure, answer Yes. A Yes ends the interview
  here."
- The form source already names the ACTC (`forms/2025/household.yaml:748-752`) [V], so it is unchanged.
- The entry's "only an arithmetic or missing-SSN notice is a math error" is left out: no archived source defines
  the term (per the plan's grep). That an audit disallowance is not a math or clerical error is inferred from the
  phrase [I].

### BUG-0870: `person.rmd_missed` prompt and help (questions.yaml, order 180 seq 25)
- Prompt: "For this person (you, or your spouse on a joint return) — Was any amount you had to take out of a
  retirement account by a 2025 deadline not taken out in full by then, even if you made it up later?"
- Help: "This includes a yearly minimum (at 73 or older, or on an inherited account), a first amount due April 1,
  2025, and emptying an inherited account by its deadline. A Yes is outside what this tool prepares and ends the
  interview here."
- Source: i5329, Part IX: the tax is "due for the tax year that includes the last day by which the minimum
  required distribution must be taken" (per the plan, `i5329.txt:640`). A "2025 deadline" is that rule. A first
  distribution due April 1, 2026 is correctly outside it.
- The plan's "5-year or 10-year deadline" was shortened to "by its deadline". No 10-year deadline can fall in 2025
  (the rule applies to deaths after 2019) [I: from the statute's dates, not checked in an archived source].
- The form source (`forms/2025/person.yaml:7389-7392`) is neutral and unchanged.
- The QDRO alternate-payee clause (the entry's item 3) is not added: p590b is not checked.

### BUG-0793: `eic.lived_with_relative` (eic.yaml source, which is the prompt; questions.yaml help)
- Source and prompt: "In 2025, did you live for more than half the year in the same home as a parent,
  grandparent, brother, sister, aunt or uncle, counting step, half and foster relatives?"
- Help: "Great-grandparents, great-aunts and great-uncles count. Time either of you was away for a while, such as
  at school, counts as time together. If you are not sure, answer Yes."
- Source: i1040gi p. 41, Step 3 ("...stepbrother, stepsister, half brother, half sister, or a descendant of any of
  them") and its temporary-absence rule (per the plan, `i1040gi.txt:763-788, 923`). The temporary-absence clause
  moves from the source into help. That is a judgment: the reviewer may want it kept in the source.
- Including "foster" siblings is wider than the rule. That is safe, because a Yes only asks
  `eic.qc_of_another`. The birth and death exception is left out (the plan's judgment; "If you are not sure,
  answer Yes" covers it).

### BUG-0861: `dependent.ptc_files` (dependent.yaml source; questions.yaml prompt and help), wording option
- Prompt: the current text plus "(a taxable scholarship counts as pay)".
- Help: "With both kinds, they must file if the total is over the larger of $1,350 and their pay (up to $15,300)
  plus $450. Limits are higher for a dependent 65 or older or blind: $3,350 not from work, $17,750 of pay ($5,350
  and $19,750 if both)."
- Form source: the single, under-65, not-blind figures are now introduced as that case, with "earned income, which
  includes taxable scholarship and fellowship grants". It adds "higher limits for a dependent 65 or older or
  blind, and other limits for a married dependent". The cite adds the Chart B quotes.
- Source [V: sources/2025/i1040gi.txt:471-500]: "Earned income includes salaries, wages, tips, professional fees,
  and taxable scholarship and fellowship grants"; single dependents 65 or older or blind: "$3,350 ($5,350 if 65 or
  older and blind)" and "$17,750 ($19,750 if 65 or older and blind)".
- **Residual (state on the closure):** the combined-income test for a dependent 65 or older or blind uses $2,450
  ($4,450), not $450. The help gives only the under-65 version, so a 65+ dependent with both kinds of income can
  over-answer Yes, which understates the PTC. Married dependents (the $5 rule and their own limits) are left to
  the source wording. Both are rare. The computed option (decision 4) removes them.
- The self-employment point is settled (D7(b), `amb.2025.ptc_dependent_filing`, Chart B only). Cite it on the
  closure.

### BUG-0796: Form 5695 (questions.yaml `f5695.any` help, `f5695.panel` tick, `f5695.line21a` prompt; f5695.yaml sources)
- `f5695.any` help: "Count work finished in 2025, and work in a home built or rebuilt that you first lived in
  during 2025. Count your share of work a condo association or housing co-op paid for. A panel, wiring or energy
  audit counts. If in doubt, answer Yes." Source [V: sources/2025/i5695.txt:58-59 (reconstruction, "when your
  original use of the reconstructed home begins"), :82-83 (condo association / co-op), :184 (Part II: "in your main home that you owned during 2025 ... if the original use of the
  component begins with you")]. The construction-timing rule for Part I is relayed from the entry's i5695 p. 1 quote, not re-read here [T]. This is wider than Part II for new construction, which is harmless at a gate
  (`f5695.b_new_home` sits below it, per the plan).
- `f5695.panel` tick: "An electrical panel, circuits or wiring, put in in 2024 or 2025". Its form source:
  "Did that include an electrical panel, circuits or wiring, put in in 2024 or 2025?" Source [V: i5695.txt:440-447,
  "If the enabling property and the enabled property were installed in consecutive tax years, then you can treat
  both as having been installed in the later of the tax year..."]. A 2024 panel with no 2025 enabled item reaches
  `line25a` and is answered No there, so no credit is given [V: f5695.yaml line25a source]. The reverse case (a 2025
  panel enabling a 2024 item) stays unasked. Note it on the closure.
- `f5695.line21a`: the prompt ends "...that you lived in during 2025?". The form source reads "that you used as a
  residence during 2025". The form label (the printed line text) is unchanged. Source [V: i5695.txt:208, "you used
  during 2025 located in the United States"].

## Siblings checked
- `f8863.ban` and `household.credit_disallowed` are the two Form 8862 screens. Both are fixed here.
- The other `eic.*` relationship screens: only `eic.lived_with_relative` names relatives [I: no other source in
  eic.yaml lists relatives, by grep of "grandparent"].
- `f5695.line25a` already carries the consecutive-year choice [V]. `f5695.condo` and `f5695.construction_later`
  are unchanged (they sit below a Yes).
- `person.rmd_missed`: its gate `person.rmd_possible` is not changed. Whether that gate reaches a filer under 73
  who has only a first distribution due April 1, 2025 (someone who turned 73 in 2024) is **not checked**.

## Fixtures
None change: no expression changes. Inputs read by fixtures, per the plan: `eic.lived_with_relative` (8
files), `household.credit_disallowed` (11), `f5695.any` (12), `dependent.ptc_files` (1). Their recorded answers keep
their meaning.

## What to run
`node engine/dist/main.js test-fixtures` (expected: no change); `interview-coverage --write`, then check (the
wording is quoted); `tick-groups` (the panel tick is 12 words, at the limit); `draft-walk` for an EIC filer without
a child and for an energy-credit filer.

## Reviews made due (line-scoped, one per form per round)
- Transcription: `eic.lived_with_relative`, `dependent.ptc_files`, `f5695.panel`, `f5695.line21a` (sources changed).
- Question reviews: all eight inputs.
- Screen and false-no samples: gates `eic.lived_with_relative`, `dependent.ptc_files`, `f5695.any`,
  `f5695.panel_if_any`, `f5695.line21a`. False-no only: `f8863.aoc_claimed`, `household.claims_8862_credit`,
  `person.rmd_possible`.

## Closure entries to record when this lands
One pending closure per bug (`Closes=BUG-0797` and so on, `Closure=fixed`). Record "in part" for BUG-0861 if the
owner later chooses the computed option. The residuals to name: 0797 (spouse silence), 0861 (65+ combined test,
married dependents), 0796 (a 2025 panel for a 2024 item), 0870 (QDRO alternate payee).
