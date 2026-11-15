# Lane notes: rc (second round, order numbers 250 to 319)

Branch `lane/rc`, worktree `.claude/worktrees/provisional-rc`, cut from `provisional/interview-graph` at `926fb406`.
Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call was made and no model was
called from code.

The range: a person's own business with its vehicles and equipment, interest, dividends, sales of investments and
loss carryovers, borrowing to invest, tax paid abroad, accounts and assets outside the United States, the rare
situations, tax already paid, and the last checks for credits. Two other agents have 100 to 169 (`lane/ra`) and 170
to 249 (`lane/rb`); a fourth (`lane/tickrule`) relaxes the group rules and declares `rare_credits`.

WORKING STATE (kept current; a successor continues from here): see "Status" at the foot.

## How to work here

A build takes 5 to 11 minutes on the shared machine and the coverage rows much longer, so bank changes were tried
first without the build:

```
node docs/provisional/lanes/rc_trial/trial.mjs "$PWD" --personas 01_single_w2,13_self_employed_actual_vehicle_computer --list
node docs/provisional/lanes/rc_trial/trial.mjs "$PWD" --all --rows credits.yaml,business.yaml [--lists lists.json]
```

`trial.mjs` reads the working copy of `interview/2025/questions.yaml`, gives the built `full` interview its `order`,
`seq`, `group` and `tick` in memory (and the groups' headings), runs the build's group rules, `tick-groups`' walk on the
background return, the personas (`draft-walk`'s own functions, with the figures of the questions of 250 to 319 apart)
and the rows of the coverage files named. `--lists` reorders the refusal entries of the lines named in a JSON file, in
memory. It needs a build of the forms as they stand; a change to a form, a prompt or a help text needs the build.

## 1. The tick-box groups

Thirteen groups are declared by this lane in `interview/2025/questions.yaml`; a fourteenth, `rare_credits` (three
Schedule 3 questions at 290), came with the merge of `lane/tickrule` (`f009095a`) and is not in this list. Each member keeps its own prompt, help and input; the heading
and labels are new wording no review has read.

Asked of every filer:

| Group (order) | Heading | Boxes (member: label) |
|---|---|---|
| `sales_rare` (274/20 to 24) | In 2025, did you (or, on a joint return, your spouse) have any of these less common sales or trades? | `sd.sold_other`: Sold real estate or business property, or got installments from any sale. `sd.sec1256`: Traded futures, foreign currency contracts or index options, or held a straddle. `sd.condemned`: Had business or investment property taken by a government. `sd.small_business_stock`: Lost money on small-company stock and claim it as an ordinary loss. `sd.trader_election`: Trade securities as a business under a mark-to-market election |
| `invest_other` (276/1, 2) | Is either of these true of your (or, on a joint return, your spouse's) investments? | `sd.carryover`: A loss from selling investments in 2024, or one carried into 2024. `f4952.has_interest`: Interest paid on money borrowed to buy investments, in 2025 or before |
| `outside_us` (285/1 to 6) | At any time in 2025, did you (or, on a joint return, your spouse) have any of these outside the United States? | `sb.account_any`: An account in another country, or the power to sign for one. `sb.asset_any`: Other property abroad, or money owed to you by someone abroad. `sb.trust_any`: A tie to a trust or family foundation abroad. `sb.company_any`: A foreign company you help run, or own 10% or more of. `sb.territory_any`: An account, investment, company or trust in a U.S. territory. `scope.foreign_shares`: Shares of a foreign company or fund, held outside a U.S. fund |
| `other_taxes` (291/1 to 3) | Do you (or, on a joint return, your spouse) owe any of these for 2025? | `s2.credit_recapture`: A tax credit from an earlier year that must be paid back. `s2.amt_owed`: Alternative minimum tax. `s2.other_tax`: Another federal tax you have not been asked about |
| `paid_already` (300/1, 2) | Besides tax taken out of wages, did you (or, on a joint return, your spouse) pay federal tax for 2025 in either of these ways? | `f1040.withheld_other_any`: Tax taken out of a pension, social security or other money. `f1040.estimated_any`: Estimated tax payments, or a 2024 refund applied to 2025 |

Asked of each business (the build puts "For this business — " before the heading; likewise "For this vehicle — " and
"For this property — "):

| Group (order) | Heading | Boxes |
|---|---|---|
| `biz_refused` (251/1 to 4) | Is any of these true of it? | `sc.spouse_owned`: Owned jointly by a husband and wife. `sc.statutory`: Its income is from a “statutory employee” W-2 job, or notary fees. `sc.business_credit`: It claims a business tax credit, such as for research. `sc.fuel_credit`: It wants federal fuel tax back for fuel used off the road |
| `biz_had` (252/16 to 20) | Which of these did it have in 2025? | `sc.travel_meals`: Overnight travel, or meals, food or drink it paid for. `sc.employees`: Employees paid wages (not freelancers or contractors). `sc.goods`: Goods it bought or made to sell, or held for sale. `sc.ho_uses`: Part of your home used only for it or storing its stock. `sc.hi_uses`: Health insurance for its owner or the owner's family |
| `veh_history` (255/18 to 22) | Is any of these true of its history? | `scveh.before_2017`: Got before September 28, 2017. `scveh.converted`: Changed between personal and business use during 2025. `scveh.disposed`: Sold, traded in, given away or scrapped in 2025. `scveh.basis_changed`: A major improvement, tax credit, deduction or casualty loss changed its cost. `scveh.short_year`: A tax year of under 12 months since its business use began |
| `veh_use` (255/23 to 26) | Is any of these true of how it is used or depreciated? | `scveh.for_hire`: Carries people or goods for pay, or is an ambulance or hearse. `scveh.investment`: Also used in 2025 to earn income outside the business. `scveh.others_use`: Used by someone else, or for entertainment. `scveh.method_other`: Depreciated by straight line, 150% declining balance or the alternative system (ADS) |
| `veh_prior` (255/30 to 32) | In an earlier year, was any of these true of it? | `scveh.prior_bonus`: A special (“bonus”) depreciation allowance was claimed for it. `scveh.prior_smr`: The standard mileage rate was used for it. `scveh.prior_low_use`: Half or less of its use was for business |
| `asset_kind` (257/4 to 7) | Is it any of these? | `asset.kind_excluded`: A building, land, a vehicle, an aircraft, a film or a recording. `asset.software`: Computer software. `asset.industry`: Used in a utility, energy, recycling, rent-to-own, racetrack or loan-financed dealer business. `asset.long_production`: Built to order over a long period, or “qualified production property” |
| `asset_history` (257/16 to 20) | Is any of these true of its history? | `asset.before_2017`: Got before September 28, 2017. `asset.ended_2025`: Sold, given away, scrapped or taken for personal use in 2025. `asset.basis_changed`: A casualty loss, tax credit or special deduction changed its cost. `asset.use_changed`: The business share of its use has changed. `asset.short_year`: A tax year of under 12 months since its business use began |
| `asset_method` (257/21 to 23) | Is any of these true of how it is depreciated or used? | `asset.method_other`: A special depreciation method was chosen instead of the IRS tables. `asset.ads_required`: The alternative depreciation system (ADS) is required for it. `asset.outside_use`: Used mostly abroad; leased to a charity, government or foreigner; or bond-financed |

Why each is as it is, and what was decided against:

- **`sales_rare`.** Lane 5b's proposal less `sd.f2439`. That question is asked only of a filer with dividends
  (`sd.f2439_if_dividends` reads `div.any`), and `tick-groups` fails a group one of whose members the background
  return is never asked with the others. It is about a paper a fund sends, so it now sits at the end of the
  dividend questions (272/18). `sd.sold_other`'s three children follow the screen (274/26 to 28).
- **`invest_other`.** Two boxes. `f4952.*` moved from 277 to 276 (the group needs one order number, and what a
  member opens must follow the group): the borrowing questions are 276/3 to 8 and the loss carryover figures
  (`clcw.*`, `f8960.prior_2i`, `clcw26.final_return`) 276/10 to 17. A filer with both is asked the borrowing amounts
  before the carryover figures; the build's rule gives no other order (the `clcw` questions are not gated children).
  The label for `sd.carryover` says "or one carried into 2024" because the prompt's help does: a person who sold
  nothing in 2024 can still carry a loss.
- **`outside_us`.** The five parents lane 5a made of `sb.foreign_any`, and `scope.foreign_shares` (was 287/1) as
  the sixth, added after the merge of `lane/tickrule` (below). `s3.foreign_any` cannot be a seventh (six is the
  limit) and stays a question of its own before the screen. `scope.pfic` and `scope.cfc` are 285/12 and 13.
- **`other_taxes`.** The three Schedule 2 questions of 291 to 293, now 291/1 to 3. "Alternative minimum tax" is a
  term, not a plain fact: a filer who does not know it cannot tick it, and the typical filer does not owe it. The
  question itself is lane 7b's and has the same weakness asked alone.
- **`paid_already`.** The children (`f1040.line25b`, `line25c_other`, `line26`) follow at 300/3 to 5.
- **`biz_refused`.** Lane 6a's second list. The label for `sc.spouse_owned` has no "you": the group is asked for
  each person's business, and "your husband or wife" would be reworded for the spouse.
- **`biz_had`.** Lane 6a's first list. The five parents were in four order numbers with their children between; they
  are now 252/16 to 20, with what each opens after the screen in the same order as before (travel and meals, wages,
  goods, the home, the owner's insurance), `sc.line48` (other expenses) before the screen with the other amounts.
  Two of the five are commonly ticked (travel or meals, a home office); it is a "which of these" list, not an
  off-ramp, and is still one step in place of five.
- **The vehicle.** `scveh.got_other` stays a question of its own: its fact needs more than a dozen words (a
  trade-in, an exchange, a replacement, a relative, a business you control). The other ten flat questions are two
  screens, and the three about earlier years (asked only of a vehicle first used before 2025) a third.
  `scveh.records` is not in a group (its typical answer is Yes).
- **The item of equipment.** `asset.got_other` alone for the same reason. `asset.s179` (the amount chosen) moved
  from 257/23 to 257/14: the history questions are not open until it is answered, so it was already asked before
  them, and a group must come after what its members wait on. `asset.industry` is in `asset_kind` because the form
  reads it between `asset.software` and `asset.long_production`; its label is the weakest of the thirteen groups
  ("loan-financed dealer" for "a dealer that finances its stock with a loan secured by it").

### The scope questions and the group rule (half solved by `lane/tickrule`; one request left)

At `926fb406` the build refused any group with a `scope.*` member: it read `household.credit_disallowed` (310/1) as
opened by 53 different answers (every scope question and the `eic.*` questions; the next most was 6), because that
question's gate reads the earned income credit's eligibility lines, which read every scope screen. `lane/tickrule`
removed that rule (`f009095a`), and `scope.foreign_shares` joined `outside_us` after the merge.

What is left: **the last scope question in the order of asking cannot be in a group.** When it is answered No, the
questions that waited on the scope screens open (`person.eic_ssn` at 311, the `qbi` questions), and `tick-groups`
reports them as opened by the screen with no box ticked. Tried after the merge, built: `scope.reforestation` and
`scope.attorney_fees` (295/1, 2) as a pair; `tick-groups` failed with "group rare_events: none ticked: the answer
opens person[taxpayer].eic_ssn (order 311), asked only after s3.line10 (order 305), which was already waiting". The
pair was taken out again; the two are single questions.

**Request (to the owner of `engine/src/tick-groups-check.ts`):** do not report what a screen's answers open when no
box is ticked. Nothing ticked is no parent, and what then opens belongs to its own topic. With that, the pair can
be declared (bank fields only; heading "Did you (or, on a joint return, your spouse) do either of these?", labels
"Paid to plant trees on timber land you own, since 2018" and "Paid a lawyer in 2025 to win a discrimination or
whistleblower claim"): one step fewer for every filer. They cannot join `rare_credits` instead: a group with the
last scope question and a member whose Yes does not refuse fails the same check with that member ticked.

## 2. The order of asking

- `ftc.carryover`: 279/5, after `s3.foreign_any` and its three children. Its gate asks it when `s3.foreign_any` is
  Yes, and otherwise when `s3.prior_other_forms` (290/5) is Yes; in the second case it is asked directly after that
  answer (the lowest open number goes first), before `s3.prior_amt`.
- `sd.f2439`: 274/28 to 272/18 (the end of the dividend questions; it is asked only with dividends).
- `f4952.*`: 277 to 276 (see `invest_other`).
- The business: `sc.line48` joins the plain amounts (252/15); the five parents and what they open are 252/16 to 40
  (they were spread over 252, 253, 254 and 259); `sc.business_credit` and `sc.fuel_credit` come before
  `sc.passive`, `sc.method_other` and `sc.special` (251). Gross receipts (`sc.line1`) are asked first after the
  list of businesses in every walk made here (the merged order mechanism already did this; lane 6a's report was of
  its own branch).
- The item of equipment: `asset.s179` before the history questions (above).
- `scope.business_before` and its three children: 295/3 to 6 moved to 258/1 to 4, directly before
  `s179.prior_form` (now 258/5), because of the model change of section 4. For a filer with no business it follows
  the (empty) list of businesses; for a business owner it follows the equipment.
- `qbi.prior_form` and its children, `qbi.suspended`, `qbi.coop_patron`: 262 to 296. They are read only once taxable
  income is known, so at 262 they were asked after 295 in every walk (an order number re-entered); 296 is where
  they arrive. A filer of 65 or over still gets them after `person.work_ssn` (311), which the senior deduction
  reads first.
- Tried and undone: `s179.prior_form` at 296 with the other "earlier years" questions. The business's profit reads
  the carryover, so everything that reads the profit waited for it: row `business.self_employment_screen` was asked
  `scope.se_plan_other` after its refusing answer. The carryover question belongs with the business.
- Not changed: the last checks for credits (310 to 319). Each opens when the one before it is answered (a chain of
  tests in the forms, not the bank's numbers), so they already arrive after everything else, in the forms' order:
  for the single parent of persona `03`, combat pay, the two social security number questions, the disallowed
  credit, Puerto Rico, the child's half year, the third number question, tax-exempt interest, the relative's home.
  What would shorten the stretch is the open request of the integration notes (one social security card question
  in place of `person.tin`, `person.work_ssn` and `person.eic_ssn`, in `person.yaml`). `f1040.tax_exempt_interest`
  (271/1), which this stretch asks of a filer with no interest, now has a plain prompt in the bank (it was the
  form's 56-word line label).
- Seen in `interview-order` on the committed build (`/tmp/order_rc.md`; 79 walks) and left: `sc.at_risk` (252/38)
  waited on `scope.business_before` (258/1) in 2 walks, an order number re-entered. Asking the earlier-business
  question directly after the list of businesses (250) would mend it, at the price of one question between the
  list and the business's receipts. The other late questions of this range in that report are the ones described
  here (`person.eic_ssn`, `qbi.prior_form` and `f1040.tax_exempt_interest` behind the last scope question or the
  credit checks; `ftc.carryover` behind `s3.prior_other_forms` in 1 walk) and children that follow a tick-box
  screen and not their own parent, which the group rule intends.
- Not done: one order number for a whole business. The business's questions are in 250, 251, 252, 255, 257, so a
  person with two businesses is asked both businesses' receipts, then both businesses' screens, and so on. Giving
  every question of `sc`, `scveh` and `asset` one order number (and `seq` in the present sequence) would ask each
  business through. No persona has two businesses and the coverage rows would need walking again.

## 3. Refusals told at their question (N11)

Six refusal lists were put in the order of asking (`forms/2025/`; entries moved, none added, removed or changed):

| Line | Order of entries now | What it mends |
|---|---|---|
| `s3.line7` | adoption, adoption (earlier year), mortgage certificate, the three vehicle entries, bond, the two earlier-year entries, elderly | the stitch study's order: a vehicle or mortgage certificate refusal no longer waits for `s3.credit_bond` (290) |
| `s3.line14` | section 965, section 960(c), Virgin Islands, farmland deferral, repaid income | the three foreign children no longer wait for `s3.farmland` |
| `sc.line1` | business credit, fuel credit, the screen | a business credit or fuel credit refusal no longer waits for `sc.special` |
| `scveh.cost` | too old, the screen | a vehicle placed in service before 2019 (`scveh.too_old`) is refused at its year, not after the screen questions |
| `asset.done` | listed property used half or less for business or a share over 100 (`asset.listed_low`), the screen | told when `asset.listed` and the share are answered, not after the screen questions |
| `div.screen` | section 1202, special boxes, AMT, unsupported, components | box order of the form |

Found with a scan (`rc_trial/scan.py`: for each line with more than one refusal entry, the last place of asking of
the questions each entry reads through its own form, in list order) and then checked by the fixtures (1854 of 1854
after the change, so no fixture names another refusal) and the coverage rows (below). Left: `person.ira_line11`
(`person.yaml`, not this lane's), `f4952.election_checked` (its third entry is a computed test; not looked into).

## 4. Never ask twice (N8): one model change

`s179.prior_form` ("Do you have a deduction for business equipment left over from an earlier year?") was asked of
every filer, directly after an empty list of businesses. It is now asked only when `scope.business_before` is Yes
(an earlier business, farm, rental or share of a partnership or S corporation): a deduction can only be left over
from a business of an earlier year. `forms/2025/s179.yaml`: `s179.prior_form` is `gated_by` the new line
`s179.prior_form_if_before`, and `s179.carryover_if_prior_form` reads that line. Fixtures: the 16 cases that state
`s179.prior_form: true` now also state `scope.business_before: true` (in `s179.json`, `sc.json`, `classm.json`,
`classm.deepseek.json`, `mutation.json`; inputs only). One of them is the return with a carryover and no business
in 2025, which is still refused at `s179.line13`. Review debt: one new gate line and a changed gate in `s179`.

Considered and not built: `qbi.prior_form` ("does your 2024 return include Form 8995 or 8995-A?") is settled by a
No to `s3.prior_other_forms` ("does your 2024 return include any separate form?"). The gate is three lines in
`forms/2025/qbi.yaml`, but the `sales` profile asks `qbi.prior_form` and not `s3.prior_other_forms`, so the profile
would have to gain that question and its children. Worth doing at adoption: it removes one question for every
filer whose 2024 return was a plain one.

## 5. Help and prompts

Help cut to about 40 words or less, the refusal sentence kept: `s2.credit_recapture` (56 to 37), `s2.amt_owed` (53
to 38), `s2.other_tax` (58 to 42), `f4952.has_interest` (44 to 36), `sb.asset_any` (49 to 41), `sd.trader_election`
(44 to 39), `f1040.withheld_other_any` (44 to 38), `s179.prior_form` (the sentence the gate now makes true is gone).
`s3.line10` (the amount paid with an extension request, asked of everyone) has a bank prompt of 26 words in place of
the form's 40, and help that no longer restates it. `f1040.tax_exempt_interest` has a bank prompt and help (above).
The other help texts of the typical filer's questions in this range were already at or under 40 words and were
left.

## 6. Coverage rows restated (answers only; no `expect` changed)

Walked per file with `interview-coverage --rows FILE` and changed with `tools/draft/fix_rows.py`, each change read:

- `credits.yaml`, 33 changes in 15 rows. 30 are answers removed because the refusal now comes before the question
  is asked: the business credit and fuel credit rows no longer answer `sc.passive`, `sc.method_other`, `sc.special`
  and `sc.spouse_owned`; the vehicle rows no longer answer `s3.credit_bond`; `credits.mcc` no longer answers
  `s3.prior_other_forms`; the three foreign rows no longer answer `s3.farmland`, `ftc.taxes` and `ftc.carryover`.
  These are the refusals of section 3 arriving on the row's own answer. Three answers added:
  `credits.form1116` answers `ftc.carryover` No (it is now asked directly after the foreign children);
  `credits.gap.foreign_tax_carryover_form` answers `f5695.carry` No; `credits.employment_credit` answers
  `sc.business_credit` No (see "For the owner").
- `home.yaml` (4 rows) and `other.yaml` (11 rows): `scope.attorney_fees: false` added. These are the fifteen rows
  of the integration notes whose refusal waits for the last scope question; that question was
  `scope.business_before` and is now `scope.attorney_fees` (295/2). The late telling itself is unchanged (lane 9's
  finding; not this lane's forms).
- `vehicles_equipment.yaml`: three rows answer `scveh.method_other` No (it now comes before the three questions
  `scveh.others_use` opens); `equipment.screen_qbu_low` loses two answers (refused earlier, at `asset.listed`);
  `equipment.carryover_none` and `equipment.carryover_no_business` were restated by hand for the model change of
  section 4: each now answers `scope.business_before` Yes (and its three children No) before the carryover question.

## 7. From the coordinator, during the run

- The agent of 170 to 249 set two bank entries of this range (order and `seq` only): `f5695.carry` and
  `f5695.line12` at 290/8 and 290/9. This lane did not touch them (on this branch they are still 239/1 and 239/2)
  and leaves 290/8 and 290/9 free. That agent also adds targets `sa.line17` and `s2.other` to
  `interview/2025/full.yaml`, which this lane did not edit.
- `person.sav_claimed` (315/2) and `person.tin` (311/1) stay where they are. As relayed, and not checked here: the
  other agent placed them at 241 so that a student's education questions are asked together, `interview-rules`
  failed on generated return 10 (`person.tin` and `dependent.edu_tin_issued` reachable out of bank order, or
  `person.tin` asked and unread), and it put them back. So a student still meets the education questions at the
  end of the interview: `person.edu` waits on `person.sav_claimed`, the rest of the block on `person.tin`.
  **Not attempted here.** What holds it, as far as this lane read: both questions are read by several forms under
  computed conditions (the saver's credit, the child credits, the earned income credit, education), so at an early
  number they are open for some filers only after a later answer, and for others not read at all; the bank's
  numbers cannot open a question (order contract, 1.6). The remedy is in the forms, not the bank: ask each once,
  of everyone, in "About you" (a filer knows at once whether they have a social security number and whether
  someone claims them), so that no credit's condition decides whether it is asked. `person.yaml` is not this
  lane's file; this is a request to its owner.

## 8. Before and after, in this range

"Baseline" is `docs/provisional/walks/before/`, counting the questions of this range's subjects (the three scope
catch-alls, whose items partly moved here, are not counted, so the baseline is understated). "Round one" is the
merged draft at `926fb406`; "now" is this branch. Round one and now are the questions whose bank order is 250 to
319, counted by `rc_trial/trial.mjs` with `draft-walk`'s own functions; the whole-walk totals it prints equal
`draft-walk`'s. A tick-box screen is one step and is read as its heading and labels. Help words count every
question's help, including that behind a box.

| Persona | | Steps | Questions | Prompt words | Help words |
|---|---|---|---|---|---|
| `01_single_w2` | baseline | 25 | 25 | 2,075 | 701 |
| | round one | 35 | 35 | 833 | 1,105 |
| | now | 19 | 34 | 593 | 994 |
| `06_investor_loss_carryover` | baseline | 53 | 53 | 4,596 | 1,112 |
| | round one | 61 | 61 | 1,537 | 1,799 |
| | now | 45 | 60 | 1,297 | 1,688 |
| `05_self_employed` | baseline | 77 | 77 | 5,259 | 771 |
| | round one | 86 | 86 | 2,446 | 2,137 |
| | now | 63 | 85 | 2,110 | 2,026 |
| `13_self_employed_actual_vehicle_computer` | round one | 134 | 134 | 3,695 | 2,710 |
| | now | 96 | 133 | 3,089 | 2,599 |

The whole walk of `01_single_w2`: 125 questions on 125 steps, 2,567 prompt words and 3,548 help words at round
one; 124 questions on 109 steps, 2,327 and 3,437 now (with `rare_credits` from `lane/tickrule` merged).

The 19 steps of `01_single_w2` in this range: the list of businesses; an earlier business; the list of interest
payers; dividends; the list of sales; the less common sales (one screen); the loss carried and borrowing to invest
(one screen); tax paid abroad; outside the United States (one screen, six boxes); the three rare credits (one
screen, `lane/tickrule`'s); other forms in the 2024 return; other taxes (one screen); the list of other income; timber; legal
fees; the 2024 business-income form; a farm cooperative; tax already paid (one screen); the extension payment.

## 9. Not finished, in rank order

1. **`scope.reforestation` and `scope.attorney_fees` as one screen** (one step for every filer). Blocked by the
   walk check (section 1, the request).
2. **`qbi.prior_form` behind `s3.prior_other_forms`** (section 4): one question for most filers; needs the `sales`
   profile changed.
3. **A yes/no parent over `s3.line10`** (the extension payment), as a third box of `paid_already`. Prepared and not
   applied: `social-security.yaml` and `stage4.yaml` list `s3.line10`, so both profiles would gain the parent, and
   their scripted walks were not looked at. The amount is asked of everyone meanwhile, in 26 words.
4. **`qbi.coop_patron`** is a single question at 296 (it waits for the last scope question and for taxable
   income, so it cannot share a screen with a question asked earlier).
5. **One order number for a business** (section 2).
6. **The last checks for credits** (section 2): unchanged.
7. `f4952.election_checked`'s list; `sc.special` (255 words, lane 6a's first unfinished item), `sc.ho_other`,
   `sc.hi_screen`, `person.se_screen`, `scveh.passenger`, `asset.listed`, `asset.not179` are still long questions on
   a business owner's path; none was reworded here.

## 10. Requests, and what the merger must know

- **Merger.** This branch holds `lane/tickrule` at `f009095a` (merged in `9fb75722`; the one conflict of substance
  was `bank.groups`, where both lists are kept: 14 groups). The two other range branches will conflict in the same
  list; keep every group. `engine/` is not touched by this lane.
- **Merger.** This branch moved bank entries of other agents' forms inside 250 to 319: `scope.business_before`,
  `scope.nol`, `scope.passive`, `scope.f8978` (295/3 to 6, now 258/1 to 4); `scope.foreign_shares`, `scope.pfic`,
  `scope.cfc` (287, now 285/6, 12, 13); `s2.credit_recapture`, `s2.amt_owed`,
  `s2.other_tax` (291/1, 292/1, 293/1, now 291/1 to 3, in `other_taxes`); `f1040.*` of 300 renumbered. It reworded
  the help of the three `s2` entries. It did not touch the four entries of section 7.
- **Merger.** `s179.prior_form` now reads `scope.business_before`. If the agent of 100 to 169 moves or regates that
  question, the carryover question moves with it; it must stay asked before 259 (the business's profit reads it).
- **Merger.** Rows of `home.yaml` and `other.yaml` (other agents' topics) gained `scope.attorney_fees: false`; if
  another branch changes the same rows, keep that answer while `scope.attorney_fees` is the last scope question.
- **Owner of the tick-box check:** the one change of section 1.
- **Owner of `s2.yaml`:** nothing needed for the three questions of `other_taxes` (answered on one screen). With
  `s2.other` a target (section 7) the remaining Schedule 2 items are asked at their own numbers.
- **Owner of `person.yaml`:** one social security card question (integration notes); `person.ira_line11`'s refusal
  entries are not in the order of asking (`rc_trial/scan.py person`).
- **Owner of `scope.yaml`:** `scope.attorney_fees` is now the last scope question in the order of asking, so the
  fifteen late refusals of lane 9's finding are told there (295/2).

## 11. For the owner

- **The boxes' words.** 51 labels and 13 headings are this lane's and new. The weakest: "Alternative minimum tax" (a term);
  "loan-financed dealer" in `asset_kind`; "installments from any sale" in `sales_rare` (for "being paid over more
  than one year for anything you sold"); "A tie to a trust or family foundation abroad".
- **`biz_had` is a list people tick**, not one they pass: a home office and meals are common.
- **An employment credit is a business credit.** `sc.business_credit` ("Does this business claim any business tax
  credit?") is now asked before `sc.special`, whose list holds the employment credits. Row
  `credits.employment_credit` answers the first No and the second Yes, as it did, and ends where it did; a real
  filer with an employment credit would likely tick the business credit box and be refused there instead (another
  refusal, the same outcome: this tool cannot prepare the return). The two questions overlap (N8); `sc.special` is
  lane 6a's unfinished list.
- **`scope.business_before` moved to the business topic** and now gates the carryover question. A person who has
  run the same business for years answers it Yes and is asked its three children; the personas answer it No.
- **Review debt** from this lane: the group wording; the reordered refusal lists of six lines; one new gate line
  and one changed gate in `s179`; reworded help on eight questions and two bank prompts.

## Status

Commits: `e4649ca2` (the groups, the lists, the carryover gate, the rows), `9fb75722` (the merge of `lane/tickrule`
and the scope boxes), then the final tree in two commits (the server assertion on its own).

Run on the final tree and seen:

- `tools/draft_check.sh`, whole, once (build 798 s on the loaded machine): build OK; fixtures 1854 of 1854;
  interview-rules 0 problems (177 walks, 415 random traversals); coverage rows 0 problems; `tick-groups` passed;
  person-wording report current; the spouse-wording and check self-tests; 1026 command-line invocations;
  properties; the `draft-walk`, `interview-order` (692 checks) and `tick-groups` (35 cases) self-tests; twins 0
  problems. **Two stages were red in that run and were mended and rerun alone, not by a second whole run:**
  - `render --check`: seven rendered forms differed (the reordered refusal lists and the new gate line).
    Regenerated with `render`; `render --check` then passed.
  - `test-serve`: one assertion of `engine/src/serve-check.ts` (from `lane/tickrule`) required that the only
    vetting cards with a tick-box label be the three of `rare_credits`. It now requires that the cards of group
    `rare_credits` be those three. `test-serve` then passed (513 checks). This is a check's expectation restated,
    in a commit of its own; the other two range branches will meet the same assertion when they declare groups.
- `draft-walk` over the 14 personas: 0 problems, every end unchanged. `tick-groups`: passed (14 groups; 6 shown
  whole on the background return, 8 lie behind a business and are not checked by that command). The eight business
  groups were seen whole in the walks of personas `05` and `13` (`trial.mjs --list`); `veh_prior` and
  `asset.use_changed` in no walk (no persona has a vehicle or an item of an earlier year).

Inferred, not checked: that the groups read well in the page (no browser was opened; `ui/test_browser.mjs` was not
run); that a second business or a joint return shows the per-business screens correctly (the build's
person-wording rule passed the labels; no persona has two businesses); that the reordered lists tell every refusal
at its question for filers the rows do not cover; that the stages which passed in the whole run would pass again
after the two mends (the mends touch only the rendered files and one test assertion).
