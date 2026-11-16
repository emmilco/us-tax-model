# Lane b1-mutA: the AMT screen's unexplained mutation survivors (BUG-0656, lane F7b's share)

claude-opus-5-5, judgment, tax year 2025, jurisdiction us. Worktree `.claude/worktrees/b1-mutA` (snapshot of the
final goal-1 merge B1). Nothing committed; no check-all; no paid review and no model call. Lane b1-mutB handles the
other 12 survivors (household, s3, scveh).

## Result

Of the 71 survivors in scope (60 in s2, the 6 operands of person.amt_dep, 5 amt.* parameters):

| Outcome | Count | Mutants |
|---|---|---|
| Killed by a new fixture | 66 | all but the five below |
| Argued equivalent (keyed argument, sampled check) | 2 | `operand.s2.s2.amt_rel.zero.then1`, `operand.s2.s2.amt_l15.amt_l13.then1` |
| Left, with a pending defect | 3 | `operand.s2.s2.amt_l7.amt_l39.then1`, `operand.s2.s2.amt_tmt_over.amt_l7.gt.0` (they reveal it), `operand.s2.s2.amt_l16.amt_l15` (tied to it) |

Federal `MUTATE_WORKERS=8 node engine/dist/main.js mutate` (one run, about 100 minutes under a load average of 150 to
290): **exit 1, on 15 survivors not yet explained: this lane's 3 left above and lane b1-mutB's 12** (household 7, s3
3, scveh 2; untouched here). 7758 mutants; checker 2801; fixtures 4581 (60 only by class M); 376 surviving (354
equivalent on every input, 7 on answered inputs only); score 95.2%, adjusted 99.7% / 99.8%. 0 stale arguments; every
self-test 0 problems; sampled check: 114 keyed arguments on 94 lines, 300 generated returns and 2040 fixture cases at 4
rates, controls rejected 69 of 77, 0 problems. Before (B1's report): 443 surviving, 83 unexplained.

Side effects of the new cases: four mutants that only class M cases killed are now killed by stage fixtures too
(`minmax.s2.s2.amt_mfs_add`, `operand.s2.s2.amt_l13_14.amt_l13`, `operand.s2.s2.amt_mortgage.zero.then1`,
`operand.sdtw.sdtw.line13.line10`). No keyed argument is killed by them (checked before the run against all 114).

## The defect (BUG-0764, `bug_pending/b1-mut-01.md`)

`s2.amt_l7` takes Part III (line 40) only when `f1040.gate.qdcg_applies`, which also requires taxable income above
zero. Form 6251 line 7 completes Part III whenever qualified dividends or capital gain distributions are reported (or
Schedule D lines 15 and 16 are both gains), with no taxable-income condition. With zero taxable income the screen
uses line 39 (26%/28% on all of line 6), which is never less than line 40, so the defect only over-refuses. Example
evaluated here: single, $15,000 of qualified dividends as the only income, $85,000 of private activity bond
interest; line 6 $11,900 all at 0% in Part III, so line 7 is $0 and not over line 10 ($0); the screen takes $3,094 and
refuses with Form 6251. The two mutants that read Part III there are the form's rule, which is why no fixture can kill
them without pinning the over-refusal. Not fixed (stop on the mutant, per the brief).

**Prefix collision for the coordinator.** The brief named `--pending b1-mut`; lane b1-mutB may write
`bug_pending/b1-mut-01.md` too. If both lanes did, rename one before `new_bug.py --assign`.

**For the coordinator:** after `--assign`, the three left survivors can be listed in `OPEN_DEFECT_SURVIVORS`
(engine/src/mutate.ts) under the assigned id so the step passes while the entry is open; the table refuses a
`BUG-NEW-*` placeholder (it needs an open entry in BUG_INVENTORY.md), so I did not add them.

## Fixtures (fixtures/2025/s2.json, 12 new cases, appended; no existing case touched)

Every expected value was predicted by hand from f6251/i6251 (2025), the Schedule D Tax Worksheet, the Tax
Computation Worksheet and, for depreciation, Pub. 946 Table A-1, before the engine evaluated it; the evidence note of
each case has the derivation. All 12 predictions matched on the first evaluation. Each case expects only lines in
their context on that return (no line the form skips, no married-filing-separately line on another status).

| Case | Return | Kills |
|---|---|---|
| `s2.mut.amt_sdtw_phaseout` | single, wages $500,000, capital gain distributions $200,000 (box 2b $50,000, 2d $30,000), tax-exempt $10,000 | exemption phase-out (l5, phaseout_start, rate_25), Part III with the Schedule D Tax Worksheet (l13_14, l15_sdtw x2, l18 x3, l28, l35 x3, l36 x2, l37_rate, l37), the bound's exemption and 28% branch (h_ex_over, h_ex_cut, h5, h6_high, h39 x3), h_extra |
| `s2.mut.amt_line40_rounding` | single, wages $100,000.04, distributions $10,000 (2d $9,999.98, 2b $0.02) | l40 (l39 operand), l7 (l40 operand): line 38 exceeds line 39 by one cent of rounding |
| `s2.mut.amt_line6_at_bracket` / `_over_bracket` | wages $327,200 / $327,201 | l6_high and h6_high boundaries; amt.bracket +$1 |
| `s2.mut.amt_line17_at_bracket` | wages $327,200, qualified dividends $50,000 | l17_high boundary; l14 zero operand; l14_any boundary |
| `s2.mut.amt_depreciation_bound` | Schedule C with 3-, 5-, 7-, 10-year 2025 property (no bonus), 2024 5-year property, a listed camera | the six person.amt_dep operands; amt_rel (rel_items operand) |
| `s2.mut.amt_related_without_depreciation` | the IRA case stage19.mut.ira_single_full_edge | amt_dep_any boundary and operand |
| `s2.mut.amt_pab_over_tax_exempt` | private activity bond interest entered above tax-exempt interest | pab_over x2, the refusal on amt_l4, l14_any (l14 operand), l37 (zero operand) |
| `s2.mut.amt_boat_mortgage` | itemizer, mortgage interest $45,000, boat question Yes | amt_could, amt_boat_ask, s2.amt (amt_owed operand) |
| `s2.mut.amt_mfs_addback` | MFS, wages $1,000,350, taxable state refund $1,400 | the MFS addition chain (mfs_over, mfs_quarter, mfs_add, l4_mfs x2, l4m), mfs_addback_start, amt_l4 (l4_known operand), the bound's MFS chain (h_mfs_over, h_mfs_quarter, h_mfs_add x2 incl. minmax) |
| `s2.mut.amt_mfs_addback_max` | MFS, wages $1,500,000 | the $68,500 cap (mfs_add, h_mfs_add), mfs_addback_max |
| `s2.mut.amt_line15_sdtw_line10` | wages $200,000, distributions $50,000 all box 2b, Form 4952 election $30,000 | l15 (l15_sdtw operand): unrecaptured gain above worksheet line 9, so line 15's "smaller of" binds |

Weaker kills, named so the reader can weigh them: four boundary mutants (l6_high, h6_high, l17_high, l14_any)
change only a gate's own value on their fixture (the amounts on either side of a bracket edge
are continuous); h6_high's fixture has no tax-exempt or mortgage interest, so no question reads that gate there. Two
kills (l14_any's operand, l37's zero operand) are on the private activity bond return, where line 4 refuses: they turn
line 14's gate and line 37 from their skip values into that refusal.

## Arguments (engine/src/mutate.ts, two entries added to EQUIVALENT_IF before `...nyEquivalences()`)

- `operand.s2.s2.amt_rel.zero.then1`: the false alternative reads s2.amt_dep, which is $0 wherever the guard
  (amt_dep > 0) is a known false, and is never a refusal where the guard is unknown. Premises: s2.amt_rel,
  amt_dep_any, amt_dep, s2.zero, param sales.zero.
- `operand.s2.s2.amt_l15.amt_l13.then1`: line 14 is a choice on the same guard with s2.zero on the false side, so
  lines 13 + 14 are line 13 there; under an unknown guard line 14 never refuses, so the second way refuses on both
  routes alike. Premises: s2.amt_l15, amt_l13_14, amt_l14, s2.zero, param sales.zero.

Pre-tested with the run's own sampled check (`sampledPlan`/`sampledShare` from engine/dist/mutate.js on these two
sites, 300 generated returns and every fixture case at the four rates, 9,360 sets each) before the full run: neither
contradicted; amt_rel's reached 9,146 sets and exercised none (amt_dep is $0 wherever the guard is false), amt_l15's
reached 8,093 and exercised 2,235. The amt_rel control (rel_items operand, killed by the depreciation case) was
rejected; the amt_l15 control (l15_sdtw operand, killed by `s2.mut.amt_line15_sdtw_line10`) was not, because its kill
there is on Part III lines, all helpers, and line 7 stays under line 10 on that return (the run fails only if no
control at all is rejected).

## Files changed

- `fixtures/2025/s2.json`: 12 cases appended (rewritten with the file's own format, `json.dumps(indent=2,
  ensure_ascii=False)`, which reproduces the original byte for byte; the diff is additions only). Merge by case id.
- `engine/src/mutate.ts`: 2 keyed arguments added (4 lines). No other change.
- `bug_pending/b1-mut-01.md`: the pending defect.
- `reports/2025/mutation.md`: regenerated by the run.
- `mutation.json` is not changed: the cases are in s2.json, which takes the defaults and is the second file mutate
  tries for an s2 mutant; this also keeps clear of lane b1-mutB's edits to mutation.json.

## Verification

- `npm run build` (compile and build): build OK; `tsc -p engine` again after the mutate.ts edit.
- `node engine/dist/main.js test-fixtures`: 2040/2040 (2028 before, plus the 12).
- Every expected value of the 12 cases compared with the engine before writing: 0 mismatches with the hand
  predictions. Every one of the 71 mutants evaluated against the 12 cases with a throwaway script
  (`/tmp/b1mutA/harness.mjs`, not in the tree) before the full run: 66 killed on expected lines, the same 66 the run
  then reports killed.
- The federal mutate run above (once). Not run: check-all, `mutate --ny` (no New York line or case changed),
  `test-fixtures --ny`, reviews (no form, expression, question or parameter changed; the cases are fixtures only).
- Cost: no paid call, no model call; agent time only.
