# Ruling audit 1: claims that a refusal protects a case

Branch `claude/ruling-audit-1`, based on `main` at 5eec22f. Setup: `npm ci`, `npm run build`, `npm run render`. Every
result below comes from `node engine/dist/main.js eval --inputs <witness> --json`. The two confirmed paths were also
replayed through the `full` interview profile (`tools/replay.py`). Witness inputs are fixture cases with one to four
answers changed; each witness file is named in the tables. `runlog.txt` holds the raw output of every run.

Scope of claims: each witness supports only the path it runs. "Held" means the refusal fired on that path. It does not
mean the ruling holds on every path.

## Confirmed

Both findings have the same mechanism. `asset.screen` and `asset.listed_low` refuse only through `asset.cost` and
`asset.basis`. On a property placed in service before 2025, those lines are read only while the asset is inside its
**GDS** recovery period. Once `asset.done` (`asset.year > asset.last`, forms/2025/asset.yaml:362) is true, the line 13
path never reads `asset.cost` or `asset.basis`. The interview therefore never asks the screen, the cost, the
business-use percentage or the listed-property question, and the return completes with $0 depreciation for that asset.
Property depreciated under ADS has a longer recovery period than under GDS. A filer still inside the ADS period is owed
depreciation that the tool never computes. This is the same class as BUG-0310: the refusal sits on a line the path does
not read.

### C1. ADS property whose GDS period has ended completes with $0 depreciation (Form 4562 line 22 / Schedule C line 13)

- **Rulings:**
  - `reviews/2025/render/f4562.md:82`, with sidecar `reviews/2025/render/f4562.rulings.json` entries 0–2 (lines 9, 15, 21).
  - `reviews/2025/render/sc.rulings.json` entry 7 (line 54; log heading `reviews/2025/render/sc.md:127`).
  - What they claim: "line 20 (ADS) through asset.screen ('you depreciate it under ADS'), each refusing asset.cost
    (asset.screened) ... With those refused the total is the lines listed." The same claim covers "an elected straight
    line or 150% declining balance method, or by a method other than the MACRS percentage tables".
- **Source:**
  - i4562 (2025) PDF p. 9, Line 17: "For tangible property placed in service in tax years beginning before 2025 and
    depreciated under MACRS (“MACRS asset”), enter the deductions for the current year." p. 9 also says MACRS "includes
    the General Depreciation System (GDS) and the Alternative Depreciation System (ADS)".
  - i4562 p. 13, Column (g): "Figure the depreciation deduction in the same manner as under GDS, except use the straight
    line method over the ADS recovery period and use the applicable convention."
  - p946 (2025) PDF p. 99, Table B-1, class 00.11 Office Furniture, Fixtures, and Equipment: class life 10, GDS 7, ADS 10.
  - p946 PDF p. 75, Table A-8 (straight line, half-year), 10-year column: year 10 "10.0", year 11 "5.0".
- **Prediction (made before running):**
  - Office furniture (class 00.11), $10,000 cost, 100% business use, placed in service in 2015 under ADS, half-year.
  - 2025 is year 11 of the 10-year ADS period, so line 17 is 5% × $10,000 = **$500** and Schedule C line 13 is $500.
  - Expected tool behaviour, given the ruling: a refusal from `asset.screen`.
- **Witnesses:**
  - `witnesses/asset_ads_2015_furniture.json`: stage14.asset.done with class `c00_11`, cost 1000000 and screen true.
  - `witnesses/asset_ads_2015_furniture_noscreen.json`: the same with the screen and cost answers removed.
  - `witnesses/asset_ads_2016_furniture.json`: placed in service 2016. That is year 10, so the prediction is 10% = $1,000.
  - Control: `witnesses/asset_prior7_screen_control.json` (a 2023 asset inside its GDS period, screen true) refuses
    `sc.line13` and `f1040.line24` on `asset.screened`.
- **Actual:**
  - All three witnesses evaluate to `sc[desk].line13` = **$0.00** and `f1040.line24` = $9,775.78, with no refusal.
  - The witness without the screen and cost answers gives the same values. Those inputs are not read.
  - Interview replay (full profile, 155 questions): status `complete`. `asset[pc].screen`, `cost` and `pct` are never
    asked.
- **Proposed fix:** put the `asset.screened` refusal (and `asset.listed_low`, see C2) on a line every asset reads, such
  as `asset.year`, `asset.done` or the class lookup. Another option is to ask whether the property is depreciated under
  ADS or another method before deciding `asset.done`.

### C2. Listed property used 50% or less, placed in service before its GDS period ended, completes with $0 (Form 4562 26(h)/line 27)

- **Rulings:**
  - `reviews/2025/render/f4562.md:96`, with sidecar `reviews/2025/render/f4562.rulings.json` entries 3–5 (lines 27,
    33, 39).
  - What they claim: "Listed property used 50% or less (line 27) is refused on the asset (asset.basis refuses on
    asset.listed_low ...)".
  - The same reliance appears in `reviews/2025/transcription/f4562.md:234` (rulings.json line 75, "the project reaches
    the same set because listed property used 50% or less is refused") and `transcription/f4562.md:251` (line 81, "the
    line 27 term ... is zero wherever the project admits the return, since that property is refused").
- **Source:**
  - i4562 PDF p. 15, Column (f): "For property placed in service after 1986 and used 50% or less in a qualified business
    use, depreciate the property using the straight line method over its ADS recovery period."
  - p946 Table B-1 (00.11: ADS 10) and Table A-8 (10-year, year 11: 5.0%), as in C1.
- **Prediction (made before running):**
  - Listed property in class 00.11, $10,000 cost, 40% business use, placed in service in 2015.
  - Business basis is $4,000. 2025 is year 11 of ADS 10, so the line 27 depreciation is 5% × $4,000 = **$200**.
  - Expected tool behaviour, given the ruling: a refusal on `asset.listed_low`.
- **Witness:** `witnesses/asset_listed_low_2015.json` (stage14.asset.done with class `c00_11`, cost 1000000, listed
  true, pct 40).
- **Actual:**
  - `sc[desk].line13` = **$0.00**, `f1040.line24` = $9,775.78, no refusal.
  - Interview replay: `complete`. `pct`, `cost` and `screen` are never asked, so the filer is never asked about low
    business use.
- **Proposed fix:** the same as C1. The `asset.listed_low` refusal must sit on a line read for every listed asset,
  including one whose GDS period has ended.

Limits of the evidence:
- Both findings were run on one fixture base (stage14.asset.done), class 00.11 only, placed in service in 2015 and 2016.
- Other classes whose ADS period is longer than their GDS period should behave the same way, by the same
  `asset.done` short-circuit, but they were not run.
- Vehicles (`scveh`) were not affected on the paths run (see H3).

## Tested and held

Each row: the ruling or claim, the gate that fired, and the witness. Values are from the evaluator. The full refusal
records are in `runlog.txt`.

| # | Ruling / claim | Protected case | Gate that fired (refusal line reached) | Witness |
|---|---|---|---|---|
| H1 | render/se.rulings.json entry 8 (8a): RRTA refused "through person.rrta ... Schedule 3 line 11 and Form 8959 line 1" | RRTA filer with Schedule C, wages above base | `person.se_rrta` refuses `se_line12` and `f1040.line24` (also `person.rrta` on s3.line11). **Note:** the protection holds, but through `person.se_rrta`, not the lines the ruling names. | se8a_rrta |
| H2 | render/person.rulings.json entry 51 (Step 1): plan with more than one Schedule C refused | SIMPLE (match) and SEP each with a second Schedule C | `person.plan_screened` refuses s1.line16 and f1040.line24 | plan_simple_two_sc, plan_sep_two_sc |
| H3 | render/f4562.rulings.json entry 4, vehicle limb (`scveh.placed` refuses on `scveh.low_use`) | owned 2023 car on actual expenses, use dropped to 43% | `scveh.low_use` refuses f1040.line24 | veh_prior_low_use |
| H4 | render/f1040 entry 1 (13a), render/qbi entry 0 (3), screens qbi.unsupported, completeness f1040#11 | cooperative patron / suspended loss with a Schedule C only (no REIT dividends) | `qbi.unsupported` refuses qbi.eligible, f8995.line15, f1040.line13a, line24 | qbi_unsupported_sc_only |
| H5 | render/scveh entries 24, 25, 27 and scveh.deepseek entry 4 (20a); completeness scveh#1 | leased vehicle on actual expenses with a lease inclusion amount (`sc.special` yes) | `sc.screened` refuses sc.line1 → f1040.line24 | scveh_lease_special |
| H6 | render/f1040 entry 6 (1a): inmate wages, 8t pensions refused via s1.line8_other | W-2 filer answering s1.line8_other yes | `s1.line8_other` refuses f1040.line8, line24 | f1040_1a_line8_other |
| H7 | render/ira.deepseek entry 4 (8): combat pay refused via ira.combat_gate; completeness f1040#14 (IRA limb only) | traditional IRA contribution with combat pay | `ira.combat_gate` refuses s1.line20, f1040.line24 | ira_combat (fixture stage16.refuse.ira.combat_pay, rerun) |
| H8 | render/ltc entry 0 (2(b)), completeness ltc#1, ltc#3: multi-business LTC / retired PSO refused by sc.hi_screen | LTC premiums only (line 1 = 0), hi_screen yes | `sc.hi_screened` refuses s1.line17, f1040.line24 | sehi_ltc_only_screen |
| H9 | tipjob.mixed refusal on tipjob.amount (cited in s1a rulings) | one employer, tips partly non-qualified | `tipjob.mixed` refuses s1a.line4c, line13 | tips_mixed_one (stage12 partial profile; s1a only) |
| H10 | f8880 ABLE refusal (`person.sav_able` on the prior-distribution inputs) | ABLE contributor with no other contributions | `person.sav_able` refuses f8880.line12, s3.line4, f1040.line24 | saver_able_only |
| H11 | completeness f8962#4, #5: claimable filer refused at return level via sa.dependent | claimable filer, standard-deduction path | `sa.dependent` refuses f1040.line12e, line24. The itemizing branch was checked by reading `sa.deduction` (refusal on the choose line itself), not run. | sa_dependent |
| H12 | render/s1 entry 0 (1), render/refund entry 0, screens refund.exc_tax / refund.not_2024 | 2024 dependent with worksheet used; refund for another year without itemizing | `refund.exc_who` and `refund.not_2024` refuse s1.line1, f1040.line24 | refund_exc_who, refund_not2024_notitemized |
| H13 | completeness dependent#8, f1040#15: AOC ban handled by f8863.ban_refused on line 7 | AOC with and without phaseout | `f8863.ban_refused` refuses f8863.line8, line19, f1040.line24 (on an LLC-only return the ban does not apply, and nothing refuses, as it should) | aoc_ban_phaseout, aoc_ban_nophaseout, aoc_ban |
| H14 | render/dependent entry 1 (2(c), second point), completeness f2441#2 | care for a qualifying person who is not a dependent | `f2441.nondependent_gate` refuses f2441.line11, f1040.line24 | f2441_nondependent |
| H15 | screens sb.fbar_required / sb.form8938 ("covered" by sb.unsupported); ira entry 2 (12a, Form 8815) | $300 of interest with a special item | `sb.unsupported` refuses f1040.line2b, line24 | sb_unsupported_small |
| H16 | render/person entries 3, 59, render/se entries 0, 2, 4, 6, 9, s8812 entry 3, s179 entry 2, completeness f2441#3, f2441#4 | statutory employee, SE screen, passive business, sc.special; SE screen with profit under $400 | `sc.screened` / `person.se_screened` refuse f1040.line24 | fx_refuse.statutory, fx_refuse.se_screen, fx_refuse.passive, fx_refuse.special, se_screen_under400 |

Broader sweep: `sweep/` holds the scripts and `sweep/flags.json` the raw flags.
- What it did: it flipped, one at a time, every Bool input that feeds a refusal gate within four steps. There were 136
  distinct inputs, each run on up to 12 completing stage fixtures from different fixture files: 1,561 evaluations.
- What it flagged: every case where the flipped answer made a gate true while `f1040.line24` still completed.
- Result: none of those inputs was read on its path. For every flagged case, removing the input left line 24 computed,
  so the interview would not ask it there.
- What this shows: on these fixtures, no gate input that is asked fails to refuse.
- What it cannot show: the C1/C2 kind of gap, where a relevant screen is never asked. The sweep only flips answers the
  fixtures already hold.

## Not tested

- **f8962 / f1095a rulings:** about 100 entries rest on `f8962.married_in_2025`, `void_form`, `marriage`, `alloc`,
  `other` and `s3.mfs`. No witness was built. The sweep shows these gates true with the return completing only on
  returns without Form 1095-A, where they are not read.
- **s3.mfs** (211 mentions): it refuses `scope.ready`. It was not run separately. Every witness above has another status.
- **g28 / sales / sd rulings** (sales.special, sales.digital, sales.bad_code, sd.other_forms, sd.carryover): these
  rulings record their own "checked:" runs, which were not repeated.
- **f1040 6b lump-sum election and the s1a 36b roster refusal:** these already have recorded checks or fixtures, which
  were not re-run.
- **Assets that have left their GDS period, beyond C1/C2.** These were not run:
  - classes other than 00.11;
  - property acquired in a like-kind exchange (an exchanged basis keeps the relinquished property's schedule, so it
    could run past the GDS period);
  - property depreciated under the elected 150% declining balance method. Its recovery period is the GDS period, so no
    gap is expected.
- **Representation rulings (priority 2):**
  - The 51 render-log representation rulings whose objection names a limiting rule were read.
  - None was turned into a witness except through H15 (ira 12a, Form 8815).
  - Transcription-log rulings classed "representation" or "scope;" (784 texts matched "scope;") were not reviewed
    individually.
- **Screen WIDE findings** (over-refusals): out of this audit's class.

## Counts

- **Rulings examined (read against the forms):** about 189. That is:
  - 42 distinct (form, line) "refusal located elsewhere" render rulings;
  - 41 completeness rulings classed "out of scope" or "covered";
  - 55 screen-review NARROW "covered" findings;
  - 51 render representation rulings.
- **Tested by execution:** about 47 ruling entries across 31 witness files, plus the 1,561-run sweep.
  - 46 of the 47 are the entries named in H1–H16 and in C1–C2 (counting sidecar duplicates for one printed line
    once).
  - The 47th is the transcription f4562 26(h)/28 pair, which shares a witness with C2.
- **Confirmed wrong:** 2 findings with one shared root cause. They contradict 7 ruling entries:
  - render f4562 entries 0–2 (line 22);
  - render sc entry 7 (line 13);
  - render f4562 entries 3–5 (26(h), asset limb);
  - transcription f4562 lines 75 and 81 of the sidecar (26(h), 28).

## Notes for the integrator

- No guard or hook blocked anything in this run.
- `tools/t.sh` and `tools/mk.py` rebuild every witness from its fixture case and overrides. The command for each
  witness is the `###` line of `runlog.txt`.
- Before the scripts were copied into `tools/`, they ran from a scratch directory, so early `runlog.txt` lines show
  scratch paths. The commands are otherwise the same.
- `tools/replay.py <witness>` drives the full-profile interview from a witness and lists the answers it never asked.
