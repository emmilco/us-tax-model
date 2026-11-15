# Lane land3-adj12: class M adjudication of asset, f8962, ira, sc, scveh (2026-11-14)

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us.

## Status: rulings decided, not applied

The Claude class M logs of these five forms (dated 2026-11-14, written in `land3-cmB`) are present in the landing
tree only as the generated views `.transcription/logs/2025/classm/<form>.md`. Their tracked results were not
carried: `reviews/2025/classm/<form>.index.json`, the five new records in `reviews/store/classm/`
(5f59477d..., 488627d1..., ceee3fe3..., e9ba0211..., c2b1c0ae...) and the regenerated cases in
`fixtures/2025/classm.json` exist only as uncommitted changes in `land3-cmB` (worktree_data.py carry-back leaves
tracked files out). In landing the store view (`review_store.view`) is still the earlier review (no open
ruling), so `carry.py` saw 0 of 0 and `check_logs.py` reports "the classm log reviewed an earlier computation".
`rule.py` was not run: it reads the store view, would rule nothing, and writing back would overwrite the new view.

To apply, after land3-cmB's tracked class M results are in landing:

    for f in asset f8962 ira sc scveh; do
      python3 tools/transcription/rule.py --form $f --kind classm --rulings /tmp/land3-adj12/$f.json
    done
    python3 tools/transcription/check_logs.py 2>&1 | grep -E '^\[claude\] (asset|f8962|ira|sc|scveh):'

Every key in the rulings files was checked against the open sections of the new logs (32 of 32).
Every ruling sets `drop: true`.

## Rulings (32 lines; no finding; none left open)

- asset (3): model error 3. Case 3, item_1 is qualified improvement property: `period` y15sl vs the model's y15,
  and `macrs_this_year` $155.63 (Table A-12, 15-year, Q4, year 1 0.83% x $18,751.20) vs $234.39 (the model's
  Table A-5 150% DB). p946 Table 4-1 puts QIP placed in service after 2017 under "GDS using SL". Case 4 `basis`
  ($165.00 vs $0.00): the line is labeled "before section 179 and the special allowance"; the model subtracted
  section 179, which belongs to 19(c) (`asset.col19c`), as settled in the transcription rulings on (c).
- f8962 (1): scope 1. Case 1, line 24 ($2,730.00 vs $0.00): the case is married filing separately, which the
  return refuses (`scope.ready_credits` at `s3.mfs`). Same as the earlier ruling on this case id.
- ira (2): representation 2. Case 3, lines 7a and 7b ($0.00 vs $8,000.00): no traditional IRA contributions
  (`ira.any_trad` false), so the project shows zero on a worksheet nobody completes. Lines 12a, 12b and Schedule 1
  line 20 are zero either way.
- sc (5): representation 5 (helper of a branch not taken). Case 2, business d, Form 7206 lines 4, 7, 8, 10 and 13:
  no plan is established under the business (`sc.hi_uses` false), line 14 agrees at $0.00. Same as the earlier
  rulings on classm.sc.2 and sc.3.
- scveh (21): owner's ruling 21 (ambiguity class). Cases 1 to 4: a difference of one or two cents from the
  business-use ratio rounded to six places (amb.2025.vehicle_business_pct). Each project amount was reproduced
  with the six-place ratio.

Summaries: a "Landing round (2026-11-14), class M" section appended to
`reviews/2025/transcription/adjudication/{asset,f8962,ira,sc,scveh}.md`.

Observation, not filed: the class M job generator still produces married-filing-separately cases for f8962,
which the return refuses (second time for classm.f8962.1). A paid case is spent on out-of-scope input each time.

## Applied (coordinator, 2026-11-14)

After land3-cmB's tracked class M results were merged into the landing tree (fixtures/2025/classm.json merged by case id against the class M snapshot; indexes and records applied), the 32 rulings above were applied with rule.py; check_logs.py reports nothing for asset, f8962, ira, sc or scveh.
