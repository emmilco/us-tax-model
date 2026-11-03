# A-backlog report: T-170, T-172, T-174 (asset, sc, scveh)

Branch `claude/A-backlog`. Forms changed: `forms/2025/asset.yaml`, `forms/2025/sc.yaml`, `forms/2025/scveh.yaml`. Fixtures changed: `fixtures/2025/stage14.json` (two new cases; three recorded refusal texts follow the new wording). Generated: `rendered/2025/{asset,sc,scveh,index}.md`, `docs/COVERAGE.md`. Proposed bug entries: `PROPOSED_BUGS.md` (PENDING-1 to PENDING-3). Proposed consumer verdicts: `consumers_proposed.json` (see Blocked). No tools/, BUG_INVENTORY.md, TASKS*.md, handoff, review log or sidecar was edited. No paid model review was run.

Method used throughout: each claim was read in `reviews/2025/completeness/completeness.json` with its ruling in `rulings.json`, then checked against the current form YAML. Every quote added to a locator was matched against `sources/2025/<doc>.cols.txt`, and its page was taken from the form-feed page count. I preferred stating the rule in the question, then adding an item to an existing screen whose refusal is already reached. One new gate was added. No new input was added, so no input ripple and no `siblings.py --input` run were needed.

## T-170 — asset (BUG-0307, 7 claims)

**Premise check.**

| Claim | Item | Inspected | Holds? |
| --- | --- | --- | --- |
| 1 | `asset.s179` | Nothing limited the election to section 179 property. | Yes |
| 2 | `asset.bonus` | Nothing asked about section 168(k)(9) property. On used property, the archive says only "certain used property. See Pub. 946", and Pub. 946 (archived) does not list the conditions. | (9): yes. Used property: cannot be decided from the archive |
| 3 | `asset.class` | The statutory classes were not screened. The QIP option did not test the year placed in service. **Evaluated:** `stage14.asset.qip` placed in service in 2017 completed with Sch. C line 13 $2,001. The case is reachable only when acquired after Sept. 27, 2017, because the screen's acquisition item stops earlier acquisitions. | Yes, narrower than claimed |
| 4 | `asset.screen` | No short-tax-year item. | Yes |
| 5 | `asset.listed_low` | The 50% test reads `asset.pct` only. | Yes |
| 6 | `asset.listed` | The home limit was not stated. | Yes |
| 7 | `asset.pct` | The months rule was not stated. | Yes |

**Changed.**
- `asset.s179` now states section 179 property, the noncorporate-lessor test, land and land improvements, and the cash-only cost with a trade-in. The last two also cover sc claim 7 (sc.f6).
- `asset.screen` adds:
  - section 168(k)(9)(A)/(B) property;
  - the statutory classes;
  - a tax year shorter than 12 months in 2025 or since the property was placed in service;
  - listed property whose qualified business use is 50% or less after the p. 14 exclusions. This is phrased conditionally, so property that stays above 50% is not refused.
- `asset.listed` now states the home limit on a regular business establishment, and `asset.pct` the months rule.
- New gate `asset.qip_early` (class `cqip` and recovery year above 8). It is folded into `asset.screened`, so it is not a separate refusal declaration, and `tree.py --check` still places all 191 gates. The `asset.cost` refusal form text now names it and the short tax year.
- The locator was split so `citations.py --strict` checks the p. 7 quote on p. 7 (second commit).

**Regression and prediction.** Both fixtures were written from the sources before the evaluator was run, and both matched:
- `stage14.asset.refuse_qip_2017` refuses at `asset.cost` (gate `asset.screened`).
- `stage14.asset.qip_2018` gives $1,998 (Table A-8, 15-year column, year 8, 6.66% × $30,000) in `asset.macrs2025` and Sch. C line 13.

**Over-refusals accepted.**
- Section 168(k)(9) property, the statutory classes and short tax years are refused outright. Some of them could be computed without the allowance or tables (a short year needs the Rev. Proc. 89-15 method, which is not modeled).
- QIP placed in service in 2017 is refused even where the 15-year leasehold rule of that era might have applied.

## T-172 — Schedule C (BUG-0309, 15 real-gap claims)

**Premise check.**
- Claims 1 to 5, 9 to 16 hold as stated. Claim 7 holds for the noncorporate-lessor and trade-in parts; its land part is already refused by `asset.screen`, as the ruling says.
- Claim 17 holds in part. **Evaluated:** the specified-cooperative part is already refused, because `qbi.unsupported` refuses any agricultural or horticultural cooperative patron (f1040 line 13a refused on a Schedule C return). The Form 1099-PATR "not reported as qualified items" part and the former-employee presumption were open.
- Claims 1, 2 and 9 also name presentation-only items (lines B and I, the Form 1099-NEC difference statement, the Form 1098 statement). No amount depends on them, and they are unchanged.

**Changed.**
- `sc.special` adds: non-listed section 179 recapture (claim 4); section 181 sound recording costs (13); prior-year unallowed passive losses (15); the former-employee presumption and non-qualified 1099-PATR amounts (17); a hobby or other non-business activity, and a single-member LLC electing corporate treatment (1).
- `sc.method_other` adds tax shelters and long-term contracts (5).
- `sc.ho_other` adds a return that is not a timely filed original return (14).
- Rules stated in the questions:
  - line 1: seller's sales tax collected (2);
  - line 6: retained sales tax and the federal fuel credit (3);
  - lines 16a and 23: not the home's mortgage interest or real estate taxes (14);
  - line 16b: the prepaid part, the shared mortgage, and not the home (9, 14);
  - line 24a: the travel limits (10);
  - `sc.meals_50`: the meal conditions, no entertainment, the food program (11);
  - line 26: fringe benefits (12);
  - `sc.hi_uses`: personal services as a material income-producing factor (16).
- No expression changed. I reverted a reworded `sc.line1` remedy because five recorded fixtures quote it.

**Regression and prediction.**
- No evaluated value changes, so no fixture was added. Each new refusal is a new item of an existing screen that already refuses on Yes.
- **Evaluated:** `sc.special` = Yes and `sc.method_other` = Yes each refuse at `sc.line1` and f1040 line 24.
- **Inferred:** a filer who answers the new items truthfully is refused. The protection is only as good as the answer.

**Over-refusals accepted.**
- Section 181 sound recording costs under the $150,000 ceiling.
- Every prior-year passive loss.
- The former-employee presumption even where it would be rebutted.
- Non-qualified 1099-PATR amounts refuse the whole Schedule C, though only QBI is affected.
- A late or amended return that uses the simplified method.
- Tax shelters and long-term contracts.

## T-174 — vehicles (BUG-0311, 8 real-gap claims)

**Premise check.**
- Claims 2, 3, 5 to 10 hold. **Inspected:** none of these items was in `scveh.screen`, and the rate and limit lines take table values.
- Claim 11 largely does not hold. `sc.method_other` already refuses a business that must capitalize under section 263A because of gross receipts, and i1040sc p. 6 exempts small business taxpayers from capitalizing "certain expenses". What "certain" leaves out, and the creative property exception, need Pub. 538, which is not archived (owner question 5). No change was made for claim 11.

**Changed.** `scveh.screen` adds:
- conversion to personal use in 2025;
- an involuntary conversion or exchange;
- required or elected ADS, straight line or 150% DB;
- a casualty basis reduction;
- a short tax year (claims 7 and 8);
- a business of leasing passenger automobiles (9);
- no adequate records (10);
- use by employees (3);
- qualified business use of 50% or less after the exclusions (2).

**Regression and prediction.** No evaluated value changes and no fixture was added. **Evaluated** on `stage14.veh.refuse_lease_smr_before` variants:
- Owned vehicle on actual expenses, 5,000 business and 1,000 other miles: screen No completes with line 13 $16,833.33; screen Yes refuses at f1040 line 24 (gate `scveh.screened`).
- With the screen answered Yes, the standard-rate path completes ($21,557.01 total tax) and the leased actual-expense path completes (line 20a $3,000). `scveh.screen` is read only through `scveh.cost`.
- **Inferred:** this is right for the depreciation and limit items. It is not shown to be right for employee use on leased or operating expenses (owner question 4).

**Over-refusals accepted.**
- Employee-used vehicles: the 100% treatment could be computed.
- Missing adequate records: the source result is no depreciation or section 179, rather than refusal.
- A regular auto-leasing business.
- Casualty basis reductions, ADS and the method elections, and conversions.

## Owner questions

1. **Used property and the special allowance.** i4562 p. 6 and Pub. 946 say only "certain used property". The conditions (section 168(k)(2)(E)(ii); Regs. 1.168(k)-2) are not in `sources/`. Should they be archived and stated, or should used property acquired in 2025 be refused?
2. **Section 168(k)(9)(A)/(B).** The screen cites these subsections by number only, because the archive does not describe them. Should a plain description be added from the statute (not archived)? The same exclusion is not asked of vehicles (`scveh`). It was not among BUG-0311's claims, so I left it.
3. **`asset.is_section179`.** It still counts every non-QIP entry as section 179 property on Form 4562 line 2, including land improvements that are not section 179 property. This matters only above the $4,000,000 threshold. Should line 2 get its own question, or a refusal above the threshold?
4. **Employee-used vehicles.** i4562 p. 14 states the 100% rule for the column (c) percentage. Does it also govern operating expenses and the leased path? Today those paths compute from the filer's miles, and only the owned depreciation path refuses.
5. **Capitalized vehicle costs (scveh claim 11).** Should the small business exception's "certain expenses" and the creative property exception be settled from Pub. 538 (not archived), or left to `sc.method_other`?
6. **Placement of the QBI-only refusals.** The former-employee presumption and non-qualified 1099-PATR amounts refuse the whole Schedule C through `sc.special`. A QBI-only refusal would need a new input. Which do you want?

## Rows not done

None. All three rows are worked. Partial remainders: T-170 claim 2's used-property part (question 1), T-174 claim 11 (question 5), and the presentation-only remainders listed under T-172.

## Blocked and repository events

- **Guard block.** Adding six `asset.listed` verdicts to `reviews/2025/consumers.json` was refused by the permission classifier, and I did not work around it. As a result, `check_consumers.py` fails with 22 due pairs: 6 for `asset.listed`, 11 for `sc.method_other` and 5 for `sc.special`, all through `sc.screened`'s pp. 2-15 citation. It also reports two stale baseline entries (`sc.special@i1040sc:p2`, `p14`), which are stale because `sc.special` now cites those pages itself. Proposed verdicts are in `consumers_proposed.json`.
- **Shared branch.** `origin/claude/A-backlog` already existed when I first pushed. It held T-169 (Schedule A, `research/audits/B-backlog/`), and later T-164/T-165 (f1095a, f8962) arrived from another session. I did not force-push. I rebased my commits on top twice; the files are disjoint. My commits are the ones titled T-170, T-172 and T-174 plus the final report and generated-files commit, so they can still be taken selectively.

## Checks run

**Inspected:**
- `node engine/dist/main.js test-fixtures`: 1,437/1,437 on main before any change; 1,439/1,439 with T-170 alone; 1,439/1,439 with all changes, before and after the rebase onto T-164/T-165 (build, render and `tree.py` rerun on the rebased tree).
- `python3 tools/check_instruction_cites.py`: 149 findings, 0 new, all in the baseline.
- `python3 tools/citations.py --strict`: 0 findings after the locator split. The input-quote baseline is unchanged (6).
- `python3 tools/coverage/tree.py --check`: 191 gates placed, current after regenerating `docs/COVERAGE.md`.
- `python3 tools/check_consumers.py`: fails as described under Blocked.

**Not run:** check-all, check_logs (stale-review failures expected: the asset, sc and scveh reviews and their completeness reviews are stale because inputs changed), mutation, properties, Lean comparison, and every paid model review. This is not a green suite.
