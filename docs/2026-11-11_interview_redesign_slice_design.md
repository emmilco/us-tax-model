# Interview redesign, first slice: design for review

Prepared 2026-11-11 for the owner, before anything is built. Tax year 2025, federal. Nothing in the repository was changed to write this. The intent document (`docs/2026-11-11_interview_redesign_intent.md`) is the authority; this document applies it to three parts of the interview:

1. **the opening**: who is on the return, the filing status, and the "whose entry is this" question;
2. **the credits screen** (`scope.credits`), taken apart completely;
3. **health savings accounts** (HSAs), from the first question to the last.

A few terms used throughout, in plain words:

- **Input**: one fact the tax model needs from the filer. Each input has one question.
- **Roster**: a question whose answer is a list of things (the people on the return, the employers, the HSAs).
- **Refusal**: the tool stops and says, with a citation, that it cannot prepare this return. A refusal is a correct outcome, not an error.
- **Catch-all**: a question that lists everything the tool cannot do and asks "any of these?". A Yes refuses.
- **Gate**: a question whose answer decides whether other questions are asked at all.
- **Filing status**: one of five boxes on Form 1040 that sets the tax rates and many limits: single, married filing jointly, married filing separately, head of household, qualifying surviving spouse.
- **HSA**: a savings account for medical costs that goes with a high-deductible health insurance plan. Form 8889 is the tax form for it.
- **Schedule 3**: the page of Form 1040 that collects most tax credits. A **credit** is an amount taken off the tax itself.

---

## Summary (one page)

### The redesigned slice at a glance

**Opening** (today 3 to 4 questions; proposed 1 to 2)

- *Who is this tax return for?* "Just me" or "Me and my husband or wife, together on one return".
  - "Together" also records the filing status (married filing jointly) and which entry is whose. Nothing more is asked.
  - "Just me" is followed by *Which of these fits you on December 31, 2025?*, with the four remaining filing statuses described as situations in a life, each with its official name in parentheses.
- The "whose entry is this, yours or your spouse's?" question is no longer asked. The first answer already says it.
- The household questions that test head of household and qualifying surviving spouse stay where they are, as the precise layer beneath the plain option.

**Credits** (today one 129-word catch-all at the start, plus two "type in a total" questions; proposed: no credits screen at all)

- Eight short questions, each asked where its topic comes up: a vehicle bought, an adoption, a mortgage credit certificate, a disability retirement, last year's return, money paid back, two rare papers, and one short list of four rare payments.
- Two more for people with a business (business credits, fuel).
- Four situations need no new question, because an existing answer already catches them.

**Health savings accounts** (today a 84-word roster question, a 232-word catch-all, a 339-word coverage question and 14 others, scattered among 27 unrelated questions; proposed: one block, asked together)

- *Did you have a health savings account (HSA) in 2025, or get money from one?*
  - three short questions about the account itself (owner died; inherited; Archer MSA);
  - **money in**: employer amount, own amount, a transfer from an IRA, money taken back;
  - **coverage**: one three-way question, then one short check, then the month questions only if the year was not uniform;
  - **money out**: total, the code in box 3 of Form 1099-SA, money put back, a mistaken payment, whether it all paid medical costs;
  - one question about loans and dealings with the account.
- The 232-word catch-all is replaced by eight short yes/no questions, and a ninth asked only of people whose coverage had a gap. One of its ten situations needs no question, because another answer settles it.

### What a typical filer reads, before and after

Words of question text, counting the answer options (help text is counted separately in section G).

| Filer | Today | Proposed |
|---|---|---|
| Opening, one unmarried person | 58 words, 3 questions | 87 words, 2 questions |
| Opening, married couple filing together | 82 words, 4 questions | 18 words, 1 question |
| Credits, a filer with none of the unusual ones | 156 words, 3 questions | 170 words, 8 questions |
| HSA, a filer with no HSA (per person) | 95 words, 1 question | 17 words, 1 question |
| HSA, an ordinary account (payroll deposits, card spending) | 1,167 words, 9 questions | 340 words, 17 questions |

Two honest remarks. For credits the words do not fall: one unanswerable 129-word question becomes eight answerable ones of about 20 words each. For an unmarried person the opening is a little longer, because the filing statuses are described instead of shown as codes (`mfj`, `hoh`). The gain in both places is that every question can be answered by someone with no tax vocabulary.

### The coverage claim

Every situation the two catch-alls cover today has a path of plain questions that reaches it (section C: 29 rows for credits, 13 for HSAs). None is dropped. Three refusals become slightly wider than today (each noted). Sections A and C also show six places where today's interview asks about the same situation twice, and three where today's catch-all misses a situation or refuses one the tool could prepare.

### Decisions needed from the owner (section H)

1. May one answer record more than one input (the "who is this return for" choice also recording role and joint status)? This touches the rule that the interview sets no input. **Recommended: yes, narrowly.**
2. Should the "were you married" question move ahead of the filing status, so that the status question shows two or three options, not four? It costs a model change. **Recommended: not in this slice.**
3. The two Schedule 3 questions that ask the filer to type in a total from a form the tool does not prepare (`s3.line12`, `s3.line14`): refuse instead, or keep? **Recommended: refuse.**
4. Where are refusal questions asked: at their topic (later, but in context), or early? **Recommended: at their topic.**
5. Three scope changes the sources would support: a spouse who inherited an HSA; the credit for the elderly or the disabled; a dormant Archer MSA. **Recommended: not in this slice.**
6. Archive the instructions of the credit forms that are not in `sources/2025/` before their precise questions are written. **Recommended: yes.**
7. The per-person frame. **Recommended: show "About you" and "About your spouse" on a joint return and nothing on a one-person return.**
8. The child question about a health FSA at work (section D.3): add it? **Recommended: yes.**
9. Refuse on the fact of an adoption or a mortgage credit certificate, or only on the wish to claim the credit? **Recommended: on the fact.**

---

## A. Today, precisely

The full text of every question in the slice, exactly as built, is in the appendix (generated from `canonical/2025/interview-full.json`, so it is verbatim). The tables here give the facts about each. "Words" counts the question text; where a question shows answer options, their words are given too.

"When asked" was checked by walking the built interview (profile `full`) with synthetic answers, five returns: a single filer with no HSA, three single filers with HSAs, and a married couple. The logs were written outside the repository.

### A.1 The opening

| Id | Type | Words | When asked | What the answer does |
|---|---|---|---|---|
| `$person` | Roster with two fixed choices | 16, options 8, help 58 | First, always | "Just me" creates one entry keyed `taxpayer` (shown as "You"). "Me and my spouse (joint return)" creates two, `taxpayer` and `spouse`. No line reads the roster itself; lines add up over its entries. |
| `f1040.status` | One of five codes: `single`, `mfj`, `mfs`, `hoh`, `qss` | 5, options 5 (the bare codes), no help | Second, always | Read by 111 lines (tax tables, limits, the checks below). `mfs` (married filing separately) is refused by the lines that read it, for example `s3.line11` and `f8889.line13_figured`. |
| `person.role` | `taxpayer` or `spouse` | 22, options 2, help 12 | Third; once per person, so twice on a joint return. On a joint return the spouse's entry is asked first (alphabetical). | Read by 33 lines (34 references): they pick out "your" amounts or "your spouse's" on Forms 2441, 8863, 8880, the IRA worksheets, Schedules A and 1-A, and the household counts. |

Three checks tie these answers together, and each ends in a refusal shown as "conflicting answers":

- `household.roster_bad`: the entries must be one `taxpayer`, plus one `spouse` exactly when the status is `mfj`. Message: "Enter one person with the role taxpayer, and, only when married filing jointly, one person with the role spouse."
- `household.filing_status_conflict`: single but married at the end of 2025; or joint but not married and no spouse who died in 2025.
- `household.hoh_fails` and `household.qss_fails`: head of household or qualifying surviving spouse chosen, and the household questions later show its tests are not met. `household.widowed_2025`: single or head of household chosen although the spouse died in 2025.

**What this means for a filer today.** A couple filing together says "joint" in question 1, must pick `mfj` from five unlabelled codes in question 2, and then says twice which entry is whose. Later (question 13 on the walked joint return) they are asked the 217-word `household.married`. Each of these can be answered against the first answer, and the tool then reports a conflict.

The household questions that decide the two unfamiliar statuses exist, and are asked only after that status is chosen: `household.unmarried` (325 words), `household.home_cost` (118), the per-dependent tests, and `household.qss_eligible` (375 words: five tests in one yes/no).

### A.2 The credits screen, `scope.credits`

| Id | Type | Words | When asked | What the answer does |
|---|---|---|---|---|
| `scope.credits` | Yes/no | 129, help 30 | Fourth, always | Yes refuses. The answer is read as a refusal by `scope.ready` and by seven other lines (see below). No is read by nothing else: it changes no amount. |
| `s3.line12` | Amount | 15, help 19 | Always (question 47 on the minimal single return) | Added into Schedule 3 line 15. The filer types the credit from Form 4136, which the tool does not prepare. |
| `s3.line14` | Amount | 12, help 23 | Always (question 48) | Added into Schedule 3 line 15. The filer types the total of Schedule 3 lines 13a to 13z, which the tool does not prepare. |

The seven other readers of `scope.credits`, with the message each gives: Form 1040 line 30 and Schedule 3 line 8 ("Other credit forms (Schedule 3 lines 6a to 6z; Form 1040 lines 30 and 31)"); Schedule 8812 Credit Limit Worksheet A lines 2 and 4; the Form 8863 credit limit worksheet line 5; and the two Form 5695 credit limit worksheets. Those five worksheet lines refuse because another credit, if claimed, would change the order in which credits use up the tax.

`s3.line12` and `s3.line14` are listed here although they are not named in the slice, because they are about the same credits (finding 1 below).

**The complete list of situations `scope.credits` covers.** The question asks about "any credit other than" eleven. The printed Schedule 3 and the Form 1040 instructions make the rest a closed list. For each: the source, and whether anything else in today's interview already catches it.

| # | Situation | Source | Already caught elsewhere today? |
|---|---|---|---|
| 1 | Foreign tax credit that needs Form 1116 (Schedule 3 line 1) | i1040gi p. 115, Line 1 | **Yes.** `ftc.needs1116` refuses ("Form 1116"), `forms/2025/ftc.yaml` line 309. |
| 2 | General business credit, Form 3800 (line 6a) | i1040gi p. 116, "usually apply only to individuals who are partners, shareholders in an S corporation, self-employed, or who have rental property" | Partly. Partnerships, S corporations and rentals are refused by `scope.schedule1`. For a business on Schedule C, `sc.special` refuses "wages or benefits reduced by an employment credit (Forms 5884, 8844, 8846, 8932, 8941 or 8994)". Other business credits, and credits carried from earlier years, are caught only here. |
| 3 | Credit for prior-year minimum tax, Form 8801 (6b) | p. 116 | No. |
| 4 | Adoption credit, Form 8839 (6c) | p. 116, "if you paid expenses to adopt a child or you adopted a child with special needs and the adoption became final in 2025" | No. (Employer adoption benefits are refused by `scope.other_income`.) |
| 5 | Refundable adoption credit (Form 1040 line 30) | i1040gi p. 61, Line 30 | No. |
| 6 | Credit for the elderly or the disabled, Schedule R (6d) | p. 116 | No. |
| 7 | Clean vehicle credit, new vehicle, Form 8936 (6f) | p. 116, "the personal use part of any credit for new clean vehicles" | No. (A repayment of the credit is refused by `s2.other`.) |
| 8 | Mortgage interest credit, Form 8396 (6g) | p. 116, "if a state or local government gave you a mortgage credit certificate" | No. |
| 9 | District of Columbia first-time homebuyer credit, Form 8859 (6h) | p. 116, "only if you have a credit carryforward from 2024" | No. |
| 10 | Qualified electric vehicle credit, Form 8834 (6i) | p. 116, "only if you have an electric vehicle passive activity credit carried forward from a prior year" | No. |
| 11 | Alternative fuel vehicle refueling property credit, Form 8911 (6j) | p. 116 | No. |
| 12 | Credit to holders of tax credit bonds, Form 8912 (6k) | p. 116 | No. |
| 13 | Form 8978 amount (6l): a partner's share of a partnership audit | p. 116; i8978 p. 2, "Every partner ... that receives a Form 8986 ... must file Form 8978" | **Yes.** `scope.other_line16` lists "a Form 8978 amount" and refuses. |
| 14 | Credit for previously owned clean vehicles, Form 8936 (6m) | p. 116 | No. |
| 15 | Line 6z, "other nonrefundable credits" | p. 116: "Line 6z. Leave line 6z blank." | Nothing to catch: the line is not used for 2025. |
| 16 | Credit for federal tax on fuels, Form 4136 (line 12) | p. 117; i4136 p. 1 | **Taken as a typed-in amount** by `s3.line12`. |
| 17 | Form 2439 (13a): tax a fund paid on gains it kept | Schedule 3 line 13a | **Yes.** `sd.other_forms` names Form 2439 and refuses (`forms/2025/sd.yaml` line 122). Also taken as a typed-in amount by `s3.line14`. |
| 18 | Credit for repayment of income reported in an earlier year (13b) | p. 117, Line 13b | Taken as a typed-in amount by `s3.line14`. |
| 19 | Net elective payment election amount from Form 3800 (13c) | p. 117, Line 13c | Same. |
| 20 | Deferred net 965 tax liability (13d) | p. 117, Line 13d | Same. `scope.other_line16` refuses a filer who owns stock in a controlled foreign corporation now. |
| 21 | Section 960(c) credit (13z) | p. 117, Line 13z | Same. |
| 22 | Tax allocable to the U.S. Virgin Islands, Form 8689 (13z) | p. 117 | Same. |
| 23 | Deferred tax on a sale of qualified farmland, Form 1062 (13z) | p. 117 | Same. |
| 24 | A credit on the tool's list, in a form the tool does not figure (for example a premium tax credit case the Form 8962 screens refuse) | each form's own screens | Yes, by each form's own questions. Not traced here; outside the slice. |

**Could the tool in fact prepare any of these?** None of the forms behind rows 2 to 14 and 16 to 23 is modelled. Rows 16 to 23 are accepted today as amounts the filer has worked out alone, which is not preparing them.

**Findings.**

1. *Today's interview contradicts itself on Schedule 3 Part II.* `scope.credits` asks about "any credit other than" its list, and its refusal names "Form 1040 lines 30 and 31". A fuel credit, a Form 2439 credit or a repayment credit is such a credit, so a truthful filer answers Yes and is refused at question 4. Yet `s3.line12` and `s3.line14` exist to accept exactly those amounts. A filer who gets past question 4 by reading it narrowly is asked for them 43 questions later.
2. *The closed list is shorter than the intent document says.* Schedule 3 Part I prints twelve named credits beyond lines 1 to 5 (6a to 6d and 6f to 6m; 6e is reserved) and one "other" line, 6z, which the instructions say to leave blank. Part II prints line 12, four named lines 13a to 13d, and 13z, for which the instructions name three uses. The intent document's "14 named credits and two 'other' lines" was read from the form alone.
3. *Four rows are already refused elsewhere* (1, 13, 17, and part of 2). A filer in those situations is asked twice.
4. *The owner's notes say `scope.credits` is read by `scope.ready` and eight other lines.* The notes list seven, and the built data has seven.

### A.3 Health savings accounts

There are 18 questions: the roster and 17 inputs. Together they are 1,696 words. All are asked once per person who has an HSA, and each begins with the 12-word frame "For this person (you, or your spouse on a joint return) — ", which is included in the counts.

| Id | Type | Words | When asked | What the answer does |
|---|---|---|---|---|
| `$f8889` | Roster with two fixed choices, "Yes (one Form 8889 for all of this person's HSAs)" and "No" | 84, options 11, help 11 | Once per person, always | Yes creates the person's one Form 8889 entry. |
| `f8889.unsupported` | Yes/no | 232, help 22 | Every HSA entry, first | Yes refuses Form 8889 line 13 (the deduction) and line 16 (taxable distributions). Message: "Form 8889 Part III, Form 8853, a Form 8889 for a person who died in 2025 (prepare it with the decedent's final return), or other HSA situations". |
| `f8889.line2` | Amount | 96 | Every entry | Own contributions. Deduction is the smaller of this and the limit. |
| `f8889.line9` | Amount | 50 | Every entry | Employer contributions. Reduce the limit. |
| `f8889.coverage_year` | `self_only`, `family` or `changed` | 339, options 26, help 37 | Every entry, even one with no contributions (seen on the walked return with zero contributions and zero distributions) | Sets the yearly limit; `changed` opens the month questions. |
| `f8889.months_eligible` | Count | 58 | When coverage `changed` | Months counted for the limit. |
| `f8889.months_family` | Count | 109 | When coverage `changed` | Months at the family amount. |
| `f8889.dec_coverage` | `none`, `self_only` or `family` | 113, options 22 | When coverage `changed` (formally gated) | December 1 coverage. |
| `f8889.last_month` | Yes/no | 56, help 35 | When covered on December 1 and coverage `changed` (formally gated) | Yes treats the December 1 coverage as held all year. |
| `f8889.age55` | Yes/no | 23 | Every entry | Adds $1,000 to the limit. |
| `f8889.allocation` | `equal` or `agreed` | 57, help 24 | Joint return, both spouses have HSAs, and family coverage at some time | How the spouses divide the family limit. |
| `f8889.allocated` | Amount | 42 | When `agreed` | This person's part. |
| `f8889.employer_in_box1` | Yes/no | 46 | When employer contributions exceed the limit | No refuses ("Excess employer HSA contributions not included in Form W-2 box 1"). |
| `f8889.line14a` | Amount | 54, help 17 | Every entry | Total distributions. |
| `f8889.rollover` | Amount | 73, help 11 | When distributions are above zero | Subtracted. More than the total refuses (a conflict). |
| `f8889.medical` | Amount | 179 | When distributions are above zero | Subtracted; the rest is taxable. |
| `f8889.line17a` | Yes/no | 35, help 15 | When some distribution is taxable | Whether the 20% additional tax is reduced. |
| `f8889.subject_part` | Amount | 50, help 16 | When `line17a` is Yes | The part still subject to the 20% tax. |

Three of the 17 (`f8889.line2`, `f8889.line9`, `f8889.employer_in_box1`) carry, as their only help, the sentence "Married filing separately and unsupported items are refused with citations." Two (`f8889.age55`, `f8889.dec_coverage`) have no help.

**Order as asked.** The HSA questions are not asked together. On the walked return with a mid-year change of coverage, the roster was question 17; then eleven questions about dividends, withholding, education and foreign tax; then nine HSA questions (29 to 37); then five others; then three HSA questions (43 to 45); then eleven others; then `line17a` (57). The reason is that all but one of them have order number 10, which 144 questions share (the owner's notes), and questions with the same number are sorted by id.

**The ten situations in `f8889.unsupported`, traced.** Page numbers are of the 2025 Instructions for Form 8889 (i8889) unless marked.

| # | Situation, in the question's words | Source that puts it outside the tool | Could the tool prepare it? Is it asked elsewhere? |
|---|---|---|---|
| 1 | "a qualified HSA funding distribution from an IRA in 2025" | p. 7, Line 10: a direct transfer from an IRA; it reduces the limit and starts a 12-month testing period. Line 10 is fixed at zero in the model. | Not prepared. **Also asked elsewhere:** `retirement.special` (per Form 1099-R) lists "a qualified charitable distribution or HSA funding distribution" and refuses. |
| 2 | "contributions by you or your employer to an Archer MSA for 2025 (Form 8853), or, if you or your spouse had family coverage ... any contribution by anyone to your spouse's Archer MSA" | f8889 line 4; p. 4, "Your maximum contribution is reduced by ... any contributions made to your Archer MSA". Line 4 is fixed at zero. Form 8853 is not modelled. | Not prepared. |
| 3 | "excess HSA contributions from an earlier year that remain in your HSA" | p. 8, Prior Year Excess Contributions, "see the Instructions for Form 5329, Part VII, line 43". | Not prepared. **Asked a second time:** `person.x_other`, asked of every person, lists "excess HSA contributions from an earlier year that you had not removed or used up before 2025 ..., whether or not you have a Form 8889 for 2025", and refuses. |
| 4 | "failing to remain an eligible individual during a testing period that began in an earlier year (last-month rule or qualified HSA funding distribution)" | p. 9, Part III (lines 18 to 21, not modelled); p. 2, Testing period. | Not prepared. **Settled for most by another answer:** a testing period that began in 2024 ends in 2025, so a person who was an eligible individual on the first day of every month of 2025 cannot have failed it. That is exactly what the answers "Self-only all year" and "Family all year" to `f8889.coverage_year` say. Also listed in `s2.other` ("the additional tax on an HSA you did not keep as an eligible individual"). |
| 5 | "an HSA you acquired because of the account beneficiary's death" | p. 3, Death of Account Beneficiary: a beneficiary who is not the spouse reports the account's value as a distribution and skips Part I. | **Partly, yes.** The same passage says: "If the account beneficiary's surviving spouse is the designated beneficiary, the HSA is treated as if the surviving spouse were the account beneficiary. The surviving spouse completes Form 8889 as though the HSA belonged to the surviving spouse." The question has no time limit, so a widow who took over a spouse's HSA years ago is refused every year, though her Form 8889 is an ordinary one. This is a finding. |
| 6 | "the HSA of a person who died in 2025 whose estate is the beneficiary" | p. 3: the value at death goes on the account owner's final return. | Not prepared. It is a case of situation 10: the return it belongs on is the final return of a person who died in 2025. |
| 7 | "a deemed distribution from an HSA in 2025 (a prohibited transaction, or any part of an HSA used as security for a loan)" | p. 3, Deemed Distributions From HSAs. | Not prepared. |
| 8 | "a withdrawal of excess contributions or their earnings, made in 2025 or in 2026 by the due date of your 2025 return" | p. 8, Excess Contributions You Make, and Line 14b. The model's line 14b takes rollovers only. | Not prepared. |
| 9 | "a mistaken distribution you repaid to your HSA" | p. 9, Note under Lines 17a and 17b; Form 1099-SA, Instructions for Recipient. | Not prepared. |
| 10 | "this person died in 2025 ..." | p. 2, Last-month rule, "the 1st day of the last month of the tax year (December 1, for most individuals)"; i1040gi p. 12, Death of a Taxpayer. The model takes December as the last month. | Not prepared. The interview has no single "did this person die in 2025" fact; it is asked in five other places for other forms (`household.spouse_died_2025`, `f2441.spouse_died`, `eic.died_2025`, `clcw26.final_return`, `person.died_before_65`). |

**Findings.**

5. *One situation is missing from the catch-all.* Money moved from an Archer MSA into an HSA is a rollover (i8889 p. 3, "from one HSA or Archer MSA"), and money paid out of an Archer MSA requires Form 8853 whatever it was used for (i8853 p. 1, Who Must File). The catch-all names only *contributions* to an Archer MSA. I found no other question that catches a tax-free Archer MSA payout (searched every question's text for "Archer" and "8853"; `s1.line8_other` names only taxable "income from Form 8853").
6. *The roster question is itself a catch-all.* At 84 words it names a qualified HSA funding distribution, Form 1099-SA, a testing period, Form 8889 Part III and an acquired interest. The owner's notes do not mention it, because he answered it without stopping; a filer without the vocabulary would stop.
7. *A dormant account can hide two situations.* The roster asks whether money went in or came out. A person whose HSA had no activity in 2025 answers No, and is then never asked about a loan secured on it (situation 7).
8. *The coverage question is asked of people it cannot affect.* A person with distributions and no contributions has no limit to figure, but reads the 339 words because the excess-contribution line reads the limit unconditionally.

---

## B. The redesigned question trees

How to read the tables. **Asked when** names what gates the question. **Words** counts the question text, then the options. A question marked *refuses* stops the return on Yes. Ids are proposals; none carries a year.

Every question was written to be read by a person holding their papers and knowing no tax terms. A tax term appears only where it is printed on a paper the person holds (a form number, a box number, a word such as "Archer MSA" printed next to a checkbox), or in parentheses after the plain words, so that a person who does know the term can find it.

### B.1 The opening

| # | Id | Question and options | Asked when | Words |
|---|---|---|---|---|
| O1 | `$person` (existing roster, reworded) | **Who is this tax return for?** <br>• Just me <br>• Me and my husband or wife, together on one return | First, always | 6 + 12 |
| O2 | `f1040.status` (existing input, reworded, options labelled) | **Which of these fits you on December 31, 2025?** <br>• Married, and filing apart from my husband or wife (married filing separately) <br>• I paid over half the cost of the home of my child, or of a relative I support (head of household) <br>• Widowed in 2023 or 2024, not remarried, and my child lived with me all of 2025 (qualifying surviving spouse) <br>• None of these: I was not married (single) | Only after "Just me". After "together" the status is already recorded. | 9 + 60 |
| — | `person.role` | Not asked. The O1 choice records it. | — | 0 |

Help for O1: "Choose “together” only if you are married and you are both putting your income on this one return. If your husband or wife died during 2025, you can still choose “together”. If you are married but each of you files a separate return, choose “Just me”." (46 words. Today's help about where Forms W-2 are entered moves to the W-2 question.)

Help for O2: "Take the first line that is true for you. If you pick one of the lines about a child or relative, later questions check the details (who lived with you, for how long, who paid for the home). If they do not fit, you will be told, and you can come back and choose again." (55 words)

The fifth status, married filing jointly, is not among the options: a person who chose "Just me" cannot file jointly, and a couple who chose "together" is not asked.

**A variant with fewer options (not recommended for the slice; see E.3).** Ask the existing question "Were you married on December 31, 2025?" second, and then show only the statuses that answer allows: two for a married person (38 words with the question), three for an unmarried one (49 words). It reads better and costs a change to the model.

Section E explains the choices made here and what they need.

### B.2 Credits: no screen; questions at their topics

Each row is one question: eight asked of everyone, two follow-ups (C1a, C4a), and two asked once per business (C5, C6). All are yes/no. There is no top "credits" question, because a filer does not know that these things are credits; each is asked as a fact, where its topic comes up.

| # | Id | Question | Asked where, and when | On Yes | Words |
|---|---|---|---|---|---|
| C1 | `s3.ev_bought` | **In 2025, did you buy an electric, plug-in hybrid or fuel-cell vehicle, new or used, or put in a charger for one?** | With the car questions (next to `s1a.carloan`), always | Asks C1a | 22 |
| C1a | `s3.ev_credit` | **Did you get a tax credit for it at the dealer, or do you want one on this return?** Help: "A dealer may have taken the credit off the price; that still has to be reported on the return." | Only after C1 Yes | *Refuses*: "This tool does not prepare the clean vehicle credits (Form 8936) or the charger credit (Form 8911)." | 19 |
| C2 | `s3.adoption` | **Did you adopt a child, or pay costs toward adopting one, in 2025?** | With the dependents questions, always | *Refuses*: "You may be entitled to the adoption credit (Form 8839), which this tool does not prepare." | 13 |
| C3 | `s3.mcc` | **Do you have a “mortgage credit certificate” from a state or local housing agency for your home loan?** Help: "It is a paper issued when the loan was made, usually to first-time buyers. Most home loans do not have one." | With the home mortgage interest question (`sa.line8a`), always | *Refuses*: "The mortgage interest credit (Form 8396) changes both your credits and your mortgage interest deduction; this tool does not prepare it." | 18 |
| C4 | `person.disability_retired` | **Have you retired on permanent and total disability?** | Per person, next to `person.age65`; only when that answer is No | Asks C4a | 8 |
| C4a | `person.elderly_credit` | **Do you want to claim the credit for the elderly or the disabled (Schedule R)?** Help: "Asked because you are 65 or older, or retired on disability. The credit is only for people with low income. This tool cannot figure it; answer No to go on without it." | Per person; only when 65 or older, or C4 Yes | *Refuses* | 15 |
| C5 | `sc.business_credit` | **Does this business claim any business tax credit, for example for research, for starting a retirement plan, or for making the premises accessible?** | Per business (Schedule C), with `sc.special` | *Refuses*: "Business credits (Form 3800) are outside this tool." | 23 |
| C6 | `sc.fuel_credit` | **Did this business use gasoline, diesel or another taxed fuel off the road, such as in equipment or a boat, and want the federal fuel tax back?** | Per business | *Refuses* (or asks for the Form 4136 amount; decision 3) | 27 |
| C7 | `s3.prior_forms` | **Does your 2024 federal return include any of these forms: 3800, 8396, 8801, 8834, 8839 or 8859?** Help: "Each can leave a tax credit to carry into 2025 (business credits, a mortgage credit certificate, alternative minimum tax paid earlier, an electric vehicle from before 2007, an adoption, a first home in Washington, D.C.). The form number is printed at the top left of each page. If you did not file for 2024, the answer is No." | With the other "from last year's return" questions (`sd.carryover`, `refund.received`), always | *Refuses*: "A credit carried over from an earlier year is outside this tool." | 17 |
| C8 | `s3.repaid_income` | **In 2025, did you pay back more than $3,000 that you had reported as income in an earlier year?** Help: "For example wages, unemployment or benefits that were paid to you by mistake and that you returned." | With the other-income questions, always | *Refuses* (or asks for the amount; decision 3) | 19 |
| C9 | `s3.docs` | **Among your tax papers for 2025, is there a Form 1097-BTC or a Form 8986?** Help: "Form 1097-BTC reports credits from tax credit bonds. Form 8986 comes from a partnership after an audit." | With the interest and dividend papers, always | *Refuses*, naming the form | 15 |
| C10 | `s3.rare_payments` | **Does any of these apply?** <br>• you are paying “section 965” tax on foreign company earnings in yearly installments <br>• part of your tax is owed to the U.S. Virgin Islands (Form 8689) <br>• you claim a refund under “section 960(c)” <br>• you sold farmland and chose to pay the tax on the gain in installments (Form 1062) | With the payments questions, always. Kept as its own separate question: see below. | *Refuses* (or asks for the amount; decision 3) | 58 |

Notes on particular questions.

- **C10 is the one place the design keeps a list.** No fact of an ordinary life leads to these four; a person in one of them was told so by an adviser and will recognise the words. The intent document provides for this: a situation no plain question leads to stays as its own separate question. The list is closed (four items the instructions name for lines 13d and 13z), positive, and has no "other" entry. It is 58 words; I could not make it shorter without dropping an item.
- **C4a is not a plain question**, and it is a child, so it need not be. But a 70-year-old with low income cannot tell whether to "claim" a credit they have never heard of. The honest state is that the tool cannot tell them either: Schedule R and its instructions are not in the archive. Decision 5 offers a better design once they are.
- **C7 asks about papers, not law.** A person can open last year's return and look for six numbers. It replaces six separate "do you have a carryforward of ..." questions that nobody without training could answer.
- **C2 refuses on the fact, not on the wish.** Today a filer is refused only if they "want to claim" the credit. A person who adopted in 2025 and has never heard of the credit would answer No today and get a return without it. The proposed question refuses that person, with a message that tells them why. This is a deliberate widening.
- **What is not asked.** Form 1116, a Form 8978 amount, Form 2439 and employment credits of a business are each already refused by another question (section C). No new question is added for them.

### B.3 Health savings accounts

Asked as one block, in this order, once for each person. On a one-person return the questions are shown with no frame. On a joint return each is shown under "About you" or "About your spouse" (decision 7). Within these questions "you" always means the person named in the frame; the other spouse is "your husband or wife".

| # | Id | Question and options | Asked when | On Yes / effect | Words |
|---|---|---|---|---|---|
| H0 | `$f8889` (existing roster, reworded) | **Did you have a health savings account (HSA) in 2025, or get money from one?** Yes / No | Per person, always | Yes opens the block | 15 + 2 |
| | | *The account* | | | |
| H1 | `f8889.owner_died` | **Did the owner of this HSA die in 2025?** | Every HSA | *Refuses*: "An HSA return for a person who died in 2025 follows special rules (the year ends at the month of death); prepare it with the final return." | 9 |
| H2 | `f8889.inherited` | **Did this HSA come to you from someone who died?** Help: "For example, a parent or a spouse named you as the beneficiary of their HSA." | Every HSA | *Refuses*: "An inherited HSA is reported differently; this tool does not prepare it." | 10 |
| H3 | `f8889.archer` | **Did you, or your husband or wife, have an Archer MSA in 2025?** Help: "An Archer MSA is an older kind of medical savings account; almost none have been opened since 2007. On a Form 1099-SA or 5498-SA for one, the box “Archer MSA” is checked. If you have never heard of it, the answer is No." | Every HSA | *Refuses*: "Archer MSAs (Form 8853) are outside this tool." | 13 |
| | | *Money in* | | | |
| H4 | `f8889.line9` (existing, reworded) | **How much did your employer put into your HSA for 2025, including money taken out of your pay?** Help: "Use the amount in box 12 of your Form W-2 next to the letter W. Take off any part of it that was for 2024, and add anything your employer put in for 2025 after December 31, 2025. Zero if none." | Every HSA | Amount | 18 |
| H5 | `f8889.line2` (existing, reworded) | **How much did you put into your HSA for 2025 yourself, outside your paycheck?** Help: "Count deposits made by you, or by anyone other than your employer, up to April 15, 2026, that were for 2025 (later if you served in a combat zone). Do not count money taken out of your pay, money moved in from another HSA, or money moved in from an IRA. Zero if none." | Every HSA | Amount | 14 |
| H6 | `f8889.ira_transfer` | **Was any money moved into your HSA straight from an IRA in 2025?** | Every HSA | *Refuses*: "A transfer from an IRA to an HSA (a qualified HSA funding distribution) is outside this tool." | 13 |
| H7 | `f8889.excess_withdrawn` | **In 2025, or in 2026 before filing this return, did you take money back out of your HSA because too much had been put in?** Help: "This is called withdrawing excess contributions. Answer Yes also if you plan to do it before the filing deadline." | Every HSA | *Refuses* | 25 |
| | | *Coverage* (asked only when something needs the yearly limit; see F.3) | | | |
| H8 | `f8889.coverage_year` (existing, reworded) | **Was your health plan in 2025 a high-deductible plan that works with an HSA, and the same kind all year?** <br>• Yes, all 12 months, covering only me <br>• Yes, all 12 months, covering me and at least one other person <br>• No: it started, stopped or changed during 2025, or I am not sure | H4 or H5 above zero; or both spouses have HSAs; or H14 Yes | Sets the limit, or opens H10 to H13 | 20 + 32 |
| H9 | `f8889.clear_all_year` | **In every month of 2025, were all three of these true?** <br>• you were not enrolled in Medicare <br>• you had no other health coverage that pays medical bills (dental, vision, accident, disability and long-term care insurance do not count) <br>• nobody could claim you as a dependent <br>Help (68 words): what other coverage counts and what does not; "If you are not sure, answer No; the month-by-month questions follow." | H8 answered with either Yes | No opens H10 to H13, as if H8 were "No" | 48 |
| H9a | `f8889.spouse_family` | **In any month of 2025, did your husband or wife have a high-deductible plan covering more than one person?** | H8 "covering only me", H9 Yes, and married (`household.married`) | Yes opens H10 to H13 | 19 |
| H10 | `f8889.months_eligible` (existing, reworded) | **On the first day of how many months of 2025 were you covered by an HSA-qualifying plan, with all three of these true?** (the same three lines) | Year not uniform | Count | 45 |
| H11 | `f8889.months_family` (existing, reworded) | **In how many of those months did your plan cover more than one person?** Help: "Count a month also if you were covered by someone else's family plan, or if you were married, you could both have HSAs, and either of you had family coverage. Zero if your plan covered only you in all of them." | Year not uniform | Count | 14 |
| H12 | `f8889.dec_coverage` (existing, reworded) | **What did you have on December 1, 2025?** <br>• No HSA-qualifying coverage that day <br>• A plan covering only me <br>• A plan covering me and at least one other person | Year not uniform | | 8 + 20 |
| H13 | `f8889.last_month` (existing, reworded) | **You were covered on December 1 but not for all of 2025. Do you want to be treated as covered all year?** Help (57 words): the last-month rule, the condition to stay covered through December 31, 2026, and "If you put in no more than your covered months allow, answer No." | Covered on December 1, year not uniform | | 22 |
| H14 | `f8889.testing_2024` | **For 2024, did you put in a full year's amount although you were covered only part of 2024, or move money from an IRA into your HSA during 2024?** Help: "Both moves came with a condition: to stay covered by an HSA-qualifying plan for a further 12 months." | Only when the answers so far do not show cover in all 12 months of 2025: H10 below 12, or no 2025 contributions (so coverage was not asked). In the second case a Yes makes H8 to H10 follow. | *Refuses* when Yes and not covered in all 12 months: "Income and additional tax for not staying covered (Form 8889 Part III) are outside this tool." | 29 |
| H15 | `f8889.age55` (existing, reworded) | **Were you 55 or older on December 31, 2025?** | When the limit is needed (as H8) | | 9 |
| H16, H17 | `f8889.allocation`, `f8889.allocated` (existing, reworded) | **You and your spouse both have HSAs and share one family limit. How do you split it?** Half each / A different split we both agree on. Then: **How much of the shared family limit is yours?** | As today | | 17 + 9; 9 |
| H18 | `f8889.employer_in_box1` (existing, reworded) | **Your employer put more into your HSA than your limit. Is the extra included in box 1 of your Form W-2?** | As today | No *refuses*, as today | 21 |
| | | *Money out* | | | |
| H19 | `f8889.line14a` (existing, reworded) | **How much came out of your HSA in 2025 in total?** Help: "Add box 1 of all your 2025 Forms 1099-SA. This includes payments made straight to a doctor or pharmacy with the HSA card. Do not count money the bank moved directly into another HSA of yours. Zero if none." | Every HSA | Amount | 11 |
| H20 | `f8889.dist_code` | **Does box 3 of any of your 2025 Forms 1099-SA show a number other than 1 or 3?** Help: "Box 3 is the “distribution code”. 1 is an ordinary payment and 3 a payment after disability. 2 means excess contributions taken back, 4 or 6 a payment after a death, and 5 a prohibited transaction." | H19 above zero | *Refuses*, naming what the code means | 18 |
| H21 | `f8889.rollover` (existing, reworded) | **How much of that did you put back into another HSA of your own within 60 days?** | H19 above zero | Amount | 17 |
| H22 | `f8889.mistake_repaid` | **Was any money paid out of your HSA by mistake and later put back?** | Every HSA | *Refuses* | 14 |
| H23 | `f8889.medical_all` | **Did all of the money that came out pay for doctor, dental, vision, hospital or pharmacy costs of you, your husband or wife, or your dependents?** Help: "Answer No if any of it paid for insurance premiums, for someone else (such as an adult child you do not claim), for costs from before you opened the HSA, or for costs that insurance paid back to you." | H19 above zero | Yes: nothing is taxable; H24 to H26 are skipped | 26 |
| H24 | `f8889.medical` (existing; its 179 words kept, laid out as a list) | **How much of it paid for medical costs that count?** followed by the full rules as bullets: whose costs; after the HSA was opened and not paid back; the four kinds of premium that count. | H23 No | Amount | 10 + the rules |
| H25, H26 | `f8889.line17a`, `f8889.subject_part` (existing, reworded) | **Was any of the money not spent on medical costs taken out after you turned 65 or became disabled?** Then: **How much of it came out before you turned 65 or became disabled?** | As today | | 19; 13 |
| | | *Dealings with the account* | | | |
| H27 | `f8889.loan` | **In 2025, did you use your HSA as security for a loan, borrow from it, lend to it, or buy from or sell to it yourself?** | Every HSA | *Refuses*: "These count as taking money out of the HSA (a deemed distribution); this tool does not prepare that." | 26 |

Notes.

- **Where the precision went.** Today's coverage question holds, in 339 words, three things: the three-way choice, the definition of an "eligible individual", and the rules for when a month counts as family coverage. In the tree the choice is H8 (short), the definition is H9 (a child, asked only of those who said "all year"), the married-couple rule is H9a (asked only of married people who said "only me"), and the remaining family rules are in the help of H11, where they are needed. A person whose year was uniform never reads the month rules.
- **H23 is Idea A applied to an amount.** Most people spend their HSA on medical bills and nothing else. They answer one 26-word question instead of reading 179 words to type the same number they typed a moment before.
- **H20 uses a paper the person holds.** Form 1099-SA prints a code in box 3. Reading a number off a form needs no vocabulary, and it catches three of the ten situations at once (Form 1099-SA, Instructions for Recipient, box 3: "1—Normal distribution; 2—Excess contributions; 3—Disability; 4—Death distribution other than code 6; 5—Prohibited transaction; 6—Death distribution after year of death to a nonspouse beneficiary"). The plain questions H2, H7 and H27 remain for the cases where no form shows it.
- **Order numbers.** The block needs its own run of consecutive order numbers in the question bank; today 17 of the 18 share number 10 or 11 with unrelated questions. The order of the interview as a whole is outside the slice; the block only has to be contiguous.
- **Top questions that are longer than a sentence or two:** H9 (48 words) and H10 (45), because each must carry the three conditions as a list; C10 (58), discussed above. Everything else is 29 words or fewer.

---

## C. Coverage: every situation covered today, and its path

This is the proof of "airtight underneath". One row per situation from section A. **Path** is the sequence of plain questions a person in that situation answers. **Caught at** is where the tool learns of it. No row is dropped.

Where a row says an existing answer settles the situation, the answer and the lines are named, and the claim was checked against the built form data (file given). Those rows add no question.

### C.1 The opening

The opening has no catch-all, but it has checks, and all are kept.

| Situation | Path | Caught at | What happens |
|---|---|---|---|
| Married, filing together | O1 "together" | O1 | Two entries, roles and status `mfj` recorded. `household.roster_bad` and `household.filing_status_conflict` still run. |
| Filing together, spouse died in 2025 | O1 "together" → existing `household.married` No → existing `household.spouse_died_2025` Yes | existing check | Accepted, as today. |
| Filing together, not married, no death | O1 "together" → `household.married` No → `household.spouse_died_2025` No | `household.filing_status_conflict` | Conflict shown, as today. |
| Married, filing a separate return | O1 "Just me" → O2 first option | O2 | Refused as soon as the option is chosen, as today (checked by answering `mfs` in the built interview: the return is refused at once, gate `s3.mfs`, "The rules for a married filing separately return ... are outside this tool. Married filing jointly is supported."). |
| Married, living apart, child at home (may be head of household) | O1 "Just me" → O2 second option | existing `household.unmarried`, `household.home_cost`, dependent tests | As today: accepted if the tests are met, else `household.hoh_fails`. |
| Unmarried with a child or supported relative | O1 "Just me" → O2 second option | same household questions | As today. |
| Widowed in 2023 or 2024 with a child | O1 "Just me" → O2 third option | existing `household.qss_eligible` | As today. |
| Unmarried, none of these | O1 "Just me" → O2 last option | — | Single. |
| Married, picks "None of these" | O1 "Just me" → O2 last option → existing `household.married` Yes | `household.filing_status_conflict` | Conflict shown, as today. |
| Spouse died in 2025, filing alone | O1 "Just me" → O2 any → existing `household.spouse_died_2025` Yes | `household.widowed_2025` | Refused, as today, with today's message (file jointly with the deceased spouse, or separately, which the tool does not support). |
| Wrong entries (two taxpayers, a spouse without joint status) | Cannot be produced through the interview; possible only with typed-in inputs | `household.roster_bad` | Kept, as today. |

### C.2 Credits (the 24 rows of A.2, three of them split: 29 rows)

| # | Situation | Path of plain questions | Caught at | What happens |
|---|---|---|---|---|
| 1 | Foreign tax credit needing Form 1116 | The existing foreign tax questions (`ftc.taxes` and the four that follow) | `ftc.needs1116` | **Settled by existing answers.** Refused: "Form 1116". Checked: `forms/2025/ftc.yaml` line 309. |
| 2a | Business credit of a business on this return, other than the employment credits | Has a business → C5 | C5 | Refused. |
| 2b | Employment credit of a business on this return (Forms 5884, 8844, 8846, 8932, 8941, 8994) | Has a business → existing `sc.special` | `sc.special` | **Settled by an existing answer.** Checked: the built text of `sc.special` names all six forms. |
| 2c | Business credit through a partnership, S corporation or rental | Existing `scope.schedule1` | `scope.schedule1` | **Settled by an existing answer** (those activities are refused whole). That screen is outside the slice. |
| 2d | Business credit carried from an earlier year | C7 (Form 3800 in the 2024 return) | C7 | Refused. |
| 3 | Credit for prior-year minimum tax | C7 (Form 8801) | C7 | Refused. |
| 4 | Adoption credit, adoption in 2025 | C2 | C2 | Refused. Wider than today: refused on the fact, not on the wish to claim (B.2). |
| 4b | Adoption credit carried from an earlier year | C7 (Form 8839) | C7 | Refused. |
| 5 | Refundable adoption credit (Form 1040 line 30) | C2 | C2 | Refused. |
| 6 | Credit for the elderly or the disabled | Existing `person.age65` Yes, or C4 Yes → C4a | C4a | Refused if wanted. |
| 7 | Clean vehicle credit, new vehicle | C1 → C1a | C1a | Refused. |
| 8 | Mortgage interest credit, current year | C3 | C3 | Refused. Slightly wider than today: a certificate holder who does not want the credit is refused too. |
| 8b | Mortgage interest credit carried forward | C7 (Form 8396) | C7 | Refused. |
| 9 | D.C. first-time homebuyer credit (carryforward only) | C7 (Form 8859) | C7 | Refused. |
| 10 | Qualified electric vehicle credit (carryforward only) | C7 (Form 8834) | C7 | Refused. |
| 11 | Charger credit (alternative fuel vehicle refueling property) | C1 ("or put in a charger for one") → C1a. For a business: C5. | C1a or C5 | Refused. |
| 12 | Tax credit bonds | C9 (Form 1097-BTC) | C9 | Refused. |
| 13 | Form 8978 amount | C9 (Form 8986) | C9; also existing `scope.other_line16` | Refused. Asked here as a paper, so that the row no longer depends on the 196-word line 16 screen. |
| 14 | Credit for a previously owned clean vehicle | C1 ("new or used") → C1a | C1a | Refused. |
| 15 | Line 6z | — | — | Nothing to catch for 2025 (i1040gi p. 116: "Leave line 6z blank"). If a later year uses the line, the year's review of the instructions adds a question. |
| 16 | Credit for federal tax on fuels | Has a business → C6 | C6 | Refused, or amount taken (decision 3). A filer with no business on this return cannot have the credit except through a farm or a partnership, which `scope.schedule1` refuses (i4136 p. 1: Part I, "Information About Your Business", is required of every claimant). |
| 17 | Form 2439 | Existing `sd.other_forms` | `sd.other_forms` | **Settled by an existing answer.** Refused: "Schedule D additional source forms". Checked: `forms/2025/sd.yaml` line 122 and the built question text. |
| 18 | Credit for repayment of income of an earlier year | C8 | C8 | Refused, or amount taken (decision 3). |
| 19 | Net elective payment election amount (Form 3800) | Has a business → C5; else C7 | C5 or C7 | Refused. |
| 20 | Deferred net 965 tax liability | C10, first item | C10 | Refused, or amount taken (decision 3). |
| 21 | Section 960(c) credit | C10, third item | C10 | Same. |
| 22 | U.S. Virgin Islands tax, Form 8689 | C10, second item | C10 | Same. |
| 23 | Farmland sale, Form 1062 | C10, fourth item | C10 | Same. |
| 24 | A credit on the tool's list in a form it does not figure | Each form's own questions | Each form's screens | Unchanged; outside the slice. |

**Kept as its own separate question:** rows 20 to 23 (C10), because no plain question about a life leads to them.

**What the removal of `scope.credits` needs.** Its seven reading lines keep their refusals, pointed at the new answers (F.2). Nothing that refused before computes now, with one class of exception to state plainly: a filer who answers every new question No but would have answered the old one Yes. Section D is about that filer.

### C.3 Health savings accounts (the ten situations of A.3, one of them split, and two more: 13 rows)

| # | Situation | Path of plain questions | Caught at | What happens |
|---|---|---|---|---|
| 1 | Transfer from an IRA in 2025 (qualified HSA funding distribution) | H0 → H6 | H6 | Refused. (Also, as today, `retirement.special` on the IRA's Form 1099-R.) |
| 2 | Archer MSA contributions, own or spouse's | H0 → H3 | H3 | Refused. Slightly wider than today: today the spouse's Archer MSA matters only if one of them had family coverage. |
| 3 | Excess contributions of an earlier year still in the account | Existing `person.x_other`, asked of every person | `person.x_other` | **Settled by an existing answer.** Refused through Form 5329 lines 4 and 49. Checked: the built text of `person.x_other` ("whether or not you have a Form 8889 for 2025") and its two readers. Seen asked on all five walked returns. No HSA question is added. When `person.x_other` is itself taken apart, this item should move into the HSA block. |
| 4 | Failed a testing period that began in 2024 | H0 → (H8 "No", or H9 No) → H10 below 12 → H14; or, with no 2025 contributions, H0 → H14 → H8 to H10 | H14 | Refused. **Settled without a question** for a person covered in all 12 months of 2025 (H8 Yes and H9 Yes, or H10 = 12): the testing period for 2024 runs to December 31, 2025 at the latest (i8889 p. 2, Testing period; p. 7 for an IRA transfer), so that person did not fail it. |
| 5 | HSA acquired because its owner died | H0 (help: "Answer Yes also if you were paid money from the HSA of someone who died") → H2; also H20 (box 3 code 4 or 6) | H2 or H20 | Refused. |
| 6 | HSA of a person who died in 2025, estate is beneficiary | H0 → H1 | H1 | Refused. It is a case of row 10. |
| 7a | Prohibited transaction | H0 → H27; also H20 (box 3 code 5) | H27 or H20 | Refused. |
| 7b | HSA used as security for a loan | H0 → H27 | H27 | Refused. |
| 8 | Excess contributions (or their earnings) withdrawn, in 2025 or in 2026 by the due date | H0 → H7; also H20 (box 3 code 2) | H7 or H20 | Refused. |
| 9 | Mistaken distribution repaid | H0 → H22 | H22 | Refused. |
| 10 | The HSA's owner died in 2025 | H0 → H1 | H1 | Refused. |
| 11 | *(new)* Money moved from, or paid out of, an Archer MSA | H0 → H3 | H3 | Refused. Not covered today (finding 5). Only a person who also has an HSA is reached; an Archer MSA holder with no HSA is outside this block, as today. |
| 12 | *(today's other HSA refusals)* Married filing separately; impossible month counts; excess employer contributions not in box 1; rollover or 20%-tax part larger than its whole | Unchanged | Unchanged | Unchanged. |

**One path that is new.** Today a person whose HSA had no money in or out in 2025 answers the roster No and is never asked about a loan secured on it (row 7b) or a prohibited transaction (7a). H0 asks whether the person *had* an HSA, so these are now reached.

**Rows where the form data, not an assumption, was read:** 3 (`person.x_other` text and readers), 4 (the option texts of `f8889.coverage_year`: "on the first day of every month of 2025 you were an eligible individual"), 1 (the text and refusals of `retirement.special`), 12 (the `refuses` entries of `f8889.line13_figured`, `f8889.line14b`, `f8889.subject_excepted`).

---

## D. Who could answer No wrongly

A plain question is easier to answer wrongly than a precise one. For each question asked of people outside its category, this section names the three most plausible people who would answer it wrongly, how likely that is, and what the design does. Where a gap is found, the remedy is a child question, a separate question, or a stated residual; no top question is lengthened.

Frequencies are from `interview/2025/gate_frequencies.yaml` where it has an entry, and are its estimates (several are judgments, as that file says). "No estimate" means the file has none.

**One fact shapes the whole credits half.** A credit only lowers tax. A filer who wrongly answers No to a credits question gets a return that is correct as far as it goes and pays too much; the IRS is not shortchanged. That is still a failure of the intent ("a correct return, or told early and clearly"), but it is a different kind from an HSA question answered wrongly, where income can go unreported. The HSA half is therefore held to the stricter standard.

### D.1 The opening

**O1, who is this return for.** Share answering "together": 34% (the file's joint returns, within its `married` entry).

1. *A married person whose spouse has no income* thinks the return is "just mine". They choose "Just me" and then meet four options, of which only "Married, and filing apart" is true of them. **Remedy:** that option's refusal message says "If you and your spouse are putting, or could put, your income on one return, go back and choose 'together'; a couple can file together even if only one had income" (i1040gi p. 13, "even if only one had income"). No lengthening of O1; its help already says it.
2. *An unmarried couple living together* chooses "together". The existing `household.married` No, then `household.spouse_died_2025` No, then the existing conflict. **Remedy:** none needed; the conflict message is today's.
3. *A person whose spouse died in 2025* chooses "Just me" out of habit, then "None of these"; the existing `household.spouse_died_2025` Yes refuses with today's message, which tells them to file jointly. Share: 0.6% (`spouse_died`). **Remedy:** existing; adequate.

**O2, which of these fits you.** No estimate for head of household or qualifying surviving spouse in the file.

1. *A single parent who has never heard of "head of household"* is the person the question is written for. The option describes their home, not the term, and stands above "None of these". Risk: they pay most of the costs but share a home with their own parent, are unsure whether they "paid over half", and take "None of these". Result: a correct return at single rates, with more tax than necessary. **Remedy:** an accepted residual in this slice, because the cure (asking the household facts of every unmarried filer with a dependent, and offering the better status) belongs to the household section; see E.3.
2. *A person supporting a parent who lives elsewhere.* The option says "the home of my child, or of a relative I support"; it does not say "my home", because a parent need not live with the filer (i1040gi p. 14, Test 1). They may still read it as their own home. **Remedy:** the existing child question `dependent.parent_home_paid` is where the precision is; the option's wording is the best short form I found. Residual, same kind as 1.
3. *A divorced parent whose child lives with them but is claimed by the other parent* believes that without the dependent they cannot use the status (they can: i1040gi p. 14, Test 2, item 4). They take "None of these". **Remedy:** residual, same kind.

In the other direction, a person who picks head of household or qualifying surviving spouse wrongly is caught by the existing household questions and refused with today's messages. Nothing wrong gets through; the cost of the plain wording falls only on people who under-claim.

### D.2 Credits

**C1, a vehicle or charger.** Share Yes: 0.8% (`clean_vehicle`).

1. *A person who leased an electric car.* They did not "buy", and answer No. As I understand the rule a lessee has no credit of their own, so No is right; the Form 8936 instructions are not in the archive to confirm it (decision 6).
2. *A person who bought in 2024 and got the car in 2025*, or ordered in 2025 and received it in 2026. "In 2025, did you buy" is read as the purchase date, and the credit may turn on the delivery date instead. **Remedy:** a child cannot help someone who answered No. Residual, small; it cannot be sized, and the Form 8936 instructions are not in the archive to check which date counts (decision 6).
3. *A person who bought a plug-in hybrid and does not think of it as "electric".* The question names "plug-in hybrid" for this reason.

**C2, adoption.** Share Yes: 0.3% (`adoption`, which covers six years; one year is less).

1. *A person whose adoption became final in 2025 but who paid the costs in 2023 and 2024.* They "adopted a child in 2025": Yes. Covered.
2. *A person who paid costs in 2024 for an adoption not yet final.* As I understand the rule, the credit for such costs is taken the year after they are paid; this person did not adopt or pay in 2025, so answers No. **Remedy:** this cannot be closed by C7 either (no Form 8839 was filed for 2024). It needs a child of a broader top question, for example "Have you been in the process of adopting a child at any time since 2020?" I have not written it, because the timing rule is in the Form 8839 instructions, which are not archived. Residual until then (decision 6).
3. *A stepparent adoption.* Yes, and refused, though (as I understand it) the credit does not apply to a spouse's child. An over-refusal of a rare case; the precise child would release it. Same dependency on the unarchived instructions.

**C3, mortgage credit certificate.** Share Yes: 0.4% (`agency_home_purchase`, which is broader).

1. *A buyer who signed many papers at closing and does not remember one.* The help says most loans do not have one; a holder was told the certificate saves tax every year, and the lender's yearly statement often mentions it. Residual; under-claims only.
2. *A person who refinanced and whose certificate was reissued.* Still "has" one: Yes.
3. *A person who confuses it with the yearly Form 1098.* They answer Yes and are refused wrongly. **Remedy:** the help ("a paper issued when the loan was made, usually to first-time buyers"); the refusal message repeats it, so they can go back.

**C4, retired on permanent and total disability.** No estimate.

1. *A person receiving Social Security disability* who never "retired" from a job. As I understand Schedule R, the credit needs taxable disability income from an employer plan, so No is harmless; Schedule R is not in the archive to confirm it.
2. *A person who stopped work for disability and thinks of it as "leave".* Under-claims only.
3. *A veteran with a disability rating* answers Yes, reaches C4a, and can answer No there.

**C7, forms in the 2024 return.** Prior-year minimum tax credit: 0.07% of returns (the file's `equity_comp_or_amt` note). Others: no estimate.

1. *A person whose 2024 return was prepared by software and who has only a summary.* They cannot look. **Remedy:** the help says where the number is printed; a person who cannot find the return answers No and under-claims.
2. *A person who paid alternative minimum tax in 2023 and whose 2024 return did not include Form 8801.* The credit still exists. Residual; no archived source describes the form's filing rule.
3. *A person who did not file for 2024* but has a credit from 2023. Same.

**C8, repaid more than $3,000.** Share: 0.5% (`repayment`).

1. *A person who repaid unemployment benefits.* Caught earlier by the existing `s1.uc_unsupported`.
2. *A person who repaid $2,500.* No, correctly: the choice between a deduction and a credit exists only above $3,000 (Pub. 525 p. 36, "Repayment over $3,000").
3. *A person who repaid a signing bonus to a former employer* thinks of it as a debt, not income. The help's example ("wages ... paid to you by mistake") does not fit them well. **Remedy:** add "or a bonus you had to return" to the help's examples; the question stays as it is.

**C9, two papers; C10, four rare payments.** No estimates. These ask whether a named paper or a named arrangement exists; the person who has one has been told its name. The wrong No is a person who has not opened their mail. C10's first item has a known false-no (a person who sold the foreign shares but is still paying the installments; the false-no review calls it L-29); the item is worded as "you are paying", not "you own", for that reason.

**C5 and C6, per business.** Asked only of people who have entered a business. The plausible wrong No to C5 is an owner who does not know that an accountant claimed a credit last year; under-claims only.

### D.3 Health savings accounts

**H0, did you have an HSA or get money from one.** Share Yes: 11% (`hsa`; the file calls the estimate weak).

1. *An employee whose employer opened an HSA and put money in, who has never used it.* They may not know it is theirs. **Remedy:** a separate cue at the W-2, where the evidence is: when the W-2 questions are redesigned, "Does box 12 show the letter W?" should be asked there, and a Yes should make H0 unnecessary. In this slice the help of H0 names box 12 code W. Residual until then: this is the largest false-no in the slice. The consequence is real: Form 8889 is required whenever an employer contributed (i8889 p. 1, Who Must File), and employer money above the limit is taxable.
2. *A person who confuses an HSA with a flexible spending account* answers Yes and meets questions that do not fit. The help separates the two; H4 will come out zero and nothing wrong results.
3. *A person who closed the account in January.* "In 2025" covers it; the payout is a distribution and they "got money from one".

**H1 to H3, the account.** H1 and H2 turn on a death, which no one overlooks. H3: a wrong No needs a person who has an Archer MSA and does not know its name; the name is printed on its statements.

**H6, money from an IRA.** A person who did this arranged it deliberately with two institutions. Backstop: the IRA's Form 1099-R, where `retirement.special` asks again.

**H7, took money back.** Wrong No: a person whose bank "corrected" an over-deposit without their asking. **Backstop:** H20, the box 3 code 2 on the Form 1099-SA the bank then issued.

**H8 and H9, coverage.** These are the questions where a wrong answer changes tax. The three most plausible:

1. *A person who turned 65 in 2025 and whose Medicare started without their doing anything.* H8 "Yes, all 12 months" (the employer plan did not change). H9 asks about Medicare in so many words; this is why H9 exists as a separate child and is not folded into H8's help.
2. *A person whose spouse has a general-purpose health FSA at work.* It counts as other coverage for both. H9's question says "no other health coverage that pays medical bills"; the FSA is in the help, not the question. **This is a real gap in the short form.** Remedy, per the intent: a child, not a longer H9. Proposed child `f8889.fsa` (yes/no, asked after H9 Yes): "Did you or your husband or wife have a health FSA or HRA at work in 2025 that pays ordinary medical bills?" I have left it out of the tree and the counts so the owner can see the choice; I recommend adding it (20 words, asked of all contributors).
3. *An adult child on a parent's family plan who opened their own HSA.* H8: "covering only me"? No: the plan covers the family, so "me and at least one other person" is right, and gives the family limit, which is what the instructions give (today's text: "including as a member of someone else's plan"). The option wording leads there. The other trap is H9's third line: can a parent claim them? They may not know. "If you are not sure, answer No" sends them to the month questions, which ask again; the uncertainty is not resolved by any wording.

**H23, did all of it pay medical costs.** A wrong *Yes* is the risk here: tax on the rest is lost.

1. *A person who paid health insurance premiums from the HSA.* Named first in the help. If the reader test shows people say Yes anyway, the remedy is a child ("Did any of it pay insurance premiums?"), not a longer H23.
2. *A person who paid a domestic partner's or adult child's bills.* Named in the help.
3. *A person who reimbursed themselves for bills from before the HSA existed.* Named in the help.

**H22 and H27** ask about events a person would remember. **H14** is asked only of people with a gap in 2025; its wrong No is a person who does not know they relied on the last-month rule for 2024 (their software applied it). Residual; the same person would not have recognised today's wording either.

### D.4 Summary of what the design does about each gap

| Gap | Remedy |
|---|---|
| Employer-opened HSA the filer does not know about | Separate question at the W-2 (outside this slice); help cue now. Residual. |
| Spouse's health FSA | Child question `f8889.fsa` (recommended; not yet in the counts). |
| Premiums paid from the HSA | Help now; child if the reader test shows the error. |
| Adoption costs paid in an earlier year, adoption not final | Needs the Form 8839 instructions; residual until archived. |
| Under-claimed head of household | Residual in this slice; cure belongs to the household section. |
| Carried credits with no form in the 2024 return | Residual; under-claims only. |
| Repaid bonus | One example added to the help of C8. |

---

## E. The opening, specifically

### E.1 The problem in one sentence

For a couple filing together, the model holds one fact in three inputs: the list of people (`$person`), each person's role (`person.role`), and the filing status (`f1040.status`). Today the interview asks all three, so the filer says the same thing three or four times and can contradict themselves.

The model is not wrong to hold them separately. A return typed in directly (the `eval` command, the fixtures) needs each. The question is only how the *interview* fills them.

The obstacle is a rule the interview obeys today: **the interview sets no input**. Every value in the answer log is one the filer gave, and each choice label maps to exactly one value. The `interview-rules` check enforces it (`engine/src/interview-rules.ts`, "no-input-set"). Any design that stops asking a question whose answer is already fixed must either change the model so the input no longer exists, or restate this rule.

### E.2 What happens to `person.role`: three options

`person.role` is read by 33 lines (34 references; the owner's notes say 35). 502 of the 1,764 fixture cases state it.

**Option 1. The roster choice supplies it (recommended).** The two choices of the "who is this return for" question each carry, in the question bank, the role of each entry they create. Picking a choice writes the roster and the roles to the answer log as ordinary answers, in one step.

- *Model:* no change. `person.role` stays an input; its 33 readers are untouched; so is the Lean evaluator.
- *Fixtures:* none change. *Mutation check:* unaffected (no form line changes).
- *Interview engine:* a choice gains a list of answers it supplies; answering applies them together; changing the choice later replaces them. The page needs no change beyond not showing the role question.
- *Checks:* the "no-input-set" rule is restated: *every value in the log comes from a choice the filer made; a choice's label maps to exactly one roster and one fixed set of supplied answers; a supplied answer must be an input of an entry that choice creates, or be named in a short allow-list in the check* (see E.4 for the one other use). Its self-test gains cases for a choice that supplies a value its label does not state. The build rule "a reachable input has no question in the bank" gains the exception "unless every choice of its roster supplies it".
- *Weighed against the spec:* the spec (4.4) says nothing about how a roster is answered; it is unaffected. The rule's purpose, that the tool never invents an answer, is kept, because the label the filer picked ("Me and my husband or wife") states who the two entries are.
- *Size:* small. One engine file, one check, the bank, their tests.

**Option 2. The model derives it from the entry.** `person.role` stops being an input; a line reads the entry's key (`taxpayer` or `spouse`).

- *Spec:* today "a roster entry's key carries no meaning to the model" (the owner's notes, and how 4.4 is written). This option reverses that for the `person` collection: its keys become a closed set with meaning.
- *Model:* a new kind of expression ("the key of this entry") in the schema, in both evaluators (TypeScript and Lean), in the checker, in the mutation tool's operators and equivalence arguments, and in the return generator.
- *Fixtures:* the 502 cases that state a role lose that input. 13 cases use other keys (`sample`, `second`) and must be rekeyed; the one that tests two taxpayers (`taxpayer`, `second`) can no longer be written and is replaced by a test of an unknown key.
- *Checks:* `interview-rules` pins the slice profiles' fixed filer as `{$person: [taxpayer], person[taxpayer].role: taxpayer}`; that constant changes.
- *Reviews:* the `person` form's transcription, render and class M subjects change.
- *Size:* large, almost all of it outside the interview.

**Option 3. It stays an input, and the interview answers it from the choice.** The question stays in the bank; the engine fills it in by a rule ("for an entry created by a fixed choice, the role is the key").

- *Model, fixtures:* no change.
- *Difference from option 1:* the answer comes from a rule in the engine, not from data attached to the choice the filer read. Either the engine writes answers the log's reader cannot trace to a label, or it does not write them and the log no longer replays to the same return. Both break the "no-input-set" rule more deeply than option 1 does, for the same result.
- *Size:* small, like option 1.

**Recommendation: option 1.** It removes the question at the least cost, changes nothing that carries evidence (model, fixtures, Lean, mutation, reviews), and bends the rule in the narrowest way that can be checked. Option 2 is the right answer only if the owner wants direct evaluation, not just the interview, to stop needing the role; nothing in the intent asks for that.

### E.3 The filing status: asked once, in plain words

**Who needs to be asked.** A couple filing together has already said so. Under option 1, extended by one allow-listed input, the "together" choice also supplies `f1040.status = mfj` (decision 1). Nobody who chose "together" sees the status question.

**What the others are asked.** A person filing alone has one of the four other statuses. The question (O2 in B.1) lists the four as situations, each with its official name in parentheses, in an order that puts the three special ones first and the common one last: a reader who takes the first line that is true lands on the right one.

The option for married filing jointly is withheld from a person who chose "Just me". The page does this by a general rule, not a hand-written condition: it does not offer a value that would trip one of the model's consistency checks given the answers so far (here `household.roster_bad`: one person cannot file jointly). The rule is presentation only; every option offered still maps to exactly one value.

**How a person who does not know "head of household" gets there.** The option does not use the term as its handle. It describes a home: "I paid over half the cost of the home of my child, or of a relative I support", with the term after it for those who know it. The same for qualifying surviving spouse: "Widowed in 2023 or 2024, not remarried, and my child lived with me all of 2025".

**How the opening and the household questions relate.** They keep the relation they have today, stated openly:

- The opening option is the plain top: one line, recognisable, not exact.
- The household questions are the precise layer beneath it. They are asked only of a person who chose that option, as today: for head of household, `household.unmarried`, `household.home_cost` and the per-dependent tests; for qualifying surviving spouse, `household.qss_eligible`.
- If the precise layer says the option does not fit, the tool says so (`household.hoh_fails`, `household.qss_fails`) and the filer chooses again. The two refusal messages should say that in plain words: "Go back to 'Which of these fits you?' and choose another line."

**What this does not fix, and should be decided with the household section.**

- A person who is entitled to head of household and picks "None of these" gets a correct return at a higher tax, and nothing tells them. The cure is to ask the household facts of every unmarried filer who lists a dependent, and then offer the status. That means asking the status *after* the dependents, with the household lines reading the facts before the status. It is a redesign of the household section, which the brief excludes.
- `household.married` (217 words) is still asked later of everyone, including a couple who said "together" (they answer Yes, or No and then "my spouse died in 2025"). It is the next redundancy to remove, and it is a household question.
- `household.qss_eligible` (375 words, five tests in one yes/no) and `household.unmarried` (325 words) are catch-all-shaped and want the same treatment as the HSA catch-all.

The opening proposed here does not stand in the way of any of these.

**The variant: marriage first (decision 2).** If "Were you married on December 31, 2025?" were asked second, the status question could show two options to a married person and three to an unmarried one, by the same withholding rule and the existing check `household.filing_status_conflict`. It reads better. Its cost is in the model:

- `household.married` cannot be asked before the status today. The check that compares them looks at the status first, so the marriage question is not reachable until the status is answered (verified in the built interview: after the first answer `household.married` is not among the pending questions; after the status, it is). The check would be rewritten to look at the marriage answer first, with two helper lines.
- The check would gain two cases (married and qualifying surviving spouse; not married and filing separately), so that those options are withheld too.
- With the marriage answer read first, a fixture that leaves it unstated gets an unknown where it has a value today. The fixture defaults withhold `household.married` when the status is `mfj` or `mfs`; 94 cases state `mfs`. Those expectations, and the default's withholding condition, would need to change, with the acknowledged affected-cases report that a changed default requires.

I do not recommend it for the slice: it saves 20 to 30 words of options for people filing alone, and it spends evidence in the household form, which is about to be redesigned anyway.

### E.4 The overlap between the roster choice and the status

With the above, the overlap is gone for couples (one answer) and for people filing alone (the status question does not offer "jointly"). The three consistency checks stay in the model; through the interview they can now fire in only three cases: an unmarried pair choosing "together", a married person choosing "None of these", and a wrongly chosen special status.

If the owner declines to let a choice supply the status (decision 1), the fallback is: the status question is asked of everyone, with a fifth labelled option "Married, filing together on one return (married filing jointly)", and a couple clicks it once more. That is one redundant question for a third of filers, still far better than today's unlabelled codes.

---

## F. What changes in the formal model

Conventions followed: ids carry no year; a question asked only under a condition is an input marked `gated_by` a line that is a `choose` on that condition, with a false or zero parameter as its other branch (`engine/src/gates.ts`); a refusal is an entry in a line's `refuses` list with its own message and citation.

**The rule about unknowns.** Section 1 of the interview-rules catalog shows how a line written as "A and B" or "A or B" reads B while A is unanswered, which makes B's question reachable out of turn. **No line proposed here has that shape.** Every new condition is a `choose` on one answer, nested where two answers are needed, in the order the questions are asked; every new refusal is a separate entry in a `refuses` list, which the evaluator reads in order and stops at the first unanswered one (spec 4.7.1). Each part below lists its new lines so this can be checked.

A general point about wording. Each input line keeps two texts, as the build already allows: the line's own wording in the form data (precise, in the instructions' terms, the thing the transcription and render reviews compare with the source), and the interview's wording in the question bank (plain). The bank already overrides a line's wording where "the line does not carry" interview wording (`interview/README.md`, Question data). The redesign uses that mechanism for every question in the slice; it does not make the form data less precise.

### F.1 The opening

| Item | Change |
|---|---|
| Inputs added or removed | None. `$person`, `person.role` and `f1040.status` stay inputs. |
| Lines whose expressions change | None (recommended variant). |
| Questions no longer asked | `person.role` (supplied by the O1 choice). `f1040.status` for couples (supplied by the "together" choice). |
| Question bank | `$person`: new prompt, labels, help, and the answers each choice supplies. `f1040.status`: a prompt and help (it has neither today), a label for each of its five values. `person.role`: entry removed. |
| Interview engine | A choice can supply answers (E.2). The page does not offer a value that trips a consistency check (E.3). |
| Refusal messages | `household.hoh_fails`, `household.qss_fails`: add "go back and choose another line". The married-filing-separately message: add the pointer to "together" (D.1). These are text changes on existing entries; a refusal is compared whole in fixtures, so every case expecting these refusals is re-recorded (mechanical). |
| Fixtures | No inputs change. Cases that expect the three reworded refusals are re-recorded. |
| Mutation check | Unaffected by the inputs. Reworded refusals change the recorded values the mutation run compares against, nothing else. |
| `interview-rules` | "no-input-set" restated as in E.2, with self-test cases. The walk of each fixture must apply the supplied answers when it answers `$person`. |
| Reviews | `f1040.status` has never had a question review (the review left out the three enum questions). It gets one. What it should test is in F.4. |
| Unknowns | No new line. |

Size: **small.** No form line changes. The work is in the interview engine, one check, the bank and the page.

(The marriage-first variant adds: one rewritten line and two helpers in `household.yaml`, two added cases in the check, a changed fixture default, and up to 94 re-recorded cases. Medium.)

### F.2 Credits

**Inputs removed:** `scope.credits`. If decision 3 is "refuse": also `s3.line12` and `s3.line14`, whose lines become zero behind the new refusals.

**Inputs added (all yes/no):**

| Id | Document | Gated by |
|---|---|---|
| `s3.ev_bought` | s3 | — |
| `s3.ev_credit` | s3 | `s3.ev_credit_if_bought` (a `choose` on `s3.ev_bought`) |
| `s3.adoption` | s3 | — |
| `s3.mcc` | s3 | — |
| `s3.prior_forms` | s3 | — |
| `s3.repaid_income` | s3 | — |
| `s3.docs` | s3 | — |
| `s3.rare_payments` | s3 | — |
| `person.disability_retired` | person | `person.disability_if_under65` (a `choose` on `person.age65`) |
| `person.elderly_credit` | person | `person.elderly_credit_if_asked` (a `choose` on the helper `person.elderly_ask`, itself a `choose` on `person.age65` and then on `person.disability_if_under65`) |
| `sc.business_credit` | sc | — |
| `sc.fuel_credit` | sc | — |

**Lines whose expressions or refusals change:**

- `scope.ready` and `s3.line8`: the one `scope.credits` entry is replaced by one entry per situation, each with its own plain message (the messages in B.2). These are the lines whose refusal the filer sees.
- A new helper `s3.other_credit` (yes/no): a chain of nested `choose` lines over the eight return-level answers and a count of the per-person ones, in asking order. It is true when any is true.
- `f1040.line30`, `s8812.clw_a2`, `s8812.clw_a4`, `f8863.clw5`, `f5695.rce_ws2`, `f5695.eehi_ws2`: each keeps its present message and reads `s3.other_credit` where it read `scope.credits`.
- The Schedule C lines that refuse on `sc.special` gain entries for `sc.business_credit` and `sc.fuel_credit`.
- `s3.line15`: if decision 3 is "refuse", it no longer adds `s3.line12` and `s3.line14`.

**Unknowns.** `s3.other_credit` is the only line that combines several answers; it is a nested `choose`, each level on one answer. `person.elderly_ask` likewise. No "and"/"or" over different inputs.

**Fixtures.** 509 of 1,764 cases state `scope.credits` (9 of them Yes). 422 state `s3.line12` and `s3.line14` (4 with an amount above zero).

- The hand-written stage files take unstated inputs from `fixtures/2025/defaults.json`; the new inputs get a default there (No), which needs only the normal tier.
- The class M and mutation files take no defaults: 356 of their cases state `scope.credits` (`classm.json` 248, `mutation.json` 108) and need the new inputs written in. Mechanical work. (The second-family files `classm.deepseek.json` and `classm.gpt.json` state it in 117 more; they are historical.)
- The 9 Yes cases are each rewritten to one named situation. New cases: at least one refused case per new refusal entry (about 14), and one "gate closed" case for each of the three gated inputs.
- If decision 3 is "refuse": the 4 cases with an amount on line 12 or 14 change from a computed line 15 to a refusal.

**Mutation check.** Each new refusal entry and each level of the two chains is a place a mutant can be made; each needs a case that tells the mutant from the original. The cases above are sized for that. Any pinned equivalence argument that names `scope.credits` or `s3.line8` as a premise is un-pinned and re-argued (not counted here).

**`interview-rules`.** Its minimal returns open each existence gate alone; the three new gates join them. Nothing here sets an input.

Size: **medium.** 12 inputs, about 6 helper and gate lines, 10 reading lines edited across 7 forms (scope, s3, f1040, s8812, f8863, f5695, sc) and person. The reviews of those forms are due on the changed lines only (line-scoped reruns).

### F.3 Health savings accounts

**Inputs removed:** `f8889.unsupported`.

**Inputs added:**

| Id | Type | Gated by |
|---|---|---|
| `f8889.owner_died`, `f8889.inherited`, `f8889.archer`, `f8889.ira_transfer`, `f8889.excess_withdrawn`, `f8889.mistake_repaid`, `f8889.loan` | yes/no | — |
| `f8889.dist_code` | yes/no | `f8889.dist_code_if_dist` (a `choose` on the existing `f8889.has_dist`) |
| `f8889.testing_2024` | yes/no | `f8889.testing_if_asked` (a `choose` on the helper `f8889.ask_testing`: a `choose` on the existing `f8889.any`, then on the new helper `f8889.covered_12`) |
| `f8889.clear_all_year` | yes/no | `f8889.clear_if_uniform` (a `choose` on `f8889.coverage_year`) |
| `f8889.spouse_family` | yes/no | `f8889.spouse_family_if_asked` (a `choose` on a helper that takes `f8889.coverage_year`, then `f8889.clear_if_uniform`, then `household.married`, in that order) |
| `f8889.medical_all` | yes/no | `f8889.medical_all_if_dist` (a `choose` on `f8889.has_dist`) |
| (`f8889.fsa`, if the owner accepts D.3) | yes/no | a `choose` on `f8889.clear_if_uniform` |

`f8889.medical`, an existing input, becomes gated: `f8889.medical_if_partial` (a `choose` on `f8889.medical_all_if_dist`).

**Lines whose expressions or refusals change:**

- `f8889.line13` and `f8889.line16`: the one `f8889.unsupported` entry is replaced by entries for `owner_died` and `inherited` (both lines), each with its message.
- `f8889.line4` (Archer MSA contributions, zero today): refuses on `f8889.archer`. `f8889.line10` (funding distributions, zero today): refuses on `f8889.ira_transfer`. These two lines already say in their citations that the catch-all refuses them; the refusal moves onto the line it is about.
- `f8889.line14b`: refuses on `excess_withdrawn`, `dist_code_if_dist` and `mistake_repaid`, before its existing consistency check. `f8889.line16`: also refuses on `loan` and on the new `f8889.testing_failed` (a `choose` on `testing_if_asked`, then on `covered_12`).
- A new line `f8889.coverage` (the three-way value actually used): `coverage_year`, turned to "changed" when `clear_if_uniform` is No or `spouse_family_if_asked` is Yes. A nested `choose`. The four lines that read `f8889.coverage_year` today (`f8889.line3`, `f8889.full_year`, `f8889.bad_months`, `f8889.dec_coverage_if_changed`) read `f8889.coverage`.
- `f8889.line15`: a `choose` on `f8889.has_dist` as today, then on `medical_all`: all medical gives line 14c; otherwise the amount typed in (`medical_if_partial`).
- `f8889.excess_amt`: a `choose` on `f8889.any`; with no contributions it is zero and does not read the limit. This is what stops the coverage questions being asked of a person who only took money out (finding 8).

About 12 new inputs, about 12 gate and helper lines, 10 existing lines edited, in one form of 113 lines.

**Unknowns.** Every helper above is a `choose` on one answer, nested in asking order. The three conjunctions already in this form that the catalog lists (family H1: `f8889.excess`, `f8889.married_family`, `f8889.split`) are untouched by this design and remain on hold with T-276; they should be rewritten in the same change, since the form's reviews will be due anyway.

**Refusal messages.** One per situation, as in B.3, each citing its own passage (the pages in A.3). The single message "Form 8889 Part III, Form 8853, a Form 8889 for a person who died in 2025 ..., or other HSA situations" goes.

**Fixtures.** 565 cases have an HSA entry; 314 state `f8889.unsupported` (9 of them Yes); 350 state `f8889.coverage_year`; 141 state `f8889.medical`.

- Defaults cover the stage files: `clear_all_year` Yes, `spouse_family` No, `medical_all` No (so every existing case keeps its stated `f8889.medical` and its values), the refusal answers No. `f8889.unsupported`'s default is removed.
- The class M and mutation files: 215 cases state `f8889.unsupported` (`classm.json` 162, `mutation.json` 53) and are rewritten by rule. Mechanical.
- The 9 Yes cases become named situations. New cases: one refused case per new entry on each line that carries it (about 14); `medical_all` Yes with a taxable amount of zero; `clear_all_year` No and `spouse_family` Yes each leading into the month path; `testing_2024` on both of its routes; a distribution-only case showing the coverage inputs are not read.
- `fixtures/2025/f8889.json` has 49 cases today; expect it to grow by about 25.

**Mutation check.** As for credits. The equivalence arguments pinned on `f8889` premises are un-pinned (the catalog counted 3 of 52 for a smaller change to this form).

**`interview-rules`.** Six new gates join the minimal returns. The check's lists of questions reachable out of order must stay empty for the new inputs; by construction they do, and the one-entry minimal return for `$f8889` that the catalog recommends (section 6.2 b) would show it.

Size: **large for one form, contained in it.** Apart from `fixtures`, nothing outside `f8889.yaml`, the bank and `defaults.json` changes; `person.yaml` and `household.yaml` are untouched.

### F.4 What each review checks at each level

Under the redesign a top question is deliberately not in the form's words. The reviews need their subjects restated, not weakened.

| Review | Checks today | For a precise question (a leaf: its answer is a line's amount or decides a refusal) | For a plain top question (its answer only decides whether children are asked) |
|---|---|---|---|
| Transcription, render, class M | The form line's wording and arithmetic against the source | Unchanged. The line keeps its precise wording in the form data. | The gate line is a line like any other; its condition is checked as today. The plain wording is not their subject. |
| Question review | Whether an ordinary filer's truthful answer to the question, as shown, is the value the reading lines need (MATCH, NARROW, WIDE ...) | Unchanged, with one addition: the plain wording in the bank is compared with the line's precise wording, and any situation where they part is a finding. | Two tests replace "matches the source": (1) *can it be answered* by a person holding the named papers and knowing no tax terms (every term either printed on a paper or explained in the same sentence; no "other than"; one fact per question); (2) *is Yes wide enough*: every situation any child covers is one in which a truthful person answers the top question Yes. It should not be marked down for being wider than the source: wide is the design. |
| False-no review | For each gate: who answers No while a gated line has an amount | Not applicable. | This is its unit, unchanged in kind. New units: `s3.ev_bought`, the `person.age65` and `person.disability_retired` pair, `f8889.coverage_year` with `clear_all_year` and `spouse_family`, `f8889.has_dist`. Two extensions: a roster with fixed choices (`$f8889`, `$person`) should be a unit, since its No hides a whole form; and `f8889.medical_all` is a gate whose *Yes* hides an amount, so it needs the mirror-image test ("who answers Yes while some of the money was not for medical costs"). When this review finds a wrong No, the remedy it may propose is a child or a separate question; a longer top question is out of bounds. |
| Screen review | For each yes/no that refuses: is it narrower or wider than the instruction text of the lines it stands in for | Each new refusal question is a screen of one situation, reviewed against its own passage. | Not applicable. |
| Completeness review | Does the form's model cover the form's source | Gains the set-level duty the catch-all carried: the refusal entries on a line, taken together, must cover every situation of the instructions that the line does not compute. The coverage table (section C) is the claim it tests. | — |

Cost, by the project's rule (review what changed, one review per form per round): transcription, render and class M for `f8889` and, line-scoped, for the forms in F.2; sampled question, screen and false-no reviews for about 45 new or reworded questions at their next milestone. Their cost was not estimated here; it should be estimated with `--dry-run` before the round, and a run above $3.00 needs the owner's approval.

---

## G. Measures expected

Words of question text, with the words of the answer options added (a filer reads those too). Help text is given separately; it is shown under the question and is optional reading. "Today" is counted from the built interview. "Proposed" is counted by script from the wording in section B, so the other lane's measurements can be checked against it. Questions are counted for one person unless stated.

### G.1 The opening

| Filer | Today: questions asked | Today: words (help) | Proposed: questions asked | Proposed: words (help) |
|---|---|---|---|---|
| One person, any status | `$person`, `f1040.status`, `person.role` | 58 (70) | O1, O2 | 87 (101) |
| Couple filing together | `$person`, `f1040.status`, `person.role` twice | 82 (82) | O1 | 18 (46) |

Today's 58 is 16 + 8 for the roster and its two labels, 5 + 5 for the status prompt and its five bare codes, and 22 + 2 for the role. The proposed 87 is 6 + 12 and 9 + 60. `household.married` (217 words) is asked later in both and is not counted.

The person filing alone reads 29 more words and answers one question fewer. The words are the four descriptions that replace the codes.

### G.2 Credits

| Filer | Today: questions asked | Today: words (help) | Proposed: questions asked | Proposed: words (help) |
|---|---|---|---|---|
| Outside: none of the unusual credits, under 65, no business | `scope.credits`, `s3.line12`, `s3.line14` | 156 (72) | C1, C2, C3, C4, C7, C8, C9, C10 | 170 (113) |
| Outside, 65 or older | same | 156 (72) | C1, C2, C3, C4a, C7, C8, C9, C10 | 177 (145) |
| Outside, with one business | same | 156 (72) | the eight, and C5, C6 | 220 (113) |
| Inside: bought an electric car with a credit | `scope.credits` (Yes: refused at question 4) | 129 (30) | C1, C1a (refused at the car questions) | 41 (19) |

The filer outside the category reads slightly more than today, in eight questions where there were three. What changes is that each of the eight can be answered. 58 of the 170 words are C10, the kept list of four rare payments; the other seven average 16 words.

On a joint return C4 is asked of each spouse under 65 (8 words more).

### G.3 Health savings accounts

| Filer (one person) | Today: questions asked | Today: words (help) | Proposed: questions asked | Proposed: words (help) |
|---|---|---|---|---|
| Outside: no HSA | `$f8889` | 95 (11) | H0 | 17 (89) |
| Inside, ordinary: payroll deposits, same plan all year, all spending medical | roster, `unsupported`, `line2`, `line9`, `coverage_year`, `age55`, `line14a`, `medical`, `rollover` | 1,167 (127) | H0 to H9, H15, H19 to H23, H27 (17 questions) | 340 (464) |
| Inside, the same and married | the same nine | 1,167 (127) | the same and H9a (18) | 359 (485) |
| Inside, money out only (no 2025 deposits) | the same nine | 1,167 (127) | H0 to H7, H14, H19 to H23, H27 (15) | 260 (414) |
| Inside, account not used in 2025 | `$f8889` answered No | 95 (11) | H0 to H7, H14, H19, H22, H27 (12) | 199 (318) |
| Inside, coverage for part of the year, some spending not medical | 14 questions | 1,560 (209) | 23 questions | about 625 (about 560) |

Remarks.

- The ordinary HSA owner reads under a third of today's words and answers nearly twice as many questions. Every one of the 17 is a sentence.
- The owner of an unused account reads more than today, because today they are asked nothing. That is the price of reaching the two situations a dormant account can hide (section C.3).
- In the last row the proposed figure includes the 179 words of rules that `f8889.medical` keeps, laid out as a list; they are shown only to a person who said that not all the money paid medical costs.
- Help grows. Today's help for these questions is mostly one boilerplate sentence or nothing; the proposed help carries the examples and the paper cues ("box 12 of your Form W-2 next to the letter W"). A reader who does not need it does not open it.
- On a joint return today each HSA question carries the 12-word frame (counted above). Proposed: "About you" or "About your spouse", 2 or 3 words, and none on a one-person return (decision 7); the proposed counts are without a frame.

### G.4 What the reader test should show

For the other lane's personas, the design predicts:

- no question in the slice that a persona "cannot tell", except: C4a (a person 65 or older asked about a credit they do not know), H9's third line for a young adult on a parent's plan, and H13 (the last-month rule);
- wrong answers concentrated in the cases section D names: the employer-opened HSA, the spouse's health FSA, premiums paid from the HSA, and head of household not recognised.

If the test shows other failures, the tree is wrong there, and the remedy is a child or a separate question.

---

## H. Open questions for the owner

Each can be answered on its own. They are numbered 1 to 9. (Elsewhere in this document H0 to H27 are the HSA questions and C1 to C10 the credits questions.)

**Decision 1. May one answer record more than one input?**
The "Who is this tax return for?" choice would record the list of people, each person's role, and (for "together") the filing status. Today a rule checked by `interview-rules` says the interview sets no input and each choice maps to one value.
- *Yes, narrowly (recommended).* The rule becomes: every value comes from a choice the filer made; a choice may supply inputs of the entries it creates, plus inputs on a short allow-list in the check (one entry: `f1040.status` for the joint choice). Cost: small (interview engine, one check, the bank). Removes two to three questions for every couple and one for everyone else.
- *Yes for the role only.* Couples are still asked the status, with a labelled "filing together" option. Cost: the same; one redundant question for a third of filers.
- *No; change the model instead.* The role is derived from the entry's key. Cost: large (a new kind of expression in both evaluators and Lean, 502 fixture cases, the spec's statement that keys carry no meaning). The status overlap is not solved by this.
- *No change.* The questions stay, with better wording.

**Decision 2. Should "Were you married on December 31, 2025?" move ahead of the filing status?**
Then a person filing alone sees two or three status options, not four.
- *Not in this slice (recommended).* Four labelled options, 69 words. No model change.
- *Yes.* 38 or 49 words. Cost: one rewritten check and two helpers in the household form, a changed fixture default, up to 94 cases re-recorded. Better taken with the household redesign.

**Decision 3. The two "type in a total" questions on Schedule 3 (`s3.line12`, fuel credit; `s3.line14`, other payments and refundable credits).**
Today the filer is asked to enter an amount from a form the tool does not prepare, and `scope.credits`, read literally, refuses the same filer.
- *Refuse (recommended).* The plain questions C6, C8 and C10 refuse on Yes; the two inputs are removed. A filer described by the intent cannot produce these amounts, and a refusal tells them so. Cost: 4 fixture cases change from a value to a refusal; 422 cases lose two stated inputs; the tool prepares slightly less than it does on paper today.
- *Keep the amounts beneath the plain questions.* A Yes to C6, C8 or C10 leads to "enter the amount from the form you prepared". Cost: two more gate lines; the tool keeps a capability only a tax-literate filer can use.
- This also settles the umbrella gate U3 (`f1040.other_payments_any`), on hold, for its Schedule 3 half.

**Decision 4. Where are refusal questions asked?**
The intent says each piece goes where its topic comes up. A filer who bought an electric car is refused today at question 4 and, under the design, at the car questions, after entering wages and more.
- *At the topic (recommended).* Each question is short and in context. The cost is effort wasted before a refusal; it can be reduced later by the order of topics, which is outside this slice.
- *Early, as a short "quick check" page of the plain questions that refuse.* Refusals come first, but the questions are asked out of context, which is the complaint about today's opening.

**Decision 5. Three scope changes the sources would support.** None is needed for the slice; each is a decision to prepare something the tool refuses today.
- *A spouse who inherited an HSA.* The instructions treat it as the spouse's own (i8889 p. 3). The design keeps today's refusal of every inherited HSA. To prepare it: H2 gets a child ("Was it your husband's or wife's, and did they die before 2025?") and a Yes goes on as an ordinary account. Cost: one input, one gate, fixtures.
- *The credit for the elderly or the disabled.* With Schedule R archived, the model could rule the credit out from income already on the return for nearly everyone 65 or older, and ask nothing. Until then C4a asks a question most people cannot answer. Cost: archive, then a small screen in the model.
- *A dormant Archer MSA.* H3 refuses anyone who has one. A child ("Did money go into or come out of it in 2025?") would let the untouched ones through. Cost: one input, one gate.
- Recommended: none in this slice; take the first with the next HSA change.

**Decision 6. Archive the instructions the precise questions need.**
Of the forms behind the unhandled credits, only Form 8978's instructions, Form 2439 and Form 4136 with its instructions are in `sources/2025/`. Forms 3800, 8396, 8801, 8834, 8839, 8859, 8911, 8912, 8936 and Schedule R are not; nor is Form 5498-SA. The questions in B.2 are therefore only as precise as the one-line descriptions in the Form 1040 instructions (pp. 115 to 117), and four statements in section D are marked "as I understand the rule".
- *Archive them before the credits questions are written (recommended).* Cost: fetching and extracting about eleven documents. It closes the residuals for adoption timing and vehicle delivery dates, and lets C7's list of form numbers be cited.
- *Proceed on the Form 1040 instructions alone.* The questions refuse a little more widely than they need to.

**Decision 7. The per-person frame.**
Today every per-person question begins "For this person (you, or your spouse on a joint return) — ".
- *Show "About you" or "About your spouse" on a joint return, and nothing on a one-person return (recommended).* The stored text keeps a frame, as with the spouse phrase, so reviews are unaffected; the rewording is applied when a question is shown. Cost: small, in the engine's wording step; the entry's label ("You", "Your spouse") is already saved with the roster answer.
- *Keep the frame.* 12 words on every per-person question, for each spouse.

**Decision 8. The health FSA child question** (D.3): "Did you or your husband or wife have a health FSA or HRA at work in 2025 that pays ordinary medical bills?", asked after H9.
- *Add it (recommended).* 20 words for every contributor; closes the likeliest wrong answer about coverage.
- *Leave it in H9's help.* Shorter; relies on the help being read.

**Decision 9. Refusing on the fact of an adoption or a mortgage credit certificate, not on the wish to claim** (B.2, rows 4 and 8 of C.2).
- *Refuse on the fact (recommended).* A filer who does not know the credit exists is told the tool cannot give them their best return.
- *Add a child, "Do you want to go on without this credit?"* The tool prepares a correct return that leaves money unclaimed, with the filer's informed consent. Cost: one more question for a rare filer; arguably closer to "a correct return".

---

## I. What was verified, and what was inferred

### I.1 Verified by reading the form data or the built interview

| Claim | Where it was read |
|---|---|
| Text, help, type, options and order of every question in the slice | `canonical/2025/interview-full.json` (the appendix is generated from it) |
| `person.role` is read by 33 lines, 34 references | computed over every `canonical/2025/*.json` form with the reference rule of `engine/src/gates.ts` |
| `f1040.status` is read by 111 lines | same |
| `scope.credits` is read as a refusal by `scope.ready` and seven other lines, and by nothing else | same; the `refuses` entries in `forms/2025/{scope,f1040,s3,s8812,f8863,f5695}.yaml` |
| `f8889.unsupported` is read only by the refusals of `f8889.line13` and `f8889.line16` | same; `forms/2025/f8889.yaml` |
| `s3.line12` and `s3.line14` are inputs, each read only by `s3.line15`, and are asked of every filer | `forms/2025/s3.yaml`; the walked returns (questions 47 and 48 of the minimal single return) |
| When each HSA question is asked, and the order they come in | five synthetic returns walked through the built interview (`node engine/dist/main.js interview ...`, logs outside the repository) |
| `household.married` is not reachable before the filing status is answered | the pending list after one answer and after two |
| Married filing separately is refused as soon as it is chosen | answered `mfs` in the built interview |
| The interview-rules "no-input-set" rule and what it checks | `engine/src/interview-rules.ts`, lines 1 to 60 |
| The gate conventions | `engine/src/gates.ts` |
| How an unknown is passed over by "and"/"or", and how `choose` and refusal lists treat it | `spec/spec.md` 4.7.1 to 4.7.3; catalog section 1 |
| Existing answers that settle a situation: Form 1116; employment credits; Form 2439; a Form 8978 amount; prior-year excess HSA contributions; a funding distribution on the IRA side | the `refuses` entries and built question text of `ftc.needs1116`, `sc.special`, `sd.other_forms`, `scope.other_line16`, `person.x_other`, `retirement.special` |
| "All year" answers to `f8889.coverage_year` mean an eligible individual on the first day of every month | the option texts in `forms/2025/f8889.yaml` |
| Fixture counts (1,764 cases; 509 state `scope.credits`, 9 Yes; 314 state `f8889.unsupported`, 9 Yes; 502 state a role; 13 use other person keys; 422 state `s3.line12`/`s3.line14`, 4 above zero; 94 `mfs`) | counted over `fixtures/2025/*.json` |
| How fixture defaults work, and that class M and mutation files take none | `fixtures/2025/defaults.json` (its note); `tools/README.md`, "Test-data defaults" |
| What the question, screen and false-no reviews test | the header comments of `tools/transcription/{question,screen,false_no}_review.py` |

### I.2 Verified against the archived sources

| Claim | Source |
|---|---|
| The lines of Schedule 3 | `sources/2025/f1040s3.txt` (the printed form) |
| What each of lines 6a to 6m, 9 to 12 and 13b to 13z is for; "Leave line 6z blank" | i1040gi pp. 115 to 117 |
| Line 30, refundable adoption credit | i1040gi p. 61 |
| The filing statuses and their tests; death of a taxpayer | i1040gi pp. 12 to 15 |
| Every HSA rule cited in A.3 and C.3 | i8889 (read in full, pp. 1 to 9); the printed Form 8889 |
| The codes in box 3 of Form 1099-SA; boxes 2, 4 and 5 | f1099sa, Instructions for Recipient |
| Examples of prohibited transactions | p969 p. 9 |
| Who must file Form 8853 | i8853 p. 1 |
| Every partner who receives Form 8986 must file Form 8978 | i8978 p. 2 |
| The fuel credit is for business use | i4136 p. 1 |
| The repayment credit applies above $3,000 | p525 p. 36 |
| Frequencies | `interview/2025/gate_frequencies.yaml` (its own estimates, several of them judgments) |

### I.3 The intent document's two paper examples, checked

**"Schedule 3 prints 14 named credits and two 'other' lines."** Corrected in A.2, finding 2. Part I has twelve named credits beyond lines 1 to 5, one reserved line, and an "other" line the instructions say to leave blank. Part II has line 12, four named lines and one "other" line with three named uses. The conclusion drawn from the example holds and is stronger than stated: the list is closed.

**"What lies outside ... can be asked about positively, as facts of a life: a vehicle bought, a child adopted."** True for about half. A vehicle, an adoption, a mortgage certificate, a disability retirement and a repayment are facts of a life. The rest are not: five are leftovers from earlier years that only last year's return shows (hence C7, which asks about papers), two are papers received (C9), and four are arrangements nobody has without having been told (C10).

**"The ten items of `f8889.unsupported` fall into five plain kinds (a transfer from an IRA; an Archer MSA; a death or an inherited account; a correction of a mistake or a loan; something left over from an earlier year)."** Checked item by item against i8889:

- *A transfer from an IRA* and *an Archer MSA*: correct, one item each. The Archer item is narrower than the instructions (finding 5).
- *A death or an inherited account*: three items (5, 6, 10), and item 6 is a case of item 10. Correct as a kind; two questions cover it (H1, H2).
- *A correction of a mistake or a loan*: this joins three unrelated things. A withdrawal of excess contributions and a repaid mistaken distribution are corrections. A loan secured on the account is not a correction, and the other half of that item, a prohibited transaction, is not a loan. The design uses three questions (H7, H22, H27) and one paper check (H20).
- *Something left over from an earlier year*: this joins two items that share nothing a filer would recognise. Prior-year excess contributions are already asked of every person by another question, so the HSA block need not ask at all. A failed testing period is not "left over": its plain fact is "your coverage had a gap this year, and last year you relied on a rule that required you to stay covered". Most people are spared the question by their coverage answer.

So the five kinds become nine short questions (one of them a check of a box on a form, one asked only of people with a coverage gap), plus one situation that needs none.

### I.4 Inferred, or taken from outside the archive

| Statement | Status |
|---|---|
| Forms 3800, 8396 and 8839 can leave a credit to carry into the next year (the basis of three of C7's six form numbers) | From general knowledge; consistent with the tool's own refusal text on Schedule 8812 ("Credit Limit Worksheet B (Forms 8396, 8839, 8859)"). Forms 8859 and 8834 are confirmed by i1040gi p. 116. To be confirmed when the instructions are archived (decision 6). |
| A dealer who took the vehicle credit off the price still obliges the buyer to report it | General knowledge; not in the archive. |
| The statements marked "as I understand" in section D (lessee; delivery date; adoption costs the year before; stepparent adoption; Schedule R's disability income) | General knowledge; not in the archive. |
| Form 5498-SA exists and has a box for "Archer MSA" | Named in the help of H0 and H3 as a paper a filer may hold; the form is not in the archive. Form 1099-SA's box 5 is confirmed. |
| A sale of qualified farmland with a Form 1062 election would also be refused by `sd.other_forms` | Not checked; C10 lists it regardless. |
| A filer with no business cannot have the fuel credit except through a farm or partnership | Inferred from i4136 p. 1 (Part I, "Information About Your Business", is required). |
| `person.x_other` is asked of every person on every return | Seen on all five walked returns and expected from its readers (Form 5329 lines 4 and 49); not proved for every path. |
| The 2024 testing period cannot extend past December 31, 2025 | Derived from i8889 p. 2 and p. 7 (12 months after the month it begins). |
| Sizes in section F | Estimates from line and case counts; nothing was built. |
| That no other question catches a tax-free payout from an Archer MSA | A search of every built question's text for "Archer" and "8853"; a negative result, so weaker than a positive one. |

### I.5 Where today's interview differs from what the intent document or the owner's notes assume

1. **`scope.credits` and two later questions contradict each other.** The screen refuses a filer with a fuel credit or another Part II credit; `s3.line12` and `s3.line14` ask that same filer to type the amount in (finding 1).
2. **The Schedule 3 list** is twelve named credits and an unused "other" line in Part I, not "14 named credits and two 'other' lines" (finding 2).
3. **Four of the credit situations are already refused by other questions** (Form 1116, employment credits of a business, Form 2439, a Form 8978 amount).
4. **`person.role` has 33 reading lines (34 references), not 35.** `scope.credits` has seven readers besides `scope.ready`, not eight.
5. **The HSA catch-all's ten items overlap other questions and each other.** Prior-year excess is asked of everyone elsewhere; the IRA transfer is asked again at the Form 1099-R; item 6 is a case of item 10; item 4 is settled for most people by their coverage answer.
6. **The HSA catch-all refuses something the instructions call ordinary** (a surviving spouse's inherited HSA) **and misses something they require a form for** (money moved or paid out of an Archer MSA).
7. **The HSA roster question is itself an 84-word catch-all** in tax vocabulary, and by asking about activity it lets a dormant account skip the loan question.
8. **The HSA questions are not asked together.** On a walked return they came in four places, separated by 27 unrelated questions. The 339-word coverage question is asked even of a person with no contributions.
9. **Only three of the HSA questions carry the boilerplate help** the notes found on 213 questions overall; the HSA problem is the prompts, not the help.
10. **The "five plain kinds" for the HSA catch-all do not hold as kinds** (I.3).
11. **Most of the credit forms are not in the archive**, so the precise layer for credits cannot yet be written to the project's citation standard (decision 6).
12. **A person's death in 2025 is asked in six places** (five existing questions and the HSA catch-all), each for one form. A single fact at the opening would serve all of them; it is outside the slice and noted for the plan.
13. **`household.married` cannot be asked before the filing status** in today's model, which is why a design that "starts from what a person knows" (married or not) needs a model change there.

---

## Appendix. The questions of the slice exactly as built

Generated from `canonical/2025/interview-full.json` (profile `full`), main at the time of writing. Each question is given whole: its text as the filer sees it, its help, and its options. Word counts are of the text.

### `$person`

Order number 0; 16 words; help 58 words. Cited: f1040.

> Who is on this return: just you, or you and your spouse on a joint return?

Help: 

> Choose “Me and my spouse” only if you are married and filing a joint return. Forms W-2 and Forms 1099-R (IRA distributions, pensions and annuities) are entered under the person who received them. Amounts that are not asked person by person (interest, dividends, sales, social security benefits, deductions, payments) are entered once, for you and your spouse combined.

Options: "Just me"; "Me and my spouse (joint return)".

### `f1040.status`

Order number 0; 5 words; help 0 words. Cited: f1040.

> Form 1040, Filing Status checkboxes

Help: none.

Options: the five codes `single`, `mfj`, `mfs`, `hoh`, `qss`, shown without labels.

### `person.role`

Order number 0; 22 words; help 12 words. Cited: f1040.

> For this person (you, or your spouse on a joint return) — Whose entry is this, yours (the taxpayer) or your spouse's?

Help: 

> Your own entry is the taxpayer's; your spouse's entry is the spouse's.

Options: `taxpayer`, `spouse`.

### `scope.credits`

Order number 0; 129 words; help 30 words. Cited: f1040.

> Do you want to claim any credit other than the following, or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?
>
> - the foreign tax credit claimed without Form 1116
> - the excess social security credit
> - the child tax credit
> - the credit for other dependents
> - the additional child tax credit
> - the earned income credit
> - the credit for child and dependent care expenses (Form 2441)
> - the retirement savings contributions credit (Form 8880)
> - the residential energy credits (Form 5695)
> - the net premium tax credit this tool figures on Form 8962 from your Forms 1095-A (Schedule 3 line 9)
> - the education credits this tool figures on Form 8863 (the American opportunity and lifetime learning credits)

Help: 

> Yes if you want any credit not in the question's list of credits this tool figures, or have any other amount for Schedule 3 Part I; Yes refuses the return.

### `s3.line12`

Order number 10; 15 words; help 19 words. Cited: f1040s3.

> Credit for federal tax on fuels from Form 4136 (supplied subtotal; preparation outside Stage 2)

Help: 

> The credit for federal tax on fuels from Form 4136, which this tool does not prepare. Zero if none.

### `s3.line14`

Order number 10; 12 words; help 23 words. Cited: f1040s3.

> Total other payments or refundable credits (supplied subtotal; preparation outside Stage 2)

Help: 

> The total of Schedule 3 lines 13a through 13z (other payments and refundable credits), which this tool does not prepare. Zero if none.

### `$f8889`

Order number 10; 84 words; help 11 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — Did you, your employer or someone else contribute to a health savings account (HSA) for you for 2025 (including a qualified HSA funding distribution, a direct transfer from your IRA to your HSA), did your HSA make a distribution in 2025 (Form 1099-SA), did you stop being an eligible individual during a testing period (Form 8889 Part III), or did you acquire an interest in an HSA because the account beneficiary died?

Help: 

> One Form 8889 per person covers all of that person's HSAs.

Options: "Yes (one Form 8889 for all of this person's HSAs)"; "No".

### `f8889.unsupported`

Order number 10; 232 words; help 22 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — Any of these: a qualified HSA funding distribution from an IRA in 2025; contributions by you or your employer to an Archer MSA for 2025 (Form 8853), or, if you or your spouse had family coverage under an HDHP at any time during 2025, any contribution by anyone to your spouse's Archer MSA; excess HSA contributions from an earlier year that remain in your HSA; failing to remain an eligible individual during a testing period that began in an earlier year (last-month rule or qualified HSA funding distribution); an HSA you acquired because of the account beneficiary's death; the HSA of a person who died in 2025 whose estate is the beneficiary (its value at death is included on the final return); a deemed distribution from an HSA in 2025 (a prohibited transaction, or any part of an HSA used as security for a loan); a withdrawal of excess contributions or their earnings, made in 2025 or in 2026 by the due date of your 2025 return, including extensions; a mistaken distribution you repaid to your HSA; or this person died in 2025 (a joint return with a spouse who died in 2025, or the final return of a person who died in 2025), since the last month of a decedent's tax year is the month of death, not December?

Help: 

> HSA distributions that were not used for qualified medical expenses are not among these; Form 8889 Part II asks about them separately.

### `f8889.line2`

Order number 10; 96 words; help 10 words. Cited: f8889.

> For this person (you, or your spouse on a joint return) — HSA contributions you made for 2025 (or those made on your behalf), including those made by April 15, 2026 that were for 2025 (or by a later date if you served in, or in support of, the U.S. Armed Forces in a designated combat zone or contingency operation); do not include employer contributions, payroll contributions through a cafeteria plan, rollovers, amounts the trustee of another of your HSAs transferred directly to this one (a trustee-to-trustee transfer), or qualified HSA funding distributions; zero if none

Help: 

> Married filing separately and unsupported items are refused with citations.

### `f8889.line9`

Order number 10; 50 words; help 10 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — Employer contributions to your HSAs for 2025, including payroll contributions through a cafeteria plan (Form W-2 box 12, code W, less employer contributions for 2024 included there, plus employer contributions for 2025 made in 2026); zero if none

Help: 

> Married filing separately and unsupported items are refused with citations.

### `f8889.coverage_year`

Order number 10; 339 words; help 37 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — Was your high-deductible health plan (HDHP) coverage self-only all year, family all year, or did it change during 2025 (including starting or ending)?
>
> - Self-only all year: on the first day of every month of 2025 you were an eligible individual with self-only HDHP coverage, and no month counts as family coverage under the rules below.
> - Family all year: on the first day of every month of 2025 you were an eligible individual with family HDHP coverage, or counted as having it under the rules below.
> - Changed: anything else, including coverage that started, ended or changed type during 2025, any month in which you were not an eligible individual, or if you are not sure. The month-by-month questions follow.
>
> An eligible individual on the first day of a month:
> - is covered by an HDHP
> - has no other health coverage, apart from the coverage the instructions disregard (accident, disability, dental, vision, long-term care, telehealth and other remote care, workers' compensation, tort or property liability insurance, insurance for a specified disease or illness, and insurance paying a fixed amount per day of hospitalization); a general-purpose health FSA or HRA that pays your medical expenses, yours or your spouse's, is other health coverage, while VA care for a service-connected disability and benefits under surprise billing laws are not
> - is not enrolled in Medicare, counting Medicare coverage backdated to an earlier month
> - cannot be claimed as a dependent on someone else's 2025 return
>
> A month counts as family coverage:
> - if you were covered by a family HDHP (HDHP coverage for you and at least one other person, such as an employee-plus-spouse or employee-plus-children tier), including as a member of someone else's plan (your spouse's or a parent's, for example)
> - if you were covered by a self-only HDHP and a family HDHP at the same time
> - if you and your spouse were both eligible individuals and either of you had family HDHP coverage

Help: 

> The first day of each month is what counts. Medicare enrollment, other health coverage that is not disregarded, or being someone else's dependent in any month means the coverage was not the same all year; choose Changed.

Options (value: label): `changed`: "Changed during the year (including starting or ending), or not sure"; `family`: "Family all year (yours, or your spouse's while you were both eligible)"; `self_only`: "Self-only all year".

### `f8889.months_eligible`

Order number 10; 58 words; help 20 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — Number of months of 2025 on the first day of which you were an eligible individual (covered by a high-deductible health plan, with no other disqualifying health coverage, not enrolled in Medicare, and not able to be claimed as a dependent on someone else's 2025 return)

Help: 

> Count a month only if every condition held on its first day. December 1 counts as one of the months.

### `f8889.months_family`

Order number 10; 109 words; help 12 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — Of those eligible months, the number in which you had or were treated as having family (not self-only) high-deductible health plan coverage on the first day of the month; zero if your coverage was self-only in all of them. If you and your spouse were both eligible individuals for a month and either of you had family HDHP coverage, count that month as family coverage for both of you and disregard either spouse's self-only plan. Count the actual eligible months here; the separate last-month-rule question determines whether December 1 coverage is treated as applying throughout the year.

Help: 

> Count only months of family coverage, not every month you were covered.

### `f8889.dec_coverage`

Order number 10; 113 words; help 0 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — The high-deductible health plan coverage you had or were treated as having on December 1, 2025: none (you were not an eligible individual that day), self_only, or family. Family is HDHP coverage for you and at least one other person, and includes coverage as a member of someone else's family HDHP (your spouse's or a parent's, for example) and a self-only HDHP and a family HDHP held at the same time. If you and your spouse were both eligible individuals that day and either of you had family HDHP coverage, answer family for both spouses and disregard either spouse's self-only plan.

Help: none.

Options (value: label): `family`: "Family HDHP coverage (yours, or your spouse's while you were both eligible)"; `none`: "Not an eligible individual on December 1"; `self_only`: "Self-only HDHP coverage".

### `f8889.last_month`

Order number 10; 56 words; help 35 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — Do you use the last-month rule: treat yourself as an eligible individual for all of 2025 with the coverage you had on December 1, 2025, which requires you to remain an eligible individual from December 1, 2025 through December 31, 2026 (the testing period)?

Help: 

> If you stop being an eligible individual during the testing period (other than by death or disability), the contributions the rule allowed are included in income, with a 10% additional tax (Form 8889 Part III).

### `f8889.age55`

Order number 10; 23 words; help 0 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — Were you age 55 or older at the end of 2025?

Help: none.

### `f8889.allocation`

Order number 10; 57 words; help 24 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — you and your spouse each have an HSA and family coverage. Do you divide the family contribution limit equally (equal), or by a different allocation you both agree on, such as allocating nothing to one spouse (agreed)? Use the same answer on both Forms 8889.

Help: 

> The family limit is figured on each Form 8889 for the months treated as having family coverage (Step 1 of the line 6 instructions).

Options: `equal`, `agreed`.

### `f8889.allocated`

Order number 10; 42 words; help 9 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — the part of the family contribution limit (Step 1) allocated to this person under the allocation you agreed on. The two parts together may not be more than the limit.

Help: 

> Your spouse's part is the rest of the limit.

### `f8889.employer_in_box1`

Order number 11; 46 words; help 10 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — Are your employer's HSA contributions above the limit included in your wages in Form W-2 box 1? (Answer no if the employer has not included them; asked only when employer contributions exceed the limit.)

Help: 

> Married filing separately and unsupported items are refused with citations.

### `f8889.line14a`

Order number 10; 54 words; help 17 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — Total distributions you received in 2025 from all of your own HSAs (box 1 of your Forms 1099-SA, including distributions you rolled over, but not an amount the trustee transferred directly to the trustee of another of your HSAs); zero if none

Help: 

> A direct transfer from one of your HSAs to another (trustee to trustee) is not a distribution.

### `f8889.rollover`

Order number 10; 73 words; help 11 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — The part of those distributions that you rolled over within 60 days to another HSA of yours (an HSA of the same account beneficiary); do not count a rollover into an HSA that had already received a rollover contribution in the 1-year period before it, since an HSA can receive only one rollover contribution during a 1-year period; zero if none

Help: 

> An HSA can receive only one rollover in a 1-year period.

### `f8889.medical`

Order number 10; 179 words; help 9 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — The part of your 2025 HSA distributions used to pay qualified medical expenses (not reimbursed by insurance or other coverage, and incurred after the HSA was established) of you, your spouse, your dependents, and anyone who would be your dependent except that they filed a joint return, had gross income, or you (or your spouse, on a joint return) could be claimed as someone else's dependent; a child of divorced or separated parents counts for both parents. Insurance premiums count only if they are for long-term care insurance, health care continuation coverage (such as COBRA), health care coverage while receiving unemployment compensation under federal or state law, or Medicare and other health care coverage if you were 65 or older (not a Medicare supplemental policy, such as Medigap); continuation coverage and coverage while receiving unemployment compensation can be for your spouse or a dependent, but if you, the HSA owner, are under 65, Medicare premiums for your spouse or dependents generally do not count; zero if none

Help: 

> You cannot also deduct these expenses on Schedule A.

### `f8889.line17a`

Order number 10; 35 words; help 15 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — Were any of your taxable HSA distributions made after you became disabled or turned age 65 (the exceptions to the additional 20% tax)?

Help: 

> Answer No if every taxable distribution was made before you became disabled or turned 65.

### `f8889.subject_part`

Order number 10; 50 words; help 16 words. Cited: i8889.

> For this person (you, or your spouse on a joint return) — The part of your taxable HSA distributions (Form 8889 line 16) that was made before you became disabled or turned age 65 (the part subject to the additional 20% tax); zero if all of it was made after

Help: 

> The taxable distributions are your distributions less rollovers and the part used for qualified medical expenses.
