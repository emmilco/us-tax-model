# int-amt.patch: tax-exempt interest asked as a yes/no box (plan-interview item 1)

Lane patch-interview, claude-opus-5-5, judgment, 2025, us. Made from copies of xint (frozen tree, about 00:30
2026-11-16); nothing in xint was written. No build, walk, check or model call was run. Labels: **[C path:line]**
checked against that file; **[I]** inferred, not run.

## Summary

- New input `f1040.tax_exempt_any` (Bool, gate) and gate line `f1040.tax_exempt_interest_if_any` (`choose`: the
  amount when Yes, `div.zero` when No), copying the `f1040.estimated_any` / `f1040.line26_if_estimated` pattern
  [C forms/2025/f1040.yaml:986-1003, 1144-1166]. `f1040.tax_exempt_interest` gains `gated_by`. Its four readers
  (`f1040.line2a`, `s2.amt_pab_ask`, `s2.amt_pab_over`, `s2.amt_h_extra`) read the gate line instead. No other
  form, profile target or tool reads the amount [C grep of forms/, interview/, engine/, tools/].
- Bank: new tick group `interest_dividends` (`f1040.tax_exempt_any` seq 1, `div.any` seq 2, order 272). The amount
  moves from order 271 to 272 seq 3, its prompt loses the example (now on the box). The rest of order 272 is
  renumbered +2 in its present order.
- Fixtures: one default, one inserted line per case that states the amount (782 cases), the engine case generator,
  four personas and six coverage files. No expected value and no expected end is edited.
- **Answer to the brief's question: the runner accepts an input behind a gate answered No, and silently ignores it.**
  Details below; this is why every case with a non-zero or withheld amount must state the box as true.

## The runner and an input behind a closed gate [C]

- `validateInputs` checks only that each key is a declared input of a listed entry and that its value has the
  input's type. It does not look at gates [C engine/src/eval.ts:843-873].
- The fixture runner (`test-fixtures`) passes each case's resolved inputs to `eval` and compares only the
  expected values [C engine/src/fixtures.ts:48-75].
- Before that, `applyDefaults` gives every unstated input its default, gated or not, and the defaults check
  requires a default for every input template [C engine/src/fixture-inputs.ts:9-18, 281-316]. So the amount must
  keep its default (0) after it is gated, and every default-taking case carries an amount behind the box.
- The gate line is a `choose`: with the box false it takes `div.zero` and never reads the amount
  [C engine/src/eval.ts:660-690]. Nothing reports the unread amount. (Interview-side checks do: `interview-rules`
  throws on asking an input behind a closed gate, and the walks fail on a stale answer
  [C engine/src/interview-rules.ts:359; interview/README.md:801-802].)
- Consequence: a case that states a non-zero amount and takes the box's default (false) would have its amount
  dropped. Its expected values would then fail. They would not pass wrongly, but the failure would point at
  the wrong cause. Hence `true` in those cases.
- Precedent: no fixture states a non-zero `f1040.line26` without `f1040.estimated_any: true` [C python scan of
  fixtures/2025, fixtures/ny/2025].
- The class M and mutation files take no defaults [C fixture-inputs.ts:19, 441-443]. A case there that states the
  amount but not the box would leave the gate unknown, and with it line 2a and every reader. So the box is stated
  in each of them (the g1-f6 precedent for `sd.qof` [C docs/provisional/lanes/g1-f6.md:10-14]).

## Hunks

| File | Change |
|---|---|
| forms/2025/f1040.yaml | `f1040.tax_exempt_any` (input, Bool). `gated_by` on the amount. Gate line `f1040.tax_exempt_interest_if_any` after it. `line2a` reads the gate line. Cites copy the amount's locator. |
| forms/2025/s2.yaml | Three reads changed to `f1040.tax_exempt_interest_if_any` (lines 209, 239, 736). |
| interview/2025/questions.yaml | Group `interest_dividends`, heading "In 2025, did you (or, on a joint return, your spouse) get either of these?" (15 words). Box `f1040.tax_exempt_any`: order 272, seq 1, tick "Tax-exempt interest, such as from a city or state bond" (10 words; the plan says 9 but hyphenated words count once). Box help (26). `div.any` joins the group: seq 2, tick "Shares or a fund outside a retirement account, or a Form 1099-DIV" (12, at the cap); help unchanged. Amount: order 271 → 272, seq 3. New prompt "How much tax-exempt interest did you (or, on a joint return, your spouse) get in 2025? Zero if none." Help unchanged. `sb.ordinary_dividends`, `f1040.line3a`, `sd.distributions`, `qbi.dividends`, `div.box12`, `div.other_boxes`, `div.box2b`..`div.box13`, `div.basis_reconciled`, `sd.f2439`: seq +2 (2..18 → 4..20). |
| fixtures/2025/defaults.json | `f1040.tax_exempt_any: false`, reason "Closed: …" (the text `div.any` uses). The amount's default 0 stays (required). |
| fixtures (inserted line `"f1040.tax_exempt_any": …,` before each stated amount, no reformatting) | Default-taking files. **true** where the amount is non-zero: ssb 1, f1040 1, f8962 1, s2 6, ny it201 1. **true** where the amount is withheld (null): eic 1, f1040 3, f2441 1, f4952 2, person 1, s179 1, s1a 2, s3 4, sd 1. **false** where it is 0: ny it201 5. No-default files: classm.json 318 false + 1 true (`classm.f8962.9`); classm.deepseek 94 false; classm.gpt 6 false; mutation 148 false; ny classm 53, ny classm.deepseek 54, ny mutation 106, all false. |
| tools/engines/generate_cases.py | `"f1040.tax_exempt_any": False` beside the amount in the generator's base inputs. The generated returns state every input, so without it line 2a would be unknown in every engine-differential return [I]. |
| personas 03, 04, 07, 08 | `f1040.tax_exempt_interest: 0` → `f1040.tax_exempt_any: false` (the amount is no longer asked, so the old answer would be stale). |
| coverage care (set low_earner), marketplace (set one_form), mfs (`mfs.ssb_apart_all_year`), retirement (`ssb.ordinary`) | Amount 0 → box false (stale-answer rule [C engine/src/interview-coverage.ts:269-276, 348]). |
| coverage other (`other.amt_pab`), ny (`ny.other_state_bonds`) | Box true added before the amount. |

### Why `true`, not `null`, for the withheld cases

`sales.loss.mfs.0` expects `eic.check_27c` = `{"kind":"unknown","reason":"no input supplied for
f1040.tax_exempt_interest","input":"f1040.tax_exempt_interest"}` [C fixtures/2025/sd.json:320-343].
- With the box `true`, the gate takes the amount, which is still withheld. The unknown is the same object, so the
  expected value stands unedited [I: the gate passes the operand's value through, eval.ts:683-686].
- With the box `null`, the unknown would name `f1040.tax_exempt_any`: an expected-value change.
- With the default `false`, the line would become known: also a change.
The other 16 withheld cases expect refusals or known values and have no tax-exempt text in their expectations
[C scan]. `true` keeps their evaluation identical too, for the same reason.

## Hand-predicted values

No new fixture and no new coverage row. Every existing expected value should be unchanged [I]:
- box true: `if_any` = the amount;
- box false and amount 0: `if_any` = 0 = the old amount;
- withheld: same unknown.

## Siblings checked

- Readers of the amount: only the four above [C grep forms/2025, forms/ny]. NY reads `f1040.line2a`, not the
  amount. The 2026 forms are not on this tree.
- `research/ty2026/forms-proposed/f1040.yaml:92,110` declares and reads `f1040.tax_exempt_interest`. The 2026
  adoption should carry the same gate [I; not edited, outside the 2025 tree].
- Tick-group build rules [C interview/README.md:582-600]:
  - 2 members, both yes/no;
  - labels ≤ 12 words, heading ≤ 25;
  - one order;
  - no other order-272 `seq` between 1 and 2;
  - two once-per-return forms, neither a list's form;
  - neither member's gate reads the other. `div.any` is read by `div.*_if_dividends`; `f1040.tax_exempt_any` by
    its own gate.
- `interview/2025/gate_frequencies.yaml` has an `interest` situation that already counts tax-exempt interest
  [C :184-195]. No new entry is required. One for the box (6,893,860 of 160,602,107 returns, 4.3%) is optional.

## What to run (in a lane worktree, after applying)

1. Build (gate conventions, tick-group build rules, defaults check).
2. `test-fixtures`, federal and `--ny`. Expect 0 failures and no edited expectation.
3. `interview-coverage`: the six restated rows keep their ends. Regenerate `reports/2025/interview_coverage.md`.
4. `tick-groups`: the new screen shows both boxes for the background return.
5. `draft-walk`, all personas.
   - Expected [I]: 01 goes 58 → 57 steps (the two screens become one); 07 loses one step.
   - 03, 04 and 08 were also asked the amount, so they likely save a step as well [I].
   - No persona should show an opened-and-unanswered question at the amount.
6. `interview-rules` (the asked-unread classes may move), `interview-order`, `mutate` (s2 and f1040 mutants on the
   new gate), engine differential if the generator change is to be exercised.
7. Regenerate `rendered/2025/f1040.md`, `rendered/2025/s2.md`, canonical.

## Reviews made due

- **f1040:** transcription and class M, line-scoped to the two new lines and line 2a.
- **s2:** render, line-scoped to the three lines whose reads changed.
- **Questions review:** the new box and the amount's prompt.
- **False-no sample:** `f1040.tax_exempt_any`. Who could pass over it wrongly: a holder of muni bonds at a broker
  whose combined statement shows "tax-exempt interest" only in its 1099-INT part. The label uses that term.
- **Class M subjects:** they change for every form whose class M cases gained the inserted false input. It is
  input-only with no value change; D6 decides whether that reruns anything (the g1-f6 precedent).

## Combining with the lane's other patches

On a scratch copy of xint's bank and coverage/sales.yaml, I applied int-p18, int-n10 and int-n10-ticks, then this
patch's questions.yaml hunks, with `patch -p1`. All applied cleanly, and the bank parsed. Each patch also dry-runs
alone against xint copies.

## Unverified

- Every expected walk effect and every "values unchanged" claim. Nothing was run.
- That `div.any` and the new box are both open at the same moment for every persona, so that the screen is never a
  screen of one [I from README:604-610; `tick-groups` decides].
