# int-p18.patch: the less-common-sales screen asked before the list of sales (plan-interview item 4)

Lane patch-interview, claude-opus-5-5, judgment, 2025, us. Bank only, plus answer restatements in four coverage rows.
Nothing was run. **[C]** checked against the file named; **[I]** inferred.

## Summary

Within order 274, `seq` is renumbered so that the following are asked before `$sales`:
- the `sales_rare` screen: `sd.sold_other` 1, `sd.sec1256` 2, `sd.condemned` 3, `sd.small_business_stock` 4,
  `sd.trader_election` 5, `sd.qof` 6;
- the follow-ups of `sd.sold_other`: `sd.business_property` 7, `sd.installment` 8, `sd.like_kind` 9.

The sale questions keep their relative order: `$sales` 10, `sd.route_each` 11, `sales.box` 12,
`sales.special` 13, `proceeds` 14, `reported_basis` 15, `correct_basis` 16, `code` 17, `wash_loss` 18,
`route` 19, `aggregate_eligible` 20.

No form, gate id, refusal or expected end changes.

## Why

- The walk confirms the plan's reading.
  - Persona 18 answers `sales[nft].special` Yes at Q101.
  - It is then asked proceeds, basis and code (Q102-104), which it cannot answer.
  - Then the whole `sales_rare` screen (Q105-110).
  - The refusal arrives "on a background answer (question 110, sd.qof)"
  - [C /private/tmp/wout-after/18_refused_nft_art.md:9-12, 637-719, 857-869].
- Mechanism.
  - The special refusal is the first entry of `sales.one` [C forms/2025/sales.yaml:693-700].
  - `sales.one` is read through `sd.count` [C forms/2025/sd.yaml:373-381].
  - `sd.count` refuses first on `sd.other_forms` [C :384-391], an `any` over the rare boxes, their follow-ups,
    `sd.f2439_if_dividends`, `sd.casualty` and `sd.qof` [C :226-268].
  - Lane g1-f6 recorded the same wait: "the sale's refusal waits for the last box of `sales_rare`"
    [C docs/provisional/lanes/g1-f6.md:20-21].
- Asking the rare screen first settles `sd.other_forms` before any sale is entered. `sd.casualty` (order 200) and
  `sd.f2439` (272) are already answered by then.

## Hunks

1. `interview/2025/questions.yaml`: 20 `seq` values in order 274. Each new number is distinct; the group's members
   (1-6) are contiguous with no other order-274 `seq` between them.
2. `interview/2025/coverage/sales.yaml`: rows `sales.collectible_sold`, `sales.extraordinary_dividend_loss`,
   `sales.constructive_ownership_gain` and `sales.nft_collectible` drop their answers to `sales[a].proceeds`,
   `sales[a].reported_basis` / `correct_basis` and `sales[a].code`.
   - Those answers were asked only because the refusal had not yet arrived. With it arriving on `special`, they
     would be stale, and the stale-answer rule would fail the row [C engine/src/interview-coverage.ts:269-276].
   - Their ends (`refused: sales[a].special`) are unchanged. Their `sd.trader_election` / `sd.qof: false` answers
     are still asked, now earlier, and are kept.
   - **If `interview-coverage` reports these four rows as stopping at `proceeds` unanswered, the reorder did not
     have the inferred effect: revert hunk 2 and look at why.**

## Rows checked and left as they are [C python scan of coverage/*.yaml and personas]

- Rows refused at a rare box with no sale answered: `sales.business_property_sold`, `installment_sale`,
  `like_kind_exchange`, `futures`, `condemnation`, `small_business_stock_loss`, `trader_mark_to_market`,
  `qof_held`, and `scope.business_property_sale`. They answer no sale, so nothing becomes stale; their refusal
  still comes on their own box.
- `sales.home_sold_nothing_special` (proceeds): no change.
- Rows refused at `bad_code` (`sales.nominee_sale`, `crypto_code_b_no_form`, `crypto_cost_code`) and the
  completing crypto rows: their sale answers precede `code`, which they need, so they stay asked [I].
- Persona 18 needs no edit. It never answered proceeds, basis or code (the walk closed them).

## Expected effect [I]

- Persona 18 ends at its own answer to `sales[nft].special`, with no opened-and-unanswered question. That is about
  three fewer steps (102-104).
- Every other filer sees the same steps. For a filer with sales, the "less common sales or trades" screen now comes
  before the list of sales.
- A QOF holder or a trader is refused before typing in any sale (N7 off-ramps first; 3.6).

## What to run

1. Build (tick-group build rule on `seq`).
2. `tick-groups`.
3. `interview-coverage`: the 4 restated rows plus all sales and scope rows, with ends unchanged.
4. `draft-walk`: 18, 06, 14, 17 (the sale personas) and 01.
5. `interview-order`: the special refusal should no longer be listed as late.
6. `interview-rules`: the fixtures' walk classes may shift with the order.
7. Regenerate `reports/2025/interview_coverage.md`.

## Reviews due

None of the paid kinds: no form line, wording or citation changes. The owner should glance at the screen's heading
"…less common sales or trades?", which now comes before the ordinary sales question.

## Side note (not in the patch)

`sales.special` (145 words, the longest prompt in the walk [C walk:744]) still lists "an investment in an
opportunity zone fund", which `sd.qof` now asks earlier for the whole return. Under N8 that item could go once the
owner agrees the box covers it (a QOF sale needs a QOF holding in 2025, which `sd.qof` asks) [I].
