# Lane notes: 7a (your home, taxes you paid, gifts to charity, medical bills, the state tax refund)

Branch `lane/l7a`. Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no
model call was made. Form files: `forms/2025/sa.yaml`, `gift.yaml`, `refund.yaml`. Bank entries: `sa.*` (not
`sa.dependent`, `sa.excluded_income`, which are lane 1's), `$gift`, `gift.*`, `refund.*`.

A successor reads this file top to bottom, then "Not finished, in rank order".

## The design in one paragraph

The coordinator decided: plain parents, each a fact a person knows, with the amounts beneath; no single "do your
deductions exceed the standard deduction" question (a wrong No there would change the tax). Each parent's wrong No is
guarded by a second question asked only after a No, never by a longer parent. The model's printed lines keep their
values: a parent only decides whether an amount is asked or is zero, so the same facts give the same return.

## Step 1 (done): the Schedule A amounts beneath plain parents

Order numbers: 200 home, 201 taxes, 202 gifts, 203 medical, 204 the rest of Schedule A. Every entry has a `seq`.

**Superseded in part by step 4:** the state income tax rows below (`sa.state_fund_any`, `sa.state_tax_asked`) describe
step 1 as first built; step 4 replaced that guard with `sa.state_tax_other_any`.

| Parent (new input) | Asked | Its No-guard (new input, asked only after a No) | Amount beneath (gate line) |
|---|---|---|---|
| `sa.home_owner` "At any time in 2025, did you own a home or other real estate?" | everyone, 200/1 | `sa.home_other` (a loan on a boat, camper or mobile home one can live in; a mortgage on a home in someone else's name), 200/2 | `sa.mortgage_interest` (new input; `sa.line8a` is now its gate line), 200/3; `sa.line5b` (gate `sa.line5b_if_home_owner`), 200/6 |
| `sa.state_tax_any` "did you pay any state or local income tax? Count tax taken out of your pay (boxes 17 and 19 of a Form W-2)" | everyone, 201/1 | `sa.state_fund_any` (money taken from pay for a state disability, unemployment, family leave or Washington workers' compensation fund), 201/2 | `sa.line5a` (gate `sa.line5a_if_state_tax`), 201/3 |
| `sa.personal_property_tax_any` (a yearly tax on a car, boat or belongings based on value) | everyone, 201/4 | none: the question is the fact itself, and its help says a registration fee can carry it | `sa.line5c` (gate `sa.line5c_if_taxed`), 201/5 |
| `sa.gifts` (existing input, now 2025 gifts only; one line) | everyone, 202/1 | `sa.gift_carryover` (a gift carried over from an earlier year; refuses), 202/2 | `sa.line11`, `$gift`, `gift.*`, `sa.charity_limited` (existing gates), 202/3 to 8 |
| `sa.medical_any` "Were the medical and dental costs you paid in 2025 large: more than 7.5% of your income, after what insurance paid?" | everyone, 203/1 | `sa.medical_premiums` (health insurance paid for oneself: Medicare, Marketplace, COBRA, long-term care), 203/2 | `sa.line1` (gate `sa.line1_if_medical`), 203/3 |

Helper lines added: `sa.home_asked`, `sa.state_tax_asked`, `sa.medical_asked` (each: the parent or its guard is yes),
and the guards' gate lines `sa.home_other_if_not_owner`, `sa.state_fund_if_no_tax`, `sa.medical_premiums_if_not_large`,
`sa.gift_carryover_if_no_gifts`.

### Who could say No wrongly, and the guard

| Parent | The person who says No wrongly | Guard |
|---|---|---|
| `sa.home_owner` | Someone paying a loan on a houseboat or camper, or the mortgage on a home in a parent's or partner's name (an equitable owner), who does not think "I own a home". A person who sold in January: "at any time in 2025" is in the question | `sa.home_other` |
| `sa.state_tax_any` | A worker in Washington or Alaska (no income tax) with mandatory fund contributions taken from pay, which line 5a counts. A person who forgets withholding: the question names the W-2 boxes | `sa.state_fund_any` |
| `sa.gifts` | A person who gave nothing in 2025 but has a carryover: today a Yes to `sa.gifts` and then to `sa.charity_limited`, which refuses. A volunteer with out-of-pocket costs: named in the parent ("or spend your own money doing volunteer work for one") | `sa.gift_carryover`, which refuses with the same remedy text |
| `sa.medical_any` | A retired person whose Medicare premiums alone pass 7.5% of a small income; a person buying their own insurance. Neither thinks of premiums as "medical bills" | `sa.medical_premiums` |

### Cost and share (my estimates; the owner rates costs himself)

Shares marked *gf* are from `gate_frequencies.yaml`; the others are my judgment. Cost on the owner's scale.

| Question | Share answering yes | Cost of No | Cost of Yes | Children's cost C | Pays for itself (g < q·C)? |
|---|---|---|---|---|---|
| `sa.home_owner` | about 60% (*gf* `home_or_charity` is 60% for a mortgage, property tax or gifts together; owners alone I put at 55%) | 1 | 1 | 10 (two amounts read from papers; today 17 + 232 words) | 1 < 0.45 × 10 |
| `sa.home_other` | under 1% | 1 | 2 | the same amounts | a guard, not a saving: costs 1 for the 45% who said No |
| `sa.state_tax_any` | about 70% of wage earners (judgment: states with an income tax) | 1 | 2 | 5 to 10 (the amount: add W-2 boxes) | 2 < 0.3 × 8, narrowly. Its main gain is the wording: the typical Yes now reads 27 words, then an amount with a list, where it read 237 |
| `sa.state_fund_any` | 2% of those asked (judgment) | 1 to 2 | 3 | the amount | a guard |
| `sa.personal_property_tax_any` | 15% (judgment) | 1 | 2 | 5 | 1 < 0.85 × 5 |
| `sa.gifts` | 40% (*gf*) | 1 | 1 | 10 to 15 | existing parent |
| `sa.gift_carryover` | under 0.5% | 1 to 2 | 5 | refuses | a guard needed by N9 (the refusal must stay reachable) |
| `sa.medical_any` | 10% (judgment) | 2 to 3 (7.5% of income needs a moment) | 3 | 20 (totalling a year's medical costs) | 3 < 0.9 × 20 |
| `sa.medical_premiums` | 25% of those asked (retired people, Marketplace buyers; judgment) | 1 | 2 | 20 | a guard. It sends about a quarter of filers to the amount, most of whom take the standard deduction; the owner may prefer to fold "counting insurance you pay for yourself" into the parent |

### Model changes (step 1)

- **Inputs added:** `sa.home_owner`, `sa.home_other`, `sa.mortgage_interest`, `sa.state_tax_any`, `sa.state_fund_any`,
  `sa.personal_property_tax_any`, `sa.medical_any`, `sa.medical_premiums`, `sa.gift_carryover`. Defaults (all no, or
  zero) in `fixtures/2025/defaults.json`.
- **Input renamed:** `sa.line8a` (input) is now `sa.mortgage_interest`; `sa.line8a` remains as the printed line 8a, a
  `choose` on `sa.home_asked` (Part 4.1 of the map, "the old id stays, as a derived line"). Reason: `s3.yaml`, which
  no lane may edit, reads `sa.line8a` (`s3.has_mortgage_interest`, the gate of `s3.mcc`), and the build refuses any
  reader of a gated input other than its gate line. Lane 7b's `s2.mortgage_subsidy` can gate on `sa.line8a` above
  zero, as the map says.
- **Inputs now gated** (ids kept, the convention of the formal gates design): `sa.line1`, `sa.line5a`, `sa.line5b`,
  `sa.line5c`. The printed line numbers 1, 5a, 5b, 5c moved to their gate lines; `sa.line4` and `sa.line5d` read the
  gate lines.
- **`sa.gifts`** now means gifts made in 2025 only; the carryover bullet left its label. A carryover with no 2025
  gifts is `sa.gift_carryover`.
- **Refusal added:** `sa.line13` refuses `when: sa.gift_carryover_if_no_gifts`, with the form and remedy text of the
  existing `sa.charity_limited_if_gifts` refusal. This departs from Part 4.1 item 3 (refuse through the old id's
  line): `sa.charity_limited_if_gifts` is the gate line of `sa.charity_limited` and a gate line may hold only its
  input and a false. The situation is one today's interview covers (not a change of scope); its gate id is new.
- **Fixtures:** inputs only. A script added the parent as yes wherever a case states a non-zero amount beneath it,
  renamed `sa.line8a` to `sa.mortgage_interest` in `inputs`, and, in the class M and mutation files (which take no
  defaults), stated the parents and guards as no where the amount is zero. No `expect` was touched.
- **Engine:** `engine/src/generate.ts` sets the parents from the drawn amounts (as it did `sa.gifts`), so generated
  returns are unchanged; `engine/src/integration.ts` answers `sa.home_owner` before the mortgage interest;
  `tools/engines/generate_cases.py` states the new inputs. Profiles `sales.yaml` and `stage4.yaml` list them.

### Wording decisions and doubts (step 1)

- `sa.line1` (429 words) is now 250 words, reached only after a Yes to `sa.medical_any` or `sa.medical_premiums`. It
  still carries the rules as lists ("Whose costs count", "Leave out", "Special amounts"). N10 wants each rule as a
  child; that is a model change of about ten inputs (each exclusion its own amount) which I did not start. See "Not
  finished".
- `sa.line5a` and `sa.line5b` likewise: one question line and a list, reached only after a Yes.
- **The whaling captain** (a bullet of today's `sa.gifts`) is in the help of `sa.gifts`, not in a question. A person
  it applies to knows the expense is treated as a gift to charity. Unsure: the owner may want a question.
- **A gift shown on a Schedule K-1** left `sa.gifts` (map 2.7: `scope.schedule1` refuses every K-1 today, and lane
  9's `scope.k1` will).
- **`sa.charity_limited`**: the typical answer is now settled by one fact in the prompt ("A limit can apply only when
  the year's gifts are more than 20% of your income", Pub. 526 p. 14 tip, read in `sources/2025/p526.txt` line 1421).
  A filer above 20% still has to read Pub. 526, as today.
- `sa.medical_any` asks the filer to compare with 7.5% of income. The help gives one worked figure and "If you are
  not sure, answer Yes". A wrong Yes costs only the amount question.
- Dollar figures in `sa.line1` ($5,200, $50, the long-term care limits) are copied from the form line's `source`
  text in `sa.yaml`, not from the map.

## Review debt this creates

Every review log of `sa` is stale (transcription, render, class M, completeness, screen, false-no, question
review): new inputs and gate lines, changed labels, changed prompts. The wrong-No analyses above are mine and have
had no adversarial gate review. `rendered/2025/sa.md` and the reports under `reports/2025/` are regenerated only
where the draft check does so.

## Step 2 (done): the state refund, order 165

What the form did: `refund.received` (an amount, "zero if none", 62 words) was asked of everyone; above zero it
opened `refund.box8` and `refund.not_2024` (both refuse whether or not the filer itemized), then `refund.itemized`,
`refund.sales`, the two exception screens and the 2024 figures.

The map says "ask `refund.itemized` before the amount (90% leave there)". Read against the YAML this is only partly
possible: the two refusing screens are asked of every refund recipient today, and N9 keeps them so (a refund for
another year, or of a business tax, is refused whether or not the filer itemized for 2024). What changed:

1. `refund.any` (new input), a yes or no parent in place of the amount asked of everyone. `refund.has` is now
   "`refund.any` is yes" (it was "`refund.received` above zero"); `s1.yaml` reads `refund.has` as before.
2. `refund.received` is asked only where the worksheet is used (itemized for 2024, no sales tax choice): it is gated
   by `refund.received_if_worksheet`, which `refund.line1` reads. A filer who took the standard deduction for 2024
   answers five yes or no questions and never types the amount.
3. `refund.not_2024` is two inputs, `refund.other_year` (box 3 of Form 1099-G) and `refund.paid_other_time`; the old
   id is a derived line (either is yes), so the refusal is the same line with the same text (map 4.1).
4. Plain prompts by the paper for all nine questions before the 2024 figures; `refund.exc_tax` and `refund.exc_who`
   are lists, one item a line, in place of one sentence each.

Asking order seen in the coverage walks: `refund.any`, `refund.box8`, `refund.other_year`,
`refund.paid_other_time`, `refund.itemized`. Box 8 comes before the year because its refusal entry stands first on
`refund.taxable` (cause 2 of T-284); the `seq` numbers follow what the engine does today.

| Question | Share yes | Cost of No | Cost of Yes | Note |
|---|---|---|---|---|
| `refund.any` | 40% (*gf* `state_refund`) | 1 | 1 | today: 62 words and a typed zero |
| `refund.box8` | under 1% of recipients | 2 (a glance at Form 1099-G) | 2 | refuses |
| `refund.other_year` | 3% (judgment) | 2 | 2 | refuses |
| `refund.paid_other_time` | 5% (judgment: January estimated payments, balances due) | 2 to 3 | 3 | refuses |
| `refund.itemized` | about 10% | 1 | 1 | a No ends the topic |

**Wrong No to `refund.any`:** a filer whose refund was applied to next year's tax or taken for a debt and who "got
no refund": the help says to count both; and a filer with no Form 1099-G (the help says a state usually reports it).
I did not add a guard question: the old amount question had the same exposure and the wording carries it. Unsure.

**Fixtures:** `refund.any` yes where a case states a non-zero refund; `refund.not_2024` rewritten as
`refund.other_year` (and `refund.paid_other_time` no where it was no); four cases that withheld `refund.received`
(`null`) now withhold `refund.any`. The one refusal case, `stage16.refuse.refund.not_2024`, has `refund.other_year`
yes: its note does not say which of the two facts it meant.

## Step 3 (done): `sa.unsupported` taken apart

| Item of today's question | Goes to |
|---|---|
| Casualty or theft loss, a disaster loss added to the standard deduction | Deleted (map 2.7): `sd.other_forms` asks for "a casualty or theft of property" and refuses; lane 5b's `sd.casualty` takes it over. Request to lane 5b below |
| Line 16 list: casualty or theft of income-producing property | The same |
| Line 16 list: repayment over $3,000 under a claim of right | Deleted: `s3.repaid_income` asks exactly this and refuses |
| Line 16 list: federal estate tax on income in respect of a decedent; amortizable bond premium; ordinary loss on a contingent payment or inflation-indexed debt instrument; unrecovered investment in a pension; impairment-related work expenses | Five one-line questions, order 204, adjacent `seq` (candidates for one tick-list) |
| Foreign tax deduction (line 6) | A wish child at order 284, asked only when foreign tax was entered (`ftc.has_tax`, a derived line of `ftc.yaml`) |
| Generation-skipping tax deduction (line 6) | Deleted: the tax is charged on income distributions from a trust, which a Schedule K-1 reports, and `scope.schedule1` (lane 9: `scope.k1`) refuses those. My inference; flagged for the owner |
| Mortgage interest or points not on Form 1098 (lines 8b, 8c) | One child beneath the home parent |
| Mortgage debt over the limit; loan money used for something other than the home | Two children asked when mortgage interest is above zero |
| The sales tax election | A wish question at order 201 ("answer No to deduct income tax instead") |


`sa.unsupported` is a derived line, true when any item is (map 4.1), so every `refuses: when: sa.unsupported` is
unchanged, with the same form and remedy text.

**Inputs added (ten):** `sa.mortgage_unreported` (gate `sa.mortgage_unreported_if_home`, on `sa.home_asked`),
`sa.mortgage_over_limit` and `sa.mortgage_other_use` (gates `..._if_interest`, on the new helper
`sa.has_mortgage_interest`, line 8a above zero), `sa.sales_tax_wish`, `sa.foreign_tax_deduct` (gate
`sa.foreign_tax_deduct_if_tax`, on `ftc.has_tax`), `sa.estate_tax_income`, `sa.bond_premium`,
`sa.debt_instrument_loss`, `sa.pension_unrecovered`, `sa.impairment_work`. **Input removed:** `sa.unsupported`.

**Fixtures:** a case that stated `sa.unsupported` no now states nothing (or, in the class M and mutation files, all
ten items no). The eight cases that stated it yes state `sa.sales_tax_wish` yes: none says which item it meant
(five are class M cases whose expected values are on other forms; two are `stage4.refuse.sa.unsupported*`), and the
sales tax question is the one item asked of everyone with no gate.

**What a filer with nothing now meets in place of the 71 words:** the sales tax wish (20 words) and five one-line
rare questions (about 30 words each). The count rises by five; see "Candidates for one tick-list".

**The mortgage limit question** asks "more than $750,000 at any time in 2025, or more than the home is worth", with
the $1,000,000 limit for older loans in the help. It is a screen and errs toward a Yes (a refusal): a filer with
debt from before October 14, 1987 above the limit is refused though Pub. 936 would not limit them. Figures read in
`sources/2025/i1040sca.txt` (lines 543 to 560), not from the map.

## Step 4 (done): the two commonest amounts made short

After step 3 the walks showed the ordinary filer's commonest Yes still read a long list: `sa.line5a` 182 words for
every wage earner with state tax, `sa.line5b` 162 words for every homeowner. N4 puts the detail only a rare answer
needs behind the rare answer, so both were split (this supersedes the state tax row of the step 1 tables):

- **State income tax.** `sa.state_tax_any` now asks only about pay ("was state or local income tax taken out of your
  pay? Boxes 17 and 19 of a Form W-2 show it"), and `sa.line5a` is that amount ("Add boxes 17 and 19 of each Form
  W-2", 22 words). Every other way of paying (estimates, a payment with a return, withholding on other income, the
  state funds, territory tax, the charity-credit safe harbor) is `sa.state_tax_other_any`, asked of everyone, with
  its amount `sa.state_tax_other` (the list) beneath. Printed line 5a is the new `sa.line5a_total`, the sum of the
  two. `sa.state_fund_any`, its gate line and `sa.state_tax_asked` are gone: `sa.state_tax_other_any` is asked
  whatever the first answer, so it is also the guard of a wrong No (the Washington worker's fund contribution).
  Existing fixture amounts stay in `sa.line5a`; the sum is the same.
- **Property tax.** `sa.line5b` is one line ("How much property tax did you pay in 2025 on your home and on any other
  real estate you own that is not used for business?"). Its rules are a yes or no child,
  `sa.property_tax_other_any` (a list of six things the bill may include that do not count), and on a Yes the
  amount to leave out, `sa.property_tax_leave_out`. Printed line 5b is the new `sa.line5b_net` (the amount less the
  part left out, not below zero). This is the map's worked example 3, with its two children merged into one.

Inputs added in step 4: `sa.state_tax_other_any` (renamed from `sa.state_fund_any`), `sa.state_tax_other`,
`sa.property_tax_other_any`, `sa.property_tax_leave_out`. Lines added: `sa.state_tax_other_if_any`,
`sa.line5a_total`, `sa.property_tax_other_if_home`, `sa.property_tax_leave_out_if_any`, `sa.line5b_net`.

| Question | Share yes | Cost of No | Cost of Yes | Note |
|---|---|---|---|---|
| `sa.state_tax_any` | 70% of wage earners (judgment) | 1 | 2 (a glance at the W-2) | then `sa.line5a`, cost 3 |
| `sa.state_tax_other_any` | 15% (judgment) | 2 | 3 | then the list amount, cost 10 |
| `sa.property_tax_other_any` | 10% of owners (judgment; trash and sewer charges on a tax bill are not rare) | 3 (six lines to read) | 5 | then the amount to leave out, cost 10 |

Unsure: `sa.property_tax_other_any` is a list of six unlike items behind one yes or no. It is asked only of owners
and the typical answer is No after reading six short lines; splitting it further (one question per item) would be
six questions for every homeowner.

## Gifts: the per-group questions (wording only)

`gift.deduction`, `gift.public_securities` and `gift.special` have plain prompts; `gift.special` is a list of nine
one-line items. The Schedule K-1 item is kept, against map 2.7: `test-serve` uses this question as its example of a
bare "Schedule K-1" (`engine/src/serve-check.ts`), and the item costs only filers who list a group of property. The map's parent for it ("Is this group ordinary used
clothing or household goods worth $5,000 or less in all?"; a Yes skips the list) is **not built**: it needs
`gift.special` to become a derived line over a renamed input (the refusal names `gift.special`), and a rename of the
per-entry fixture inputs.

## Before and after (persona walks; `draft-walk --out /tmp/l7a_walks`, read after step 4)

Counted over this lane's questions only (`sa.*` but not `sa.dependent` and `sa.excluded_income`; `$gift`, `gift.*`,
`refund.*`), prompt words as shown.

| Persona | Before: questions, words | After: questions, words | Whole walk before | Whole walk after |
|---|---|---|---|---|
| `01_single_w2` (renter, one W-2, nothing in the topic) | 9, 1,405 | 17, 422 | 86 questions, 6,777 words | 94, 5,794 |
| `02_couple_children_mortgage` (mortgage, property tax, state tax, gifts of money) | 12, 1,471 | 25, 725 | 133, 10,168 | 146, 9,422 |

The renter's seventeen: `refund.any`; `sa.home_owner`, `sa.home_other`; `sa.sales_tax_wish`; `sa.elect_itemize`;
the five uncommon deductions; `sa.gifts`, `sa.gift_carryover`; `sa.state_tax_any`, `sa.state_tax_other_any`;
`sa.personal_property_tax_any`; `sa.medical_any`, `sa.medical_premiums`. The longest is 34 words. The count nearly
doubled while the reading fell by 70%: nine of today's questions were amounts and long screens (cost 5 to 20 each);
the seventeen are yes or no facts (cost 1 to 3 each). Five of them are the tick-list candidates.

The persona leaves `sa.state_tax_any` at the background's No; a wage earner in a state with an income tax says Yes
and is asked one amount more (`sa.line5a`, 22 words).

The couple's longest prompts are now `sa.property_tax_other_any` (the six-line screen) and `sa.charity_limited`
(44 words); `sa.line5a` fell from 240 words to 24 and `sa.line5b` from 235 to 29.

The transcripts were written to a scratch directory, not to `docs/provisional/walks/after/`, which every lane would
write and collide on.

## Questions that arrive away from their place (for the order agent)

Seen in the persona walks after step 2 (`node engine/dist/main.js draft-walk --out /tmp/...`), single W-2 filer:
`sa.home_owner`, `sa.home_other`, then `sa.elect_itemize` and `sa.unsupported` (order 204) **before** `sa.gifts`
(202), `sa.state_tax_any` (201) and `sa.medical_any` (203); `sa.gift_carryover` (202/2) arrives after
`sa.personal_property_tax_any` (201/4), not directly after `sa.gifts`. For the couple with a mortgage: `s3.mcc`
between `sa.mortgage_interest` and the rest; `sa.charity_limited` directly after `sa.gifts` and before `sa.line11`
and `$gift`; `sa.line5b` (200) after the gifts questions.

What I think each waits on: the refusal entries of `sa.line6` and the other refusing lines are evaluated in the
order written (`sa.unsupported` first, then the charity gate), and a line's own operands become reachable only after
them (cause 2 of T-284); the amounts are reached through `sa.line17`'s sum, in the sum's order (line 4 medical, 7
taxes, 10 interest, 14 gifts), not the block's. A direct target per block in `full.yaml` (`sa.line8e`, `sa.line5d`,
`sa.line14`, `sa.line4`) might keep each together; I did not edit `full.yaml`.

The whole topic comes after every question still numbered 0 to 31, since 165 and 200 to 204 are the highest numbers
on this branch.

## Requests to other lanes

- **Lane 5b (`sd.casualty`)**: the casualty words left `sa.unsupported`. `sd.casualty` must catch a personal casualty
  or theft loss, a loss of income-producing property (including a financial scam), and a disaster loss claimed with
  the standard deduction, each of which `sa.unsupported` named.
- **Lane 9 (`scope.k1`)**: a gift to charity and a generation-skipping tax deduction that reach a filer through a
  trust or a Schedule K-1 are no longer asked in `sa`; `scope.k1` (today `scope.schedule1`) is their refusal.
- **Lane 7b**: `sa.gambling_losses` (order 204, seq 7) belongs directly after the gambling winnings question in
  `s1` (N5); it is asked only with winnings. `s2.mortgage_subsidy` and `s3.mcc` can gate on `sa.line8a` above zero
  as planned (or on `sa.has_mortgage_interest`, the same test, now a line of `sa.yaml`).
- **Lane 1**: `sa.dependent` and `sa.excluded_income` are untouched in `sa.yaml` and the bank.
- **Order agent**: the section above.

## Candidates for one tick-list

Heading: **"Uncommon deductions"** (order 204, seq 2 to 6; each is its own yes or no, and a Yes to any refuses):
`sa.estate_tax_income`, `sa.bond_premium`, `sa.debt_instrument_loss`, `sa.pension_unrecovered`,
`sa.impairment_work`. Five items, about 30 words each as questions; as tick-boxes they shorten to "estate tax paid
on income you inherited", "premium left to deduct on a bond bought above face value", "a loss on an
inflation-protected or contingent payment bond", "after-tax money in a pension not got back before the owner died",
"work costs of a person with a disability". They are one theme only as "deductions few people have"; if the owner
finds that too loose, the two bond items could instead sit beneath lane 5a's interest questions and the pension
item beneath lane 4a's.

## Not finished, in rank order

1. **The rules inside `sa.line1` as children** (N10). The medical amount (about 250 words) still carries its rules
   as three lists, behind a Yes to `sa.medical_any` or `sa.medical_premiums`. The pattern of step 4 fits: a short
   amount ("How much did you pay for medical and dental care and health insurance, after what insurance paid
   back?"), then yes or no children each with an amount to leave out or a cap (insurance paid pretax or by an
   employer; costs paid from an HSA; Marketplace premiums and the credit; long-term care premiums over the age
   limit; a person on the policy who is not a dependent). New inputs default to no, so fixtures need no change.
   The same for `sa.state_tax_other` (about 130 words, reached by few).
2. **`gift.special` beneath a parent** (above).
3. **`sa.elect_itemize`** is reworded but still asked of everyone. It could be asked only when the itemized total is
   above zero and below the standard deduction (a computed gate). That removes a situation typed-in inputs can
   state today (electing to itemize nothing), so I left it for the owner.
4. **`refund.exc_tax` and `refund.exc_who`** as separate inputs, each item its own question read from the 2024
   return by its line. They are lists now. `refund.status` has no `value_labels`.
5. **`sa.medical_premiums`**: whether it should be folded into the parent (see the cost table).
6. `sa.spouse_itemizes`, `sa.spouse_extra` (married filing separately only; that status is refused) keep their
   wording, at order 204.

## For the owner

- The three guards asked after a No (`sa.home_other`, `sa.gift_carryover`, `sa.medical_premiums`) are not marked `gated_by`: the interview-rules check refuses a marked input that the
  all-No return is asked, and these are asked exactly then. Each is read only by its own `choose` line, as the
  convention for unmarked Count inputs has it.
- A renter with nothing answers more questions in this topic than before (see the report), each short. The count
  is what the owner objected to in the credits redesign; the tick-list would take five of them.
- The generation-skipping tax deduction and the whaling captain's expenses have no question of their own (above).
- `sa.gift_carryover` refuses through a new entry on `sa.line13` (same text, new gate id).

## What was run and seen, and what is inferred

Ran and saw: `tools/draft_check.sh` (the full check) on the tree of the final commit, every step ok: build; fixtures
1,854 of 1,854; interview-rules 0 problems (177 walks); coverage rows 0 problems; person wording current; the
spouse-wording, check and draft-walk self-tests; 753 CLI invocations; properties; the server test (351 checks);
twins; `render --check`. `draft-walk` over the twelve personas: 0 problems, ten complete, two refused where the
baseline refuses them. I read the one-line listings of personas 01 and 02 and the full text of a few questions as
shown; I did not read every new question as shown to a joint filer.

Inferred, not checked: that each plain prompt says what its form line's source-faithful label says (no review was
run; the wording of the amounts and screens was condensed by me from the labels in `sa.yaml`, `gift.yaml` and
`refund.yaml`); the wrong-No analyses; every share not marked *gf*; that lane 5b's and lane 9's questions will
catch the casualty and Schedule K-1 items that left this lane's questions (on this branch `sd.other_forms` and
`scope.schedule1` do, read in the YAML); that the generation-skipping tax deduction reaches a filer only through a
trust. The 2024 line numbers in the refund prompts are those already in the form's labels; none was added.
