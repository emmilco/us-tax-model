# Lane D2-trimfollow: the model-change follow-ups of trimA (F1 to F7) and trimB (F1 to F4)

claude-opus-5-5, judgment, year 2025, us and ny. Written 2026-11-16. Read only on `P/scratch/b-chain/work/` (base), with
xint for files the work tree does not hold. No build, walk, test, review, engine run or paid call. Scratch:
`P/scratch/round5-trimfollow/` (`lib.py` and one `u_<unit>.py` per patch; each writes `<unit>/a`, `<unit>/b` and the patch).
**[C]** = checked in this session against the named file. **[I]** = my inference. Word counts are whitespace counts
of the bank text as written (frame included where the bank writes it), not the engine's n10 rule.

## Summary

- **Five units have patches; six are designs only.** Every patch was checked with `patch --dry-run -p1` against a copy of
  its base, and each `b/` file was parsed (YAML or JSON) [C].
- **Ranking by filer benefit per cost** (section 1). Done as patches, in rank order: A-F3, A-F4, B-F1, A-F1, B-F2.
  A-F2 (`sa.line1`) has the largest benefit but is a lane of its own; it is designed here, not patched.
- **Three units are not worth doing as proposed:**
  - **A-F7 (seq swap).** The swap alone cannot drop the widowed sentence, because joint filers still meet
    `married_dec31` first (section 3, A-F7).
  - **B-F3 (NY `est_any` split).** It raises the words every NY filer reads.
  - **B-F4 (529 child).** It adds a question for the typical college-only filer, against N4.
- **Every patch keeps every refusal and value:**
  - Old ids that other forms read are kept as derived lines: `gift.special`, `asset.listed`, `f1040.digital_assets` and
    `ny_it201.ask.owes_use_tax`.
  - Or the old input is kept and only gated: `dependent.ptc_files`.
  - No expected value, refusal id or check baseline is touched.
- **What the patches do not include:**
  - The restated fixture inputs. The plans for them are in section 2.
  - New coverage rows, except two NY rows in B-F2. The rows a patch would break are restated in the patch.
- **One finding outside the brief (owner):** `gift.unrelated_use` ("Art or other belongings the charity will not use
  for its purpose") can draw a Yes from a thrift-store clothing donor ("Goodwill sells it"). That Yes is over-refused.
  - Under p526, the unrelated-use rule reduces only capital gain property [C p526.cols.txt:560-567].
  - The over-refusal is pre-existing; the old prompt has the same item. I did not narrow it, because that would change
    a refusal (N9).

### Bases and trims (COMMON round 5)

| Patch | Files (base) | Trim applied to the `a/` copy first |
|---|---|---|
| `patches/v4/tf-a-f3.patch` | work: `forms/2025/dependent.yaml`, `interview/2025/questions.yaml` | none (no trimmed field touched; trimA's `ptc_files` help is untouched by these hunks) |
| `patches/v4/tf-a-f4.patch` | work: `forms/2025/asset.yaml`, bank; xint: persona 13 | trimA `asset.listed` prompt (the entry is replaced) |
| `patches/v4/tf-b-f1.patch` | work: `f1040.yaml`, `s1.yaml`, bank, `fixtures/2025/defaults.json`, coverage `other.yaml`, `sales.yaml`; xint: personas 17 and 18 | trimB `f1040.digital_assets` help (`old_raw`→`new_raw`) |
| `patches/v4/tf-a-f1.patch` | work: `gift.yaml`, bank, `defaults.json`; xint: coverage `home.yaml` | none |
| `patches/v4/tf-b-f2.patch` | work: `forms/ny/2025/ny_it201.yaml`, NY bank, coverage `ny.yaml`; xint: `fixtures/ny/2025/defaults.json` | trimB `owes_use_tax` prompt and help (`old_raw`→`new_raw`) |

- The three patches that touch the bank (A-F4, B-F1, A-F1) touch different entries. A-F1 also moves `sa.line1` to seq 60.
- A-F4 and A-F1 overlap in no hunk, and B-F1 overlaps neither [I]. They were not applied in sequence.
- The defaults patches of B-F1 and A-F1 touch different entries [I].

## 1. Ranking (benefit per cost)

Benefit is the reading saved or the wrong answer prevented, multiplied by who reads it. Cost is the model change, the
fixture restatement and the reviews. Shares are my judgment [I], labelled for the owner to overrule.

| Rank | Unit | Who reads it | Benefit | Cost | Done |
|---|---|---|---|---|---|
| 1 | A-F3 `ptc_files` | Marketplace (PTC) filers with dependents | A dependent with no money of their own (most children) skips a 40-word threshold question. The gate is `dependent.own_money`, which is already asked, so no question is added (N8). | 1 gate line, 1 help sentence, 0 fixtures | patch |
| 2 | A-F4 `asset.listed` | every business asset entry | Typical asset: 54 words become 37 words. The computer item is asked only for property placed before 2018, known from `asset.placed` (N8). | 3 lines, a seq shift, 1 fixture | patch |
| 3 | A-F2 `sa.line1` | every medical-cost itemizer, including Medicare premium payers sent by `sa.medical_premiums` | 325 words become about 45, plus rare boxes. The largest saving in the set. | Large: a new sum, several amount children, the Marketplace term computed or asked, and about 1,000 fixture refs | design (own lane) |
| 4 | B-F1 `digital_assets` | every federal filer | Two one-subject boxes (N1); prompts of 24 and 22 words, from 32. A seller who received nothing skips `s1.digital_income`. Words read: about equal. | 3 lines, a seq shift, about 1,000 mechanical fixture refs, 8 coverage rows, 2 personas | patch |
| 5 | A-F1 `gift.special` | each noncash gift group of an itemizer | A 141-word list becomes two tick screens (about 120 words, scannable, labels ≤ 12). One step more. | 12 lines, 2 groups, about 310 fixture refs, 2 coverage rows | patch |
| 6 | B-F2 NY use tax | every NY filer | Parent goes from 40 words to 30. The DMV exclusion becomes its own child for the rare buyer. | 4 lines, 1 prompt, about 125 fixture refs | patch |
| 7 | A-F6 `days_personal` | landlords with personal use | Moves the 12-month rule to a child | Count input: it cannot be gated or chosen between (gates design) | design |
| 8 | A-F5 `rprop.basis` | every rental building | 37 words become about 13 + 13, but one step is added for every landlord (N12) | 3 lines, 18 fixtures | design; not recommended |
| 9 | B-F3 NY `est_any` | every NY filer | Guards a trust beneficiary (rare) | Words read rise from 32 to about 45 | design; not recommended |
| 10 | A-F7 household | ever-married filers | The seq swap does not let the help sentence go | Walk changes for every widowed single or HOH filer | design; not recommended |
| 11 | B-F4 NY 529 | NY 529 withdrawers | The help is 4 words over | Adds a question for the typical filer (N4) | design; not recommended |

## 2. Patches

### A-F3. `dependent.ptc_files` asked only of a dependent with money of their own (`tf-a-f3.patch`)

**Change.**
- `dependent.ptc_files` gains `gated_by: dependent.ptc_files_if_own_money`.
- The new gate line is a `choose`: `own_money` true selects `ptc_files`, and false selects `dependent.no`.
- `ptc_magi_counted`, the only reader [C `dependent.yaml:2285,2291`], now reads the gate line. This is the
  gates-design rule "every former reader … reads the gate line" [C `docs/2026-11-06_formal_gates_design.md:75-78`].
- `own_money` is unconditioned and asked for each dependent at order 120 [C `dependent.yaml:3451`, bank seq 16].
- `ptc_files` is at order 199, so the parent comes first.
- The `ptc_files` prompt is unchanged. It is now a child, so it is within the 40-word limit; it is 40 words.

**Who could answer No wrongly at the parent, and the guard.**
- The `own_money` source asks about "any income, benefits, savings …" [C `dependent.yaml:3456`]. Anyone who has to file
  because of income has income, so a true No cannot hide a filer.
- **The wrong No:** a student whose only income is a taxable scholarship of more than $15,750 (earned income for Chart B
  [C `i1040gi.cols.txt:165`]). The scholarship may be paid straight to the school, and the tick label says "money of
  their own".
- **Guard added (help):** "Count any income, even a scholarship." (help now 27 words).
- **Side effect:** that student now also meets `self_support_view`. Its help already says "A scholarship does not count
  as the person's own money" [C bank:2513]. That is one extra question and no value change.

**Red team.**
- "even a scholarship" is wider than "taxable scholarship". A student with a tax-free scholarship answers Yes and is then
  asked the threshold question (with "a taxable scholarship is pay"). Extra questions only.
- The gate's cite quotes i8962 p. 8 [C, existing cite] and i1040gi Chart B [C `i1040gi.cols.txt:165`].

**Fixture plan.**
- No restatement is needed. `own_money` defaults to true [C `defaults.json`, "true: the answer that opens …"].
- The 3 cases that state `ptc_files: true` (`f8962.json`: `stage18.blind.p15`, `stage18.mut.unclaimed_relative`) do not
  state `own_money` [C, script].
- The 128 cases stating false are unaffected.

**Coverage rows to add (predicted ends; not written into the patch).** Both need a full Marketplace walk. Build them from
`marketplace.yaml` sets `one_form`, `plain`, `column_b_right`, `lower_48` and `amounts_year`, plus a dependent
`kid` [I on the exact background].
- `marketplace.dependent_no_money`: `dependent[kid].own_money: false`. Expect proceeds, with
  `not_asked: [dependent[kid].ptc_files]`.
- `marketplace.dependent_files`: `own_money: true`, `ptc_files: true`, `ptc_magi: 2000000`. Expect proceeds with
  `dependent[kid].ptc_magi: 2000000`.

**Reviews made due.**
- dependent form: line-scoped transcription and render of 3 lines (1 new gate, `ptc_files` marker, `ptc_magi_counted`
  guards).
- The screen review of the new gate condition (`gate:dependent.own_money`).
- The question review of `dependent.own_money` (help).
- Class M for dependent: only if the review rules count a gate as a content change [I].

### A-F4. `asset.listed` taken apart (`tf-a-f4.patch`)

**Change.**
- `asset.listed_rec` is a new input: the entertainment or recreation item, with exception 1.
- `asset.listed_computer` is a new input, gated by `asset.listed_computer_if_early`. That gate is a `choose`:
  `asset.year` > 8 selects the item, and ≤ 8 selects `asset.no`.
- This is the same test as `asset.qip_early` for "placed before 2018" [C `asset.yaml:78-97`]. `asset.placed` is seq 3,
  before the item.
- `asset.listed` becomes `test any` of the two, so its readers are unchanged: `qbu_low_if_listed`, `listed_low`, lines
  25 to 26, `shown_when` [C `asset.yaml:778-784,1119,1178,1197,1215,2111`] and `sc.yaml` [C xint `sc.yaml:1751,1924`].
- Bank: `listed_rec` is seq 12 and `listed_computer` seq 13. The topic's later seqs shift by one, 13..32 to 14..33,
  because `seq` is integer and unique per order [C `schema/data.schema.json:63`; `interview/README.md:495`].

**Words.**
- `listed_rec`: 37, with the frame.
- `listed_computer`: 19. It is asked of pre-2018 property only.
- A typical new asset: 37 words, from 54 after trimA (60 before).

**Red team.**
- Exception 1, "used exclusively in a taxpayer's trade or business or at the taxpayer's regular business
  establishment" [C `i4562.cols.txt:50`], is kept for the recreation item.
- Exception 2, "used exclusively at a regular business establishment" [C :50], is kept for the computer item.
- The home sentence is on both [C :51].
- The 2025 i4562 no longer lists computers at all [C :49]. The pre-2018 rule is carried over from the existing line
  (relayed; IRC 280F is not archived).
- **Who could answer wrongly:**
  - A pre-2018 computer bought used: `placed` is the year the filer began using it, which is the right test.
  - A computer whose `placed` was entered wrong: a pre-existing risk.
- C8 (a phone used 40% for business is refused) is unchanged and pre-existing.

**Fixture plan** [C, script over every fixture]:
- `…asset[x].listed: false` becomes `…asset[x].listed_rec: false`. This is 109 cases, mechanical. The computer item
  defaults to false.
- `listed: true` with `placed` ≥ 2018 becomes `listed_rec: true`. This is 16 cases.
- `listed: true` with `placed` before 2018: one case, `asset.json` `stage14.asset.refuse_listed_low_past_gds`. Its
  `asset[pc]` was placed in 2015, so it becomes `listed_computer: true`, a possible person.
- Persona 13 (`asset[computer].listed: false`, placed 2025) is restated to `listed_rec: false` in the patch [C xint
  persona :88,95].
- Defaults: remove `asset.listed`. Add `asset.listed_rec` and `asset.listed_computer`, both false and closed. The
  defaults change is not in this patch. Removing a default needs the `defaults_guard` affected-cases report.

**Coverage rows (predicted).**
- `vehicles_equipment.camera_part_personal`: `listed_rec: true`, `pct: 80`. Expect proceeds,
  `asset[a].listed_rec: true`.
- `…computer_2016_home`: `placed: y2016`, `listed_computer: true`, `pct: 40`. Expect `refused: …asset[a].listed_low`.
- `…computer_2020`: `placed: y2020`. Expect proceeds, `not_asked: […asset[a].listed_computer]`.
- The entry path prefix (`person[taxpayer].sc[d].asset[a]`) follows the fixtures [C]; the rows' backgrounds are [I].

**Reviews made due.**
- asset form: transcription and render of 4 lines.
- The screen review of the gate `asset.year`.
- The question review of 2 new entries.
- Bank seq shift only for the others: no review.

### B-F1. `f1040.digital_assets` as a two-box tick screen (`tf-b-f1.patch`)

**Change.**
- `f1040.digital_got` and `f1040.digital_disposed` are new inputs.
- `f1040.digital_assets` keeps its id, `printed: Digital Assets`, label and cite. It becomes `test any` of the two, so
  the printed answer is the Or of the source's (a) and (b) [C `i1040gi.cols.txt:291`].
- `f1040.digital_conflict` reads it unchanged.
- `s1.digital_income_if_assets` now guards on `digital_got`: line 8v is received income only [C `i1040gi.cols.txt:8668`,
  "received ordinary income"].
- New group `digital` (heading 21 words; labels 9 and 7 words). `s1.digital_income` moves to seq 3 and
  `s1.digital_amount` to seq 4.

**Prompts.** 24 and 22 words, from 32. Help 29 and 28.

**Red team.**
- **Gift recipient (A10):** "No: … getting it as a gift or inheritance" in the got help. Source: (a) is "as a reward,
  award, or payment" [C :291], and "Don't report a gift or inheritance of digital assets on line 8v" [C :8668].
- **Airdrop recipient:** "new coins" in the label, and "airdrop" in the help and source. Relayed from wording-redteam A10
  and the current text; the archive lists mining, staking and hard fork [C :295].
- **NFT or stablecoin seller:** the heading says "crypto or another digital asset".
- **Moving between own wallets, holding, buying with dollars:** these are No [C :295].
- **Gifting coins away:** this is Yes, as "otherwise disposed of" [C :291], and as in the current wording.
- **A seller who also staked:** they tick both boxes, and 8v is asked. A seller who received nothing skips
  `s1.digital_income`. A value changes only if such a seller had 8v income, and 8v income is received [C :8668].

**Restated in the patch.**
- `fixtures/2025/defaults.json`: `digital_assets` is replaced by two closed defaults. The consistency rule "never No
  with a sale in boxes G to L" now names `digital_disposed`, since a digital sale is a disposal.
- coverage `other.yaml`: 3 rows become got yes, disposed no.
- coverage `sales.yaml`: 6 rows become got no, disposed yes, and drop `s1.digital_income`, which is no longer asked and
  would be a stale answer. `crypto_said_no` becomes both no.
- Personas: 17 is both yes; 18 is disposed only, dropping `s1.digital_income`.
- No expected end changed.

**Fixture plan (mechanical)** [C, script]:
- `"f1040.digital_assets": false` becomes both false. This is 935 occurrences, mostly classm, mutation and NY classm.
  Deleting the key also works, since both default to false.
- `true` becomes `"digital_got": true, "digital_disposed": true`. This is 39 cases (sales 20, sd 13, s1 4, f1040 1,
  person 1).
- This keeps every path, including the `s1.digital_income` answers they state. Hand cases may then be narrowed by
  situation: sales.json and sd.json are sellers and could be disposed only, but then they must drop `s1.digital_income`.
- **Year 2026:** `changes/2026/f1040.x1-digital.yaml` sets only `cite.locator` of `f1040.digital_assets`, which is
  unchanged [C xint]. The new sources say "In 2025" and move at adoption.

**Reviews made due.**
- f1040: transcription and render of 3 lines.
- s1: 1 line.
- The false-no review of `f1040.digital_*`. There is an existing false-no log for f1040 [C xint
  `reviews/2025/false_no/f1040.json` names digital_assets].
- The screen review of the new group.
- tick-groups and interview-coverage.
- draft-walk of personas 01 (every filer meets the screen), 17 and 18.

### A-F1. `gift.special` as two per-entry tick screens (`tf-a-f1.patch`)

**Change.**
- 11 new Bool inputs, one per item of the bank list [C bank:951-979], each with the old line's cite:
  `gift.vehicle`, `passthrough`, `ip`, `inventory`, `clothing_poor`, `unrelated_use`, `k1`, `partial`, `restricted`,
  `private_fdn` and `use_only`.
- `gift.special` becomes `test any` of the 11.
- The refusal on `gift.allowed`, `when: gift.special`, is untouched [C `gift.yaml:146-152`].
- Groups:
  - `gift_kind`, "Is this group any of these?": 6 boxes, seq 45-50.
  - `gift_how`, "Is any of these true of how this group was given?": 5 boxes, seq 51-55.
- `sa.line1` moves from seq 50 to 60, to clear the members' range [C `interview/README.md:583-584`].
- Labels are ≤ 12 words. There are 2 to 6 members per group, all per-entry and in one form.
- One help, on `vehicle`: Form 1098-C [C `i8283.cols.txt:76-79`, "A qualified vehicle is any motor vehicle …; a boat;
  or an airplane"].

**Words.**
- Labels and headings: about 63 + 59 = 122, from 141, in 2 steps instead of 1.
- The gain is mainly scanning: one line per box, each to be passed over at a glance.

**Red team.**
- **`vehicle`:** "of any kind, including a boat or a plane" keeps the old reach ("it is a vehicle"). Narrowing it to qualified
  vehicles would turn some refusals into computations, which is N9; not done.
- **`clothing_poor`:** "a … item over $500", per item, as the old prompt [C bank:979].
- **`private_fdn`:** the old wording, "not publicly traded stock", is kept. The source says "other than qualified
  appreciated stock" [C p526 via `gift.yaml:74` cite]. Publicly traded bonds given to a private foundation are a Yes,
  as before.
- **`unrelated_use`:** see the Summary owner note (Goodwill). I added no help that could widen the Yes.
- **`use_only`:** carried from the bank's 11th item, which the form label folds into "partial interests".
- **3.1(a):** one refusal line now stands behind two screens. A Yes on the first screen may show its refusal only after
  the second screen is answered, if the evaluator does not short-circuit `any` on an unanswered operand [I].
  - That costs one screen for refused filers only.
  - Splitting the refusal would change the refusal id in fixtures, so it was not done.

**Restated in the patch.**
- `defaults.json`: `gift.special` is replaced by 11 closed false defaults. They are inserted at the old spot; re-sort if
  the guard wants the list in order [I].
- coverage `home.yaml`: 2 rows replace `gift[g].special: false` with the 11 items false.

**Fixture plan** [C, script]:
- `special: false` is 307 cases. Delete the key; the defaults are false.
- `special: true` is 4 cases: `sa.json` 1, `classm.json` 1, `classm.deepseek.json` 2.
  - Restate each to the one item its situation names, read from its evidence note.
  - Otherwise use `gift.inventory: true`. Any single item is a possible person, and all reach the same refusal.

**Coverage rows (predicted).**
- `home.gift_clothing`: clothing worth $300 and all 11 items No. Expect proceeds, `gift[g].deduction: 30000`.
- `home.gift_car`: `vehicle: true`. Expect `refused: gift[g].special`.
  - The row must answer the 5 `gift_how` boxes if the refusal waits on them. If the evaluator short-circuits, those
    answers are stale.
  - Run it once both ways [I].

**Reviews made due.**
- gift form: transcription and render of 12 lines.
- Class M (gift).
- The screen review of the two new groups.
- The question review of 11 entries.
- tick-groups.
- draft-walk: no persona lists a noncash gift (persona 02 has `$gift: []` [C xint]), so add one or rely on the coverage rows.

### B-F2. NY use tax: plain parent plus DMV child (`tf-b-f2.patch`)

**Change.**
- `ny_it201.ask.bought_untaxed` is the new parent.
- `ny_it201.ask.use_tax_dmv_only` is the new child, gated by `use_tax_dmv_only_if_bought`.
- `ny_it201.use_tax_not_dmv` is a new helper.
- `ny_it201.ask.owes_use_tax` keeps its id as a derived line. It is a nested `choose`, per the gates design's "leaking
  conjunctions" [C `docs/2026-11-06_formal_gates_design.md:88-90`]: parent Yes selects `use_tax_not_dmv`, and No
  selects `no`.
- Line 59, `gate.use_tax_abode` and `gate.use_tax_st141` are untouched [C `ny_it201.yaml:2003,2021,2030-2044`].
- The `use_tax_st141` prompt gains "Leaving out a vehicle or boat taxed at the DMV" (37 words, a child).
  - Without it, a filer who registered a car and also bought small things online answers the child No.
  - They would then read "any one of those purchases cost $1,000 or more" as including the car, and be refused
    wrongly.

**Words.**
- Parent: 30 (whitespace). The 25 aim is exceeded only by the spouse phrase, and the owner rules the 25.
- Child: 21.

**Red team.**
- **Source:** "You may not use this line to report … any unpaid sales and use tax on motor vehicles, trailers, all-terrain
  vehicles, vessels, or snowmobiles. This tax is paid directly to the Department of Motor Vehicles (DMV). If you will
  not be registering or titling it at the DMV, you should remit the tax directly to the Tax Department …"
  [C `ny_it201i.cols.txt:445-446`].
- The child's help, "If you will not register it at the DMV, answer No", follows the source.
- Such a buyer then meets `st141`, where the unregistered vehicle counts toward $1,000. That leads to the ST-141
  refusal, which is right.
- "taxable in New York" stays, as trimB's guard against the exempt-goods buyer.
- The business leave-out stays in the parent's help (trimB text).

**Restated in the patch.**
- NY `defaults.json`: `owes_use_tax` is replaced by two closed defaults.
- coverage `ny.yaml`:
  - `ny.item_c_new_york_only` now expects `asks: ny_it201.ask.bought_untaxed`. This is the same situation; the
    question asked has a new id. The coordinator should accept this as an id rename, not a changed end.
  - `ny.use_tax_exact` and `ny.use_tax_large` now give parent Yes and child No.
  - Two new rows:
    - `ny.use_tax_vehicle_only`: proceeds, with `st141` and `abode_part_year` not asked.
    - `ny.use_tax_vehicle_and_small`: proceeds.
    - Both are unverified.

**Fixture plan** [C, script]:
- `"ny_it201.ask.owes_use_tax": true` becomes `bought_untaxed: true`. This is 20 cases (it201 6, mutation 12,
  classm 1, deepseek 1). `use_tax_dmv_only` defaults to false.
- `false` becomes `bought_untaxed: false`, or the key is deleted. This is 105 cases.
- Any fixture that **expects** `owes_use_tax` keeps it, because the line still exists.

**Reviews made due.**
- ny_it201: transcription and render of 4 new lines and 1 changed line.
- Class M (NY).
- The screen review of the gate `ny_it201.ask.bought_untaxed`.
- NY question review of 3 entries.
- interview-coverage (ny profile).
- draft-walk of the NY personas, which every NY filer passes.

## 3. Designs not patched

### A-F2. `sa.line1` (325 words; rank 3; recommend its own Opus lane)

**Design.** Keep `sa.line1` as a derived `sum`, so `sa.line1_if_medical` and every fixture's expected Schedule A
values stand. Its parts:
- **`sa.med_costs`**, the core amount (about 45 words): "How much did you (or, on a joint return, your spouse) pay
  in 2025 for medical and dental care and health insurance for yourselves and your dependents, after what insurance
  paid back? Leave out costs paid from an HSA and insurance taken from pay before tax."
- **Marketplace premiums: computed, not asked.** The term is "total premiums … minus the premium tax credit allowed on
  Form 8962, line 24, and minus any excess advance payments you do not have to repay (line 27 minus line 29)"
  [C `sa.yaml` source]. It is computable from Form 1095-A column A and `f8962` lines 24, 27 and 29. Schedule A does
  not feed MAGI, so this is not circular [I].
  - The core prompt then says "Leave out Marketplace premiums; they are counted from your Form 1095-A".
  - This removes the hardest rule for the filer.
  - Check one thing first: the 1095-A column A total equals the premiums of people on the return. `f8962.shared_policy`
    refuses the shared case [C coverage `marketplace.yaml`, `plain` set].
- **A return-level tick screen `med_rare`, "Did any of your medical costs include these?":**
  - costs of someone you support who is not your dependent;
  - long-term care insurance premiums (amount child with the age table, or computed from birth years where the person
    is on the return);
  - care that was part nursing, part housework;
  - meals or lodging on a medical trip;
  - premiums paid from a public safety officer's retirement plan;
  - self-employed health insurance already deducted. This one could be subtracted automatically from Schedule 1
    line 17 [I].
  - Each Yes opens one amount (add or leave out), and `sa.line1` adds or subtracts it.
- The earlier-year reimbursement sentence stays in the core help (it is about what not to subtract).
- **Value risk.** Each child's amount must equal the part of the old single amount that the rule governed. Restated
  fixtures put the whole old value in `sa.med_costs` and zero elsewhere, which gives the same sum.
- **Fixtures.** About 650 cases state `sa.line1` (classm, mutation, NY classm, hand files) [C, counts]. All are
  mechanical.
- **Cost.**
  - The Marketplace computation is a new formula, which needs owner sign-off and the full review set for sa.
  - The other children are routine.
- Not done here: too large to complete and check in this lane (protocol 5.8).

### A-F5. `rprop.basis` (rank 8; not recommended as proposed)

- **Design.** `rprop.converted` (Bool, per building): "Did you live in it, or use it yourself, before you first rented
  it?"
  - Two amount children, each with an `_if_` gate:
    - `basis_cost`: "Your share of what it cost, not counting the land."
    - `basis_converted`: "the smaller of what the building was worth when you began renting it and what you paid plus
      improvements, both without the land".
  - `rprop.basis` becomes a derived `choose` on `converted`. The 18 `rental.json` and classm fixtures restate to
    `basis_cost` with `converted: false`.
- **Why not.** Every landlord gains a step (N12) to save about 11 words on a per-entry question already within 40.
- No earlier answer settles "used it yourself before renting":
  - `rental.days_personal` covers only 2025.
  - The `rprop.disposed` help covers the reverse case.
- Revisit only if the owner sets the per-entry limit at 25.

### A-F6. `rental.days_personal` (rank 7; blocked by the Count rule)

- `days_personal` is a Count. The gates design says that a `choose` takes no Count alternatives, and that Count inputs
  are not marked [C `docs/2026-11-06_formal_gates_design.md:84-87`].
  - So a main-home child cannot carry its own Count variant into a derived `days_personal`.
- **Design if the engine allows Count arithmetic:**
  - `rental.main_home` (Bool, child of `personal_any`): "Was it your main home at any time in 2025?"
  - Only after a Yes, a Count `rental.main_home_days_left_out`, with the 12-month rule and its sale exception.
  - `days_personal` loses that clause (about 25 words).
  - Personal days = `days_personal` minus the left-out days. This needs a Count subtraction that I did not find among
    the ops in use [C op census of `forms/2025`: no Count subtract seen; I].
- Owner or engine decision first.

### A-F7. `spouse_died_this_year` before `married_dec31` (rank 10; the swap does not achieve the aim)

- Both questions are gated on `household.marriage_possible` [C `household.yaml:621-660, 1426-1450`].
- `spouse_died_this_year` is read directly only where status is single or HOH (`widowed_this_year`) and through
  `no_spouse_died` [C :1452-1500, 1670-1685].
- **For single or HOH filers,** a seq swap would ask it first. The widowed filer is then refused there (help: "a Yes ends
  the interview here") and never reaches `married_dec31`.
- **For joint filers,** `married_dec31` is read for the status conflict, and `spouse_died` is reached through it, so it is
  still asked after [I, from the line structure; not walked].
  - A widow filing jointly who answers `married_dec31` Yes (she still feels married) changes the lines that read
    "unmarried at the end of 2025" (for example the i8889 rule cited on the line [C :652]).
  - So the help's widowed sentence must stay.
- Dropping it would need `married_dec31` gated behind `spouse_died` No. That means a new gate line, and every reader of
  `married_dec31` moved to it: about 60 fixture files and 15 coverage files name `married_dec31` [C, file list].
- Not recommended. Keep trimA's 60-word help, which is an owner overrun decision.

### B-F3. NY `est_any` as three inputs (rank 9; not recommended)

- **Design.** Group `ny_paid`, heading "Besides tax taken from pay, did you (or, on a joint return, your spouse) pay New
  York tax for 2025 in any of these ways?" (about 25 words). Boxes:
  - "Estimated payments, or a payment with a request for more time"
  - "A 2024 New York refund applied to 2025"
  - "Estimated tax passed to you by an estate or trust"
- `ny_it201.ask.est_any` becomes the derived Or, so `line75` is unchanged [C `ny_it201.yaml:2423`]. The 125
  `est_any` fixture refs are restated to the first box.
- **Why not.** Every NY filer would read about 45 words instead of 32 (trimB) to protect a rare trust beneficiary, who is
  also covered by the `line75_amount` help [C NY bank:307-308]. Keep trimB's version unless the owner rates the trust
  case higher.

### B-F4. NY 529 exceptions child (rank 11; not recommended)

- **Design.** A child after a No to `529_nonqualified`: "Was any of it for career training or a student loan?" A Yes
  leads to a refusing-free narrow question on the July 4 date, the eligible school and the sibling loan. The old id
  becomes the Or.
- **Why not.** The typical withdrawer (college only) answers the parent No and would then meet a guard asked after a No,
  which N4 names as a violation. The help is 44 words, 4 over "about 40" (trimB).
- Recommend the owner accept the overrun.

## 4. What to run on the landing branch (none was run here)

1. Apply in rank order: A-F3, A-F4, B-F1, A-F1, B-F2.
   - Apply the round-4 trims named in the base table first.
   - Each patch was dry-run only against its own base plus trims.
2. Restate the fixtures by the plans above, mechanically and inputs only. Run `tools/defaults_guard.mjs` for the
   removed defaults (`asset.listed` comes with A-F4's fixture step).
3. Build (wording, gates, schema, tick-groups). Then test-fixtures, interview-coverage (`full` and `ny`), the self-tests
   and draft-walk of the personas named per unit.
4. Reviews, line-scoped as listed per unit (CLAUDE.md, inference cost).

**Not verified anywhere:**
- That the build accepts each change (gate checks, tick rules).
- That the restated and new coverage rows end as predicted.
- Whether `any` short-circuits on an unanswered operand (A-F1, A-F4).
- Every "who could answer wrongly" judgment [I].
