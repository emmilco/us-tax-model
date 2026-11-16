# Patches older-scha (BUG-0803, 0805, 0815) and older-scha-0817a / older-scha-0817b (BUG-0817)

Lane patch-older, claude-opus-5-5, judgment, 2026-11-16. Year 2025, jurisdiction us. Base: the frozen xint
worktree. **[V]** = checked against the file named; **[I]** = inferred; **[T]** = relayed.

## Summary
- **`/tmp/nightplan/patches/older-scha.patch`** (`interview/2025/questions.yaml`, `forms/2025/sa.yaml`). This is
  wording only: BUG-0803 (gifts to foreign organizations), BUG-0805 ("substantially improve", with the Pub. 936
  gloss), and BUG-0815 (an applied refund and other withholding). No fixture changes.
- **BUG-0817 is split into two alternative patches**, because owner decision 2 is open and the structural option
  costs more than the plan estimated. Land **one** of them, after or alongside older-scha. Each applies cleanly
  with older-scha [V: applied in sequence to the base copies].
  - **`older-scha-0817a.patch`** (the plan's recommendation (a): ask the carryover of every filer). It touches
    `forms/2025/sa.yaml`, `interview/2025/questions.yaml`, `interview/2025/coverage/home.yaml` and
    `engine/src/mutate.ts`, and **fills `sa.gift_carryover: false` into 298 fixture cases**: classm.json 139,
    classm.deepseek.json 82, classm.gpt.json 5, mutation.json 72. The plan did not count this. Class M and
    mutation files take no defaults (`engine/src/fixture-inputs.ts:441-443`, `takesDefaults`) [V], so every case
    with `sa.gifts: true` would otherwise leave the line 13 refusal gate unknown.
  - **`older-scha-0817b.patch`** (option (b), wording only: one hunk on `sa.charity_limited`). It still asks two
    things in one question (N1).
- Pub. 936 (2025) is **not archived yet**. The BUG-0805 help cites it from the coordinator's fetch
  (`/tmp/nightplan/sources/p936.txt`, p. 12). Archive it, as `/tmp/nightplan/sources/README.md` describes,
  before or with this patch, or the citation points at nothing in `sources/`.

## older-scha.patch: hunks

### BUG-0803: gifts to foreign organizations
- `sa.line11` prompt: "give to charity" becomes "give to U.S. charities" (48 words; was 47).
- `sa.line11` help: adds "A U.S. charity that sends money abroad counts; a charity abroad does not." (67 words;
  was 54). The optional move of the receipt sentence into the prompt (plan item 4) was **not** made: the prompt
  is already 48 words.
- `$gift` help: adds "Leave out things given straight to a charity abroad." (28 words.)
- `sa.line11` form source: adds to the Leave-out list "gifts to foreign organizations (a gift to a U.S.
  organization that transfers funds to a foreign charity is not left out)". The cite adds the instruction's
  sentence. Source [V: sources/2025/i1040sca.txt:769-772]: "Gifts to foreign organizations. However, you may be
  able to deduct gifts to certain U.S. organizations that transfer funds to foreign charities and certain
  Canadian, Israeli, and Mexican charities." This source change goes beyond the plan, which proposed interview
  text only. It keeps the source and the prompt in step, and it makes a line-scoped transcription review due.
- **Owner decision 1 is taken as "leave out"**: a gift to a treaty-eligible Canadian, Israeli or Mexican charity
  is excluded, so the deduction is understated for those filers. State this residual on the closure.
- Sibling, not changed: the `gift.deduction` source and prompt (property gifts) do not exclude foreign
  organizations. The `$gift` help sentence covers the interview side, and the property line's source should
  follow in the same review round [I].

### BUG-0805: `sa.mortgage_other_use`
- Prompt: "...other than buying, building or substantially improving it, such as paying off other debts?" (26
  words.) The form source already says "substantially improve" [V: forms/2025/sa.yaml:1102], so it is unchanged.
- Help: "An improvement adds to the home's value, makes it last longer or adapts it to new uses; repairs such as
  repainting are other uses. Refinancing for no more than was still owed is a No. A return with limited mortgage
  interest is outside what this tool prepares; a Yes ends the interview here." (53 words; was 46.)
- Source for the gloss [V: /tmp/nightplan/sources/p936.txt, Pub. 936 (2025) p. 12, continued on p. 13]:
  "Substantial improvement. An improvement is substantial if it: • Adds to the value of your home, • Prolongs your
  home's useful life, or • Adapts your home to new uses. Repairs that maintain your home in good condition, such as
  repainting your home, aren't substantial improvements." **Cite it as Pub. 936 (2025) p. 12. It is not yet
  archived under `sources/2025/`.** The plan's "furniture" example is not used: Pub. 936 does not name it.
- The old help's "A loan used only to buy or build the home" was dropped, because the prompt now states it. "Or a
  refinancing for no more than was still owed on such a loan" is kept, shortened.
- Since the help now has its own source, consider adding a `cite` locator for p936 on `sa.mortgage_other_use`
  once it is archived. That is a form change and is not in this patch.

### BUG-0815: `sa.state_tax_other_any`
- Prompt: "...such as estimated payments (including an earlier year's refund applied to 2025) or a payment with a
  state return, or pay into a state disability or family leave fund?" (49 words; was 41).
- Help: "Count state tax taken out of anything but wages (a pension or IRA, unemployment, winnings, a 1099-NEC or
  1099-MISC); a state disability, unemployment, workers' compensation or family leave fund taken from pay (W-2 box
  14 or 19: SDI, SUI, FLI); income tax of a U.S. territory; and a state tax credit for a gift to charity that you
  applied to your tax." (62 words; was 54). Both are over N10. The current text is over as well.
- Source [V: i1040sca.txt:222 "...1099-G, 1099-R, 1099-MISC, and 1099-NEC may also show..."; :229-231 "including any
  part of a prior year refund that you chose to have credited to your 2025 state or local income taxes"]. The form
  source already covers "tax withheld from other income, estimated payments" [V: sa.yaml:503], so it is unchanged.
- The tick label is unchanged, so the screen review is not due.

## older-scha-0817a.patch (option a): hunks
1. `forms/2025/sa.yaml`, `sa.gift_carryover_if_no_gifts`: the expression becomes `op: copy, from:
   sa.gift_carryover` (technique 3.1: the id is kept, so the second refusal entry of `sa.line13` and the fixtures
   naming it are unchanged). The label is reworded. The id's "if_no_gifts" now misleads. Renaming it would touch
   `sa.line13`, the fixtures and the mutation argument, so it is left; flag it in review.
2. `forms/2025/sa.yaml`, `sa.charity_limited` (label and source) and `sa.charity_limited_if_gifts` (label): the
   carryover clause is removed. The question asks only about the 2025 income limit.
3. `interview/2025/questions.yaml`, `sa.charity_limited`: prompt "Were your 2025 gifts to charity so large that the
   law limits what you can deduct? (This can happen only when they are more than 20% of your income.)" (29 words).
   The help drops "or carried-over". `sa.gift_carryover` (a tick in group `paid_more`, seq 8) is unchanged. It is
   now reached by every filer who reaches line 13.
4. `interview/2025/coverage/home.yaml`:
   - `home.gifts_of_money` answers `sa.gift_carryover: false` and expects it in `proceeds`, in place of
     `not_asked: [sa.gift_carryover]`.
   - `home.gifts_limited`: the situation is narrowed to the income limit (its end is unchanged).
   - New row `home.gifts_and_carryover` (gifts Yes, carryover Yes, limited No), which ends `refused:
     sa.gift_carryover_if_no_gifts`. The row answers `sa.charity_limited: false` because line 13's first refusal
     entry (`charity_limited_if_gifts`) must be a known false before the second is read (spec 4.7.1, as quoted in the
     mutate.ts argument) [V: sa.yaml:1585-1596 order].
     **Unverified:** whether the walk asks `sa.line11` or `$gift` before the refusal is told. They have seq 41 and
     42, after `charity_limited` at 40. If it does, the row must answer them (interview/README.md: a question the
     row's answers opened must be answered by the row).
   - The alternative, putting the carryover refusal first on line 13, would tell it earlier (N11). It was not
     done: it changes which refusal a filer with both Yes answers sees.
5. `engine/src/mutate.ts`: removes the pinned argument `operand.sa.sa.gift_carryover_if_no_gifts.no.then1` (digest
   2b2ce17871763401). Its mutant (the `sa.no` operand of the choose) no longer exists, and a stale argument fails
   the mutation run (BUG-0630's guard) [V: mutate.ts:1922-1923; no other pin lists these premises, by grep]. The
   `copy` may generate new mutants. The mutation run will tell.
6. Fixtures: `"sa.gift_carryover": false` is inserted right after `"sa.gifts": true` in every case of
   `fixtures/2025/classm.json`, `classm.deepseek.json`, `classm.gpt.json` and `mutation.json` that lacked it (298
   cases; the files are canonical `json.dumps(indent=2, ensure_ascii=False)`, round-trip checked [V]). The
   hand-predicted effect is no value change: `sa.gift_carryover_if_no_gifts` was `sa.no` (false) for these cases
   and is now the copied false. The class M evidence notes still list the old branch names
   (`sa.gift_carryover_if_no_gifts#1`). They are left as historical. `engine/src/generate.ts:864` already sets
   `sa.gift_carryover: false` on generated cases [V], so new class M cases need nothing. The 2 deepseek/gpt
   files are dormant second-family data. They are filled only because `takesDefaults` reads every `classm*` file.

## older-scha-0817b.patch (option b): one hunk
`sa.charity_limited` prompt: "Were your 2025 gifts to charity so large that the law limits what you can deduct
(only possible above 20% of your income)? Or is a gift from an earlier year that was too large to deduct then still
carried over?" Help: adds "A carryover is shown on an earlier return that itemized, or a worksheet kept with it."
No other file changes. The carryover-only filer keeps `sa.gift_carryover` (gifts No).

## Siblings checked
- The refusal entries of `sa.line13` [V: sa.yaml:1585-1597]. `sa.charity_limited_if_gifts` is the gate of eight
  refusal entries in all, line 13's among them (lines 1495-1862). Its expression is unchanged in both options.
- Coverage rows elsewhere naming `gift_carryover`: none outside home.yaml [V: grep].
- Fixture references to `sa.gift_carryover_if_no_gifts`: classm.json 8 (evidence notes), mutation.json 2 [V].

## What to run
- older-scha: `node engine/dist/main.js test-fixtures` (expected: no change); `interview-coverage --write`, then
  check; `draft-walk` for a homeowner with a home equity loan and for a charitable giver.
- 0817a additionally: `test-fixtures` (expect the 298 filled cases unchanged; any change means a case relied on an
  unknown gate); `interview-coverage` (the new row and `home.gifts_of_money`); `tick-groups` (`paid_more` now
  reached by givers too); the mutation run for `sa` (the stale pin removed, new `copy` mutants).

## Reviews made due
- older-scha: question reviews of `sa.line11`, `$gift`, `sa.mortgage_other_use`, `sa.state_tax_other_any`;
  line-scoped transcription of `sa.line11` (source); screen and false-no samples of gate
  `sa.has_mortgage_interest` (prompt changed); false-no samples of `sa.gifts` and `sa.state_tax_other_any`.
- 0817a: line-scoped transcription of `sa.gift_carryover_if_no_gifts`, `sa.charity_limited`,
  `sa.charity_limited_if_gifts`; screen and false-no samples of gates `sa.charity_limited_if_gifts` and
  `sa.gift_carryover_if_no_gifts`; question reviews; the coverage report.
- 0817b: the question review and the false-no sample of `sa.charity_limited`.

## Closure entries to record when these land
`Closes=BUG-0803` (residual: the treaty charities, decision 1), `BUG-0805` (evidence: Pub. 936 p. 12, once
archived), `BUG-0815`, and `BUG-0817` (fixed under (a); under (b), record the two-subject residual or "in part").
