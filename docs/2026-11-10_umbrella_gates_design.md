# Umbrella gates: design

Status: proposal for the owner (phase 3, the interview pass, lane E). Nothing here is landed: forms, interview and
fixtures are unchanged. Builds on the formal gates design (`docs/2026-11-06_formal_gates_design.md`, approved
2026-11-06) and on lane A's measurement (`reports/2025/interview_length.md`).

## Why

Lane A measured the federal interview on 253 synthetic returns and found that question order cannot shorten it: today's
order is at, or within 3 questions of, the floor (the inputs the complete return reads) on every complete return. Re-run
in this lane on the merged tree (without `--write`): 253 returns measured, 161 complete, 0 problems. The length comes from breadth:
77 to 96% of answers are no, 0 or none, on questions the evaluation reads, and 60 templates are asked of every complete
full-profile return. The owner approved (2026-11-10) designing **umbrella gates**: one existence question whose no makes
a group of rare-situation questions unreachable, in the formal model, under the gates design's conventions.

## What qualifies as an umbrella

The gates design admits two kinds of new gate input: **A**, an applicability condition the instructions state, and
**B**, an existence fact defined as exactly the situations in which a line it gates could be non-zero. An umbrella is a
B gate (or an A gate where a source states the condition) over several inputs. This design adds three tests, from the
brief and from the false-no patterns (`tools/transcription/false_no_review.py`, PATTERNS 1 to 8):

1. **Source terms.** The question is stated in the source's own terms: a printed line list (Schedule 1 lines 8a to
   8z), a printed part heading (Schedule B Part III, "Foreign Accounts and Trusts"), a form's own section (Form 1040
   "Payments"; Schedule 3 Part II), or a form's title (Form 5695, Form 2441). Its help enumerates every situation a
   gated line covers, in the instructions' words.
2. **One concept the filer recognizes.** A no must be one judgment ("nothing foreign at all"), not several judgments
   disguised as one. A grouping of unrelated rows ("tips, overtime or a car loan") fails this test: the filer must
   still weigh each row, so the umbrella saves a click, not a judgment, and invites a skim (pattern 6).
3. **No hierarchy leak (pattern 5).** No gated line may have a source of its amount outside the umbrella's
   definition. Where an input serves two concepts (alimony gates both received, line 2a, and paid, line 19a), it
   stays out of an umbrella that names only one.

A cost test is added for the recommendation, not for qualification: an umbrella whose gated inputs are read across
many forms makes every one of those forms change (each reader must read the gate line), and each changed form is due
for its reviews.

## Measurement

`node engine/dist/main.js interview-length --what-if --write` (new in this lane; `engine/src/umbrella-what-if.ts`)
puts each candidate into a copy of the built data in memory, exactly as the conventions would: a new Bool input; a gate
line `<input>_if_<umbrella>` (a `choose` on the umbrella with a zero or false parameter as else) read in place of each
gated input by every former reader, refusal gates (`refuses: when`) and `shown_when` included; for a roster, each line
that reads its collection put under the same `choose` (the Count-input pattern of the gates design). The umbrella's
question is placed in the bank at the earliest order of the inputs it covers. Every return of lane A's report is walked
in today's order as built and with the umbrella, and the umbrella is answered yes exactly when the walk as built
answered one of its inputs with something other than false, 0 or none: the truthful answer for that return. Both
walks must reach the same status, and the same values on a complete return or the same refusals on a refused one
(refusals compared with the gate line's name put back to the screen's; a refused return's other targets can stay
unknown, and an answered umbrella settles more of them). They do on all 253 returns in all 13 scenarios (run of
2026-11-10, 0 problems). An umbrella is answered only on a return whose walk as built asked one of its inputs. The self-test (in `check-all`) checks one umbrella on `stage5.return.owed`: it
replaces the questions it covers with one, keeps the values, and a no given while a line 8 amount is non-zero changes
the values.

The returns are synthetic and answer nearly every rare question no, so the measured saving is close to the most an
umbrella saves. The **expected saving per real filer** weighs it by the share answering yes in
`interview/2025/gate_frequencies.yaml`: with *n* questions covered and share *p* yes, a no saves *n* − 1 and a yes
costs 1, so the expectation is (1 − *p*)(*n* − 1) − *p* = (1 − *p*)*n* − 1. Shares are those of the situations
named; where an umbrella spans several, the share is their sum (an upper bound; overlaps make it smaller). These are
estimates, labelled as such.

## 1. Candidate umbrellas

Twelve candidates were measured: every group among lane A's 60 always-asked templates that a source structure
suggests, plus two variants. *n* is the questions the umbrella covers that a return answering no is asked today (one
person); *p* the summed share yes; *Measured* the mean saving on the 12 complete full-profile returns (Stage 5 and
generated; `reports/2025/umbrella_savings.md`); *Expected* (1 − *p*)*n* − 1 per real filer (estimate).

| Umbrella (new Bool) | Covers | *n* | *p* | Measured | Expected | Forms touched | Verdict |
|---|---|---|---|---|---|---|---|
| **U1 `s1.line8_any`**: any income for Schedule 1 line 8 | `s1.gambling_winnings` (8b), `s1.cod_any` (8c), `s1.line8g`, `8h`, `8i`, `8j`, `8r`, `s1.line8_other` (8a, 8d–8f, 8k–8q, 8s–8v), `$oi8z` (8z) | 9 | 0.08 | 8.0 | 7.3 | s1 | **recommend** |
| U1x `s1.part1_other_any`: U1 and unemployment (line 7) | U1 and `s1.uc_paid` | 10 | 0.11 | 9.0 | 7.9 | s1 | alternative |
| **U2 `sb.foreign_any`**: any foreign account, foreign financial asset, foreign trust or foreign corporation | `sb.fbar_required`, `sb.form8938`, `sb.line8`, `sb.form5471` | 4 | 0.03 | 3.0 | 2.9 | sb | **recommend** |
| U2w `sb.foreign_wide_any`: U2 and excluded foreign or territory income | U2 and `sa.excluded_income` | 5 | 0.03 | 4.0 | 3.8 | 11 (sa's 23 readers) | alternative |
| **U3 `f1040.other_payments_any`**: tax withheld other than on a W-2, or any other payment or refundable credit | `f1040.line25b`, `f1040.line25c_other`, `f1040.line26`, `s3.line10`, `s3.line12`, `s3.line14` | 6 | 0.29 | 2.0 | 3.2 | f1040, s3 | **recommend** |
| U3w `f1040.withholding_other_any` (survey B-4) | `f1040.line25b`, `f1040.line25c_other` | 2 | 0.21 | 1.0 | 0.6 | f1040 | alternative |
| **U4 `f5695.any`**: residential energy credits | `f5695.part1_any`, `f5695.part2_any` | 2 | 0.03 | 1.0 | 1.0 | f5695, s3 | **recommend** |
| **U5 `sd.carryovers_any`**: a carryover into 2025 shown on an earlier year's return | `sd.carryover`, `s179.line10`, `qbi.carryforward` | 3 | 0.06 | 2.0 | 1.8 | sd, clcw, f8960, s179, sc, qbi, f8995 | **recommend, last** |
| U6 `f2441.any`: child and dependent care expenses or benefits | `f2441.care`, `f2441.benefits` | 2 | 0.06 | 1.0 | 0.9 | f2441, s3, f1040, dependent, ny_it201 | optional |
| U7 `s2.other_taxes_any`: merged additional-tax screens | `s2.amt`, `s2.other`, `scope.other_line16`, `person.x_other`, `f8959.unsupported` | 5 | 0.02 | 4.0 | 3.9 | 10 | not recommended |
| U8 `s1.adjustments_any`: educator expenses or student loan interest | `person.educator_expenses`, `sli.interest` | 2 | 0.10 | 0.8 | 0.8 | s1, person, sli | not recommended |
| U9 `s1a.any`: tips, overtime or car loan interest | `s1a.tips`, `s1a.overtime`, `s1a.carloan` | 3 | 0.20 | 2.0 | 1.4 | s1a | not recommended |

**Recommended together (U1 to U5): measured 111.2 → 95.2 questions on the complete full-profile returns
(16.0 saved, 14%; 19 on the minimal return that answers every gate no), and an expected saving of about 16 per real filer (estimate: the sum of the
expected column, 7.3 + 2.9 + 3.2 + 1.0 + 1.8).** Every measured number above is exact for these synthetic returns; the
expected column is an estimate resting on the frequency file's shares, several of them recorded judgments.

Not candidates, and why:
- Templates with a share yes above about 15% (`household.married`, `person.age65`, `refund.received`, `ssb.benefits`,
  `$dependent`, `$retirement`, `$interest`, Schedule A amounts, `s1a.overtime`): a no saves little and a yes costs a
  question for many filers.
- Single, unrelated rare rows (`person.blind`, `person.under16`, `household.spouse_died_2025`, `sa.dependent`,
  `person.rrta`, `f8863.paid`, `qbi.unsupported`, `sa.unsupported`, `scope.credits`, `scope.other_income`,
  `scope.schedule1`): no source concept groups them (test 2); they stay on the rare-situation grids as rows, which the
  gates design already decided. Possible C gates (no new question) are noted in section 6, not designed here.

### U1 Schedule 1 line 8 income (survey B-2)

- **Source.** Schedule 1 (2025) line 8, "Other income", lines 8a to 8z, and i1040gi pp. 91–92. The printed lines 8a to
  8v are a closed list; 8z is the residual ("any taxable income not reported elsewhere"). The survey's concern was that
  the i1040gi p. 3 table calls itself "a general guide"; the umbrella does not rest on that table but on the line list.
- **Definition.** Yes when any of lines 8a to 8z could be non-zero for you or your spouse, including the subtractions
  (8a NOL, 8d Form 2555 exclusion, 8s Medicaid waiver payments). The help lists every printed line in the
  instructions' words, then 8z's examples (recoveries of amounts deducted earlier, fractional-gift recapture, RTAA
  payments, kickbacks, and "anything else taxable that no other question asked about").
- **Why a no is right in every case covered.** The nine inputs are exactly lines 8a to 8z (`s1.line8_other` is today's
  complement for 8a, 8d–8f, 8k–8q, 8s–8v). A truthful no means every line 8 entry is zero, so each gate line's zero
  else is the line's true value. Gambling losses (Schedule A line 16) are read through `s1.has_gambling` and are
  limited to winnings, so a no hiding them is right. `s1.jury_to_employer` stays behind its existing gate on 8h, now
  reading `s1.line8h_if_line8`.
- **False-no risk (highest of the set).** A wrong no silently drops up to nine lines. Patterns: 8 (amounts not
  perceived as income: cancelled debt, a prize in kind, a scholarship spent on room and board, a refund of an amount
  deducted earlier, the Alaska dividend as a state benefit; and 8s, a caregiver's Medicaid waiver payments, which
  are a subtraction the filer gains by answering yes); 6 (8z's open list read as complete); 4 (gambling with no
  W-2G); 1 (recapture of an earlier year's item, L-6); 3 (the spouse's items). Today each of 8b, 8c, 8g to 8r has
  its own specific prompt; under U1 the filer must recognise it in a list, which is the real increase in risk. The
  survey's findings L-6, L-10, L-19 and L-25 are designed out only if the help names them (8z recapture, 8a NOL,
  recoveries, 8v forks and staking).
- **Wording rule.** "In 2025, did you (or your spouse) have any of the following, with or without a form?" then one
  bullet per line, "Not sure" counts as yes.

### U2 foreign (Schedule B Part III and its neighbours)

- **Source.** Schedule B Part III heading: "You must complete this part if you ... (b) had a foreign account; or (c)
  received a distribution from, or were a grantor of, or a transferor to, a foreign trust" (f1040sb, Part III);
  i1040sb lines 7a, 7b and 8; Form 8938 (specified foreign financial assets); the Form 5471 clause split out of the
  Schedule B screen (finding L-34).
- **Definition.** Yes when, at any time in 2025, you or your spouse had a financial interest in or signature authority
  over an account outside the United States; held any other foreign financial asset (stock or securities of a foreign
  issuer not held in a US account, an interest in a foreign entity, a foreign pension or a foreign insurance or annuity
  contract with a cash value); received a distribution from, were a grantor of, or transferred to a foreign trust
  (or were a beneficiary of one); or were an officer, director or 10% shareholder of a foreign corporation.
- **Why a no is right.** Each of the four screens can be yes only in one of those situations: FinCEN 114 requires a
  foreign financial account; Form 8938 requires a specified foreign financial asset (which includes the accounts);
  line 8 is the foreign trust; Form 5471 the foreign corporation. A truthful no leaves every screen false.
- **False-no risk (moderate; the gated lines are refusal screens).** A wrong no drops a refusal, so the return is
  computed where the tool should have refused (the tool cannot prepare FinCEN 114, 8938 or 5471). Patterns: 6
  (signature authority, L-7; an existing trust's grantor, L-8; a beneficiary, L-24); 1 (an account closed early in
  2025: "at any time"); 8 (a foreign pension, a foreign mobile-money or payment account, foreign-held crypto);
  3 (the spouse).
- **Line 7a.** `sb.line7a` exists and is unreached (only `sb.partIII`, which no target reads, reads it). The
  source's own structure is "7a; if Yes, 7b (FinCEN 114)": under U2's yes, `sb.fbar_required` can itself be
  gated by `sb.line7a` (an A gate, no new input). That adds a question on a yes and saves one where 7a is no; it is
  optional and does not change U2's saving on a no.
- **Why not U2w.** Adding `sa.excluded_income` (Form 2555, Form 4563, Puerto Rico) saves one more question but its
  23 readers sit in 11 forms (eic, f2441, f8863, f8880, f8962, ira, s1a, s8812, sa, sb, sli), each of which changes
  and is due for its reviews; and its concept (income earned while living abroad or in a territory) is not the
  accounts-and-assets concept of U2, so a US citizen working abroad and paid into a US account is the filer who
  would answer U2w no wrongly (pattern 5) unless the question grows a second concept (test 2).

### U3 other payments

- **Source.** Form 1040 lines 25b ("Form(s) 1099"), 25c ("Other forms") and 26 (estimated payments and amount applied
  from 2024), i1040gi p. 39; Schedule 3 Part II "Other Payments and Refundable Credits", lines 10 (extension), 12
  (fuels, Form 4136) and 13a–13z (line 14). Lines 25a (W-2), 27–30 and Schedule 3 lines 9 and 11 are figured or
  asked elsewhere and are not covered.
- **Definition.** Yes when any federal income tax was withheld for you or your spouse on anything other than a
  Form W-2 (1099-R box 4, any 1099 box 4, SSA-1099 box 6, RRB-1099 box 10, W-2G, Schedule K-1, 1042-S, 8805, 8288-A),
  or you made or applied any payment toward 2025 tax (estimated payments, a 2024 overpayment applied, a payment with
  an extension request), or you have a Schedule 3 line 12 or 13 credit (Form 4136, Form 2439 and the others listed).
- **Why a no is right.** The six inputs are exactly those lines; a truthful no makes each zero.
- **False-no risk (moderate; a wrong no is in the government's favour).** A dropped payment overstates the balance
  due; the filer overpays or the IRS adjusts. Patterns: 4 (withholding on a 1099-R or SSA-1099 not seen as "withheld";
  Form 2439 from a REIT, L-2); 1 (a 2024 overpayment applied in 2025; an extension payment made in 2026); 8 (the fuel
  credit is a credit, not a payment). The help names each.
- **On a yes** (share about 29%, mostly 1099 withholding) all six are asked, as now. U3w (withholding alone) is the
  survey's B-4: lower risk but saves 0.6 per filer.

### U4 residential energy credits

- **Source.** Form 5695, "Residential Energy Credits", Parts I and II (i5695). The gates design already decided "one
  home-energy row, the Form 5695 questions being its follow-ups"; U4 makes that row a formal gate.
- **Definition.** Yes when Part I or Part II could be non-zero: the union of today's two questions (clean energy
  property installed in 2025 or a carryforward from 2024; energy efficient improvements installed in 2025).
- **False-no risk (low).** Patterns 1 (installation completed in 2025 but paid in 2024, or a carryforward) and 8
  (a heat pump or water heater not seen as an "improvement"; a home energy audit). Today's two questions carry the
  same risk; U4's help is their union.

### U5 prior-year carryovers (survey B-5, extended)

- **Source.** 2024 Schedule D line 21 and the Capital Loss Carryover Worksheet (i1040sd); 2024 Form 4562 line 13
  (i4562); 2024 Form 8995 line 16, "Total qualified business (loss) carryforward", or the same
  carryforward on Form 8995-A (i8995, i8995a).
- **Definition.** Yes when your (or your spouse's) return for an earlier year shows a capital loss carryover, a
  section 179 carryover of disallowed deduction, or a qualified business loss carryforward into 2025. These are
  document facts (finding L-20: ask what the filer can check).
- **False-no risk (moderate).** Pattern 1: a filer who did not file for 2024 still has a carryover from an earlier
  year, so the wording is "any earlier year", not "2024"; pattern 3: a spouse's carryover from a separate return.
  The NOL (8a) stays under U1 and `scope.schedule1`; the investment interest and charity carryovers stay under their
  own gates.
- **Cost.** The 10 readers sit in 7 forms, so U5 costs more reviews than it saves questions relative to U1 to U4.

### Not recommended

- **U7 (merged Schedule 2 screens).** Measured 4.0 and expected 3.9, but "additional tax" is a legal classification
  (pattern 7: the alternative minimum tax needs Form 6251 to know); each screen is already a list, and one merged
  list of about 30 items invites the skim of pattern 6; and it touches 10 forms. The screens stay direct, on the grid.
- **U8 (adjustments).** "Adjustments to income" is a term filers do not use; the two items are unrelated facts (test
  2), and it saves under one question.
- **U9 (Schedule 1-A).** Overtime is common (15%), the three items are unrelated, and a no saves at most two. A C
  gate (tips and overtime only with wages or self-employment) needs no new input but saves nothing on returns with a
  W-2, which is nearly all of them.
- **U1x.** Unemployment compensation is a recognised document fact (Form 1099-G) with its own concept; folding it
  into "other income" saves 0.6 more per filer and weakens U1's single concept. Leave it direct.
- **U6 (dependent care).** A real concept (Form 2441), but it saves under one question per filer and its readers reach
  the New York form, so New York reviews become due. Optional, after U1 to U5.

## 2. Formal encoding

Every umbrella is a **B gate** (an existence fact defined as exactly the situations of the lines it gates) with one new
`Bool` input; U2's optional line 7a nesting is an **A gate** with no new input. No C gate is proposed.

- **The umbrella input** sits in the form of its lines: `s1.line8_any`, `sb.foreign_any`, `f1040.other_payments_any`,
  `f5695.any`, `sd.carryovers_any` (names provisional). Label and source say "you (or your spouse)"; the help lists
  every case; "Not sure" is yes (standing rule 6).
- **One gate line per gated input,** `<input>_if_<umbrella>` (for example `s1.line8i_if_line8`), in the input's own
  form: a `choose` with guards `umbrella = true` (then the input) and `umbrella = false` (then the form's zero or false
  parameter line). The input keeps its id and gets `gated_by`. Every former reader reads the gate line; the build's
  gate check (`engine/src/gates.ts`) fails on a missed reader. Readers in other forms change too (U3: s3; U4: s3; U5:
  clcw, f8960, sc, f8995, qbi).
- **The roster** `$oi8z` (U1) cannot carry `gated_by`. As with the Form 8889 month counts, its one reader,
  `s1.line8z`, is put under a `choose` on the umbrella (the expression moves to a helper line, `s1.line8z` becomes the
  `choose`), so the roster is never asked after a no.
- **Existing gates.** A gated input that is itself a guard (`s1.line8h` guards `s1.jury_to_employer_if_pay`) is read
  by that guard through its new gate line; the nested gate then opens only after both yeses. Inputs read by computed
  tests (`s1.gambling_winnings` by `s1.has_gambling`, `sd.carryover` by the Schedule D, carryover worksheet and Form
  8960 lines) are read through their gate lines in the same way. No existing gate line gates a covered input, so no input gets two
  gates.
- **Refusal screens and refusals firing early.** U2's four inputs are refusal screens on Schedule B lines 2, 3 and 6
  (`refuses: when`). The `when` becomes the gate line. A refusal gate is evaluated before its line's expression, and
  an unknown gate makes the line pending, so the umbrella is asked at the point where the first screen was asked
  before; on a no the gate lines are false and nothing refuses; on a yes the screens follow at once, and a yes to one
  refuses as now. A refused return asks one more question (the umbrella) before refusing; its refusal is unchanged
  except that it names the gate line instead of the screen (as `sb.unsupported`'s did when `div.any` landed). The
  scope screens (`scope.ready`) are not gated, so a return outside the tool's scope still refuses as early as now.
- **Order.** The interview places each umbrella in the bank at the order of the first input it covers. Order never
  changes a value; the what-if checks that.
- **Lean.** The new lines use `choose`, `test` and `param` only; no new semantics.

## 3. Measured savings

From `reports/2025/umbrella_savings.md` (written by the tool, deterministic). The per-return saving of an umbrella is
*n* − 1 on every return answering it no and −1 on every return answering it yes, so on these returns it is exact.

| Scenario | Returns asking the umbrella (of 253) | Answering yes | Full profile, complete (12): mean saved | Minimal, every gate closed | All complete returns (161): mean saved | All returns, refused included |
|---|---|---|---|---|---|---|
| U1 `s1.line8_any` | 229 | 0 | 8.0 | 8 | 7.2 | 6.9 |
| U1x `s1.part1_other_any` | 229 | 0 | 9.0 | 9 | 8.1 | 7.8 |
| U2 `sb.foreign_any` | 223 | 4 | 3.0 | 3 | 2.7 | 2.6 |
| U2w `sb.foreign_wide_any` | 232 | 5 | 4.0 | 4 | 3.6 | 3.4 |
| U3 `f1040.other_payments_any` | 50 | 7 | 2.0 | 5 | 0.5 | 0.4 |
| U3w `f1040.withholding_other_any` | 29 | 0 | 1.0 | 1 | 0.1 | 0.1 |
| U4 `f5695.any` | 29 | 1 | 1.0 | 1 | 0.1 | 0.1 |
| U5 `sd.carryovers_any` | 218 | 1 | 2.0 | 2 | 1.0 | 0.7 |
| U6 `f2441.any` | 225 | 1 | 1.0 | 1 | 0.1 | 0.1 |
| U7 `s2.other_taxes_any` | 232 | 6 | 4.0 | 4 | 2.2 | 2.3 |
| U8 `s1.adjustments_any` | 229 | 3 | 0.8 | 1 | 0.9 | 0.9 |
| U9 `s1a.any` | 198 | 1 | 2.0 | 2 | 1.8 | 1.3 |
| **U1 to U5 together** | 253 | 13 | **16.0** (111.2 → 95.2) | 19 | 11.5 | 10.8 |

The slice profiles (social security, sales, stage4) reach few of these forms, which is why the all-returns means are
lower; U3 and U4 are reached only on the full profile's returns that reach the payments and credits lines. U3's full
profile mean (2.0) is below its no-return saving (5) because 6 of the 12 returns have other withholding or payments
and answer it yes, each paying one question.

Two limits. The synthetic returns answer the rare questions no almost everywhere (U1 is answered yes by none of
them), so the measured column is near the ceiling; the expected column is the honest guide for real filers, and rests
on shares several of which are recorded judgments. And the New York interview is not measured; it asks the same
federal questions first, so the federal saving carries over to a New York return.

## 4. Cost of landing

Costs are estimates. Review prices are the recent means per call in `.transcription/costs.jsonl`: class M about
$0.56 per form, transcription about $0.60 and render about $0.29 per form (less when line-scoped), completeness about
$0.27 per sample, screen about $0.08 and false-no about $0.12 per sample. One sample per subject per milestone
(`samples.py`, N = 1).

| Umbrella | Forms changed | Interview | Fixture files with a non-zero covered input (need yes) | Reviews due | Estimated review cost |
|---|---|---|---|---|---|
| U1 | s1 | 1 question (full, and any slice that reaches s1) | 11 (s1, f1040, oi8z, classm, mutation, …) | s1: transcription and render (line-scoped), class M, completeness; new gate: screen and false-no | about $2 |
| U2 | sb | 1 question | 6 (sb, sa, carloan, classm, mutation) | sb: the four; new gate: screen and false-no; the four existing sb screens become due (their gated lines change) | about $2.5 |
| U3 | f1040, s3 | 1 question | 20 (the largest ripple: withholding and estimated payments are common in fixtures) | f1040, s3: the four each; new gate: screen and false-no | about $3.5 |
| U4 | f5695, s3 | 1 question | 6 | f5695 (and s3, shared with U3 in one round): the four; new gate: screen and false-no | about $2 (with U3) |
| U5 | sd, clcw, f8960, s179, sc, qbi, f8995 | 1 question | 11 | seven forms, the four each; new gate: screen and false-no | about $11 |
| U6 (optional) | f2441, s3, f1040, dependent, ny_it201 | 1 question (federal and New York) | 7 | five forms, New York included | about $8 |

Every umbrella also touches: `interview/2025/questions.yaml` (and `stage4.yaml` or `sales.yaml` where a slice
reaches the form); `fixtures/2025/defaults.json` (the new input's default: no); `engine/src/generate.ts` and
`tools/engines/generate_cases.py` (the generated returns set the umbrella from the amounts it gates, as they do for
`div.any`); `tools/ny_fixtures.py` where New York fixtures answer the covered inputs; refusal records in fixtures
that name a gated screen (U2); `docs/COVERAGE.md` and the README coverage table (`tree.py`) for U2's screens; and the
adapter contracts of the forms whose boundary inputs change. Agent work: the fixture ripple and bookkeeping are
mechanical (Sonnet); the wording, the adjudication of the false-no and screen findings and any reading of sources are
judgment (Opus).

**Lanes under `tools/claims.py`.** Each umbrella adds an input id, and the `inputs` claim admits one branch at a time,
so the input-adding commits are serial whatever the split. Recommended: one lane per umbrella, in the order of
section 5, each claiming `inputs` and its forms, landing, and releasing before the next takes `inputs`. Work that does
not add inputs runs beside it: the wording and false-no pre-review of the next umbrella (no form edit), and the
reviews and adjudication of the previous one. U3 and U4 both change s3, so they land as one lane (one review of s3 per
round). U5's seven forms make it the one umbrella worth splitting by form only if `inputs` is landed first in a
small commit (the new input and its question) and the reader redirects follow per form.

## 5. Order of landing

By expected saving per estimated review cost, adjusted for risk:

1. **U1** (s1; 7.3 per filer, about $2). Biggest saving, one form. Also the highest false-no risk: land it with its
   false-no review adjudicated before merge, not after.
2. **U2** (sb; 2.9, about $2.5). One form; refusal screens only.
3. **U3 with U4** (f1040, s3, f5695; 3.2 + 1.0, about $5.5). The largest fixture ripple; one s3 review.
4. **U5** (seven forms; 1.8, about $11). Last of the set.
5. U6 only if the owner wants it (0.9, about $8, New York reviews).

Expected cumulative effect: about 16 fewer questions per real filer (estimate); measured 16.0 fewer
(111.2 → 95.2) on the complete full-profile returns. Lane A's floor still holds afterwards: order adds nothing.

## 6. Decisions for the owner

1. **Adopt U1, the Schedule 1 line 8 umbrella (survey B-2)?** One question, listing every Schedule 1 line 8 item
   (gambling, cancelled debt, Alaska dividend, jury pay, prizes, hobby income, scholarships not on a W-2, the rest of
   8a–8v, and any other income), replaces nine questions. It saves about 7 questions per filer, the largest single
   saving, and has the largest risk: a wrong no silently drops up to nine income lines (and the Medicaid-waiver
   subtraction). The first gates build deferred it for that reason. Yes, no, or yes only after its false-no review is
   ruled clean?
2. **Foreign umbrella scope: Schedule B and neighbours only (U2), or also excluded foreign income (U2w)?** U2 covers
   FinCEN 114, Form 8938, foreign trusts and Form 5471 (saves about 3 per filer, one form changes). U2w adds the
   Form 2555 / Form 4563 / Puerto Rico question: one more question saved, but 11 forms change and the question must
   also ask about living or working abroad.
3. **Payments: one umbrella over withholding, estimated and other payments (U3), or withholding only (U3w, the
   survey's B-4)?** U3 saves about 3 per filer (six questions behind one; about 29% answer yes and see all six); U3w
   saves under one. A wrong no understates payments (the filer overpays), not tax.
4. **Prior-year carryovers (U5): adopt, though it changes seven forms for about 2 questions per filer?**
5. **Dependent care (U6): adopt, defer, or drop?** About 1 question per filer; changes five forms including New York's.
6. **Confirm the qualification rule** (section "What qualifies"): an umbrella must be one concept in the source's
   terms, with no gated line reachable from outside its definition; so the merged additional-tax screens (U7),
   "adjustments" (U8) and Schedule 1-A (U9) are not umbrellas, and the remaining rare single questions stay as grid rows.
7. **Landing order and lanes:** serial by `inputs` claim, U1, U2, U3 with U4, U5, as in section 5?
