# Consumers check, group C2: pairs not ruled (13)

These pairs are not ruled. The verdict column says "differs" where a filer covered by the page's rule can truthfully answer the question No, so the reader drops the case without warning, and "unsure" where the gap is real but narrow or depends on text outside the cited page. For each pair I read the reader line in `forms/2025/<form>.yaml`, the input's own line, its `interview/2025/questions.yaml` entry (prompt and help) and the page text in the prompt file under `/tmp/landing2/cprompts/us/`.

## Differs

### consumer:sa.mortgage_over_limit@i1040sca:p8 (reader sa.mortgage_over_limit_if_interest)
- Question: "Is your home mortgage interest limited because the mortgage debt is more than $750,000 (more than $1,000,000 where it was all taken out on or before December 15, 2017), or because the mortgages together are more than the fair market value of the home?" The interview prompt says "more than $750,000"; the help gives only the $1,000,000 alternative.
- Page: "you can only deduct home mortgage interest on up to $1,000,000 ($500,000 if you are married filing separately) of that debt" (the $375,000 MFS figure for post-2017 debt follows on p. 9).
- Why: the question gives no married-filing-separately halves. An MFS filer with, for example, $600,000 of pre-2018 debt answers No, the limit is never applied, and the full interest is deducted. I found no other MFS mortgage refusal in sa.yaml (I searched for 375,000, 500,000 and "separately").

### consumer:s3.adoption_any@i1040gi:p24 (reader scope.adoption_benefits_if_adoption)
- Question: "In 2024 or 2025, did you (or, on a joint return, your spouse) adopt a child, or pay expenses in connection with adopting a child or trying to adopt one?" The prompt reads "Since the start of 2024 ... adopt a child, or pay costs toward adopting one?"
- Page: "Employer-provided adoption benefits should be shown in box 12 of your Form(s) W-2 with code T."
- Why: if an employer paid adoption costs in 2025 directly to the provider, and no adoption was final and the filer paid nothing since 2024, the filer truthfully answers No. That happens with a foreign adoption still in progress, or when the filer's own payments were in 2023. The code T question is then never asked. Benefits for a foreign adoption that is not yet final are taxable on line 1f. The W-2 entry does not catch code T either: `w2.box12_any` lists D, E, F, G, H, S, AA, BB and EE only.

### consumer:scope.church_exempt_wages@i1040sse:p1 (reader scope.church_exempt_wages_if_religious_work)
- Question: "Did a church or church organization pay you wages with no social security or Medicare tax taken out (boxes 4 and 6 of its W-2 are empty)?"
- Page: "Church employee income is wages you received as an employee (other than as a minister, member of a religious order, or Christian Science practitioner) of a church or qualified church-controlled organization that has a certificate in effect electing an exemption from employer social security and Medicare taxes."
- Why: the parent question (scope.religious_work) asks about "you (or, on a joint return, your spouse)", but this question asks only about "you". On a joint return where only the spouse has church employee income, the filer answers No, and the spouse's Schedule SE tax is never refused. Every other scope question in this group names the spouse.

### consumer:scope.f8978@i1040gi:p34 (reader scope.f8978_if_business_before)
- Question: "Did a partnership you were in send you a Form 8986 about changes made by an audit?"
- Page: "Tax from Form 8978, line 14 (relating to partner's audit liability under section 6226)."
- Why: the page's tax falls on either spouse of a joint return, and the parent asks about the spouse too, but this question asks only about "you". If only the spouse received a Form 8986, the answer is No, and the Form 8978 tax is never refused. scope.k1 does not cover this case: the partner may have no 2025 K-1.

### consumer:scope.reservist_repaid@i1040gi:p95 (reader scope.reservist_repaid_if_armed_forces)
- Question: "In 2025, did you put back into an IRA money you had taken out of a retirement plan when you were called to active duty as a reservist?"
- Page: "Don't include any repayments of qualified reservist distributions."
- Why: the parent (scope.armed_forces) names the spouse, but this question asks only about "you". A spouse's 2025 repayment is then not refused. It could then be entered as an ordinary IRA contribution, which the page forbids.

### consumer:scope.business_before@i1040gi:p91 (reader scope.nol_if_business_before)
- Question: "In any year before 2025, did you (or, on a joint return, your spouse) own a business, a farm, a rental property, or a share of a partnership or an S corporation?"
- Page: "Net operating loss (NOL) deduction. Enter any deduction for an NOL from an earlier year."
- Why: an individual's NOL can come from a personal casualty or theft loss, such as one in a federally declared disaster, without any business. The child question's own help says "Answer Yes too for such a loss that came from a casualty or theft". The parent gate never reaches that filer, who answers No, so the NOL carryover is never refused. The page itself only points to the Form 172 instructions; that an NOL can arise from a casualty loss is general NOL law, not text on p. 91.

### consumer:scope.pfic@i1040gi:p114 and consumer:scope.pfic@i1040gi:p34 (reader scope.pfic_if_foreign_shares)
- Question: "Was any of it a foreign investment fund, such as a mutual fund or ETF set up outside the United States (a 'passive foreign investment company')?"
- Page: p. 34, "Any tax from Form 8621, line 16e, relating to a section 1291 fund."; p. 114, "Enter any interest amount from Form 8621, line 16f, relating to distributions from, and dispositions of, stock of a section 1291 fund."
- Why: a section 1291 fund is any PFIC without an election. A PFIC is any foreign corporation that meets the 75% passive-income test or the 50% passive-asset test, which includes holding companies and cash-rich operating companies, not only funds. The question's defining words, "foreign investment fund", let a holder of such a company answer No; only the parenthetical names the term. Severity is moderate, since a filer seldom knows a company's PFIC status. The question could ask about any foreign company whose income or assets are mostly investments, or simply refuse every foreign holding that is not a fund.

## Unsure (narrow, or the rule lies outside the cited page's words)

### consumer:scope.religious_work@i1040sse:p1 (reader scope.clergy_if_religious_work)
- Question: "In 2025, were you (or, on a joint return, your spouse) paid for work by a church or other religious body, or for work as clergy (a minister, priest, rabbi or imam)?"
- Page: "you must pay SE tax on salaries and other income for services you performed as a minister, member of a religious order who hasn't taken a vow of poverty, or Christian Science practitioner"
- Why: a Christian Science practitioner is paid by patients, not by a religious body, and is not clergy, so the truthful answer is No, and scope.clergy (which names practitioners) is never asked. Without Form 4361, the practitioner's Schedule C produces the ordinary SE tax, so the harm is limited to a practitioner with an approved Form 4361 exemption. Adding "or as a Christian Science practitioner" to the parent closes the gap.

### consumer:scope.passive@i8582:p1 (reader scope.passive_if_business_before)
- Question: "In 2025, did you have income or a loss from, or sell your share of, a business or rental that you owned but did not help run (a 'passive activity')?"
- Page: "Form 8582 is used by noncorporate taxpayers to figure the amount of any passive activity loss (PAL) for the current" ... "(including prior year unallowed losses)".
- Why: this question asks only about "you", while the parent names the spouse. Most of the spouse's 2025 cases are refused by other questions (scope.rental, scope.k1, scope.farm, Schedule C line G). A spouse's prior-year unallowed loss with no 2025 activity is not covered by the question's "In 2025 ... income or a loss" wording either. Low impact; the fix is a wording change: "(or, on a joint return, your spouse)" and "or a loss carried from an earlier year".

### consumer:scope.se_plan_other@i1040gi:p93 (reader scope.se_plan_other_if_business)
- Question: "In 2025, did you (or, on a joint return, your spouse) put money into a retirement plan of your own business other than a SEP or a SIMPLE, such as a solo 401(k)?"
- Page: "Self-Employed SEP, SIMPLE, and Qualified Plans" / "If you were self-employed or a partner, you may be able to take this deduc-" (the page ends there).
- Why: the line 16 deduction is for contributions for 2025, which can be made up to the return's due date in 2026. "In 2025, did you put money into" lets a filer whose solo 401(k) contribution for 2025 was made in early 2026 answer No, and the return is then prepared without that deduction and without a refusal. The timing rule is in the line 16 text after p. 93 and in Pub. 560, not in the cited page's words.

### consumer:sa.personal_property_tax_any@i1040sca:p3 (reader sa.line5c_if_taxed)
- Question: "In 2025, did you (or, on a joint return, your spouse) pay a state or local tax on personal property, such as a car or a boat, that is charged every year and based on the value of the property?"
- Page: "Include taxes imposed by a U.S. territory with your state and local taxes on lines 5a, 5b, and 5c."
- Why: the question says "state or local", so a filer whose only value-based yearly personal property tax is a territory's can answer No, and line 5c then omits it. The sibling questions name territory tax: sa.state_tax_other_any asks for territory income tax, and sa.property_tax_other_any's help treats territory real estate tax as ordinary. This is a very narrow case.

### consumer:sd.sold_other@i1040sd:p6 (reader sd.installment_if_sold)
- Question: "In 2025, did you (or, on a joint return, your spouse) sell or trade real estate or business property? Answer Yes too if you are being paid over more than one year for anything you sold, in 2025 or before."
- Page: "If you sold property (other than publicly traded stocks or securities) at a gain and you will receive a payment in a tax year after the year of sale, you must generally report the sale on the installment method unless you elect not to."
- Why: the page needs only one payment in a later year. "Paid over more than one year" can read as several payments spread over years. A 2025 sale of other property, such as privately held stock or a collectible, paid in a single 2026 payment could be answered No, and the installment question is skipped. A narrow case; changing the wording to "a payment for it in a later year" would close it.
