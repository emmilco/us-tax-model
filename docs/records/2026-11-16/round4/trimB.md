# Lane T-trimB: N10 trims for the overruns outside the k1/sche/rental/sa/household lane

claude-opus-5-5, judgment, year 2025, us and ny. Written 2026-11-16. Read only on `P/scratch/b-chain/work/` and xint.
No build, walk, engine run, test or model call was made.
Labels: **[C path:line]** means checked against that file in this session. **[I]** means my inference.

## Summary

- **Scope.** 44 rows of `fix-round.md` section 7 are in my share: 35 federal and all 9 NY.
- **Output.** `P/round4/trimB.json` holds 49 edits.
  - Scope sources whose `label` repeats the source get two rows each: `label` and `source`.
  - `tipjob.listed` gets a help edit, because the help takes the examples cut from its prompt.
- **What each row holds.** Each row has:
  - `old` and `new`: the parsed YAML values. `old` was read from the work tree.
  - `line`, `old_raw` and `new_raw`: the exact source lines. Several bank and form texts are wrapped plain scalars, so the
    parsed value does not appear in the file as written.
  - `old_raw` occurs exactly once in its file [C].
  - Each `new_raw` is one line, in the same scalar style as the original.
  - f8853c rows also carry `words_shown_*`, which count the per-entry frame.
- **Verification [C `scratch/round4-trimB/trims.py`, `check.txt`].**
  - All 49 raw replacements were applied to copies in `scratch/round4-trimB/applied/`. Each of the 7 files was reparsed.
  - Each parsed file equals the original with only the named fields changed to `new`. No other value differs.
  - Words are counted by the engine rule from `n10.py`.
- **Result: 37 of 44 rows are now within the limit.** Seven stay over, each with its reason below:
  - `f1040.digital_assets` prompt: 32, unchanged.
  - `scope.foreign_shares`: 28.
  - `ny_it201.ask.529_nonqualified` help: 44.
  - `ny_it201.ask.owes_use_tax` prompt: 40.
  - `ny_it201.ask.owes_use_tax` help: 41.
  - `ny_it201.ask.est_any` prompt: 32.
  - The f8853c per-entry prompts: within 40 shown. Whether 25 or 40 applies is the owner's call (caveat in section 7).
- **Guards.** No cut removes a guard. Two items move from a prompt into help or a tick label, and both are flagged:
  - `ny_it201.ask.est_any`: estimated tax passed from an estate or trust moves to the help.
  - `scope.medicaid_waiver`: "through an agency" now appears only in the shown tick label and the help.
- **Wording fixes beyond length.** Two edits also fix a wrong reading:
  - `ny_it201.ask.real_property_credit` prompt: a renter who owns no real estate no longer reads the $85,000 test as
    true. Under the old wording that was an over-refusal.
  - `f5695.any` help: "A panel" becomes "An electric panel".

## Table

Words are before and after. "shown" adds the per-entry frame (11 words).

| Entry | Field | Where | Before | After |
|---|---|---|---|---|
| `f1040.withheld_other_any` | help | us bank | 44 | 40 |
| `s2.hsa_testing` | help | us bank | 42 | 40 |
| `sales.aggregate_eligible` | prompt | us bank | 39 | 25 |
| `sb.bonds_any` | help | us bank | 42 | 35 |
| `scope.armed_forces` | label + source | scope.yaml | 30 | 25 |
| `scope.rental` | label + source | scope.yaml | 36 | 25 |
| `scope.medicaid_waiver` | label + source | scope.yaml | 33 | 22 |
| `scope.medicaid_waiver` | help | us bank | 42 | 39 |
| `scope.religious_work` | label + source | scope.yaml | 53 | 25 |
| `scope.recovery` | help | us bank | 44 | 40 |
| `scope.foreign_shares` | label + source | scope.yaml | 43 | **28 (kept over)** |
| `scope.nol` | help | us bank | 41 | 39 |
| `sd.sold_other` | help | us bank | 42 | 38 |
| `f1040.estimated_any` | help | us bank | 44 | 40 |
| `f1040.line26` | help | us bank | 43 | 39 |
| `eic.lived_with_relative` | source | eic.yaml | 30 | 25 |
| `f8962.mfs_exception` | help | us bank | 50 | 40 |
| `f8962.alien_below` | prompt (child) | us bank | 41 | 39 |
| `s1.alimony_any` | prompt | us bank | 32 | 25 |
| `s1.alimony_any` | help | us bank | 41 | 35 |
| `s1.inmate_wages` | prompt | us bank | 29 | 23 |
| `s1.gambling_winnings` | help | us bank | 44 | 40 |
| `s1.scholarship_any` | prompt | us bank | 27 | 25 |
| `s1.hobby_any` | prompt | us bank | 29 | 25 |
| `f1040.digital_assets` | prompt | us bank | 32 | **32 (kept, no row)** |
| `f1040.digital_assets` | help | us bank | 45 | 35 |
| `s1.alimony_paid` | help | us bank | 41 | 40 |
| `s1.cod_bankrupt` | source | s1.yaml | 36 | 25 |
| `s1.cod_interest` | source | s1.yaml | 30 | 23 |
| `f8853c.periodic` | prompt (per-entry) | us bank | 28 (shown 39) | 25 (shown 36) |
| `f8853c.others_paid` | prompt (child, per-entry) | us bank | 38 (shown 49) | 29 (shown 40) |
| `f8853c.line24` | prompt (child, per-entry) | us bank | 31 (shown 42) | 26 (shown 37) |
| `rec.two_returns` | help | us bank | 43 | 40 |
| `tipjob.listed` | source | tipjob.yaml | 41 | 25 |
| `tipjob.listed` | help (not an overrun; takes examples) | us bank | 33 | 36 |
| `f5695.any` | help | us bank | 41 | 38 |
| `ny_it201.ask.special_accrual` | prompt (child) | ny bank | 41 | 38 |
| `ny_it201.ask.out_of_state_bond_interest` | help | ny bank | 44 | 40 |
| `ny_it201.ask.529_nonqualified` | help | ny bank | 53 | **44 (kept over)** |
| `ny_it201.ask.real_property_credit` | prompt (child) | ny bank | 46 | 37 |
| `ny_it201.ask.real_property_credit` | help | ny bank | 59 | 37 |
| `ny_it201.ask.owes_use_tax` | prompt (parent) | ny bank | 49 | **40 (kept over)** |
| `ny_it201.ask.owes_use_tax` | help | ny bank | 53 | **41 (kept over)** |
| `ny_it201.ask.est_any` | source (parent) | ny_it201.yaml | 48 | **32 (kept over)** |
| `ny_it201.ask.est_any` | help | ny bank | 43 | 35 |

## Kept overruns and the wrong answer that cutting would cause

1. **`f1040.digital_assets` prompt (32; no edit).**
   - `s1.digital_income` (staking, mining, fork, airdrop) is asked only after a Yes here
     [C work forms/2025/s1.yaml:585-591].
   - **Cutting "new coins":** an airdrop or fork recipient answers No, line 8v income is dropped, and the printed answer
     is wrong. Source: Yes if "Received digital assets as a result of a hard fork" [C sources/2025/i1040gi.cols.txt:295].
   - **Cutting "or another digital asset":** someone who only sold an NFT or a stablecoin reads "crypto" and answers No.
   - The Yes-list in the help was cut instead, 45 to 35.
   - Follow-up F1 would get it under 25.
2. **`scope.foreign_shares` (28).**
   - **Cutting "not through a U.S. fund":** a holder of a U.S. international index fund (common) answers Yes. They then
     meet `scope.pfic` ("Was any of it a fund … set up outside the United States"), may answer Yes about their own fund,
     and are refused wrongly [C work forms/2025/scope.yaml:996-1002].
   - **Cutting "set up abroad" for "foreign":** an Irish-incorporated company listed in the U.S. may read as American.
     The help glosses "set up abroad even if bought in the U.S." [I on the misreading].
   - "warrants" left the prompt, but is still in the tick label shown on screen.
3. **`ny_it201.ask.529_nonqualified` help (44).**
   - Each of the three exceptions prevents a wrong Yes, which adds the line 22 amount to NY income:
     - **Career training before July 4, 2025, or not paid to an eligible school, is nonqualified** [C
       sources/ny/2025/ny_it201i.cols.txt:251, "credentialing expenses … at an eligible educational institution on or
       after July 4, 2025"; :253, "credentialing expenses that are not paid to an eligible educational institution"].
     - **Loans only of the beneficiary or a sibling** [C :251].
     - **Transfers between family members' NY accounts** "are not considered distributions" [C :252].
   - Red-team A8 offered to drop the family-transfer sentence. I kept it: a parent who moves money to a sibling's
     account reads "take money out" and answers Yes [I].
4. **`ny_it201.ask.owes_use_tax` prompt (40, a parent).**
   - **"taxable in New York":** line 59 takes the income chart for any Yes without a large purchase
     [C work forms/ny/2025/ny_it201.yaml line59 `choose`]. Someone who bought only exempt goods out of state would be
     charged the chart amount.
   - **"Leave out a vehicle or boat taxed at the DMV":** without it, a car buyer whose tax went to the DMV answers Yes,
     then Yes to `use_tax_st141` ($1,000 or more), and is refused.
     - Source: "any unpaid sales and use tax on motor vehicles, trailers, all-terrain vehicles, vessels, or snowmobiles.
       This tax is paid directly to the Department of Motor Vehicles" [C ny_it201i.cols.txt:446].
     - The DMV exclusion cannot move to the child. A car-only buyer would answer the parent Yes and the child No, and be
       charged the chart.
   - **"such as online or out of state"** was kept as the recognition cue [C :446 lists "through the Internet, by
     catalog … or … in another state"].
   - Follow-up F2.
5. **`ny_it201.ask.owes_use_tax` help (41).**
   - Each item named there prevents a wrong value:
     - lower-rate purchases;
     - the Oneida exception [C :446, "(except for purchases subject to Oneida Nation taxes)"];
     - business purchases;
     - the $1,000 split that the next question uses.
   - What was dropped: "they go on its own return" and "by income".
6. **`ny_it201.ask.est_any` prompt (32, a parent).**
   - **"Besides tax taken from pay":** without it, a W-2 earner answers Yes and enters withholding again on
     `line75_amount`.
   - **"have a 2024 New York refund applied":** without it, someone who only had a refund applied answers No, and line 75
     is understated. "New York" also stops a federal refund applied to the federal 2025 tax from being counted.
   - The estate or trust item moved to the help (see below).
   - Follow-up F3.

## Moves into help or tick labels (allowed as pure wording; the reviewer should weigh them)

- **`ny_it201.ask.est_any`: estimated tax passed from an estate or trust** moves from the prompt to the help.
  `line75_amount` help already names it [C work interview/ny/2025/questions.yaml:307-308].
  - **Who could now answer wrongly:** a trust beneficiary who does not open the help answers No and loses the allocated
    payment on line 75. Source: "If you are a beneficiary of an estate or trust and are claiming your portion of any
    payment of estimated taxes allocated to you … include your amount on line 75" [C ny_it201i.cols.txt:583].
  - Rare. Follow-up F3 removes the trade.
- **`scope.medicaid_waiver`: "directly or through an agency or care plan"** leaves the prompt. It stays in the help.
  The tick label shown on screen keeps "through any agency" [C work questions.yaml, `scope.medicaid_waiver` tick].
  - **Who could now answer wrongly:** only someone on the CLI or "answer on its own" path who reads the full prompt and
    not the help, and who does not know that agency pay is Medicaid pay.
- **`tipjob.listed`: hotel housekeepers, desk clerks and barbers** move to the help. The prompt keeps server, bartender,
  cook, hairdresser and driver, and keeps "not manager".
  - Sources: tipped-occupations.txt lines 245 (bartenders), 249 (chefs and cooks), 272 (hotel desk clerks), 273 (maids
    and housekeeping cleaners), 301 (barbers, hairdressers), 321 (taxi and rideshare drivers), 323 (goods delivery
    people) [C].
  - **Who could now answer wrongly:** a hotel housekeeper or desk clerk who does not open the help may answer No, and
    their tips deduction is lost [I].
  - "driver" is broader than "taxi and delivery". A tipped driver who is not on the list (rare) may answer Yes [I].
  - The help drops "and nothing more is asked about them", which describes the engine's next step and is not a guard.
- **`s1.cod_bankrupt`: "or is it otherwise excluded from income (Form 982)"** leaves the prompt. The help already
  says "Count any other exclusion on Form 982 too".
  - The sibling ticks of `cod_why` cover the other Form 982 grounds [C work questions.yaml:4297-4326]: student loan or
    main-home mortgage; gift; price cut; stockholder; business, rental or farm.
  - Every tick refuses. A wrong No here is caught by a sibling for every Form 982 ground I know of [I].
- **`s1.cod_interest`: the medical-bill example** is already in the help.

## Red-team of every cut (who could now answer wrongly; source)

**Federal**

- **`f1040.withheld_other_any` help**
  - Kept: the K-1, 1042-S, 8805 and 8288-A forms, and "even with nothing paid to you".
  - Source: "Federal income tax withheld that is shown on a Schedule K-1. • Tax withheld that is shown on Form 1042-S,
    Form 8805, or Form 8288-A" [C i1040gi.cols.txt:898].
  - Nobody new could answer wrongly.
- **`s2.hsa_testing` help**
  - Only "put in" was dropped.
  - Source for the testing period: it "ends on the last day of the 12th month following that month … other than because
    of death or becoming disabled" [C i8889.cols.txt:38, 205].
- **`sales.aggregate_eligible` prompt**
  - Still five conditions, same as the source: "(other than sales of collectibles) … doesn't show any adjustments in box
    1f or 1g; • The Ordinary box … isn't checked; … don't need to make any adjustments …; and • You aren't electing to
    defer income due to an investment in a QOF" [C i8949.cols.txt:70].
  - **Who could now answer wrongly:** "not an opportunity zone fund" could be read as being about the thing sold, not
    a deferral election. The old "fund investment" had the same reach [I].
- **`sb.bonds_any` help**
  - Nothing dropped. "CD" is glossed at first use.
  - Source: p550 treats CDs of more than one year under OID [C p550.cols.txt:308]. That a brokered CD counts here is
    relayed from the existing help [I].
- **`scope.armed_forces` source and label**
  - "Since the start of 2022" becomes "In 2022 or later". The span is the same.
  - Nobody new could answer wrongly.
- **`scope.rental` source and label**
  - The examples are cut. "anything you own or lease" stays.
  - **Who could now answer wrongly:** a person who rents out a car on a car-sharing app reads only the prompt and
    thinks "rent out" means real estate.
  - The help and the tick ("Anything you own or lease rented or offered for rent") still cover them [C work
    questions.yaml, `scope.rental`].
- **`scope.medicaid_waiver` source, label and help**
  - Covered under "Moves" above.
  - "living in your home" is kept. Source: "caring for someone living in your home with you" [C i1040gi.cols.txt:8661].
  - A13 sentence: "Pay for caring … is pay for work in someone's home" becomes "Caring … is paid work in someone's
    home". Same meaning.
- **`scope.religious_work` source and label**
  - This is a parent of the refusing children `scope.clergy` and `scope.church_exempt_wages` [C work
    scope.yaml:649-690].
  - Cut from the prompt: "paid in any form (money, housing or offerings), by anyone", "of any title (a minister,
    priest, rabbi or imam)" and "for work".
  - **Who could now answer wrongly:**
    - A minister paid only in housing, or only by families' wedding fees. The help names both ("pay in housing or
      offerings … fees from families").
    - An imam or rabbi unsure whether "clergy" applies to them [I, low].
  - Source: "services you performed as a minister, member of a religious order, or Christian Science practitioner"
    [C i1040sse.cols.txt:14]. Church employees: "wages you received as an employee … of a church or qualified
    church-controlled organization" [C :25].
- **`scope.recovery` help**
  - Nothing dropped.
  - Source: "If you didn't itemize deductions for the year for which you received the recovery of an expense that was
    deductible only if you itemized, don't include any of the recovery" [C p525.cols.txt:835].
- **`scope.nol` help**
  - The A3 wording is kept, and so is its Form 8582 exclusion. The source was relayed by red-team A3 [I].
- **`sd.sold_other` help**
  - Nothing dropped.
  - Oil, gas and mineral property is listed with business property [C i4797.cols.txt:5].
- **`f1040.estimated_any` help**
  - Nothing dropped. The January 2025 exclusion from C1 is kept.
  - "joint payments a spouse or former spouse sent" becomes "joint payments with a spouse or former spouse". This now
    covers payments either one sent, which matches the line 26 rule.
  - Source: "If you and your spouse paid joint estimated tax but are now filing separate income tax returns, you can
    divide the amount paid in any way you choose as long as you both agree" [C i1040gi.cols.txt:902].
- **`f1040.line26` help**
  - Same rule as before.
  - Source: as above, plus "If you can't agree, you must divide the payments in proportion to each spouse's individual
    tax as shown on your separate returns for 2025" [C :902].
- **`eic.lived_with_relative` source**
  - "in the same home as" becomes "with".
  - Source: "Could you be a qualifying child of another person for 2025?" [C i1040gi.cols.txt:978, 994].
  - Nobody new could answer wrongly.
- **`f8962.mfs_exception` help**
  - "another family member" becomes "a relative".
  - "Keep any records you have; do not send them" becomes "Send no proof". This keeps the reassurance that stops a
    victim without papers from answering No.
  - Source: "Domestic abuse includes physical, psychological, sexual, or emotional abuse, including efforts to control,
    isolate, humiliate, and intimidate … abuse of an individual's child or other family member living in the household
    may constitute abuse" [C i8962.cols.txt:82]. Also: "Do not attach documentation" [C :87].
  - The 3-year limit is a separate child, `f8962.mfs_three_years` [C xint forms/2025/f8962.yaml:232].
- **`f8962.alien_below` prompt**
  - Only "who was" was dropped. No meaning change.
- **`s1.alimony_any` prompt and help**
  - "alimony: support paid to or for a husband or wife after a divorce or separation" becomes "alimony or other spousal
    support after divorce or separation". Separate maintenance under a separation is kept.
  - "paid to a landlord or school" was dropped. "Count payments made for the other person" stays.
  - Source: "Cash payments, checks, or money orders to a third party on behalf of your spouse … can be alimony"
    [C p504.cols.txt:422].
- **`s1.inmate_wages` prompt**
  - "other correctional facility" was dropped.
  - **Who could now answer wrongly:** someone held in a juvenile or other non-"jail or prison" facility [I, rare]. A
    Yes refuses.
  - Source: "services performed while an inmate in a penal institution" [C i1040gi.cols.txt:8666].
- **`s1.gambling_winnings` help**
  - Kept: "goods won by gambling" (A14), and "Give 0 if none was gambling". The parent also takes prizes and awards
    [C work s1.yaml:694].
  - Source: "Gambling winnings include lotteries, raffles, a lump-sum payment from the sale of a right to receive future
    lottery payments" [C i1040gi.cols.txt:8611].
- **`s1.scholarship_any`, `s1.hobby_any` prompts**
  - Articles were dropped. "or pastime not run as a business" becomes "(not a business)".
  - Source: "Activity not engaged in for profit income" [C i1040gi.cols.txt:8636].
- **`f1040.digital_assets` help**
  - The Yes-list items that repeat the prompt were dropped. Every No item is kept, including gift and inheritance.
  - Source: "Don't report a gift or inheritance of digital assets on line 8v" [C i1040gi.cols.txt:8668].
- **`s1.alimony_paid` help**
  - "only" was dropped. Noncash transfers are still left out by "Leave out … property".
  - Source: "Cash payments, checks, or money orders" [C p504.cols.txt:422].
- **`s1.cod_bankrupt`, `s1.cod_interest`**
  - Covered under "Moves" above.
  - Source cited in the form: "Debt canceled in a title 11 bankruptcy case isn't included" and "to the extent that you
    were insolvent immediately before the cancellation" (p4681 p. 6) [C work s1.yaml:1394, relayed cite].
- **f8853c**
  - `periodic`: keeps "or other period" and the box 3 check. Source: "per diem or other periodic basis"
    [C i8853.cols.txt:250].
  - `others_paid`: keeps both payment kinds. "accelerated death benefits" becomes "life insurance paid early due to
    illness" [C :257].
  - `line24`: keeps the set-rate exclusion in the prompt. A per-diem-only filer who counted those payments as
    reimbursement would raise line 24 and overstate line 26 [I, line arithmetic, as in red-team A5].
- **`rec.two_returns` help**
  - Kept: C3's "counts as money back", and the note on what the next questions are about.
- **`tipjob.listed`**
  - Covered under "Moves" above.
- **`f5695.any` help**
  - Kept: condo and co-op work [C i5695.cols.txt:32, "treated as having paid your proportionate share"].
  - "electric panel" is added. The panelboard is enabling property [C :163].

**NY**

- **`special_accrual` prompt**
  - "reported for 2025" was dropped. "reported federally in another" still carries it.
  - A Yes ends the NY part. Source: "you may have to use special accrual rules" [C ny_it201i.cols.txt:841].
- **`out_of_state_bond_interest` help**
  - "Most" and "State" were dropped. "its cities and agencies" and "a U.S. territory" are kept.
  - Source: "states other than New York State or its local governments … tax-exempt bond mutual funds" [C :240].
- **`real_property_credit` prompt and help**
  - Source for the two tests: "The average monthly rent … was $450 or less, not counting charges for heat, gas,
    electricity, furnishings, or board", and "The current market value of all real property you owned … was $85,000
    or less" [C ny_it214i.cols.txt:11, 13].
  - "Own real estate worth $85,000 or less in all" no longer makes a renter who owns nothing answer Yes. That case could
    not qualify unless rent was $450 or less.
  - Help:
    - The $18,000 income test was dropped. The gate already applies it before the question is asked
      [C work ny_it201.yaml:2172-2185, `ny_it201.low_income`].
    - "six months or more" is kept [C ny_it214i.cols.txt:11].
    - "paid rent or property tax on it" was dropped.
  - **Who could now answer wrongly:** an owner whose home is fully tax-exempt and worth $85,000 or less answers Yes
    and is refused. This is over-refusal only, and the same as before.
- **`owes_use_tax`, `est_any`**
  - Covered under "Kept" and "Moves" above.

## Proposed follow-ups (model changes; not made)

- **F1. `f1040.digital_assets` as a tick-box parent of two items.** Use technique 3.1.
  - The items: "got crypto as pay, a reward or new coins" and "sold, traded, spent or gave crypto away".
  - The printed answer becomes the derived Or of the two, and `s1.digital_income` gates on the first item only.
  - Each prompt would be about 20 words.
- **F2. `owes_use_tax`: a DMV off-ramp of its own.**
  - Make the parent "bought anything taxable in New York without paying its sales tax", then a child "Was every such
    purchase a vehicle or boat whose tax you pay at the DMV?". A Yes to the child sets line 59 to 0.
  - This needs a new input and a new guard on line 59.
- **F3. `est_any` as three inputs with the old id derived.**
  - The inputs: estimated or extension payments; a 2024 NY refund applied; estimated tax passed from an estate or
    trust. They could share a small NY tick screen.
  - This removes the help move above.
- **F4. `529_nonqualified`: a child for the narrow exceptions.**
  - Ask "Was any of it for career training or a student loan?", then the date, school and sibling tests beneath it.
    The help shrinks to the rollover, death or disability and family-transfer items.
- **F5 (owner). The limit for per-entry prompts with a frame.** Section 7 caveat. My f8853c trims hold the shown text
  at 40 or less, not 25.
- **F6 (owner, plan item 5). Does N10's 25 bind tick-member prompts shown only behind "What this asks"?**
  - If not, these scope edits could keep more of their old detail:
    - `scope.religious_work`: "of any title", "housing or offerings".
    - `scope.rental`: the examples.
- **Side observation [I, not checked]:** the `out_of_state_bond_interest` help says "ends the interview". Other NY
  refusal helps say "ends the New York part". I left the text as it was.

## Reviews this makes due (when landed; line-scoped)

- **Form source and label changes:**
  - render and transcription for scope (7 lines), eic (1), s1 (2), tipjob (1) and ny_it201 (1);
  - `render --check`.
- **Bank prompt and help changes:** the next sampled screen review of the touched topics.
- **Coverage rows:** none should change, since no input, gate or order changed.
- **To confirm on the landing branch:** interview-coverage and a draft-walk of personas 03, 07, 15 and 21, which touch
  the money_a and money_b, paid_already and NY payments screens. Not run here.

## Files

- `P/round4/trimB.json`: the 49 edits.
- `P/scratch/round4-trimB/trims.py`: builds the JSON from the work tree, applies it to `applied/` and checks it.
- `P/scratch/round4-trimB/check.txt`: the check output.
- `P/scratch/round4-trimB/dump.txt`: the texts as found.
- `P/scratch/round4-trimB/applied/`: the 7 files after applying, for diffing against `P/scratch/b-chain/work/`.
