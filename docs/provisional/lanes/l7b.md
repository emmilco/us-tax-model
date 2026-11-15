# Lane notes: 7b (other money received, other taxes, the rare situations)

Branch `lane/l7b`. Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no
model call was made. Form files: `s1`, `oi8z`, `s2`, `f8959`; order numbers only for the redesigned `s3` questions.

**For a successor.** The work is done by four small scripts kept outside the repository while the lane ran
(`/tmp/l7b/`: `gen.py`, `bank.py`, `fix_fixtures.py`, `autofix.py`); they are not needed to continue, every change they
made is in the commits. The state of each step is under "Status" below; read that first.

## Status

| Step | What | State |
|---|---|---|
| 0 | Order numbers and `seq` for the 26 `s3` entries (118, 126, 215, 225, 279, 290, 305, 318); boilerplate help deleted on my entries | done |
| 1 | `s2.amt`, `s2.other`, `f8959.unsupported` taken apart; the old ids are derived lines | done |
| 2 | `s1.line8_other` taken apart; the old id is a derived line | done |
| 3 | The amounts asked of everyone beneath yes or no parents; alimony beneath a plain parent | done |
| 4 | `$oi8z` and `oi8z.kind` wording and labels; `s1.cod_*`, `s1.uc_unsupported`, `s1.alimony_unsupported` reworded (bank only) | done as wording; not taken apart (see "Not done") |

All five steps are in one commit: the machine was shared and one build took nine minutes, so the steps were checked
together. Coverage rows: `interview/2025/coverage/other.yaml` (32 rows); one row each of `hsa.yaml` and
`credits.yaml` re-answered.

## The check (run and seen)

`tools/draft_check.sh` (the full check), run once on the final tree: the build, `test_fixtures` (1854 of 1854),
`interview_rules` (0 problems), `interview_coverage` (0 problems, 111 rows), `person_wording`, `spouse_self_test`,
`check_self_test`, `test_integration` (722 invocations), `properties`, `test_serve`, `draft_walk_self_test` and
`twins` passed; `render_check` failed because `rendered/2025/` had not been rewritten for the changed forms. After
`node engine/dist/main.js render`, `render --check` passes. The whole script was not run a second time (one run took
about 40 minutes on the shared machine), so "green" is twelve steps of one run and the thirteenth run alone.

## The derived-line technique (MAP 4.1): it works

Tried first on `f8959.unsupported`, then `s2.amt`, `s2.other`, `s1.line8_other`. The old id stops being an input and
becomes a Bool line (`op: test` with `any:` over its items, or `eq` for one item). The build accepts it as a refusal's
`when`; every reader in other lanes' files (`tipjob.col_c`, `s1a.line4b_calc`, `s8812.line22`, the seven `f8959`
lines, `s1.line9`) is untouched, and every fixture's expected refusal still names the old id as its `gate`, unedited.

Two things a lane meets when it does this:

- **A fixture path that ends in a refusal can meet a question it did not answer before**, because the question that
  refuses moved later in the order (`interview-check.ts`, "missing or repeated question"). Such fixtures state `null`
  for the questions they expect not to reach. The remedy is an input, not an expected value: the `null` becomes the
  question's default answer. Every such edit is listed under "Fixture inputs changed for other lanes' ids".
- The profiles `interview/2025/stage4.yaml` and `sales.yaml` list inputs by id and need the new ids.

## What the catch-alls became

Each row: the item, where it is asked now, and through which old id it refuses. "Caught" = no question is built
because another question refuses the same situation for every filer who has it (MAP 2.7); the check is stated.

### `s2.amt` (17 words, cost 20)

Read: `sources/2025/i6251.txt` "Who Must File". Its four tests are computations (Form 6251 line 7 greater than line
10; a general business credit; three credits; negative adjustments). **No test there is a fact a person can
recognize**, so MAP Part 5 question 6 is answered: the form-worded question has to stay as the last child, because
only a computation finds whether the tax is owed. The 2025 Form 1040 instructions no longer carry a worksheet for it
(read: the Schedule 2 line 2 text in `i1040gi-html.txt`; it says only "See the Instructions for Form 6251").

| Item | Now | Refuses through |
|---|---|---|
| Incentive stock options exercised and the stock kept (Form 6251 line 2i) | `s2.options_any` (parent, everyone) then `s2.iso` | `s2.amt` |
| Everything else | `s2.amt_owed`, reworded "Do you owe alternative minimum tax for 2025?", asked late (292) | `s2.amt` |

Not built: a paper question for private activity bond interest (Form 1099-INT box 9, Form 1099-DIV box 13), which
would sit beneath tax-exempt interest in lane 5a's topic. It is still covered by `s2.amt_owed`.

### `s2.other` (124 words, cost 20)

Read: the printed Schedule 2 (`f1040s2.txt`) and the Schedule 2 line instructions in `i1040gi-html.txt` (lines 1b to
1y, 5 to 19).

| Schedule 2 line | Item | Now |
|---|---|---|
| 1b, 1c | Clean vehicle credit taken by a dealer, to be repaid | **Caught** by `s3.ev_dealer`. The map proposed `s2.ev_repayment` for a 2024 purchase; the instructions for lines 1b and 1c tie them to Schedule A (Form 8936) of this return, that is, to a vehicle of 2025, which `s3.ev` then `s3.ev_dealer` asks. Not built |
| 1d, 1e, 1f, 1y, 16, 17a, 19, 17z (penalties tied to credits) | A credit of an earlier year to be paid back | `s2.credit_recapture` (291), everyone. The map put it beneath a business; the instructions name credits a person without a business can have taken (a vehicle charger, low-income housing), so it is not gated |
| 5, 6 | Tips not reported; wages with no social security tax withheld | **Caught** by `scope.other_income` today (its items 2 and 6) and by lane 9's `scope.pay_no_w2` after the merge |
| 5 (allocated tips), 13, 17h, 17k | Box 8 of a W-2; box 12 codes A, B, M, N; codes Z and K | `s2.w2_marks` (148), one paper check. The map's `s2.w2_code_z` is merged into it: the filer's act is the same (read box 12) and both refuse through `s2.other` |
| 9 | Household employment taxes | `s2.household_help` (parent, 159) then `s2.household_employee` |
| 14, 15 | Interest on deferred tax, installment sales | **Caught** by `sd.other_forms` (Form 6252; exists, refuses directly, asked of everyone) |
| 17b | Federal mortgage subsidy to be repaid | `s2.mortgage_subsidy` (215), asked only when mortgage interest is entered, like `s3.mcc` |
| 17d | Health savings account, testing period failed, no account in 2025 | `s2.hsa_testing` (193), everyone. With an account in 2025: `f8889.testing_prior`, `f8889.ira_prior` |
| 17e, 17f | Archer or Medicare Advantage MSA | **Caught** by `person.x_other` and `scope.schedule1` today; lane 9's `scope.archer_msa` after the merge (request below) |
| 17g | Charitable deduction recaptured | **Caught** by `oi8z.kind` = `charitable_recapture` |
| 17l | Accumulation distribution of a trust | **Caught** by `scope.schedule1` (trusts) and `sb.line8` today |
| 17n | Look-back interest | `s2.lookback` (267), asked only when the return has a Schedule C (`s1.has_sc`) |
| 17o | Tax for part of the year as a nonresident alien | **Caught** by `scope.other_income` item 1 today, `scope.nonresident` after the merge |
| 17p, 17q | Interest from Form 8621 | **Caught** by `scope.other_line16` items 4 and 5 today, `scope.pfic` after the merge |
| 20 | Section 965 installment | **Caught** by `s3.section965` |
| 17h, 17i (no W-2), 17j, 17k (no W-2), 17m, 1y and 17z write-ins | No plain parent | `s2.other_tax` (293), the residual question; the map's `s2.rare_excise` is merged into it (both are things a person learns only from a payer or a notice) |

### `f8959.unsupported` (67 words, one sentence)

| Item | Now |
|---|---|
| Church employee income | **Caught** by `scope.schedule1` items 2 and 3 today; lane 9's `scope.clergy`, `scope.church_exempt_wages` after |
| Other self-employment income outside Schedule SE | **Caught**: Schedule SE's sources are a Schedule C (asked; `person.se_screen` refuses the special cases), a farm, a partnership and clergy or church income, all refused at `scope.schedule1` today. I found no kind left; `f8959.other_se` is not built |
| Railroad compensation | **Caught** by `person.rrta` (direct refusal, every person) |
| Tips not reported, Form 8919 wages | **Caught** as Schedule 2 lines 5 and 6 above |
| Allocated tips (box 8), codes B and N | `s2.w2_marks`. These now refuse at `s2.other`, not at the Form 8959 lines: the same situations are refused, with Schedule 2's wording |
| Wage statement of a U.S. territory | `f8959.territory_w2` (148), everyone; refuses through `f8959.unsupported` |

### `s1.line8_other` (189 words)

| Line | Item | Now |
|---|---|---|
| 8a, 8d, 8l, 8n, 8o, 8q, 8s | | **Caught** as MAP 2.6 says; today by `scope.schedule1` (items 6, 9, 11), `sa.excluded_income`, `scope.other_line16` item 5, `person.x_other` |
| 8e | Long-term care insurance payouts, accelerated death benefits | `s1.ltc_payout` (161). The Archer MSA part: request to lane 9 below |
| 8k | Stock option income not on a W-2 | `s1.stock_options`, beneath `s2.options_any` (149) |
| 8m | Olympic and Paralympic medals and prize money | `s1.olympic`, beneath `s1.winnings_any` (160) |
| 8p | Excess business loss adjustment | **Caught** by the model itself: `s1.ebl` (computed from the Schedules C, refuses at `s1.line3`). Other business losses (a farm, a K-1) are refused at `scope.schedule1`. No question (N8) |
| 8t | Deferred compensation pension | `s1.nqdc_pension` (148, a W-2 box 11 check; the map had it in topic 170, but the paper is the W-2) |
| 8u | Pay for work while an inmate | `s1.inmate_wages` (161) |
| 8v | Digital assets received as income | `s1.digital_income` (161) |

## The amounts asked of everyone, and alimony

Each amount that every filer was asked ("zero if none") now sits beneath a yes or no parent. The five amounts that
were themselves printed lines (8g, 8h, 8i, 8j, 8r) were inputs under the line's own id; the input is renamed and the
printed line is now a derived line (the parent's Yes gives the amount, its No gives zero), so every expected value
keyed by the line id is unchanged.

| Parent (new) | Children | Note |
|---|---|---|
| `s1.uc_any` | `s1.uc_paid`, `s1.uc_repaid`, `s1.uc_unsupported` | `s1.uc_unsupported` reworded in the bank from 75 words to 21; it still holds two facts joined by "or" (paying into a state fund; repaying benefits of an earlier year). Not split: it is met only by the 3% with benefits |
| `s1.alimony_any` | `s1.alimony` (now "Was that alimony paid under an agreement made in 2018 or earlier?"), then `s1.alimony_received`, `s1.alimony_paid`, `s1.alimony_unsupported` | The parent says "since the start of 2023" so that a person with a recapture and no payment in 2025 (the third year) does not answer No; coverage row `other.alimony_recapture` |
| `s1.winnings_any` | `s1.gambling_winnings` (then `s1.gambling_pro`), `s1.prizes` (was `s1.line8i`), `s1.olympic` | One parent for gambling and prizes: one subject, winning something. After a Yes the two amounts are asked with "give 0 if none" |
| `s1.scholarship_any` | `s1.scholarship_taxable` (was `s1.line8r`) | Kept apart from winnings (N1), though it costs one more question |
| `s1.jury_any` | `s1.jury_pay` (was `s1.line8h`), then `s1.jury_to_employer` | |
| `s1.alaska_any` | `s1.alaska_dividend` (was `s1.line8g`) | |
| `s1.hobby_any` | `s1.hobby_income` (was `s1.line8j`) | |
| `s1.cod_any` (existed) | `s1.cod_amount`, `s1.cod_unsupported` | Reworded only |

**Alimony beneath "ever divorced or separated" was considered and not built.** A parent over one cheap child does
not pay for itself (N3: g = 1, q about 0.65, C = 1). The right gate is lane 1's `household.ever_married`, which is not
on this branch; see the requests.

## Cost and share table (NORMS section 3)

Shares marked *gf* are from `interview/2025/gate_frequencies.yaml`; the others are my judgment. Costs are my
estimates on the owner's scale (1 known at once, 5 a moment's thought or a look at a paper, 20 must find out what is
asked).

| Question | Asked of | Share answering yes | Cost of No | Cost of Yes | Beneath it |
|---|---|---|---|---|---|
| `s2.w2_marks` | everyone (a W-2 gate is requested) | under 1%, judgment | 3 (look at box 8 and box 12) | 3 | nothing: refuses |
| `s1.nqdc_pension` | everyone (same) | under 0.5%, judgment | 2 (box 11 is empty) | 5 | refuses |
| `f8959.territory_w2` | everyone | under 0.5%, judgment | 1 | 1 | refuses |
| `s2.options_any` | everyone | 2%, judgment | 1 | 1 | `s2.iso` (5), `s1.stock_options` (10); pays: 1 < 0.98 x 15 |
| `s1.inmate_wages` | everyone | under 0.5%, judgment | 1 | 1 | refuses |
| `s2.household_help` | everyone | 10%, judgment | 1 | 1 | `s2.household_employee` (5 to 8, three thresholds); pays: 1 < 0.9 x 6 |
| `s1.uc_any` | everyone | 3% *gf* (`unemployment`) | 1 | 1 | three questions, about 8; pays |
| `s1.alimony_any` | everyone | 0.3% *gf* (`alimony`) for an old agreement; 2% any alimony, judgment | 1 | 1 | `s1.alimony` and three more; pays |
| `s1.cod_any` | everyone | 0.6% *gf* | 1 | 2 | two questions |
| `s1.winnings_any` | everyone | 3% *gf* (`gambling`), more with prizes | 1 | 1 | amounts, about 6; pays |
| `s1.scholarship_any` | everyone | 5%, judgment | 1 | 1 | one amount (5 to 10: the taxable part needs thought) |
| `s1.jury_any` | everyone | 2%, judgment | 1 | 1 | amount |
| `s1.alaska_any` | everyone | 0.4%, judgment (Alaska's share of returns) | 1 | 1 | amount |
| `s1.hobby_any` | everyone | 1%, judgment | 2 ("is my side money a hobby?") | 2 | amount |
| `s1.ltc_payout` | everyone | under 0.5%, judgment | 1 | 1 | refuses |
| `s2.hsa_testing` | everyone | under 0.1%, judgment | 2 (the first clause, "in 2024 but not in 2025", settles it) | 10 | refuses |
| `s1.digital_income` | everyone | 1%, judgment | 1 | 1 | refuses |
| `s2.credit_recapture` | everyone | under 0.2%, judgment | 2 | 5 | refuses |
| `s2.amt_owed` | everyone | 0.15% *gf*-like (`s2.amt`) | **10 to 20: a filer cannot know without the computation** | 20 | refuses |
| `s2.other_tax` | everyone | under 0.1% | 3 | 5 | refuses |
| `$oi8z` | everyone | 5% *gf* | 3 | 5 | kind and amount |
| `s2.mortgage_subsidy` | mortgage interest entered | under 1% of those | 1 | 2 | refuses |
| `s2.lookback` | a Schedule C on the return | under 0.5% of those | 2 | 5 | refuses |

## Ids

**Added (inputs):** `s2.options_any`, `s2.iso`, `s2.amt_owed`, `s2.w2_marks`, `s2.household_help`,
`s2.household_employee`, `s2.mortgage_subsidy`, `s2.hsa_testing`, `s2.credit_recapture`, `s2.lookback`,
`s2.other_tax`, `f8959.territory_w2`, `s1.ltc_payout`, `s1.stock_options`, `s1.olympic`, `s1.nqdc_pension`,
`s1.inmate_wages`, `s1.digital_income`, `s1.uc_any`, `s1.alimony_any`, `s1.winnings_any`, `s1.scholarship_any`,
`s1.jury_any`, `s1.alaska_any`, `s1.hobby_any`.

**Added (gate and helper lines):** `s2.no`, `s2.iso_if_options`, `s2.household_employee_if_help`,
`s2.has_mortgage_interest`, `s2.mortgage_subsidy_if_interest`, `s2.lookback_if_business`,
`s1.stock_options_if_options`, `s1.olympic_if_winnings`, `s1.uc_paid_if_any`, `s1.gambling_winnings_if_winnings`,
`s1.alimony_if_any`.

**No longer inputs, kept as derived lines with the same id:** `s2.amt`, `s2.other`, `f8959.unsupported`,
`s1.line8_other`, and the printed lines `s1.line8g`, `s1.line8h`, `s1.line8i`, `s1.line8j`, `s1.line8r`.

**Inputs renamed:** `s1.line8g` to `s1.alaska_dividend`, `s1.line8h` to `s1.jury_pay`, `s1.line8i` to `s1.prizes`,
`s1.line8j` to `s1.hobby_income`, `s1.line8r` to `s1.scholarship_taxable`.

**Now gated (marked `gated_by`):** `s1.uc_paid`, `s1.gambling_winnings`, `s1.alimony`, and the five renamed amounts
(each gated by its printed line, which is the gate line; the name does not follow `<input>_if_<condition>`).

**Ids changed from the map:** `s2.w2_code_z` merged into `s2.w2_marks`; `s2.rare_excise` merged into `s2.other_tax`;
`s2.ev_repayment`, `s2.business_credit_recapture` (built as `s2.credit_recapture`, not gated on a business),
`s1.excess_business_loss` and `f8959.other_se` not built, for the reasons in the tables above; `s2.amt` is no longer a
question (its residual is `s2.amt_owed`); `s2.household_help` is a new parent over `s2.household_employee`;
`s2.options_any` is a new parent over `s2.iso` and `s1.stock_options`; `s1.winnings_any`, `s1.uc_any` and the other
`_any` parents are new.

**Fixture inputs.** Where a fixture stated an old catch-all, it now states one item with the same value:
`s2.amt` as `s2.amt_owed`, `s2.other` as `s2.other_tax`, `f8959.unsupported` as `f8959.territory_w2`,
`s1.line8_other` as `s1.ltc_payout` (the fixtures do not say which item their filer had). Where a fixture states an
amount that is now beneath a parent, the parent is stated true. No expected value or refusal was edited.

## Candidates for one tick-list

Each member is its own yes or no question, in one order number with the seq shown (children of a member follow it
and are not shown to a filer who does not tick it).

**"Look at your W-2s" (order 148; three members):**
1. `s2.w2_marks` (seq 1): an amount in box 8, or the letter A, B, K, M, N or Z in box 12
2. `s1.nqdc_pension` (seq 2): box 11 shows money paid to you from an employer's deferred pay plan
3. `f8959.territory_w2` (seq 3): a wage statement from an employer in Puerto Rico or another U.S. territory

**"In 2025, did you get any of these?" (order 160; six members):**
1. `s1.uc_any` (seq 1): unemployment benefits
2. `s1.alimony_any` (seq 5): alimony, paid or received since the start of 2023
3. `s1.cod_any` (seq 10): a debt canceled or forgiven by a lender
4. `s1.winnings_any` (seq 13): money or a prize won (gambling, a lottery, a raffle, a contest, an award)
5. `s1.scholarship_any` (seq 18): a scholarship, a fellowship or a grant for study
6. `s1.jury_any` (seq 20): pay for serving on a jury

**"And any of these?" (order 161; five members):**
1. `s1.alaska_any` (seq 1): an Alaska Permanent Fund dividend
2. `s1.hobby_any` (seq 3): money from a hobby or pastime not run as a business
3. `s1.ltc_payout` (seq 5): a payout from a long-term care insurance policy, or part of a life insurance death benefit paid early
4. `s1.inmate_wages` (seq 6): pay for work done while in a jail or prison
5. `s1.digital_income` (seq 7): crypto received as pay, as a reward, or from mining or staking

The map placed `s1.inmate_wages` with the jobs (149) and `s1.digital_income` with sales of investments (275); both
are in 161 so that the group is one order number. If the tick-list is not adopted they go back (bank only).

Not candidates (each is one question with children, or a residual that must come last): `s2.options_any`,
`s2.household_help`, `s2.hsa_testing`, `s2.credit_recapture`, `s2.amt_owed`, `s2.other_tax`, `$oi8z`.

## Before and after (run and seen: `draft-walk`, the twelve personas, all with their ends unchanged and no problem)

The one-W-2 filer (`01_single_w2`), this lane's questions only (ids of `s1`, `oi8z`, `s2`, `f8959`):

| | Questions | Prompt words | Which |
|---|---|---|---|
| Before | 14 | 862 | `f8959.unsupported` 67, `s1.alimony` 95, `s1.line8_other` 189, `$oi8z` 23, `s1.cod_any` 27, `s1.gambling_winnings` 61, `s1.line8g` 40, `s1.line8h` 24, `s1.line8i` 78, `s1.line8j` 42, `s1.line8r` 50, `s1.uc_paid` 25, `s2.amt` 17, `s2.other` 124 |
| After | 21 | 363 | `s1.nqdc_pension` 17, `f8959.territory_w2` 16, `s2.options_any` 19, `s1.uc_any` 7, `s1.alimony_any` 23, `s1.winnings_any` 20, `s1.jury_any` 10, `s1.ltc_payout` 21, `s1.inmate_wages` 14, `s1.digital_income` 20, `s1.cod_any` 15, `s1.scholarship_any` 14, `s1.alaska_any` 10, `s1.hobby_any` 18, `s2.amt_owed` 8, `s2.w2_marks` 25, `s2.household_help` 24, `s2.hsa_testing` 29, `s2.credit_recapture` 16, `s2.other_tax` 16, `$oi8z` 21 |
| After, with the three tick-list groups each one screen | 10 screens | 363 | 14 of the 21 are group members (3, 6 and 5) |

The count rose by seven and the reading fell by 499 words (58%). The longest question of the topic went from 189
words to 29. Every one of the 21 is answered No (or an empty list) by this filer. Whole walk of the same persona:
86 questions and 6,777 prompt words before, 93 and 6,278 after (help 2,376 to 2,561 words). Each of the ten personas
that complete moved by the same seven questions (eight for the two that meet `s2.mortgage_subsidy` or `s2.lookback`).
The return with nothing at all (the minimal return of `interview-rules`): 82 questions before (the map's figure), 89
after (the check's own line, "every gate closed asks 89 question(s)").

Not measured: a filer with the topic's common case. No persona has unemployment benefits, winnings or a canceled
debt. By the bank, a filer with unemployment benefits answers three more questions than the one above
(`s1.uc_paid`, `s1.uc_repaid`, `s1.uc_unsupported`; the coverage row `other.unemployment` walks that path).

Where the seven come from, and what would take them back: three W-2 or wage-statement checks where one sentence of
`f8959.unsupported` and one bullet of `s2.other` stood; `s2.options_any`, `s2.household_help`, `s2.hsa_testing`,
`s2.credit_recapture`, `s2.other_tax` where `s2.other` stood (one question became six, with `s2.w2_marks`); four
items of `s1.line8_other` that have no plain parent (`s1.ltc_payout`, `s1.inmate_wages`, `s1.digital_income`, and
`s1.nqdc_pension` already counted); `s1.scholarship_any` apart from `s1.winnings_any`; less the two amounts that
merged beneath `s1.winnings_any` and the items another question already catches. Each is one fact a person knows at
once; none has a plain parent that most people could answer No to more cheaply than the fact itself (N3), which is
why they are tick-list candidates and not layered.

## Order: what the walks show

`order` and `seq` are set as the map's slot table says. In the walk of `01_single_w2` (after), this lane's questions
arrive as follows; the engine was not changed.

| Seen | Expected by order number | What I think it waits on |
|---|---|---|
| `s1.nqdc_pension`, `f8959.territory_w2` (148) come at 59 and 60, after the whole of Schedule A, the business list and Form 5695; `s2.w2_marks` (148 seq 1) comes at 84 | Directly after the W-2 boxes | The Schedule 2 questions are reachable only once a Schedule 2 line is (Form 1040 lines 17 and 23, near the end). Target wanted in `full.yaml`: `s2.other` and `s2.amt` (or `s2.line21`), `s1.line9`, `f8959.line1` |
| `s2.household_help` (159), `s2.hsa_testing` (193), `s2.credit_recapture` (291), `s2.amt_owed` (292), `s2.other_tax` (293) come together at 83 to 88, with `s2.amt_owed` first | Each in its topic; `s2.amt_owed` and `s2.other_tax` last | The same |
| The `s1` yes or no questions come together (64 to 74) but not in `seq`: `s1.uc_any`, `s1.alimony_any`, `s1.winnings_any`, `s1.jury_any`, `s1.ltc_payout`, `s1.inmate_wages`, `s1.digital_income`, then `s1.cod_any`, `s1.scholarship_any`, `s1.alaska_any`, `s1.hobby_any` | 160 by `seq`, then 161 | Line 9's sum becomes reachable one term at a time |
| A child can be asked before its elder sibling: `s1.olympic` before `s1.prizes`; `s1.uc_unsupported` before `s1.uc_repaid`; `s1.alimony_unsupported` before the two amounts (seen in the coverage walks: rows that answered the amounts were stale) | By `seq` | A refusal's `when` is reached before the amount lines beside it (cause 2 of T-284) |
| `s3.kerosene` (225) comes before `s3.foreign_any` (279), then `s3.credit_bond` (290), `s3.disability_retired` (118), `s3.ev` (225) | By order number | Reachability, not the bank |
| `s2.mortgage_subsidy` (215 seq 2) comes five questions after `s3.mcc` (215 seq 1) in `02_couple_children_mortgage`, and both about 45 questions after `sa.line8a` | Directly after `sa.line8a` | The same |
| `s2.lookback` (267) is question 134 of 141 in `05_self_employed` | With the business | The same |

## Requests to other lanes and to the stitch

1. **A gate "a W-2 is listed"** (order agent or lane 3; MAP 4.6, 4.8 item 4). `s2.w2_marks` and `s1.nqdc_pension` are
   questions about a W-2 and are asked of everyone, because no line counts the W-2s (the per-person sums are amounts,
   and I may not add a line to `person.yaml` or `w2.yaml`). Their help says "With no W-2, answer No." Wanted: a Bool
   line true when any person lists a W-2; then each gets a gate line as `s2.lookback` has. `f8959.territory_w2`
   should stay ungated: a filer whose only wage statement is a Form 499R-2/W-2PR may not list it as a W-2.
2. **Lane 1, `household.ever_married`.** When it exists, `s1.alimony_any` is asked only of a filer who was ever
   married (N8: never-married filers have no alimony). Not gated now: the fact is not on this branch.
3. **Lane 9, `scope.archer_msa`.** Its words must cover money taken out of an Archer MSA or a Medicare Advantage MSA
   (Schedule 1 line 8e, Form 8853; Schedule 2 lines 17e and 17f), not only the deduction. `s1.ltc_payout` covers only
   the long-term care and accelerated death benefit part of Form 8853. Until then `person.x_other` (item 3) and
   `scope.schedule1` (item 16) are what refuse it on this branch.
4. **Lane 9, `scope.pay_no_w2`.** It becomes the only asker of tips not reported to an employer and of wages on
   which no social security tax was withheld (Forms 4137 and 8919). `s2.other` and `f8959.unsupported` no longer
   name them. On this branch `scope.other_income` (items 2 and 6) still refuses them.
5. **Lane 5a.** A paper question beneath tax-exempt interest: "Is there an amount in box 9 of a Form 1099-INT or box
   13 of a Form 1099-DIV?" (private activity bond interest, an alternative minimum tax item). It would refuse
   through `s2.amt`; today only `s2.amt_owed` covers it.
6. **Order agent.** See "Order: what the walks show".
7. **Coordinator, the merge.** Fixture inputs in other lanes' fixture files were changed where they stated my old
   ids (a rename of the key, value unchanged), and in two stage4 refusal fixtures three withheld answers of lane 3's
   questions (`s1a.tips`, `s1a.overtime`, `s1a.carloan`: `null` became `false`) because the refusing question now
   comes after them: `stage4.refuse.8959` (`fixtures/2025/f8959.json`) and `stage4.refuse.scope.credits`
   (`fixtures/2025/scope.json`). The second is caused by the `s3.adoption*` order number (2 to 126).
   `engine/src/generate.ts` (the list of inputs the return generator does not draw), `engine/src/interview-rules.ts`
   (New York's minimal return now also says yes to `s1.uc_any`) and `engine/src/umbrella-what-if.ts` (lists of ids)
   were edited for the new ids; other lanes may touch the same lists.

## For the owner

1. **Alternative minimum tax cannot be asked plainly.** Whether it is owed is a computation, and the only question
   that covers every case is "Do you owe alternative minimum tax for 2025?", which a filer cannot answer (cost 10 to
   20, asked of everyone). The remedy is not wording: the tool has the figures for the first lines of Form 6251
   (taxable income, the state tax deduction or the standard deduction, the exemption and its phase-out, capital
   gains). A computed screen could ask the question only of the few returns where the tentative minimum tax comes
   near the regular tax, as Form 8960 is reached only above its threshold. That is new arithmetic, so it was not
   built in this redraft.
2. **The count rose, the reading fell.** See "Before and after". A filer with nothing answers more questions in
   this topic than before, each one short. With the three tick-list groups the screens are fewer than before.
3. **`$oi8z` prepares only two kinds of other income** (trade adjustment wage payments and kickbacks); every other
   kind, "something else" included, ends the interview (`oi8z.figured`, unchanged). So the list is nearly a refusal
   question. It is worded as a list still; a yes or no "Did you have any other taxable income you have not been
   asked about?" with the list beneath it would be plainer.
4. **`s2.mortgage_subsidy` is asked only when mortgage interest is entered** (as the map says). A person who paid
   off the subsidized loan before 2025 and sold the home in 2025 within nine years is not asked. Rare; say if it
   should be asked of everyone who sold a home once lane 5b's sale question exists.
5. **Refusals that changed place, not substance.** A W-2 with box 8 or codes B or N was refused at the Form 8959
   lines (when `f8959.unsupported` was asked first); it is now refused at Schedule 2 (`s2.other`), with that
   refusal's words.

## Unsure

- `s2.household_employee` states the three Schedule H tests from the Form 1040 instructions (Schedule 2 line 9). I
  did not read the Schedule H instructions (not looked for in `sources/2025/`); the exclusions there (a spouse, a
  child under 21, a parent) are not in the help.
- `s1.scholarship_taxable`: the prompt asks for the part "for room, board, travel or anything other than tuition and
  required course costs", from the line's own source text. A person not studying for a degree is told in the help
  to give the whole amount. This is the hardest of the new children (cost 5 to 10).
- `s2.hsa_testing`: one question holding the fact (an account in 2024, none in 2025) and the condition. I did not
  check in `f8889.yaml` whether a person with no account in 2025 can be asked `f8889.testing_prior`; the existing
  coverage row `hsa.testing_period_no_account_left` says not, and now answers `s2.hsa_testing`.
- The share figures marked judgment.
- Help over the map's 40 words: `s2.other_tax` (58) and `s2.credit_recapture` (56), each with the 17-word sentence
  that says what a Yes does; their examples are what tells a filer the answer is No. Prompts over 40 words:
  `s1.cod_unsupported` (60) and `s1.alimony_unsupported` (45), the two lists not taken apart.
- No row was written to `research/costs/agent_runs.jsonl` from this worktree; the launcher records the run.
- `s1.alimony_unsupported` and `s1.cod_unsupported` are still lists of several refusing facts joined in one
  question (43 and 60 words). They are met only after two Yes answers; taking them apart is model work not done.

## Review debt

Every form line added or changed has no transcription, render or class M review: all lines listed under "Ids", and
`s2.amt`, `s2.other`, `f8959.unsupported`, `s1.line8_other`, `s1.line8g` to `s1.line8r`, `s1.has_uc`,
`s1.line7_figured`, `s1.has_gambling`, `s1.line8b`, `s1.line2a`, `s1.line19a` (readers moved to gate lines). The
question reviews of every bank entry of `s1`, `oi8z`, `s2`, `f8959` are stale. The cites of the new inputs name the
printed line only (for example "Schedule 1 (2025), line 8u"); they carry no quotation and were not checked by a
tool. `reports/`, `canonical/` and `rendered/` were rewritten by the build.

## Not done, in rank order

1. A W-2 gate for `s2.w2_marks` and `s1.nqdc_pension` (request 1).
2. `s1.alimony_unsupported`, `s1.cod_unsupported`, `s1.uc_unsupported` taken apart into one fact each.
3. `$oi8z` as a yes or no parent with the list beneath (owner item 3).
4. The private activity bond question (request 5).
5. `oi8z.amount`, `s1.cod_amount`: read in the persona walks only by their bank text; no persona has them.
