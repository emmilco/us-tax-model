# Lane notes: 6b (business vehicles and equipment)

Branch `lane/l6b`. Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no
model call. Form files: `scveh`, `asset`, `s179`, `f4562`, `mq`. Bank entries: `$scveh`, `scveh.*`, `$asset`,
`asset.*`, `s179.*`. Order numbers: 255 (vehicles), 257 (equipment), 258 (the section 179 carryover and its interest
question); 256 is unused.

A successor continues from "State of the work"; "What is checked" says what each commit was checked with.

## State of the work

| # | Step | State |
|---|---|---|
| 1 | `s179.line10` (77 words, asked of everyone) beneath a plain parent `s179.prior_form` | done, commit `9694f4ab` |
| 2 | The catalog's tested rewrites V1 (`scveh.owned` after the method) and A1 (`asset.not179` after the amount) | done, same commit |
| 3 | The standard mileage path: order, words, `scveh.smr_ok` (62 words) taken apart | done, commit `54c16d87` |
| 4 | `asset.screen` (843 words) taken apart into 17 questions | done, commit `54c16d87` |
| 5 | `scveh.screen` (732 words) taken apart into 19 questions | done, commit `54c16d87` |
| 6 | Order 255/257/258 and a `seq` for every question; plain words for the common questions; labels for every choice | done, commit `54c16d87` |
| 7 | 42 coverage rows (`interview/2025/coverage/vehicles_equipment.yaml`); persona `13`; four rows of `credits.yaml` lose two answers; the return generator | done, commits `54c16d87` and `1bf18c34` |
| 8 | Not done: see "Not finished, in rank order" | |

Rank differs from the map's in one place: the map puts `scveh.screen` before `asset.screen`. In
`forms/2025/scveh.yaml` the vehicle screen's refusal sits on `scveh.cost`, which is read only for a vehicle on actual
expenses that is owned; the typical vehicle (standard mileage) never met it (baseline walk `05`, questions 112 to
115). `asset.screen` is met by every item of equipment listed. Both are done, so the difference no longer matters.

How the second commit was made (so it can be redone or adjusted): the scripts in `docs/provisional/lanes/l6b_work/`.
`split.py <spec>` takes a screen input apart from a spec (`asset_spec.py`, `scveh_spec.py`: each child's id, the
statement kept as the form line's label, the question, and the fact that opens it); `smr.py` did `scveh.smr_ok`;
`fixtures.py` rewrote the fixture inputs and defaults; `bank.py` writes every bank entry of the lane (order, `seq`,
prompts, help, labels); `coverage.py` writes the coverage rows from the bank's `seq` numbers. `split.py`, `smr.py` and
`fixtures.py` run once (they are not idempotent); `bank.py` and `coverage.py` can be rerun after an edit.

## Step 1. The carryover (`s179`)

What a filer met: `s179.line10`, 77 words, an amount, asked of everyone including a filer with no business (baseline
walk `01`, observation 22).

Now: `s179.prior_form` (yes or no): "Do you (or, on a joint return, your spouse) have a deduction for business
equipment left over from an earlier year?" Beneath a Yes, `s179.carryover` (the amount, read from line 13 of the last
Form 4562).

Model (`forms/2025/s179.yaml`):

- New input `s179.prior_form` (Bool). New input `s179.carryover` (NonNegDollars), `gated_by`
  `s179.carryover_if_prior_form` (new gate line: the amount when `prior_form` is true, `s179.zero` otherwise).
- `s179.line10` keeps its id, its printed number and its label, and is now a copy of the gate line (MAP 4.1.2: the old
  id stays, as a derived line; the technique works, the build accepts it). Its readers are untouched: `s179.mfs`,
  `s179.line9_10`, `s179.orphan`, and `sc.ho_s179_max` in lane 6a's `sc.yaml`, which is why the old id could not
  simply be marked `gated_by`.
- The refusal of a carryover with no business (`s179.orphan`) is reached as before: the parent is asked of everyone.
  That is why the parent is not beneath the business list.

Ids: the map's wording for `s179.prior_form` ("Does your 2024 return, or the last one you filed with a business,
include Form 4562 with an amount on line 13?") names the thing by a form number, which a filer with no business cannot
answer without finding out what Form 4562 is (N6; the owner's second calibration example). I kept the id and asked the
fact; the paper cue is in the help and in the child. `s179.carryover` is new (the map did not name the child).

Who could answer No wrongly: an owner who elected section 179 years ago and does not remember that part was held
over. The cost of the error is a deduction not taken. The guard is the help's paper cue; a second question would be
asked of everyone and does not pay for itself (N3).

## Step 3. The standard mileage path (`scveh`)

The typical vehicle (the owner's own car, by the mile) met four questions, 114 words, one of them `scveh.smr_ok`
(62 words, two rules joined by "if you own / if you lease" and an exception in parentheses). It now meets five:

| seq | Question | Words as stored (with the frame) |
|---|---|---|
| 2 | `scveh.method`: "How do you want to figure what this vehicle cost the business in 2025?" with two labelled choices | 17 |
| 3 | `scveh.miles_business`: "How many miles did you drive it for this business in 2025? Do not count driving between home and your regular workplace." | 25 |
| 4 | `scveh.parking` | 18 |
| 5 | `scveh.smr_always`: "Have you used the standard mileage rate for this vehicle every year you have used it for the business? (Answer Yes if 2025 is the first year.)" | 30 |
| 7 | `scveh.fleet`: "In 2025, did you use five or more vehicles in the business at the same time?" | 19 |

`scveh.smr_first` (seq 6: "Do you own this vehicle, and did you use the standard mileage rate for it in the first
year you used it for the business? (Answer No if you lease it.)") is asked only after a No to `smr_always`.

Model: `scveh.smr_ok` keeps its id and its refusal (`scveh.smr_bad`) and is derived: not `fleet`, and (`smr_always`
or `smr_first`). The old question's full text is its label. Same facts, same end: an owner who used the rate in the
first year but not every year answers No then Yes and goes on, as a Yes did before; a lessee who did not use it for
the whole lease answers No then No and is refused, as a No did before.

Unsure: `scveh.fleet` is a fact about the business, asked once per vehicle (the old question had it per vehicle too).
With one vehicle listed it is a strange question. It could be asked only when the business lists five or more
vehicles, but the rule counts vehicles "used in the business at the same time" whether or not expenses are claimed
for each, so a count of the list does not settle it. Left as it is; the owner may prefer to drop it into the help of
the list question.

## Steps 4 and 5. The two screens

Each screen was one yes/no input whose Yes refused. Each is now a derived line with the same id (`asset.screen`,
`scveh.screen`), true when any child is true, so the refusal is the same gate with the same wording as before
(`asset.screened`, `scveh.screened`; MAP 4.1.3). The old question's whole text is the derived line's label
(MAP 4.1.4). A child that only some entries can meet has a gate line (`<child>_if_<fact>`) and is asked only of them.

Every item of the old lists, and where it went. "Parent" means a question whose Yes refuses nothing and only opens
children.

### `asset.screen` (843 words; every item of equipment) → 17 inputs

| New question | Asked of | Items of the old list it holds |
|---|---|---|
| `asset.kind_excluded` | every item | real property or land; a car, truck or other vehicle; a film, videotape or sound recording; an aircraft (from the "long production period, an aircraft" item) |
| `asset.software` (parent) → `asset.software_spread` | every item → software | computer software, unless placed in service in 2025 and deducted in full in 2025 |
| `asset.industry` (parent) → `asset.industry_item` | every item → businesses of those kinds | reuse and recycling property; the six named special classes; the land clearing and grading improvement for utility property; the two section 168(k)(9) kinds (utility, floor plan financing) with a special allowance |
| `asset.long_production` | every item | property with a long production period; qualified production property |
| `asset.got_other` | every item | like-kind exchange, involuntary conversion, trade-in, related person, gift or inheritance |
| `asset.before_2017` | every item | acquired before September 28, 2017 |
| `asset.used_before` | 2025 items with a special allowance | a special allowance claimed and original use did not begin with you (the rebuilt-property rule is in the help) |
| `asset.ended_2025` | every item | disposed of, a portion disposed of, or converted to personal use in 2025 |
| `asset.basis_changed` | every item | basis adjusted other than by depreciation; basis reduced by a credit or deduction (the seven examples are in the label; six in the help) |
| `asset.use_changed` | items placed in service before 2025 | business use percentage changed since placed in service |
| `asset.short_year` | every item | a tax year shorter than 12 months |
| `asset.method_other` | every item | ADS, straight line or 150% declining balance elected; a method other than the tables; a general asset account; amortized |
| `asset.ads_required` | every item | ADS required (the four cases are in the label; the question names them in short) |
| `asset.outside_use` | every item | used predominantly outside the United States; tax-exempt use or tax-exempt bond financed property |
| `asset.qbu_low` | listed property | listed property whose qualified business use is 50% or less (the four excluded uses) |

Deleted, because an earlier answer settles it (N8): "it was placed in service before 2005" (`asset.placed` offers
2005 to 2025 only).

An ordinary 2025 purchase meets 13 of these (all but `software_spread`, `industry_item`, `use_changed`, `qbu_low`),
each answered No: 334 words as shown in the walk of persona `13`, in place of 843.

### `scveh.screen` (732 words; a vehicle on actual expenses that is owned) → 19 inputs

| New question | Asked of | Items of the old list it holds |
|---|---|---|
| `scveh.records` (a No refuses) | every such vehicle | no adequate records of business use |
| `scveh.got_other` | every | a trade-in or from a related person; an involuntary conversion or a like-kind exchange |
| `scveh.before_2017` | placed in service in 2025 | placed in service in 2025 but acquired before September 28, 2017 |
| `scveh.used_before`, `scveh.bonus_excluded` | 2025 with a special allowance | original use did not begin with you; the two section 168(k)(9) kinds |
| `scveh.prior_bonus`, `scveh.prior_smr`, `scveh.prior_low_use` | placed in service before 2025 | a special allowance in an earlier year; the standard mileage rate in an earlier year; business use 50% or less in an earlier year |
| `scveh.converted` | every | converted from personal to business use during 2025; from business to personal use during 2025 |
| `scveh.disposed` | every | disposed of in 2025 |
| `scveh.basis_changed` | every | a substantial improvement; basis reduced by a clean-fuel deduction or vehicle credit; basis reduced by a casualty |
| `scveh.short_year` | every | a tax year shorter than 12 months |
| `scveh.for_hire` | every | transporting persons or property for hire; an ambulance or hearse |
| `scveh.investment` | every | used in 2025 for investment |
| `scveh.others_use` (parent) → `scveh.leasing`, `scveh.exempt_use`, `scveh.qbu_low` | every → vehicles others use | the business of leasing passenger automobiles; purchased and leased to others (with its exception); used by a tax-exempt organization, a governmental unit or a foreign person (with the two exceptions); qualified business use 50% or less |
| `scveh.method_other` | every | ADS required (for example used predominantly outside the United States) or ADS, straight line or 150% declining balance elected |

Deleted (N8): "placed in service before 2019" (`scveh.placed` answers it, and `scveh.too_old` refuses it);
"an electric vehicle placed in service before 2007" (no vehicle placed in service before 2019 gets this far).

A vehicle bought in 2025 with the special allowance meets 13 (343 words as shown in the walk of persona `13`, in
place of 732), a vehicle of an earlier year 14.

### Who could answer No wrongly, and the guard

| Parent | Who | Guard |
|---|---|---|
| `asset.industry` ("Is your business a utility or energy producer, a recycler, a rent-to-own dealer, a motor racing track, or a dealer that finances its stock with a loan secured by it?") | A business outside those trades that owns one such item (a natural gas gathering line held by an investor). | None built. The child list holds trade-specific property, so the risk is small; a successor could ask the child of everyone whose `asset.class` is a utility or energy class. |
| `scveh.others_use` ("Does anyone but you use this vehicle (someone you lease or lend it to, a relative, a co-owner, or someone who gets its use as pay), or is any of its use for entertainment?") | An owner whose own use includes a use "nondeductible under section 274" that is not entertainment. I do not know what else that phrase covers for a vehicle; the old list did not say either. | None. For the owner. |
| `asset.software` | Nobody: a filer knows whether the item is software. | |
| `asset.method_other` | An owner whose preparer chose straight line years ago and who does not know it. | The same person could not answer the old screen either; the help says "If you have never chosen a depreciation method for it, the answer is No", which is the old default. |

### Places I was unsure

- "Related person" is asked as "a relative or a business you control". That is my gloss; the statute's definition
  (section 179(d)(2), section 267) is wider (certain trusts, corporations by share of ownership) and narrower (not
  every relative). The label keeps "related person". A reviewer should set the words.
- `asset.long_production`: I did not write the statute's tests for a long production period (I recall a production
  period over one year and a cost over $1 million, but did not check it against an archived source), so the question
  uses the term with a short gloss.
- `asset.before_2017` is asked of every item because the old list said "you acquired it before September 28, 2017"
  with no condition, though the form supports items placed in service from 2005. Read literally the old screen
  refused every item acquired before that date, which makes the years 2005 to 2017 of `asset.placed` unreachable for
  anything but an item bought earlier and first used later. The vehicle screen has the condition "placed in service
  in 2025". I kept the literal reading (N9); see "For the owner".
- The two `short_year` questions are a fact about the person, asked per item. A single question about the person
  could replace them, but "any tax year since you placed it in service" depends on the item. Left per item.

## The order the questions arrive in (seen in the walks)

`seq` is set as the foot of this file lists, but a question is asked only once it is reachable, and a line's refusal
entries are decided before the line's own inputs are read. So the walks show:

- **By the mile** (persona `05`, questions 125 to 130): the list, the method, parking, `smr_always`, `fleet`, and the
  miles last. `scveh.smr_bad` is a refusal entry on `scveh.smr_amount`, so the two rate questions are decided before
  the miles are read. Waiting on: cause 2 of T-284 (MAP 4.8.1(a)).
- **Actual expenses, owned, 2025** (persona `13`, 125 to 154, 30 questions): the list, method, parking,
  `employee_use`, the three mileages, running costs, owned, the year, then the 11 ungated screen questions, the weight
  question, the section 179 amount, the special allowance choice and its three questions, the two questions that
  depend on it, and only then the cost and the quarter. The cost comes late because the screen is a refusal entry on
  `scveh.cost`. For a filer this is the right way round for N11 (every refusing fact before the amount is typed) and
  the wrong way round for a story (the price after the depreciation choices).
- **Equipment, 2025** (persona `13`, 155 to 179, 24 questions): the list, the class, the year, then the percentage
  of business use, `listed` and the section 179 amount, then the screen questions, `not179`, the special allowance
  questions, and the cost and quarter last. The percentage, `listed` and the section 179 amount come before the screen
  because `asset.listed_low` and `asset.s179_bad` are refusal entries on lines read before `asset.cost`.
- **Equipment of an earlier year**: the class, the year, then the screen at once (`asset.done` carries the screen's
  refusal first).
- `s179.prior_form` is the last question of the filer with no business (walk `01`, question 86) and comes directly
  after the equipment list for a business owner. It has its own order number (258) so that it stays out of the
  per-item questions.

`asset.not179` is asked of every 2025 item used more than half for the business even with no section 179 amount
(`asset.is_section179` reads it for the cost counted on Form 4562 line 2), so the A1 rewrite does not remove it from
the common path. It was 149 words; its bank prompt is now 41 as shown, with the lease and exempt-use exceptions in the help.
Those exceptions are the precision a child should carry (not done).

## Model changes, all of them

| Form | Added inputs | Added gate and helper lines | Changed | Removed inputs |
|---|---|---|---|---|
| `s179` | `prior_form`, `carryover` | `carryover_if_prior_form` | `line10` is a copy of the gate line | `line10` as an input |
| `scveh` | `smr_always`, `smr_first`, `fleet`; the 19 children of the screen | `smr_first_if_not_always`; `claims_bonus_2025`; one `_if_` gate line for each of the 10 gated children; `no`, `is_actual_owned_test1`, `is_actual_leased_test1`, `is_actual_leased_test2` (the V1 patch) | `smr_ok` and `screen` are derived tests | `smr_ok`, `screen` as inputs |
| `asset` | the 17 children of the screen | `bonus_claimed`, `claims_bonus`; one `_if_` gate line for each of the 5 gated children; `no` and five `s179_bad_*` lines (the A1 patch) | `screen` is a derived test | `screen` as an input |

No refusal entry was added, removed or reworded. No arithmetic line was touched. `f4562.yaml` and `mq.yaml` are
unchanged.

Fixtures (inputs only; no expected value or refusal edited):

- `s179.line10: v` became `s179.prior_form` (true when v is above zero, false at zero, withheld when withheld) and
  `s179.carryover: v`.
- `scveh.smr_ok: true` became `smr_always: true, smr_first: false, fleet: false`.
- `<entry>.screen: false` became every child stated false (`scveh.records: true`). The model-family files
  (`classm.deepseek.json`, `classm.gpt.json`) take no defaults, so each child has to be stated there.
- The three cases that answered a screen Yes: `stage14.asset.refuse_ads_past_gds` now says `asset.method_other: true`
  (its note: property "under ADS"); `stage14.veh.refuse_pre_2017` says `scveh.before_2017: true`;
  `stage14.veh.refuse_screen` says `scveh.disposed: true`. That case's note gives "for example a special allowance
  claimed in an earlier year", but its vehicle is placed in service in 2025, for which that question is no longer
  asked, so I chose an item any vehicle can have. Its expected refusal is unchanged.
- Defaults: every new yes/no false, `scveh.records` true, `s179.carryover` 0.
- The older profiles `stage4.yaml` and `sales.yaml` list the new inputs in place of the three old ones.

## Words (bank)

Every question of the lane has order 255, 257 or 258 and a `seq`; the list is at the foot of this file. Bank prompts
were written for the common questions (the lists, the method, miles, parking, running costs, the year, the cost, the
section 179 amount, the special allowance choice, the quarter); every choice has plain labels (`scveh.method`,
`placed`, `quarter`, `bonus_choice`, `prior_conv`, and the 141 classes of `asset.class`, with a computer, office
furniture and office machines first and the rest by their titles in Pub. 946 Appendix B). The help lines "One of the
values of ..." are gone.

`asset.s179` went from 271 words to 31: the list of what does not qualify is asked by `asset.not179` (N8). The positive tests it also carried (bought, for use in the active conduct of the business; tangible
personal property or off-the-shelf software) are now only in its help in short; a building, a gift and a related
seller are refused by the screen questions before it.

`asset.class` went from 198 words to 22 in the prompt; its instructions on Table B-2 and on additions are the help.

## Cost and share table (NORMS section 3; my estimates unless marked *gf*)

Costs on the owner's scale. "Share yes" is of those asked.

| Question | Asked of | Share yes | Cost yes | Cost no | Before |
|---|---|---|---|---|---|
| `s179.prior_form` | everyone | 1.2% (*gf* `carryforwards`, shared with two other carryovers; likely lower) | 5 (find the paper) | 1 to 2 | `s179.line10`: 10 either way |
| `scveh.smr_always` | vehicles by the mile (about 80% of vehicles) | 95% | 1 | 2 | `scveh.smr_ok`: 5 either way |
| `scveh.fleet` | the same | under 1% | 1 | 1 | part of `smr_ok` |
| `scveh.smr_first` | a No to `smr_always` | 50% | 3 | 3 | part of `smr_ok` |
| the 13 children a 2025 owned vehicle meets | owned vehicles on actual expenses (about 15% of vehicles) | each under 5%, but `got_other` (a trade-in) perhaps 30%, `used_before` perhaps 40%, `for_hire` perhaps 15% | 1 to 2 each | 1 each, 13 to 16 in all | `scveh.screen`: 20 either way (732 words) |
| `scveh.others_use` (parent) | the same | 5% | 2, then 3 children at 5 each | 1 | in the screen |
| the 13 children a 2025 item meets | every item of equipment | each under 3%, but `used_before` perhaps 20%, `got_other` perhaps 5% | 1 to 2 each | 1 each, 13 to 15 in all | `asset.screen`: 20 either way (843 words) |
| `asset.industry` (parent) | every item | under 1% | 2, then a list at 10 | 2 | in the screen |
| `asset.software` (parent) | every item | 5% | 1, then 3 | 1 | in the screen |

N3 for the three parents: `asset.industry` g = 2, q = 0.99, C = 10 (a 250-word list): pays. `asset.software` g = 1,
q = 0.95, C = 3: pays. `scveh.others_use` g = 2 (33 words), q = 0.95, C = 15: pays.

The flat questions do not have a parent because no plain parent can be answered No rightly without reading them
(N2). Thirteen yes/no questions in a row is what the owner rejected for everyone; here they are asked per item of
equipment and per owned vehicle on actual expenses, and are the candidates for tick-lists below. Without the
tick-list page the gain over the old screens is in reading (300 words against 800) and in each answer being about one
thing, not in the number of answers.

## Candidates for one tick-list

Each group is short yes/no facts of one theme with adjacent `seq`, each its own input. A No to every one is the
typical answer.

Equipment (order 257):

1. "What this item is" (seq 4, 5, 7, 9): `asset.kind_excluded`, `asset.software`, `asset.industry`,
   `asset.long_production`. (`software` and `industry` open a child.)
2. "How you got it" (seq 14, 15): `asset.got_other`, `asset.before_2017`; `asset.used_before` (seq 28) belongs here
   by theme but is known to be needed only after the special allowance choice.
3. "What has happened to it" (seq 16 to 19): `asset.ended_2025`, `asset.basis_changed`, `asset.use_changed`,
   `asset.short_year`.
4. "How it is depreciated and where it is used" (seq 20 to 22): `asset.method_other`, `asset.ads_required`,
   `asset.outside_use`.

Vehicles on actual expenses that are owned (order 255):

5. "How you got this vehicle and what has happened to it" (seq 17 to 22): `scveh.got_other`, `scveh.before_2017`,
   `scveh.converted`, `scveh.disposed`, `scveh.basis_changed`, `scveh.short_year`.
6. "How this vehicle is used" (seq 23 to 25, 29): `scveh.for_hire`, `scveh.investment`, `scveh.others_use` (opens
   three children), `scveh.method_other`.
7. "In earlier years" (seq 30 to 32): `scveh.prior_bonus`, `scveh.prior_smr`, `scveh.prior_low_use`.

Not for a tick-list: `scveh.records` (its typical answer is Yes).

## Review debt

- `s179`, `scveh`, `asset`: transcription, render and class M reviews are stale (new and changed lines); the gate
  reviews (`screen_review`, `false_no_review`) have 16 new gate lines and 3 new parents to read.
- Every new input cites its old screen's citation whole (the passages for all the screen's items), not the passage
  for its own item. A citation per child is review work not done.
- The question review of the lane's bank entries is stale throughout.
- `rendered/2025/` was regenerated by `npm run render` for `render --check`.

## Engine change

`engine/src/generate.ts` (the generated returns of `properties`, `compare` and class M seeds) named `scveh.smr_ok`,
`scveh.screen` and `asset.screen` as inputs. It now gives each generated vehicle and item the new inputs, answered so
that nothing refuses (as `smr_ok: true` and `screen: false` did). No other engine file is changed.

## Found and not fixed

- `engine/src/umbrella-what-if.ts` (line 43) and `tools/engines/generate_cases.py` (line 699) still name
  `s179.line10` as an input. Neither is in `tools/draft_check.sh`. `tools/human_review/reading_list.json` names it as
  a line, which it still is.
- The refusal shown for any screen child is the screen's one sentence listing everything ("Vehicle depreciation
  outside this tool (placed in service before 2019, an earlier special allowance, ...)"). It does not name what the
  filer said (walk observation 6). A refusal entry per child would fix it and would change refusal wording, which
  this redraft does not do without the coordinator (MAP 4.1.3).
- `scveh.suv` (87 words) is asked of a vehicle that is not a passenger automobile even when no section 179 amount is
  elected, because `scveh.s179_bad` is an `any` over an `all`. Nesting it (as the A1 patch did for `asset.s179_bad`)
  would ask it only with an amount. Not done.
- Within one order number the engine asks by person, then `seq`, then id (`askOrder`), so two vehicles of one
  business are asked question by question (the method of A, the method of B), not vehicle by vehicle. MAP 4.8.1(b).

## Not finished, in rank order

1. `scveh.passenger` (57 words), `scveh.suv` (87), `scveh.lease_smr_before`, `scveh.after_jan19`,
   `scveh.bonus_same`, `asset.bonus_same` and the `prior_*` questions are still in the form's words. `asset.listed`
   and `asset.not179` have shorter bank prompts but are each still two or three facts in one question: `listed`
   should be two questions (recreational equipment; a computer before 2018, asked only of that year), and the lease
   and exempt-use exceptions of `not179` should be children.
2. `asset.industry_item` is still a list (250 words, reached by under 1%), and `asset.qbu_low`, `scveh.qbu_low`,
   `scveh.leasing`, `scveh.exempt_use` keep the instructions' wording with their exceptions.
3. `asset.class`: 141 labels by official title. Plain labels for the common activity classes (a shop, a restaurant, a
   professional practice) need a reader of Table B-2.
4. Coverage rows for a leased vehicle on actual expenses (`scveh.lease`, `scveh.lease_smr_before`), which this lane
   did not change, and a persona with a vehicle or equipment of an earlier year.

## Requests to other lanes

- **Lane 6a** (`sc.yaml`): `scveh.fleet` and the two `short_year` questions are facts about the business or the
  person; if 6a adds a per-business place for such facts, they belong there.
- **Order agent**: one entry's questions before the next entry's within an order number (above). Nothing needed in
  `full.yaml`: `s179.line13` is already a target, and the vehicle and equipment questions are reachable through the
  business.
- **Coordinator, after the merge**: `interview/2025/coverage/vehicles_equipment.yaml` uses one set of answers for a
  business (persona `05`'s). When lane 6a changes the business questions these rows go stale together; rewrite the set
  `business` once (or regenerate with `l6b_work/coverage.py` after updating persona `05`).

## For the owner

1. `asset.before_2017`: should an item acquired before September 28, 2017 be refused whatever year it was first used
   (the old screen's words, kept), or only when first used in 2025 (as for vehicles)? The second would let the
   question be asked of 2025 items only.
2. `scveh.fleet` per vehicle (above).
3. The refusal sentence that does not name what the filer said (above).
4. The wording of "related person" (above).

## Before and after (from the walks; prompt words as shown to a single filer)

| Filer | Before | After |
|---|---|---|
| No business (persona `01`): this lane's topic | 1 question, 77 words (`s179.line10`) | 1 question, 14 words (`s179.prior_form`) |
| The same filer's whole walk | 86 questions, 6,777 words | 86 questions, 6,714 words |
| Self-employed, own car by the mile (persona `05`): the vehicle's questions | 4 questions, 114 words, one of 62 | 5 questions, 111 words, the longest 30 |
| The same filer: the topic with its two lists and the carryover | 7 questions, 285 words | 8 questions, 206 words |
| The same filer's whole walk | 133 questions, 9,905 words | 134 questions, 9,826 words |
| An owned van on actual expenses and a computer, both new in 2025 (persona `13`, new: no baseline walk; its whole walk is 182 questions, 11,075 words) | each entry met its screen: 732 and 843 words, a Yes or No to 30 items at once; `asset.s179` 271 words, `asset.class` 198, `asset.not179` 149 | vehicle 30 questions, the 13 screen questions 343 words; computer 24 questions, the 13 screen questions 334 words; `asset.s179` 31, `asset.class` 28, `asset.not179` 41, `asset.listed` 61 (was 81) |

The topic is asked together in the after walks: persona `05`, questions 125 to 132; persona `13`, 125 to 180. In the
baseline the vehicle's questions (112 to 115) stood inside the business's yes/no screens and the two lists 40
questions earlier (72, 73).

## What is checked

| Commit | Ran and saw |
|---|---|
| `9694f4ab` | build OK; `test-fixtures` 1854/1854. `interview-rules` (0 problems) and `interview-coverage` (0 problems) ran on the carryover change before the two catalog patches were applied and before the zero-carryover fixture fix. |
| `54c16d87` | build OK; `interview-coverage --rows` on the new file, 42 rows, 0 problems; `draft-walk`, 13 personas, 0 problems; `test-fixtures` 1854/1854 on the same forms before a bank-only wording change. |
| third | the full `tools/draft_check.sh`, first run: every step ok except `properties`, which failed because `engine/src/generate.ts` still named `scveh.smr_ok` and the two screens. After the generator was taught the new inputs: `properties` alone, 9 properties over 400 generated returns, 0 failing; `draft-walk`, 13 personas, 0 problems. |
| `1bf18c34` | the full `tools/draft_check.sh`: green, all 13 steps ok (`draft-check: green (1bf18c34, tree 1645a7f0df9d)`): build; fixtures 1854/1854; interview-rules 0 problems; interview-coverage 0 problems; person wording current; the self-tests; integration 696; properties; serve 338; twins; render check. |
| last | notes only (and any report the check rewrote); nothing the check reads was changed after the green run. |

## Order and seq, as set

| Order | seq | Question |
|---|---|---|
| 255 | 1 | `$scveh` |
| 255 | 2 | `scveh.method` |
| 255 | 3 | `scveh.miles_business` |
| 255 | 4 | `scveh.parking` |
| 255 | 5 | `scveh.smr_always` |
| 255 | 6 | `scveh.smr_first` |
| 255 | 7 | `scveh.fleet` |
| 255 | 8 | `scveh.miles_commuting` |
| 255 | 9 | `scveh.miles_other` |
| 255 | 10 | `scveh.operating` |
| 255 | 11 | `scveh.employee_use` |
| 255 | 12 | `scveh.owned` |
| 255 | 13 | `scveh.lease` |
| 255 | 14 | `scveh.lease_smr_before` |
| 255 | 15 | `scveh.placed` |
| 255 | 16 | `scveh.records` |
| 255 | 17 | `scveh.got_other` |
| 255 | 18 | `scveh.before_2017` |
| 255 | 19 | `scveh.converted` |
| 255 | 20 | `scveh.disposed` |
| 255 | 21 | `scveh.basis_changed` |
| 255 | 22 | `scveh.short_year` |
| 255 | 23 | `scveh.for_hire` |
| 255 | 24 | `scveh.investment` |
| 255 | 25 | `scveh.others_use` |
| 255 | 26 | `scveh.leasing` |
| 255 | 27 | `scveh.exempt_use` |
| 255 | 28 | `scveh.qbu_low` |
| 255 | 29 | `scveh.method_other` |
| 255 | 30 | `scveh.prior_bonus` |
| 255 | 31 | `scveh.prior_smr` |
| 255 | 32 | `scveh.prior_low_use` |
| 255 | 33 | `scveh.cost` |
| 255 | 34 | `scveh.passenger` |
| 255 | 35 | `scveh.suv` |
| 255 | 36 | `scveh.s179_elect` |
| 255 | 37 | `scveh.bonus_choice` |
| 255 | 38 | `scveh.after_jan19` |
| 255 | 39 | `scveh.bonus_same` |
| 255 | 40 | `scveh.used_before` |
| 255 | 41 | `scveh.bonus_excluded` |
| 255 | 42 | `scveh.quarter` |
| 255 | 43 | `scveh.prior_179` |
| 255 | 44 | `scveh.prior_conv` |
| 255 | 45 | `scveh.placed_date` |
| 257 | 1 | `$asset` |
| 257 | 2 | `asset.class` |
| 257 | 3 | `asset.placed` |
| 257 | 4 | `asset.kind_excluded` |
| 257 | 5 | `asset.software` |
| 257 | 6 | `asset.software_spread` |
| 257 | 7 | `asset.industry` |
| 257 | 8 | `asset.industry_item` |
| 257 | 9 | `asset.long_production` |
| 257 | 10 | `asset.cost` |
| 257 | 11 | `asset.pct` |
| 257 | 12 | `asset.listed` |
| 257 | 13 | `asset.qbu_low` |
| 257 | 14 | `asset.got_other` |
| 257 | 15 | `asset.before_2017` |
| 257 | 16 | `asset.ended_2025` |
| 257 | 17 | `asset.basis_changed` |
| 257 | 18 | `asset.use_changed` |
| 257 | 19 | `asset.short_year` |
| 257 | 20 | `asset.method_other` |
| 257 | 21 | `asset.ads_required` |
| 257 | 22 | `asset.outside_use` |
| 257 | 23 | `asset.s179` |
| 257 | 24 | `asset.not179` |
| 257 | 25 | `asset.bonus_choice` |
| 257 | 26 | `asset.after_jan19` |
| 257 | 27 | `asset.bonus_same` |
| 257 | 28 | `asset.used_before` |
| 257 | 29 | `asset.quarter` |
| 257 | 30 | `asset.prior_conv` |
| 257 | 31 | `asset.prior_179` |
| 257 | 32 | `asset.prior_bonus` |
| 258 | 1 | `s179.prior_form` |
| 258 | 2 | `s179.carryover` |
| 258 | 3 | `s179.wc_interest` |
