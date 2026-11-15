# Lane notes: 6a (a person's own business; the owner's plan, insurance and deduction)

Branch `lane/l6a`. Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no
model call was made. Form files: `sc`, `ltc`, `qbi` (`se`, `f8995`, `f8995a` hold no question). Bank only:
`person.plan`, `plan_screen`, `se_screen`, `sep_*`, `simple_*`.

A successor continues from "Not finished, in rank order" at the foot. Step 1 is commit `e8a85cf0`; steps 2 and 3
are one commit after it. The full `tools/draft_check.sh` was run on the tree of that second commit less these notes
and was green (all thirteen checks).

## Order numbers and what each block holds

| Order | Block | Questions, in `seq` order |
|---|---|---|
| 250 | What the business took in | `$sc`, `sc.line1`, `line2`, `line6`, `tips_ot` |
| 251 | Facts about the business the tool cannot handle | `sc.spouse_owned`, `statutory`, `passive`, `method_other`, `special`, `business_credit`, `fuel_credit` |
| 252 | Expenses, in the order a person thinks of them | `sc.line8`, `line11`, `line10`, `line18`, `line22`, `line20b`, `rent_equipment`, `line25`, `line15`, `line17`, `line23`, `line21`, `line16a`, `line16b`; `travel_meals`, then `line24a`, `meals_50`, `meals_80`, `meals_100`; `employees`, then `line26`, `line14`, `line19`; `line48` |
| 253 | Goods for sale | `sc.goods`, then `sc.line35` to `line41`, `inventory_other` |
| 254 | The home, and a loss | `sc.ho_uses`, `ho_other`, `ho_sqft`, `ho_home_sqft`, `at_risk` |
| 255–258 | Lane 6b (vehicles, equipment) | |
| 259 | The owner's health and long-term care insurance | `sc.hi_uses`, `hi_screen`, `f7206_line1`, `$ltc`, `ltc.payments`, `ltc.age` |
| 260 | The owner's own retirement plan | `person.plan`, `plan_screen`, `sep_rate`, `sep_contrib`, `simple_deferral`, `simple_age`, `simple_kind`, `simple_employer` |
| 261 | Self-employment tax | `person.se_screen` |
| 262 | The deduction for business income | `qbi.prior_form`, then `qbi.carryforward`, `qbi.reit_loss`; `qbi.suspended`; `qbi.coop_patron` |
| 263–264 | free | |

Why income first and the refusing facts second: N7's rule (lowest cost per chance of leaving first) would put the
five refusing facts before gross receipts, which nobody leaves on; the brief asks that the typical owner be asked
what they took in first, and one amount before the facts costs a refused filer one answer. The facts still come
before the thirty expense amounts (N11).

## Step 1 (bank only): order, `seq` and plain words for all 63 entries

Every entry of the lane has its new `order` and a `seq`. Every prompt except those named below is rewritten in the
bank; the form line's `source` and `label` are unchanged and stay as the source-faithful statement. The boilerplate
help "One of the values of …" is gone; the three enums have `value_labels`.

- **Frame.** The `sc` questions no longer begin "For this business — ": each says "this business" in its own
  sentence. Per-person questions (`$sc`, `person.*`) keep the person frame exactly, as the build requires.
- **`$sc` stays a list, worded as a question.** A yes/no selector (`choices`) fixes the entry keys, so it would cap
  the number of businesses a person can list; today's interview has no cap (N9). For the owner: the cheapest form
  would be Yes/No, then "add another business", which the page does not have.
- **Amounts are asked as "How much did this business …?"** with the common case in the prompt. What the source text
  excludes is in a short help ("Leave out …"), not in children. This is the part of N10 this step does not meet: the
  rules a rare filer needs are in help, where the norm wants them in children reached from the rare answer. It is
  listed under "Not finished".
- **Still lists (N1 not met), in plain words:** `sc.special` (18 items; a chapter 11 case and Medicaid waiver
  payments deleted as asked by `scope.other_income`), `sc.ho_other` (8), `sc.hi_screen` (6), `sc.method_other`,
  `person.plan_screen`, `person.se_screen`; `sc.statutory` is two refusing facts joined by "or".
- **`person.se_screen` cut from nine items to five** (bank only). Deleted as asked elsewhere, each checked against
  the text of the question that catches it on this branch: church employee income (`scope.schedule1`,
  `f8959.unsupported`); ministers, religious orders and Christian Science practitioners (`scope.schedule1`); a
  partnership's Schedule K-1 (`scope.schedule1`); farm income (`scope.schedule1`); a chapter 11 case
  (`scope.other_income`); Form 4137 and Form 8919 (`f8959.unsupported`); community income on a separate return
  (separate returns are refused). Kept: an approved Form 4361 or 4029; director's, fiduciary and fee-basis fees;
  Conservation Reserve Program payments (kept though the map deletes it with farm income: a landowner who does not
  farm may receive them); the optional method; exempt foreign earnings. The deletion holds only while lane 9's
  replacements for the scope screens keep those items (N9); see "Requests to other lanes".

### What the walk shows after step 1 (ran `draft-walk --only 05_self_employed`)

The self-employed persona: 133 questions as before, prompt words 9,905 → 8,373. Three things still arrive away
from their place, none of which a bank entry can move (for the order agent):

- **`sc.line1` (gross receipts, `seq` 2 of 250) is asked after all of block 251**, twenty questions after `$sc`.
  It waits on its own line's refusal entries (`sc.screened`, `sc.business_credit`, `sc.fuel_credit` stand on
  `sc.line1`), which the engine asks first (cause 2 of T-284). `sc.line2`, `line6` and `tips_ot` come before it.
- **`sc.line35` (opening inventory, first of 253) is asked last of 253**, after `sc.inventory_other`, whose refusal
  stands on `sc.line35`.
- **`s1a.overtime` and `s1a.tips` (lane 3) interrupt** between `sc.tips_ot` and block 251, and the vehicle's
  questions (lane 6b, still order 12 here) come between `$sc` and the income amounts. I take the first to be
  `sc.tips_ot` making Schedule 1-A reachable, and the second to be this branch's old order numbers for 6b; neither
  was traced.

## Step 2 (model): `qbi.unsupported` and `qbi.carryforward`, asked of everyone, taken apart

Before: every filer read `qbi.unsupported` (76 words, four unrelated items in form words, refuses) and
`qbi.carryforward` (30 words, an amount named by a form line). After: every filer answers two one-line questions by
the paper, and a business owner a third.

| Old item | Now |
|---|---|
| (1) qualified business or PTP income or loss other than the dividends and the Schedule C businesses | No question of its own. Its sources are a Schedule K-1, a rental (Schedule E) and a farm (Schedule F), each refused by `scope.schedule1` on this branch, which every filer answers first. Coverage row `business.qbi_other_income`. **This is my inference about what "other qualified business income" can be**, not read from the instructions line by line |
| (2) a REIT or PTP loss carried from an earlier year | `qbi.reit_loss`, a child of `qbi.prior_form` = Yes; refuses through `qbi.unsupported` |
| (3) losses or deductions suspended earlier and allowed now | `qbi.suspended`, asked only when the return has a business (`s1.has_sc`); refuses through `qbi.unsupported` |
| (4) a patron of an agricultural or horticultural cooperative | `qbi.coop_patron`, asked of everyone (a patron without a business is refused today, so the question keeps no gate); refuses through `qbi.unsupported` |
| `qbi.carryforward` | A child of `qbi.prior_form` = Yes |

- `qbi.prior_form` (new parent, by the paper): "Does your 2024 tax return include Form 8995 or Form 8995-A, the form
  for the deduction for business income?" Worded "include", not "claim": a 2024 return with a net business loss has
  the form and no deduction.
- `qbi.unsupported` is now a derived line (true when any of the three refusing children is true), so
  `qbi.eligible` still refuses `when: qbi.unsupported` with the same form text and remedy (MAP 4.1, item 2: the
  technique works; the build accepted it).
- Who could answer `qbi.prior_form` No wrongly: a person with a loss carried from 2023 whose 2024 return left the
  form out (the form is required in that case, so this is an incomplete 2024 return); a person whose 2024 return was
  joint with a former spouse. Neither has a guard.
- Who could answer `qbi.suspended`'s gate wrongly: nobody answers it; it is computed from the business list. A filer
  with suspended losses and no business in 2025 has them from a K-1 or a rental (`scope.schedule1`).
- The line numbers in the two children's prompts (line 16 and line 17 of the 2024 Form 8995) are those of the 2025
  form in `sources/2025/f8995.txt`; the existing model text already said line 16 of the 2024 form. I did not read a
  2024 form. Form 8995-A's lines are named by their title only.

## Step 3 (model): three plain parents over thirteen expense amounts

| Parent (new input) | Amounts now asked only after a Yes | Who could answer No wrongly, and the guard |
|---|---|---|
| `sc.employees` "Did this business have employees in 2025: people it paid wages to, not freelancers or contractors?" | `sc.line26`, `line14`, `line19` | An owner whose only employee is a husband, wife or child: the help says they count |
| `sc.goods` "Did this business sell goods in 2025 that it bought or made, or hold goods for sale at the start or end of the year?" | `sc.line35` to `line39`, `line41`; `sc.inventory_other` is reached only through `line35` | A builder or caterer unsure whether materials are "goods": the help says materials that become part of what is sold count, and to answer Yes when unsure |
| `sc.travel_meals` "In 2025, did this business pay for overnight travel, or for any meals, food or drink?" | `sc.line24a`, `meals_50`, `meals_80`, `meals_100` | A daycare owner (food for the children), an employer (a staff party), a shop giving food away: the parent says "any meals, food or drink" and the help names all three. Row `business.daycare_food` |

A wrong No to any of the three leaves out a deduction: the return then shows more tax, never less. Each parent is a
Bool input of `sc`; each amount keeps its id, is marked `gated_by`, and is read only by its gate line
(`sc.<amount>_if_<parent>`, zero when the parent is No). The map's third parent covered travel and business meals
only; `meals_100` (food deducted in full) holds daycare food and staff parties, so the parent was widened to "any
meals, food or drink" instead of leaving `meals_100` asked of every business.

Fixtures: every case with one of the thirteen amounts above zero (or `inventory_other` true) for a business now
states that business's parent as true (165 parent answers, in `fixtures/2025` and none needed in `fixtures/ny`);
no expected value or refusal was touched. `qbi.unsupported` left every fixture's inputs (true became
`qbi.coop_patron: true` in the seven cases that had it, none of which says which item it meant), and the one case
with a carryforward states `qbi.prior_form: true`.

The class M and mutation fixture files take no defaults, so every case of theirs that read the old questions now
states the new ones (`qbi.prior_form`, `qbi.coop_patron`, with a business `qbi.suspended`, and the three parents of
each business; false unless the rule above made one true), in `fixtures/2025` and `fixtures/ny/2025`. Checked by
script against the tree before this lane: 933 changed cases compared, none differs outside its `inputs`.

## Before and after, from the persona walks (ran `draft-walk`; counts are of this lane's questions only)

"This lane's questions": `$sc`, `sc.*`, `$ltc`, `ltc.*`, the `qbi.*` questions but `qbi.dividends`, and
`person.plan*`, `sep_*`, `simple_*`, `se_screen`. Counted by a scratch script over the one-line listings.

| Persona | Before: questions, prompt words | After: questions, prompt words |
|---|---|---|
| `01_single_w2` (no business) | 3 (`$sc`, `qbi.unsupported`, `qbi.carryforward`), 154 | 3 (`$sc`, `qbi.prior_form`, `qbi.coop_patron`), 72 |
| `02_couple_children_mortgage` (no business, two people) | 4, 216 | 4, 122 |
| `05_self_employed` (one business, a car, a home office) | 49, 3,130 | 43, 1,404 |

The whole walk of `05_self_employed`: 133 questions and 9,905 prompt words before; 127 and 8,179 after. Its help words
rose from 2,360 to 3,243: the amounts' exclusions went from the prompts into help (see "Not finished", 3).

A filer with no business still meets three of this lane's questions, not one: the business topic itself is one
question (`$sc`), and the two `qbi` questions are asked of everyone because a loss carried on a 2024 Form 8995 and a
cooperative's patron are situations today's interview covers for a filer with no business (N9).

A business the tool cannot handle is now told so sooner: the four `credits.yaml` rows that end at a refusal on the
business (`sc.business_credit`, `sc.fuel_credit`, `sc.screened`) are refused after about 90 answers, before any
expense is asked; before, the refusal came after every amount. Their rows lost the answers no longer reached.

## Cost and share table (my estimates on the owner's scale; shares from `gate_frequencies.yaml` where marked gf)

| Question or parent | Asked of | Share answering yes | Cost of yes, of no (before → after) | Note |
|---|---|---|---|---|
| `$sc` | every person | 19% gf (`business_any`) | no: 5 → 1; yes: 5 → 2 | 48 → 34 words; the No is "leave the list empty" |
| `qbi.prior_form` (new parent) | everyone | 20% est. (a business or real estate fund dividends in 2024) | replaces `qbi.unsupported` 20, 20 and `qbi.carryforward` 5, 5; now no: 2, yes: 5 (find the form) | Children `qbi.carryforward` 5 and `qbi.reit_loss` 5: C = 10, q = 0.8, g = 2 < 8 (N3) |
| `qbi.coop_patron` | everyone | under 1% est. | no: 1; yes: 2 | was one clause of `qbi.unsupported` |
| `qbi.suspended` | a return with a business | 1% est. | no: 2; yes: 5 | |
| `sc.employees` (new parent) | every business | 10% est. | no: 1, yes: 1; three amounts at 3 each: C = 9, q = 0.9, g = 1 < 8.1 | |
| `sc.goods` (new parent) | every business | 20% est. | no: 1, yes: 2; six amounts and a screen: C = 20, q = 0.8, g = 1.5 < 16 | |
| `sc.travel_meals` (new parent) | every business | 35% est. | no: 1, yes: 1; four amounts (were 214, 135, 73, 173 words): C = 20 → 12 reworded, q = 0.65, g = 1 < 7.8 | |
| `sc.line1` | every business | amount | 5 → 3 | 93 → 23 words |
| The seventeen other amounts asked of every business | every business | amounts | 3 to 5 each → 1 to 2 each | Exclusions moved to short help; see "Not finished" |
| `sc.special` | every business | 3% est. | no: 15 → 10; yes: 15 → 10 | Still one list of 18 (267 → about 200 words); not layered |
| `sc.passive` | every business | 95% est. yes (the answer that goes on) | yes: 10 → 3; no: 10 → 5 | 100 → 32 words; the rental clause is a second subject (not split) |
| `person.se_screen` | every person with a business | 1% est. | no: 10 → 5 | 146 → 73 words; five items left |
| `person.plan` | every person with a business | 5% est. | 3 → 1 | plain labels |

Shares marked est. are my judgment, not measurements.

## Model changes

| File | Change |
|---|---|
| `forms/2025/qbi.yaml` | New inputs `qbi.prior_form`, `qbi.reit_loss`, `qbi.suspended`, `qbi.coop_patron`; new constant `qbi.no` (the year parameter `s3.no`); gate lines `qbi.reit_loss_if_prior_form`, `qbi.suspended_if_business` (reads `s1.has_sc`), `qbi.carryforward_if_prior_form`. `qbi.unsupported` is a derived line, no longer an input. `qbi.carryforward` is marked `gated_by`; `qbi.business_any` reads its gate line |
| `forms/2025/f8995.yaml` | `f8995.line3` reads `qbi.carryforward_if_prior_form` (one word) |
| `forms/2025/sc.yaml` | New inputs `sc.employees`, `sc.goods`, `sc.travel_meals`; thirteen amounts marked `gated_by`, each with a gate line (`sc.line26_if_employees`, `line14_if_employees`, `line19_if_employees`; `sc.line35_if_goods` to `line39_if_goods`, `line41_if_goods`; `sc.line24a_if_travel_meals`, `meals_50_if_travel_meals`, `meals_80_if_travel_meals`, `meals_100_if_travel_meals`); the readers (`sc.line28`, `line28_pre179`, `line40`, `line42`, `meals_50_ded`, `meals_80_ded`, `line24b`) read the gate lines. No other line changed |
| `interview/2025/stage4.yaml`, `sales.yaml` | The new inputs listed where the old ones were |
| `fixtures/2025/defaults.json` | Defaults (false) for the seven new Bool inputs; `qbi.unsupported` removed |
| Fixtures' inputs | As step 2 and step 3 say; `fixtures/ny/2025` lost its `qbi.unsupported: false` entries |
| `engine/src/generate.ts` | Generated businesses answer the three parents yes (so every amount is still read) and `qbi.prior_form` no |
| `interview/2025/coverage/business.yaml` | New, 14 rows. `credits.yaml`: its four rows with a business answer `tips_ot` and the three parents and no longer state the gated amounts |
| `interview/2025/personas/05_self_employed.yaml` | Same person; the three parents answered (employees no, goods no, travel and meals yes), the amounts beneath a No removed, `qbi.suspended: false` |

## Review debt

Every reworded prompt is unreviewed (no question review, screen review or false-no review was run). The forms
`sc`, `qbi` and `f8995` changed, so their transcription, render, class M, screen and completeness logs are stale;
the seven gates added have had no adversarial "who answers No wrongly" review beyond the tables above.
`engine/src/mutate.ts` pins mutants of `sc` lines by hash and mutation testing was not run; `docs/COVERAGE.md`
and `tools/coverage/tree.json` still name `qbi.unsupported` as a question.

## Places I was unsure

- **Items deleted from a prompt because another question refuses them** rest on the scope screens as they are on
  this branch: from `person.se_screen` (step 1), from `qbi.unsupported` item 1 (step 2), and from `sc.special` in the
  bank (a chapter 11 case and Medicaid waiver payments, both in `scope.other_income`). The form lines' labels still
  hold every item. If lane 9's replacements drop one of these, the item must come back here.
- **`sc.passive`** is asked as "did you yourself do all or most of the work of this business, or work in it more
  than 500 hours?", three of the seven tests, with the others in help. A filer who qualifies only by another test
  and does not open the help answers No and is refused: a refusal the old wording would not have given. I judged
  that better than seven tests in the prompt; the owner may not.
- **`sc.goods`**: the Schedule C instructions decide who must keep an inventory, and I did not put that rule in
  the question. The help tells an unsure filer to answer Yes.
- **`qbi.coop_patron`** says "farm cooperative" for "agricultural or horticultural cooperative", with the term in
  the help.
- **`$sc` help** no longer says which Forms 1099 are not a business; it gives the common sign only.
- **The typed amounts' help** ("Leave out …") is my shortening of each line's source text. I did not check each
  prompt against its source clause by clause afterwards. Left out knowingly: the name, image and likeness royalties rule and the accounting
  method clause of `sc.line10`, `line11` and `line26` (cash: paid in 2025; accrual: incurred); conventions outside
  North America and the $5 a day for incidentals in `sc.line24a`; the conditions on a client meal in `sc.meals_50`
  (ordinary and necessary, you or an employee present, billed apart from entertainment); the standard meal and snack
  rates for family daycare in `sc.meals_100`. The form lines keep them.

## Found and not fixed

- Commit `e8a85cf0` (step 1) left four rows of `coverage/credits.yaml` failing: `sc.tips_ot` is now asked before
  the refusals those rows end at. I committed without reading the coverage result to its end. The next commit
  fixes the rows.
- `sc.line1` carries the three refusals of the whole business (`sc.screened`, `business_credit`, `fuel_credit`), so
  under today's engine no order number can bring gross receipts first. Moving the refusals to another line would
  change the line a fixture names in an expected refusal, so I left them.
- `sc.statutory` joins two refusing facts with "or" (MAP 4.3 wants two questions).
- A person whose only plan is a solo 401(k) answers `person.plan` "No, neither" and is never asked
  `person.plan_screen`; the catch today is `scope.schedule1` ("other qualified retirement plans for the
  self-employed"), and after the redraft lane 9's `scope.se_plan_other`.

## Requests to other lanes

- **Order agent.** (1) `sc.line1` asked at its `seq` (2 of block 250) although refusal entries stand on its line;
  the same for `sc.line35` and `sc.inventory_other`. (2) Lane 3's `s1a.overtime` and `s1a.tips` not to interrupt
  after `sc.tips_ot`. (3) Blocks 259 to 262 are per business, per person and per return in turn; they should be
  asked in that order after lane 6b's blocks.
- **Lane 9.** Keep refusing, in the questions that replace the scope screens: church employee income; ministers,
  religious orders and Christian Science practitioners; a partnership's or S corporation's Schedule K-1 (including
  a publicly traded partnership); rentals and royalties; farm income; a chapter 11 case; Medicaid waiver payments;
  Form 4137 and Form 8919 (with lane 7b's `f8959` questions). Lane 6a's shortened `person.se_screen`, `sc.special`
  and `qbi.unsupported` rely on them.
- **Lane 6b.** `$scveh` and `$asset` are still at order 11 and 12 on this branch, so they are asked straight after
  `$sc`, before the business's income; at 255 and 257 they follow block 254.
- **Lane 3.** `sc.tips_ot` (250, `seq` 5) is the business's side of the tips and overtime deduction; if the tips
  topic wants it beneath its own questions, it is a bank entry of mine to move.
- **Lane 4b (`person.yaml`).** Splitting `person.plan_screen` (six items) and `person.se_screen` (five items) into
  children needs inputs in `person.yaml`. Wanted: beneath `person.plan` = SEP, the rate question first and "a rate
  that is not a whole percent or is over 25%" as its check; beneath any plan, "Did you also put money into another
  retirement plan for 2025, at a job or of your own?"; Roth SEP or SIMPLE as a value of `person.plan`.
- **Lane 8a.** `sc.hi_screen`'s first item (Marketplace insurance with a premium tax credit) is known from
  `$f1095a` (N8). I did not build the gate.

## Candidates for one tick-list

1. **"Which of these did this business have in 2025?"** (every business; each a parent with questions beneath
   it): employees (`sc.employees`); goods for sale (`sc.goods`); overnight travel, meals or food
   (`sc.travel_meals`); part of your home used for it (`sc.ho_uses`); health insurance you paid for yourself
   (`sc.hi_uses`). Five ticks. Their `seq` numbers are not adjacent today, because each is followed by its own
   children; a tick-list page would ask the five first.
2. **"Is any of these true of this business?"** (every business; each refuses): owned together with your husband
   or wife (`sc.spouse_owned`); a statutory employee's income or notary fees (`sc.statutory`); it claims a business
   tax credit (`sc.business_credit`); it wants fuel tax back (`sc.fuel_credit`). Four ticks, `seq` 1, 2, 6, 7 of
   block 251. `sc.passive` does not belong: its ordinary answer is Yes.
3. For another lane's list of rare situations asked of everyone: `qbi.coop_patron`; and for a list "from your 2024
   return": `qbi.prior_form` (with lane 6b's section 179 carryover and lane 5b's capital loss carryover).

## Ids added, removed, renamed

- Added (questions): `sc.employees`, `sc.goods`, `sc.travel_meals`, `qbi.prior_form`, `qbi.reit_loss`,
  `qbi.suspended`, `qbi.coop_patron`.
- Added (lines without a question): `qbi.no`, `qbi.carryforward_if_prior_form`, `qbi.reit_loss_if_prior_form`,
  `qbi.suspended_if_business`, and the thirteen `sc.<amount>_if_<parent>` gate lines.
- Removed as a question: `qbi.unsupported` (it stays as a derived line and as the refusal's gate).
- Renamed: none. Ids changed from the map: none (`qbi.prior_form` and `qbi.coop_patron` are the map's; the map
  named no ids for the three parents or for the two other `qbi` children).

## Not finished, in rank order

1. **`sc.special` (map rank 4).** Reworded in the bank only: 18 items in plain words, still one list read by every
   business (255 words as shown). The layering I would build: employment credits beneath `sc.employees` = Yes;
   licenses to amortize beneath `sc.line23` above zero; cruise travel beneath `sc.line24a` above zero; Form
   1099-PATR amounts beneath `sc.line6` above zero; business interest limited beneath `sc.line16a` or `line16b`
   above zero; recapture and lease inclusion beneath lane 6b's equipment and vehicle questions (a request to 6b);
   a parent by trade for depletion, the commercial buildings deduction, sound recordings, the capital construction
   fund and extraterritorial income; and flat one-line questions for the rest (work for a former employer, a
   hobby, an LLC taxed as a corporation, the installment method, research costs, a dependent care plan for
   yourself, earlier passive losses). Each child refuses through `sc.special` kept as a derived line, as
   `qbi.unsupported` was. With it: `sc.method_other` as "cash or accrual, unchanged in 2025?" with children;
   `sc.passive` split from its rental clause; `sc.at_risk` behind a plain parent; `sc.statutory` as two questions.
2. **The home office and the owner's insurance (map rank 5).** `sc.ho_other` and `sc.hi_screen` are reworded in the
   bank and still lists (each reached only after a Yes). `sc.f7206_line1` and `ltc.payments` are shorter, with the
   tests of a qualified long-term care contract in help instead of beneath "Is it a policy sold as tax-qualified
   long-term care insurance?".
3. **Exclusions as children (N10; map rank 7).** The amounts' "Leave out …" rules sit in help. Each belongs in a
   child of an amount above zero.
4. **`person.plan_screen`, `person.se_screen` (map rank 6).** Shortened in the bank; the split needs
   `person.yaml` (lane 4b).
5. **`$sc` as Yes or No.** Needs a page that adds entries after a Yes.
