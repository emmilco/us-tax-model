# int-personas.patch: the answers that complete personas 21 and 22 (plan-interview item 3)

Lane patch-interview, claude-opus-5-5, judgment, 2025, us. Persona files only. Nothing run. **[C]** checked;
**[I]** inferred.

## Hunks

**21_money_back_itemizer**
- `who:` gains one sentence: "Their 2024 Schedule A deducted $5,000 of state income tax and $4,000 of property
  tax."
  - This matches the stated `refund.line5d_prior_year: 900000`.
  - It lets the fourth `refund.exc_tax` bullet be answered from the story: the $400 refund is less than $5,000
    less any sales-tax alternative.
  - The form has no 5a input, so nothing else needs stating [C forms/2025/refund.yaml:343-398, no `line5a`].
- Ten answers, all `false`, each the one the walk had closed [C wout-after/21:9-18]:

| Answer | Reason from the story |
|---|---|
| `refund.box8` | A wage earner's state income tax, not a tax on business income only |
| `refund.other_year` | "2024 state income tax" |
| `refund.paid_other_time` | Withheld from 2024 pay; the help says that counts as paid in 2024 [C bank help] |
| `refund.exc_tax` | $90,000 of wages: no AMT, no unused credits, line 16 not zero; fourth bullet as above |
| `refund.exc_who` | 58, own return, single in 2024 |
| `refund.you_born` | Born 1967 |
| `refund.you_blind` | Not in the story |
| `scope.passive` | The loss is from a business they ran and closed (an NOL), not one they did not help run |
| `scope.f8978` | No partnership |
| `s179.prior_form` | The story names only the NOL as carried |

**22_refused_old_loss**
- `scope.passive: false`, `scope.f8978: false`, `s179.prior_form: false`, for the same reasons [C wout-after/22:9-11].

## The end discrepancy in 22: resolved, no edit

- The persona's `end` is `s1.nol_before_limit_date_if_nol`; the walk ended at `s1.nol_pre2018_if_nol`.
- The walk is older than the rename: it was written 22:10 and the persona file 23:23
  [C file times, /private/tmp/wout-after/22_refused_old_loss.md and interview/2025/personas/22_refused_old_loss.yaml].
- xint's s1.yaml has only the new name [C forms/2025/s1.yaml:1470, 1480, 1685].
- So the persona is current and the walk is stale.
- The same holds for 21's `s1.nol_before_limit_date` answer.

## What to run

`draft-walk` for 21 and 22. Expected [I]: no problems. 21 ends `complete` and 22 at its gate, with the same step
counts as before (the closed answers are now persona answers). If the renamed NOL questions changed the order, new
problems may appear that the 22:10 walk could not show.

## Reviews due

None.

## Not in the patch: the N8 finding

- `refund.you_born` ("Were you born before January 2, 1960?") is asked after `person.birth_year`.
  - Proposal: technique 3.3. Derive it from the birth year (≤ 1959 true, ≥ 1961 false) and ask a narrow question
    only for 1960. Treat a 2024 joint return's spouse box the same way.
  - That is a model change with its own fixtures, and it is not drafted here.
  - Bug-entry text for the inventory: "`refund.you_born` asks a birth date already settled by
    `person.birth_year` (N8); derive it, with a narrow question for birth year 1960."
