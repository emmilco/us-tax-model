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

- verbs after "you" that change for "your spouse": "are" to "is", "were" to "was", "have" to "has", "weren't" to "wasn't", "aren't" to "isn't", "don't" to "doesn't", "file" to "files", "teach" to "teaches", "contribute" to "contributes", "receive" to "receives", "stop" to "stops"
- verbs after "this person" or "your spouse" that change for "you": "is" to "are", "was" to "were", "has" to "have", "does" to "do", "isn't" to "aren't", "wasn't" to "weren't", "doesn't" to "don't"
- words after a subject or an object that need no change: "a", "acquired", "age", "agreed", "an", "and", "applied", "applying", "as", "at", "became", "blind", "born", "by", "can", "can't", "cannot", "claimed", "contributed", "could", "covered", "deducted", "deferred", "did", "died", "enrolled", "filed", "for", "fully", "had", "if", "in", "made", "more", "never", "of", "on", "or", "overtime", "paid", "received", "recharacterized", "repaid", "rolled", "served", "to", "took", "under", "with"

84 questions carry the frame.

## `f8889.allocation`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — you and your spouse each have an HSA and family coverage. Do you divide the family contribution limit equally (equal), or by a different allocation you both agree on, such as allocating nothing to one spouse (agreed)? Use the same answer on both Forms 8889.

Shown on a one-person return:

> You and your spouse each have an HSA and family coverage. Do you divide the family contribution limit equally (equal), or by a different allocation you both agree on, such as allocating nothing to one spouse (agreed)? Use the same answer on both Forms 8889.

Shown for you on a couple's return:

> About you — you and your spouse each have an HSA and family coverage. Do you divide the family contribution limit equally (equal), or by a different allocation you both agree on, such as allocating nothing to one spouse (agreed)? Use the same answer on both Forms 8889.

Shown for your spouse:

> About your spouse — you and your spouse each have an HSA and family coverage. Does your spouse divide the family contribution limit equally (equal), or by a different allocation you both agree on, such as allocating nothing to one spouse (agreed)? Use the same answer on both Forms 8889.

**Help, as stored**

> The family limit is figured on each Form 8889 for the months treated as having family coverage (Step 1 of the line 6 instructions).

Shown on a one-person return:

> The family limit is figured on each Form 8889 for the months treated as having family coverage (Step 1 of the line 6 instructions).

Shown for you on a couple's return:

> The family limit is figured on each Form 8889 for the months treated as having family coverage (Step 1 of the line 6 instructions).

Shown for your spouse:

> The family limit is figured on each Form 8889 for the months treated as having family coverage (Step 1 of the line 6 instructions).

## `f8889.allocated`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — the part of the family contribution limit (Step 1) allocated to this person under the allocation you agreed on. The two parts together may not be more than the limit.

Shown on a one-person return:

> The part of the family contribution limit (Step 1) allocated to you under the allocation you agreed on. The two parts together may not be more than the limit.

Shown for you on a couple's return:

> About you — the part of the family contribution limit (Step 1) allocated to you under the allocation you agreed on. The two parts together may not be more than the limit.

Shown for your spouse:

> About your spouse — the part of the family contribution limit (Step 1) allocated to your spouse under the allocation your spouse agreed on. The two parts together may not be more than the limit.

**Help, as stored**

> Your spouse's part is the rest of the limit.

Shown on a one-person return:

> Your spouse's part is the rest of the limit.

Shown for you on a couple's return:

> Your spouse's part is the rest of the limit.

Shown for your spouse:

> Your part is the rest of the limit.

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

## `f8889.employer_in_box1`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Are your employer's HSA contributions above the limit included in your wages in Form W-2 box 1? (Answer no if the employer has not included them; asked only when employer contributions exceed the limit.)

Shown on a one-person return:

> Are your employer's HSA contributions above the limit included in your wages in Form W-2 box 1? (Answer no if the employer has not included them; asked only when employer contributions exceed the limit.)

Shown for you on a couple's return:

> About you — Are your employer's HSA contributions above the limit included in your wages in Form W-2 box 1? (Answer no if the employer has not included them; asked only when employer contributions exceed the limit.)

Shown for your spouse:

> About your spouse — Are your spouse's employer's HSA contributions above the limit included in your spouse's wages in Form W-2 box 1? (Answer no if the employer has not included them; asked only when employer contributions exceed the limit.)

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

> For this person (you, or your spouse on a joint return) — Did you, your employer or someone else contribute to a health savings account (HSA) for you for 2025 (including a qualified HSA funding distribution, a direct transfer from your IRA to your HSA), did your HSA make a distribution in 2025 (Form 1099-SA), did you stop being an eligible individual during a testing period (Form 8889 Part III), or did you acquire an interest in an HSA because the account beneficiary died?

Shown on a one-person return:

> Did you, your employer or someone else contribute to a health savings account (HSA) for you for 2025 (including a qualified HSA funding distribution, a direct transfer from your IRA to your HSA), did your HSA make a distribution in 2025 (Form 1099-SA), did you stop being an eligible individual during a testing period (Form 8889 Part III), or did you acquire an interest in an HSA because the account beneficiary died?

Shown for you on a couple's return:

> About you — Did you, your employer or someone else contribute to a health savings account (HSA) for you for 2025 (including a qualified HSA funding distribution, a direct transfer from your IRA to your HSA), did your HSA make a distribution in 2025 (Form 1099-SA), did you stop being an eligible individual during a testing period (Form 8889 Part III), or did you acquire an interest in an HSA because the account beneficiary died?

Shown for your spouse:

> About your spouse — Did your spouse, your spouse's employer or someone else contribute to a health savings account (HSA) for your spouse for 2025 (including a qualified HSA funding distribution, a direct transfer from your spouse's IRA to your spouse's HSA), did your spouse's HSA make a distribution in 2025 (Form 1099-SA), did your spouse stop being an eligible individual during a testing period (Form 8889 Part III), or did your spouse acquire an interest in an HSA because the account beneficiary died?

**Help, as stored**

> One Form 8889 per person covers all of that person's HSAs.

Shown on a one-person return:

> One Form 8889 per person covers all of that person's HSAs.

Shown for you on a couple's return:

> One Form 8889 per person covers all of that person's HSAs.

Shown for your spouse:

> One Form 8889 per person covers all of that person's HSAs.

## `f8889.line2`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — HSA contributions you made for 2025 (or those made on your behalf), including those made by April 15, 2026 that were for 2025 (or by a later date if you served in, or in support of, the U.S. Armed Forces in a designated combat zone or contingency operation); do not include employer contributions, payroll contributions through a cafeteria plan, rollovers, amounts the trustee of another of your HSAs transferred directly to this one (a trustee-to-trustee transfer), or qualified HSA funding distributions; zero if none

Shown on a one-person return:

> HSA contributions you made for 2025 (or those made on your behalf), including those made by April 15, 2026 that were for 2025 (or by a later date if you served in, or in support of, the U.S. Armed Forces in a designated combat zone or contingency operation); do not include employer contributions, payroll contributions through a cafeteria plan, rollovers, amounts the trustee of another of your HSAs transferred directly to this one (a trustee-to-trustee transfer), or qualified HSA funding distributions; zero if none

Shown for you on a couple's return:

> About you — HSA contributions you made for 2025 (or those made on your behalf), including those made by April 15, 2026 that were for 2025 (or by a later date if you served in, or in support of, the U.S. Armed Forces in a designated combat zone or contingency operation); do not include employer contributions, payroll contributions through a cafeteria plan, rollovers, amounts the trustee of another of your HSAs transferred directly to this one (a trustee-to-trustee transfer), or qualified HSA funding distributions; zero if none

Shown for your spouse:

> About your spouse — HSA contributions your spouse made for 2025 (or those made on your spouse's behalf), including those made by April 15, 2026 that were for 2025 (or by a later date if your spouse served in, or in support of, the U.S. Armed Forces in a designated combat zone or contingency operation); do not include employer contributions, payroll contributions through a cafeteria plan, rollovers, amounts the trustee of another of your spouse's HSAs transferred directly to this one (a trustee-to-trustee transfer), or qualified HSA funding distributions; zero if none

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `f8889.line9`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Employer contributions to your HSAs for 2025, including payroll contributions through a cafeteria plan (Form W-2 box 12, code W, less employer contributions for 2024 included there, plus employer contributions for 2025 made in 2026); zero if none

Shown on a one-person return:

> Employer contributions to your HSAs for 2025, including payroll contributions through a cafeteria plan (Form W-2 box 12, code W, less employer contributions for 2024 included there, plus employer contributions for 2025 made in 2026); zero if none

Shown for you on a couple's return:

> About you — Employer contributions to your HSAs for 2025, including payroll contributions through a cafeteria plan (Form W-2 box 12, code W, less employer contributions for 2024 included there, plus employer contributions for 2025 made in 2026); zero if none

Shown for your spouse:

> About your spouse — Employer contributions to your spouse's HSAs for 2025, including payroll contributions through a cafeteria plan (Form W-2 box 12, code W, less employer contributions for 2024 included there, plus employer contributions for 2025 made in 2026); zero if none

**Help, as stored**

> Married filing separately and unsupported items are refused with citations.

Shown on a one-person return:

> Married filing separately and unsupported items are refused with citations.

Shown for you on a couple's return:

> Married filing separately and unsupported items are refused with citations.

Shown for your spouse:

> Married filing separately and unsupported items are refused with citations.

## `f8889.unsupported`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Any of these: a qualified HSA funding distribution from an IRA in 2025; contributions by you or your employer to an Archer MSA for 2025 (Form 8853), or, if you or your spouse had family coverage under an HDHP at any time during 2025, any contribution by anyone to your spouse's Archer MSA; excess HSA contributions from an earlier year that remain in your HSA; failing to remain an eligible individual during a testing period that began in an earlier year (last-month rule or qualified HSA funding distribution); an HSA you acquired because of the account beneficiary's death; the HSA of a person who died in 2025 whose estate is the beneficiary (its value at death is included on the final return); a deemed distribution from an HSA in 2025 (a prohibited transaction, or any part of an HSA used as security for a loan); a withdrawal of excess contributions or their earnings, made in 2025 or in 2026 by the due date of your 2025 return, including extensions; a mistaken distribution you repaid to your HSA; or this person died in 2025 (a joint return with a spouse who died in 2025, or the final return of a person who died in 2025), since the last month of a decedent's tax year is the month of death, not December?

Shown on a one-person return:

> Any of these: a qualified HSA funding distribution from an IRA in 2025; contributions by you or your employer to an Archer MSA for 2025 (Form 8853), or, if you or your spouse had family coverage under an HDHP at any time during 2025, any contribution by anyone to your spouse's Archer MSA; excess HSA contributions from an earlier year that remain in your HSA; failing to remain an eligible individual during a testing period that began in an earlier year (last-month rule or qualified HSA funding distribution); an HSA you acquired because of the account beneficiary's death; the HSA of a person who died in 2025 whose estate is the beneficiary (its value at death is included on the final return); a deemed distribution from an HSA in 2025 (a prohibited transaction, or any part of an HSA used as security for a loan); a withdrawal of excess contributions or their earnings, made in 2025 or in 2026 by the due date of your 2025 return, including extensions; a mistaken distribution you repaid to your HSA; or you died in 2025 (a joint return with a spouse who died in 2025, or the final return of a person who died in 2025), since the last month of a decedent's tax year is the month of death, not December?

Shown for you on a couple's return:

> About you — Any of these: a qualified HSA funding distribution from an IRA in 2025; contributions by you or your employer to an Archer MSA for 2025 (Form 8853), or, if you or your spouse had family coverage under an HDHP at any time during 2025, any contribution by anyone to your spouse's Archer MSA; excess HSA contributions from an earlier year that remain in your HSA; failing to remain an eligible individual during a testing period that began in an earlier year (last-month rule or qualified HSA funding distribution); an HSA you acquired because of the account beneficiary's death; the HSA of a person who died in 2025 whose estate is the beneficiary (its value at death is included on the final return); a deemed distribution from an HSA in 2025 (a prohibited transaction, or any part of an HSA used as security for a loan); a withdrawal of excess contributions or their earnings, made in 2025 or in 2026 by the due date of your 2025 return, including extensions; a mistaken distribution you repaid to your HSA; or you died in 2025 (a joint return with a spouse who died in 2025, or the final return of a person who died in 2025), since the last month of a decedent's tax year is the month of death, not December?

Shown for your spouse:

> About your spouse — Any of these: a qualified HSA funding distribution from an IRA in 2025; contributions by your spouse or your spouse's employer to an Archer MSA for 2025 (Form 8853), or, if you or your spouse had family coverage under an HDHP at any time during 2025, any contribution by anyone to your Archer MSA; excess HSA contributions from an earlier year that remain in your spouse's HSA; failing to remain an eligible individual during a testing period that began in an earlier year (last-month rule or qualified HSA funding distribution); an HSA your spouse acquired because of the account beneficiary's death; the HSA of a person who died in 2025 whose estate is the beneficiary (its value at death is included on the final return); a deemed distribution from an HSA in 2025 (a prohibited transaction, or any part of an HSA used as security for a loan); a withdrawal of excess contributions or their earnings, made in 2025 or in 2026 by the due date of your spouse's 2025 return, including extensions; a mistaken distribution your spouse repaid to your spouse's HSA; or your spouse died in 2025 (a joint return with a spouse who died in 2025, or the final return of a person who died in 2025), since the last month of a decedent's tax year is the month of death, not December?

**Help, as stored**

> HSA distributions that were not used for qualified medical expenses are not among these; Form 8889 Part II asks about them separately.

Shown on a one-person return:

> HSA distributions that were not used for qualified medical expenses are not among these; Form 8889 Part II asks about them separately.

Shown for you on a couple's return:

> HSA distributions that were not used for qualified medical expenses are not among these; Form 8889 Part II asks about them separately.

Shown for your spouse:

> HSA distributions that were not used for qualified medical expenses are not among these; Form 8889 Part II asks about them separately.

## `f8889.coverage_year`

**Question, as stored**

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

Shown on a one-person return:

> Was your high-deductible health plan (HDHP) coverage self-only all year, family all year, or did it change during 2025 (including starting or ending)?
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

Shown for you on a couple's return:

> About you — Was your high-deductible health plan (HDHP) coverage self-only all year, family all year, or did it change during 2025 (including starting or ending)?
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

Shown for your spouse:

> About your spouse — Was your spouse's high-deductible health plan (HDHP) coverage self-only all year, family all year, or did it change during 2025 (including starting or ending)?
>
> - Self-only all year: on the first day of every month of 2025 your spouse was an eligible individual with self-only HDHP coverage, and no month counts as family coverage under the rules below.
> - Family all year: on the first day of every month of 2025 your spouse was an eligible individual with family HDHP coverage, or counted as having it under the rules below.
> - Changed: anything else, including coverage that started, ended or changed type during 2025, any month in which your spouse was not an eligible individual, or if your spouse is not sure. The month-by-month questions follow.
>
> An eligible individual on the first day of a month:
> - is covered by an HDHP
> - has no other health coverage, apart from the coverage the instructions disregard (accident, disability, dental, vision, long-term care, telehealth and other remote care, workers' compensation, tort or property liability insurance, insurance for a specified disease or illness, and insurance paying a fixed amount per day of hospitalization); a general-purpose health FSA or HRA that pays your spouse's medical expenses, yours or your spouse's, is other health coverage, while VA care for a service-connected disability and benefits under surprise billing laws are not
> - is not enrolled in Medicare, counting Medicare coverage backdated to an earlier month
> - cannot be claimed as a dependent on someone else's 2025 return
>
> A month counts as family coverage:
> - if your spouse was covered by a family HDHP (HDHP coverage for your spouse and at least one other person, such as an employee-plus-spouse or employee-plus-children tier), including as a member of someone else's plan (yours or a parent's, for example)
> - if your spouse was covered by a self-only HDHP and a family HDHP at the same time
> - if you and your spouse were both eligible individuals and either of you had family HDHP coverage

**Help, as stored**

> The first day of each month is what counts. Medicare enrollment, other health coverage that is not disregarded, or being someone else's dependent in any month means the coverage was not the same all year; choose Changed.

Shown on a one-person return:

> The first day of each month is what counts. Medicare enrollment, other health coverage that is not disregarded, or being someone else's dependent in any month means the coverage was not the same all year; choose Changed.

Shown for you on a couple's return:

> The first day of each month is what counts. Medicare enrollment, other health coverage that is not disregarded, or being someone else's dependent in any month means the coverage was not the same all year; choose Changed.

Shown for your spouse:

> The first day of each month is what counts. Medicare enrollment, other health coverage that is not disregarded, or being someone else's dependent in any month means the coverage was not the same all year; choose Changed.

## `f8889.months_eligible`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Number of months of 2025 on the first day of which you were an eligible individual (covered by a high-deductible health plan, with no other disqualifying health coverage, not enrolled in Medicare, and not able to be claimed as a dependent on someone else's 2025 return)

Shown on a one-person return:

> Number of months of 2025 on the first day of which you were an eligible individual (covered by a high-deductible health plan, with no other disqualifying health coverage, not enrolled in Medicare, and not able to be claimed as a dependent on someone else's 2025 return)

Shown for you on a couple's return:

> About you — Number of months of 2025 on the first day of which you were an eligible individual (covered by a high-deductible health plan, with no other disqualifying health coverage, not enrolled in Medicare, and not able to be claimed as a dependent on someone else's 2025 return)

Shown for your spouse:

> About your spouse — Number of months of 2025 on the first day of which your spouse was an eligible individual (covered by a high-deductible health plan, with no other disqualifying health coverage, not enrolled in Medicare, and not able to be claimed as a dependent on someone else's 2025 return)

**Help, as stored**

> Count a month only if every condition held on its first day. December 1 counts as one of the months.

Shown on a one-person return:

> Count a month only if every condition held on its first day. December 1 counts as one of the months.

Shown for you on a couple's return:

> Count a month only if every condition held on its first day. December 1 counts as one of the months.

Shown for your spouse:

> Count a month only if every condition held on its first day. December 1 counts as one of the months.

## `f8889.months_family`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Of those eligible months, the number in which you had or were treated as having family (not self-only) high-deductible health plan coverage on the first day of the month; zero if your coverage was self-only in all of them. If you and your spouse were both eligible individuals for a month and either of you had family HDHP coverage, count that month as family coverage for both of you and disregard either spouse's self-only plan. Count the actual eligible months here; the separate last-month-rule question determines whether December 1 coverage is treated as applying throughout the year.

Shown on a one-person return:

> Of those eligible months, the number in which you had or were treated as having family (not self-only) high-deductible health plan coverage on the first day of the month; zero if your coverage was self-only in all of them. If you and your spouse were both eligible individuals for a month and either of you had family HDHP coverage, count that month as family coverage for both of you and disregard either spouse's self-only plan. Count the actual eligible months here; the separate last-month-rule question determines whether December 1 coverage is treated as applying throughout the year.

Shown for you on a couple's return:

> About you — Of those eligible months, the number in which you had or were treated as having family (not self-only) high-deductible health plan coverage on the first day of the month; zero if your coverage was self-only in all of them. If you and your spouse were both eligible individuals for a month and either of you had family HDHP coverage, count that month as family coverage for both of you and disregard either spouse's self-only plan. Count the actual eligible months here; the separate last-month-rule question determines whether December 1 coverage is treated as applying throughout the year.

Shown for your spouse:

> About your spouse — Of those eligible months, the number in which your spouse had or was treated as having family (not self-only) high-deductible health plan coverage on the first day of the month; zero if your spouse's coverage was self-only in all of them. If you and your spouse were both eligible individuals for a month and either of you had family HDHP coverage, count that month as family coverage for both of you and disregard either spouse's self-only plan. Count the actual eligible months here; the separate last-month-rule question determines whether December 1 coverage is treated as applying throughout the year.

**Help, as stored**

> Count only months of family coverage, not every month you were covered.

Shown on a one-person return:

> Count only months of family coverage, not every month you were covered.

Shown for you on a couple's return:

> Count only months of family coverage, not every month you were covered.

Shown for your spouse:

> Count only months of family coverage, not every month your spouse was covered.

## `f8889.age55`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you age 55 or older at the end of 2025?

Shown on a one-person return:

> Were you age 55 or older at the end of 2025?

Shown for you on a couple's return:

> About you — Were you age 55 or older at the end of 2025?

Shown for your spouse:

> About your spouse — Was your spouse age 55 or older at the end of 2025?

## `f8889.dec_coverage`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — The high-deductible health plan coverage you had or were treated as having on December 1, 2025: none (you were not an eligible individual that day), self_only, or family. Family is HDHP coverage for you and at least one other person, and includes coverage as a member of someone else's family HDHP (your spouse's or a parent's, for example) and a self-only HDHP and a family HDHP held at the same time. If you and your spouse were both eligible individuals that day and either of you had family HDHP coverage, answer family for both spouses and disregard either spouse's self-only plan.

Shown on a one-person return:

> The high-deductible health plan coverage you had or were treated as having on December 1, 2025: none (you were not an eligible individual that day), self_only, or family. Family is HDHP coverage for you and at least one other person, and includes coverage as a member of someone else's family HDHP (your spouse's or a parent's, for example) and a self-only HDHP and a family HDHP held at the same time. If you and your spouse were both eligible individuals that day and either of you had family HDHP coverage, answer family for both spouses and disregard either spouse's self-only plan.

Shown for you on a couple's return:

> About you — The high-deductible health plan coverage you had or were treated as having on December 1, 2025: none (you were not an eligible individual that day), self_only, or family. Family is HDHP coverage for you and at least one other person, and includes coverage as a member of someone else's family HDHP (your spouse's or a parent's, for example) and a self-only HDHP and a family HDHP held at the same time. If you and your spouse were both eligible individuals that day and either of you had family HDHP coverage, answer family for both spouses and disregard either spouse's self-only plan.

Shown for your spouse:

> About your spouse — The high-deductible health plan coverage your spouse had or was treated as having on December 1, 2025: none (your spouse was not an eligible individual that day), self_only, or family. Family is HDHP coverage for your spouse and at least one other person, and includes coverage as a member of someone else's family HDHP (yours or a parent's, for example) and a self-only HDHP and a family HDHP held at the same time. If you and your spouse were both eligible individuals that day and either of you had family HDHP coverage, answer family for both spouses and disregard either spouse's self-only plan.

## `f8889.last_month`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Do you use the last-month rule: treat yourself as an eligible individual for all of 2025 with the coverage you had on December 1, 2025, which requires you to remain an eligible individual from December 1, 2025 through December 31, 2026 (the testing period)?

Shown on a one-person return:

> Do you use the last-month rule: treat yourself as an eligible individual for all of 2025 with the coverage you had on December 1, 2025, which requires you to remain an eligible individual from December 1, 2025 through December 31, 2026 (the testing period)?

Shown for you on a couple's return:

> About you — Do you use the last-month rule: treat yourself as an eligible individual for all of 2025 with the coverage you had on December 1, 2025, which requires you to remain an eligible individual from December 1, 2025 through December 31, 2026 (the testing period)?

Shown for your spouse:

> About your spouse — Does your spouse use the last-month rule: treat himself or herself as an eligible individual for all of 2025 with the coverage your spouse had on December 1, 2025, which requires your spouse to remain an eligible individual from December 1, 2025 through December 31, 2026 (the testing period)?

**Help, as stored**

> If you stop being an eligible individual during the testing period (other than by death or disability), the contributions the rule allowed are included in income, with a 10% additional tax (Form 8889 Part III).

Shown on a one-person return:

> If you stop being an eligible individual during the testing period (other than by death or disability), the contributions the rule allowed are included in income, with a 10% additional tax (Form 8889 Part III).

Shown for you on a couple's return:

> If you stop being an eligible individual during the testing period (other than by death or disability), the contributions the rule allowed are included in income, with a 10% additional tax (Form 8889 Part III).

Shown for your spouse:

> If your spouse stops being an eligible individual during the testing period (other than by death or disability), the contributions the rule allowed are included in income, with a 10% additional tax (Form 8889 Part III).

## `f8889.line14a`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Total distributions you received in 2025 from all of your own HSAs (box 1 of your Forms 1099-SA, including distributions you rolled over, but not an amount the trustee transferred directly to the trustee of another of your HSAs); zero if none

Shown on a one-person return:

> Total distributions you received in 2025 from all of your own HSAs (box 1 of your Forms 1099-SA, including distributions you rolled over, but not an amount the trustee transferred directly to the trustee of another of your HSAs); zero if none

Shown for you on a couple's return:

> About you — Total distributions you received in 2025 from all of your own HSAs (box 1 of your Forms 1099-SA, including distributions you rolled over, but not an amount the trustee transferred directly to the trustee of another of your HSAs); zero if none

Shown for your spouse:

> About your spouse — Total distributions your spouse received in 2025 from all of your spouse's own HSAs (box 1 of your spouse's Forms 1099-SA, including distributions your spouse rolled over, but not an amount the trustee transferred directly to the trustee of another of your spouse's HSAs); zero if none

**Help, as stored**

> A direct transfer from one of your HSAs to another (trustee to trustee) is not a distribution.

Shown on a one-person return:

> A direct transfer from one of your HSAs to another (trustee to trustee) is not a distribution.

Shown for you on a couple's return:

> A direct transfer from one of your HSAs to another (trustee to trustee) is not a distribution.

Shown for your spouse:

> A direct transfer from one of your spouse's HSAs to another (trustee to trustee) is not a distribution.

## `f8889.rollover`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — The part of those distributions that you rolled over within 60 days to another HSA of yours (an HSA of the same account beneficiary); do not count a rollover into an HSA that had already received a rollover contribution in the 1-year period before it, since an HSA can receive only one rollover contribution during a 1-year period; zero if none

Shown on a one-person return:

> The part of those distributions that you rolled over within 60 days to another HSA of yours (an HSA of the same account beneficiary); do not count a rollover into an HSA that had already received a rollover contribution in the 1-year period before it, since an HSA can receive only one rollover contribution during a 1-year period; zero if none

Shown for you on a couple's return:

> About you — The part of those distributions that you rolled over within 60 days to another HSA of yours (an HSA of the same account beneficiary); do not count a rollover into an HSA that had already received a rollover contribution in the 1-year period before it, since an HSA can receive only one rollover contribution during a 1-year period; zero if none

Shown for your spouse:

> About your spouse — The part of those distributions that your spouse rolled over within 60 days to another HSA of your spouse's (an HSA of the same account beneficiary); do not count a rollover into an HSA that had already received a rollover contribution in the 1-year period before it, since an HSA can receive only one rollover contribution during a 1-year period; zero if none

**Help, as stored**

> An HSA can receive only one rollover in a 1-year period.

Shown on a one-person return:

> An HSA can receive only one rollover in a 1-year period.

Shown for you on a couple's return:

> An HSA can receive only one rollover in a 1-year period.

Shown for your spouse:

> An HSA can receive only one rollover in a 1-year period.

## `f8889.medical`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — The part of your 2025 HSA distributions used to pay qualified medical expenses (not reimbursed by insurance or other coverage, and incurred after the HSA was established) of you, your spouse, your dependents, and anyone who would be your dependent except that they filed a joint return, had gross income, or you (or your spouse, on a joint return) could be claimed as someone else's dependent; a child of divorced or separated parents counts for both parents. Insurance premiums count only if they are for long-term care insurance, health care continuation coverage (such as COBRA), health care coverage while receiving unemployment compensation under federal or state law, or Medicare and other health care coverage if you were 65 or older (not a Medicare supplemental policy, such as Medigap); continuation coverage and coverage while receiving unemployment compensation can be for your spouse or a dependent, but if you, the HSA owner, are under 65, Medicare premiums for your spouse or dependents generally do not count; zero if none

Shown on a one-person return:

> The part of your 2025 HSA distributions used to pay qualified medical expenses (not reimbursed by insurance or other coverage, and incurred after the HSA was established) of you, your spouse, your dependents, and anyone who would be your dependent except that they filed a joint return, had gross income, or you (or your spouse, on a joint return) could be claimed as someone else's dependent; a child of divorced or separated parents counts for both parents. Insurance premiums count only if they are for long-term care insurance, health care continuation coverage (such as COBRA), health care coverage while receiving unemployment compensation under federal or state law, or Medicare and other health care coverage if you were 65 or older (not a Medicare supplemental policy, such as Medigap); continuation coverage and coverage while receiving unemployment compensation can be for your spouse or a dependent, but if you, the HSA owner, are under 65, Medicare premiums for your spouse or dependents generally do not count; zero if none

Shown for you on a couple's return:

> About you — The part of your 2025 HSA distributions used to pay qualified medical expenses (not reimbursed by insurance or other coverage, and incurred after the HSA was established) of you, your spouse, your dependents, and anyone who would be your dependent except that they filed a joint return, had gross income, or you (or your spouse, on a joint return) could be claimed as someone else's dependent; a child of divorced or separated parents counts for both parents. Insurance premiums count only if they are for long-term care insurance, health care continuation coverage (such as COBRA), health care coverage while receiving unemployment compensation under federal or state law, or Medicare and other health care coverage if you were 65 or older (not a Medicare supplemental policy, such as Medigap); continuation coverage and coverage while receiving unemployment compensation can be for your spouse or a dependent, but if you, the HSA owner, are under 65, Medicare premiums for your spouse or dependents generally do not count; zero if none

Shown for your spouse:

> About your spouse — The part of your spouse's 2025 HSA distributions used to pay qualified medical expenses (not reimbursed by insurance or other coverage, and incurred after the HSA was established) of your spouse, you, your spouse's dependents, and anyone who would be your spouse's dependent except that they filed a joint return, had gross income, or you (or your spouse, on a joint return) could be claimed as someone else's dependent; a child of divorced or separated parents counts for both parents. Insurance premiums count only if they are for long-term care insurance, health care continuation coverage (such as COBRA), health care coverage while receiving unemployment compensation under federal or state law, or Medicare and other health care coverage if your spouse was 65 or older (not a Medicare supplemental policy, such as Medigap); continuation coverage and coverage while receiving unemployment compensation can be for you or a dependent, but if your spouse, the HSA owner, is under 65, Medicare premiums for you or dependents generally do not count; zero if none

**Help, as stored**

> You cannot also deduct these expenses on Schedule A.

Shown on a one-person return:

> You cannot also deduct these expenses on Schedule A.

Shown for you on a couple's return:

> You cannot also deduct these expenses on Schedule A.

Shown for your spouse:

> Your spouse cannot also deduct these expenses on Schedule A.

## `f8889.line17a`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were any of your taxable HSA distributions made after you became disabled or turned age 65 (the exceptions to the additional 20% tax)?

Shown on a one-person return:

> Were any of your taxable HSA distributions made after you became disabled or turned age 65 (the exceptions to the additional 20% tax)?

Shown for you on a couple's return:

> About you — Were any of your taxable HSA distributions made after you became disabled or turned age 65 (the exceptions to the additional 20% tax)?

Shown for your spouse:

> About your spouse — Were any of your spouse's taxable HSA distributions made after your spouse became disabled or turned age 65 (the exceptions to the additional 20% tax)?

**Help, as stored**

> Answer No if every taxable distribution was made before you became disabled or turned 65.

Shown on a one-person return:

> Answer No if every taxable distribution was made before you became disabled or turned 65.

Shown for you on a couple's return:

> Answer No if every taxable distribution was made before you became disabled or turned 65.

Shown for your spouse:

> Answer No if every taxable distribution was made before your spouse became disabled or turned 65.

## `f8889.subject_part`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — The part of your taxable HSA distributions (Form 8889 line 16) that was made before you became disabled or turned age 65 (the part subject to the additional 20% tax); zero if all of it was made after

Shown on a one-person return:

> The part of your taxable HSA distributions (Form 8889 line 16) that was made before you became disabled or turned age 65 (the part subject to the additional 20% tax); zero if all of it was made after

Shown for you on a couple's return:

> About you — The part of your taxable HSA distributions (Form 8889 line 16) that was made before you became disabled or turned age 65 (the part subject to the additional 20% tax); zero if all of it was made after

Shown for your spouse:

> About your spouse — The part of your spouse's taxable HSA distributions (Form 8889 line 16) that was made before your spouse became disabled or turned age 65 (the part subject to the additional 20% tax); zero if all of it was made after

**Help, as stored**

> The taxable distributions are your distributions less rollovers and the part used for qualified medical expenses.

Shown on a one-person return:

> The taxable distributions are your distributions less rollovers and the part used for qualified medical expenses.

Shown for you on a couple's return:

> The taxable distributions are your distributions less rollovers and the part used for qualified medical expenses.

Shown for your spouse:

> The taxable distributions are your spouse's distributions less rollovers and the part used for qualified medical expenses.

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
