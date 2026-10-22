# Handoff: Stage 13 (married filing jointly) done

Read `HANDOFF.md` first, then `TASKS.md`, then this file. `handoffs/HANDOFF-STAGE-12.md`
describes the stage before. `PROJECT_INDEX.md` is current; `BUG_INVENTORY.md`
has 49 entries.

## Scope (owner-confirmed)

Married filing jointly, with every per-person rule in scope re-derived from the
archived text for two people; married filing separately stays refused (`s3.mfs`,
i1040gi p. 14) and is now rung 9 of the coverage ladder. Ownership is a record per
person (design A); the Form 8889 spouse rule is supported, with an equal or an
agreed allocation (owner).

## What changed

- **Per-person records** (`forms/2025/person.yaml`): `person.role` (taxpayer or
  spouse), the facts that belong to one person (born before January 2, 1961; blind;
  SSN or ITIN issued; ITIN applied for; SSN valid for employment; EIC birth dates;
  educator status and expenses; the Schedule 1-A decedent question), and the
  collections within a person: `w2`, `tipjob`, `otjob`, and `f8889` (one per person,
  i8889 p. 4). The former inputs (`sa.age65`, `household.taxpayer_work_ssn`, ...)
  remain as lines meaning the taxpayer's own answer.
- **Roster** (`household.roster_ok`): one entry for you and, only on a joint return,
  one for your spouse; anything else is refused at Form 1040 line 1a. The full
  interview asks `$person` and each entry's role; per-person prompts address "this
  person".
- **Joint rules**, each from the archived text:
  - identification: EIC needs SSNs valid for employment for both spouses (p. 40);
    the child tax credit for one, with an issued SSN or ITIN for the other (p. 17);
    the credit for other dependents an SSN or ITIN, or an ITIN application, for
    both (p. 19, Step 5);
  - EIC Step 4: you or your spouse 25 to 64 (`eic.age_range`);
  - standard deduction boxes for both spouses (line 12d);
  - educator expenses: $300 per person (Schedule 1 line 11 is the sum);
  - Schedule 1-A: tips and overtime count only for a person with a valid SSN, the
    cap per return; Parts II and III need the taxpayer's SSN unless filing jointly
    and a receiving spouse's SSN on a joint return; seniors per person, line 36b
    computed, a decedent gate for each spouse;
  - Form 8889: line 3 without the additional contribution amount once married with
    family coverage (p. 5 Note); line 6 by Steps 1 to 4 (p. 7) with cross-spouse
    checks (family months counted alike, the same allocation method, no more than
    the Step 1 limit, an agreed allocation only between equal Step 1 limits);
    line 7 by the Additional Contribution Amount Worksheet;
  - a dependent younger than you or your spouse (p. 17; Pub. 501 p. 13).
- **Engine**: `eval`, `evaluateAll`, mutation and the coverage report evaluate every
  line of every confirmed entry (BUG-0044); `evaluate` takes an entry line as a
  target.
- **Sources**: Pub. 501 (2025) archived through `fetch_sources.py`.

## Evidence

- `fixtures/2025/stage13.json`: 44 cases (42 joint returns and two married-filing-separately Schedule A cases), predicted by hand before recording
  (the derivation is in each evidence note), all matching. Builder:
  `/tmp/s13/build_stage13.py` with `/tmp/s13/compare13.py` (if /tmp is gone, edit the
  JSON directly).
- The 43 earlier married-filing-jointly fixtures gained a spouse with neutral
  facts; six expectations that encoded the old married refusal were changed, each
  explained in its evidence note (`ss.mfj`, `ss.mfs`, `stage11.refuse.hsa_married`,
  `stage4.refuse.married`, `stage4.refuse.standard.spouse_extra`, `classm.s1a.8`);
  `stage12.refuse.spouse_senior` became `stage12.single.spouse_boxes_answer`.
- Engine differential: 400 generated joint returns added to the 1,000 (case ids of
  the 1,000 unchanged): 1,400 cases, 0 unexplained.
- Lean and TypeScript agree on every case; the compare harness gives its generated
  joint cases a spouse.
- Mutation: adjusted 96.9%, no new unexplained survivor; four reasoned equivalences
  (`hsaSplitSum` and two Form 8889 last-month entries in `engine/src/mutate.ts`).
- Reviews (paid `claude -p`, fixed prompt): transcription and render of the 13
  changed forms (about $15), all ruled; three render findings were real
  (BUG-0047 to BUG-0049) and are fixed. Class M of the 11 changed documents (about $11.50; the job builder now draws a spouse): `s1a` 43, `s1` 24, `f1040` 196, `s3`, `tipjob` agree on every value; 63 disagreements in `f8889`, `otjob`, `eic`, `person`, `sa`, `dependent` ruled, almost all helpers of branches not taken; one was real (the Form 8889 family amount for a married filer aged 55, fixed, no printed line changed).
- Coverage estimate: 47.8% of returns (range 38.1% to 59.2%), from 33.9%; next
  rung self-employment (to about 58%).

## Open for the owner (TASKS.md T-038)

- `amb.2025.hsa_line7_months`: every eligible month counts on the line 7 worksheet
  (the second transcription read family months only).
- An agreed HSA allocation between spouses whose Step 1 limits differ is refused.
- On a joint return, Parts II and III of Schedule 1-A apply only if a spouse who
  received the tips or overtime has a valid SSN; `classm.s1a.8` changed.
- The filer's and spouse's SSN question uses the child tax credit's wording for the
  EIC as well (the question of `amb.2025.eic_valid_ssn`).
- T-037: the EIC age test for a person who died in 2025 (Pub. 596) is not screened.

## Facts a fresh session needs

- A person's input is keyed `person[taxpayer].x` or `person[spouse].x`; an entry's
  line `person[spouse].f8889[hsa].line6`. A return's roster is `$person`.
- The full interview no longer presets the roster; the stage profiles (Stage 2,
  sales, Stage 4) still preset `["taxpayer"]`.
- A refusal's condition is evaluated whenever its line is; keep a refusal on a line
  reached only in the case it is for (BUG-0046).
- `choose` selects money only, never a count; months chosen under the last-month rule
  are carried as money amounts (`f8889.family_year`, `self_year`, `line7_year`).
- The class M job builder and the property tests draw a random spouse on joint
  returns (`engine/src/generate.ts`).

## Next: Stage 14, self-employment (readback confirmed by the owner; not started)

The owner confirmed the intent readback and these choices; nothing has been built,
fetched or archived for it yet (TASKS.md T-039).

- **Slice:** Schedule C (one or more businesses per person), Schedule SE, Schedule 1
  lines 3 and 15, Schedule 2 line 4, and Form 8995 below the threshold; Form 8995-A,
  specified service trades or businesses and the W-2 wage and property limits stay
  refused. Earned-income readers (EIC, the refundable child tax credit, Form 8959's
  self-employment part) see self-employment earnings; each spouse has their own
  Schedule C and SE.
- **Schedule C depth (d):** the Part II expense lines, Part III cost of goods sold, the
  simplified home-office method, the standard mileage rate, and depreciation on
  Form 4562.
- **Adjustments:** self-employed health insurance (Schedule 1 line 17) and SEP/SIMPLE
  contributions (line 16) come in too.
- **Measure first:** the owner approved fetching and archiving the IRS
  sole-proprietorship statistics through `fetch_sources.py` to measure which Schedule C
  features are common, before the slice is fixed in detail.
- Still owed before building: the source archive (Schedule C, SE, Forms 4562, 8829 if
  needed, 8995 instructions are archived) and a premise check against it.
