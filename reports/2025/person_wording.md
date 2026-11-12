# Questions asked of a person, as stored and as shown

Written by `node engine/dist/main.js spouse-wording --report`; check-all fails when it is not current (`--report --check`).

A question asked of a person on the return is stored once, in the second person, after the frame "For this person (you, or your spouse on a joint return) —". It is shown for
the entry it is asked of (`shownFor` in `engine/src/spouse-wording.ts`): with no frame on a return with one person, after "About you" for the
taxpayer's entry of a couple's return, and after "About your spouse" for the spouse's entry, where the person is named in the third person.
The reviews read the stored text; this report is the record of the shown text.

How each word of the stored text is shown for the spouse's entry:

| Stored | Shown for the spouse | Example |
|---|---|---|
| "you" as a subject | "your spouse", and the verb after it agrees | "you have" to "your spouse has"; "you were" to "your spouse was" |
| a question's auxiliary and "you" | the auxiliary agrees | "were you" to "was your spouse", "are you" to "is your spouse", "do you" to "does your spouse", "have you" to "has your spouse"; "did you", "can you" and "could you" keep their auxiliary |
| a second verb joined by "or" or "and" | agrees too | "you had or were treated" to "your spouse had or was treated" |
| a verb after an apposition | agrees too | "you, the HSA owner, are" to "your spouse, the HSA owner, is" |
| "you" as an object | "your spouse" | "paid to you" to "paid to your spouse"; "gave you a Form W-2" to "gave your spouse a Form W-2" |
| "your" | "your spouse's" | "your Form W-2" to "your spouse's Form W-2" |
| "yours" | "your spouse's" | "another HSA of yours" to "another HSA of your spouse's" |
| "yourself" | "himself or herself" | "contributions you made for yourself" to "contributions your spouse made for himself or herself" |
| "this person", "this person's", "you (this person)" | "your spouse", "your spouse's", "your spouse" | "allocated to this person" to "allocated to your spouse" |
| "your spouse" (the husband or wife of the person asked about) | "you", and the verb after it agrees | "a joint return with your spouse" to "a joint return with you" |
| "your spouse's" | "your" before a noun, "yours" otherwise | "your spouse's Archer MSA" to "your Archer MSA"; "(your spouse's or a parent's)" to "(yours or a parent's)" |
| a phrase that means both people | as stored | "you (or your spouse, on a joint return)", "you, or your spouse on a joint return", "you and your spouse", "you or your spouse", "yours or your spouse's", "your or your spouse's", "your and your spouse's", "either of you", "both of you", "you both" |

For the taxpayer's entry only "this person" changes: "this person" to "you" with the verb agreeing ("this person was" to "you were"),
"this person's" to "your", "you (this person)" to "you".

The closed lists the rule works from (a framed question with a subject before a word in neither list fails the build):

- verbs after "you" that change for "your spouse": "are" to "is", "were" to "was", "have" to "has", "weren't" to "wasn't", "aren't" to "isn't", "don't" to "doesn't", "file" to "files", "teach" to "teaches", "contribute" to "contributes", "receive" to "receives", "stop" to "stops", "plan" to "plans", "stay" to "stays", "do" to "does"
- verbs after "this person" or "your spouse" that change for "you": "is" to "are", "was" to "were", "has" to "have", "does" to "do", "isn't" to "aren't", "wasn't" to "weren't", "doesn't" to "don't"
- words after a subject or an object that need no change: "a", "acquired", "age", "agreed", "an", "and", "applied", "applying", "as", "at", "became", "blind", "born", "by", "can", "can't", "cannot", "claimed", "contributed", "could", "covered", "deducted", "deferred", "did", "died", "enrolled", "filed", "for", "fully", "had", "have", "if", "in", "inherited", "made", "more", "never", "of", "on", "opened", "or", "overtime", "paid", "put", "received", "recharacterized", "repaid", "returned", "rolled", "served", "to", "took", "turned", "under", "with"

97 questions carry the frame.

## `person.rrta`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or did you file Form CT-2 as an employee representative?

Shown on a one-person return:

> Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or did you file Form CT-2 as an employee representative?

Shown for you on a couple's return:

> About you — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or did you file Form CT-2 as an employee representative?

Shown for your spouse:

> About your spouse — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or did your spouse file Form CT-2 as an employee representative?

**Help, as stored**

> Yes if any of this person's Forms W-2 reports railroad retirement (RRTA) compensation or tax in box 14, or this person filed Form CT-2 as an employee representative. Railroad retirement compensation is outside this tool and is refused.

Shown on a one-person return:

> Yes if any of your Forms W-2 reports railroad retirement (RRTA) compensation or tax in box 14, or you filed Form CT-2 as an employee representative. Railroad retirement compensation is outside this tool and is refused.

Shown for you on a couple's return:

> Yes if any of your Forms W-2 reports railroad retirement (RRTA) compensation or tax in box 14, or you filed Form CT-2 as an employee representative. Railroad retirement compensation is outside this tool and is refused.

Shown for your spouse:

> Yes if any of your spouse's Forms W-2 reports railroad retirement (RRTA) compensation or tax in box 14, or your spouse filed Form CT-2 as an employee representative. Railroad retirement compensation is outside this tool and is refused.

## `person.age65`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you born before January 2, 1961?

Shown on a one-person return:

> Were you born before January 2, 1961?

Shown for you on a couple's return:

> About you — Were you born before January 2, 1961?

Shown for your spouse:

> About your spouse — Was your spouse born before January 2, 1961?

**Help, as stored**

> Yes if this person was born before January 2, 1961. It counts for the age box on Form 1040 line 12d and the higher standard deduction.

Shown on a one-person return:

> Yes if you were born before January 2, 1961. It counts for the age box on Form 1040 line 12d and the higher standard deduction.

Shown for you on a couple's return:

> Yes if you were born before January 2, 1961. It counts for the age box on Form 1040 line 12d and the higher standard deduction.

Shown for your spouse:

> Yes if your spouse was born before January 2, 1961. It counts for the age box on Form 1040 line 12d and the higher standard deduction.

## `person.blind`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you blind at the end of 2025?
>
> Answer yes if you were totally blind as of December 31, 2025.
>
> If you weren't totally blind, answer yes only if you have a statement certified by your eye doctor (ophthalmologist or optometrist) that you can't see better than 20/200 in your better eye with glasses or contact lenses, or that your field of vision is 20 degrees or less (or, if your eye condition isn't likely to improve beyond these conditions, a certified statement to that effect).
>
> If your vision can be corrected beyond these limits only by contact lenses that you can wear only briefly because of pain, infection or ulcers, answer yes.
>
> Keep the statement for your records.

Shown on a one-person return:

> Were you blind at the end of 2025?
>
> Answer yes if you were totally blind as of December 31, 2025.
>
> If you weren't totally blind, answer yes only if you have a statement certified by your eye doctor (ophthalmologist or optometrist) that you can't see better than 20/200 in your better eye with glasses or contact lenses, or that your field of vision is 20 degrees or less (or, if your eye condition isn't likely to improve beyond these conditions, a certified statement to that effect).
>
> If your vision can be corrected beyond these limits only by contact lenses that you can wear only briefly because of pain, infection or ulcers, answer yes.
>
> Keep the statement for your records.

Shown for you on a couple's return:

> About you — Were you blind at the end of 2025?
>
> Answer yes if you were totally blind as of December 31, 2025.
>
> If you weren't totally blind, answer yes only if you have a statement certified by your eye doctor (ophthalmologist or optometrist) that you can't see better than 20/200 in your better eye with glasses or contact lenses, or that your field of vision is 20 degrees or less (or, if your eye condition isn't likely to improve beyond these conditions, a certified statement to that effect).
>
> If your vision can be corrected beyond these limits only by contact lenses that you can wear only briefly because of pain, infection or ulcers, answer yes.
>
> Keep the statement for your records.

Shown for your spouse:

> About your spouse — Was your spouse blind at the end of 2025?
>
> Answer yes if your spouse was totally blind as of December 31, 2025.
>
> If your spouse wasn't totally blind, answer yes only if your spouse has a statement certified by your spouse's eye doctor (ophthalmologist or optometrist) that your spouse can't see better than 20/200 in your spouse's better eye with glasses or contact lenses, or that your spouse's field of vision is 20 degrees or less (or, if your spouse's eye condition isn't likely to improve beyond these conditions, a certified statement to that effect).
>
> If your spouse's vision can be corrected beyond these limits only by contact lenses that your spouse can wear only briefly because of pain, infection or ulcers, answer yes.
>
> Keep the statement for your spouse's records.

**Help, as stored**

> Yes if this person was blind at the end of 2025, as the question defines it; if not totally blind, a statement certified by an eye doctor is needed. It counts for the blindness box on Form 1040 line 12d.

Shown on a one-person return:

> Yes if you were blind at the end of 2025, as the question defines it; if not totally blind, a statement certified by an eye doctor is needed. It counts for the blindness box on Form 1040 line 12d.

Shown for you on a couple's return:

> Yes if you were blind at the end of 2025, as the question defines it; if not totally blind, a statement certified by an eye doctor is needed. It counts for the blindness box on Form 1040 line 12d.

Shown for your spouse:

> Yes if your spouse was blind at the end of 2025, as the question defines it; if not totally blind, a statement certified by an eye doctor is needed. It counts for the blindness box on Form 1040 line 12d.

## `$w2`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — List the employers that gave you a Form W-2, one entry per employer. If one employer gave you more than one Form W-2, list that employer once and enter their boxes combined.

Shown on a one-person return:

> List the employers that gave you a Form W-2, one entry per employer. If one employer gave you more than one Form W-2, list that employer once and enter their boxes combined.

Shown for you on a couple's return:

> About you — List the employers that gave you a Form W-2, one entry per employer. If one employer gave you more than one Form W-2, list that employer once and enter their boxes combined.

Shown for your spouse:

> About your spouse — List the employers that gave your spouse a Form W-2, one entry per employer. If one employer gave your spouse more than one Form W-2, list that employer once and enter their boxes combined.

**Help, as stored**

> One entry per distinct employer, not per Form W-2: the excess social security credit turns on the number of employers, so an employer's corrected or additional Forms W-2 are combined under that employer. Leave the list empty if there are none. Forms W-2 and Forms 1099-R (IRA distributions, pensions and annuities) are entered under the person who received them. Amounts that are not asked person by person (interest, dividends, sales, social security benefits, deductions, payments) are entered once, for you and your spouse combined.

Shown on a one-person return:

> One entry per distinct employer, not per Form W-2: the excess social security credit turns on the number of employers, so an employer's corrected or additional Forms W-2 are combined under that employer. Leave the list empty if there are none. Forms W-2 and Forms 1099-R (IRA distributions, pensions and annuities) are entered under the person who received them. Amounts that are not asked person by person (interest, dividends, sales, social security benefits, deductions, payments) are entered once, for you and your spouse combined.

Shown for you on a couple's return:

> One entry per distinct employer, not per Form W-2: the excess social security credit turns on the number of employers, so an employer's corrected or additional Forms W-2 are combined under that employer. Leave the list empty if there are none. Forms W-2 and Forms 1099-R (IRA distributions, pensions and annuities) are entered under the person who received them. Amounts that are not asked person by person (interest, dividends, sales, social security benefits, deductions, payments) are entered once, for you and your spouse combined.

Shown for your spouse:

> One entry per distinct employer, not per Form W-2: the excess social security credit turns on the number of employers, so an employer's corrected or additional Forms W-2 are combined under that employer. Leave the list empty if there are none. Forms W-2 and Forms 1099-R (IRA distributions, pensions and annuities) are entered under the person who received them. Amounts that are not asked person by person (interest, dividends, sales, social security benefits, deductions, payments) are entered once, for you and your spouse combined.

## `person.tin`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Do you have an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? An ITIN that has expired counts only if it has been renewed by then (a renewal only applied for does not count here).

Shown on a one-person return:

> Do you have an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? An ITIN that has expired counts only if it has been renewed by then (a renewal only applied for does not count here).

Shown for you on a couple's return:

> About you — Do you have an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? An ITIN that has expired counts only if it has been renewed by then (a renewal only applied for does not count here).

Shown for your spouse:

> About your spouse — Does your spouse have an SSN or ITIN issued on or before the due date of your spouse's 2025 return (including extensions)? An ITIN that has expired counts only if it has been renewed by then (a renewal only applied for does not count here).

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.itin_applied`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — If you have neither (or your ITIN has expired and was not renewed), have you applied, or are you applying, for an ITIN, or for the renewal of your expired ITIN, on or before the due date of your 2025 return (including extensions)? Answer Yes if you are applying with this return, for example by filing Form W-7 with it.

Shown on a one-person return:

> If you have neither (or your ITIN has expired and was not renewed), have you applied, or are you applying, for an ITIN, or for the renewal of your expired ITIN, on or before the due date of your 2025 return (including extensions)? Answer Yes if you are applying with this return, for example by filing Form W-7 with it.

Shown for you on a couple's return:

> About you — If you have neither (or your ITIN has expired and was not renewed), have you applied, or are you applying, for an ITIN, or for the renewal of your expired ITIN, on or before the due date of your 2025 return (including extensions)? Answer Yes if you are applying with this return, for example by filing Form W-7 with it.

Shown for your spouse:

> About your spouse — If your spouse has neither (or your spouse's ITIN has expired and was not renewed), has your spouse applied, or is your spouse applying, for an ITIN, or for the renewal of your spouse's expired ITIN, on or before the due date of your spouse's 2025 return (including extensions)? Answer Yes if your spouse is applying with this return, for example by filing Form W-7 with it.

**Help, as stored**

> An application (or a renewal application) by the due date counts for the credit for other dependents, but not for the child tax credit, and for this person as a student for the American opportunity credit; the lifetime learning credit for a student whose ITIN was only applied for is refused.

Shown on a one-person return:

> An application (or a renewal application) by the due date counts for the credit for other dependents, but not for the child tax credit, and for you as a student for the American opportunity credit; the lifetime learning credit for a student whose ITIN was only applied for is refused.

Shown for you on a couple's return:

> An application (or a renewal application) by the due date counts for the credit for other dependents, but not for the child tax credit, and for you as a student for the American opportunity credit; the lifetime learning credit for a student whose ITIN was only applied for is refused.

Shown for your spouse:

> An application (or a renewal application) by the due date counts for the credit for other dependents, but not for the child tax credit, and for your spouse as a student for the American opportunity credit; the lifetime learning credit for a student whose ITIN was only applied for is refused.

## `person.work_ssn`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Do you have an SSN valid for employment, issued before the due date of your 2025 return (including extensions)? If your card says "Valid for Work Only With DHS Authorization", answer yes only if the DHS authorization is valid.

Shown on a one-person return:

> Do you have an SSN valid for employment, issued before the due date of your 2025 return (including extensions)? If your card says "Valid for Work Only With DHS Authorization", answer yes only if the DHS authorization is valid.

Shown for you on a couple's return:

> About you — Do you have an SSN valid for employment, issued before the due date of your 2025 return (including extensions)? If your card says "Valid for Work Only With DHS Authorization", answer yes only if the DHS authorization is valid.

Shown for your spouse:

> About your spouse — Does your spouse have an SSN valid for employment, issued before the due date of your spouse's 2025 return (including extensions)? If your spouse's card says "Valid for Work Only With DHS Authorization", answer yes only if the DHS authorization is valid.

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.eic_ssn`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Do you have a social security number issued on or before the due date of your 2025 return (including extensions) that is valid for the EIC? Any number issued by the Social Security Administration is valid unless the card says "Not Valid for Employment" and the number was issued solely to apply for or receive a federally funded benefit; a card that says "Valid for Work Only With DHS Authorization" is valid only while the authorization is valid.

Shown on a one-person return:

> Do you have a social security number issued on or before the due date of your 2025 return (including extensions) that is valid for the EIC? Any number issued by the Social Security Administration is valid unless the card says "Not Valid for Employment" and the number was issued solely to apply for or receive a federally funded benefit; a card that says "Valid for Work Only With DHS Authorization" is valid only while the authorization is valid.

Shown for you on a couple's return:

> About you — Do you have a social security number issued on or before the due date of your 2025 return (including extensions) that is valid for the EIC? Any number issued by the Social Security Administration is valid unless the card says "Not Valid for Employment" and the number was issued solely to apply for or receive a federally funded benefit; a card that says "Valid for Work Only With DHS Authorization" is valid only while the authorization is valid.

Shown for your spouse:

> About your spouse — Does your spouse have a social security number issued on or before the due date of your spouse's 2025 return (including extensions) that is valid for the EIC? Any number issued by the Social Security Administration is valid unless the card says "Not Valid for Employment" and the number was issued solely to apply for or receive a federally funded benefit; a card that says "Valid for Work Only With DHS Authorization" is valid only while the authorization is valid.

**Help, as stored**

> This is the earned income credit's definition of a valid SSN, which differs from the child tax credit's "valid for employment" question asked earlier.

Shown on a one-person return:

> This is the earned income credit's definition of a valid SSN, which differs from the child tax credit's "valid for employment" question asked earlier.

Shown for you on a couple's return:

> This is the earned income credit's definition of a valid SSN, which differs from the child tax credit's "valid for employment" question asked earlier.

Shown for your spouse:

> This is the earned income credit's definition of a valid SSN, which differs from the child tax credit's "valid for employment" question asked earlier.

## `person.under16`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you under age 16 at the end of 2025?

Shown on a one-person return:

> Were you under age 16 at the end of 2025?

Shown for you on a couple's return:

> About you — Were you under age 16 at the end of 2025?

Shown for your spouse:

> About your spouse — Was your spouse under age 16 at the end of 2025?

**Help, as stored**

> A return for a person under age 16 at the end of 2025 (you, or your spouse on a joint return) is outside this tool.

Shown on a one-person return:

> A return for a person under age 16 at the end of 2025 (you, or your spouse on a joint return) is outside this tool.

Shown for you on a couple's return:

> A return for a person under age 16 at the end of 2025 (you, or your spouse on a joint return) is outside this tool.

Shown for your spouse:

> A return for a person under age 16 at the end of 2025 (you, or your spouse on a joint return) is outside this tool.

## `person.born_before_2001`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you born before January 2, 2001?

Shown on a one-person return:

> Were you born before January 2, 2001?

Shown for you on a couple's return:

> About you — Were you born before January 2, 2001?

Shown for your spouse:

> About your spouse — Was your spouse born before January 2, 2001?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.born_after_1960`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you born after December 31, 1960?

Shown on a one-person return:

> Were you born after December 31, 1960?

Shown for you on a couple's return:

> About you — Were you born after December 31, 1960?

Shown for your spouse:

> About your spouse — Was your spouse born after December 31, 1960?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did anyone pay qualified education expenses in 2025 for this person at an eligible educational institution (a college, university, vocational school, or other postsecondary school eligible for federal student aid)?

Shown on a one-person return:

> Did anyone pay qualified education expenses in 2025 for you at an eligible educational institution (a college, university, vocational school, or other postsecondary school eligible for federal student aid)?

Shown for you on a couple's return:

> About you — Did anyone pay qualified education expenses in 2025 for you at an eligible educational institution (a college, university, vocational school, or other postsecondary school eligible for federal student aid)?

Shown for your spouse:

> About your spouse — Did anyone pay qualified education expenses in 2025 for your spouse at an eligible educational institution (a college, university, vocational school, or other postsecondary school eligible for federal student aid)?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_1098t`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did the student receive a 2025 Form 1098-T from the educational institution? Answer yes also if the institution was not required to furnish one (for example a qualified nonresident alien, expenses paid entirely with scholarships or under a formal billing arrangement, or only courses for which no academic credit is awarded), or if the institution did not furnish it and, after February 2, 2026, but before you file, you or the student requested it, you fully cooperated with the institution's efforts to gather the information needed to furnish it, and you can show the enrollment and the payments.

Shown on a one-person return:

> Did the student receive a 2025 Form 1098-T from the educational institution? Answer yes also if the institution was not required to furnish one (for example a qualified nonresident alien, expenses paid entirely with scholarships or under a formal billing arrangement, or only courses for which no academic credit is awarded), or if the institution did not furnish it and, after February 2, 2026, but before you file, you or the student requested it, you fully cooperated with the institution's efforts to gather the information needed to furnish it, and you can show the enrollment and the payments.

Shown for you on a couple's return:

> About you — Did the student receive a 2025 Form 1098-T from the educational institution? Answer yes also if the institution was not required to furnish one (for example a qualified nonresident alien, expenses paid entirely with scholarships or under a formal billing arrangement, or only courses for which no academic credit is awarded), or if the institution did not furnish it and, after February 2, 2026, but before you file, you or the student requested it, you fully cooperated with the institution's efforts to gather the information needed to furnish it, and you can show the enrollment and the payments.

Shown for your spouse:

> About your spouse — Did the student receive a 2025 Form 1098-T from the educational institution? Answer yes also if the institution was not required to furnish one (for example a qualified nonresident alien, expenses paid entirely with scholarships or under a formal billing arrangement, or only courses for which no academic credit is awarded), or if the institution did not furnish it and, after February 2, 2026, but before your spouse files, your spouse or the student requested it, your spouse fully cooperated with the institution's efforts to gather the information needed to furnish it, and your spouse can show the enrollment and the payments.

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_inst`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Qualified education expenses paid in 2025 for this student, by anyone, that had to be paid to the institution, for academic periods beginning in 2025 or in the first 3 months of 2026:
>
> - tuition
> - required enrollment fees
> - books, supplies and equipment required to be paid to the institution as a condition of enrollment or attendance
>
> Use the amounts actually paid, which may differ from Form 1098-T box 1.
>
> Do not include:
> - amounts paid in 2024 or 2026
> - room and board
> - insurance
> - medical expenses (including student health fees)
> - transportation
> - expenses deducted elsewhere (for example on Schedule C)
> - expenses used for a tax-free distribution from a Coverdell ESA or qualified tuition program (529 plan)
> - a course or other education involving sports, games or hobbies, or any noncredit course, unless it is part of the student's degree program or, where this student can't get the American opportunity credit, it helps the student acquire or improve job skills
>
> Zero if none

Shown on a one-person return:

> Qualified education expenses paid in 2025 for this student, by anyone, that had to be paid to the institution, for academic periods beginning in 2025 or in the first 3 months of 2026:
>
> - tuition
> - required enrollment fees
> - books, supplies and equipment required to be paid to the institution as a condition of enrollment or attendance
>
> Use the amounts actually paid, which may differ from Form 1098-T box 1.
>
> Do not include:
> - amounts paid in 2024 or 2026
> - room and board
> - insurance
> - medical expenses (including student health fees)
> - transportation
> - expenses deducted elsewhere (for example on Schedule C)
> - expenses used for a tax-free distribution from a Coverdell ESA or qualified tuition program (529 plan)
> - a course or other education involving sports, games or hobbies, or any noncredit course, unless it is part of the student's degree program or, where this student can't get the American opportunity credit, it helps the student acquire or improve job skills
>
> Zero if none

Shown for you on a couple's return:

> About you — Qualified education expenses paid in 2025 for this student, by anyone, that had to be paid to the institution, for academic periods beginning in 2025 or in the first 3 months of 2026:
>
> - tuition
> - required enrollment fees
> - books, supplies and equipment required to be paid to the institution as a condition of enrollment or attendance
>
> Use the amounts actually paid, which may differ from Form 1098-T box 1.
>
> Do not include:
> - amounts paid in 2024 or 2026
> - room and board
> - insurance
> - medical expenses (including student health fees)
> - transportation
> - expenses deducted elsewhere (for example on Schedule C)
> - expenses used for a tax-free distribution from a Coverdell ESA or qualified tuition program (529 plan)
> - a course or other education involving sports, games or hobbies, or any noncredit course, unless it is part of the student's degree program or, where this student can't get the American opportunity credit, it helps the student acquire or improve job skills
>
> Zero if none

Shown for your spouse:

> About your spouse — Qualified education expenses paid in 2025 for this student, by anyone, that had to be paid to the institution, for academic periods beginning in 2025 or in the first 3 months of 2026:
>
> - tuition
> - required enrollment fees
> - books, supplies and equipment required to be paid to the institution as a condition of enrollment or attendance
>
> Use the amounts actually paid, which may differ from Form 1098-T box 1.
>
> Do not include:
> - amounts paid in 2024 or 2026
> - room and board
> - insurance
> - medical expenses (including student health fees)
> - transportation
> - expenses deducted elsewhere (for example on Schedule C)
> - expenses used for a tax-free distribution from a Coverdell ESA or qualified tuition program (529 plan)
> - a course or other education involving sports, games or hobbies, or any noncredit course, unless it is part of the student's degree program or, where this student can't get the American opportunity credit, it helps the student acquire or improve job skills
>
> Zero if none

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_mat`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Other course materials paid for in 2025 for this student: books, supplies and equipment needed for a course of study that did not have to be paid to the institution (they count for the American opportunity credit only); the same exclusions as for the expenses paid to the institution; zero if none

Shown on a one-person return:

> Other course materials paid for in 2025 for this student: books, supplies and equipment needed for a course of study that did not have to be paid to the institution (they count for the American opportunity credit only); the same exclusions as for the expenses paid to the institution; zero if none

Shown for you on a couple's return:

> About you — Other course materials paid for in 2025 for this student: books, supplies and equipment needed for a course of study that did not have to be paid to the institution (they count for the American opportunity credit only); the same exclusions as for the expenses paid to the institution; zero if none

Shown for your spouse:

> About your spouse — Other course materials paid for in 2025 for this student: books, supplies and equipment needed for a course of study that did not have to be paid to the institution (they count for the American opportunity credit only); the same exclusions as for the expenses paid to the institution; zero if none

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_a2025`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Tax-free educational assistance received in 2025 for this student's 2025 expenses: the tax-free part of scholarships and fellowship grants (including Pell grants; Form 1098-T box 5 may help), tax-free employer-provided educational assistance, veterans' educational assistance, and other tax-free educational assistance. Do not include wages, loans, gifts, inheritances, withdrawals from personal savings, emergency financial aid grants, or a scholarship the student includes in income (for you or your spouse, the amount on Schedule 1 line 8r); zero if none

Shown on a one-person return:

> Tax-free educational assistance received in 2025 for this student's 2025 expenses: the tax-free part of scholarships and fellowship grants (including Pell grants; Form 1098-T box 5 may help), tax-free employer-provided educational assistance, veterans' educational assistance, and other tax-free educational assistance. Do not include wages, loans, gifts, inheritances, withdrawals from personal savings, emergency financial aid grants, or a scholarship the student includes in income (for you or your spouse, the amount on Schedule 1 line 8r); zero if none

Shown for you on a couple's return:

> About you — Tax-free educational assistance received in 2025 for this student's 2025 expenses: the tax-free part of scholarships and fellowship grants (including Pell grants; Form 1098-T box 5 may help), tax-free employer-provided educational assistance, veterans' educational assistance, and other tax-free educational assistance. Do not include wages, loans, gifts, inheritances, withdrawals from personal savings, emergency financial aid grants, or a scholarship the student includes in income (for you or your spouse, the amount on Schedule 1 line 8r); zero if none

Shown for your spouse:

> About your spouse — Tax-free educational assistance received in 2025 for this student's 2025 expenses: the tax-free part of scholarships and fellowship grants (including Pell grants; Form 1098-T box 5 may help), tax-free employer-provided educational assistance, veterans' educational assistance, and other tax-free educational assistance. Do not include wages, loans, gifts, inheritances, withdrawals from personal savings, emergency financial aid grants, or a scholarship the student includes in income (for you or your spouse, the amount on Schedule 1 line 8r); zero if none

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_a2026`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Tax-free educational assistance received in 2026, before you file this return, that is allocable to an academic period of these 2025 expenses; zero if none

Shown on a one-person return:

> Tax-free educational assistance received in 2026, before you file this return, that is allocable to an academic period of these 2025 expenses; zero if none

Shown for you on a couple's return:

> About you — Tax-free educational assistance received in 2026, before you file this return, that is allocable to an academic period of these 2025 expenses; zero if none

Shown for your spouse:

> About your spouse — Tax-free educational assistance received in 2026, before your spouse files this return, that is allocable to an academic period of these 2025 expenses; zero if none

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_refunds`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Refunds of these 2025 qualified education expenses received in 2025, or in 2026 before you file this return; zero if none

Shown on a one-person return:

> Refunds of these 2025 qualified education expenses received in 2025, or in 2026 before you file this return; zero if none

Shown for you on a couple's return:

> About you — Refunds of these 2025 qualified education expenses received in 2025, or in 2026 before you file this return; zero if none

Shown for your spouse:

> About your spouse — Refunds of these 2025 qualified education expenses received in 2025, or in 2026 before your spouse files this return; zero if none

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_line23`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Has the American opportunity credit been claimed (by you or anyone else) for this student for any 4 tax years before 2025?

Shown on a one-person return:

> Has the American opportunity credit been claimed (by you or anyone else) for this student for any 4 tax years before 2025?

Shown for you on a couple's return:

> About you — Has the American opportunity credit been claimed (by you or anyone else) for this student for any 4 tax years before 2025?

Shown for your spouse:

> About your spouse — Has the American opportunity credit been claimed (by your spouse or anyone else) for this student for any 4 tax years before 2025?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_line24`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Was the student enrolled at least half-time (Form 1098-T box 8) for at least one academic period that began in 2025, or in the first 3 months of 2026 if paid for in 2025, at an eligible educational institution, in a program leading toward a postsecondary degree, certificate or other recognized postsecondary educational credential?

Shown on a one-person return:

> Was the student enrolled at least half-time (Form 1098-T box 8) for at least one academic period that began in 2025, or in the first 3 months of 2026 if paid for in 2025, at an eligible educational institution, in a program leading toward a postsecondary degree, certificate or other recognized postsecondary educational credential?

Shown for you on a couple's return:

> About you — Was the student enrolled at least half-time (Form 1098-T box 8) for at least one academic period that began in 2025, or in the first 3 months of 2026 if paid for in 2025, at an eligible educational institution, in a program leading toward a postsecondary degree, certificate or other recognized postsecondary educational credential?

Shown for your spouse:

> About your spouse — Was the student enrolled at least half-time (Form 1098-T box 8) for at least one academic period that began in 2025, or in the first 3 months of 2026 if paid for in 2025, at an eligible educational institution, in a program leading toward a postsecondary degree, certificate or other recognized postsecondary educational credential?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_line25`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did the student complete the first 4 years of postsecondary education before 2025, as determined by the institution (4 years of academic credit, not counting credit awarded solely for proficiency examinations)?

Shown on a one-person return:

> Did the student complete the first 4 years of postsecondary education before 2025, as determined by the institution (4 years of academic credit, not counting credit awarded solely for proficiency examinations)?

Shown for you on a couple's return:

> About you — Did the student complete the first 4 years of postsecondary education before 2025, as determined by the institution (4 years of academic credit, not counting credit awarded solely for proficiency examinations)?

Shown for your spouse:

> About your spouse — Did the student complete the first 4 years of postsecondary education before 2025, as determined by the institution (4 years of academic credit, not counting credit awarded solely for proficiency examinations)?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_line26`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Was the student convicted, before the end of 2025, of a federal or state felony for possession or distribution of a controlled substance?

Shown on a one-person return:

> Was the student convicted, before the end of 2025, of a federal or state felony for possession or distribution of a controlled substance?

Shown for you on a couple's return:

> About you — Was the student convicted, before the end of 2025, of a federal or state felony for possession or distribution of a controlled substance?

Shown for your spouse:

> About your spouse — Was the student convicted, before the end of 2025, of a federal or state felony for possession or distribution of a controlled substance?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_ein`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Do you have the educational institution's employer identification number (EIN), from Form 1098-T or from the institution?

Shown on a one-person return:

> Do you have the educational institution's employer identification number (EIN), from Form 1098-T or from the institution?

Shown for you on a couple's return:

> About you — Do you have the educational institution's employer identification number (EIN), from Form 1098-T or from the institution?

Shown for your spouse:

> About your spouse — Does your spouse have the educational institution's employer identification number (EIN), from Form 1098-T or from the institution?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_over`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Was there an academic period for which the tax-free educational assistance and refunds allocable to it were more than that period's qualified education expenses that had to be paid to the institution (tuition, required fees and course materials required to be paid to the institution)?

Shown on a one-person return:

> Was there an academic period for which the tax-free educational assistance and refunds allocable to it were more than that period's qualified education expenses that had to be paid to the institution (tuition, required fees and course materials required to be paid to the institution)?

Shown for you on a couple's return:

> About you — Was there an academic period for which the tax-free educational assistance and refunds allocable to it were more than that period's qualified education expenses that had to be paid to the institution (tuition, required fees and course materials required to be paid to the institution)?

Shown for your spouse:

> About your spouse — Was there an academic period for which the tax-free educational assistance and refunds allocable to it were more than that period's qualified education expenses that had to be paid to the institution (tuition, required fees and course materials required to be paid to the institution)?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_born_2007`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you born before January 2, 2007?

Shown on a one-person return:

> Were you born before January 2, 2007?

Shown for you on a couple's return:

> About you — Were you born before January 2, 2007?

Shown for your spouse:

> About your spouse — Was your spouse born before January 2, 2007?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_born_2002`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you born before January 2, 2002?

Shown on a one-person return:

> Were you born before January 2, 2002?

Shown for you on a couple's return:

> About you — Were you born before January 2, 2002?

Shown for your spouse:

> About your spouse — Was your spouse born before January 2, 2002?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_fulltime`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you a full-time student for 2025: during any part of any 5 calendar months of 2025, were you enrolled as a full-time student at an eligible educational institution, or did you take a full-time, on-farm training course given by such an institution or by a state, county, or local government agency?

Shown on a one-person return:

> Were you a full-time student for 2025: during any part of any 5 calendar months of 2025, were you enrolled as a full-time student at an eligible educational institution, or did you take a full-time, on-farm training course given by such an institution or by a state, county, or local government agency?

Shown for you on a couple's return:

> About you — Were you a full-time student for 2025: during any part of any 5 calendar months of 2025, were you enrolled as a full-time student at an eligible educational institution, or did you take a full-time, on-farm training course given by such an institution or by a state, county, or local government agency?

Shown for your spouse:

> About your spouse — Was your spouse a full-time student for 2025: during any part of any 5 calendar months of 2025, was your spouse enrolled as a full-time student at an eligible educational institution, or did your spouse take a full-time, on-farm training course given by such an institution or by a state, county, or local government agency?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_half_support`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Was your earned income for 2025 less than one-half of your support? Earned income is wages, salaries, professional fees and other pay for personal services (including the part of a scholarship that pays for teaching, research or other required services). Support includes food, shelter, clothing, medical and dental care, education and the like, provided by you, your parents and others; a scholarship is not support if you were a full-time student.

Shown on a one-person return:

> Was your earned income for 2025 less than one-half of your support? Earned income is wages, salaries, professional fees and other pay for personal services (including the part of a scholarship that pays for teaching, research or other required services). Support includes food, shelter, clothing, medical and dental care, education and the like, provided by you, your parents and others; a scholarship is not support if you were a full-time student.

Shown for you on a couple's return:

> About you — Was your earned income for 2025 less than one-half of your support? Earned income is wages, salaries, professional fees and other pay for personal services (including the part of a scholarship that pays for teaching, research or other required services). Support includes food, shelter, clothing, medical and dental care, education and the like, provided by you, your parents and others; a scholarship is not support if you were a full-time student.

Shown for your spouse:

> About your spouse — Was your spouse's earned income for 2025 less than one-half of your spouse's support? Earned income is wages, salaries, professional fees and other pay for personal services (including the part of a scholarship that pays for teaching, research or other required services). Support includes food, shelter, clothing, medical and dental care, education and the like, provided by your spouse, your spouse's parents and others; a scholarship is not support if your spouse was a full-time student.

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.edu_parent`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Was at least one of your parents alive at the end of 2025?

Shown on a one-person return:

> Was at least one of your parents alive at the end of 2025?

Shown for you on a couple's return:

> About you — Was at least one of your parents alive at the end of 2025?

Shown for your spouse:

> About your spouse — Was at least one of your spouse's parents alive at the end of 2025?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.x_other`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Does any of these apply to you?
>
> - a taxable distribution from a Coverdell ESA, a qualified tuition program (529 plan) or an ABLE account
> - excess contributions to a traditional or Roth IRA for an earlier year that remained in the IRA at the end of 2025 (whether or not you contributed for 2025)
> - excess contributions to a Coverdell ESA, an Archer MSA or an ABLE account
> - excess HSA contributions from an earlier year that you had not removed or used up before 2025 (including any amount on line 48 of your 2024 Form 5329, or an excess you never reported), whether or not you have a Form 8889 for 2025
> - a required minimum distribution from an IRA or plan that you did not receive in full by its deadline (including a shortfall you made up later)

Shown on a one-person return:

> Does any of these apply to you?
>
> - a taxable distribution from a Coverdell ESA, a qualified tuition program (529 plan) or an ABLE account
> - excess contributions to a traditional or Roth IRA for an earlier year that remained in the IRA at the end of 2025 (whether or not you contributed for 2025)
> - excess contributions to a Coverdell ESA, an Archer MSA or an ABLE account
> - excess HSA contributions from an earlier year that you had not removed or used up before 2025 (including any amount on line 48 of your 2024 Form 5329, or an excess you never reported), whether or not you have a Form 8889 for 2025
> - a required minimum distribution from an IRA or plan that you did not receive in full by its deadline (including a shortfall you made up later)

Shown for you on a couple's return:

> About you — Does any of these apply to you?
>
> - a taxable distribution from a Coverdell ESA, a qualified tuition program (529 plan) or an ABLE account
> - excess contributions to a traditional or Roth IRA for an earlier year that remained in the IRA at the end of 2025 (whether or not you contributed for 2025)
> - excess contributions to a Coverdell ESA, an Archer MSA or an ABLE account
> - excess HSA contributions from an earlier year that you had not removed or used up before 2025 (including any amount on line 48 of your 2024 Form 5329, or an excess you never reported), whether or not you have a Form 8889 for 2025
> - a required minimum distribution from an IRA or plan that you did not receive in full by its deadline (including a shortfall you made up later)

Shown for your spouse:

> About your spouse — Does any of these apply to your spouse?
>
> - a taxable distribution from a Coverdell ESA, a qualified tuition program (529 plan) or an ABLE account
> - excess contributions to a traditional or Roth IRA for an earlier year that remained in the IRA at the end of 2025 (whether or not your spouse contributed for 2025)
> - excess contributions to a Coverdell ESA, an Archer MSA or an ABLE account
> - excess HSA contributions from an earlier year that your spouse had not removed or used up before 2025 (including any amount on line 48 of your spouse's 2024 Form 5329, or an excess your spouse never reported), whether or not your spouse has a Form 8889 for 2025
> - a required minimum distribution from an IRA or plan that your spouse did not receive in full by its deadline (including a shortfall your spouse made up later)

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.x_prior09`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Total of your earlier IRA distributions (before 2025) for which the first-home exception was used; zero if none

Shown on a one-person return:

> Total of your earlier IRA distributions (before 2025) for which the first-home exception was used; zero if none

Shown for you on a couple's return:

> About you — Total of your earlier IRA distributions (before 2025) for which the first-home exception was used; zero if none

Shown for your spouse:

> About your spouse — Total of your spouse's earlier IRA distributions (before 2025) for which the first-home exception was used; zero if none

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.x_births`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — For how many births or adoptions (children born or adopted, each counted once) did you take the birth or adoption distributions?

Shown on a one-person return:

> For how many births or adoptions (children born or adopted, each counted once) did you take the birth or adoption distributions?

Shown for you on a couple's return:

> About you — For how many births or adoptions (children born or adopted, each counted once) did you take the birth or adoption distributions?

Shown for your spouse:

> About your spouse — For how many births or adoptions (children born or adopted, each counted once) did your spouse take the birth or adoption distributions?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `$retirement`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — List each Form 1099-R this person received, one entry per form (for example by payer). Leave the list empty if this person received none.

Shown on a one-person return:

> List each Form 1099-R you received, one entry per form (for example by payer). Leave the list empty if you received none.

Shown for you on a couple's return:

> About you — List each Form 1099-R you received, one entry per form (for example by payer). Leave the list empty if you received none.

Shown for your spouse:

> About your spouse — List each Form 1099-R your spouse received, one entry per form (for example by payer). Leave the list empty if your spouse received none.

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.educator_expenses`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Qualified educator expenses you paid in 2025 (professional development courses you took that are related to the curriculum you teach or to the students you teach, and books, supplies, equipment (including computer equipment, software and services) and other materials used in the classroom, including personal protective equipment, disinfectant and other supplies used to prevent the spread of coronavirus; not expenses for home schooling or nonathletic supplies for courses in health or physical education), reduced by excludable savings bond interest (Form 8815), nontaxable qualified tuition program or Coverdell earnings or distributions, and reimbursements not reported in box 1 of your Form W-2; zero if none

Shown on a one-person return:

> Qualified educator expenses you paid in 2025 (professional development courses you took that are related to the curriculum you teach or to the students you teach, and books, supplies, equipment (including computer equipment, software and services) and other materials used in the classroom, including personal protective equipment, disinfectant and other supplies used to prevent the spread of coronavirus; not expenses for home schooling or nonathletic supplies for courses in health or physical education), reduced by excludable savings bond interest (Form 8815), nontaxable qualified tuition program or Coverdell earnings or distributions, and reimbursements not reported in box 1 of your Form W-2; zero if none

Shown for you on a couple's return:

> About you — Qualified educator expenses you paid in 2025 (professional development courses you took that are related to the curriculum you teach or to the students you teach, and books, supplies, equipment (including computer equipment, software and services) and other materials used in the classroom, including personal protective equipment, disinfectant and other supplies used to prevent the spread of coronavirus; not expenses for home schooling or nonathletic supplies for courses in health or physical education), reduced by excludable savings bond interest (Form 8815), nontaxable qualified tuition program or Coverdell earnings or distributions, and reimbursements not reported in box 1 of your Form W-2; zero if none

Shown for your spouse:

> About your spouse — Qualified educator expenses your spouse paid in 2025 (professional development courses your spouse took that are related to the curriculum your spouse teaches or to the students your spouse teaches, and books, supplies, equipment (including computer equipment, software and services) and other materials used in the classroom, including personal protective equipment, disinfectant and other supplies used to prevent the spread of coronavirus; not expenses for home schooling or nonathletic supplies for courses in health or physical education), reduced by excludable savings bond interest (Form 8815), nontaxable qualified tuition program or Coverdell earnings or distributions, and reimbursements not reported in box 1 of your spouse's Form W-2; zero if none

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `person.eligible_educator`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?

Shown on a one-person return:

> Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?

Shown for you on a couple's return:

> About you — Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?

Shown for your spouse:

> About your spouse — Was your spouse an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `$f8889`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you have a health savings account (HSA) in 2025, or get money from one?

Shown on a one-person return:

> Did you have a health savings account (HSA) in 2025, or get money from one?

Shown for you on a couple's return:

> About you — Did you have a health savings account (HSA) in 2025, or get money from one?

Shown for your spouse:

> About your spouse — Did your spouse have a health savings account (HSA) in 2025, or get money from one?

**Help, as stored**

> Signs that you had one: box 12 of your Form W-2 shows the letter W, or the bank that holds the account sent you a Form 5498-SA (money put in) or a Form 1099-SA (money paid out). Answer Yes even if nothing went in or came out in 2025, and if an HSA, or money from one, came from someone who died. A flexible spending account (FSA) is not an HSA.

Shown on a one-person return:

> Signs that you had one: box 12 of your Form W-2 shows the letter W, or the bank that holds the account sent you a Form 5498-SA (money put in) or a Form 1099-SA (money paid out). Answer Yes even if nothing went in or came out in 2025, and if an HSA, or money from one, came from someone who died. A flexible spending account (FSA) is not an HSA.

Shown for you on a couple's return:

> Signs that you had one: box 12 of your Form W-2 shows the letter W, or the bank that holds the account sent you a Form 5498-SA (money put in) or a Form 1099-SA (money paid out). Answer Yes even if nothing went in or came out in 2025, and if an HSA, or money from one, came from someone who died. A flexible spending account (FSA) is not an HSA.

Shown for your spouse:

> Signs that your spouse had one: box 12 of your spouse's Form W-2 shows the letter W, or the bank that holds the account sent your spouse a Form 5498-SA (money put in) or a Form 1099-SA (money paid out). Answer Yes even if nothing went in or came out in 2025, and if an HSA, or money from one, came from someone who died. A flexible spending account (FSA) is not an HSA.

## `f8889.owner_died`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did the owner of this HSA die in 2025?

Shown on a one-person return:

> Did the owner of this HSA die in 2025?

Shown for you on a couple's return:

> About you — Did the owner of this HSA die in 2025?

Shown for your spouse:

> About your spouse — Did the owner of this HSA die in 2025?

**Help, as stored**

> The owner is the person these questions are about. Answer Yes on that person's final return, and for that person on a joint return filed with the surviving husband or wife.

Shown on a one-person return:

> The owner is the person these questions are about. Answer Yes on that person's final return, and for that person on a joint return filed with the surviving husband or wife.

Shown for you on a couple's return:

> The owner is the person these questions are about. Answer Yes on that person's final return, and for that person on a joint return filed with the surviving husband or wife.

Shown for your spouse:

> The owner is the person these questions are about. Answer Yes on that person's final return, and for that person on a joint return filed with the surviving husband or wife.

## `f8889.inherited`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you get an HSA, or money from one, because its owner died?

Shown on a one-person return:

> Did you get an HSA, or money from one, because its owner died?

Shown for you on a couple's return:

> About you — Did you get an HSA, or money from one, because its owner died?

Shown for your spouse:

> About your spouse — Did your spouse get an HSA, or money from one, because its owner died?

**Help, as stored**

> For example, a parent, or a husband or wife who has died, named you as the beneficiary of their HSA. Answer Yes whatever year the owner died in.

Shown on a one-person return:

> For example, a parent, or a husband or wife who has died, named you as the beneficiary of their HSA. Answer Yes whatever year the owner died in.

Shown for you on a couple's return:

> For example, a parent, or a husband or wife who has died, named you as the beneficiary of their HSA. Answer Yes whatever year the owner died in.

Shown for your spouse:

> For example, a parent, or a husband or wife who has died, named your spouse as the beneficiary of their HSA. Answer Yes whatever year the owner died in.

## `f8889.archer`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you or your spouse have an Archer MSA in 2025?

Shown on a one-person return:

> Did you or your spouse have an Archer MSA in 2025?

Shown for you on a couple's return:

> About you — Did you or your spouse have an Archer MSA in 2025?

Shown for your spouse:

> About your spouse — Did your spouse or you have an Archer MSA in 2025?

**Help, as stored**

> An Archer MSA is an older kind of medical savings account; on a Form 1099-SA (box 5) or Form 5498-SA (box 6) for one, the box “Archer MSA” is checked. Answer Yes also if money was put into one for 2025 after the year ended. If you have never heard of it, the answer is No.

Shown on a one-person return:

> An Archer MSA is an older kind of medical savings account; on a Form 1099-SA (box 5) or Form 5498-SA (box 6) for one, the box “Archer MSA” is checked. Answer Yes also if money was put into one for 2025 after the year ended. If you have never heard of it, the answer is No.

Shown for you on a couple's return:

> An Archer MSA is an older kind of medical savings account; on a Form 1099-SA (box 5) or Form 5498-SA (box 6) for one, the box “Archer MSA” is checked. Answer Yes also if money was put into one for 2025 after the year ended. If you have never heard of it, the answer is No.

Shown for your spouse:

> An Archer MSA is an older kind of medical savings account; on a Form 1099-SA (box 5) or Form 5498-SA (box 6) for one, the box “Archer MSA” is checked. Answer Yes also if money was put into one for 2025 after the year ended. If your spouse has never heard of it, the answer is No.

## `f8889.line9`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much did your employer put into your HSA for 2025, including money taken out of your pay?

Shown on a one-person return:

> How much did your employer put into your HSA for 2025, including money taken out of your pay?

Shown for you on a couple's return:

> About you — How much did your employer put into your HSA for 2025, including money taken out of your pay?

Shown for your spouse:

> About your spouse — How much did your spouse's employer put into your spouse's HSA for 2025, including money taken out of your spouse's pay?

**Help, as stored**

> Use the amount in box 12 of your Form W-2 next to the letter W. Take off any part of it that was for 2024, and add anything your employer put in for 2025 after December 31, 2025. Zero if none.

Shown on a one-person return:

> Use the amount in box 12 of your Form W-2 next to the letter W. Take off any part of it that was for 2024, and add anything your employer put in for 2025 after December 31, 2025. Zero if none.

Shown for you on a couple's return:

> Use the amount in box 12 of your Form W-2 next to the letter W. Take off any part of it that was for 2024, and add anything your employer put in for 2025 after December 31, 2025. Zero if none.

Shown for your spouse:

> Use the amount in box 12 of your spouse's Form W-2 next to the letter W. Take off any part of it that was for 2024, and add anything your spouse's employer put in for 2025 after December 31, 2025. Zero if none.

## `f8889.line2`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much did you put into your HSA for 2025 yourself, not counting money in box 12 of your Form W-2?

Shown on a one-person return:

> How much did you put into your HSA for 2025 yourself, not counting money in box 12 of your Form W-2?

Shown for you on a couple's return:

> About you — How much did you put into your HSA for 2025 yourself, not counting money in box 12 of your Form W-2?

Shown for your spouse:

> About your spouse — How much did your spouse put into your spouse's HSA for 2025 himself or herself, not counting money in box 12 of your spouse's Form W-2?

**Help, as stored**

> Count deposits by you, or by anyone other than your employer, that were for 2025, made up to April 15, 2026 (later if you served in a combat zone). Box 12 of your Form W-2 shows, next to the letter W, what your employer put in and what was taken out of your pay before tax; leave that out, and leave out pre-tax money taken from your pay in early 2026 for 2025 (it belongs in the question before). Money taken out of your pay after tax counts here. Do not count money moved in from another HSA, an Archer MSA or an IRA. Zero if none.

Shown on a one-person return:

> Count deposits by you, or by anyone other than your employer, that were for 2025, made up to April 15, 2026 (later if you served in a combat zone). Box 12 of your Form W-2 shows, next to the letter W, what your employer put in and what was taken out of your pay before tax; leave that out, and leave out pre-tax money taken from your pay in early 2026 for 2025 (it belongs in the question before). Money taken out of your pay after tax counts here. Do not count money moved in from another HSA, an Archer MSA or an IRA. Zero if none.

Shown for you on a couple's return:

> Count deposits by you, or by anyone other than your employer, that were for 2025, made up to April 15, 2026 (later if you served in a combat zone). Box 12 of your Form W-2 shows, next to the letter W, what your employer put in and what was taken out of your pay before tax; leave that out, and leave out pre-tax money taken from your pay in early 2026 for 2025 (it belongs in the question before). Money taken out of your pay after tax counts here. Do not count money moved in from another HSA, an Archer MSA or an IRA. Zero if none.

Shown for your spouse:

> Count deposits by your spouse, or by anyone other than your spouse's employer, that were for 2025, made up to April 15, 2026 (later if your spouse served in a combat zone). Box 12 of your spouse's Form W-2 shows, next to the letter W, what your spouse's employer put in and what was taken out of your spouse's pay before tax; leave that out, and leave out pre-tax money taken from your spouse's pay in early 2026 for 2025 (it belongs in the question before). Money taken out of your spouse's pay after tax counts here. Do not count money moved in from another HSA, an Archer MSA or an IRA. Zero if none.

## `f8889.ira_transfer`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Was any money moved into your HSA straight from an IRA in 2025?

Shown on a one-person return:

> Was any money moved into your HSA straight from an IRA in 2025?

Shown for you on a couple's return:

> About you — Was any money moved into your HSA straight from an IRA in 2025?

Shown for your spouse:

> About your spouse — Was any money moved into your spouse's HSA straight from an IRA in 2025?

**Help, as stored**

> The IRA's custodian sends the money directly to the HSA. Money you took out of an IRA and deposited yourself does not count.

Shown on a one-person return:

> The IRA's custodian sends the money directly to the HSA. Money you took out of an IRA and deposited yourself does not count.

Shown for you on a couple's return:

> The IRA's custodian sends the money directly to the HSA. Money you took out of an IRA and deposited yourself does not count.

Shown for your spouse:

> The IRA's custodian sends the money directly to the HSA. Money your spouse took out of an IRA and deposited himself or herself does not count.

## `f8889.excess_withdrawn`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — In 2025, or in 2026 before filing this return, did you take money back out of your HSA because too much had been put in?

Shown on a one-person return:

> In 2025, or in 2026 before filing this return, did you take money back out of your HSA because too much had been put in?

Shown for you on a couple's return:

> About you — In 2025, or in 2026 before filing this return, did you take money back out of your HSA because too much had been put in?

Shown for your spouse:

> About your spouse — In 2025, or in 2026 before filing this return, did your spouse take money back out of your spouse's HSA because too much had been put in?

**Help, as stored**

> This is called withdrawing excess contributions. It covers money put in by you, your employer or anyone else. Answer Yes also if you plan to do it before the filing deadline, extensions included.

Shown on a one-person return:

> This is called withdrawing excess contributions. It covers money put in by you, your employer or anyone else. Answer Yes also if you plan to do it before the filing deadline, extensions included.

Shown for you on a couple's return:

> This is called withdrawing excess contributions. It covers money put in by you, your employer or anyone else. Answer Yes also if you plan to do it before the filing deadline, extensions included.

Shown for your spouse:

> This is called withdrawing excess contributions. It covers money put in by your spouse, your spouse's employer or anyone else. Answer Yes also if your spouse plans to do it before the filing deadline, extensions included.

## `f8889.coverage_year`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Was your health plan in 2025 a high-deductible plan that works with an HSA, and the same kind all year?

Shown on a one-person return:

> Was your health plan in 2025 a high-deductible plan that works with an HSA, and the same kind all year?

Shown for you on a couple's return:

> About you — Was your health plan in 2025 a high-deductible plan that works with an HSA, and the same kind all year?

Shown for your spouse:

> About your spouse — Was your spouse's health plan in 2025 a high-deductible plan that works with an HSA, and the same kind all year?

**Help, as stored**

> What counts is the plan you had on the first day of each month; plan papers usually call such a plan “HSA-eligible” or “HDHP”. If you were covered all year as a member of someone else's plan (a parent's, or your spouse's), or by a plan for only you and a family plan at once, choose “covering more than one person”; if that was so for only part of the year, choose “No”. A change of insurer with no gap and the same kind of plan is not a change.

Shown on a one-person return:

> What counts is the plan you had on the first day of each month; plan papers usually call such a plan “HSA-eligible” or “HDHP”. If you were covered all year as a member of someone else's plan (a parent's, or your spouse's), or by a plan for only you and a family plan at once, choose “covering more than one person”; if that was so for only part of the year, choose “No”. A change of insurer with no gap and the same kind of plan is not a change.

Shown for you on a couple's return:

> What counts is the plan you had on the first day of each month; plan papers usually call such a plan “HSA-eligible” or “HDHP”. If you were covered all year as a member of someone else's plan (a parent's, or your spouse's), or by a plan for only you and a family plan at once, choose “covering more than one person”; if that was so for only part of the year, choose “No”. A change of insurer with no gap and the same kind of plan is not a change.

Shown for your spouse:

> What counts is the plan your spouse had on the first day of each month; plan papers usually call such a plan “HSA-eligible” or “HDHP”. If your spouse was covered all year as a member of someone else's plan (a parent's, or yours), or by a plan for only your spouse and a family plan at once, choose “covering more than one person”; if that was so for only part of the year, choose “No”. A change of insurer with no gap and the same kind of plan is not a change.

## `f8889.clear_all_year`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — On the first day of every month of 2025, were all three of these true?
>
> - you were not enrolled in Medicare
> - you had no other health coverage that pays medical bills (dental, vision, accident, disability and long-term care insurance do not count)
> - nobody could claim you as a dependent

Shown on a one-person return:

> On the first day of every month of 2025, were all three of these true?
>
> - you were not enrolled in Medicare
> - you had no other health coverage that pays medical bills (dental, vision, accident, disability and long-term care insurance do not count)
> - nobody could claim you as a dependent

Shown for you on a couple's return:

> About you — On the first day of every month of 2025, were all three of these true?
>
> - you were not enrolled in Medicare
> - you had no other health coverage that pays medical bills (dental, vision, accident, disability and long-term care insurance do not count)
> - nobody could claim you as a dependent

Shown for your spouse:

> About your spouse — On the first day of every month of 2025, were all three of these true?
>
> - your spouse was not enrolled in Medicare
> - your spouse had no other health coverage that pays medical bills (dental, vision, accident, disability and long-term care insurance do not count)
> - nobody could claim your spouse as a dependent

**Help, as stored**

> Other health coverage means a second plan that pays medical bills before the high deductible is met, such as your spouse's ordinary plan that also covers you. These do not count either: telehealth, workers' compensation, liability cover under a car or home policy, insurance for one named illness or a fixed amount per day in hospital, and VA care for a service-connected disability. Medicare counts from the month its coverage began, even if that was set back. If you are not sure, answer No.

Shown on a one-person return:

> Other health coverage means a second plan that pays medical bills before the high deductible is met, such as your spouse's ordinary plan that also covers you. These do not count either: telehealth, workers' compensation, liability cover under a car or home policy, insurance for one named illness or a fixed amount per day in hospital, and VA care for a service-connected disability. Medicare counts from the month its coverage began, even if that was set back. If you are not sure, answer No.

Shown for you on a couple's return:

> Other health coverage means a second plan that pays medical bills before the high deductible is met, such as your spouse's ordinary plan that also covers you. These do not count either: telehealth, workers' compensation, liability cover under a car or home policy, insurance for one named illness or a fixed amount per day in hospital, and VA care for a service-connected disability. Medicare counts from the month its coverage began, even if that was set back. If you are not sure, answer No.

Shown for your spouse:

> Other health coverage means a second plan that pays medical bills before the high deductible is met, such as your ordinary plan that also covers your spouse. These do not count either: telehealth, workers' compensation, liability cover under a car or home policy, insurance for one named illness or a fixed amount per day in hospital, and VA care for a service-connected disability. Medicare counts from the month its coverage began, even if that was set back. If your spouse is not sure, answer No.

## `f8889.fsa`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you or your spouse have a health FSA or HRA at work in 2025 that pays ordinary medical bills?

Shown on a one-person return:

> Did you or your spouse have a health FSA or HRA at work in 2025 that pays ordinary medical bills?

Shown for you on a couple's return:

> About you — Did you or your spouse have a health FSA or HRA at work in 2025 that pays ordinary medical bills?

Shown for your spouse:

> About your spouse — Did your spouse or you have a health FSA or HRA at work in 2025 that pays ordinary medical bills?

**Help, as stored**

> It counts as other health coverage for you and your spouse alike, even when only one person signed up for it. Answer No if it pays only dental and vision costs, or pays nothing until the minimum annual deductible for an HSA plan is met ($1,650 for a plan covering one person, $3,300 for more). Answer Yes if it was suspended for only part of 2025, or if it pays only after retirement and the person who has it had retired. A 2024 health FSA's extra months in early 2025 count only if money was left in it at the end of 2024. A dependent care FSA is not a health FSA.

Shown on a one-person return:

> It counts as other health coverage for you and your spouse alike, even when only one person signed up for it. Answer No if it pays only dental and vision costs, or pays nothing until the minimum annual deductible for an HSA plan is met ($1,650 for a plan covering one person, $3,300 for more). Answer Yes if it was suspended for only part of 2025, or if it pays only after retirement and the person who has it had retired. A 2024 health FSA's extra months in early 2025 count only if money was left in it at the end of 2024. A dependent care FSA is not a health FSA.

Shown for you on a couple's return:

> It counts as other health coverage for you and your spouse alike, even when only one person signed up for it. Answer No if it pays only dental and vision costs, or pays nothing until the minimum annual deductible for an HSA plan is met ($1,650 for a plan covering one person, $3,300 for more). Answer Yes if it was suspended for only part of 2025, or if it pays only after retirement and the person who has it had retired. A 2024 health FSA's extra months in early 2025 count only if money was left in it at the end of 2024. A dependent care FSA is not a health FSA.

Shown for your spouse:

> It counts as other health coverage for you and your spouse alike, even when only one person signed up for it. Answer No if it pays only dental and vision costs, or pays nothing until the minimum annual deductible for an HSA plan is met ($1,650 for a plan covering one person, $3,300 for more). Answer Yes if it was suspended for only part of 2025, or if it pays only after retirement and the person who has it had retired. A 2024 health FSA's extra months in early 2025 count only if money was left in it at the end of 2024. A dependent care FSA is not a health FSA.

## `f8889.spouse_family`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — In any month of 2025, did your spouse have a high-deductible plan covering more than one person?

Shown on a one-person return:

> In any month of 2025, did your spouse have a high-deductible plan covering more than one person?

Shown for you on a couple's return:

> About you — In any month of 2025, did your spouse have a high-deductible plan covering more than one person?

Shown for your spouse:

> About your spouse — In any month of 2025, did you have a high-deductible plan covering more than one person?

**Help, as stored**

> A plan covering more than one person includes one for an employee and a child. Answer Yes even if your spouse has no HSA and even if the plan did not cover you. In a month when both of you qualified to have an HSA, both of you are treated as having family coverage, and the limit is the family one, shared between you both.

Shown on a one-person return:

> A plan covering more than one person includes one for an employee and a child. Answer Yes even if your spouse has no HSA and even if the plan did not cover you. In a month when both of you qualified to have an HSA, both of you are treated as having family coverage, and the limit is the family one, shared between you both.

Shown for you on a couple's return:

> A plan covering more than one person includes one for an employee and a child. Answer Yes even if your spouse has no HSA and even if the plan did not cover you. In a month when both of you qualified to have an HSA, both of you are treated as having family coverage, and the limit is the family one, shared between you both.

Shown for your spouse:

> A plan covering more than one person includes one for an employee and a child. Answer Yes even if you have no HSA and even if the plan did not cover your spouse. In a month when both of you qualified to have an HSA, both of you are treated as having family coverage, and the limit is the family one, shared between you both.

## `f8889.months_eligible`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — On the first day of how many months of 2025 were you covered by an HSA-qualifying plan, with all three of these true?
>
> - you were not enrolled in Medicare
> - you had no other health coverage that pays medical bills, counting a health FSA or HRA at work that pays ordinary medical bills, yours or your spouse's (dental, vision, accident, disability and long-term care insurance do not count)
> - nobody could claim you as a dependent

Shown on a one-person return:

> On the first day of how many months of 2025 were you covered by an HSA-qualifying plan, with all three of these true?
>
> - you were not enrolled in Medicare
> - you had no other health coverage that pays medical bills, counting a health FSA or HRA at work that pays ordinary medical bills, yours or your spouse's (dental, vision, accident, disability and long-term care insurance do not count)
> - nobody could claim you as a dependent

Shown for you on a couple's return:

> About you — On the first day of how many months of 2025 were you covered by an HSA-qualifying plan, with all three of these true?
>
> - you were not enrolled in Medicare
> - you had no other health coverage that pays medical bills, counting a health FSA or HRA at work that pays ordinary medical bills, yours or your spouse's (dental, vision, accident, disability and long-term care insurance do not count)
> - nobody could claim you as a dependent

Shown for your spouse:

> About your spouse — On the first day of how many months of 2025 was your spouse covered by an HSA-qualifying plan, with all three of these true?
>
> - your spouse was not enrolled in Medicare
> - your spouse had no other health coverage that pays medical bills, counting a health FSA or HRA at work that pays ordinary medical bills, yours or your spouse's (dental, vision, accident, disability and long-term care insurance do not count)
> - nobody could claim your spouse as a dependent

**Help, as stored**

> Count a month only if everything held on its first day; December counts as one of the months. An FSA or HRA that pays only dental and vision costs, or nothing until the minimum annual deductible for an HSA plan is met ($1,650 for a plan covering one person, $3,300 for more), does not count against a month; nor do telehealth, workers' compensation, insurance for one named illness or a fixed amount per day in hospital, or VA care for a service-connected disability. Zero if there was no such month.

Shown on a one-person return:

> Count a month only if everything held on its first day; December counts as one of the months. An FSA or HRA that pays only dental and vision costs, or nothing until the minimum annual deductible for an HSA plan is met ($1,650 for a plan covering one person, $3,300 for more), does not count against a month; nor do telehealth, workers' compensation, insurance for one named illness or a fixed amount per day in hospital, or VA care for a service-connected disability. Zero if there was no such month.

Shown for you on a couple's return:

> Count a month only if everything held on its first day; December counts as one of the months. An FSA or HRA that pays only dental and vision costs, or nothing until the minimum annual deductible for an HSA plan is met ($1,650 for a plan covering one person, $3,300 for more), does not count against a month; nor do telehealth, workers' compensation, insurance for one named illness or a fixed amount per day in hospital, or VA care for a service-connected disability. Zero if there was no such month.

Shown for your spouse:

> Count a month only if everything held on its first day; December counts as one of the months. An FSA or HRA that pays only dental and vision costs, or nothing until the minimum annual deductible for an HSA plan is met ($1,650 for a plan covering one person, $3,300 for more), does not count against a month; nor do telehealth, workers' compensation, insurance for one named illness or a fixed amount per day in hospital, or VA care for a service-connected disability. Zero if there was no such month.

## `f8889.months_family`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — On the first day of how many of those months did your plan cover more than one person, or did your spouse have a high-deductible plan covering more than one person?

Shown on a one-person return:

> On the first day of how many of those months did your plan cover more than one person, or did your spouse have a high-deductible plan covering more than one person?

Shown for you on a couple's return:

> About you — On the first day of how many of those months did your plan cover more than one person, or did your spouse have a high-deductible plan covering more than one person?

Shown for your spouse:

> About your spouse — On the first day of how many of those months did your spouse's plan cover more than one person, or did you have a high-deductible plan covering more than one person?

**Help, as stored**

> Count a month also if you were covered by someone else's family plan, or had a plan for only you and a family plan at once. Your spouse's plan counts for a month in which the three conditions held for your spouse as well, with or without an HSA, and whether or not the plan covered you. Zero if none.

Shown on a one-person return:

> Count a month also if you were covered by someone else's family plan, or had a plan for only you and a family plan at once. Your spouse's plan counts for a month in which the three conditions held for your spouse as well, with or without an HSA, and whether or not the plan covered you. Zero if none.

Shown for you on a couple's return:

> Count a month also if you were covered by someone else's family plan, or had a plan for only you and a family plan at once. Your spouse's plan counts for a month in which the three conditions held for your spouse as well, with or without an HSA, and whether or not the plan covered you. Zero if none.

Shown for your spouse:

> Count a month also if your spouse was covered by someone else's family plan, or had a plan for only your spouse and a family plan at once. Your plan counts for a month in which the three conditions held for you as well, with or without an HSA, and whether or not the plan covered your spouse. Zero if none.

## `f8889.dec_coverage`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — What did you have on December 1, 2025?

Shown on a one-person return:

> What did you have on December 1, 2025?

Shown for you on a couple's return:

> About you — What did you have on December 1, 2025?

Shown for your spouse:

> About your spouse — What did your spouse have on December 1, 2025?

**Help, as stored**

> Choose the first answer if on December 1 you were enrolled in Medicare, had other health coverage that pays medical bills, or could be claimed as a dependent. Choose the third if you were on someone else's HSA-qualifying family plan, if you had both kinds of plan at once, or if you were married, both of you qualified for an HSA that day, and either of you had a plan covering more than one person.

Shown on a one-person return:

> Choose the first answer if on December 1 you were enrolled in Medicare, had other health coverage that pays medical bills, or could be claimed as a dependent. Choose the third if you were on someone else's HSA-qualifying family plan, if you had both kinds of plan at once, or if you were married, both of you qualified for an HSA that day, and either of you had a plan covering more than one person.

Shown for you on a couple's return:

> Choose the first answer if on December 1 you were enrolled in Medicare, had other health coverage that pays medical bills, or could be claimed as a dependent. Choose the third if you were on someone else's HSA-qualifying family plan, if you had both kinds of plan at once, or if you were married, both of you qualified for an HSA that day, and either of you had a plan covering more than one person.

Shown for your spouse:

> Choose the first answer if on December 1 your spouse was enrolled in Medicare, had other health coverage that pays medical bills, or could be claimed as a dependent. Choose the third if your spouse was on someone else's HSA-qualifying family plan, if your spouse had both kinds of plan at once, or if your spouse was married, both of you qualified for an HSA that day, and either of you had a plan covering more than one person.

## `f8889.last_month`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Do you want to be treated as having had your December 1 coverage for all of 2025?

Shown on a one-person return:

> Do you want to be treated as having had your December 1 coverage for all of 2025?

Shown for you on a couple's return:

> About you — Do you want to be treated as having had your December 1 coverage for all of 2025?

Shown for your spouse:

> About your spouse — Does your spouse want to be treated as having had your spouse's December 1 coverage for all of 2025?

**Help, as stored**

> This is the “last-month rule”. It lets you put in the full yearly amount for the coverage you had on December 1 although you were not covered that way all year. The condition is that you stay covered by an HSA-qualifying plan through December 31, 2026; if you do not, the extra amount becomes income, with a 10% additional tax. If no more was put in, by anyone, than your covered months allow, answer No.

Shown on a one-person return:

> This is the “last-month rule”. It lets you put in the full yearly amount for the coverage you had on December 1 although you were not covered that way all year. The condition is that you stay covered by an HSA-qualifying plan through December 31, 2026; if you do not, the extra amount becomes income, with a 10% additional tax. If no more was put in, by anyone, than your covered months allow, answer No.

Shown for you on a couple's return:

> This is the “last-month rule”. It lets you put in the full yearly amount for the coverage you had on December 1 although you were not covered that way all year. The condition is that you stay covered by an HSA-qualifying plan through December 31, 2026; if you do not, the extra amount becomes income, with a 10% additional tax. If no more was put in, by anyone, than your covered months allow, answer No.

Shown for your spouse:

> This is the “last-month rule”. It lets your spouse put in the full yearly amount for the coverage your spouse had on December 1 although your spouse was not covered that way all year. The condition is that your spouse stays covered by an HSA-qualifying plan through December 31, 2026; if your spouse does not, the extra amount becomes income, with a 10% additional tax. If no more was put in, by anyone, than your spouse's covered months allow, answer No.

## `f8889.age55`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you 55 or older on December 31, 2025?

Shown on a one-person return:

> Were you 55 or older on December 31, 2025?

Shown for you on a couple's return:

> About you — Were you 55 or older on December 31, 2025?

Shown for your spouse:

> About your spouse — Was your spouse 55 or older on December 31, 2025?

## `f8889.allocation`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — You both have HSAs and share one family limit. How is it split between you both?

Shown on a one-person return:

> You both have HSAs and share one family limit. How is it split between you both?

Shown for you on a couple's return:

> About you — You both have HSAs and share one family limit. How is it split between you both?

Shown for your spouse:

> About your spouse — You both have HSAs and share one family limit. How is it split between you both?

**Help, as stored**

> Give the same answer for both of you. The shared limit is the family amount for the months both of you are treated as having family coverage (Step 1 of the Form 8889 line 6 instructions).

Shown on a one-person return:

> Give the same answer for both of you. The shared limit is the family amount for the months both of you are treated as having family coverage (Step 1 of the Form 8889 line 6 instructions).

Shown for you on a couple's return:

> Give the same answer for both of you. The shared limit is the family amount for the months both of you are treated as having family coverage (Step 1 of the Form 8889 line 6 instructions).

Shown for your spouse:

> Give the same answer for both of you. The shared limit is the family amount for the months both of you are treated as having family coverage (Step 1 of the Form 8889 line 6 instructions).

## `f8889.allocated`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much of the shared family limit is yours?

Shown on a one-person return:

> How much of the shared family limit is yours?

Shown for you on a couple's return:

> About you — How much of the shared family limit is yours?

Shown for your spouse:

> About your spouse — How much of the shared family limit is your spouse's?

**Help, as stored**

> The shared limit is the family amount for the months both of you are treated as having family coverage ($8,550 for a full year). Your spouse's part is the rest; the two parts together may not be more than it.

Shown on a one-person return:

> The shared limit is the family amount for the months both of you are treated as having family coverage ($8,550 for a full year). Your spouse's part is the rest; the two parts together may not be more than it.

Shown for you on a couple's return:

> The shared limit is the family amount for the months both of you are treated as having family coverage ($8,550 for a full year). Your spouse's part is the rest; the two parts together may not be more than it.

Shown for your spouse:

> The shared limit is the family amount for the months both of you are treated as having family coverage ($8,550 for a full year). Your part is the rest; the two parts together may not be more than it.

## `f8889.employer_in_box1`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Your employer put more into your HSA than your limit. Is the extra included in box 1 of your Form W-2?

Shown on a one-person return:

> Your employer put more into your HSA than your limit. Is the extra included in box 1 of your Form W-2?

Shown for you on a couple's return:

> About you — Your employer put more into your HSA than your limit. Is the extra included in box 1 of your Form W-2?

Shown for your spouse:

> About your spouse — Your spouse's employer put more into your spouse's HSA than your spouse's limit. Is the extra included in box 1 of your spouse's Form W-2?

**Help, as stored**

> Box 1 is your taxable wages. Answer No if your employer has not added the extra to it.

Shown on a one-person return:

> Box 1 is your taxable wages. Answer No if your employer has not added the extra to it.

Shown for you on a couple's return:

> Box 1 is your taxable wages. Answer No if your employer has not added the extra to it.

Shown for your spouse:

> Box 1 is your spouse's taxable wages. Answer No if your spouse's employer has not added the extra to it.

## `f8889.ira_prior`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Was any money moved into your HSA straight from an IRA during 2024?

Shown on a one-person return:

> Was any money moved into your HSA straight from an IRA during 2024?

Shown for you on a couple's return:

> About you — Was any money moved into your HSA straight from an IRA during 2024?

Shown for your spouse:

> About your spouse — Was any money moved into your spouse's HSA straight from an IRA during 2024?

**Help, as stored**

> The IRA's custodian sends the money directly to the HSA. It came with a condition, to stay able to have an HSA for the 12 months after the month of the transfer. Money you took out of an IRA and deposited yourself does not count.

Shown on a one-person return:

> The IRA's custodian sends the money directly to the HSA. It came with a condition, to stay able to have an HSA for the 12 months after the month of the transfer. Money you took out of an IRA and deposited yourself does not count.

Shown for you on a couple's return:

> The IRA's custodian sends the money directly to the HSA. It came with a condition, to stay able to have an HSA for the 12 months after the month of the transfer. Money you took out of an IRA and deposited yourself does not count.

Shown for your spouse:

> The IRA's custodian sends the money directly to the HSA. It came with a condition, to stay able to have an HSA for the 12 months after the month of the transfer. Money your spouse took out of an IRA and deposited himself or herself does not count.

## `f8889.testing_prior`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — For 2024, was more put into your HSA, by you, your employer or anyone else, than the months you could have an HSA, and the kind of plan you had in each, allowed?

Shown on a one-person return:

> For 2024, was more put into your HSA, by you, your employer or anyone else, than the months you could have an HSA, and the kind of plan you had in each, allowed?

Shown for you on a couple's return:

> About you — For 2024, was more put into your HSA, by you, your employer or anyone else, than the months you could have an HSA, and the kind of plan you had in each, allowed?

Shown for your spouse:

> About your spouse — For 2024, was more put into your spouse's HSA, by your spouse, your spouse's employer or anyone else, than the months your spouse could have an HSA, and the kind of plan your spouse had in each, allowed?

**Help, as stored**

> This is about the “last-month rule”. A person who could have an HSA on December 1, 2024 was allowed the full yearly amount for the plan held that day, on condition of staying able to have an HSA through December 31, 2025. Answer Yes if more went in for 2024 than your own months allowed, counting each month by the plan of that month. That can be so if your plan began during 2024; if for part of 2024 you were someone's dependent or had other health coverage, counting a health FSA or HRA at work (also the extra months of a 2023 health FSA early in 2024, and your spouse's FSA); or if your plan, or a plan your spouse had, went from covering one person to covering more. Line 3 of your 2024 Form 8889 then shows the full yearly amount ($4,150 for a plan covering one person, $8,300 for more, before the extra $1,000 from age 55) although not every month of 2024 earned it. If you are not sure, answer Yes.

Shown on a one-person return:

> This is about the “last-month rule”. A person who could have an HSA on December 1, 2024 was allowed the full yearly amount for the plan held that day, on condition of staying able to have an HSA through December 31, 2025. Answer Yes if more went in for 2024 than your own months allowed, counting each month by the plan of that month. That can be so if your plan began during 2024; if for part of 2024 you were someone's dependent or had other health coverage, counting a health FSA or HRA at work (also the extra months of a 2023 health FSA early in 2024, and your spouse's FSA); or if your plan, or a plan your spouse had, went from covering one person to covering more. Line 3 of your 2024 Form 8889 then shows the full yearly amount ($4,150 for a plan covering one person, $8,300 for more, before the extra $1,000 from age 55) although not every month of 2024 earned it. If you are not sure, answer Yes.

Shown for you on a couple's return:

> This is about the “last-month rule”. A person who could have an HSA on December 1, 2024 was allowed the full yearly amount for the plan held that day, on condition of staying able to have an HSA through December 31, 2025. Answer Yes if more went in for 2024 than your own months allowed, counting each month by the plan of that month. That can be so if your plan began during 2024; if for part of 2024 you were someone's dependent or had other health coverage, counting a health FSA or HRA at work (also the extra months of a 2023 health FSA early in 2024, and your spouse's FSA); or if your plan, or a plan your spouse had, went from covering one person to covering more. Line 3 of your 2024 Form 8889 then shows the full yearly amount ($4,150 for a plan covering one person, $8,300 for more, before the extra $1,000 from age 55) although not every month of 2024 earned it. If you are not sure, answer Yes.

Shown for your spouse:

> This is about the “last-month rule”. A person who could have an HSA on December 1, 2024 was allowed the full yearly amount for the plan held that day, on condition of staying able to have an HSA through December 31, 2025. Answer Yes if more went in for 2024 than your spouse's own months allowed, counting each month by the plan of that month. That can be so if your spouse's plan began during 2024; if for part of 2024 your spouse was someone's dependent or had other health coverage, counting a health FSA or HRA at work (also the extra months of a 2023 health FSA early in 2024, and your FSA); or if your spouse's plan, or a plan you had, went from covering one person to covering more. Line 3 of your spouse's 2024 Form 8889 then shows the full yearly amount ($4,150 for a plan covering one person, $8,300 for more, before the extra $1,000 from age 55) although not every month of 2024 earned it. If your spouse is not sure, answer Yes.

## `person.x_hsa_value`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Total value of your HSAs on December 31, 2025, including contributions for 2025 that you made in 2026 (asked only when you have excess HSA contributions)

Shown on a one-person return:

> Total value of your HSAs on December 31, 2025, including contributions for 2025 that you made in 2026 (asked only when you have excess HSA contributions)

Shown for you on a couple's return:

> About you — Total value of your HSAs on December 31, 2025, including contributions for 2025 that you made in 2026 (asked only when you have excess HSA contributions)

Shown for your spouse:

> About your spouse — Total value of your spouse's HSAs on December 31, 2025, including contributions for 2025 that your spouse made in 2026 (asked only when your spouse has excess HSA contributions)

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `f8889.line14a`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much came out of your HSA in 2025 in total?

Shown on a one-person return:

> How much came out of your HSA in 2025 in total?

Shown for you on a couple's return:

> About you — How much came out of your HSA in 2025 in total?

Shown for your spouse:

> About your spouse — How much came out of your spouse's HSA in 2025 in total?

**Help, as stored**

> Add box 1 of your 2025 Forms 1099-SA for HSAs (box 5 marks the kind of account). This includes payments made straight to a doctor or pharmacy with the HSA card. Do not count money the bank moved directly into another HSA of yours. If you have no form, use the account's statements. Zero if none.

Shown on a one-person return:

> Add box 1 of your 2025 Forms 1099-SA for HSAs (box 5 marks the kind of account). This includes payments made straight to a doctor or pharmacy with the HSA card. Do not count money the bank moved directly into another HSA of yours. If you have no form, use the account's statements. Zero if none.

Shown for you on a couple's return:

> Add box 1 of your 2025 Forms 1099-SA for HSAs (box 5 marks the kind of account). This includes payments made straight to a doctor or pharmacy with the HSA card. Do not count money the bank moved directly into another HSA of yours. If you have no form, use the account's statements. Zero if none.

Shown for your spouse:

> Add box 1 of your spouse's 2025 Forms 1099-SA for HSAs (box 5 marks the kind of account). This includes payments made straight to a doctor or pharmacy with the HSA card. Do not count money the bank moved directly into another HSA of your spouse's. If your spouse has no form, use the account's statements. Zero if none.

## `f8889.dist_code`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Does box 3 of any of your 2025 Forms 1099-SA for an HSA show a number other than 1 or 3?

Shown on a one-person return:

> Does box 3 of any of your 2025 Forms 1099-SA for an HSA show a number other than 1 or 3?

Shown for you on a couple's return:

> About you — Does box 3 of any of your 2025 Forms 1099-SA for an HSA show a number other than 1 or 3?

Shown for your spouse:

> About your spouse — Does box 3 of any of your spouse's 2025 Forms 1099-SA for an HSA show a number other than 1 or 3?

**Help, as stored**

> Box 3 is the “distribution code”. 1 is an ordinary payment and 3 a payment after disability. 2 means excess contributions taken back, 4 or 6 a payment after a death, and 5 a prohibited transaction.

Shown on a one-person return:

> Box 3 is the “distribution code”. 1 is an ordinary payment and 3 a payment after disability. 2 means excess contributions taken back, 4 or 6 a payment after a death, and 5 a prohibited transaction.

Shown for you on a couple's return:

> Box 3 is the “distribution code”. 1 is an ordinary payment and 3 a payment after disability. 2 means excess contributions taken back, 4 or 6 a payment after a death, and 5 a prohibited transaction.

Shown for your spouse:

> Box 3 is the “distribution code”. 1 is an ordinary payment and 3 a payment after disability. 2 means excess contributions taken back, 4 or 6 a payment after a death, and 5 a prohibited transaction.

## `f8889.rollover`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much of the money that came out did you put into another HSA of your own within 60 days?

Shown on a one-person return:

> How much of the money that came out did you put into another HSA of your own within 60 days?

Shown for you on a couple's return:

> About you — How much of the money that came out did you put into another HSA of your own within 60 days?

Shown for your spouse:

> About your spouse — How much of the money that came out did your spouse put into another HSA of your spouse's own within 60 days?

**Help, as stored**

> An HSA can take in only one such deposit in any 12 months; do not count a second one, or money the bank moved directly (that is not part of the total). Zero if none.

Shown on a one-person return:

> An HSA can take in only one such deposit in any 12 months; do not count a second one, or money the bank moved directly (that is not part of the total). Zero if none.

Shown for you on a couple's return:

> An HSA can take in only one such deposit in any 12 months; do not count a second one, or money the bank moved directly (that is not part of the total). Zero if none.

Shown for your spouse:

> An HSA can take in only one such deposit in any 12 months; do not count a second one, or money the bank moved directly (that is not part of the total). Zero if none.

## `f8889.mistake_repaid`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Was any money paid out of your HSA by mistake and later put back?

Shown on a one-person return:

> Was any money paid out of your HSA by mistake and later put back?

Shown for you on a couple's return:

> About you — Was any money paid out of your HSA by mistake and later put back?

Shown for your spouse:

> About your spouse — Was any money paid out of your spouse's HSA by mistake and later put back?

**Help, as stored**

> For example, the HSA paid a bill that turned out not to be a medical cost, and you returned the money to the HSA. Answer Yes also if you plan to return it.

Shown on a one-person return:

> For example, the HSA paid a bill that turned out not to be a medical cost, and you returned the money to the HSA. Answer Yes also if you plan to return it.

Shown for you on a couple's return:

> For example, the HSA paid a bill that turned out not to be a medical cost, and you returned the money to the HSA. Answer Yes also if you plan to return it.

Shown for your spouse:

> For example, the HSA paid a bill that turned out not to be a medical cost, and your spouse returned the money to the HSA. Answer Yes also if your spouse plans to return it.

## `f8889.medical_all`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did all of the money that came out pay for doctor, dental, vision, hospital or pharmacy costs of you, your spouse, or your dependents?

Shown on a one-person return:

> Did all of the money that came out pay for doctor, dental, vision, hospital or pharmacy costs of you, your spouse, or your dependents?

Shown for you on a couple's return:

> About you — Did all of the money that came out pay for doctor, dental, vision, hospital or pharmacy costs of you, your spouse, or your dependents?

Shown for your spouse:

> About your spouse — Did all of the money that came out pay for doctor, dental, vision, hospital or pharmacy costs of your spouse, you, or your spouse's dependents?

**Help, as stored**

> Answer No if any of it paid for insurance premiums, for someone else (such as an adult child you do not claim), for costs from before you opened the HSA, or for costs that insurance or anyone else paid back to you. Money you put into another HSA within 60 days does not count against a Yes. These costs cannot also be deducted on Schedule A.

Shown on a one-person return:

> Answer No if any of it paid for insurance premiums, for someone else (such as an adult child you do not claim), for costs from before you opened the HSA, or for costs that insurance or anyone else paid back to you. Money you put into another HSA within 60 days does not count against a Yes. These costs cannot also be deducted on Schedule A.

Shown for you on a couple's return:

> Answer No if any of it paid for insurance premiums, for someone else (such as an adult child you do not claim), for costs from before you opened the HSA, or for costs that insurance or anyone else paid back to you. Money you put into another HSA within 60 days does not count against a Yes. These costs cannot also be deducted on Schedule A.

Shown for your spouse:

> Answer No if any of it paid for insurance premiums, for someone else (such as an adult child your spouse does not claim), for costs from before your spouse opened the HSA, or for costs that insurance or anyone else paid back to your spouse. Money your spouse put into another HSA within 60 days does not count against a Yes. These costs cannot also be deducted on Schedule A.

## `f8889.medical`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much of the money that came out paid for medical costs that count?
>
> The costs must not have been paid back by insurance or anyone else, and must date from after you opened the HSA.
>
> Whose costs count:
> - yours, and your spouse's
> - your dependents'
> - those of a person you could claim as a dependent but for their income, their joint return, or your being someone else's dependent
> - those of your child if you are divorced, separated or lived apart from the other parent for the last six months of the year, whichever parent claims the child
>
> Insurance premiums count only for:
> - long-term care insurance
> - continuation coverage such as COBRA, for you, your spouse, or a dependent
> - health coverage while you, your spouse, or a dependent received unemployment compensation
> - Medicare and other health coverage if you were 65 or older, but not a Medicare supplement (Medigap) policy; if you are under 65, Medicare premiums for your spouse or a dependent do not count
>
> Zero if none.

Shown on a one-person return:

> How much of the money that came out paid for medical costs that count?
>
> The costs must not have been paid back by insurance or anyone else, and must date from after you opened the HSA.
>
> Whose costs count:
> - yours, and your spouse's
> - your dependents'
> - those of a person you could claim as a dependent but for their income, their joint return, or your being someone else's dependent
> - those of your child if you are divorced, separated or lived apart from the other parent for the last six months of the year, whichever parent claims the child
>
> Insurance premiums count only for:
> - long-term care insurance
> - continuation coverage such as COBRA, for you, your spouse, or a dependent
> - health coverage while you, your spouse, or a dependent received unemployment compensation
> - Medicare and other health coverage if you were 65 or older, but not a Medicare supplement (Medigap) policy; if you are under 65, Medicare premiums for your spouse or a dependent do not count
>
> Zero if none.

Shown for you on a couple's return:

> About you — How much of the money that came out paid for medical costs that count?
>
> The costs must not have been paid back by insurance or anyone else, and must date from after you opened the HSA.
>
> Whose costs count:
> - yours, and your spouse's
> - your dependents'
> - those of a person you could claim as a dependent but for their income, their joint return, or your being someone else's dependent
> - those of your child if you are divorced, separated or lived apart from the other parent for the last six months of the year, whichever parent claims the child
>
> Insurance premiums count only for:
> - long-term care insurance
> - continuation coverage such as COBRA, for you, your spouse, or a dependent
> - health coverage while you, your spouse, or a dependent received unemployment compensation
> - Medicare and other health coverage if you were 65 or older, but not a Medicare supplement (Medigap) policy; if you are under 65, Medicare premiums for your spouse or a dependent do not count
>
> Zero if none.

Shown for your spouse:

> About your spouse — How much of the money that came out paid for medical costs that count?
>
> The costs must not have been paid back by insurance or anyone else, and must date from after your spouse opened the HSA.
>
> Whose costs count:
> - your spouse's, and yours
> - your spouse's dependents'
> - those of a person your spouse could claim as a dependent but for their income, their joint return, or your spouse's being someone else's dependent
> - those of your spouse's child if your spouse is divorced, separated or lived apart from the other parent for the last six months of the year, whichever parent claims the child
>
> Insurance premiums count only for:
> - long-term care insurance
> - continuation coverage such as COBRA, for your spouse, you, or a dependent
> - health coverage while your spouse, you, or a dependent received unemployment compensation
> - Medicare and other health coverage if your spouse was 65 or older, but not a Medicare supplement (Medigap) policy; if your spouse is under 65, Medicare premiums for you or a dependent do not count
>
> Zero if none.

**Help, as stored**

> Nonprescription medicines and menstrual care products count. These costs cannot also be deducted on Schedule A.

Shown on a one-person return:

> Nonprescription medicines and menstrual care products count. These costs cannot also be deducted on Schedule A.

Shown for you on a couple's return:

> Nonprescription medicines and menstrual care products count. These costs cannot also be deducted on Schedule A.

Shown for your spouse:

> Nonprescription medicines and menstrual care products count. These costs cannot also be deducted on Schedule A.

## `f8889.loan`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — In 2025, did you use your HSA as security for a loan, borrow from it, lend to it, or buy from or sell to it yourself?

Shown on a one-person return:

> In 2025, did you use your HSA as security for a loan, borrow from it, lend to it, or buy from or sell to it yourself?

Shown for you on a couple's return:

> About you — In 2025, did you use your HSA as security for a loan, borrow from it, lend to it, or buy from or sell to it yourself?

Shown for your spouse:

> About your spouse — In 2025, did your spouse use your spouse's HSA as security for a loan, borrow from it, lend to it, or buy from or sell to it himself or herself?

**Help, as stored**

> It counts whether you did it yourself or through someone else. Renting property to or from the HSA, being paid by it for goods or services, and using or taking over something it owns count too. An HSA used only to save and to pay medical bills has none of these.

Shown on a one-person return:

> It counts whether you did it yourself or through someone else. Renting property to or from the HSA, being paid by it for goods or services, and using or taking over something it owns count too. An HSA used only to save and to pay medical bills has none of these.

Shown for you on a couple's return:

> It counts whether you did it yourself or through someone else. Renting property to or from the HSA, being paid by it for goods or services, and using or taking over something it owns count too. An HSA used only to save and to pay medical bills has none of these.

Shown for your spouse:

> It counts whether your spouse did it himself or herself or through someone else. Renting property to or from the HSA, being paid by it for goods or services, and using or taking over something it owns count too. An HSA used only to save and to pay medical bills has none of these.

## `f8889.line17a`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Was any of the money not spent on medical costs taken out after you turned 65 or became disabled?

Shown on a one-person return:

> Was any of the money not spent on medical costs taken out after you turned 65 or became disabled?

Shown for you on a couple's return:

> About you — Was any of the money not spent on medical costs taken out after you turned 65 or became disabled?

Shown for your spouse:

> About your spouse — Was any of the money not spent on medical costs taken out after your spouse turned 65 or became disabled?

**Help, as stored**

> Answer No if all of it was taken out before you turned 65 or became disabled. Money taken out earlier carries an additional 20% tax.

Shown on a one-person return:

> Answer No if all of it was taken out before you turned 65 or became disabled. Money taken out earlier carries an additional 20% tax.

Shown for you on a couple's return:

> Answer No if all of it was taken out before you turned 65 or became disabled. Money taken out earlier carries an additional 20% tax.

Shown for your spouse:

> Answer No if all of it was taken out before your spouse turned 65 or became disabled. Money taken out earlier carries an additional 20% tax.

## `f8889.subject_part`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much of the money not spent on medical costs came out before you turned 65 or became disabled?

Shown on a one-person return:

> How much of the money not spent on medical costs came out before you turned 65 or became disabled?

Shown for you on a couple's return:

> About you — How much of the money not spent on medical costs came out before you turned 65 or became disabled?

Shown for your spouse:

> About your spouse — How much of the money not spent on medical costs came out before your spouse turned 65 or became disabled?

**Help, as stored**

> This is the part that carries the additional 20% tax. Zero if all of it came out after.

Shown on a one-person return:

> This is the part that carries the additional 20% tax. Zero if all of it came out after.

Shown for you on a couple's return:

> This is the part that carries the additional 20% tax. Zero if all of it came out after.

Shown for your spouse:

> This is the part that carries the additional 20% tax. Zero if all of it came out after.

## `person.died_before_65`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Is this the final return of a person born between January 2, 1960, and January 1, 1961, who died in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)

Shown on a one-person return:

> Is this the final return of a person born between January 2, 1960, and January 1, 1961, who died in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)

Shown for you on a couple's return:

> About you — Is this the final return of a person born between January 2, 1960, and January 1, 1961, who died in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)

Shown for your spouse:

> About your spouse — Is this the final return of a person born between January 2, 1960, and January 1, 1961, who died in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `$tipjob`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — List the employers from which you received tips you are deducting, one entry per employer. Leave the list empty if none.

Shown on a one-person return:

> List the employers from which you received tips you are deducting, one entry per employer. Leave the list empty if none.

Shown for you on a couple's return:

> About you — List the employers from which you received tips you are deducting, one entry per employer. Leave the list empty if none.

Shown for your spouse:

> About your spouse — List the employers from which your spouse received tips your spouse is deducting, one entry per employer. Leave the list empty if none.

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `$otjob`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — List the employers that paid you overtime you are deducting, one entry per employer. Leave the list empty if none.

Shown on a one-person return:

> List the employers that paid you overtime you are deducting, one entry per employer. Leave the list empty if none.

Shown for you on a couple's return:

> About you — List the employers that paid you overtime you are deducting, one entry per employer. Leave the list empty if none.

Shown for your spouse:

> About your spouse — List the employers that paid your spouse overtime your spouse is deducting, one entry per employer. Leave the list empty if none.

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `$sc`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you operate a business or practice a profession as a sole proprietor in 2025 (income reported to you on Forms 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business)? List each such business, one entry per business; leave the list empty if none.

Shown on a one-person return:

> Did you operate a business or practice a profession as a sole proprietor in 2025 (income reported to you on Forms 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business)? List each such business, one entry per business; leave the list empty if none.

Shown for you on a couple's return:

> About you — Did you operate a business or practice a profession as a sole proprietor in 2025 (income reported to you on Forms 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business)? List each such business, one entry per business; leave the list empty if none.

Shown for your spouse:

> About your spouse — Did your spouse operate a business or practice a profession as a sole proprietor in 2025 (income reported to your spouse on Forms 1099-NEC, 1099-K or 1099-MISC for your spouse's own work is usually such a business)? List each such business, one entry per business; leave the list empty if none.

## `person.se_screen`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Does any of these apply to this person?
>
> - church employee income (wages from a church or qualified church-controlled organization that elected exemption from social security and Medicare taxes)
> - being a minister, a member of a religious order or a Christian Science practitioner, or having an approved Form 4361 or Form 4029
> - net earnings from self-employment from a partnership (Schedule K-1, box 14, code A) or other self-employment income not on a Schedule C (such as director's fees, fiduciary fees, or fees as a fee-basis state or local government employee)
> - farm income (Schedule F) or Conservation Reserve Program payments
> - electing an optional method (Schedule SE Part II)
> - a chapter 11 bankruptcy case
> - community income on a separate return
> - self-employment income exempt under an international social security agreement or earned as a U.S. citizen employed by a foreign government
> - tips reported on Form 4137 or wages on Form 8919

Shown on a one-person return:

> Does any of these apply to you?
>
> - church employee income (wages from a church or qualified church-controlled organization that elected exemption from social security and Medicare taxes)
> - being a minister, a member of a religious order or a Christian Science practitioner, or having an approved Form 4361 or Form 4029
> - net earnings from self-employment from a partnership (Schedule K-1, box 14, code A) or other self-employment income not on a Schedule C (such as director's fees, fiduciary fees, or fees as a fee-basis state or local government employee)
> - farm income (Schedule F) or Conservation Reserve Program payments
> - electing an optional method (Schedule SE Part II)
> - a chapter 11 bankruptcy case
> - community income on a separate return
> - self-employment income exempt under an international social security agreement or earned as a U.S. citizen employed by a foreign government
> - tips reported on Form 4137 or wages on Form 8919

Shown for you on a couple's return:

> About you — Does any of these apply to you?
>
> - church employee income (wages from a church or qualified church-controlled organization that elected exemption from social security and Medicare taxes)
> - being a minister, a member of a religious order or a Christian Science practitioner, or having an approved Form 4361 or Form 4029
> - net earnings from self-employment from a partnership (Schedule K-1, box 14, code A) or other self-employment income not on a Schedule C (such as director's fees, fiduciary fees, or fees as a fee-basis state or local government employee)
> - farm income (Schedule F) or Conservation Reserve Program payments
> - electing an optional method (Schedule SE Part II)
> - a chapter 11 bankruptcy case
> - community income on a separate return
> - self-employment income exempt under an international social security agreement or earned as a U.S. citizen employed by a foreign government
> - tips reported on Form 4137 or wages on Form 8919

Shown for your spouse:

> About your spouse — Does any of these apply to your spouse?
>
> - church employee income (wages from a church or qualified church-controlled organization that elected exemption from social security and Medicare taxes)
> - being a minister, a member of a religious order or a Christian Science practitioner, or having an approved Form 4361 or Form 4029
> - net earnings from self-employment from a partnership (Schedule K-1, box 14, code A) or other self-employment income not on a Schedule C (such as director's fees, fiduciary fees, or fees as a fee-basis state or local government employee)
> - farm income (Schedule F) or Conservation Reserve Program payments
> - electing an optional method (Schedule SE Part II)
> - a chapter 11 bankruptcy case
> - community income on a separate return
> - self-employment income exempt under an international social security agreement or earned as a U.S. citizen employed by a foreign government
> - tips reported on Form 4137 or wages on Form 8919

## `person.plan`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you (this person) contribute for yourself, as a self-employed person, to a SEP IRA (sep) or a SIMPLE IRA (simple) for 2025, or to neither (none)?

Shown on a one-person return:

> Did you contribute for yourself, as a self-employed person, to a SEP IRA (sep) or a SIMPLE IRA (simple) for 2025, or to neither (none)?

Shown for you on a couple's return:

> About you — Did you contribute for yourself, as a self-employed person, to a SEP IRA (sep) or a SIMPLE IRA (simple) for 2025, or to neither (none)?

Shown for your spouse:

> About your spouse — Did your spouse contribute for himself or herself, as a self-employed person, to a SEP IRA (sep) or a SIMPLE IRA (simple) for 2025, or to neither (none)?

**Help, as stored**

> One of the values of retire_plan.

Shown on a one-person return:

> One of the values of retire_plan.

Shown for you on a couple's return:

> One of the values of retire_plan.

Shown for your spouse:

> One of the values of retire_plan.

## `person.plan_screen`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Does any of these apply: a SARSEP; a SEP plan whose contribution rate is not a whole percentage or is more than 25%; a SIMPLE IRA plan of an employer that allows the higher contribution limits of section 117 of the SECURE 2.0 Act; contributions for yourself to more than one plan, or to a qualified plan (such as a solo 401(k)); salary reduction contributions or elective deferrals to any other plan in 2025 (such as a 401(k) or 403(b) through an employer); Roth SEP or Roth SIMPLE contributions; or contributions that are more than the maximum deductible amount?

Shown on a one-person return:

> Does any of these apply: a SARSEP; a SEP plan whose contribution rate is not a whole percentage or is more than 25%; a SIMPLE IRA plan of an employer that allows the higher contribution limits of section 117 of the SECURE 2.0 Act; contributions for yourself to more than one plan, or to a qualified plan (such as a solo 401(k)); salary reduction contributions or elective deferrals to any other plan in 2025 (such as a 401(k) or 403(b) through an employer); Roth SEP or Roth SIMPLE contributions; or contributions that are more than the maximum deductible amount?

Shown for you on a couple's return:

> About you — Does any of these apply: a SARSEP; a SEP plan whose contribution rate is not a whole percentage or is more than 25%; a SIMPLE IRA plan of an employer that allows the higher contribution limits of section 117 of the SECURE 2.0 Act; contributions for yourself to more than one plan, or to a qualified plan (such as a solo 401(k)); salary reduction contributions or elective deferrals to any other plan in 2025 (such as a 401(k) or 403(b) through an employer); Roth SEP or Roth SIMPLE contributions; or contributions that are more than the maximum deductible amount?

Shown for your spouse:

> About your spouse — Does any of these apply: a SARSEP; a SEP plan whose contribution rate is not a whole percentage or is more than 25%; a SIMPLE IRA plan of an employer that allows the higher contribution limits of section 117 of the SECURE 2.0 Act; contributions for himself or herself to more than one plan, or to a qualified plan (such as a solo 401(k)); salary reduction contributions or elective deferrals to any other plan in 2025 (such as a 401(k) or 403(b) through an employer); Roth SEP or Roth SIMPLE contributions; or contributions that are more than the maximum deductible amount?

## `person.sep_rate`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — The contribution rate stated in your SEP plan, as a whole percent (for example 10)

Shown on a one-person return:

> The contribution rate stated in your SEP plan, as a whole percent (for example 10)

Shown for you on a couple's return:

> About you — The contribution rate stated in your SEP plan, as a whole percent (for example 10)

Shown for your spouse:

> About your spouse — The contribution rate stated in your spouse's SEP plan, as a whole percent (for example 10)

## `person.sep_contrib`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — The contributions you made for yourself to your SEP IRA for 2025 (by the due date of the return, including extensions)

Shown on a one-person return:

> The contributions you made for yourself to your SEP IRA for 2025 (by the due date of the return, including extensions)

Shown for you on a couple's return:

> About you — The contributions you made for yourself to your SEP IRA for 2025 (by the due date of the return, including extensions)

Shown for your spouse:

> About your spouse — The contributions your spouse made for himself or herself to your spouse's SEP IRA for 2025 (by the due date of the return, including extensions)

## `person.simple_deferral`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — The salary reduction contributions you made for yourself to your SIMPLE IRA for 2025, including any catch-up contributions

Shown on a one-person return:

> The salary reduction contributions you made for yourself to your SIMPLE IRA for 2025, including any catch-up contributions

Shown for you on a couple's return:

> About you — The salary reduction contributions you made for yourself to your SIMPLE IRA for 2025, including any catch-up contributions

Shown for your spouse:

> About your spouse — The salary reduction contributions your spouse made for himself or herself to your spouse's SIMPLE IRA for 2025, including any catch-up contributions

## `person.simple_age`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Your age at the end of 2025 for SIMPLE catch-up contributions: under 50 (under50), 50 to 59 or 64 and over (age50), or 60, 61, 62 or 63 (age60_63)

Shown on a one-person return:

> Your age at the end of 2025 for SIMPLE catch-up contributions: under 50 (under50), 50 to 59 or 64 and over (age50), or 60, 61, 62 or 63 (age60_63)

Shown for you on a couple's return:

> About you — Your age at the end of 2025 for SIMPLE catch-up contributions: under 50 (under50), 50 to 59 or 64 and over (age50), or 60, 61, 62 or 63 (age60_63)

Shown for your spouse:

> About your spouse — Your spouse's age at the end of 2025 for SIMPLE catch-up contributions: under 50 (under50), 50 to 59 or 64 and over (age50), or 60, 61, 62 or 63 (age60_63)

**Help, as stored**

> One of the values of catchup_age.

Shown on a one-person return:

> One of the values of catchup_age.

Shown for you on a couple's return:

> One of the values of catchup_age.

Shown for your spouse:

> One of the values of catchup_age.

## `person.simple_kind`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — The employer contribution formula of your SIMPLE IRA plan for 2025: matching contributions (match) or 2% nonelective contributions (nonelective)

Shown on a one-person return:

> The employer contribution formula of your SIMPLE IRA plan for 2025: matching contributions (match) or 2% nonelective contributions (nonelective)

Shown for you on a couple's return:

> About you — The employer contribution formula of your SIMPLE IRA plan for 2025: matching contributions (match) or 2% nonelective contributions (nonelective)

Shown for your spouse:

> About your spouse — The employer contribution formula of your spouse's SIMPLE IRA plan for 2025: matching contributions (match) or 2% nonelective contributions (nonelective)

**Help, as stored**

> One of the values of simple_formula.

Shown on a one-person return:

> One of the values of simple_formula.

Shown for you on a couple's return:

> One of the values of simple_formula.

Shown for your spouse:

> One of the values of simple_formula.

## `person.simple_employer`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — The employer matching or nonelective contributions you made for yourself to your SIMPLE IRA for 2025 (by the due date of the return, including extensions)

Shown on a one-person return:

> The employer matching or nonelective contributions you made for yourself to your SIMPLE IRA for 2025 (by the due date of the return, including extensions)

Shown for you on a couple's return:

> About you — The employer matching or nonelective contributions you made for yourself to your SIMPLE IRA for 2025 (by the due date of the return, including extensions)

Shown for your spouse:

> About your spouse — The employer matching or nonelective contributions your spouse made for himself or herself to your spouse's SIMPLE IRA for 2025 (by the due date of the return, including extensions)

## `person.sav_born`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you born before January 2, 2008?

Shown on a one-person return:

> Were you born before January 2, 2008?

Shown for you on a couple's return:

> About you — Were you born before January 2, 2008?

Shown for your spouse:

> About your spouse — Was your spouse born before January 2, 2008?

**Help, as stored**

> The saver's credit (Form 8880) is not allowed for contributions made by a person born after January 1, 2008.

Shown on a one-person return:

> The saver's credit (Form 8880) is not allowed for contributions made by a person born after January 1, 2008.

Shown for you on a couple's return:

> The saver's credit (Form 8880) is not allowed for contributions made by a person born after January 1, 2008.

Shown for your spouse:

> The saver's credit (Form 8880) is not allowed for contributions made by a person born after January 1, 2008.

## `person.sav_student`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you a student in 2025: during any part of 5 calendar months of 2025, were you enrolled as a full-time student at a school, or did you take a full-time, on-farm training course given by a school or a state, county, or local government agency? (A school includes technical, trade, and mechanical schools. It does not include on-the-job training courses, correspondence schools, or schools offering courses only through the Internet.)

Shown on a one-person return:

> Were you a student in 2025: during any part of 5 calendar months of 2025, were you enrolled as a full-time student at a school, or did you take a full-time, on-farm training course given by a school or a state, county, or local government agency? (A school includes technical, trade, and mechanical schools. It does not include on-the-job training courses, correspondence schools, or schools offering courses only through the Internet.)

Shown for you on a couple's return:

> About you — Were you a student in 2025: during any part of 5 calendar months of 2025, were you enrolled as a full-time student at a school, or did you take a full-time, on-farm training course given by a school or a state, county, or local government agency? (A school includes technical, trade, and mechanical schools. It does not include on-the-job training courses, correspondence schools, or schools offering courses only through the Internet.)

Shown for your spouse:

> About your spouse — Was your spouse a student in 2025: during any part of 5 calendar months of 2025, was your spouse enrolled as a full-time student at a school, or did your spouse take a full-time, on-farm training course given by a school or a state, county, or local government agency? (A school includes technical, trade, and mechanical schools. It does not include on-the-job training courses, correspondence schools, or schools offering courses only through the Internet.)

**Help, as stored**

> A student for the saver's credit (Form 8880).

Shown on a one-person return:

> A student for the saver's credit (Form 8880).

Shown for you on a couple's return:

> A student for the saver's credit (Form 8880).

Shown for your spouse:

> A student for the saver's credit (Form 8880).

## `person.sav_claimed`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Are you claimed as a dependent on someone else's 2025 tax return?

Shown on a one-person return:

> Are you claimed as a dependent on someone else's 2025 tax return?

Shown for you on a couple's return:

> About you — Are you claimed as a dependent on someone else's 2025 tax return?

Shown for your spouse:

> About your spouse — Is your spouse claimed as a dependent on someone else's 2025 tax return?

**Help, as stored**

> Asked for the saver's credit when someone can claim you or your spouse as a dependent, for the education credits when qualified education expenses were paid, and for the student loan interest deduction when student loan interest was paid. Answer Yes only if this person is actually claimed on someone else's 2025 return.

Shown on a one-person return:

> Asked for the saver's credit when someone can claim you or your spouse as a dependent, for the education credits when qualified education expenses were paid, and for the student loan interest deduction when student loan interest was paid. Answer Yes only if you are actually claimed on someone else's 2025 return.

Shown for you on a couple's return:

> Asked for the saver's credit when someone can claim you or your spouse as a dependent, for the education credits when qualified education expenses were paid, and for the student loan interest deduction when student loan interest was paid. Answer Yes only if you are actually claimed on someone else's 2025 return.

Shown for your spouse:

> Asked for the saver's credit when someone can claim you or your spouse as a dependent, for the education credits when qualified education expenses were paid, and for the student loan interest deduction when student loan interest was paid. Answer Yes only if your spouse is actually claimed on someone else's 2025 return.

## `person.sav_trad`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you make contributions (other than rollover contributions) to a traditional IRA for 2025, deductible or not, including contributions made by the due date of your 2025 return for 2025? Do not count contributions made under a SEP or SIMPLE IRA plan, including those you made for yourself as a self-employed person.

Shown on a one-person return:

> Did you make contributions (other than rollover contributions) to a traditional IRA for 2025, deductible or not, including contributions made by the due date of your 2025 return for 2025? Do not count contributions made under a SEP or SIMPLE IRA plan, including those you made for yourself as a self-employed person.

Shown for you on a couple's return:

> About you — Did you make contributions (other than rollover contributions) to a traditional IRA for 2025, deductible or not, including contributions made by the due date of your 2025 return for 2025? Do not count contributions made under a SEP or SIMPLE IRA plan, including those you made for yourself as a self-employed person.

Shown for your spouse:

> About your spouse — Did your spouse make contributions (other than rollover contributions) to a traditional IRA for 2025, deductible or not, including contributions made by the due date of your spouse's 2025 return for 2025? Do not count contributions made under a SEP or SIMPLE IRA plan, including those your spouse made for himself or herself as a self-employed person.

**Help, as stored**

> Contributions to a traditional IRA for 2025, which may be made until April 15, 2026. They count for the IRA deduction (Schedule 1, line 20), Form 8606 and the saver's credit. Contributions under a SEP or SIMPLE IRA plan, whether your employer made them or you made them for yourself as a self-employed person, are not counted here; a self-employed person's contributions for themselves are asked with their SEP or SIMPLE plan and deducted on Schedule 1, line 16.

Shown on a one-person return:

> Contributions to a traditional IRA for 2025, which may be made until April 15, 2026. They count for the IRA deduction (Schedule 1, line 20), Form 8606 and the saver's credit. Contributions under a SEP or SIMPLE IRA plan, whether your employer made them or you made them for yourself as a self-employed person, are not counted here; a self-employed person's contributions for themselves are asked with their SEP or SIMPLE plan and deducted on Schedule 1, line 16.

Shown for you on a couple's return:

> Contributions to a traditional IRA for 2025, which may be made until April 15, 2026. They count for the IRA deduction (Schedule 1, line 20), Form 8606 and the saver's credit. Contributions under a SEP or SIMPLE IRA plan, whether your employer made them or you made them for yourself as a self-employed person, are not counted here; a self-employed person's contributions for themselves are asked with their SEP or SIMPLE plan and deducted on Schedule 1, line 16.

Shown for your spouse:

> Contributions to a traditional IRA for 2025, which may be made until April 15, 2026. They count for the IRA deduction (Schedule 1, line 20), Form 8606 and the saver's credit. Contributions under a SEP or SIMPLE IRA plan, whether your spouse's employer made them or your spouse made them for himself or herself as a self-employed person, are not counted here; a self-employed person's contributions for themselves are asked with their SEP or SIMPLE plan and deducted on Schedule 1, line 16.

## `person.ira_trad`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Your contributions to your traditional IRAs for 2025, made in 2025 or made by April 15, 2026, and designated for 2025; do not include rollover contributions, contributions made in 2025 that you deducted for 2024, contributions withdrawn (with their earnings) by the due date of your return, trustees' fees billed separately, or contributions made under a SEP or SIMPLE IRA plan, by your employer or by you for yourself as a self-employed person

Shown on a one-person return:

> Your contributions to your traditional IRAs for 2025, made in 2025 or made by April 15, 2026, and designated for 2025; do not include rollover contributions, contributions made in 2025 that you deducted for 2024, contributions withdrawn (with their earnings) by the due date of your return, trustees' fees billed separately, or contributions made under a SEP or SIMPLE IRA plan, by your employer or by you for yourself as a self-employed person

Shown for you on a couple's return:

> About you — Your contributions to your traditional IRAs for 2025, made in 2025 or made by April 15, 2026, and designated for 2025; do not include rollover contributions, contributions made in 2025 that you deducted for 2024, contributions withdrawn (with their earnings) by the due date of your return, trustees' fees billed separately, or contributions made under a SEP or SIMPLE IRA plan, by your employer or by you for yourself as a self-employed person

Shown for your spouse:

> About your spouse — Your spouse's contributions to your spouse's traditional IRAs for 2025, made in 2025 or made by April 15, 2026, and designated for 2025; do not include rollover contributions, contributions made in 2025 that your spouse deducted for 2024, contributions withdrawn (with their earnings) by the due date of your spouse's return, trustees' fees billed separately, or contributions made under a SEP or SIMPLE IRA plan, by your spouse's employer or by your spouse for himself or herself as a self-employed person

**Help, as stored**

> Form 5498 or a statement from the IRA trustee, sent by June 1, 2026, shows the contributions to your traditional IRA for 2025.

Shown on a one-person return:

> Form 5498 or a statement from the IRA trustee, sent by June 1, 2026, shows the contributions to your traditional IRA for 2025.

Shown for you on a couple's return:

> Form 5498 or a statement from the IRA trustee, sent by June 1, 2026, shows the contributions to your traditional IRA for 2025.

Shown for your spouse:

> Form 5498 or a statement from the IRA trustee, sent by June 1, 2026, shows the contributions to your spouse's traditional IRA for 2025.

## `person.ira_excess`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Does any of these apply to you?
>
> - your contributions for 2025 to traditional and Roth IRAs together were more than you were allowed to contribute (more than $7,000, or $8,000 if age 50 or older at the end of 2025, or more than your taxable compensation, or a Roth contribution above the limit for your income), and the excess was not withdrawn with its earnings by the due date of your return (including extensions)
> - you recharacterized a 2025 contribution (moved it from a traditional to a Roth IRA or the reverse)
> - an excess contribution from an earlier year remained in your traditional or Roth IRA at the end of 2025

Shown on a one-person return:

> Does any of these apply to you?
>
> - your contributions for 2025 to traditional and Roth IRAs together were more than you were allowed to contribute (more than $7,000, or $8,000 if age 50 or older at the end of 2025, or more than your taxable compensation, or a Roth contribution above the limit for your income), and the excess was not withdrawn with its earnings by the due date of your return (including extensions)
> - you recharacterized a 2025 contribution (moved it from a traditional to a Roth IRA or the reverse)
> - an excess contribution from an earlier year remained in your traditional or Roth IRA at the end of 2025

Shown for you on a couple's return:

> About you — Does any of these apply to you?
>
> - your contributions for 2025 to traditional and Roth IRAs together were more than you were allowed to contribute (more than $7,000, or $8,000 if age 50 or older at the end of 2025, or more than your taxable compensation, or a Roth contribution above the limit for your income), and the excess was not withdrawn with its earnings by the due date of your return (including extensions)
> - you recharacterized a 2025 contribution (moved it from a traditional to a Roth IRA or the reverse)
> - an excess contribution from an earlier year remained in your traditional or Roth IRA at the end of 2025

Shown for your spouse:

> About your spouse — Does any of these apply to your spouse?
>
> - your spouse's contributions for 2025 to traditional and Roth IRAs together were more than your spouse was allowed to contribute (more than $7,000, or $8,000 if age 50 or older at the end of 2025, or more than your spouse's taxable compensation, or a Roth contribution above the limit for your spouse's income), and the excess was not withdrawn with its earnings by the due date of your spouse's return (including extensions)
> - your spouse recharacterized a 2025 contribution (moved it from a traditional to a Roth IRA or the reverse)
> - an excess contribution from an earlier year remained in your spouse's traditional or Roth IRA at the end of 2025

**Help, as stored**

> An excess contribution, a recharacterization, or an earlier excess that remained in the IRA at the end of 2025 is reported on Form 5329 or with Pub. 590-A rules, which this tool does not prepare; Yes refuses the return.

Shown on a one-person return:

> An excess contribution, a recharacterization, or an earlier excess that remained in the IRA at the end of 2025 is reported on Form 5329 or with Pub. 590-A rules, which this tool does not prepare; Yes refuses the return.

Shown for you on a couple's return:

> An excess contribution, a recharacterization, or an earlier excess that remained in the IRA at the end of 2025 is reported on Form 5329 or with Pub. 590-A rules, which this tool does not prepare; Yes refuses the return.

Shown for your spouse:

> An excess contribution, a recharacterization, or an earlier excess that remained in the IRA at the end of 2025 is reported on Form 5329 or with Pub. 590-A rules, which this tool does not prepare; Yes refuses the return.

## `person.ira_age50`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you age 50 or older at the end of 2025?

Shown on a one-person return:

> Were you age 50 or older at the end of 2025?

Shown for you on a couple's return:

> About you — Were you age 50 or older at the end of 2025?

Shown for your spouse:

> About your spouse — Was your spouse age 50 or older at the end of 2025?

**Help, as stored**

> Age 50 or older at the end of 2025 raises the contribution limit to $8,000 and changes the IRA Deduction Worksheet's percentages.

Shown on a one-person return:

> Age 50 or older at the end of 2025 raises the contribution limit to $8,000 and changes the IRA Deduction Worksheet's percentages.

Shown for you on a couple's return:

> Age 50 or older at the end of 2025 raises the contribution limit to $8,000 and changes the IRA Deduction Worksheet's percentages.

Shown for your spouse:

> Age 50 or older at the end of 2025 raises the contribution limit to $8,000 and changes the IRA Deduction Worksheet's percentages.

## `person.ira_work_plan`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you covered by a retirement plan at work for 2025 (a qualified pension, profit-sharing or 401(k), annuity, SEP, SIMPLE or other employer plan), even if you were not vested in it?

Shown on a one-person return:

> Were you covered by a retirement plan at work for 2025 (a qualified pension, profit-sharing or 401(k), annuity, SEP, SIMPLE or other employer plan), even if you were not vested in it?

Shown for you on a couple's return:

> About you — Were you covered by a retirement plan at work for 2025 (a qualified pension, profit-sharing or 401(k), annuity, SEP, SIMPLE or other employer plan), even if you were not vested in it?

Shown for your spouse:

> About your spouse — Was your spouse covered by a retirement plan at work for 2025 (a qualified pension, profit-sharing or 401(k), annuity, SEP, SIMPLE or other employer plan), even if your spouse was not vested in it?

**Help, as stored**

> The "Retirement plan" box in box 13 of your Form W-2 should be checked if you were covered by a plan at work, even if you were not vested in it. If you are not sure, ask your employer. Coverage under social security or railroad retirement is not coverage by a plan. A SEP or SIMPLE IRA you contribute to as a self-employed person is taken from your Schedule C answers.

Shown on a one-person return:

> The "Retirement plan" box in box 13 of your Form W-2 should be checked if you were covered by a plan at work, even if you were not vested in it. If you are not sure, ask your employer. Coverage under social security or railroad retirement is not coverage by a plan. A SEP or SIMPLE IRA you contribute to as a self-employed person is taken from your Schedule C answers.

Shown for you on a couple's return:

> The "Retirement plan" box in box 13 of your Form W-2 should be checked if you were covered by a plan at work, even if you were not vested in it. If you are not sure, ask your employer. Coverage under social security or railroad retirement is not coverage by a plan. A SEP or SIMPLE IRA you contribute to as a self-employed person is taken from your Schedule C answers.

Shown for your spouse:

> The "Retirement plan" box in box 13 of your spouse's Form W-2 should be checked if your spouse was covered by a plan at work, even if your spouse was not vested in it. If your spouse is not sure, ask your spouse's employer. Coverage under social security or railroad retirement is not coverage by a plan. A SEP or SIMPLE IRA your spouse contributes to as a self-employed person is taken from your spouse's Schedule C answers.

## `person.ira_basis`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Your total basis in traditional IRAs (Form 8606 line 2): zero if this is the first year you file Form 8606; otherwise the amount the Total Basis Chart in the Form 8606 instructions gives for the last Form 8606 you filed (generally line 14 of that form)

Shown on a one-person return:

> Your total basis in traditional IRAs (Form 8606 line 2): zero if this is the first year you file Form 8606; otherwise the amount the Total Basis Chart in the Form 8606 instructions gives for the last Form 8606 you filed (generally line 14 of that form)

Shown for you on a couple's return:

> About you — Your total basis in traditional IRAs (Form 8606 line 2): zero if this is the first year you file Form 8606; otherwise the amount the Total Basis Chart in the Form 8606 instructions gives for the last Form 8606 you filed (generally line 14 of that form)

Shown for your spouse:

> About your spouse — Your spouse's total basis in traditional IRAs (Form 8606 line 2): zero if this is the first year your spouse files Form 8606; otherwise the amount the Total Basis Chart in the Form 8606 instructions gives for the last Form 8606 your spouse filed (generally line 14 of that form)

**Help, as stored**

> Your basis is the total of your nondeductible contributions to traditional IRAs, less any nontaxable distributions; zero if this is the first year you file Form 8606.

Shown on a one-person return:

> Your basis is the total of your nondeductible contributions to traditional IRAs, less any nontaxable distributions; zero if this is the first year you file Form 8606.

Shown for you on a couple's return:

> Your basis is the total of your nondeductible contributions to traditional IRAs, less any nontaxable distributions; zero if this is the first year you file Form 8606.

Shown for your spouse:

> Your spouse's basis is the total of your spouse's nondeductible contributions to traditional IRAs, less any nontaxable distributions; zero if this is the first year your spouse files Form 8606.

## `person.ira_basis_adjusted`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did your traditional IRA basis change other than by nondeductible contributions? That is: did the last Form 8606 you filed with Part I completed have a Line 15c Worksheet with an amount on line 6; did you have a return of excess traditional IRA contributions; did you transfer or receive a traditional IRA incident to divorce; or did you roll over a nontaxable part of a qualified retirement plan to a traditional IRA that wasn't previously reported on Form 8606, line 2?

Shown on a one-person return:

> Did your traditional IRA basis change other than by nondeductible contributions? That is: did the last Form 8606 you filed with Part I completed have a Line 15c Worksheet with an amount on line 6; did you have a return of excess traditional IRA contributions; did you transfer or receive a traditional IRA incident to divorce; or did you roll over a nontaxable part of a qualified retirement plan to a traditional IRA that wasn't previously reported on Form 8606, line 2?

Shown for you on a couple's return:

> About you — Did your traditional IRA basis change other than by nondeductible contributions? That is: did the last Form 8606 you filed with Part I completed have a Line 15c Worksheet with an amount on line 6; did you have a return of excess traditional IRA contributions; did you transfer or receive a traditional IRA incident to divorce; or did you roll over a nontaxable part of a qualified retirement plan to a traditional IRA that wasn't previously reported on Form 8606, line 2?

Shown for your spouse:

> About your spouse — Did your spouse's traditional IRA basis change other than by nondeductible contributions? That is: did the last Form 8606 your spouse filed with Part I completed have a Line 15c Worksheet with an amount on line 6; did your spouse have a return of excess traditional IRA contributions; did your spouse transfer or receive a traditional IRA incident to divorce; or did your spouse roll over a nontaxable part of a qualified retirement plan to a traditional IRA that wasn't previously reported on Form 8606, line 2?

**Help, as stored**

> Yes refuses the return (the Form 8606 line 2 adjustments are not prepared).

Shown on a one-person return:

> Yes refuses the return (the Form 8606 line 2 adjustments are not prepared).

Shown for you on a couple's return:

> Yes refuses the return (the Form 8606 line 2 adjustments are not prepared).

Shown for your spouse:

> Yes refuses the return (the Form 8606 line 2 adjustments are not prepared).

## `person.ira_dist`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — In 2025, did you take a distribution from a traditional IRA (including a SEP or SIMPLE IRA), or make a Roth IRA conversion? Do not count rollovers, qualified charitable distributions, a one-time distribution to fund an HSA, recharacterizations, or returns of contributions made by the due date of the return.

Shown on a one-person return:

> In 2025, did you take a distribution from a traditional IRA (including a SEP or SIMPLE IRA), or make a Roth IRA conversion? Do not count rollovers, qualified charitable distributions, a one-time distribution to fund an HSA, recharacterizations, or returns of contributions made by the due date of the return.

Shown for you on a couple's return:

> About you — In 2025, did you take a distribution from a traditional IRA (including a SEP or SIMPLE IRA), or make a Roth IRA conversion? Do not count rollovers, qualified charitable distributions, a one-time distribution to fund an HSA, recharacterizations, or returns of contributions made by the due date of the return.

Shown for your spouse:

> About your spouse — In 2025, did your spouse take a distribution from a traditional IRA (including a SEP or SIMPLE IRA), or make a Roth IRA conversion? Do not count rollovers, qualified charitable distributions, a one-time distribution to fund an HSA, recharacterizations, or returns of contributions made by the due date of the return.

**Help, as stored**

> Yes refuses the return (Form 8606 lines 4 to 13 are not prepared).

Shown on a one-person return:

> Yes refuses the return (Form 8606 lines 4 to 13 are not prepared).

Shown for you on a couple's return:

> Yes refuses the return (Form 8606 lines 4 to 13 are not prepared).

Shown for your spouse:

> Yes refuses the return (Form 8606 lines 4 to 13 are not prepared).

## `person.sav_able`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or did you receive any distribution from an ABLE account after 2022 and before the due date of your 2025 return (including extensions)?

Shown on a one-person return:

> As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or did you receive any distribution from an ABLE account after 2022 and before the due date of your 2025 return (including extensions)?

Shown for you on a couple's return:

> About you — As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or did you receive any distribution from an ABLE account after 2022 and before the due date of your 2025 return (including extensions)?

Shown for your spouse:

> About your spouse — As the designated beneficiary of an ABLE account, did your spouse contribute to it for 2025, or did your spouse receive any distribution from an ABLE account after 2022 and before the due date of your spouse's 2025 return (including extensions)?

**Help, as stored**

> ABLE accounts (Pub. 907) are outside this tool.

Shown on a one-person return:

> ABLE accounts (Pub. 907) are outside this tool.

Shown for you on a couple's return:

> ABLE accounts (Pub. 907) are outside this tool.

Shown for your spouse:

> ABLE accounts (Pub. 907) are outside this tool.

## `person.sav_roth`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Your contributions to a Roth IRA for 2025, including contributions made by the due date of your 2025 return that are for 2025; do not include rollover contributions or conversions; zero if none

Shown on a one-person return:

> Your contributions to a Roth IRA for 2025, including contributions made by the due date of your 2025 return that are for 2025; do not include rollover contributions or conversions; zero if none

Shown for you on a couple's return:

> About you — Your contributions to a Roth IRA for 2025, including contributions made by the due date of your 2025 return that are for 2025; do not include rollover contributions or conversions; zero if none

Shown for your spouse:

> About your spouse — Your spouse's contributions to a Roth IRA for 2025, including contributions made by the due date of your spouse's 2025 return that are for 2025; do not include rollover contributions or conversions; zero if none

**Help, as stored**

> Contributions for 2025 may be made up to the due date of your 2025 return. A contribution later recharacterized as a traditional IRA contribution is a traditional IRA contribution.

Shown on a one-person return:

> Contributions for 2025 may be made up to the due date of your 2025 return. A contribution later recharacterized as a traditional IRA contribution is a traditional IRA contribution.

Shown for you on a couple's return:

> Contributions for 2025 may be made up to the due date of your 2025 return. A contribution later recharacterized as a traditional IRA contribution is a traditional IRA contribution.

Shown for your spouse:

> Contributions for 2025 may be made up to the due date of your spouse's 2025 return. A contribution later recharacterized as a traditional IRA contribution is a traditional IRA contribution.

## `person.sav_excess`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Is the total of your elective deferrals and designated Roth contributions for 2025 (Form W-2 box 12, from all your employers) more than the limit that applies to you (for a 401(k) plan, $23,500 plus any catch-up contributions your plan allows), so that you have excess deferrals?

Shown on a one-person return:

> Is the total of your elective deferrals and designated Roth contributions for 2025 (Form W-2 box 12, from all your employers) more than the limit that applies to you (for a 401(k) plan, $23,500 plus any catch-up contributions your plan allows), so that you have excess deferrals?

Shown for you on a couple's return:

> About you — Is the total of your elective deferrals and designated Roth contributions for 2025 (Form W-2 box 12, from all your employers) more than the limit that applies to you (for a 401(k) plan, $23,500 plus any catch-up contributions your plan allows), so that you have excess deferrals?

Shown for your spouse:

> About your spouse — Is the total of your spouse's elective deferrals and designated Roth contributions for 2025 (Form W-2 box 12, from all your spouse's employers) more than the limit that applies to your spouse (for a 401(k) plan, $23,500 plus any catch-up contributions your spouse's plan allows), so that your spouse has excess deferrals?

**Help, as stored**

> Your plan administrator tells you if you deferred more than the limit.

Shown on a one-person return:

> Your plan administrator tells you if you deferred more than the limit.

Shown for you on a couple's return:

> Your plan administrator tells you if you deferred more than the limit.

Shown for your spouse:

> Your spouse's plan administrator tells your spouse if your spouse deferred more than the limit.

## `person.sav_voluntary`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Voluntary after-tax employee contributions you made for 2025 to a qualified retirement plan (including the federal Thrift Savings Plan), which may be shown in box 14 of your Form W-2; not designated Roth contributions, and not contributions designated under section 414(h)(2) (treated as employer contributions); zero if none

Shown on a one-person return:

> Voluntary after-tax employee contributions you made for 2025 to a qualified retirement plan (including the federal Thrift Savings Plan), which may be shown in box 14 of your Form W-2; not designated Roth contributions, and not contributions designated under section 414(h)(2) (treated as employer contributions); zero if none

Shown for you on a couple's return:

> About you — Voluntary after-tax employee contributions you made for 2025 to a qualified retirement plan (including the federal Thrift Savings Plan), which may be shown in box 14 of your Form W-2; not designated Roth contributions, and not contributions designated under section 414(h)(2) (treated as employer contributions); zero if none

Shown for your spouse:

> About your spouse — Voluntary after-tax employee contributions your spouse made for 2025 to a qualified retirement plan (including the federal Thrift Savings Plan), which may be shown in box 14 of your spouse's Form W-2; not designated Roth contributions, and not contributions designated under section 414(h)(2) (treated as employer contributions); zero if none

**Help, as stored**

> Required employee contributions and employer contributions are not voluntary contributions.

Shown on a one-person return:

> Required employee contributions and employer contributions are not voluntary contributions.

Shown for you on a couple's return:

> Required employee contributions and employer contributions are not voluntary contributions.

Shown for your spouse:

> Required employee contributions and employer contributions are not voluntary contributions.

## `person.sav_prior_joint`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — On a joint return: the distributions you received in 2023 and 2024 in a year for which you and your spouse filed a joint return, plus those you receive in 2026 before the due date of your 2025 return (including extensions), from any of the following; zero if none
>
> - a traditional or Roth IRA
> - a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP
> - another qualified retirement plan
>
> Do not include:
> - rollovers or trustee-to-trustee transfers
> - in-plan Roth rollovers
> - amounts rolled over or converted to a Roth IRA
> - plan loans treated as distributions
> - distributions of excess contributions or deferrals
> - IRA contributions returned by the due date
> - section 404(k) dividends
> - distributions from a military retirement plan (other than the TSP)
> - distributions from an inherited IRA as a nonspouse beneficiary

Shown on a one-person return:

> On a joint return: the distributions you received in 2023 and 2024 in a year for which you and your spouse filed a joint return, plus those you receive in 2026 before the due date of your 2025 return (including extensions), from any of the following; zero if none
>
> - a traditional or Roth IRA
> - a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP
> - another qualified retirement plan
>
> Do not include:
> - rollovers or trustee-to-trustee transfers
> - in-plan Roth rollovers
> - amounts rolled over or converted to a Roth IRA
> - plan loans treated as distributions
> - distributions of excess contributions or deferrals
> - IRA contributions returned by the due date
> - section 404(k) dividends
> - distributions from a military retirement plan (other than the TSP)
> - distributions from an inherited IRA as a nonspouse beneficiary

Shown for you on a couple's return:

> About you — On a joint return: the distributions you received in 2023 and 2024 in a year for which you and your spouse filed a joint return, plus those you receive in 2026 before the due date of your 2025 return (including extensions), from any of the following; zero if none
>
> - a traditional or Roth IRA
> - a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP
> - another qualified retirement plan
>
> Do not include:
> - rollovers or trustee-to-trustee transfers
> - in-plan Roth rollovers
> - amounts rolled over or converted to a Roth IRA
> - plan loans treated as distributions
> - distributions of excess contributions or deferrals
> - IRA contributions returned by the due date
> - section 404(k) dividends
> - distributions from a military retirement plan (other than the TSP)
> - distributions from an inherited IRA as a nonspouse beneficiary

Shown for your spouse:

> About your spouse — On a joint return: the distributions your spouse received in 2023 and 2024 in a year for which you and your spouse filed a joint return, plus those your spouse receives in 2026 before the due date of your spouse's 2025 return (including extensions), from any of the following; zero if none
>
> - a traditional or Roth IRA
> - a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP
> - another qualified retirement plan
>
> Do not include:
> - rollovers or trustee-to-trustee transfers
> - in-plan Roth rollovers
> - amounts rolled over or converted to a Roth IRA
> - plan loans treated as distributions
> - distributions of excess contributions or deferrals
> - IRA contributions returned by the due date
> - section 404(k) dividends
> - distributions from a military retirement plan (other than the TSP)
> - distributions from an inherited IRA as a nonspouse beneficiary

**Help, as stored**

> Distributions in these years go in both columns of Form 8880 line 4.

Shown on a one-person return:

> Distributions in these years go in both columns of Form 8880 line 4.

Shown for you on a couple's return:

> Distributions in these years go in both columns of Form 8880 line 4.

Shown for your spouse:

> Distributions in these years go in both columns of Form 8880 line 4.

## `person.sav_prior_other`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — The distributions you received in 2023 and 2024 in a year for which you did not file a joint return with your spouse on this return (on a return that is not a joint return: all your distributions in 2023 and 2024, and in 2026 before the due date of your 2025 return, including extensions), from any of the following; zero if none
>
> - a traditional or Roth IRA
> - a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP
> - another qualified retirement plan
>
> Do not include:
> - rollovers or trustee-to-trustee transfers
> - in-plan Roth rollovers
> - amounts rolled over or converted to a Roth IRA
> - plan loans treated as distributions
> - distributions of excess contributions or deferrals
> - IRA contributions returned by the due date
> - section 404(k) dividends
> - distributions from a military retirement plan (other than the TSP)
> - distributions from an inherited IRA as a nonspouse beneficiary

Shown on a one-person return:

> The distributions you received in 2023 and 2024 in a year for which you did not file a joint return with your spouse on this return (on a return that is not a joint return: all your distributions in 2023 and 2024, and in 2026 before the due date of your 2025 return, including extensions), from any of the following; zero if none
>
> - a traditional or Roth IRA
> - a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP
> - another qualified retirement plan
>
> Do not include:
> - rollovers or trustee-to-trustee transfers
> - in-plan Roth rollovers
> - amounts rolled over or converted to a Roth IRA
> - plan loans treated as distributions
> - distributions of excess contributions or deferrals
> - IRA contributions returned by the due date
> - section 404(k) dividends
> - distributions from a military retirement plan (other than the TSP)
> - distributions from an inherited IRA as a nonspouse beneficiary

Shown for you on a couple's return:

> About you — The distributions you received in 2023 and 2024 in a year for which you did not file a joint return with your spouse on this return (on a return that is not a joint return: all your distributions in 2023 and 2024, and in 2026 before the due date of your 2025 return, including extensions), from any of the following; zero if none
>
> - a traditional or Roth IRA
> - a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP
> - another qualified retirement plan
>
> Do not include:
> - rollovers or trustee-to-trustee transfers
> - in-plan Roth rollovers
> - amounts rolled over or converted to a Roth IRA
> - plan loans treated as distributions
> - distributions of excess contributions or deferrals
> - IRA contributions returned by the due date
> - section 404(k) dividends
> - distributions from a military retirement plan (other than the TSP)
> - distributions from an inherited IRA as a nonspouse beneficiary

Shown for your spouse:

> About your spouse — The distributions your spouse received in 2023 and 2024 in a year for which your spouse did not file a joint return with you on this return (on a return that is not a joint return: all your spouse's distributions in 2023 and 2024, and in 2026 before the due date of your spouse's 2025 return, including extensions), from any of the following; zero if none
>
> - a traditional or Roth IRA
> - a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP
> - another qualified retirement plan
>
> Do not include:
> - rollovers or trustee-to-trustee transfers
> - in-plan Roth rollovers
> - amounts rolled over or converted to a Roth IRA
> - plan loans treated as distributions
> - distributions of excess contributions or deferrals
> - IRA contributions returned by the due date
> - section 404(k) dividends
> - distributions from a military retirement plan (other than the TSP)
> - distributions from an inherited IRA as a nonspouse beneficiary

**Help, as stored**

> On a joint return these go only in your own column of Form 8880 line 4.

Shown on a one-person return:

> On a joint return these go only in your own column of Form 8880 line 4.

Shown for you on a couple's return:

> On a joint return these go only in your own column of Form 8880 line 4.

Shown for your spouse:

> On a joint return these go only in your spouse's own column of Form 8880 line 4.
