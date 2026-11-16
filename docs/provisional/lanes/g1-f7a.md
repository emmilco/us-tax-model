# Lane g1-f7a: Schedule 1, scope and sli (plan row F7a)

Lane agent: claude-opus-5-5, judgment; tax year 2025; jurisdiction us. Worktree `.claude/worktrees/nx-f7a`, base
`b3dc1c0b`. Nothing committed, no claims taken, no paid reviews, check-all not run.

## Bugs

| Bug | Real on this tree? | Outcome | Pending entry |
|---|---|---|---|
| BUG-0433 (scope, Form 8615 examples) | No longer. The redraft asks `scope.unearned_2700`: "more than $2,700 of income that was not pay for work, such as interest, dividends or gains from investments", which covers capital gains and fund capital gain distributions (Form 1099-DIV). | Closed, no change | BUG-0714 |
| BUG-0438 (s1.line8r, the services part of a grant) | Yes. The prompt asked only about non-tuition use. The help left out W-2 teaching pay, but it did not say to count services pay that no W-2 shows (p525 p. 35; p970 Worksheet 1-1 line 2). | Fixed (wording) | BUG-0716 |
| BUG-0539 (s1 other-income lows) | Partly. The redraft's `s1.cod_any` help, "A debt you paid off in full is not a canceled debt", steered a filer who got an early-payoff discount to No. | Four items fixed (wording). The oil and gas lease won by lottery is declined: it is vanishingly rare, and the error it allows overstates income. The line 8j not-for-profit rental of personal property is an over-refusal through `scope.rental`, so it is moved to its own entry: lifting it would add coverage, which is more than a wording change. | BUG-0717; BUG-0713 (new, open) |
| BUG-0563 (sli "for that year") | No longer. The phrase is gone (grep). `sli.unqualified_any` now reads "a loan taken out for someone who was not you, your spouse or your dependent at the time", and its help gives the "could have claimed" exceptions. | Closed, no change | BUG-0715 |
| BUG-0637 (s1 line 9 and line 10 citations) | Yes. Each item was traced to the screen that refuses it in `forms/2025` (listed in the entry). | Fixed (citations) | BUG-0718 |
| BUG-0626 remainder / T-321 | Yes: s1.yaml (2 places), s1.json (4), ambiguities (3.06(1)). params, tables and conjecture.ts already said section 2. | Fixed. See the note on citations.json below. | BUG-0718 (closes 0626 and 0637) |

## Changes

- `forms/2025/s1.yaml`:
  - `s1.ebl_threshold` locator and the `s1.line3` refusal citation: section 3.32 becomes section 2.32.
  - `s1.line9` and `s1.line10` locators: rewritten as BUG-0637 proposed, each as one comma-separated segment so that
    citations.py can verify it.
  - The source text and citations of `s1.scholarship_taxable`, `s1.cod_any`, `s1.cod_amount`, `s1.alaska_dividend` and
    `s1.prizes`.
- `interview/2025/questions.yaml` (s1 entries only):
  - `s1.scholarship_taxable`: the prompt is now "How much of it was for room, board, travel or anything other than
    tuition and required course costs, or was pay for teaching, research or other work the grant required?". The help
    is now "... Leave out pay that is on a W-2 ...".
  - The help of `s1.cod_any`, `s1.cod_amount`, `s1.alaska_dividend` and `s1.prizes` (wording in BUG-0717).
- `fixtures/2025/s1.json`: the four expected refusal citations change from "rp-2024-40 section 3.32" to "section 2.32".
  These are citation text, not values. The lane brief asked for this edit.
- `ambiguities/2025.yaml`: Rev. Proc. 2024-40 "section 3.06(1)" becomes "section 2.06(1)".
- `reviews/2025/citations.json`: once the change was made, the ruling on anchor "section 3.32" was unused. "section
  2.32" is not printed text either: the document prints ".32" under SECTION 2. The 3.32 ruling is therefore replaced by
  a ruling on "section 2.32" with status **proposed**. It still needs the owner's acceptance.

No expression changed (mutate was not run). No 2026 operation in `changes/2026/` names a line this lane touched.

## Verification

All of these were run on the final tree.

| Check | Result |
|---|---|
| `build` | OK |
| `render`, `render --ny`, `render --check` | OK |
| `test-fixtures` | 2003/2003 |
| `test-fixtures --ny` | 357/357 |
| `interview-rules` | 0 problems |
| `tick-groups` | passed |
| `citations.py --strict` | 0 findings, 0 unused rulings, 0 locator segments to rewrite (the same as the base tree) |
| `check_consumers` | 0 new |
| `check_questions` | 0 new |
| `check_screens` | 0 new |
| `check_false_no` | 0 new |
| `year_changes --check` | OK |
| `siblings.py --check` | rc=1. Most problems are on entries from the base tree (BUG-0651, o5-01, o6-01, o6-02, o8-01, o9-01, p2-01, r2-01). The f7a entries' Siblings checked fields pass. Entries -04, -05 and -06 report "no review log changed since HEAD for sibling form(s): s1" (and f1040 for -06). Those clear only when round 2's reviews of s1 land. |
| `check_bug_inventory.py` | rc=1, only on base-tree placeholders landing-07 and landing-09 to landing-13, cited in `docs/provisional/lanes/landing_work/` with no pending file |

Regenerated files:

- `canonical/` and `rendered/2025/`:
  - `s1.md` and `ambiguities.md` changed because of this lane.
  - `params.md` and `rate_schedule.md` changed only because the base snapshot's rendered files were stale against
    P1's section 2 parameter citations.
- `reports/2025/citations.{md,html}` and `reports/2025/input_quotes.md`.

## Round 2 reviews

- **s1:**
  - render: line-scoped to s1.line9, line10, ebl_threshold and line3, plus the five changed inputs.
  - transcription: the five inputs and the four citation changes.
  - question review: s1.scholarship_taxable, cod_any, cod_amount, alaska_dividend and prizes.
  - class M: not due, since no expression changed.
- **scope:** no content changed in this lane. The scope part of the land3-holes rerun (transcription of the gates, and
  render) is still due as the plan says. That is $3.45 together with s2, by the land3-holes dry run.
- **sli:** no change, so no review is due because of this lane.

## For the coordinator

- `reviews/2025/citations.json`: the new "section 2.32" ruling is *proposed*. Accept it, or rewrite the locator to
  name only the printed ".32 Threshold for Excess Business Loss".
- `fixtures/2025/s1.json`: the edits are citation strings inside four expected refusals. Merge them by case with the
  s1.yaml change.
- Lane F1 may touch s1 line 8 (BUG-0615). This lane did not edit `s1.line8f` or any line 8 expression. Its s1.yaml hunks
  are the inputs at about lines 240, 319, 620–720, 806–825, 1090–1120 and 1248–1280.
