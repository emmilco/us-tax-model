# Legal and liability surface

Research date: 2026-10-13. This is not legal advice. Read the "Could not verify" section before relying on anything here: several IRS publications are PDFs my fetch tool could not read, and the holding of Rev. Rul. 85-189 was never read in full.

## Summary

- **"The user files it themselves" does not take the tool out of the federal return-preparer definition; the absence of compensation does.** In Rev. Rul. 85-189 the customer completed the return with no help from the software seller, and the IRS still treated the seller as a potential preparer. The protection is the "for compensation" element of IRC 7701(a)(36). Selling the tool, and plausibly donations or paid hosting, removes that protection.
- **An interview that decides which forms apply is not "mechanical assistance."** The IRS position is that software making substantive determinations (eligibility, which deductions apply) goes beyond the typing/reproduction exception. Only the compensation element stands between the interview tool and preparer status.
- **The section 7216 regulation names software developers and says a fee is irrelevant.** What limits it is "engaged in the business" and "holds himself out." A local-only tool also never receives information it could disclose or misuse. A hosted version, telemetry, crash reports or user registration each change that.
- **The e-file belief holds, as far as I could read.** Every e-file role is defined by formatting or transmitting electronic return data to the IRS. Printing paper, or showing values the user retypes into Free File Fillable Forms, is none of those roles.
- **Printing forms brings in the substitute-forms rules (Pub. 1167 / Rev. Proc. 2025-27)** if the tool renders its own forms. Filling the official IRS PDFs largely avoids this.
- **Hosting is the step that changes the legal picture.** It adds 7216/6713 exposure, the FTC Safeguards Rule (if a business), state privacy and breach law, and a "service not product" characterization for unauthorized-practice purposes.
- **State paid-preparer laws read (CA, OR, NY) are all keyed to a fee or compensation** and none mention software.
- **I found no case challenging tax software as unauthorized practice of law, and no reported decision where a consumer won negligence damages from a tax software maker for a calculation error.** That is an absence in my searches, not proof none exists.
- **A warranty disclaimer is necessary but not sufficient.** Commercial "accuracy guarantees" are narrow: penalties and interest only, calculation errors only, with a liability cap of fees paid or $100.
- **The FTC's Intuit "free" order was vacated in March 2026 on forum grounds, not on the merits.** Avoid unqualified claims regardless.

## Findings

### 1. "Tax return preparer": IRC 7701(a)(36) and Reg. 301.7701-15

- **Statute.** A preparer is "any person who prepares for compensation, or who employs one or more persons to prepare for compensation" a return or refund claim. A person is excluded merely because he "furnishes typing, reproducing, or other mechanical assistance." Source: https://www.law.cornell.edu/uscode/text/26/7701. Confidence High; read directly (short quotes).
- **Regulation** (CFR revised 2025-04-01; T.D. 9436, 2008, as amended 2009):
  - (c): "A person who furnishes to a taxpayer or other tax return preparer sufficient information and advice so that completion of the return ... is largely a mechanical or clerical matter" is a preparer.
  - (f)(1)(viii) excludes "an individual providing only typing, reproduction, or other mechanical assistance."
  - (f)(1)(xii) excludes "a person who prepares a return ... with no explicit or implicit agreement for compensation, even if the person receives an insubstantial gift, return service, or favor."
  - The regulation never mentions software and does not define "compensation."
  - Source: https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol20/xml/CFR-2025-title26-vol20-sec301-7701-15.xml. Confidence High; read directly.
- **Rev. Rul. 85-189.** The issue is whether "a person who prepares a computer program and sells it to a taxpayer" for preparing the taxpayer's return is a preparer.
  - Facts: a Form 1040 program designed so customers "can use it even if they are not familiar with the provisions of the Code," used by the customer without the seller's help.
  - Tax Notes headnote: such a person "may be an income tax preparer."
  - Companion rulings 85-187 and 85-188 are described as turning on whether the program makes "substantive determinations" beyond mechanical assistance.
  - An IRS Chief Counsel memo (PMTA 2000-402) is quoted as saying the Service "has applied the definition of preparer to a company (and the computer programmer) that furnishes computerized tax return preparation services when the computer program goes beyond mere mechanical assistance."
  - Source: https://taxnotes.com/lr/resolve//d72v (search snippets; page returned 403). Confidence Medium. I did not read the ruling's holding or its Issue 2 (which preparer duties and penalties apply).
- **Does "for compensation" settle it for free software?** For 7701(a)(36), and so for 6694, 6695 and PTIN, yes on the text: no compensation, no preparer. Confidence Medium-High. It is a textual reading; I found no ruling on gratuitous software.
- **If sold:** squarely the 85-189 fact pattern. **Donations:** uncertain. (f)(1)(xii) tolerates only an "insubstantial gift" with "no explicit or implicit agreement." A donate button beside a tax tool is arguable either way. **Paid hosting or a paid support tier:** compensation.
- I found no evidence the IRS actually asserts preparer penalties against consumer software vendors. Non-enforcement is not the same as non-coverage.

### 2. Sections 7216 and 6713; Reg. 301.7216-1

- **Statute, 7216(a).** Covers "any person who is engaged in the business of preparing, or providing services in connection with the preparation of, returns ... or any person who for compensation prepares any such return for any other person," who "knowingly or recklessly" discloses or uses information "furnished to him." It is a misdemeanor: fine up to $1,000 ($100,000 where 6713(b) applies) and up to one year. Source: https://www.law.cornell.edu/uscode/text/26/7216. Confidence High; read directly. I did not fetch 6713 itself.
- **Regulation, (b)(2)(i)(B).** Preparer includes "any person who is engaged in the business of providing auxiliary services in connection with the preparation of tax returns, including a person who develops software that is used to prepare or file a tax return and any Authorized IRS e-file Provider."
- **(b)(2)(iii).** One is so engaged "if, in the course of the person's business, the person holds himself out to tax return preparers or to taxpayers as a person who performs auxiliary services ... whether or not the person charges a fee."
- **(b)(3)(ii) Example 1.** When a taxpayer registers purchased tax software, "the software provider is a tax return preparer ... and the information that A provides to register her purchase is tax return information."
- Source for the three points above: https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol20/xml/CFR-2025-title26-vol20-sec301-7216-1.xml. Confidence High; read directly.
- **Local, open-source, receives nothing.** Being free does not answer the status question here. The open question is whether a hobbyist is "engaged in the business" and acting "in the course of the person's business"; I found no authority on that. But the offence requires information "furnished to him." A tool that transmits nothing to the author leaves nothing to disclose or use. Conclusion: status uncertain, conduct exposure effectively nil. Confidence Medium.
- **Hosted, or any data flow back.** Squarely inside. Registration data, analytics events tied to return content, crash dumps and support emails containing return data all become "tax return information," subject to the consent rules in 301.7216-2 and -3 (not read).
- The IRS 7216 FAQ lists software developers and VITA volunteers as preparers, but the page is marked historical. Source: https://www.irs.gov/tax-professionals/section-7216-frequently-asked-questions (reviewed 28-Jun-2026).

### 3. Preparer penalties and PTIN

- **6694.** Applies to a "tax return preparer" as defined in 7701(a)(36). Penalties: greater of $1,000 or 50% of income derived (unreasonable position); greater of $5,000 or 75% (willful or reckless). Source: https://www.law.cornell.edu/uscode/text/26/6694. Confidence High; read directly.
- With no income derived and no compensation, there is no preparer and no penalty base. 6695 was not read directly; it uses the same definition.
- **PTIN, Reg. 1.6109-2(g).** Preparer is "any individual who is compensated for preparing, or assisting in the preparation of, all or substantially all" of a return. Its examples treat a person using tax software as the preparer when that person makes the substantive determinations; they do not address the software's author. Source: https://www.law.cornell.edu/cfr/text/26/1.6109-2. Confidence High.

### 4. Circular 230 and Loving

- 31 CFR 10.2 defines preparer by reference to 7701(a)(36). 31 CFR 10.8 still says compensated preparers "must have a preparer tax identification number." Sources: https://www.law.cornell.edu/cfr/text/31/10.2 and https://www.law.cornell.edu/cfr/text/31/10.8. Confidence High.
- *Loving v. IRS*, 742 F.3d 1013 (D.C. Cir. 2014), held that 31 U.S.C. 330 does not authorize regulating return preparers. A Federal Register notice of 28 Nov 2025 withdrew a 2012 preparer proposal, reportedly stating the IRS is prohibited from regulating preparers. Confidence Medium; secondary descriptions and a search snippet.
- The Taxpayer Assistance and Service Act (Crapo-Wyden discussion draft, 30 Jan 2025) would add preparer standards through section 6109. It was not enacted as of the National Taxpayer Advocate's post (updated 3 Dec 2025), and that post does not mention software. Source: https://www.taxpayeradvocate.irs.gov/news/nta-blog/the-tas-act-strikes-a-reasonable-balance-on-return-preparer-oversight/2025/04/. Later 2026 status not checked.
- A non-practitioner publishing uncompensated software does not practice before the IRS. Circular 230 does not reach the project. Confidence High.

### 5. E-file regime and substitute forms

- **Rev. Proc. 2007-40** (IRB 2007-26) role definitions:
  - ERO "originates the electronic submission of returns."
  - Transmitter "transmits electronic return information directly to the Service."
  - Intermediate Service Provider "receives tax return information from an ERO" (or taxpayer) and processes or forwards it.
  - Software Developer develops software for formatting electronic return information to IRS specifications and/or transmitting it directly (paraphrase).
  - Applicants "must apply for participation and must be accepted by the Service."
  - Source: https://www.irs.gov/irb/2007-26_IRB. Confidence High for these roles; read via the fetch tool.
- An IRS fact sheet says: "Software developers develop software to format returns according to the IRS's electronic return specifications." Source: https://www.irs.gov/e-file-providers/software-developers-technical-fact-sheet (search snippet).
- **Owner's belief: confirmed.** Paper output, or on-screen values the user retypes, involves no electronic return formatting and no transmission. Confidence Medium-High, because the current Pub. 3112 (Nov 2025) and Pub. 1345 (Dec 2025) could not be read.
- An IRS QuickAlert (Jan 2026) says the new Pub. 1345 adds a section on resellers of software as Intermediate Service Providers. Not relevant unless the project ever touches e-file.
- **The line to stay behind:** generating MeF XML, or automating entry into Free File Fillable Forms, moves toward the Software Developer or Transmitter roles.
- Free File Fillable Forms is open for the 2026 season through 15 Oct 2026. The IRS says of it: "You must follow the official form instructions and do some calculations yourself." Source: https://www.irs.gov/e-file-providers/free-file-fillable-forms (updated 24-Sep-2026). I did not check its terms of use for automation restrictions.
- **Substitute forms, Rev. Proc. 2025-27** (IRB 2025-44; becomes Pub. 1167 Rev. 10-2025):
  - A substitute form is "a tax form (or related schedule) that differs in any way from the official version."
  - Substitutes "must be approved by the IRS before being filed" unless they fully comply with the published specifications.
  - They "must conform to the physical layout of the corresponding IRS form."
  - "All substitute forms must contain ... the OMB number that is on the official form."
  - "The accuracy of the program remains the responsibility of the software package developer, distributor, or user."
  - Nonconforming forms "are subject to being returned to the filer."
  - Forms 1040-ES (OCR) may not be reproduced.
  - Source: https://www.irs.gov/irb/2025-44_IRB. Confidence Medium-High; read through section 5.1.2 only.
- So the rules do bear on software that renders its own forms. The practical consequence is rejection or processing delay for the filer; I saw no penalty provision in the part read.

### 6. FTC Safeguards Rule / GLBA; Pubs. 4557 and 5708

- 16 CFR 314.2(h): a financial institution is "any institution the business of which is engaging in an activity that is financial in nature." A listed example is "an accountant or other tax preparation service that is in the business of completing income tax returns." Source: https://www.law.cornell.edu/cfr/text/16/314.2.
- 12 CFR 225.28(b)(6)(vi) lists "providing tax-planning and tax-preparation services to any person" as a financial activity. Source: https://www.law.cornell.edu/cfr/text/12/225.28.
- "Customer information" is a record about a customer "handled or maintained by or on behalf of you." Institutions holding data on fewer than 5,000 consumers are exempt only from "certain provisions." Source: https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know (Dec 2024). Confidence High on text.
- **Local-only.** The author maintains no customer information, and a non-commercial project is arguably not a "business." The rule has nothing to attach to. Confidence Medium-High.
- **Hosted.** If operated as a business storing return data, it is plausibly a covered tax preparation service owing a written information security program. A free, non-commercial hosted service is unclear and is a lawyer question.
- Pubs. 4557 and 5708 were not read. They are understood to be addressed to tax professionals.

### 7. Unauthorized practice of law and of accountancy

- **Parsons Technology.** The district court enjoined sale of Quicken Family Lawyer as the practice of law. The Fifth Circuit ruled: "We therefore VACATE the injunction," after Texas amended its statute so that practice of law "does not include the design, creation, publication, distribution, display, or sale" of "computer software, or similar products if the products clearly and conspicuously state that the products are not a substitute for the advice of an attorney." Source: https://law.resource.org/pub/us/case/reporter/F3/179/179.F3d.956.99-10388.html. Confidence High; read directly. Current text of Tex. Gov't Code 81.101(c) not verified.
- **Janson v. LegalZoom** (W.D. Mo. 2011). Reported as distinguishing a do-it-yourself product from a document-preparation service built on a "branching intake mechanism" plus human review. The latter was held to be UPL under Missouri law, and the case settled. Confidence Medium; secondary (case briefs, Eric Goldman blog).
- **LegalZoom v. N.C. State Bar**, 2015 NCBC 96 (consent judgment). Reported terms: attorney review of templates, and disclosure that forms are not a substitute for an attorney. Confidence Medium; secondary.
- **Tax returns.** *Gardner v. Conway* (Minn. 1951) is summarized as holding that preparing a return is not itself the practice of law, but resolving "difficult legal questions" for a fee is. Older bar opinions are less generous; Kentucky KBA U-25 says even the simplest return "involves the expression of multiple legal conclusions." Confidence Low-Medium; secondary summaries only.
- **Assessment.** The risk is low but not zero and varies by state. *Janson* shows that a branching questionnaire is exactly what moved LegalZoom from product to service, though human review and a fee were also present there. A free, locally run program with no human in the loop is at the product end.
- **Unlicensed public accountancy** was not researched to primary sources. It is unanswered, not cleared.

### 8. State preparer regulation

- **California**, Bus. & Prof. Code 22251: "a person who, for a fee or for other consideration, assists with or prepares tax returns for another person." Source: https://california.public.law/codes/business_and_professions_code_section_22251 (verified 12 Oct 2026). "Other consideration" is broader than a fee, which matters for donations.
- **Oregon**, ORS 673.615: licence required to prepare, advise on or assist with personal income tax returns "for another and for valuable consideration." Source: https://oregon.public.law/statutes/ors_673.615. A 2026 bill (SB 1510) touching the definitions surfaced in search; status unchecked.
- **New York**, Tax Law 32(a)(14): "an individual who prepares a substantial portion of any return for compensation." Section 34's title refers to "software companies" in connection with e-file charges; its text was not read. Source: https://newyork.public.law/laws/n.y._tax_law_section_32.
- **Maryland.** Registration applies to individuals who prepare returns "for a fee" (board web page). The statutory text was not retrieved, and a 2024 fiscal note said the Act was scheduled to sunset 1 July 2026. Current status unverified.
- Confidence High for the quoted CA/OR/NY text; Low for Maryland. Other states were not surveyed.

### 9. Civil liability for errors

- **Case law.** Targeted searches found no reported decision awarding a consumer negligence damages against a tax software maker for a calculation error. Confidence Low that none exists.
  - A summary describes a preparer's suit against the TaxWise vendor that failed on a one-year contractual limitation period and disclaimer language (case name not recovered; source page failed to load).
  - A New Hampshire non-tax software case applied the economic-loss doctrine to bar negligence and enforced a liability cap. Source: https://www.courts.nh.gov/sites/g/files/ehbemt471/files/documents/2021-07/2020055mentissciences.pdf (not read).
- **The taxpayer stays liable.** *Bunney v. Commissioner*, 114 T.C. 259 (2000): "Tax return preparation software is only as good as the information one inputs into it." *Lam*, T.C. Memo 2010-82, and *Anyika*, T.C. Memo 2011-69, are described as holding that software reliance is not reasonable cause. Confidence Medium; secondary (https://wjlta.com/2011/09/09/reliance-on-tax-preparation-software-is-not-enough-to-establish-reasonable-cause/).
- **How TurboTax disclaims** (Desktop licence, revised Sept 2025; read via fetch tool, High):
  - Provided "as-is."
  - Liability "limited to the greater of: (1) the fees that you paid ... (2) $100."
  - "Intuit is not in the business of providing legal, financial, accounting, tax" services.
  - Binding arbitration and a class waiver.
  - The accuracy guarantee pays only penalties and interest from a calculation error. It excludes "your failure to enter all required information accurately" and "misclassification of information." It requires the latest update and a claim within 30 days.
  - Source: https://www.intuit.com/legal/terms/en-us/turbotax/desktop-license/.
- **How open tools disclaim:**
  - IRS Direct File: CC0 1.0, which "makes no warranties about the work, and disclaims liability for all uses." The repository is archived and says the code "should not be used in production systems." Sources: https://github.com/IRS-Public/direct-file and its LICENSE file.
  - UsTaxes: AGPL-3.0, with a README statement that data stays in the browser's local storage. Source: https://github.com/ustaxes/UsTaxes.
  - OpenTaxSolver: "Always double-check your tax forms!!" Source: https://opentaxsolver.sourceforge.net/.
  - H&R Block and FreeTaxUSA terms were not read.
- **Open-source disclaimers.** MIT, Apache-2.0 and AGPL all disclaim warranty and liability. I did not find primary authority on their enforceability against a consumer tort claim. General contract principles (not verified here) are that disclaimers do not reach fraud, and that state consumer-protection statutes and gross-negligence rules can limit them. Treat as unverified.

### 10. Consumer protection and Treasury names

- **Intuit.** The FTC's 2024 order barred "free" claims without adequate disclosure. The Fifth Circuit vacated it on 20 March 2026, holding after *SEC v. Jarkesy* that the deceptive-advertising claim could not be adjudicated before an administrative law judge. Commentary states the court did not hold the advertising lawful. Confidence Medium; secondary (Bloomberg Law, law-firm commentary: https://www.jdsupra.com/legalnews/article-iii-judge-required-deceptive-8049008/). The opinion PDF was unreadable.
- For a tool that really is free the "free" issue is moot. The transferable lesson is to avoid unqualified claims such as "accurate," "IRS-approved," "official," or "covers all situations."
- **31 U.S.C. 333.** Prohibits using Treasury or bureau names, initials, symbols, "or any colorable imitation," in connection with a "business activity, or product" "in a manner which could reasonably be interpreted or construed as conveying the false impression" of approval or association. Civil penalty up to $5,000 per use; criminal up to $10,000 or one year. The fetch summary indicated subsection (b) makes disclaimers non-dispositive; I did not see that text quoted. Source: https://www.law.cornell.edu/uscode/text/31/333. Confidence High on (a), (c), (d).
- Referring to "IRS Form 1040" descriptively is not obviously within the prohibition. Using the IRS eagle or logo, IRS-style branding, or a product name beginning with "IRS" is.

## Risk profile by artifact

| Artifact | Federal preparer regime (7701(a)(36), 6694/6695, PTIN) | 7216 / privacy / Safeguards | UPL / state preparer law | Civil liability | Overall |
|---|---|---|---|---|---|
| (i) Open formalization as reference material | None realistic: publication, no compensation, no return prepared | None | Negligible; it is a publication | Very low, with an accuracy disclaimer | Very low |
| (ii) Interview tool run by its author on own return | None; one's own return | None | None | None; the author bears his own accuracy penalties | Negligible |
| (iii) Tool distributed free for local use | Outside while there is truly no compensation; the interview is not "mechanical," so sale or arguably donations bring in Rev. Rul. 85-189 | Status under 301.7216-1 uncertain ("in the business"); no conduct exposure if nothing leaves the machine | Low; product not service; state preparer laws are fee-based | Low to moderate: untested, with disclaimers as the main defence and misleading accuracy claims the main hazard | Low to moderate |
| (iv) Hosted version | Same compensation analysis; any fee or subscription means preparer risk | High: receives tax return information; 7216/6713, Safeguards if a business, state breach and privacy law | Higher; closer to a "service"; multi-state reach | Moderate to high: adds data-breach liability | Materially higher; do not launch without counsel |

## Implications for this project

1. **Keep it free with no strings.** No sale, paid tier, paid support, sponsorship tied to the tool, or affiliate links. Treat a donation button as a decision needing legal advice.
2. **No data leaves the machine.** No accounts, registration, telemetry, analytics, crash upload, update pings carrying return data, or cloud sync. State this in the README and make it verifiable (no network code in the interview path). If users send return data in bug reports, ask for synthetic reproductions.
3. **Do not touch e-file.** No MeF XML, no transmission, no automation of Free File Fillable Forms. Output is filled forms and a list of values the user enters.
4. **Fill the official IRS PDFs** rather than rendering look-alike forms. If custom rendering is ever needed, follow the current Pub. 1167, including the OMB number and layout rules.
5. **Wording.** Describe it as a calculator or worksheet implementing published IRS forms and instructions. State conspicuously, at first run and in the output: not tax or legal advice; not a substitute for a professional; the user is responsible for the return; not affiliated with or endorsed by the IRS or Treasury; which forms and tax years are covered and which are not.
6. **Avoid** the words "guarantee," "accurate," "official," "IRS-approved" and "certified." Avoid IRS logos or seals and any project name containing "IRS."
7. **Licence.** Use a standard licence with a warranty and liability disclaimer (Apache-2.0, MIT or AGPL-3.0) and repeat the disclaimer in the user interface. Apache-2.0 or AGPL add patent terms. AGPL also discourages others from hosting a closed fork.
8. **Scope honesty is a liability control.** Refuse loudly on unsupported situations rather than producing a plausible but wrong return. Version every rule by tax year and cite the form or instruction line.
9. **Keep the artifacts separate.** The formalization (data, pure functions, tests, citations) carries almost none of the risk, and separation preserves that if the interview tool's status ever changes.
10. **Do not host** until the lawyer questions below are answered.

## Needs a real lawyer

Prioritized:

1. **Tax-controversy or tax-procedure attorney** (preparer-penalty and 7216 experience). Does free public distribution with a donation link, sponsorship or grant create "compensation" under 7701(a)(36) and Rev. Rul. 85-189? If so, which 6695 duties attach? Ask the attorney to read 85-187, 85-188 and 85-189 in full.
2. **Same attorney.** Is an unpaid open-source maintainer "engaged in the business of providing auxiliary services" under Reg. 301.7216-1(b)(2)(iii)? What consents would a hosted version need under 301.7216-3?
3. **Privacy and data-security attorney** (GLBA/FTC), before any hosted version: Safeguards Rule coverage, state breach statutes, and state privacy laws.
4. **Technology or product-liability attorney** in the relevant state. Enforceability of the open-source disclaimer against consumer negligence, negligent-misrepresentation and state consumer-protection claims; whether to publish through an LLC; whether insurance is available.
5. **Professional-responsibility or UPL counsel**, only if distribution becomes wide. A survey of states without a Texas-style software safe harbour, and of state accountancy acts, was not done here.
6. **Trademark or advertising counsel.** A short review of the name, description and form imagery against 31 U.S.C. 333.

## Could not verify / weak spots

- **Rev. Rul. 85-189 holding not read.** Tax Notes returned 403. I rely on a headnote ("may be an income tax preparer"), search snippets and a snippet of PMTA 2000-402. Issue 2 is unknown to me. This is the most important gap.
- **Pub. 3112 (Nov 2025), Pub. 1345 (Dec 2025), Pub. 1167 PDF, Pub. 4557, Pub. 5708** were unreadable. E-file conclusions rest on Rev. Proc. 2007-40 and an IRS fact-sheet snippet; the "Online Provider" definition was not seen. Rev. Proc. 2025-27 was read only through section 5.1.2.
- **eCFR was blocked.** Regulation text comes from govinfo's CFR annual edition (1 April 2025) and Cornell LII. Amendments after that date were not checked.
- **T.D. 9375 preamble** (why software developers were added to the 7216 regulation) not retrieved.
- **IRC 6713 and 6695** not fetched directly.
- **Loving, Janson, the LegalZoom NC consent judgment, Gardner v. Conway and the Tax Court software cases** rest on secondary descriptions. The Fifth Circuit's *Intuit v. FTC* opinion (20 March 2026) was not read.
- **Civil liability** is thinly sourced: no primary case on tax-software negligence was read and none on open-source disclaimer enforceability.
- **Unlicensed-accountancy risk** was not researched.
- **Maryland** statute text and sunset status unverified. Oregon text may predate 2025-26 amendments. States beyond CA, OR, NY and MD were not surveyed.
- **H&R Block and FreeTaxUSA terms** not read. Free File Fillable Forms terms of use not checked.
- Negative findings ("no case found") reflect a handful of web searches, not a legal-database search.
- The fetch tool limits quotations to about 125 characters and summarizes through a small model. Check quoted fragments against the originals before publishing them.

## Sources

- https://www.law.cornell.edu/uscode/text/26/7701 - IRC 7701(a)(36) preparer definition
- https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol20/xml/CFR-2025-title26-vol20-sec301-7701-15.xml - Reg. 301.7701-15 (rev. 2025-04-01)
- https://www.law.cornell.edu/cfr/text/26/301.7701-15 - same regulation, LII
- https://taxnotes.com/lr/resolve//d72v - Rev. Rul. 85-189 (headnote and snippets only)
- https://www.irs.gov/pub/lanoa/pmta00402_7127.pdf - PMTA 2000-402 (unreadable; snippet only)
- https://www.law.cornell.edu/uscode/text/26/7216 - IRC 7216
- https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol20/xml/CFR-2025-title26-vol20-sec301-7216-1.xml - Reg. 301.7216-1
- https://www.irs.gov/tax-professionals/section-7216-information-center - IRS 7216 page (7 Sep 2026)
- https://www.irs.gov/tax-professionals/section-7216-frequently-asked-questions - 7216 FAQ (historical)
- https://www.law.cornell.edu/uscode/text/26/6694 - IRC 6694
- https://www.law.cornell.edu/cfr/text/26/1.6109-2 - PTIN regulation
- https://www.law.cornell.edu/cfr/text/31/10.2 and https://www.law.cornell.edu/cfr/text/31/10.8 - Circular 230
- https://www.taxpayeradvocate.irs.gov/news/nta-blog/the-tas-act-strikes-a-reasonable-balance-on-return-preparer-oversight/2025/04/ - NTA on TAS Act draft and Loving
- https://public-inspection.federalregister.gov/2025-21581.pdf - Nov 2025 withdrawal notice (snippet only)
- https://www.irs.gov/irb/2007-26_IRB - Rev. Proc. 2007-40, e-file roles
- https://www.irs.gov/e-file-providers/software-developers-technical-fact-sheet - IRS software developer fact sheet (snippet)
- https://www.irs.gov/e-file-providers/become-an-authorized-e-file-provider - e-file application page (5 Mar 2026)
- https://www.irs.gov/pub/irs-pdf/p3112.pdf and https://www.irs.gov/pub/irs-pdf/p1167.pdf - Pubs. 3112 and 1167 (unreadable)
- https://www.irs.gov/pub/irs-efile/quickalerts-january-2026.pdf - QuickAlert on Pub. 1345 TY2025 (snippet)
- https://www.irs.gov/irb/2025-44_IRB - Rev. Proc. 2025-27, substitute forms
- https://www.irs.gov/e-file-providers/free-file-fillable-forms - Free File Fillable Forms (24 Sep 2026)
- https://www.law.cornell.edu/cfr/text/16/314.2 - Safeguards Rule definitions
- https://www.law.cornell.edu/cfr/text/12/225.28 - tax preparation as financial activity
- https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know - FTC guidance (Dec 2024)
- https://www.law.cornell.edu/uscode/text/31/333 - misuse of Treasury names and symbols
- https://law.resource.org/pub/us/case/reporter/F3/179/179.F3d.956.99-10388.html - UPL Committee v. Parsons Technology (5th Cir. 1999)
- https://blog.ericgoldman.org/archives/2011/08/missouri_federa_1.htm - commentary on Janson v. LegalZoom
- https://www.nccourts.gov/assets/documents/opinions/2015_NCBC_96.pdf - LegalZoom v. N.C. State Bar (not read; snippet)
- https://www.lexplug.com/casebrief/gardner_v_conway_66f89a4af726fc18e4ae27f4 - brief of Gardner v. Conway
- https://california.public.law/codes/business_and_professions_code_section_22251 - California tax preparer definition
- https://oregon.public.law/statutes/ors_673.615 - Oregon licensing requirement
- https://newyork.public.law/laws/n.y._tax_law_section_32 - New York preparer registration definitions
- https://labor.maryland.gov/license/taxprep/taxprepreq.shtml - Maryland registration page (snippet)
- https://www.intuit.com/legal/terms/en-us/turbotax/desktop-license/ - TurboTax Desktop licence (Sept 2025)
- https://turbotax.intuit.com/corp/softwarelicense - TurboTax guarantee summary
- https://github.com/IRS-Public/direct-file and https://raw.githubusercontent.com/IRS-Public/direct-file/main/LICENSE - Direct File repository (archived) and CC0 licence
- https://github.com/ustaxes/UsTaxes - UsTaxes
- https://opentaxsolver.sourceforge.net/ - OpenTaxSolver (25 Sep 2026)
- https://wjlta.com/2011/09/09/reliance-on-tax-preparation-software-is-not-enough-to-establish-reasonable-cause/ - commentary on Bunney, Lam, Anyika
- https://www.jdsupra.com/legalnews/article-iii-judge-required-deceptive-8049008/ and https://news.bloomberglaw.com/antitrust/ftc-order-barring-free-turbotax-ads-axed-by-us-appeals-court - commentary and news on Intuit v. FTC
- https://www.ca5.uscourts.gov/opinions/pub/24/24-60040-CV0.pdf - Intuit v. FTC opinion (unreadable)
- https://www.courts.nh.gov/sites/g/files/ehbemt471/files/documents/2021-07/2020055mentissciences.pdf - NH economic-loss case (snippet)
- https://kaner.com/pdfs/Malprac.pdf - Kaner, "Computer Malpractice" (unreadable; snippet)
