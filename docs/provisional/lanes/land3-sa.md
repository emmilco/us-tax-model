# Lane land3-sa: Schedule A text defects (BUG-0632 with its duplicate adj9-01; BUG-0639)

Agent: claude-opus-5-5, judgment; tax year 2025, jurisdiction us. Worktree `.claude/worktrees/land3-sa` (detached
snapshot of the landing tree). Not committed. No paid review call and no model call from code.

## Are the defects real

Yes, both, checked against the form data and i1040sca (2025).

- adj5-02 / adj9-01: `sa.line5a_total` adds `sa.line5a_if_state_tax` and `sa.state_tax_other_if_any`, but the input
  `sa.line5a` was labelled "State/local income taxes paid, including withholding" and its source listed estimated
  payments, prior-year tax, the fund contributions and territory tax, which `sa.state_tax_other` also covers.
  `sa.state_tax_any` was labelled "pay any state or local income tax, including tax withheld from pay or other
  income". The bank prompts were already right (withheld from pay; boxes 17 and 19).
- adj9-04: `sa.unsupported` tests the mortgage, sales-tax, foreign-tax and five line 16 items; no casualty.
  `sd.casualty` feeds `sd.other_forms` ("Schedule D additional source forms"). i1040sca p. 11, Line 15 sends a
  casualty loss through Form 4684.

## The change

`forms/2025/sa.yaml` (no expression changed):

- `sa.line5a`: label "State and local income tax withheld from your (or, on a joint return, your spouse's) pay in 2025
  (Form W-2, boxes 17 and 19)". The source says boxes 17 and 19 of each W-2, leaving out withholding deducted on
  another form. It names the other kinds of state tax as entered separately and keeps the no-refund-reduction
  sentence. Citation: the withholding and refund sentences of i1040sca p. 3, Line 5a, plus fw2 p. 4, Copy B, boxes 17 and 19.
- `sa.state_tax_other`: source now holds the moved paragraphs (withholding from other income, estimated payments,
  prior-year tax, the fund list, refunds not subtracted, the charitable tax-credit safe harbor, territory tax). The
  i1040sca p. 3 / p. 7 citation that `sa.line5a` had moved with them, plus the W-2G/1099 withholding sentence.
- `sa.line5a_if_state_tax`: citation cut to the withholding sentences.
- `sa.state_tax_any`: label "In 2025, was state or local income tax taken out of your (or, on a joint return, your
  spouse's) pay?"; source adds "Boxes 17 and 19 of a Form W-2 show it." This is word for word the bank's existing
  prompt.
- Refusal `when: sa.unsupported`: renamed "Schedule A unsupported item" on all eight lines carrying it (6, 8b, 8c, 12,
  13, 15, 16, 17). The entry named only 6, 15 and 16. The other five carry the same gate under the same name, so I
  renamed them too, to keep one gate under one name.
- `sa.line15`: citation now i1040sca p. 11, Line 15, with "(zero here: a casualty or theft loss is refused by
  sd.casualty through sd.other_forms, the refusal Schedule D additional source forms)".

Other files:

- `interview/2025/questions.yaml`: the `prompt` of `sa.state_tax_any` was removed. The build refused it ("prompt
  repeats the form line's") once the source matched it. The filer sees the same words as before.
- `fixtures/2025/sa.json`: the refusal name quoted in `stage4.refuse.sa.unsupported` and
  `stage4.refuse.sa.unsupported.simultaneous` (16 occurrences). Nothing else was edited.
- `reviews/2025/consumers.json`: removed the ruling `consumer:sa.state_tax_any@i1040sca:p7`, which
  `check_consumers.py` reported stale ("no longer fails; remove it"). The gate no longer cites the p. 7 territory
  sentence. This is a ruling removed at the tool's instruction, not a baseline added; the coordinator may want to
  confirm.
- `bug_pending/land3-adj5-02.md`, `bug_pending/land3-adj9-04.md`, and the duplicate
  `docs/provisional/lanes/landing_work/land3-adj9-01.duplicate-of-adj5-02.md`: Fix, Fix lines, Siblings checked and
  Regression predictions. The duplicate's fields point at the same change.

Protocol (interview construction protocol): no shown question text changed, so the walk is unchanged (N9). Who could
wrongly skip: a filer with only estimated payments answers No to `sa.state_tax_any`, but `sa.state_tax_other_any`
is its own box on the same tick screen (`paid_2025`) and is asked regardless (coverage rows `home.state_fund_only`,
`home.state_tax_estimates`). Fixture double count: no fixture states a positive `sa.state_tax_other`, so no case
adds a second part to a whole-total `sa.line5a`.

## Verification (this worktree, after the last edit to forms, bank and fixtures)

| Command | Result |
|---|---|
| compile, `build`, `render` | build OK (after removing the repeated bank prompt); 68 rendered files |
| `test-fixtures` | 1989/1989 |
| `test-fixtures --ny` | 357/357 |
| `citations.py --strict` | 0 findings, 0 locators to rewrite |
| `check_consumers.py` | 0 new; 1 stale ruling reported, removed (above); then 0 stale |
| `check_questions.py` | 0 new |
| `check_screens.py` | 0 new |
| `check_false_no.py` | 0 new (exit 0) |
| `siblings.py --check` | passes |
| `check_bug_inventory.py` | exit 1. Expected snapshot artifacts: adj5-02 and adj9-04 "a committed pending entry was changed or removed" (the brief asked to fill in their fields); adj9-01 cited with no pending file (it was moved to landing_work before this lane); the landing-01 to 13 lines, as at baseline |
| `interview-rules` | 0 problems (177 walks) |
| `tick-groups` | passed |
| `interview-coverage` | 498 rows, 0 row problems. The first run reported only that `reports/2025/interview_coverage.md` was out of date, and `--write` regenerated it. The committed report already said 494 rows against the snapshot's 498, so it was stale before this lane, and the regenerated diff (background counts shifting by one) is inferred to come from earlier lanes. Not proven: the untouched tree was not rerun (about 40 minutes) |
| `node tools/check_refusal_reach.mjs` | 465 refusal fixtures checked, 2 listed exceptions, exit 0 |
| `year_changes.py --check` | exit 0 (notes only) |

## Review dry run

`rerun_all.py --dry-run --kinds transcription,render,classm --forms sa --model claude-opus-5-5`: 3 jobs, $3.53. That is
above the $3.00 gate and needs `--approve-cost`. The jobs: classm sa (whole) $2.67, render sa (line-scoped) $0.34,
transcription sa (line-scoped) $0.51. Nothing was run.

## Left open

- `changes/2026/sa.yaml` (the 2026 operation adding line 8d) still names the refusal "Schedule A unsupported item / Form
  4684". Tax year 2026, outside this lane; it should be renamed to match when 2026 work touches it.
- The parent `sa.state_tax_other_any` (label and bank prompt) does not name the charitable tax-credit safe harbor,
  which its child's prompt lists. A filer whose only other state tax payment is such a credit could answer No.
  This is a rare case, not fixed here.
- Fixtures with a positive `sa.line5a` were written when it meant the whole total. Their values are unchanged (the
  sum is the same), but a scenario that had estimated payments now has them in the wrong part. This was not audited.
