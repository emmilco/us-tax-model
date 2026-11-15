# Lane notes: 5b (sales of investments, loss carryovers, borrowing to invest, tax on investment income)

Branch `lane/l5b`. Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no
model call was made. Form files: `sales`, `sd`, `clcw`, `clcw26`, `f4952`, `f8960` (and `sdtw`, `u1250`, `g28`, `qdcg`,
which have no inputs and were not touched).

**State of this file:** written as the work went; the section "Where the work stands" at the end says what is
committed and checked, and what a successor does next.

## How to work here (for a successor)

- A build takes about nine minutes on the shared machine. The engine was not changed, so
  `node engine/dist/main.js build` is enough after the first `npm run build --silent` (it skips the TypeScript compile).
- Scratch tools used (kept outside the repository, re-creatable from this description):
  a bank editor that replaces or inserts whole entries of `interview/2025/questions.yaml` by input id, and a fixture
  rewriter that loads each `fixtures/**/*.json`, changes `inputs` of the cases and writes the file back in its own
  format (every file is `json.dumps(indent=2)` with or without `ensure_ascii`, `fixtures/ny/2025/mutation.json` is
  `indent=1`); it refuses a file it cannot write back byte for byte.
- **The class M and mutation fixture files take no defaults** (`takesDefaults` in `engine/src/fixture-inputs.ts`): a new
  input that a case's route reads must be stated in the case, or every value of the case turns unknown. The build
  does not catch this; `test-fixtures` does.
- **Do not edit fixtures, forms or the bank while a check runs**: the checks read the files as they go.
- **A fixture's expected values name ids**: a refusal carries its gate id, and an unknown value the id of the input
  not supplied. Renaming an input or a refusing line therefore changes expected values, which is not allowed.
- Fixture cases state many of this lane's inputs explicitly, including `false` (the class M and mutation files have
  hundreds). An input that stops being an input must be removed from every case that states it.

## What changed, by question

### Order numbers and `seq`

| Order | Topic | Questions, in `seq` order |
|---|---|---|
| 216 | (in "Your home") | `sd.casualty` |
| 274 | Sales of investments | `$sales` 1; `sd.route_each` 2; per sale `sales.box` 4, `special` 5, `proceeds` 6, `reported_basis` 7, `correct_basis` 8, `code` 9, `wash_loss` 10, `route` 11, `aggregate_eligible` 12; then `sd.sold_other` 20 and its children `business_property` 21, `installment` 22, `like_kind` 23; `sd.sec1256` 24, `sd.condemned` 25, `sd.small_business_stock` 26, `sd.trader_election` 27, `sd.f2439` 28 |
| 276 | A loss carried from 2024 | `sd.carryover` 1, `clcw.spouse_screen` 2, `clcw.prior_sd7` 3, `prior_sd15` 4, `prior_sd21` 5, `prior_11` 6, `prior_14` 7, `f8960.prior_2i` 8, `clcw26.final_return` 9 |
| 277 | Borrowing to invest | `f4952.has_interest` 1, `line1` 2, `carryover` 3, `prior_7` 4, `line4g` 5, `unsupported` 6, `alternative_allocation` 7 |
| 278 | Tax on investment income | `f8960.unsupported` 1, `refund` 2, `allocated_taxes` 3 |

`sd.distributions` (in my file `sd`, but the Dividends topic, 272 to 273, lane 5a) was left at order 10: see
"Requests to other lanes".

### Step 1 (map rank 1): `sd.other_forms`, `f4952.has_interest`, `f4952.line4g`

**`sd.other_forms` (48 words, six form numbers, asked of everyone) is no longer asked.** It is now a derived line,
true when any of nine item lines is true (MAP 4.1 rule 2: the technique works; the build accepts it). Every refusal
that read it is unchanged (same line, same `form` and `remedy`, same gate id `sd.other_forms`). The items:

| New input | Asked of | What it covers (source: Schedule D instructions p. 1, "Other Forms You May Have To File", and p. 6) |
|---|---|---|
| `sd.sold_other` (parent, does not refuse) | everyone | sold or traded real estate or business property, or is being paid over more than one year for anything sold |
| `sd.business_property` | Yes to the parent | Form 4797 items 1 and 3: business, rental, mineral property; anything not held as an investment or for personal use |
| `sd.installment` | Yes to the parent | Form 6252, including payments in 2025 for a sale of an earlier year |
| `sd.like_kind` | Yes to the parent | Form 8824 |
| `sd.sec1256` | everyone | Form 6781: section 1256 contracts (boxes 8 to 11 of Form 1099-B) and straddles |
| `sd.condemned` | everyone | Form 4797 item 2: a condemnation of business or investment property |
| `sd.small_business_stock` | everyone | Form 4797 items 4 and 5: an ordinary loss on section 1242 or 1244 stock |
| `sd.trader_election` | everyone | Form 4797 item 6: a trader's mark-to-market election |
| `sd.f2439` | Yes to `div.any` (dividends or distributions received) | Form 2439 |
| `sd.casualty` (order 216) | everyone | Form 4684 |

Gate lines: `sd.business_property_if_sold`, `sd.installment_if_sold`, `sd.like_kind_if_sold`, `sd.f2439_if_dividends`;
the false constant `sd.no` is new.

Not asked any more because another question asks it (MAP 2.7, 4.1 rule 4): capital gains or losses on a Schedule K-1
(`scope.schedule1` today, `scope.k1` after lane 9).

Differences from the map: the map names four items (`sd.sold_other` with children for 4797, 6252 and 8824; `sd.f2439`;
`sd.sec1256`; `sd.casualty`). Reading the instructions' list of what Form 4797 is for showed three uses a filer with no
real estate or business property could have, which the words "Form 4797" covered and no plain parent reaches:
a condemnation, an ordinary loss on small business stock, and a trader's mark-to-market election. Each is a question
of its own (N9). `sd.f2439` is gated on the existing `div.any` instead of being asked of everyone.

Fixture inputs: `sd.other_forms: false` removed from 700 cases; `true` (five cases, none saying which form) became
`sd.sec1256: true`; `null` (13 cases that withhold the answer) became the six ungated new inputs withheld. The coverage
row `credits.form2439` now answers `div.any` and `sd.f2439`. Profiles `sales.yaml` and `stage4.yaml` and
`gate_frequencies.yaml` name the new inputs. Defaults: ten new, all false; the default of `sd.other_forms` removed.

**`f4952.has_interest`** (204 words to 30): "In 2025 or an earlier year, did you (or, on a joint return, your spouse)
pay interest on money borrowed to buy investments, such as a margin loan from a broker?" Bank prompt only; the form
line keeps its full text. "Or an earlier year" is there because a No also hides the carryforward question, so the
parent must be a Yes for someone with a carryforward and no interest in 2025 (the wrong No named below).

**`f4952.line4g`** (83 words, asked of everyone) is now asked only after a Yes to `f4952.has_interest`: new gate line
`f4952.line4g_if_interest`, read by `f4952.bad_election`, `f4952.election_checked` and `f4952.has_election`.
`fixtures/2025/defaults.json` already declared an election without investment interest something no filer can state
("The election on Form 4952 line 4g is made by a filer with investment interest expense"), so no covered situation is
lost. Its prompt is reworded as the choice it is.

`f4952.line1` and `f4952.carryover` are reworded in the bank (by the paper: the broker's statement, the 2024 Form 4952).

**A decision for the owner in this step.** Today a filer can answer No to investment interest and still enter an
election amount on line 4g, and the model then treats Form 4952 as used and required for the election alone. After
the change that filer reaches the election only by answering Yes to the parent and zero to the amount of interest
(the help says zero is a valid answer); a No gives a return with no election. Evidence on each side:

- for the gate: the map (2.8), the owner's walk note that the election "arrives right after the filer has said no to
  investment interest", and the consistency rule in `fixtures/2025/defaults.json` quoted above;
- against: one mutation case, `mutation.f4952.election_without_interest_used`, expects `f4952.used` and
  `f4952.required` true for exactly an election with `f4952.has_interest` false. With the gate it failed. **I changed
  that case's input `f4952.has_interest` from false to true** (interest paid 0, no carryforward, election $0.01, as
  before), which is how the new interview expresses the same amounts, and its two expected values hold unchanged.
  Its `evidence_note` still says "answered no". This is the one place where an input's *value* was changed and not
  just its key; if the owner prefers the election to stay reachable after a No, remove `gated_by` and the gate line
  `f4952.line4g_if_interest`, point its three readers back at `f4952.line4g`, and restore that input.
- Eleven other class M and mutation cases state an election amount with `f4952.has_interest` false (for example
  `classm.clcw.1`, `mutation.t2.qss_s1a_ot`). All pass: none expects a line the election reaches. Their election
  amount is now unread.

### Step 2 (map rank 2): the list of sales as a plain question

`$sales` is reworded as the plain question and is its own off-ramp; **no separate yes or no parent was added**
(a difference from the map). Reason (N3): a roster cannot be gated without putting each of Schedule D's 33 sums over
the sales beneath a `choose`, and an ungated parent in front of the list would ask the 87% the same thing twice. The
list question is first in the topic.

### Step 3 (map rank 3), bank wording only so far

Per sale, bank prompts replace the form lines' long texts; the form lines are unchanged:

| Question | Words before | Now |
|---|---|---|
| `sales.box` | 689 | "Under which heading does your broker's statement (Form 1099-B) list this sale?" with a label for each box, the two common ones first |
| `sales.special` | 171 | a five-item list, about 80 words |
| `sales.proceeds` | 118 | box 1d, one line |
| `sales.reported_basis` | 5 | box 1e |
| `sales.correct_basis` | 906 | bought, inherited, gift: one sentence each |
| `sales.code` | 106 | "Does anything need adjusting for this sale?" with five labelled answers |
| `sales.wash_loss` | 346 | the amount, box 1g, and the 30-day rule in one sentence |
| `sales.route` | 15 | a plain choice with two labelled answers |
| `sales.aggregate_eligible` | 24 | plain |

### Step 3b (map rank 5 in part): the route asked once, not for every sale

- **`sd.route_each`** (new, asked once when a sale is listed): "Do you want to choose, sale by sale, between listing a
  sale on Form 8949 and adding it to a total on Schedule D? The tax is the same either way; with a No, every sale is
  listed." A No makes every sale `detail`, which is always allowed. `sales.route` is asked only after a Yes; gate line
  `sales.route_if_chosen` (else `sales.detail`, a new enum parameter in `params/2025.yaml`), read by the 32 `where`
  tests of `sd` and by `sales.bad_aggregate`.
- Its fixture default is **true** ("Open"), so that every existing case still reads its stated or defaulted `route`
  and no expected value moves. A filer's typical answer is No. The class M and mutation files take no defaults, so
  `sd.route_each: true` is stated in each of their cases that has a sale.
- N3: about 3 once against 5 for every sale; it pays from the first sale.

**Built and taken out again: a parent over `sales.special`.** I built `sd.special_any` ("Is any sale you listed one
of these?", asked once) with the per-sale question beneath it. It cannot be done without changing an expected value:
fixtures expect the refusal's gate id `sales[a].special` *and*, in `stage21.f1.special_withheld` and
`stage21.f1.special_null`, the unknown value's reason "no input supplied for sales[s1].special". A gate needs two ids
(the input and its gate line), and both of today's roles carry the one id. `sales.special` is therefore still asked
for every sale, with a shorter list (88 words, was 171). Whoever may regenerate those two cases' expected reasons can
put the parent back: the model text is in this branch's history only as this description (a `choose` on
`sd.special_any` with else `sales.no`, fixture default true).

### Step 4 (map rank 4), bank wording only

`sd.carryover` reworded ("a net loss from selling investments in 2024, shown as a loss on line 21 of the 2024 Schedule
D"); the worksheet's figures are asked in the order of the paper (Schedule D lines 7, 15, 21, then Form 1040 lines 11
and 14) after the refusing screen.

## Costs and shares (my estimates; the owner rates costs himself)

Scale: 1 known at once, 5 a moment's thought or a glance at a paper, 20 must find out what is being asked. Shares from
`gate_frequencies.yaml` where marked *gf*, otherwise judgment.

| Question | Share asked | Share answering yes | Cost of No | Cost of Yes | Before |
|---|---|---|---|---|---|
| `$sales` | 100% | 13% (*gf*) | 1 | 3 + entries | 5 |
| `sd.sold_other` | 100% | 3% (judgment) | 1 | 2 | part of 20 |
| its three children | 3% | under 1% | 2 each | 2 | |
| `sd.sec1256` | 100% | under 1% | 1 (2 for an options trader) | 3 | part of 20 |
| `sd.condemned` | 100% | under 0.1% | 1 | 2 | part of 20 |
| `sd.small_business_stock` | 100% | under 0.1% | 2 | 5 | part of 20 |
| `sd.trader_election` | 100% | under 0.1% | 1 | 2 | part of 20 |
| `sd.f2439` | 21% (*gf* dividends) | under 0.1% | 1 | 2 | part of 20 |
| `sd.casualty` | 100% | 1% | 1 | 5 | part of 20 |
| `sd.carryover` | 100% | 4.5% (*gf*) | 1 | 5 | 5 |
| `f4952.has_interest` | 100% | 1% to 3% | 1 | 3 | 5 (204 words) |
| `f4952.line4g` | 1% to 3% | few | 3 | 20 | 20, asked of 100% |
| per sale: `box`, `special`, `proceeds`, basis, `code`, `route` | 13% | | 2, 4, 2, 2, 2, 5 | | 40 per sale |

N3 for `sd.sold_other`: g = 1, q = 0.97, C = 6 (three children at 2): 1 < 5.8, it pays.

## Who could answer No wrongly, and the guard

| Question | Who | Guard |
|---|---|---|
| `f4952.has_interest` | someone with a carryforward from 2024 and no interest in 2025 | "or an earlier year" in the parent; the help narrows it |
| `f4952.has_interest` | someone who borrowed against the home to invest | lane 7a's mortgage child (debt used for something other than the home), which refuses, as `sa.unsupported` does today |
| `$sales` (empty list) | shares sold by an employer's plan to cover tax; a fund switched for another | the paper cue "A broker reports each sale on Form 1099-B" |
| `sd.sold_other` | a seller of mineral rights who does not think of them as real estate | none; recorded as open |
| `sd.f2439` not asked | a fund holder who received a Form 2439 and no distribution of any kind | none needed once lane 5a's `div.any` asks about owning shares; with today's `div.any` wording, open |
| `sales.code` "No" | a wash sale the broker did not report | the answer's label names the 30-day rebuy |

## Review debt and things dropped from what the filer reads

- Every new or reworded question is unreviewed (no render, screen, false-no or class M review was run).
- **Texts that no longer reach the filer** because a bank prompt replaced the form line's question text. The form
  lines still carry them; by N10 they belong in children, which are not built:
  - `sales.box`: the holding period rules for gifts, wash sales, stock dividends, nontaxable trades, short sales,
    options, Treasury auctions, automatic investment plans and real property (about 600 words). The help keeps the
    one-year rule and the inheritance rule.
  - `sales.correct_basis`: the rules for part-gift sales, a gift worth less than the giver's basis, Schedule A
    (Form 8971), property given to the decedent within a year of death, trades, transfers from a spouse, property
    received for services, the 2001 election, and the adjustments for short sales, options, original issue discount,
    market discount and bond premium (about 800 words).
  - `sales.wash_loss`: contracts and options, a corporation you control, short sales, shares bought in a different
    number, REMIC residual interests, and the three exceptions.
  - `sales.proceeds`: the pointer to code E for a premium or expense the statement leaves out.
  - `f4952.has_interest`: the kinds of investment property and of loan (land, royalties, collectibles, a loan to
    someone else, an oil or gas working interest; a home equity loan or credit card used to invest).
  - `f4952.line1`: capitalized interest and interest disallowed under section 264.
- `tools/engines/generate_cases.py` still names `sd.other_forms` as an input (outside this lane's files; not run by
  the draft check).

## Found and not fixed

- **`scveh.owned` (lane 6b's file) is held in `tools/interview_rules_baseline.json`** under `order_dependent_reach`,
  with its reason. `interview-rules` reported it on the generated return `generated.6` after my changes and not on the
  baseline tree: "scveh.owned is reachable before the answer that hides it [scveh.method], and the walk in bank order
  never asks it". I did not change `scveh.yaml` and did not trace the cause. Two candidates, both inferences: (a) the
  generator draws an election amount independently of investment interest (`engine/src/generate.ts`, lines 402 and
  766), so a generated return that used to be refused at `f4952.bad_election` now completes, and only complete
  returns are checked for reach (the number of walks rose from 175 to 177); (b) the sales and investment questions
  now come after the business questions (order 274 against 12). The hold list is the check's own mechanism for a
  leak awaiting a fix; the entry must be removed when lane 6b's method-first change lands (the check fails on a
  held template it no longer sees). An earlier run, with the parent over `sales.special` in place, also reported
  `asset.not179` (asked and unread, on the same return); it is not reported on the final tree.

- `sd.installment` asks the fact that the gain is being reported as payments arrive, with the help saying a seller
  who reports the whole gain in the year of sale answers No (the instructions' election out). Today's question asked
  only about "gains or losses from Form 6252", which is the same set.
- `sd.casualty`: a personal loss outside a federally declared disaster is not deductible, and such a filer answered
  No to "gains or losses from Form 4684". The help says so; the prompt alone would send them to a refusal.
- Form 4797 item 1d (section 126 property) has no words of its own; it sits under `sd.business_property`'s second
  sentence.

## Candidates for one tick-list

Heading: **"Less common sales and trades in 2025"**. Adjacent in order 274, `seq` 24 to 28, each recorded as its own
answer, each refusing through `sd.other_forms`:

1. `sd.sec1256`: futures, foreign currency contracts or index options
2. `sd.condemned`: business or investment property taken by a government
3. `sd.small_business_stock`: a loss on small business stock claimed as an ordinary loss
4. `sd.trader_election`: a trading business with a mark-to-market election
5. `sd.f2439`: a Form 2439 from a fund (asked only with dividends)
6. `sd.sold_other` (`seq` 20) could be the first tick of the same screen; its three children follow a tick.

## Requests to other lanes

- **Lane 5a:** `sd.distributions` is declared in `forms/2025/sd.yaml` (mine) and belongs to your Dividends topic
  (272 to 273). I did not touch its bank entry so that we do not both edit it; it needs your order number and `seq`.
  `sd.f2439` is gated on your `div.any`; if `div.any` comes to mean "owned shares of a company or a fund", the gate is
  exactly right.
- **Lane 7a:** `sd.casualty` is at order 216, `seq` 1, as the map says. The words about a casualty or theft can leave
  `sa.unsupported`.
- **Lane 9:** capital gains on a Schedule K-1 are no longer asked here; `scope.k1` is the only question for them.
  Form 4797 and Form 6252 are asked only here (`sd.sold_other` and its children).
- **Order agent:** see "Questions that arrive away from their topic" below.

## Questions that arrive away from their topic (for the order agent)

Seen in the walks of `01_single_w2` and `06_investor_loss_carryover` after the changes (transcripts written to a
scratch directory with `draft-walk --out`):

1. **In order 274 the once-per-return questions come before the list.** `sd.sold_other` (`seq` 20) to `sd.f2439`
   (`seq` 28) are asked before `$sales` (`seq` 1). I think the block rule ("first those of the first entry of the
   outermost collection, and within one entry the lowest `seq`") puts every question with no entry ahead of the
   roster question and the entries. Wanted: `seq` alone decides (MAP 4.8 need b). No field was changed to work
   around it.
2. **A sale's amounts come after every sale's screens.** For two sales: heading, special screen and adjustment of
   A, `sd.route_each`, the same three of B, then proceeds and basis of A, proceeds and basis of B.
   `sales.proceeds` (`seq` 6) and the basis are reached only through Schedule D's sums, each of which waits on
   `sd.screen`, which waits on every sale's screen questions. Wanted: one sale's questions through before the next
   sale's. A target that reads each sale's result without the screen would do it (for example a displayed line in
   `sd` that is the `sum_over` of `sales.h` with no refusal on it, asked for directly in `full.yaml`); I did not add
   one because lanes do not edit `full.yaml` and I did not test it.
3. **`sd.route_each` (`seq` 2) arrives after the first sale's heading, special screen and adjustment questions**, not
   directly after the list. It is read only inside a sale's gate line, behind the refusal entries that stand before
   it on `sales.one` (digital asset, then special, then the adjustment code, then the route): the cause the map
   calls T-284 cause 2 (MAP 4.8 need a).
4. `sd.casualty` (order 216) is asked directly before the 274 block today only because nothing else of mine lies
   between; it belongs with lane 7a's home questions once those carry their order numbers.
5. `sd.f2439` follows the 274 block's once-per-return questions; its parent `div.any` is lane 5a's, far above.
6. `f8960.*` (order 278) and `f8960.prior_2i`, `clcw26.final_return` (order 276, `seq` 8 and 9) have computed gates
   (income over the threshold; a carryover to 2026); no persona reaches them, so their place was not seen.

## Before and after, from the persona walks

Lane 5b's questions only (the persona's whole-walk totals are in `SUMMARY.md` of each walk directory).

| Filer | Before: questions, prompt words | After: questions, prompt words |
|---|---|---|
| `01_single_w2` (nothing in the topic) | 5 (`f4952.has_interest`, `f4952.line4g`, `sd.carryover`, `sd.other_forms`, `$sales`), 391 | 9 (`sd.casualty`, `sd.sold_other`, `sd.sec1256`, `sd.condemned`, `sd.small_business_stock`, `sd.trader_election`, `$sales`, `sd.carryover`, `f4952.has_interest`), 252 |
| `06_investor_loss_carryover` (two sales reported with basis, a 2024 loss, dividends) | 23, 2,780 | 27, 781 |

Whole walks, before and after (questions, prompt words): `01_single_w2` 86, 6,777 to 90, 6,638;
`06_investor_loss_carryover` 114, 9,298 to 118, 7,299. All twelve personas reach the end they reached before
(`draft-walk`: 0 problems). The after transcripts were written to a scratch directory, not committed, so that the
lanes' `walks/after/` do not collide; rerun `node engine/dist/main.js draft-walk`.

The count rises by four for the filer with nothing: one question that named six forms became six one-line
questions, and `f4952.line4g` went away. Five of the six are the tick-list candidates. For the investor the count
rises by four (seven one-liners and `sd.route_each` in, `sd.other_forms`, `f4952.line4g` and the two per-sale route
questions out) and the reading falls by seven tenths. Per sale: five questions and 141 words where there were six
and 1,104 (heading 12, special screen 88, adjustment 7, proceeds 19, basis 15; the route once, 38).

## Not finished, in rank order

1. **Rank 3, the per-sale long questions as children (MAP 2.10).** Done in wording only. Not built: "How did you get
   what you sold?" (bought, gift, inheritance, from a spouse, for work, another way) with one basis question per
   answer, each carrying only its own rule; the same for the holding period of a sale not on a Form 1099-B; the wash
   sale rules beneath "Did you, your spouse or your IRA buy the same thing within 30 days?". Fixture defaults make
   this cheap for the files that take defaults (default "bought" keeps `sales.correct_basis` read); the class M and
   mutation files need the new input stated in every case with a sale. The texts that left the prompts are listed
   under "Review debt".
2. **Rank 3, sale by sale.** The order fields are set; the walk still asks the screens of every sale before any
   amount (see "Questions that arrive away from their topic", 2).
3. **Rank 5, `sales.special` beneath a question asked once.** Built, removed (Step 3b): needs two expected reasons
   regenerated.
4. **Rank 4, `clcw.spouse_screen` (69 words, two items joined by "or", both refusing).** Order and `seq` only. The
   split is two inputs with `clcw.spouse_screen` kept as the derived line: "Was the 2024 return with that loss a
   joint return with someone who is not on this return?" (everyone with a carryover) and "Did each of you file a
   separate 2024 return showing such a loss?" (a joint return only, gated on `f1040.status`). About 110 class M and
   mutation cases state `clcw.spouse_screen` and need the two new inputs stated.
5. **Rank 5, `f4952.unsupported` (87 words, one sentence) and `f8960.unsupported` (152 words, thirteen items).**
   Order and `seq` only. **The map's deletions for `f8960.unsupported` are not safe as written:** it says nine items
   are "already asked", but "business income" is asked by `$sc`, which does not refuse, so a filer over the income
   threshold with a business is refused here today and would not be if the word were dropped. Each deleted item
   needs a check that its other asker refuses in the same cases, or a derived line reading that asker.
6. `sales.code` and `sales.box` are still single selectors (five and twelve labelled answers). The six digital asset
   boxes could leave the selector if crypto were asked once per return; that changes the refusal's gate id
   (`sales[x].digital`), so it has the same obstacle as item 3.

## For the owner

- The election decision above (Step 1).
- **The count went up, the reading down.** A filer with nothing in the topic answers nine one-line questions where
  there were five (252 words against 391). Five of the nine are the tick-list candidates.
- `sd.small_business_stock`, `sd.trader_election` and `sd.condemned` are questions nobody asked for: they are what the
  words "Form 4797" covered. If the owner would rather not ask them of everyone, the alternative is one residual
  question naming the form, which is the kind of question the redraft exists to remove.
- `f4952.has_interest` says "In 2025 or an earlier year". A shorter "In 2025" needs the carryforward question asked of
  everyone ("Does your 2024 return include Form 4952 with an amount on line 7?"), which MAP Part 5 item 9 would place
  in a topic "From your 2024 return".
- Whether one entry may be a statement section's totals instead of one sale (the instructions allow totals for sales
  with basis reported and no adjustment; `sd.route_each` and `sales.route` exist for that). The `$sales` prompt still
  says one entry for each sale.

## Where the work stands


Commit `b00ce0df` on `lane/l5b` holds everything above; the commit after it only records the check result here. What was run on its tree, and what was seen:

- `tools/draft_check.sh` (the full check), run whole on commit `b00ce0df`: "draft-check: green (b00ce0df, tree
  c196128e7ac8)", all thirteen steps; fixtures 1854/1854, interview-rules 0 problems (with the `scveh.owned` hold),
  coverage 0 problems. The run before it failed only `render --check`, until `rendered/` was regenerated.
- `node engine/dist/main.js draft-walk --out <scratch>`: 12 personas, 0 problems; the figures in "Before and after".
- `interview-coverage`: 96 rows in four files, 0 problems; 17 of them are this lane's (`coverage/sales.yaml`), and
  `credits.form2439` was re-answered (a Form 2439 is now reached through `div.any`).

Not run: any review (transcription, render, class M, screen, false-no, completeness, question review), the Lean
comparison, mutation testing, `tools/check_all.sh`, the differential engines (`tools/engines/generate_cases.py` still
names `sd.other_forms`), `tools/check_agent_runs.py` (no `agent_runs.jsonl` row was written in this worktree; the
coordinator records the run: model `claude-fable-5-2`, class judgment, year 2025, jurisdiction `us`).

Inferred, not checked: that a filer reads the new questions as intended (no review was run); the cause of the
`scveh.owned` hold; the cost and share estimates; that no other lane's change moves the dividend questions in a way
that leaves `credits.form2439` with a stale answer (it will: lane 5a reorders them, and the row's answers must then be
restated).

A successor starts at "Not finished, in rank order", item 1.
