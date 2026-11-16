# Lane D6-personas: new personas for the seven new areas (round 5)

Model claude-opus-5-5, judgment class, tax year 2025, jurisdiction us (no New York persona, see "Not done").
I made no paid calls, ran no builds and ran no engine. The patch was written from copies and checked with
`git apply --check` against a copy of the base, `P/scratch/b-chain/work/interview`. No errors were printed.

## Summary

- **Patch:** `P/patches/v4/personas.patch` adds nine new files under `interview/2025/personas/`, numbered 23 to 31.
  Numbers 23 and up were free: xint has 01 to 22 (13 is used twice) and ny01 to ny05 (checked with `ls`).
- **The areas were not all empty.** The bank already holds:
  - 14: Form 1116, no carryover.
  - 15: married filing separately (MFS), not in a community property state, spouse takes the standard deduction.
  - 16: MFS, refused because the filer lived in a community property state.
  - 17: crypto, staking only.
  - 19 and 11: a rental with no personal use, and a refused rental with short stays.
  - 20: a dependent with no unearned income.
- **So the new personas split into two groups:**
  - Four fill true gaps: per diem (23), household pay (24), a dependent with unearned income (27), and the kiddie-tax
    refusal (28).
  - Five complement existing personas: the spouse's state refuses (25), the spouse itemizes (26), a foreign tax
    carryover (29), an airdrop and its sale (30), and a rental with personal use (31).
- **Answer ids:** every id names an input in the base bank. A script read the bank and the personas; the checked forms
  are listed below.
- **Values:** the gates that open each question were read in the base forms. The predicted values were worked out by
  hand from the forms and are written as YAML comments at the head of each file. The persona format does not allow a
  values key: `draft-walk.ts:451` allows only name, who, end, profile, extends and answers.
- **Not run.** Because of the rule against runs tonight, no persona was walked. Each may report "opened and
  unanswered" or "stale" problems on its first `draft-walk`. Fix the answers, never the expected end.

## How to verify (when runs are allowed)

1. `node engine/dist/main.js draft-walk --only <name>` for each of the nine. Expect zero problems and the stated end.
2. Check the values against each file's comment block with the CLI on the walk's answer log. The fixture or row form is
   for the build lane. The values are hand predictions (protocol 5.1), not evidence.
3. No review is made due: persona files are not form content.

## The personas

How to read the "Checked" and "Doubt" lines: [V] means I checked it against a file tonight; [I] means it is inferred.

### 23_ltc_per_diem_mother (extends 01): Form 8853 per diem

**Story.** A single person, 56, with a W-2 of $52,000. She owns a long-term care policy on her mother, which paid her
$450 a day for 200 days. The nursing home cost $76,000, and Medicare paid $8,000 of it.

**Answers:**
- `s1.ltc_payout` Yes, `$f8853c` [mom], periodic Yes.
- line17 90,000, nonqualified No, line19 0, others_paid No, rate_changed No.
- days 200, line22 76,000, line24 8,000, contract_before_ltc_date No.

**Predicted values:**
- Line 21 is $84,000 ($420 × 200). Line 23 is $84,000. Line 25 is $76,000. Line 26 is **$14,000**, which goes to
  Schedule 1 line 8e.
- AGI $66,000; taxable income $50,250; tax $5,975 (Tax Table, give or take $1).

**Checked.** [V]
- Gates: `f8853c.yaml:37-475`.
- The question `contract_before_ltc_date` opens only because line 24 is more than zero (`f8853c.yaml:443-476`).
- The answer sequence matches coverage row `s1o.ltc_per_diem` (`coverage/s1_other.yaml:207-220`).

**Doubt.** [I] Line 24 includes Medicare's payment. That is the open owner decision 8 (`amb.2025.f8853c_line24_public`).
If Medicare is not counted, line 24 is 0, line 25 is $84,000 and line 26 is **$6,000**. This persona is chosen to make
that decision visible.

### 24_household_pay_babysitter (extends 01): pay not on a W-2

**Story.** The filer of 01, who also babysat for two families, paid $2,300 and $2,600. Neither family gave a W-2.

**Answers:**
- `scope.pay_no_w2` Yes, `scope.household_pay` Yes.
- The other four `pay_kinds` boxes No.
- `person[taxpayer].household_wages` 4,900.

**Predicted values:**
- Line 1b $4,900; no Schedule SE, Form 4137 or Form 8919.
- AGI $56,900; taxable income $41,150; tax $4,703 (give or take $1).

**Checked.** [V] This repairs the four "opened and unanswered" problems that scratch persona 90 had (walk transcript
`xint-artifacts/walks-after/90_scratch_household_pay.md:9-12`). It follows coverage row `pay.household_wages`.

### 25_refused_mfs_spouse_california: MFS, refused by the spouse's state

**Story.** A married person in New York who files separately. Her husband's permanent home is California.

**Answers:**
- married_dec31 Yes, community_property No, spouse_cp_domicile Yes.
- End: refused at `household.mfs_community_property`.

**Checked.** [V]
- Coverage row `mfs.spouse_cp_domicile` (`coverage/mfs.yaml:97-108`).
- The gate in `household.yaml:680-730`.

Persona 16 refuses on the filer's own state; this one refuses on the spouse's.

### 26_mfs_spouse_itemizes: MFS, not community property, spouse itemizes

**Story.** A married man in Pennsylvania who lives with his wife and has a W-2 of $70,000. She itemizes, so his
standard deduction is $0. He is a renter, paid $2,849 of state and local income tax, and gave $1,200 in cash.

**Predicted values:**
- Schedule A line 5a/5d/5e $2,849; line 11 $1,200; line 17 $4,049.
- Taxable income $65,951; tax $9,429 (MFS Tax Table, give or take $1); owed $2,429.

**Checked.** [V]
- `sa.spouse_extra` is not asked when the spouse itemizes (`sa.yaml:198-224`), so the persona does not answer it. Its
  answer would be stale.
- `sa.line5b` and `sa.property_tax_other_any` are not asked of a renter (`sa.yaml:680-745`).

**Doubt.** [I] Some Schedule A question I did not trace may open, such as a sales-tax choice. The first walk will show
it.

### 27_dependent_student_interest (extends 20): dependent with unearned income

**Story.** Persona 20 (a dependent, 19, W-2 of $6,000) plus $2,100 of interest on a CD.

**Predicted values:**
- `scope.unearned_2700` stays No, so no Form 8615.
- Standard deduction $6,450 ($6,000 + $450).
- AGI $8,100; taxable income $1,650; tax $166; owed $46.

**Checked.** [V] `sb.nominee` and `sb.bonds_any` open on any interest (`sb.yaml:10-25, 506-540`). The interest
questions match persona 04's walk.

### 28_refused_dependent_kiddie_tax: dependent, refused at Form 8615

**Story.** A full-time student, 20, supported by her parents, with $4,000 of dividends.

**Answers:**
- `scope.unearned_2700` Yes, `scope.f8615` Yes.
- End: refused at `scope.other_line16`.

**Checked.** [V]
- Coverage row `scope.f8615` (`coverage/scope.yaml:507-515`).
- The question order in persona 20's walk: `scope.unearned_2700` is question 12.

The persona answers nothing after the refusal, because later answers would be stale. It is written in full, not as
`extends`, for the same reason.

### 29_foreign_tax_carryover (extends 14): Form 1116 with a carryover

**Story.** The filer of 14, with a W-2 of $90,000, plus a fund that paid $6,000 of dividends ($5,000 qualified) and
$360 of foreign tax on $4,000 of foreign income. A 2024 Form 1116 carried $100 into 2025.

**Predicted values:**
- Form 1116: line 14 $460; line 18 $80,250; line 20 $12,225; line 21 about $510; line 35 **$460**.
- Tax $12,225: $11,475 on $75,250, plus 15% of $5,000.
- Owed $765.

**Checked.** [V]
- The answers match coverage row `ftc1116` with a carryover (xint `coverage/ftc1116.yaml:520-562`).
- The line formulas: `f1116.yaml`, as dumped tonight.
- The adjustment-exception parameters: `params/2025.yaml:1911-1927`.

**Doubt.** [I]
- The rounding of line 3g and line 21 in cents. It changes nothing here, because the limit of about $510 exceeds the
  $460 to be credited.
- I set the foreign income so that the limit covers the tax. Otherwise `f1116sb.prior_year` would open. That excess
  path still has no persona.

### 30_crypto_staking_airdrop (extends 01): staking and an airdrop

**Story.** $300 of staking rewards and a $500 airdrop. The airdropped tokens were sold for $800, on a Form 1099-DA
without basis (box H). The basis is $500, their value when received.

**Predicted values:**
- Schedule 1 line 8v $800; short-term gain $300.
- AGI $53,100; taxable income $37,350; tax $4,247.

**Checked.** [V] The answers follow persona 17's pattern for one sale.

### 31_rental_cabin_personal_use (extends 01): rental with personal use

**Story.** A lake cabin bought in July 2021 (building basis $200,000), rented by the month for 180 days for $19,500.
The owner stayed 14 days herself. Costs: mortgage interest $6,000, tax $3,000, insurance $1,200, utilities $1,800.

**Predicted values:**
- The cabin is not used as a home: 14 days is not more than the larger of 14 days or 10% of the rented days.
- Expenses are divided by 180/194 (0.927835). Depreciation is $7,272 × ratio = $6,747.22.
- Line 20 $17,881.24; line 21 **$1,618.76**.
- Tax $4,307.

**Checked.** [V]
- The formulas: `rental.yaml` (base) lines `rental.home`, `rental.ws51` and `rental.div*`.
- `short_stays` asks whether stays averaged 30 days or less. An average of exactly 30 days is Yes, which opens
  `stay7`, answered No. This deliberately walks the No path of the refusing question.
- The rprop labels m7 and y2021 (`questions.yaml:7355, 7369`).

**Doubt.** [I] The model also divides costs that serve only the rental, such as advertising and commissions
(`rental.div5`, `div8`). I recall that Pub. 527 says such costs need not be divided, but I did not check that against
the archived source. The persona avoids such costs. **A lead to check, not a finding.**

## Not done, and why

- **No New York persona.** The brief named jurisdiction us and ny, but a New York persona needs the `ny` profile and
  the New York answers. I did not trace those tonight. Persona 25 lives in New York but walks only the federal
  questions.
- **The Form 1116 excess path, which carries back to 2024, has no persona.**
- **Process:**
  - The `agent_runs.jsonl` rows could not be written (read-only rule). The coordinator should record this lane and its
    one fork, both claude-opus-5-5, judgment, 2025, us.
  - Early in the run I started a `find /` while the release check was running. I stopped it after about 2 minutes.
