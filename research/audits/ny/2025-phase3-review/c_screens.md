# Review C: New York refusal screens (IT-201 / IT-2, tax year 2025)

Scope: every `ny_it201.ask.*` question and every gate named in a `refuses:` list in
`forms/ny/2025/ny_it201.yaml` and `forms/ny/2025/ny_it2.yaml`, with the help text in
`interview/ny/questions-2025.yaml`. Each one was checked against the archived instructions in
`sources/ny/2025/` (page N = N-th form-feed chunk of `ny_it201i.cols.txt`; `ny_it201i-html.txt`; `ny_it270i.txt`).
The question is whether the refusal fits the target: a full-year NYC resident on the NY standard deduction.
Nothing was executed and no file other than this one was written.

Verdicts: RIGHT, TOO WIDE, TOO NARROW, UNCLEAR. Severity: high (a completed return can be wrong), medium (an
unnecessary refusal of a common case, or an unclear question likely to be misanswered), low (wording).

## Counts

| | count |
| --- | --- |
| Screens judged (31 Bool asks + 1 dollar ask feeding a gate, 10 computed gates, IT-2 Yonkers gate) | 43 |
| RIGHT | 30 |
| TOO WIDE | 4 (2 medium, 2 low) |
| TOO NARROW | 2 (1 high, 1 low) |
| UNCLEAR | 7 (1 high, 4 medium, 2 low) |
| Uncaught situations (no screen) | 6 (1 high, 1 medium, 4 low) |

Medium-or-higher findings:

1. **H1. `gate.estimated_penalty`: TOO NARROW (high).** It fires only when there is a balance due and prepayments
   are below 100%/110% of the 2024 tax. The instructions say a penalty can be owed with a refund, and whenever
   estimated tax was underpaid for any one payment period.
2. **H2. `ask.pension_exclusion`: UNCLEAR (high).** The question says "pension or annuity income". Line 29's
   qualifying income includes IRA distributions (line 9). A filer aged 59½ or older with only IRA withdrawals will
   likely answer No, and the up-to-$20,000 subtraction is then lost.
3. **H3. Uncaught: item H dependents the filer was entitled to claim but did not (high, rare).** `item_h_count`
   counts only federally claimed dependents. Line 36, the household credits and the IT-213/IT-270 gates are then
   understated.
4. **M1. `gate.it270`: TOO WIDE (medium).** It refuses every return with a dependent and FAGI up to the highest
   threshold + $5,000 ($96,902 / $93,361). The per-dependent-count threshold and the $10,000 investment-income test
   would let most such filers through (for example, single with 1 dependent at $50,000 FAGI).
5. **M2. `gate.line25` (line 4 > 0 branch): TOO WIDE versus the 2025 instruction text (medium; owner decision B1).**
   The 2025 instruction for line 25 names only the inflation refund check.
6. **M3. `ask.special_code`: TOO WIDE (medium).** It refuses codes that change no computed line (C2 installment
   request, E3/E5 extensions, C7, D9).
7. **M4. `ask.it225`: UNCLEAR (medium).** It is a catch-all no filer can answer without the IT-225 list. The
   instructions name items that apply to ordinary residents: S-124 disability exclusion, S-118 combat pay, A-215
   NOL.
8. **M5. `ask.itemize`: UNCLEAR / partly TOO NARROW (medium).** It asks what the filer "wants", but the rule is
   "larger of". It also misses the married-filing-separately rule that both spouses must itemize if one does.
9. **M6. `ask.real_property_credit`: UNCLEAR (medium).** "Do you qualify" can only be answered with the IT-214
   instructions, which are not in the help.
10. **M7. `ask.prior_year_tax`: UNCLEAR (medium).** It does not say what to enter with no 2024 New York return or a
    part-year 2024 return. An answer of 0 switches the penalty gate off.
11. **M8. Uncaught: no prior-year safe harbor when the 2024 return was not a 12-month resident return (medium).**
    See M7.

---

## Per-screen judgements

### Residency and status screens (all refuse on line 1)

**`ask.state_resident` → `gate.part_year_state`: RIGHT, with a low UNCLEAR note.**
p. 3: "If you were a New York State resident for only part of the year, do not file Form IT-201." The question quotes
the two resident tests of p. 30. Low note: p. 30 says a New York domiciliary "is not a resident if you meet all three
of the conditions in either Group A or Group B" (30 days or less in NY with no NY abode; or 450 days abroad in 548). A
filer under either group answers "domiciled in New York State" Yes and is computed as a resident. The same applies to
the military proviso ("unless you were in active service in the military"). Both are rare. The phrase "(and your spouse,
on a joint return)" also overlaps `ask.spouse_resident`. A resident whose spouse was a nonresident will answer No here
and get the IT-203 refusal instead of the separate-returns one. Either way the return is refused, so this is low.

**`ask.city_resident` → `gate.part_year_city`: RIGHT.** p. 31: "substitute New York City or Yonkers in place of New
York State"; p. 14 Line 50: "If you were a New York City resident for only part of 2025, complete Form IT-360.1".

**`ask.spouse_resident` → `gate.spouse_nonresident`: RIGHT, with a low remedy-wording note.** p. 3: "If one of you was
a New York State resident and the other was a nonresident or part-year resident, you must each file a separate New York
return ... However, if you both choose to file a joint New York State return ... both spouses' income will be taxed as
full-year residents". Refusing the joint-as-residents election is not too wide. Such a spouse is necessarily also not
a full-year City resident. pp. 13–15 then require the City tax on a separate sheet (Line 47a/48: "only one of you was a
resident of New York City for all of 2025, do not enter an amount here. See the instructions for line 51"), which the
encoding does not do. Low: for a State-resident spouse who was only a City nonresident, the remedy text ("separate returns
or a joint return as if both were residents") is wrong. The real route is the line 51 separate-sheet computation (p. 15).

**`ask.special_accrual` → `gate.special_accrual`: RIGHT.** p. 31: "You are subject to the special accrual rules only if
you have accrued income for 2025 and • you were a nonresident of New York State on December 31, 2024; or • you will be a
New York State nonresident on January 1, 2026", and for the City "nonresident of New York City on December 31, 2024 ...
or ... will be a New York City nonresident on January 1, 2026". A State nonresident is necessarily a City nonresident,
so asking only about the City for December 31, 2024 covers both. The accrued-income clause is broader than p. 31's
("non-New York source income" for the earlier year), so it can only refuse more.

**`ask.yonkers` → `gate.yonkers`: RIGHT.** p. 5, Item D2: "If you or your spouse ... maintained or had use of an
apartment or living quarters in Yonkers during any part of 2025 ... you must mark an X in the Yes box", and "If you
marked the Yes box on line D2(4), you may be subject to the Yonkers nonresident earnings tax". The wording matches form
items D2(1) and D2(4). It is slightly wide: living quarters only make you "may be considered a resident". That is
acceptable because the outcome turns on facts and circumstances.

**`ask.special_code` → `gate.special_code`: TOO WIDE (medium) and UNCLEAR (low).** pp. 5–6, Item G. Only some codes change
a computed amount or the scope:
- A6, Build America Bond interest: Note 1 on p. 13 changes the household-credit AGI.
- M4–M9, an SCRA residence election.
- Y1, Yonkers.
- K2, killed in action.
- 56, itemized deductions.

The rest only mark timing or administration:
- C2: "Enter this code if you cannot pay your tax due in full by April 15, 2026, and would like to request an
  installment payment agreement".
- C7 and E3: extensions.
- E5: "Extension of time to file beyond six months".
- D9: a 90-day extension; the decedent screen already refuses it.

For those codes the encoding computes every line correctly, so the refusal blocks a correct return. C2 is the one likely
to come up, for a filer with a balance due. Fix: refuse only A6, M4–M9, Y1, K2 and 56, and either print the
administrative codes as entered or ask for them as a note. UNCLEAR (low): the question lists examples but not E5, K2
or 56, and most filers will not know what a "special condition code" is. The help text helps.

**`ask.decedent` → `gate.decedent`: RIGHT.** p. 4: "If the taxpayer whose name is listed first on the return died after
December 31, 2024, and before you filed your return, enter the date of death". Refusing is a scope choice. The question
leaves out "and before you filed" but means the same in practice.

**`ask.item_c` (feeds lines 34, 40, 48, 69, 69a; not a refusal): RIGHT.** p. 5, Item C: "You must mark the Yes box
even if the other taxpayer did not claim you as a dependent." The question carries that sentence.

### New York additions and subtractions

**`ask.out_of_state_bond_interest` → `gate.line20`: RIGHT.** p. 7, Line 20: "enter any such interest income ... that was
not included in your federal adjusted gross income. This includes ... interest and dividend income from tax-exempt bond
mutual funds, and – tax-exempt money market funds". The question covers funds.

**`ask.414h` → `gate.line21`: RIGHT** (low wording note). p. 8, Line 21 lists the covered systems, including "an employee
of the State or City University of New York who belongs to the Optional Retirement Program" and "a member of the
Manhattan and Bronx Surface Transit Operating Authority (MABSTOA) Pension Plan". MABSTOA staff may not see themselves as
"a public employee of New York State or its local governments". Adding "(including CUNY/SUNY and MABSTOA)" would close
that.

**`ask.529_nonqualified` → `gate.line22`: RIGHT.** p. 8, Line 22. A filer who paid K-12 tuition from a NY 529 may answer
No; the account is federally qualified, but p. 8 says "any withdrawal used to pay tuition ... at elementary or secondary
... schools" is nonqualified. That filer is still refused by `ask.529_owner` ("contribute to or withdraw from"), so no
return goes wrong.

**`ask.it225` → `gate.it225` (lines 23 and 31): UNCLEAR (medium).** p. 8, Line 23: "Use this line to report other
additions that are not specifically listed on Form IT-201." The question and help name only pass-through
modifications. The archived instructions name IT-225 items an ordinary W-2 or retired resident can have, and the filer
gets no hint of them:
- p. 10: "disability income exclusion (Form IT-225, S-124)".
- p. 32: military combat pay, "subtraction modification number S-118".
- p. 31: the NOL limit, "addition modification number A-215".
- p. 7: Form 4970 accumulation distributions, A-114.

A filer with one of these answers No, and the return is wrong. Fix: list the common items in the question or help,
with a link to IT-225.

**`gate.line25` (`line4 > 0` or `ask.inflation_check`): RIGHT for the inflation-check branch; TOO WIDE for the line 4
branch (medium, owner decision B1).** p. 8, Line 25, is the whole 2025 instruction, and the web edition (`-html` l. 438–440)
says the same: "If you received an inflation refund check from the Tax Department and included the check amount in the
calculation of federal adjusted gross income reported on line 19, then enter that amount on line 25." A filer with a
state refund on line 4 (common among federal itemizers) would, by the instruction text, have line 25 = 0. The encoding
already computes that. The form label "(from line 4)" conflicts, and the ambiguity is recorded
(`amb.ny.2025.line25`), so this is a known, deliberate over-refusal. It is listed for completeness.

**`ask.gov_pension` → `gate.line26`: RIGHT** (low UNCLEAR note). p. 9, Line 26 quoted verbatim. The help ("New York State,
local and federal government pensions") does not mention "Certain public authorities, including ... (MTA) Police ...;
(MABSTOA); and Long Island Railroad Company", military retired pay ("including the military"), or QDRO distributions to
a nonemployee spouse. A retiree under 59½ (so not caught by line 29) with an LIRR or military pension could answer No.
Add these to the help.

**`ask.us_obligation_interest` → `gate.line28`: RIGHT.** p. 9, Line 28: "Did you include interest income from U.S.
government bonds or other U.S. government obligations on lines 2, 6, or 11?" Mutual-fund dividends ("meet the 50% asset
requirement") are covered by the question.

**`ask.pension_exclusion` → `gate.line29`: UNCLEAR (high).** p. 9, Line 29: "Did you enter an amount of pension income or
annuity income, or both (generally reported on line 9 or 10)". Qualifying income includes "periodic and lump-sum
payments from an IRA" and "periodic distributions from government (IRC § 457) deferred compensation plans". The
question says "pension or annuity income" and never mentions IRAs or line 9. A 60-year-old with only IRA distributions
will naturally answer No, and the encoding then computes NY AGI up to $20,000 too high. The age test is right (p. 9: "59½
before January 1, 2025" or "became 59½ during 2025, enter only the amount you received after"). Fix: say "pension,
annuity, IRA, 401(k)/403(b)/457 distributions (Form 1040 lines 4b or 5b)". Better, gate mechanically on
f1040.line4b + line5b > 0 together with age or beneficiary status.

**`ask.529_owner` → `gate.line30`: RIGHT** (low TOO WIDE). p. 10, Line 30 covers owner contributions, owner withdrawals
"included in your federal adjusted gross income", and beneficiary withdrawals so included. Owner withdrawals that are
fully qualified and not in FAGI, with no contributions, make line 30 zero but are refused. That is rare and low.

### Deduction

**`ask.itemize` → `gate.itemize`: UNCLEAR and partly TOO NARROW (medium).** p. 10–11, Line 34: "Compare the Form IT-196,
line 49 amount to your New York standard deduction amount ... For a greater tax benefit, enter the larger". The
question asks what the filer "wants", and a filer cannot know whether IT-196 is larger without computing it. A federal
itemizer (item B Yes) with mortgage interest and charity above $8,000/$16,050 will often be better off itemizing, and
nothing prompts them. TOO NARROW part (p. 11, Notes): "If you are married and filing separate returns ..., both of you
must take the standard deduction unless both of you choose to itemize". An MFS filer whose spouse itemizes on New York
must itemize, but the question as worded lets them answer No. Fix: for MFS, ask whether the spouse itemizes on New York.
For federal itemizers, show the standard amount and suggest comparing.

### Credits and taxes (lines 40–71)

**`gate.hh_state_mfs` / `gate.hh_city_mfs`: RIGHT.** pp. 13–14, Note 4: "use your spouse's federal adjusted gross income";
table 3/6 count dependents "from both returns". This cannot be computed from one return, and the gate fires only within
the credit rows.

**`gate.hh_state_over7` / `gate.hh_city_over7`: RIGHT** (low: Note 3, "For each individual over 7, add the amount in this
column to the column 7 amount", is simple to compute, so the refusal could be lifted).

**`ask.resident_credit` → `gate.resident_credit`: RIGHT.** p. 13, Line 41, verbatim.

**`ask.other_credits` → `gate.other_credits` (lines 42, 71): RIGHT** (low). p. 13, Line 42. A filer who does not know about a
credit and answers No files an overstated but valid return.

**`ask.other_taxes` → `gate.other_taxes` (lines 45, 51): RIGHT** (low UNCLEAR). IT-201-ATT Part 2 line 20, "Other New York
State taxes" with codes, covers more than lump-sums (for example credit recaptures). The question says "for example",
so it is acceptable.

**`ask.city_credits` → `gate.city_credits`: RIGHT.** p. 15, Line 53, verbatim.

**`ask.mctmt` → `gate.mctmt`: RIGHT** (low wording). p. 15: "If an individual's net earnings from self-employment allocated
to either zone exceed $50,000 ... The $50,000 threshold is calculated on an individual basis, even if you file a joint
income tax return." The question ("you or your spouse ... of more than $50,000") does not say per person and per zone.
A couple who sum their earnings would refuse needlessly, which is wider, never narrower. Add "each of you separately, per
zone".

**`ask.owes_use_tax` / `ask.use_tax_st141` → `gate.use_tax_st141`: RIGHT.** p. 18: "You must use Form ST-141 ... if any of
the following apply: • You prefer to calculate the exact amount ... • You owe sales or use tax on an item or service
costing $1,000 or more ... • ... purchases related to a business not registered for sales tax purposes, rental real
estate, or royalty activities." The question matches. The chart's part-year abode proration does not arise for a
full-year resident. Low: p. 18 says motor-vehicle and vessel use tax "is paid directly to the Department of Motor
Vehicles" and is not reported on line 59. A filer counting a car would answer the $1,000 question Yes and be refused.

**`ask.contributions` → `gate.contributions`: RIGHT** (p. 19, Line 60, verbatim).

**`gate.child_credit` (claimed dependent under 17): RIGHT.** p. 19, Line 63: "Do you have at least one qualifying child?
(A qualifying child must be less than 17 years old on December 31st of the tax year.)" (See uncaught H3: it reads
only federally claimed dependents.)

**`ask.dependent_care` → `gate.dependent_care`: RIGHT.** p. 19, Line 64, verbatim. It also covers the NYC credit, which
requires qualifying for the federal one.

**`gate.eic` (federal EIC claimed, or FAGI below the EIC limit): RIGHT** (`amb.ny.2025.eic_could_claim`). p. 19, Line 65 /
p. 21, Line 70: "Did you claim the federal earned income credit ... or could you have claimed it based on your federal
adjusted gross income?" It also covers "If the IRS is calculating your federal earned income tax credit".

**`ask.noncustodial` → `gate.noncustodial`: RIGHT** (p. 19, Line 66, verbatim).

**`ask.real_property_credit` → `gate.real_property`: UNCLEAR (medium).** p. 19, Line 67: "Review the instructions for Form
IT-214 ... to see if you qualify". The question asks "Do you qualify" with no criteria, and the help says only "low
household income". IT-214 is not archived, so its limits cannot be quoted here. A low-income NYC renter who does not know
the credit will answer No and lose a refundable credit. Fix: state the IT-214 eligibility tests (household gross income
limit, rent/property-tax test) in the help once IT-214-I is archived, or gate mechanically on FAGI.

**`ask.college_tuition` → `gate.college_tuition`: RIGHT** (p. 19, Line 68, verbatim).

**`gate.stc_rr_income`: RIGHT** (decision B7, `amb.ny.2025.school_credit_income`). p. 20, Line 69a: "or your income (see
below) is more than $500,000, you do not qualify".

**`gate.it270` (claimed dependent and FAGI ≤ highest threshold + $5,000): TOO WIDE (medium).** `ny_it270i.txt`: the credit
needs "you claimed one or more dependents", "your federal adjusted gross income (FAGI) is no more than $5,000 above your
applicable income thresholds based on the number of dependents claimed and your filing status", and "your investment
income is $10,000 or less". The threshold table is per count. Single/HOH: 1 → $31,503, 2 → $36,824 ... 8 or more →
$88,361. MFJ: 1 → $36,789 ... 7 or more → $91,902. The gate uses only the top row ($93,361 / $96,902). So a single
parent with one child and $50,000 FAGI (limit $36,503) is refused although the credit is plainly zero. That is a common
NYC household. Fix: compare line 19 with the per-count threshold + $5,000 for `item_h_count`. Optionally also pass when
investment income (Form 1040 lines 2a + 2b + 3b + max(7a, 0), per Line D "For most taxpayers") is over $10,000.

### Payments, penalties, refund

**`ask.other_withholding` → `gate.other_withholding` (lines 72, 73): RIGHT.** pp. 21–22: "Form IT-1099-R ... • Form 1099-G
... • Form W-2G". The question names all three.

**`ny_it2.yonkers_gate` (IT-2): RIGHT.** p. 21 counts Yonkers withholding on line 74, which the encoding fixes at zero, and
Yonkers is out of scope (p. 17, Lines 55/56). Low: the refusal sits on `ny_it2.city_withheld`, not on line 74. Every IT-2
record is still reached, so it works.

**`ask.prior_year_tax` + `ask.prior_agi_high` → `gate.estimated_penalty`: TOO NARROW (high).** p. 23, Line 81: "You may owe a
penalty: • if line 80 is $300 or more and represents more than 10% of the income tax shown on your 2025 return; or • if
you underpaid your estimated tax liability for any payment period." p. 24: "It is possible for you to owe an estimated
tax penalty and also be due a refund. In that case: 1. Subtract the estimated tax penalty amount from the overpayment."
The gate requires `tax_due > 0` and compares annual totals only. Two kinds of return pass with line 81 = 0 although a
penalty can be due:
- (a) A refund return where the estimated payments (line 75) were made late or unevenly. Example: one payment on
  January 15, 2026 covering the year.
- (b) A balance-due return whose annual prepayments meet the safe harbor but whose installments did not.

Withholding is not affected in practice; the risk is confined to filers with line 75 > 0. Fix: when line 75 > 0, ask
whether the payments were made in four installments of at least a quarter of the safe harbor by each due date, and
refuse otherwise.

**`ask.prior_year_tax`: UNCLEAR (medium).** p. 23: "100% of your 2024 New York income tax based on a 12-month return". The
question gives no guidance for a filer who filed no 2024 New York return or a 2024 part-year IT-203; the target
population includes recent movers into NYC. Entering 0 makes the safe harbor $0, so the gate can never fire. Fix: ask
whether a 2024 full-year New York return was filed, and refuse (or require the 90%-of-current-year test) if not. Low:
"2024 New York income tax" does not say whether MCTMT or Yonkers amounts count. The help says State and City.

**`ask.prior_agi_high`: RIGHT.** p. 23 verbatim. The farmer/fisherman exception is not asked; that only refuses more, as
the line's note says.

**`ask.late_penalty` → `gate.late`: RIGHT** (p. 24, Line 82).

**`gate.line79_over`: RIGHT** (p. 23, Line 79: "The total of lines 78a through 79 should equal the amount on line 77").

**`ask.refund_529` → `gate.refund_529`: RIGHT** (p. 23, Line 78a).

---

## Situations no screen catches

**H3. Dependents the filer was entitled to claim but did not (high, rare).** p. 6, Item H: "Also enter the required
information for any dependent you were entitled to claim on your federal return but chose not to ... You may still claim
them as a dependent on your New York State return." `item_h_count` sums `dependent.claimed`, which is computed from the
federal dependents entered. A dependent the filer left off the federal return (the instructions' example: so the child
can take an education credit) is missing from:
- line 36 ($1,000 each);
- the household-credit people count (tables 2 and 5);
- `gate.child_credit` and `gate.it270`.

The line 36 and household-credit omissions make the return wrong; the missed gates mean credits that should refuse do
not. Fix: ask "Is there anyone you could have claimed as a dependent on your federal return but did not?" and refuse
on Yes (or add them to item H).

**M8. No 2024 full-year return (medium).** See `ask.prior_year_tax`. A first-year resident's penalty test is not
handled.

**L1. MFS spouse itemizes on New York (low–medium).** See `ask.itemize`. p. 11: "both of you must take the standard
deduction unless both of you choose to itemize".

**L2. Domicile exceptions Group A/B and the military proviso (low).** See `ask.state_resident` (p. 30).

**L3. Item A exceptions for federal joint filers (low).** p. 5: a spouse whose whereabouts are unknown, or who refuses to
sign, lets the filer use filing status ③ in New York although the federal return was joint. The encoding takes the
federal status. The joint New York return it produces is still a valid return, so this is low. A filer who must file
separately, because the spouse will not sign the New York return, gets no refusal.

**L4. Foreign income without a W-2 (low).** p. 21: "If you received foreign income but did not receive a federal Form W-2,
you must complete Form IT-2." The `$ny_it2` question asks only for W-2s. No amount changes (no New York withholding), but
the IT-2 the filer submits would be incomplete.

Also noted, not counted: no screen asks about a fiscal-year return (form header "or fiscal year beginning"). This is
presumably excluded by the federal scope.
