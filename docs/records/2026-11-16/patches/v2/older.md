# older v2: corrected patches older-ny, older-credits, older-scha, older-scha-0817a, older-scha-0817b

Lane v2-older. claude-opus-5-5, judgment, year 2025, us and ny. Written 2026-11-16. Read only on the repository.
Base: the frozen xint tree. The round-2 `a/` copies were byte-compared with xint before use (all equal). Edits were
made on copies in `/tmp/nightplan/scratch/older-v2/<lane>/b/`, and patches written with `git diff --no-index`
(paths rewritten to the repo root). Round-2 files are untouched.
**[C path:line]** = checked against that file in this session. **[I]** = inferred. **[T]** = relayed from another
lane's file, not re-read. Word counts use the engine's rule (`engine/src/tick-groups.ts:22`: whitespace tokens holding
a letter or digit), computed by script on the parsed YAML. Round-2 counts were plain whitespace splits, so a few
"before" figures below differ from the round-2 tables by one or two words.

## Summary

- **Five patches in `/tmp/nightplan/patches/v2/`.** Each passes `git apply --check` on a copy of the xint files. All
  five also apply in sequence on a scratch copy (ny, credits, scha, then 0817a; and separately ny, credits, scha, then
  0817b). Every YAML and JSON file touched parses after the sequence. No engine, walk, fixture run or model call was
  made (COMMON.md forbids them).
- **BUG-0815 (red-team A7)** is applied. W-2 box 14/19 is gone from the help. Box 19 is already in the
  withheld-from-pay amount: `sa.line5a` reads "boxes 17 and 19 of each Form W-2" [C forms/2025/sa.yaml:514, 518]. The
  state unemployment fund is now in both the help and the prompt [C sources/2025/i1040sca.cols.txt:85]. The prompt
  says "estimated payments made in 2025" [C i1040sca.cols.txt:84].
- **BUG-0851 (A8)** is applied. The current `529_nonqualified` prompt is restored byte for byte, so K-12 tuition stays
  asked in the prompt. The July 4 and eligible-school condition, the loan limit, and the transfer guard move into
  help.
- **BUG-0861 (A12)** is applied. The help gives the combined-income test for a dependent who is 65 or older or blind,
  and for one who is both.
- **N10.** Of the eleven figures in the round-2 credits table (42 to 53 words), eight are now about 40 or under. Two
  are 43 and 44, each held by a guard. The table below gives each one.
- **BUG-0790 is not in any of these patches.** That is as the brief asks: no `asset.*` line is touched [C grep of
  the five patches]. **Conflict to settle at merge:** `/tmp/nightplan/patches/sche-a.patch` (hunk at
  `interview/2025/questions.yaml` @5603, `asset.listed`) names a boat in the listed-property question. That is the
  med-k1sche version, which the red team rejects (A11), because it computes a boat used over 50% in business,
  including a yacht used for entertainment. The red team recommends the med-older version: refuse every boat through
  `asset.kind_excluded`. Only one lane should land 0790. sche-a.md (lines 24 and 180) records its choice as owner
  decision D4.
- **0817a and 0817b are byte-identical to round 2.** No red-team finding touches them (section E lists 0817(a) as
  sound). They were re-checked against the v2 older-scha patch.
- **BUG-0850 re-derivation:** both fixture values agree with round 2. There is no difference (section 4).

## 1. Changes by patch

### older-ny.patch (3 files)
- Unchanged from round 2: the `ny_it201.yaml` 0850 hunks (`dis_pension_wages`, `gov_pension_candidate`, the two
  re-gated items, the note), the `ask.ny_529` source and label, the `ask.ny_529` help, and the two fixtures.
- **Changed (A8): `ny_it201.ask.529_nonqualified`.**
  - Prompt: the current text is restored, "In 2025, did you take money out of that New York 529 account for anything
    but college, career training or student loans? School tuition before college and a move to another state's plan
    count." (34 words). The patch has no hunk on it now.
  - Help (53 words): "Career training is No only if paid from July 4, 2025, to a college or other eligible school; loans only
    if the student's or a sibling's. A Roth IRA or ABLE rollover, money taken out because the student died or became
    disabled, and a move between family members' New York accounts are No."
  - Sources [C sources/ny/2025/ny_it201i.txt]:
    - credentialing "at an eligible educational institution on or after July 4, 2025", and credentialing "not paid
      to an eligible educational institution" is nonqualified;
    - loans of "the designated beneficiary or a sibling";
    - the Roth IRA and ABLE rollovers, and "the result of the death or disability". "Because" follows this; the red
      team's "after" does not;
    - transfers between family accounts are "not considered distributions" (the Note).
  - The 4 K-12 lines are in the right column of the same page.
  - **N10 not met (53, aim about 40).** Getting to about 40 means dropping the family-transfer sentence (about 43) and
    one more guard. Each sentence guards a wrong value:
    - the career-training and loan clauses guard a wrong No, which misses the line 22 addition;
    - the rollover, death and transfer clauses guard a wrong Yes, which overstates the addition.
  - The red team accepted about 55 words to keep the transfer sentence. Owner's call.

### older-credits.patch (4 files)
- Unchanged from round 2:
  - `forms/2025/dependent.yaml`, `eic.yaml` and `f5695.yaml`;
  - `eic.lived_with_relative` help, `f5695.panel` tick and `f5695.line21a` prompt (all under the limits);
  - the BUG-0796 and 0793 hunks apart from `f5695.any`.
- Changed, by input:

| Input | Field | Base | R2 | v2 | v2 text |
|---|---|---|---|---|---|
| f8863.ban | help | 62 | 51 | 38 | "Answer No only if, after the denial or bar, you filed Form 8862 for this credit with a later year's return and it was allowed. A bar running out is not enough. A Yes ends the interview here." |
| household.credit_disallowed | prompt | 41 | 46 | **43** | "Has the IRS ever reduced or refused a child tax credit (including the additional one), a credit for other dependents or an earned income credit that you (or, on a joint return, your spouse) claimed, except to fix a math or clerical error?" |
| household.credit_disallowed | help | 39 | 43 | 40 | "Count any earlier return, including a joint one with someone else, and a credit taken back after an IRS request for proof or an audit, even if you agreed. If in doubt, answer Yes. A Yes ends the interview here." |
| person.rmd_missed | prompt | 36 | 42 | 36 | "For this person (you, or your spouse on a joint return) — Did you take less than the required amount out of a retirement account by a 2025 deadline, even if you made up the shortfall later?" |
| person.rmd_missed | help | 36 | 42 | 35 | "This includes a yearly minimum (at 73 or older, or on an inherited account), a first amount due April 1, 2025, and emptying an inherited account by its deadline. A Yes ends the interview here." |
| dependent.ptc_files | prompt | 47 | 53 | 40 | "Did this dependent have to file a 2025 return because of their own income: over $1,350 not from work, such as interest, or over $15,750 of pay (a taxable scholarship is pay)? Filing only for a refund does not count." |
| dependent.ptc_files | help | 40 | 46 | **44** | "With both kinds, they must file when the total is over the larger of $1,350 and their pay (up to $15,300) plus $450. If 65 or older or blind, $3,350, $17,750 and $2,450 replace $1,350, $15,750 and $450 ($5,350, $19,750 and $4,450 if both)." |
| f5695.any | help | 34 | 45 | 41 | "Count work finished in 2025, work on a new or rebuilt home you moved into in 2025, and your share of work paid by a condo association or co-op. A panel, wiring or energy audit counts. If in doubt, answer Yes." |

- **Refusal sentence.** "A Yes is outside what this tool prepares and ends the interview here" becomes "A Yes ends the
  interview here." That is the bank's usual form (103 uses against 12) [C xint interview/2025/questions.yaml, grep].
- **BUG-0861 (A12) values** [C sources/2025/i1040gi.cols.txt:163-166, Chart B, single dependents].
  - 65 or older or blind: unearned over $3,350, earned over $17,750, or gross over the larger of $3,350 and earned
    (up to $15,300) plus $2,450. For one who is both: $5,350, $19,750 and $4,450.
  - "Replace" carries $3,350 into both places $1,350 stands (the unearned limit and the floor of the combined test),
    which is what the chart says.
  - The red team's own example now gets the right answer: $3,000 not from work and $1,000 of pay. $4,000 is more than
    the larger of $3,350 and $3,450, so the dependent must file, and the help says so.
  - **44, not 40.** The 39-word form ("If 65 or older or blind: $3,350, $17,750 and $2,450 ...") leaves the reader to
    work out that $3,350 is also the floor of the combined test. A wrong reading gives a false Yes, which overstates
    household income on Form 8962. The four words are kept for that reason.
  - Married dependents are still left to the form source (rare; noted in round 2).
- **`household.credit_disallowed` prompt at 43** (the base is 41).
  - The ACTC clause ("(including the additional one)", 4 words) is the round-2 plan's guard. The spouse phrase is
    the fixed 7 words.
  - The only way under 40 is to drop the ACTC clause. Who would answer No wrongly then: a filer whose only
    disallowance was the ACTC and who does not read it as "child tax credit" [I]. It is kept.
- **`dependent.ptc_files` prompt.** "a 2025 return" replaces "a 2025 tax return", and the interest/dividends list
  shrinks to "such as interest". These are the cuts that brought it to 40. "Not from work" still covers dividends,
  unemployment and pensions; Chart B's "unearned income" lists them [C i1040gi.cols.txt:163].
- **`person.rmd_missed` prompt.** Back to the base wording, with "the required yearly minimum ... by its deadline"
  changed to "the required amount ... by a 2025 deadline". The help says which amounts. This keeps the plan's
  i5329 "2025 deadline" rule [T round-2 md: i5329.txt:640, not re-read] and the made-up-later guard.

### older-scha.patch (2 files)
- Unchanged from round 2: the 0803 hunks (`sa.line11` source, prompt and help; `$gift` help) and the 0805 prompt.
- **BUG-0815, `sa.state_tax_other_any` (A7):**
  - Help (43 words): "Count tax taken out of a pension, IRA, unemployment pay, winnings, 1099-NEC or 1099-MISC; a state
    disability, unemployment or family leave fund from pay (SDI, SUI, FLI); U.S. territory income tax; a state tax
    credit for a charity gift, applied to your tax." The base is 54 and R2 62.
  - Prompt (49 words): "In 2025, did you (or, on a joint return, your spouse) pay state or local income tax another way, such
    as estimated payments made in 2025 (or a past refund applied to 2025) or with a state return, or pay into a state
    disability, unemployment or family leave fund?" The base is 41 and R2 about 49.
  - Left out:
    - the A7 help's "a past refund applied to 2025", because the prompt carries it;
    - the Washington supplemental workers' compensation fund (as in A7; rare). The amount question
      `sa.state_tax_other` still lists it [C xint questions.yaml:1491].
  - **The tick is unchanged** ("Paid other state or local income tax, or a state disability fund", 12 words, at the
    tick limit) [C engine/src/tick-groups-check.ts:123]. Adding "unemployment" takes it to 14. The only cuts that
    fit drop "or local" or "disability", and CA SDI is the common case.
    - **Residual:** a PA or AK worker whose only state payroll fund is SUI reads only the tick and may answer No.
      Line 5a is then understated by that SUI. The amount is small [I: PA's employee rate is a fraction of a percent;
      no archived source].
    - Because the tick is unchanged, no screen review falls due.
  - **The prompt is over N10** (a parent; aim 25; the base is already 41). It is shown only where the question stands
    alone, outside the tick screen. "Made in 2025" and the unemployment fund were asked for, and each adds words.
- **BUG-0805 help, trimmed:** "...Refinancing for no more than was still owed is a No. A Yes ends the interview here."
  It goes from R2 53 to 41. Only the refusal sentence is shortened.
- **Not trimmed:** the `sa.line11` help (0803) at 67 words (the base is 54), and its prompt at 48. Both are outside
  the brief's table. The base text is already over the limit, and trimming it would rewrite reviewed guards. The plan
  offers moving the receipt sentence into the prompt (round-2 md).

### older-scha-0817a.patch and older-scha-0817b.patch
- Byte-identical to round 2 (`cmp`). They still apply after the v2 older-scha (checked in sequence).

## 2. Red-team findings and where each went

| Finding | Touches | Applied |
|---|---|---|
| A7 (0815: box 19, SUI, "made in 2025") | older-scha | yes. The tick residual is noted above |
| A8 (0851: K-12 in the prompt) | older-ny | yes, with the full guard set at 53 words |
| A12 (0861: 65+/blind combined test) | older-credits | yes, plus the both-65-and-blind figures |
| A11 (0790) | none of these | left out; the conflict with sche-a is noted |
| D (N10 overruns for 0815, 0861, 0862, 0870) | credits, scha | see the tables |
| D (0803 prompt 48, help about 66) | older-scha | not changed (outside the brief's table) |
| E (0793, 0796, 0797, 0805, 0817(a), 0862, 0870, 0850 sound) | all | kept |

## 3. What to run (when the machine is free), and reviews due
- `node engine/dist/main.js test-fixtures` and `test-fixtures --ny`. No value change is expected apart from the two
  new NY cases.
- `interview-coverage --write`, then the check: the changed wording is quoted.
- `tick-groups`: no tick changed in v2.
- `draft-walk` for an NY 529 owner, a PTC household with a dependent 65 or older, and a Schedule A filer with
  estimated state payments.
- Question reviews: every input in the tables above. Transcription reviews as in round 2; v2 changes no form source.
  The screen and false-no samples are as in round 2. `sa.state_tax_other_any`'s tick is unchanged, so no screen
  sample falls due for it.

## 4. BUG-0850: the fixture values re-derived from the expressions (read only)

I traced the patched expressions on the two cases' inputs. Defaults are from `fixtures/ny/2025/defaults.json` and
`fixtures/2025/defaults.json`. it201.json takes defaults [C engine/src/fixture-inputs.ts:441-443].

Federal:
1. `retirement.disability_if_plan`: the account is "plan", not an IRA, so it reads `disability` = true. Then
   `dis_early_if_disability` = true, `dis_all_early_if_early` = true, and `dis_wages` = true
   [C forms/2025/retirement.yaml:542-662].
2. `retirement.taxable` = `plan_taxable`. With no after-tax cost [I: `annuity_if_cost` false by default, not
   traced], it is `plan_simple` = box1 − `plan_excluded`. That is $18,000, with box5 = 0 and rollover_any = false
   [C defaults.json] [C retirement.yaml:2248-2300].
3. `person.dis_wages` = $18,000 [C person.yaml:1941-1953]. `person.plan_taxable` leaves out dis_wages items, so
   line 5b = $0 [C person.yaml:1918-1934]. There is no IRA, so line 4b = $0.
4. `f1040.line1z` = 1a ($38,000 + $40,000) + 1h ($18,000) = $96,000 [C forms/2025/f1040.yaml:81, 192, 203]. Line 9 =
   line 11a = $96,000. That assumes no interest amount (bank_a has none) and no adjustments [I: defaults to zero].

New York [C forms/ny/2025/ny_it201.yaml:454-970, with the patch's new items]:
5. Lines 9 and 10 = $0, so `has_pension_income` = false. `dis_pension_wages` = $18,000, so `gov_pension_candidate`
   = true.
6. **Case `ny.gate.pension_disability_wages`.** `ask.gov_pension` = true, so `gov_pension_if_income` = true,
   `gov_pension_any` = true, and `gate.line26` = true. **line26 = refusal at `ny_it201.gate.line26`** (form "Form
   IT-201 line 26", remedy "...(decision B4).").
   - **Agrees with round 2.**
   - On the unpatched tree, `gov_pension_if_income` is `no` here. The gate is then false, so this case fails
     without the patch, which is the point of a regression case.
7. **Case `..._not_gov`.** `ask.gov_pension` = false, so `gov_said_no` = true (candidate true, if_income false).
   `gov_pension_other_if_no` then asks `ask.gov_pension_other` = false, so `gov_pension_any` = false. **line26 =
   `ny.zero` = $0.**
8. **line29 = $0.** `gate.line29` takes the second branch (has_pension_income false), which is `ny_it201.no`
   [C :913-917]. The line is `ny.zero` with no refusal.
9. **line33 = $96,000.** Line 1 = $96,000 and lines 2 to 16 = $0, so line 17 = line 19 = $96,000 (line 18 =
   `s1.line26` = 0). The additions 20 to 23 are all `ny.zero`, and none refuses:
   - line 20: no tax-exempt interest;
   - line 21: `ask.public_job` defaults false;
   - line 22: `x_edu_account` defaults false;
   - line 23: `ask.it225` defaults false.

   So line 24 = $96,000. The subtractions 25 to 31 are all $0:
   - line 25: line 4 = 0 and Schedule 1 line 9 = 0;
   - line 26: as above;
   - line 27 = line 15 = 0;
   - line 28: no interest or dividends;
   - lines 29 to 31: as above, or defaults.

   Line 32 = 0, so line 33 = $96,000. **Agrees with round 2.**
- **No difference found.** [I] marks the two places resting on defaults not traced: `annuity_if_cost` and a zero
  interest amount. The round-2 witness run (`/tmp/xrel/ny/dis_out.json`) supports both. I did not open it, to keep
  this derivation independent.
- **Side note (not a value):** in case 2, `ask.gov_pension` and `ask.gov_pension_other` are not read on the unpatched
  tree. If test-fixtures flags unread inputs, that case only passes with the patch, which is as intended [I].

## 5. Files
- Patches: `/tmp/nightplan/patches/v2/older-ny.patch`, `older-credits.patch`, `older-scha.patch`,
  `older-scha-0817a.patch`, `older-scha-0817b.patch`.
- Working copies and scripts: `/tmp/nightplan/scratch/older-v2/` (`edit.py`, `edit2.py`, `count.py`; `seq-0817a`
  and `seq-0817b` are the applied-in-sequence copies).
- The round-2 closure-record drafts (BUG-0629, BUG-0092 in older-ny.md; per-bug closures in the others) still stand.
  The 0861 closure residual is now only "married dependents". The 65+/blind combined test is fixed.
