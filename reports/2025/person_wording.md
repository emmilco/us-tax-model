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

120 questions carry the frame.

## `$k1p`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Which partnerships or LLCs sent you a Schedule K-1 (Form 1065) for 2025?

Shown on a one-person return:

> Which partnerships or LLCs sent you a Schedule K-1 (Form 1065) for 2025?

Shown for you on a couple's return:

> About you — Which partnerships or LLCs sent you a Schedule K-1 (Form 1065) for 2025?

Shown for your spouse:

> About your spouse — Which partnerships or LLCs sent your spouse a Schedule K-1 (Form 1065) for 2025?

**Help, as stored**

> List each Schedule K-1 (Form 1065) once, by the partnership's name in item B. A Schedule K-1 from an S corporation (Form 1120-S) or from an estate or trust (Form 1041) is not listed here.

Shown on a one-person return:

> List each Schedule K-1 (Form 1065) once, by the partnership's name in item B. A Schedule K-1 from an S corporation (Form 1120-S) or from an estate or trust (Form 1041) is not listed here.

Shown for you on a couple's return:

> List each Schedule K-1 (Form 1065) once, by the partnership's name in item B. A Schedule K-1 from an S corporation (Form 1120-S) or from an estate or trust (Form 1041) is not listed here.

Shown for your spouse:

> List each Schedule K-1 (Form 1065) once, by the partnership's name in item B. A Schedule K-1 from an S corporation (Form 1120-S) or from an estate or trust (Form 1041) is not listed here.

## `person.rrta`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you work for a railroad in 2025?

Shown on a one-person return:

> Did you work for a railroad in 2025?

Shown for you on a couple's return:

> About you — Did you work for a railroad in 2025?

Shown for your spouse:

> About your spouse — Did your spouse work for a railroad in 2025?

**Help, as stored**

> Yes also if box 14 of a W-2 shows railroad retirement (RRTA) pay or tax, or if you filed Form CT-2. A Yes ends the interview here.

Shown on a one-person return:

> Yes also if box 14 of a W-2 shows railroad retirement (RRTA) pay or tax, or if you filed Form CT-2. A Yes ends the interview here.

Shown for you on a couple's return:

> Yes also if box 14 of a W-2 shows railroad retirement (RRTA) pay or tax, or if you filed Form CT-2. A Yes ends the interview here.

Shown for your spouse:

> Yes also if box 14 of a W-2 shows railroad retirement (RRTA) pay or tax, or if your spouse filed Form CT-2. A Yes ends the interview here.

## `person.birth_year`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — In what year were you born?

Shown on a one-person return:

> In what year were you born?

Shown for you on a couple's return:

> About you — In what year were you born?

Shown for your spouse:

> About your spouse — In what year was your spouse born?

## `person.born_jan1`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you born on January 1?

Shown on a one-person return:

> Were you born on January 1?

Shown for you on a couple's return:

> About you — Were you born on January 1?

Shown for your spouse:

> About your spouse — Was your spouse born on January 1?

**Help, as stored**

> For several rules of this return a person born on January 1 counts as a year older on the December 31 before.

Shown on a one-person return:

> For several rules of this return a person born on January 1 counts as a year older on the December 31 before.

Shown for you on a couple's return:

> For several rules of this return a person born on January 1 counts as a year older on the December 31 before.

Shown for your spouse:

> For several rules of this return a person born on January 1 counts as a year older on the December 31 before.

## `person.under16_at_year_end`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you under age 16 at the end of 2025?

Shown on a one-person return:

> Were you under age 16 at the end of 2025?

Shown for you on a couple's return:

> About you — Were you under age 16 at the end of 2025?

Shown for your spouse:

> About your spouse — Was your spouse under age 16 at the end of 2025?

**Help, as stored**

> A Yes ends the interview here.

Shown on a one-person return:

> A Yes ends the interview here.

Shown for you on a couple's return:

> A Yes ends the interview here.

Shown for your spouse:

> A Yes ends the interview here.

## `person.died_at_64`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you die in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)

Shown on a one-person return:

> Did you die in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)

Shown for you on a couple's return:

> About you — Did you die in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)

Shown for your spouse:

> About your spouse — Did your spouse die in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)

**Help, as stored**

> It decides whether the higher standard deduction and the deduction for people 65 or older apply. For a living person the answer is No.

Shown on a one-person return:

> It decides whether the higher standard deduction and the deduction for people 65 or older apply. For a living person the answer is No.

Shown for you on a couple's return:

> It decides whether the higher standard deduction and the deduction for people 65 or older apply. For a living person the answer is No.

Shown for your spouse:

> It decides whether the higher standard deduction and the deduction for people 65 or older apply. For a living person the answer is No.

## `person.blind`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you blind on December 31, 2025? (Partly blind counts only if an eye doctor has certified it in writing; the help gives the limits.)

Shown on a one-person return:

> Were you blind on December 31, 2025? (Partly blind counts only if an eye doctor has certified it in writing; the help gives the limits.)

Shown for you on a couple's return:

> About you — Were you blind on December 31, 2025? (Partly blind counts only if an eye doctor has certified it in writing; the help gives the limits.)

Shown for your spouse:

> About your spouse — Was your spouse blind on December 31, 2025? (Partly blind counts only if an eye doctor has certified it in writing; the help gives the limits.)

**Help, as stored**

> The statement must say that your better eye sees no better than 20/200 with glasses or contact lenses, or that your field of vision is 20 degrees or less, or that your sight is not likely to improve beyond those limits. Lenses you can wear only briefly (pain, infection, ulcers) do not count.

Shown on a one-person return:

> The statement must say that your better eye sees no better than 20/200 with glasses or contact lenses, or that your field of vision is 20 degrees or less, or that your sight is not likely to improve beyond those limits. Lenses you can wear only briefly (pain, infection, ulcers) do not count.

Shown for you on a couple's return:

> The statement must say that your better eye sees no better than 20/200 with glasses or contact lenses, or that your field of vision is 20 degrees or less, or that your sight is not likely to improve beyond those limits. Lenses you can wear only briefly (pain, infection, ulcers) do not count.

Shown for your spouse:

> The statement must say that your spouse's better eye sees no better than 20/200 with glasses or contact lenses, or that your spouse's field of vision is 20 degrees or less, or that your spouse's sight is not likely to improve beyond those limits. Lenses your spouse can wear only briefly (pain, infection, ulcers) do not count.

## `person.household_wages`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much were you paid in 2025 for work in or around a household's home, or for its members, by households that gave no W-2? Zero if none.

Shown on a one-person return:

> How much were you paid in 2025 for work in or around a household's home, or for its members, by households that gave no W-2? Zero if none.

Shown for you on a couple's return:

> About you — How much were you paid in 2025 for work in or around a household's home, or for its members, by households that gave no W-2? Zero if none.

Shown for your spouse:

> About your spouse — How much was your spouse paid in 2025 for work in or around a household's home, or for its members, by households that gave no W-2? Zero if none.

**Help, as stored**

> Add up the pay from every household that gave no W-2 for it, for work in or around its home or for its members. Pay on a W-2 is entered with the W-2s.

Shown on a one-person return:

> Add up the pay from every household that gave no W-2 for it, for work in or around its home or for its members. Pay on a W-2 is entered with the W-2s.

Shown for you on a couple's return:

> Add up the pay from every household that gave no W-2 for it, for work in or around its home or for its members. Pay on a W-2 is entered with the W-2s.

Shown for your spouse:

> Add up the pay from every household that gave no W-2 for it, for work in or around its home or for its members. Pay on a W-2 is entered with the W-2s.

## `$f8919firm`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Which firms paid you in that way in 2025?

Shown on a one-person return:

> Which firms paid you in that way in 2025?

Shown for you on a couple's return:

> About you — Which firms paid you in that way in 2025?

Shown for your spouse:

> About your spouse — Which firms paid your spouse in that way in 2025?

**Help, as stored**

> Name only firms that treated you as a contractor when, in your view, you were their employee. If none did, leave the list empty.

Shown on a one-person return:

> Name only firms that treated you as a contractor when, in your view, you were their employee. If none did, leave the list empty.

Shown for you on a couple's return:

> Name only firms that treated you as a contractor when, in your view, you were their employee. If none did, leave the list empty.

Shown for your spouse:

> Name only firms that treated your spouse as a contractor when, in your spouse's view, your spouse was their employee. If none did, leave the list empty.

## `person.strike`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much did you get in 2025 in strike or lockout benefits? Leave out true gifts and state unemployment pay. Zero if none.

Shown on a one-person return:

> How much did you get in 2025 in strike or lockout benefits? Leave out true gifts and state unemployment pay. Zero if none.

Shown for you on a couple's return:

> About you — How much did you get in 2025 in strike or lockout benefits? Leave out true gifts and state unemployment pay. Zero if none.

Shown for your spouse:

> About your spouse — How much did your spouse get in 2025 in strike or lockout benefits? Leave out true gifts and state unemployment pay. Zero if none.

## `$f4137row`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — At which employers did you get tips you did not report in full?

Shown on a one-person return:

> At which employers did you get tips you did not report in full?

Shown for you on a couple's return:

> About you — At which employers did you get tips you did not report in full?

Shown for your spouse:

> About your spouse — At which employers did your spouse get tips your spouse did not report in full?

**Help, as stored**

> Name each employer at which you received cash or card tips you did not report in full to the employer. If the only tips were tickets or other things, leave the list empty.

Shown on a one-person return:

> Name each employer at which you received cash or card tips you did not report in full to the employer. If the only tips were tickets or other things, leave the list empty.

Shown for you on a couple's return:

> Name each employer at which you received cash or card tips you did not report in full to the employer. If the only tips were tickets or other things, leave the list empty.

Shown for your spouse:

> Name each employer at which your spouse received cash or card tips your spouse did not report in full to the employer. If the only tips were tickets or other things, leave the list empty.

## `person.f4137_under20`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Of the cash and card tips you did not report, how much was from a month in which your tips at that job were under $20? Zero if none.

Shown on a one-person return:

> Of the cash and card tips you did not report, how much was from a month in which your tips at that job were under $20? Zero if none.

Shown for you on a couple's return:

> About you — Of the cash and card tips you did not report, how much was from a month in which your tips at that job were under $20? Zero if none.

Shown for your spouse:

> About your spouse — Of the cash and card tips your spouse did not report, how much was from a month in which your spouse's tips at that job were under $20? Zero if none.

**Help, as stored**

> Tips under $20 in a month at one job did not have to be reported to the employer. They are still income but carry no social security or Medicare tax.

Shown on a one-person return:

> Tips under $20 in a month at one job did not have to be reported to the employer. They are still income but carry no social security or Medicare tax.

Shown for you on a couple's return:

> Tips under $20 in a month at one job did not have to be reported to the employer. They are still income but carry no social security or Medicare tax.

Shown for your spouse:

> Tips under $20 in a month at one job did not have to be reported to the employer. They are still income but carry no social security or Medicare tax.

## `person.tips_gov`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you receive any of these unreported tips for work as a federal, state or local government employee whose pay was subject only to the 1.45% Medicare tax?

Shown on a one-person return:

> Did you receive any of these unreported tips for work as a federal, state or local government employee whose pay was subject only to the 1.45% Medicare tax?

Shown for you on a couple's return:

> About you — Did you receive any of these unreported tips for work as a federal, state or local government employee whose pay was subject only to the 1.45% Medicare tax?

Shown for your spouse:

> About your spouse — Did your spouse receive any of these unreported tips for work as a federal, state or local government employee whose pay was subject only to the 1.45% Medicare tax?

**Help, as stored**

> A Yes ends the interview here.

Shown on a one-person return:

> A Yes ends the interview here.

Shown for you on a couple's return:

> A Yes ends the interview here.

Shown for your spouse:

> A Yes ends the interview here.

## `person.tips_noncash`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — What was the value of the tips you received in 2025 that were not money, such as tickets, passes or other items of value? Zero if none.

Shown on a one-person return:

> What was the value of the tips you received in 2025 that were not money, such as tickets, passes or other items of value? Zero if none.

Shown for you on a couple's return:

> About you — What was the value of the tips you received in 2025 that were not money, such as tickets, passes or other items of value? Zero if none.

Shown for your spouse:

> About your spouse — What was the value of the tips your spouse received in 2025 that were not money, such as tickets, passes or other items of value? Zero if none.

**Help, as stored**

> Value them at what they were worth. You do not report these to the employer.

Shown on a one-person return:

> Value them at what they were worth. You do not report these to the employer.

Shown for you on a couple's return:

> Value them at what they were worth. You do not report these to the employer.

Shown for your spouse:

> Value them at what they were worth. Your spouse does not report these to the employer.

## `person.mw_box1`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much 2025 Medicaid pay for caring for someone who lived with you in your home is in box 1 of your W-2s? Zero if none.

Shown on a one-person return:

> How much 2025 Medicaid pay for caring for someone who lived with you in your home is in box 1 of your W-2s? Zero if none.

Shown for you on a couple's return:

> About you — How much 2025 Medicaid pay for caring for someone who lived with you in your home is in box 1 of your W-2s? Zero if none.

Shown for your spouse:

> About your spouse — How much 2025 Medicaid pay for caring for someone who lived with your spouse in your spouse's home is in box 1 of your spouse's W-2s? Zero if none.

**Help, as stored**

> Count only pay for caring for someone who lives in your home with you. Box 12 code II shows such pay that is not in box 1.

Shown on a one-person return:

> Count only pay for caring for someone who lives in your home with you. Box 12 code II shows such pay that is not in box 1.

Shown for you on a couple's return:

> Count only pay for caring for someone who lives in your home with you. Box 12 code II shows such pay that is not in box 1.

Shown for your spouse:

> Count only pay for caring for someone who lives in your spouse's home with your spouse. Box 12 code II shows such pay that is not in box 1.

## `person.mw_not_box1`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much of that Medicaid pay is not in box 1 of a W-2? Zero if none.

Shown on a one-person return:

> How much of that Medicaid pay is not in box 1 of a W-2? Zero if none.

Shown for you on a couple's return:

> About you — How much of that Medicaid pay is not in box 1 of a W-2? Zero if none.

Shown for your spouse:

> About your spouse — How much of that Medicaid pay is not in box 1 of a W-2? Zero if none.

**Help, as stored**

> It may show only in box 12 with code II, on a Form 1099-MISC or 1099-NEC, or on no form.

Shown on a one-person return:

> It may show only in box 12 with code II, on a Form 1099-MISC or 1099-NEC, or on no form.

Shown for you on a couple's return:

> It may show only in box 12 with code II, on a Form 1099-MISC or 1099-NEC, or on no form.

Shown for your spouse:

> It may show only in box 12 with code II, on a Form 1099-MISC or 1099-NEC, or on no form.

## `person.mw_1099`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much of that was reported on a Form 1099-MISC or 1099-NEC? Zero if none.

Shown on a one-person return:

> How much of that was reported on a Form 1099-MISC or 1099-NEC? Zero if none.

Shown for you on a couple's return:

> About you — How much of that was reported on a Form 1099-MISC or 1099-NEC? Zero if none.

Shown for your spouse:

> About your spouse — How much of that was reported on a Form 1099-MISC or 1099-NEC? Zero if none.

## `person.mw_business`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Do you run a business of your own that provides home care, with this pay reported on a business schedule (Schedule C)?

Shown on a one-person return:

> Do you run a business of your own that provides home care, with this pay reported on a business schedule (Schedule C)?

Shown for you on a couple's return:

> About you — Do you run a business of your own that provides home care, with this pay reported on a business schedule (Schedule C)?

Shown for your spouse:

> About your spouse — Does your spouse run a business of your spouse's own that provides home care, with this pay reported on a business schedule (Schedule C)?

**Help, as stored**

> A Yes ends the interview here.

Shown on a one-person return:

> A Yes ends the interview here.

Shown for you on a couple's return:

> A Yes ends the interview here.

Shown for your spouse:

> A Yes ends the interview here.

## `person.mw_earned`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Do you choose to count this Medicaid pay as earned income? It is not taxed either way; counting it can raise credits such as the earned income credit.

Shown on a one-person return:

> Do you choose to count this Medicaid pay as earned income? It is not taxed either way; counting it can raise credits such as the earned income credit.

Shown for you on a couple's return:

> About you — Do you choose to count this Medicaid pay as earned income? It is not taxed either way; counting it can raise credits such as the earned income credit.

Shown for your spouse:

> About your spouse — Does your spouse choose to count this Medicaid pay as earned income? It is not taxed either way; counting it can raise credits such as the earned income credit.

**Help, as stored**

> Each spouse chooses for their own pay. Counting it can raise the earned income credit and the child tax credit; it can also lower them at higher incomes. If unsure, figure the return both ways.

Shown on a one-person return:

> Each spouse chooses for their own pay. Counting it can raise the earned income credit and the child tax credit; it can also lower them at higher incomes. If unsure, figure the return both ways.

Shown for you on a couple's return:

> Each spouse chooses for their own pay. Counting it can raise the earned income credit and the child tax credit; it can also lower them at higher incomes. If unsure, figure the return both ways.

Shown for your spouse:

> Each spouse chooses for their own pay. Counting it can raise the earned income credit and the child tax credit; it can also lower them at higher incomes. If unsure, figure the return both ways.

## `$w2`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Which employers gave you a W-2 for 2025?

Shown on a one-person return:

> Which employers gave you a W-2 for 2025?

Shown for you on a couple's return:

> About you — Which employers gave you a W-2 for 2025?

Shown for your spouse:

> About your spouse — Which employers gave your spouse a W-2 for 2025?

**Help, as stored**

> Name each employer once. If one employer gave you more than one W-2, add the boxes of those W-2s together. If you had no job with a W-2, leave the list empty.

Shown on a one-person return:

> Name each employer once. If one employer gave you more than one W-2, add the boxes of those W-2s together. If you had no job with a W-2, leave the list empty.

Shown for you on a couple's return:

> Name each employer once. If one employer gave you more than one W-2, add the boxes of those W-2s together. If you had no job with a W-2, leave the list empty.

Shown for your spouse:

> Name each employer once. If one employer gave your spouse more than one W-2, add the boxes of those W-2s together. If your spouse had no job with a W-2, leave the list empty.

## `person.tin`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Do you have a social security number, or an ITIN (the tax number the IRS gives a person who cannot get a social security number)?

Shown on a one-person return:

> Do you have a social security number, or an ITIN (the tax number the IRS gives a person who cannot get a social security number)?

Shown for you on a couple's return:

> About you — Do you have a social security number, or an ITIN (the tax number the IRS gives a person who cannot get a social security number)?

Shown for your spouse:

> About your spouse — Does your spouse have a social security number, or an ITIN (the tax number the IRS gives a person who cannot get a social security number)?

**Help, as stored**

> The number must be issued by the date the 2025 return is due, extensions included. An ITIN that has expired counts only once it has been renewed; an application to renew is not enough.

Shown on a one-person return:

> The number must be issued by the date the 2025 return is due, extensions included. An ITIN that has expired counts only once it has been renewed; an application to renew is not enough.

Shown for you on a couple's return:

> The number must be issued by the date the 2025 return is due, extensions included. An ITIN that has expired counts only once it has been renewed; an application to renew is not enough.

Shown for your spouse:

> The number must be issued by the date the 2025 return is due, extensions included. An ITIN that has expired counts only once it has been renewed; an application to renew is not enough.

## `person.itin_applied`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Have you applied, or are you applying, for an ITIN or for the renewal of your expired ITIN, by the date the 2025 return is due?

Shown on a one-person return:

> Have you applied, or are you applying, for an ITIN or for the renewal of your expired ITIN, by the date the 2025 return is due?

Shown for you on a couple's return:

> About you — Have you applied, or are you applying, for an ITIN or for the renewal of your expired ITIN, by the date the 2025 return is due?

Shown for your spouse:

> About your spouse — Has your spouse applied, or is your spouse applying, for an ITIN or for the renewal of your spouse's expired ITIN, by the date the 2025 return is due?

**Help, as stored**

> Extensions count. Answer Yes if you are applying with this return, for example by sending Form W-7 with it.

Shown on a one-person return:

> Extensions count. Answer Yes if you are applying with this return, for example by sending Form W-7 with it.

Shown for you on a couple's return:

> Extensions count. Answer Yes if you are applying with this return, for example by sending Form W-7 with it.

Shown for your spouse:

> Extensions count. Answer Yes if your spouse is applying with this return, for example by sending Form W-7 with it.

## `person.work_ssn`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Do you have a social security number that allows you to work in the United States?

Shown on a one-person return:

> Do you have a social security number that allows you to work in the United States?

Shown for you on a couple's return:

> About you — Do you have a social security number that allows you to work in the United States?

Shown for your spouse:

> About your spouse — Does your spouse have a social security number that allows your spouse to work in the United States?

**Help, as stored**

> A card that says “Not Valid for Employment” does not. A card that says “Valid for Work Only With DHS Authorization” does while the authorization is valid. The number must be issued before the 2025 return is due, extensions included.

Shown on a one-person return:

> A card that says “Not Valid for Employment” does not. A card that says “Valid for Work Only With DHS Authorization” does while the authorization is valid. The number must be issued before the 2025 return is due, extensions included.

Shown for you on a couple's return:

> A card that says “Not Valid for Employment” does not. A card that says “Valid for Work Only With DHS Authorization” does while the authorization is valid. The number must be issued before the 2025 return is due, extensions included.

Shown for your spouse:

> A card that says “Not Valid for Employment” does not. A card that says “Valid for Work Only With DHS Authorization” does while the authorization is valid. The number must be issued before the 2025 return is due, extensions included.

## `person.eic_ssn`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Do you have a social security number that counts for the earned income credit? Nearly every number does: the help says which do not, if your card says “Not Valid for Employment” or “Valid for Work Only With DHS Authorization”.

Shown on a one-person return:

> Do you have a social security number that counts for the earned income credit? Nearly every number does: the help says which do not, if your card says “Not Valid for Employment” or “Valid for Work Only With DHS Authorization”.

Shown for you on a couple's return:

> About you — Do you have a social security number that counts for the earned income credit? Nearly every number does: the help says which do not, if your card says “Not Valid for Employment” or “Valid for Work Only With DHS Authorization”.

Shown for your spouse:

> About your spouse — Does your spouse have a social security number that counts for the earned income credit? Nearly every number does: the help says which do not, if your spouse's card says “Not Valid for Employment” or “Valid for Work Only With DHS Authorization”.

**Help, as stored**

> A card that says “Not Valid for Employment” counts unless the number was issued only to get a federally funded benefit. One that says “Valid for Work Only With DHS Authorization” counts while the authorization is valid. The number must be issued by the due date of the 2025 return, extensions included.

Shown on a one-person return:

> A card that says “Not Valid for Employment” counts unless the number was issued only to get a federally funded benefit. One that says “Valid for Work Only With DHS Authorization” counts while the authorization is valid. The number must be issued by the due date of the 2025 return, extensions included.

Shown for you on a couple's return:

> A card that says “Not Valid for Employment” counts unless the number was issued only to get a federally funded benefit. One that says “Valid for Work Only With DHS Authorization” counts while the authorization is valid. The number must be issued by the due date of the 2025 return, extensions included.

Shown for your spouse:

> A card that says “Not Valid for Employment” counts unless the number was issued only to get a federally funded benefit. One that says “Valid for Work Only With DHS Authorization” counts while the authorization is valid. The number must be issued by the due date of the 2025 return, extensions included.

## `person.edu`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — In 2025, was tuition or a required fee paid for this person as a student at a college, university or trade school?

Shown on a one-person return:

> In 2025, was tuition or a required fee paid for you as a student at a college, university or trade school?

Shown for you on a couple's return:

> About you — In 2025, was tuition or a required fee paid for you as a student at a college, university or trade school?

Shown for your spouse:

> About your spouse — In 2025, was tuition or a required fee paid for your spouse as a student at a college, university or trade school?

**Help, as stored**

> The school must be one that can take part in federal student aid; nearly every accredited college, university and trade school is. Answer Yes also if the only cost was books, supplies or equipment needed for a course.

Shown on a one-person return:

> The school must be one that can take part in federal student aid; nearly every accredited college, university and trade school is. Answer Yes also if the only cost was books, supplies or equipment needed for a course.

Shown for you on a couple's return:

> The school must be one that can take part in federal student aid; nearly every accredited college, university and trade school is. Answer Yes also if the only cost was books, supplies or equipment needed for a course.

Shown for your spouse:

> The school must be one that can take part in federal student aid; nearly every accredited college, university and trade school is. Answer Yes also if the only cost was books, supplies or equipment needed for a course.

## `person.edu_1098t`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did the school send this person a Form 1098-T (Tuition Statement) for 2025?

Shown on a one-person return:

> Did the school send you a Form 1098-T (Tuition Statement) for 2025?

Shown for you on a couple's return:

> About you — Did the school send you a Form 1098-T (Tuition Statement) for 2025?

Shown for your spouse:

> About your spouse — Did the school send your spouse a Form 1098-T (Tuition Statement) for 2025?

**Help, as stored**

> Answer Yes also, if the enrollment and the payments can be shown, when the school did not have to send one (for example, scholarships paid everything, or the courses gave no academic credit), or when it was asked for after February 2, 2026 and the school was given what it needed to prepare it.

Shown on a one-person return:

> Answer Yes also, if the enrollment and the payments can be shown, when the school did not have to send one (for example, scholarships paid everything, or the courses gave no academic credit), or when it was asked for after February 2, 2026 and the school was given what it needed to prepare it.

Shown for you on a couple's return:

> Answer Yes also, if the enrollment and the payments can be shown, when the school did not have to send one (for example, scholarships paid everything, or the courses gave no academic credit), or when it was asked for after February 2, 2026 and the school was given what it needed to prepare it.

Shown for your spouse:

> Answer Yes also, if the enrollment and the payments can be shown, when the school did not have to send one (for example, scholarships paid everything, or the courses gave no academic credit), or when it was asked for after February 2, 2026 and the school was given what it needed to prepare it.

## `person.edu_inst`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much was paid to the school in 2025 for this person's tuition and required fees? (Form 1098-T box 1 shows what the school received.)

Shown on a one-person return:

> How much was paid to the school in 2025 for your tuition and required fees? (Form 1098-T box 1 shows what the school received.)

Shown for you on a couple's return:

> About you — How much was paid to the school in 2025 for your tuition and required fees? (Form 1098-T box 1 shows what the school received.)

Shown for your spouse:

> About your spouse — How much was paid to the school in 2025 for your spouse's tuition and required fees? (Form 1098-T box 1 shows what the school received.)

**Help, as stored**

> Use what was actually paid, by anyone, for terms that began in 2025 or in January to March 2026. Required fees include student activity, athletic or lab fees every student must pay the school. Books, supplies and equipment count here only if they had to be bought from the school.
>
> Leave out:
> - room and board, insurance, medical costs (student health fees too) and transportation
> - amounts paid with a tax-free withdrawal from a 529 plan or a Coverdell account
> - amounts deducted elsewhere on this return
> - courses in sports, games or hobbies, and courses without credit, unless they are part of the degree program (or, for a student who cannot get the American opportunity credit, they improve job skills)

Shown on a one-person return:

> Use what was actually paid, by anyone, for terms that began in 2025 or in January to March 2026. Required fees include student activity, athletic or lab fees every student must pay the school. Books, supplies and equipment count here only if they had to be bought from the school.
>
> Leave out:
> - room and board, insurance, medical costs (student health fees too) and transportation
> - amounts paid with a tax-free withdrawal from a 529 plan or a Coverdell account
> - amounts deducted elsewhere on this return
> - courses in sports, games or hobbies, and courses without credit, unless they are part of the degree program (or, for a student who cannot get the American opportunity credit, they improve job skills)

Shown for you on a couple's return:

> Use what was actually paid, by anyone, for terms that began in 2025 or in January to March 2026. Required fees include student activity, athletic or lab fees every student must pay the school. Books, supplies and equipment count here only if they had to be bought from the school.
>
> Leave out:
> - room and board, insurance, medical costs (student health fees too) and transportation
> - amounts paid with a tax-free withdrawal from a 529 plan or a Coverdell account
> - amounts deducted elsewhere on this return
> - courses in sports, games or hobbies, and courses without credit, unless they are part of the degree program (or, for a student who cannot get the American opportunity credit, they improve job skills)

Shown for your spouse:

> Use what was actually paid, by anyone, for terms that began in 2025 or in January to March 2026. Required fees include student activity, athletic or lab fees every student must pay the school. Books, supplies and equipment count here only if they had to be bought from the school.
>
> Leave out:
> - room and board, insurance, medical costs (student health fees too) and transportation
> - amounts paid with a tax-free withdrawal from a 529 plan or a Coverdell account
> - amounts deducted elsewhere on this return
> - courses in sports, games or hobbies, and courses without credit, unless they are part of the degree program (or, for a student who cannot get the American opportunity credit, they improve job skills)

## `person.edu_mat`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much was spent in 2025 on books, supplies and equipment needed for this person's courses, bought anywhere but from the school?

Shown on a one-person return:

> How much was spent in 2025 on books, supplies and equipment needed for your courses, bought anywhere but from the school?

Shown for you on a couple's return:

> About you — How much was spent in 2025 on books, supplies and equipment needed for your courses, bought anywhere but from the school?

Shown for your spouse:

> About your spouse — How much was spent in 2025 on books, supplies and equipment needed for your spouse's courses, bought anywhere but from the school?

**Help, as stored**

> Count only what was paid in 2025. Leave out anything paid with a tax-free 529 plan or Coverdell withdrawal or deducted elsewhere on this return, and materials for a sports, games, hobby or noncredit course outside the degree program.

Shown on a one-person return:

> Count only what was paid in 2025. Leave out anything paid with a tax-free 529 plan or Coverdell withdrawal or deducted elsewhere on this return, and materials for a sports, games, hobby or noncredit course outside the degree program.

Shown for you on a couple's return:

> Count only what was paid in 2025. Leave out anything paid with a tax-free 529 plan or Coverdell withdrawal or deducted elsewhere on this return, and materials for a sports, games, hobby or noncredit course outside the degree program.

Shown for your spouse:

> Count only what was paid in 2025. Leave out anything paid with a tax-free 529 plan or Coverdell withdrawal or deducted elsewhere on this return, and materials for a sports, games, hobby or noncredit course outside the degree program.

## `person.edu_a_this_year`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much tax-free help with these school costs came in during 2025: scholarships and grants (Form 1098-T box 5), an employer's tuition assistance, veterans' education benefits?

Shown on a one-person return:

> How much tax-free help with these school costs came in during 2025: scholarships and grants (Form 1098-T box 5), an employer's tuition assistance, veterans' education benefits?

Shown for you on a couple's return:

> About you — How much tax-free help with these school costs came in during 2025: scholarships and grants (Form 1098-T box 5), an employer's tuition assistance, veterans' education benefits?

Shown for your spouse:

> About your spouse — How much tax-free help with these school costs came in during 2025: scholarships and grants (Form 1098-T box 5), an employer's tuition assistance, veterans' education benefits?

**Help, as stored**

> Count help for the terms of the costs just entered, and only the tax-free part; a Pell grant is a grant. Leave out loans, gifts, savings, wages, emergency aid grants, and a scholarship reported as income (allowed only for one whose terms let it pay for room and board or other costs).

Shown on a one-person return:

> Count help for the terms of the costs just entered, and only the tax-free part; a Pell grant is a grant. Leave out loans, gifts, savings, wages, emergency aid grants, and a scholarship reported as income (allowed only for one whose terms let it pay for room and board or other costs).

Shown for you on a couple's return:

> Count help for the terms of the costs just entered, and only the tax-free part; a Pell grant is a grant. Leave out loans, gifts, savings, wages, emergency aid grants, and a scholarship reported as income (allowed only for one whose terms let it pay for room and board or other costs).

Shown for your spouse:

> Count help for the terms of the costs just entered, and only the tax-free part; a Pell grant is a grant. Leave out loans, gifts, savings, wages, emergency aid grants, and a scholarship reported as income (allowed only for one whose terms let it pay for room and board or other costs).

## `person.edu_a_next_year`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much more of that tax-free help has come in during 2026, so far, for the same school terms?

Shown on a one-person return:

> How much more of that tax-free help has come in during 2026, so far, for the same school terms?

Shown for you on a couple's return:

> About you — How much more of that tax-free help has come in during 2026, so far, for the same school terms?

Shown for your spouse:

> About your spouse — How much more of that tax-free help has come in during 2026, so far, for the same school terms?

## `person.edu_refunds`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much of the tuition and fees paid in 2025 has the school refunded, in 2025 or so far in 2026?

Shown on a one-person return:

> How much of the tuition and fees paid in 2025 has the school refunded, in 2025 or so far in 2026?

Shown for you on a couple's return:

> About you — How much of the tuition and fees paid in 2025 has the school refunded, in 2025 or so far in 2026?

Shown for your spouse:

> About your spouse — How much of the tuition and fees paid in 2025 has the school refunded, in 2025 or so far in 2026?

## `person.edu_line23`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Has the American opportunity credit already been claimed for this person, by anyone, in four tax years before 2025?

Shown on a one-person return:

> Has the American opportunity credit already been claimed for you, by anyone, in four tax years before 2025?

Shown for you on a couple's return:

> About you — Has the American opportunity credit already been claimed for you, by anyone, in four tax years before 2025?

Shown for your spouse:

> About your spouse — Has the American opportunity credit already been claimed for your spouse, by anyone, in four tax years before 2025?

**Help, as stored**

> It is the main tax credit for the first four years of college. For a student who first went to college in 2022 or later, the answer is No.

Shown on a one-person return:

> It is the main tax credit for the first four years of college. For a student who first went to college in 2022 or later, the answer is No.

Shown for you on a couple's return:

> It is the main tax credit for the first four years of college. For a student who first went to college in 2022 or later, the answer is No.

Shown for your spouse:

> It is the main tax credit for the first four years of college. For a student who first went to college in 2022 or later, the answer is No.

## `person.edu_line24`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — For at least one term that began in 2025, was this person's enrollment at least half-time, in a program leading to a degree or certificate? (Form 1098-T box 8 is checked if so.)

Shown on a one-person return:

> For at least one term that began in 2025, was your enrollment at least half-time, in a program leading to a degree or certificate? (Form 1098-T box 8 is checked if so.)

Shown for you on a couple's return:

> About you — For at least one term that began in 2025, was your enrollment at least half-time, in a program leading to a degree or certificate? (Form 1098-T box 8 is checked if so.)

Shown for your spouse:

> About your spouse — For at least one term that began in 2025, was your spouse's enrollment at least half-time, in a program leading to a degree or certificate? (Form 1098-T box 8 is checked if so.)

**Help, as stored**

> A term that began in January to March 2026 also counts if it was paid for in 2025.

Shown on a one-person return:

> A term that began in January to March 2026 also counts if it was paid for in 2025.

Shown for you on a couple's return:

> A term that began in January to March 2026 also counts if it was paid for in 2025.

Shown for your spouse:

> A term that began in January to March 2026 also counts if it was paid for in 2025.

## `person.edu_line25`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were this person's first four years of college already complete before 2025 began, by the school's count of academic credit?

Shown on a one-person return:

> Were your first four years of college already complete before 2025 began, by the school's count of academic credit?

Shown for you on a couple's return:

> About you — Were your first four years of college already complete before 2025 began, by the school's count of academic credit?

Shown for your spouse:

> About your spouse — Were your spouse's first four years of college already complete before 2025 began, by the school's count of academic credit?

**Help, as stored**

> Credit awarded only for passing proficiency examinations is not counted.

Shown on a one-person return:

> Credit awarded only for passing proficiency examinations is not counted.

Shown for you on a couple's return:

> Credit awarded only for passing proficiency examinations is not counted.

Shown for your spouse:

> Credit awarded only for passing proficiency examinations is not counted.

## `person.edu_line26`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — By the end of 2025, was there a federal or state felony conviction of this person for possessing or distributing a controlled substance (illegal drugs)?

Shown on a one-person return:

> By the end of 2025, was there a federal or state felony conviction of you for possessing or distributing a controlled substance (illegal drugs)?

Shown for you on a couple's return:

> About you — By the end of 2025, was there a federal or state felony conviction of you for possessing or distributing a controlled substance (illegal drugs)?

Shown for your spouse:

> About your spouse — By the end of 2025, was there a federal or state felony conviction of your spouse for possessing or distributing a controlled substance (illegal drugs)?

## `person.edu_ein`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Is the school's employer identification number (EIN) at hand? Form 1098-T shows it, and the school can give it.

Shown on a one-person return:

> Is the school's employer identification number (EIN) at hand? Form 1098-T shows it, and the school can give it.

Shown for you on a couple's return:

> About you — Is the school's employer identification number (EIN) at hand? Form 1098-T shows it, and the school can give it.

Shown for your spouse:

> About your spouse — Is the school's employer identification number (EIN) at hand? Form 1098-T shows it, and the school can give it.

## `person.edu_over`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Was there a school term for which the tax-free help and the refunds came to more than what was paid in 2025 for that term's tuition, required fees and course materials (for the lifetime learning credit, only materials that had to be bought from the school)?

Shown on a one-person return:

> Was there a school term for which the tax-free help and the refunds came to more than what was paid in 2025 for that term's tuition, required fees and course materials (for the lifetime learning credit, only materials that had to be bought from the school)?

Shown for you on a couple's return:

> About you — Was there a school term for which the tax-free help and the refunds came to more than what was paid in 2025 for that term's tuition, required fees and course materials (for the lifetime learning credit, only materials that had to be bought from the school)?

Shown for your spouse:

> About your spouse — Was there a school term for which the tax-free help and the refunds came to more than what was paid in 2025 for that term's tuition, required fees and course materials (for the lifetime learning credit, only materials that had to be bought from the school)?

**Help, as stored**

> A term beginning January to March 2026 and paid for in 2025 counts as a 2025 term. With only one such term, answer by that term alone. Count help and refunds received in 2025 or in 2026 before you file. A Yes ends the interview here.

Shown on a one-person return:

> A term beginning January to March 2026 and paid for in 2025 counts as a 2025 term. With only one such term, answer by that term alone. Count help and refunds received in 2025 or in 2026 before you file. A Yes ends the interview here.

Shown for you on a couple's return:

> A term beginning January to March 2026 and paid for in 2025 counts as a 2025 term. With only one such term, answer by that term alone. Count help and refunds received in 2025 or in 2026 before you file. A Yes ends the interview here.

Shown for your spouse:

> A term beginning January to March 2026 and paid for in 2025 counts as a 2025 term. With only one such term, answer by that term alone. Count help and refunds received in 2025 or in 2026 before your spouse files. A Yes ends the interview here.

## `person.edu_fulltime`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you a full-time student during some part of at least five months of 2025?

Shown on a one-person return:

> Were you a full-time student during some part of at least five months of 2025?

Shown for you on a couple's return:

> About you — Were you a full-time student during some part of at least five months of 2025?

Shown for your spouse:

> About your spouse — Was your spouse a full-time student during some part of at least five months of 2025?

**Help, as stored**

> At a college, university or trade school. A full-time on-farm training course given by such a school or by a state, county or local government agency also counts. The months need not be in a row.

Shown on a one-person return:

> At a college, university or trade school. A full-time on-farm training course given by such a school or by a state, county or local government agency also counts. The months need not be in a row.

Shown for you on a couple's return:

> At a college, university or trade school. A full-time on-farm training course given by such a school or by a state, county or local government agency also counts. The months need not be in a row.

Shown for your spouse:

> At a college, university or trade school. A full-time on-farm training course given by such a school or by a state, county or local government agency also counts. The months need not be in a row.

## `person.edu_half_support`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — In 2025, was your pay from work less than half of your support, meaning what your food, housing, clothing, medical care, education and the like cost?

Shown on a one-person return:

> In 2025, was your pay from work less than half of your support, meaning what your food, housing, clothing, medical care, education and the like cost?

Shown for you on a couple's return:

> About you — In 2025, was your pay from work less than half of your support, meaning what your food, housing, clothing, medical care, education and the like cost?

Shown for your spouse:

> About your spouse — In 2025, was your spouse's pay from work less than half of your spouse's support, meaning what your spouse's food, housing, clothing, medical care, education and the like cost?

**Help, as stored**

> Pay from work is wages, salaries, fees and other pay for services, including the part of a scholarship paid for teaching or research. Support counts whoever paid for it, housing given at its rental value; a scholarship is not support for a full-time student.

Shown on a one-person return:

> Pay from work is wages, salaries, fees and other pay for services, including the part of a scholarship paid for teaching or research. Support counts whoever paid for it, housing given at its rental value; a scholarship is not support for a full-time student.

Shown for you on a couple's return:

> Pay from work is wages, salaries, fees and other pay for services, including the part of a scholarship paid for teaching or research. Support counts whoever paid for it, housing given at its rental value; a scholarship is not support for a full-time student.

Shown for your spouse:

> Pay from work is wages, salaries, fees and other pay for services, including the part of a scholarship paid for teaching or research. Support counts whoever paid for it, housing given at its rental value; a scholarship is not support for a full-time student.

## `person.edu_parent`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Was at least one of your parents alive at the end of 2025?

Shown on a one-person return:

> Was at least one of your parents alive at the end of 2025?

Shown for you on a couple's return:

> About you — Was at least one of your parents alive at the end of 2025?

Shown for your spouse:

> About your spouse — Was at least one of your spouse's parents alive at the end of 2025?

## `person.x_hsa_prior_excess`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Before 2025, was more put into your HSA than the limit for the year, with some of the extra still in the account at the start of 2025?

Shown on a one-person return:

> Before 2025, was more put into your HSA than the limit for the year, with some of the extra still in the account at the start of 2025?

Shown for you on a couple's return:

> About you — Before 2025, was more put into your HSA than the limit for the year, with some of the extra still in the account at the start of 2025?

Shown for your spouse:

> About your spouse — Before 2025, was more put into your spouse's HSA than the limit for the year, with some of the extra still in the account at the start of 2025?

**Help, as stored**

> Answer Yes if your 2024 Form 5329 has an amount on line 48, or if you never reported the excess. A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown on a one-person return:

> Answer Yes if your 2024 Form 5329 has an amount on line 48, or if you never reported the excess. A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown for you on a couple's return:

> Answer Yes if your 2024 Form 5329 has an amount on line 48, or if you never reported the excess. A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown for your spouse:

> Answer Yes if your spouse's 2024 Form 5329 has an amount on line 48, or if your spouse never reported the excess. A return with this is outside what this tool prepares; a Yes ends the interview here.

## `person.x_archer_excess`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Does an Archer MSA of yours (an older kind of medical savings account) still hold money that was put in above its limit in a year before 2025?

Shown on a one-person return:

> Does an Archer MSA of yours (an older kind of medical savings account) still hold money that was put in above its limit in a year before 2025?

Shown for you on a couple's return:

> About you — Does an Archer MSA of yours (an older kind of medical savings account) still hold money that was put in above its limit in a year before 2025?

Shown for your spouse:

> About your spouse — Does an Archer MSA of your spouse's (an older kind of medical savings account) still hold money that was put in above its limit in a year before 2025?

**Help, as stored**

> A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown on a one-person return:

> A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown for you on a couple's return:

> A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown for your spouse:

> A return with this is outside what this tool prepares; a Yes ends the interview here.

## `person.x_edu_account`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — At any time in 2025, did you have a 529 plan, a Coverdell education savings account or an ABLE account, or was one held for you?

Shown on a one-person return:

> At any time in 2025, did you have a 529 plan, a Coverdell education savings account or an ABLE account, or was one held for you?

Shown for you on a couple's return:

> About you — At any time in 2025, did you have a 529 plan, a Coverdell education savings account or an ABLE account, or was one held for you?

Shown for your spouse:

> About your spouse — At any time in 2025, did your spouse have a 529 plan, a Coverdell education savings account or an ABLE account, or was one held for your spouse?

**Help, as stored**

> Answer Yes whether the account is yours or is held for you, and for money put into a Coverdell for 2025 by April 15, 2026. A Form 1099-Q or Form 1099-QA sent to you for 2025 means Yes.

Shown on a one-person return:

> Answer Yes whether the account is yours or is held for you, and for money put into a Coverdell for 2025 by April 15, 2026. A Form 1099-Q or Form 1099-QA sent to you for 2025 means Yes.

Shown for you on a couple's return:

> Answer Yes whether the account is yours or is held for you, and for money put into a Coverdell for 2025 by April 15, 2026. A Form 1099-Q or Form 1099-QA sent to you for 2025 means Yes.

Shown for your spouse:

> Answer Yes whether the account is your spouse's or is held for your spouse, and for money put into a Coverdell for 2025 by April 15, 2026. A Form 1099-Q or Form 1099-QA sent to your spouse for 2025 means Yes.

## `person.x_edu_taxable`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Was any money that came out of the account in 2025 taxable: more than the education costs, or for an ABLE account the disability costs, that it paid for?

Shown on a one-person return:

> Was any money that came out of the account in 2025 taxable: more than the education costs, or for an ABLE account the disability costs, that it paid for?

Shown for you on a couple's return:

> About you — Was any money that came out of the account in 2025 taxable: more than the education costs, or for an ABLE account the disability costs, that it paid for?

Shown for your spouse:

> About your spouse — Was any money that came out of the account in 2025 taxable: more than the education costs, or for an ABLE account the disability costs, that it paid for?

**Help, as stored**

> Costs also used for an education credit, or paid by a tax-free scholarship, do not count as costs it paid. A Coverdell left at age 30 or at death counts as paid out. A Yes ends the interview here.

Shown on a one-person return:

> Costs also used for an education credit, or paid by a tax-free scholarship, do not count as costs it paid. A Coverdell left at age 30 or at death counts as paid out. A Yes ends the interview here.

Shown for you on a couple's return:

> Costs also used for an education credit, or paid by a tax-free scholarship, do not count as costs it paid. A Coverdell left at age 30 or at death counts as paid out. A Yes ends the interview here.

Shown for your spouse:

> Costs also used for an education credit, or paid by a tax-free scholarship, do not count as costs it paid. A Coverdell left at age 30 or at death counts as paid out. A Yes ends the interview here.

## `person.x_edu_excess`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Was more than the yearly limit put into a Coverdell education savings account or an ABLE account held for you, and is the extra still in the account?

Shown on a one-person return:

> Was more than the yearly limit put into a Coverdell education savings account or an ABLE account held for you, and is the extra still in the account?

Shown for you on a couple's return:

> About you — Was more than the yearly limit put into a Coverdell education savings account or an ABLE account held for you, and is the extra still in the account?

Shown for your spouse:

> About your spouse — Was more than the yearly limit put into a Coverdell education savings account or an ABLE account held for your spouse, and is the extra still in the account?

**Help, as stored**

> This includes an excess from an earlier year. A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown on a one-person return:

> This includes an excess from an earlier year. A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown for you on a couple's return:

> This includes an excess from an earlier year. A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown for your spouse:

> This includes an excess from an earlier year. A return with this is outside what this tool prepares; a Yes ends the interview here.

## `person.x_prior09`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Total of your earlier IRA distributions (before 2025) for which the first-home exception was used; zero if none

Shown on a one-person return:

> Total of your earlier IRA distributions (before 2025) for which the first-home exception was used; zero if none

Shown for you on a couple's return:

> About you — Total of your earlier IRA distributions (before 2025) for which the first-home exception was used; zero if none

Shown for your spouse:

> About your spouse — Total of your spouse's earlier IRA distributions (before 2025) for which the first-home exception was used; zero if none

## `person.x_births`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — For how many births or adoptions (children born or adopted, each counted once) did you take the 2025 birth or adoption distributions? Count only a child for whom a 2025 distribution was taken within 1 year of the birth or of the date the adoption became final.

Shown on a one-person return:

> For how many births or adoptions (children born or adopted, each counted once) did you take the 2025 birth or adoption distributions? Count only a child for whom a 2025 distribution was taken within 1 year of the birth or of the date the adoption became final.

Shown for you on a couple's return:

> About you — For how many births or adoptions (children born or adopted, each counted once) did you take the 2025 birth or adoption distributions? Count only a child for whom a 2025 distribution was taken within 1 year of the birth or of the date the adoption became final.

Shown for your spouse:

> About your spouse — For how many births or adoptions (children born or adopted, each counted once) did your spouse take the 2025 birth or adoption distributions? Count only a child for whom a 2025 distribution was taken within 1 year of the birth or of the date the adoption became final.

## `person.inherited_account`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Have you inherited an IRA or a workplace retirement account, such as a 401(k), from someone who died?

Shown on a one-person return:

> Have you inherited an IRA or a workplace retirement account, such as a 401(k), from someone who died?

Shown for you on a couple's return:

> About you — Have you inherited an IRA or a workplace retirement account, such as a 401(k), from someone who died?

Shown for your spouse:

> About your spouse — Has your spouse inherited an IRA or a workplace retirement account, such as a 401(k), from someone who died?

**Help, as stored**

> It counts even if the money is still in the account.

Shown on a one-person return:

> It counts even if the money is still in the account.

Shown for you on a couple's return:

> It counts even if the money is still in the account.

Shown for your spouse:

> It counts even if the money is still in the account.

## `person.rmd_missed`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you take less than the required amount out of a retirement account by a 2025 deadline, even if you made up the shortfall later?

Shown on a one-person return:

> Did you take less than the required amount out of a retirement account by a 2025 deadline, even if you made up the shortfall later?

Shown for you on a couple's return:

> About you — Did you take less than the required amount out of a retirement account by a 2025 deadline, even if you made up the shortfall later?

Shown for your spouse:

> About your spouse — Did your spouse take less than the required amount out of a retirement account by a 2025 deadline, even if your spouse made up the shortfall later?

**Help, as stored**

> This includes a yearly minimum (at 73 or older, or on an inherited account), a first amount due April 1, 2025, and emptying an inherited account by its deadline. A Yes ends the interview here.

Shown on a one-person return:

> This includes a yearly minimum (at 73 or older, or on an inherited account), a first amount due April 1, 2025, and emptying an inherited account by its deadline. A Yes ends the interview here.

Shown for you on a couple's return:

> This includes a yearly minimum (at 73 or older, or on an inherited account), a first amount due April 1, 2025, and emptying an inherited account by its deadline. A Yes ends the interview here.

Shown for your spouse:

> This includes a yearly minimum (at 73 or older, or on an inherited account), a first amount due April 1, 2025, and emptying an inherited account by its deadline. A Yes ends the interview here.

## `$retirement`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — In 2025, did you take money from a pension, an annuity, a 401(k) or an IRA? List each Form 1099-R you received (for example by payer), or leave the list empty.

Shown on a one-person return:

> In 2025, did you take money from a pension, an annuity, a 401(k) or an IRA? List each Form 1099-R you received (for example by payer), or leave the list empty.

Shown for you on a couple's return:

> About you — In 2025, did you take money from a pension, an annuity, a 401(k) or an IRA? List each Form 1099-R you received (for example by payer), or leave the list empty.

Shown for your spouse:

> About your spouse — In 2025, did your spouse take money from a pension, an annuity, a 401(k) or an IRA? List each Form 1099-R your spouse received (for example by payer), or leave the list empty.

**Help, as stored**

> List a Form RRB-1099-R too. Do not list a Form SSA-1099 or RRB-1099 (social security benefits); they are asked about separately.

Shown on a one-person return:

> List a Form RRB-1099-R too. Do not list a Form SSA-1099 or RRB-1099 (social security benefits); they are asked about separately.

Shown for you on a couple's return:

> List a Form RRB-1099-R too. Do not list a Form SSA-1099 or RRB-1099 (social security benefits); they are asked about separately.

Shown for your spouse:

> List a Form RRB-1099-R too. Do not list a Form SSA-1099 or RRB-1099 (social security benefits); they are asked about separately.

## `person.educator_expenses`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much did you spend in 2025 on books, supplies, equipment, software and other materials for the classroom, and on courses for your teaching?

Shown on a one-person return:

> How much did you spend in 2025 on books, supplies, equipment, software and other materials for the classroom, and on courses for your teaching?

Shown for you on a couple's return:

> About you — How much did you spend in 2025 on books, supplies, equipment, software and other materials for the classroom, and on courses for your teaching?

Shown for your spouse:

> About your spouse — How much did your spouse spend in 2025 on books, supplies, equipment, software and other materials for the classroom, and on courses for your spouse's teaching?

**Help, as stored**

> Count only costs that nobody repaid. Leave out home schooling costs, and supplies for health or physical education courses that are not for athletics. Subtract any tax-free savings bond interest, 529 plan or Coverdell money that paid for them.

Shown on a one-person return:

> Count only costs that nobody repaid. Leave out home schooling costs, and supplies for health or physical education courses that are not for athletics. Subtract any tax-free savings bond interest, 529 plan or Coverdell money that paid for them.

Shown for you on a couple's return:

> Count only costs that nobody repaid. Leave out home schooling costs, and supplies for health or physical education courses that are not for athletics. Subtract any tax-free savings bond interest, 529 plan or Coverdell money that paid for them.

Shown for your spouse:

> Count only costs that nobody repaid. Leave out home schooling costs, and supplies for health or physical education courses that are not for athletics. Subtract any tax-free savings bond interest, 529 plan or Coverdell money that paid for them.

## `person.eligible_educator`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — In 2025, did you work in a school, from kindergarten through grade 12, as a teacher, instructor, counselor, principal or aide, for at least 900 hours during a school year?

Shown on a one-person return:

> In 2025, did you work in a school, from kindergarten through grade 12, as a teacher, instructor, counselor, principal or aide, for at least 900 hours during a school year?

Shown for you on a couple's return:

> About you — In 2025, did you work in a school, from kindergarten through grade 12, as a teacher, instructor, counselor, principal or aide, for at least 900 hours during a school year?

Shown for your spouse:

> About your spouse — In 2025, did your spouse work in a school, from kindergarten through grade 12, as a teacher, instructor, counselor, principal or aide, for at least 900 hours during a school year?

**Help, as stored**

> Count the hours of a whole school year that falls partly in 2025 (2024-25 or 2025-26), not only those in 2025, at all your K-12 schools together.

Shown on a one-person return:

> Count the hours of a whole school year that falls partly in 2025 (2024-25 or 2025-26), not only those in 2025, at all your K-12 schools together.

Shown for you on a couple's return:

> Count the hours of a whole school year that falls partly in 2025 (2024-25 or 2025-26), not only those in 2025, at all your K-12 schools together.

Shown for your spouse:

> Count the hours of a whole school year that falls partly in 2025 (2024-25 or 2025-26), not only those in 2025, at all your spouse's K-12 schools together.

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

> Signs of one: the letter W in box 12 of your Form W-2, or a Form 5498-SA or 1099-SA from the account's bank. Answer Yes even if nothing went in or out in 2025, or if it came from someone who died. A flexible spending account (FSA) is not an HSA.

Shown on a one-person return:

> Signs of one: the letter W in box 12 of your Form W-2, or a Form 5498-SA or 1099-SA from the account's bank. Answer Yes even if nothing went in or out in 2025, or if it came from someone who died. A flexible spending account (FSA) is not an HSA.

Shown for you on a couple's return:

> Signs of one: the letter W in box 12 of your Form W-2, or a Form 5498-SA or 1099-SA from the account's bank. Answer Yes even if nothing went in or out in 2025, or if it came from someone who died. A flexible spending account (FSA) is not an HSA.

Shown for your spouse:

> Signs of one: the letter W in box 12 of your spouse's Form W-2, or a Form 5498-SA or 1099-SA from the account's bank. Answer Yes even if nothing went in or out in 2025, or if it came from someone who died. A flexible spending account (FSA) is not an HSA.

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

## `f8889.inherited_any`

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

## `f8889.inherited_case`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Whose HSA was it, and when did they die?

Shown on a one-person return:

> Whose HSA was it, and when did they die?

Shown for you on a couple's return:

> About you — Whose HSA was it, and when did they die?

Shown for your spouse:

> About your spouse — Whose HSA was it, and when did they die?

**Help, as stored**

> An HSA left by a husband or wife now counts as your own, so include it in the answers that follow. Anyone else's HSA stopped being an HSA when they died.

Shown on a one-person return:

> An HSA left by a husband or wife now counts as your own, so include it in the answers that follow. Anyone else's HSA stopped being an HSA when they died.

Shown for you on a couple's return:

> An HSA left by a husband or wife now counts as your own, so include it in the answers that follow. Anyone else's HSA stopped being an HSA when they died.

Shown for your spouse:

> An HSA left by a husband or wife now counts as your spouse's own, so include it in the answers that follow. Anyone else's HSA stopped being an HSA when they died.

## `f8889.archer`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — For 2025, was money put into an Archer MSA of yours or your spouse's, or did money come out of one of yours?

Shown on a one-person return:

> For 2025, was money put into an Archer MSA of yours or your spouse's, or did money come out of one of yours?

Shown for you on a couple's return:

> About you — For 2025, was money put into an Archer MSA of yours or your spouse's, or did money come out of one of yours?

Shown for your spouse:

> About your spouse — For 2025, was money put into an Archer MSA of yours or your spouse's, or did money come out of one of your spouse's?

**Help, as stored**

> An Archer MSA is an older kind of medical savings account; on a Form 1099-SA (box 5) or Form 5498-SA (box 6) for one, the box “Archer MSA” is checked. Count money put in for 2025 after the year ended, money moved from one into an HSA, and an Archer MSA that came to you in 2025 because its owner died. If you have never heard of it, the answer is No.

Shown on a one-person return:

> An Archer MSA is an older kind of medical savings account; on a Form 1099-SA (box 5) or Form 5498-SA (box 6) for one, the box “Archer MSA” is checked. Count money put in for 2025 after the year ended, money moved from one into an HSA, and an Archer MSA that came to you in 2025 because its owner died. If you have never heard of it, the answer is No.

Shown for you on a couple's return:

> An Archer MSA is an older kind of medical savings account; on a Form 1099-SA (box 5) or Form 5498-SA (box 6) for one, the box “Archer MSA” is checked. Count money put in for 2025 after the year ended, money moved from one into an HSA, and an Archer MSA that came to you in 2025 because its owner died. If you have never heard of it, the answer is No.

Shown for your spouse:

> An Archer MSA is an older kind of medical savings account; on a Form 1099-SA (box 5) or Form 5498-SA (box 6) for one, the box “Archer MSA” is checked. Count money put in for 2025 after the year ended, money moved from one into an HSA, and an Archer MSA that came to your spouse in 2025 because its owner died. If your spouse has never heard of it, the answer is No.

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

> Use the amount in box 12 of your Form W-2 next to the letter W, which includes money a health insurer put in for your employer. Take off any part of it that was for 2024, and add anything your employer put in for 2025 after December 31, 2025. Zero if none.

Shown on a one-person return:

> Use the amount in box 12 of your Form W-2 next to the letter W, which includes money a health insurer put in for your employer. Take off any part of it that was for 2024, and add anything your employer put in for 2025 after December 31, 2025. Zero if none.

Shown for you on a couple's return:

> Use the amount in box 12 of your Form W-2 next to the letter W, which includes money a health insurer put in for your employer. Take off any part of it that was for 2024, and add anything your employer put in for 2025 after December 31, 2025. Zero if none.

Shown for your spouse:

> Use the amount in box 12 of your spouse's Form W-2 next to the letter W, which includes money a health insurer put in for your spouse's employer. Take off any part of it that was for 2024, and add anything your spouse's employer put in for 2025 after December 31, 2025. Zero if none.

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

> Count deposits by you, or by anyone other than your employer, that were for 2025, made up to April 15, 2026 (later if you served in a combat zone). Box 12 of your Form W-2 shows, next to the letter W, what your employer put in and what was taken out of your pay before tax; leave that out, and leave out pre-tax money taken from your pay in early 2026 for 2025 (it belongs in the question before). Money taken out of your pay after tax counts here. Do not count money moved in from another HSA, an Archer MSA or an IRA. Only money can be put in, not stock or other property. Zero if none.

Shown on a one-person return:

> Count deposits by you, or by anyone other than your employer, that were for 2025, made up to April 15, 2026 (later if you served in a combat zone). Box 12 of your Form W-2 shows, next to the letter W, what your employer put in and what was taken out of your pay before tax; leave that out, and leave out pre-tax money taken from your pay in early 2026 for 2025 (it belongs in the question before). Money taken out of your pay after tax counts here. Do not count money moved in from another HSA, an Archer MSA or an IRA. Only money can be put in, not stock or other property. Zero if none.

Shown for you on a couple's return:

> Count deposits by you, or by anyone other than your employer, that were for 2025, made up to April 15, 2026 (later if you served in a combat zone). Box 12 of your Form W-2 shows, next to the letter W, what your employer put in and what was taken out of your pay before tax; leave that out, and leave out pre-tax money taken from your pay in early 2026 for 2025 (it belongs in the question before). Money taken out of your pay after tax counts here. Do not count money moved in from another HSA, an Archer MSA or an IRA. Only money can be put in, not stock or other property. Zero if none.

Shown for your spouse:

> Count deposits by your spouse, or by anyone other than your spouse's employer, that were for 2025, made up to April 15, 2026 (later if your spouse served in a combat zone). Box 12 of your spouse's Form W-2 shows, next to the letter W, what your spouse's employer put in and what was taken out of your spouse's pay before tax; leave that out, and leave out pre-tax money taken from your spouse's pay in early 2026 for 2025 (it belongs in the question before). Money taken out of your spouse's pay after tax counts here. Do not count money moved in from another HSA, an Archer MSA or an IRA. Only money can be put in, not stock or other property. Zero if none.

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

> What counts is the plan you had on the first day of each month; plan papers usually call such a plan “HSA-eligible” or “HDHP”. If you were covered all year as a member of someone else's plan (a parent's, or your spouse's), or by a plan for only you and a family plan at once, choose “covering more than one person”; if that was so for only part of the year, choose “No”. A change of insurer with no gap and the same kind of plan is not a change. A plan covering more than one person does not count if its deductible for any one person on it is below $3,300.

Shown on a one-person return:

> What counts is the plan you had on the first day of each month; plan papers usually call such a plan “HSA-eligible” or “HDHP”. If you were covered all year as a member of someone else's plan (a parent's, or your spouse's), or by a plan for only you and a family plan at once, choose “covering more than one person”; if that was so for only part of the year, choose “No”. A change of insurer with no gap and the same kind of plan is not a change. A plan covering more than one person does not count if its deductible for any one person on it is below $3,300.

Shown for you on a couple's return:

> What counts is the plan you had on the first day of each month; plan papers usually call such a plan “HSA-eligible” or “HDHP”. If you were covered all year as a member of someone else's plan (a parent's, or your spouse's), or by a plan for only you and a family plan at once, choose “covering more than one person”; if that was so for only part of the year, choose “No”. A change of insurer with no gap and the same kind of plan is not a change. A plan covering more than one person does not count if its deductible for any one person on it is below $3,300.

Shown for your spouse:

> What counts is the plan your spouse had on the first day of each month; plan papers usually call such a plan “HSA-eligible” or “HDHP”. If your spouse was covered all year as a member of someone else's plan (a parent's, or yours), or by a plan for only your spouse and a family plan at once, choose “covering more than one person”; if that was so for only part of the year, choose “No”. A change of insurer with no gap and the same kind of plan is not a change. A plan covering more than one person does not count if its deductible for any one person on it is below $3,300.

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

## `f8889.former_spouse_family`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did a marriage of yours end during 2025, by divorce or death, while the other person had a high-deductible plan covering more than one person?

Shown on a one-person return:

> Did a marriage of yours end during 2025, by divorce or death, while the other person had a high-deductible plan covering more than one person?

Shown for you on a couple's return:

> About you — Did a marriage of yours end during 2025, by divorce or death, while the other person had a high-deductible plan covering more than one person?

Shown for your spouse:

> About your spouse — Did a marriage of your spouse's end during 2025, by divorce or death, while the other person had a high-deductible plan covering more than one person?

**Help, as stored**

> Answer No if you were not married at any time in 2025. A plan covering more than one person includes one for an employee and a child, and counts even if it did not cover you. A Yes ends the interview here.

Shown on a one-person return:

> Answer No if you were not married at any time in 2025. A plan covering more than one person includes one for an employee and a child, and counts even if it did not cover you. A Yes ends the interview here.

Shown for you on a couple's return:

> Answer No if you were not married at any time in 2025. A plan covering more than one person includes one for an employee and a child, and counts even if it did not cover you. A Yes ends the interview here.

Shown for your spouse:

> Answer No if your spouse was not married at any time in 2025. A plan covering more than one person includes one for an employee and a child, and counts even if it did not cover your spouse. A Yes ends the interview here.

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

## `person.age55_at_year_end`

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

> For this person (you, or your spouse on a joint return) — Your employer put more into your HSA than your limit. Is all of the extra included in box 1 of your Form W-2?

Shown on a one-person return:

> Your employer put more into your HSA than your limit. Is all of the extra included in box 1 of your Form W-2?

Shown for you on a couple's return:

> About you — Your employer put more into your HSA than your limit. Is all of the extra included in box 1 of your Form W-2?

Shown for your spouse:

> About your spouse — Your spouse's employer put more into your spouse's HSA than your spouse's limit. Is all of the extra included in box 1 of your spouse's Form W-2?

**Help, as stored**

> Box 1 is your taxable wages. Answer No if your employer has added none of the extra to it, or only part.

Shown on a one-person return:

> Box 1 is your taxable wages. Answer No if your employer has added none of the extra to it, or only part.

Shown for you on a couple's return:

> Box 1 is your taxable wages. Answer No if your employer has added none of the extra to it, or only part.

Shown for your spouse:

> Box 1 is your spouse's taxable wages. Answer No if your spouse's employer has added none of the extra to it, or only part.

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

## `f8889.ira_gap`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — From the month of that transfer until 12 months after it, was there a month in which you could not have an HSA?

Shown on a one-person return:

> From the month of that transfer until 12 months after it, was there a month in which you could not have an HSA?

Shown for you on a couple's return:

> About you — From the month of that transfer until 12 months after it, was there a month in which you could not have an HSA?

Shown for your spouse:

> About your spouse — From the month of that transfer until 12 months after it, was there a month in which your spouse could not have an HSA?

**Help, as stored**

> For a transfer on June 17, 2024, the months are June 2024 through June 2025. Answer Yes if on the first day of any of them you had no HSA-qualifying plan, were enrolled in Medicare, had other health coverage that pays medical bills, or could be claimed as a dependent.

Shown on a one-person return:

> For a transfer on June 17, 2024, the months are June 2024 through June 2025. Answer Yes if on the first day of any of them you had no HSA-qualifying plan, were enrolled in Medicare, had other health coverage that pays medical bills, or could be claimed as a dependent.

Shown for you on a couple's return:

> For a transfer on June 17, 2024, the months are June 2024 through June 2025. Answer Yes if on the first day of any of them you had no HSA-qualifying plan, were enrolled in Medicare, had other health coverage that pays medical bills, or could be claimed as a dependent.

Shown for your spouse:

> For a transfer on June 17, 2024, the months are June 2024 through June 2025. Answer Yes if on the first day of any of them your spouse had no HSA-qualifying plan, were enrolled in Medicare, had other health coverage that pays medical bills, or could be claimed as a dependent.

## `f8889.testing_prior`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Could you have an HSA on December 1, 2024, and was more put into it for 2024, by you, your employer or anyone else, than the months you could have one, and the kind of plan you had in each, allowed?

Shown on a one-person return:

> Could you have an HSA on December 1, 2024, and was more put into it for 2024, by you, your employer or anyone else, than the months you could have one, and the kind of plan you had in each, allowed?

Shown for you on a couple's return:

> About you — Could you have an HSA on December 1, 2024, and was more put into it for 2024, by you, your employer or anyone else, than the months you could have one, and the kind of plan you had in each, allowed?

Shown for your spouse:

> About your spouse — Could your spouse have an HSA on December 1, 2024, and was more put into it for 2024, by your spouse, your spouse's employer or anyone else, than the months your spouse could have one, and the kind of plan your spouse had in each, allowed?

**Help, as stored**

> This is about the “last-month rule”. A person who could have an HSA on December 1, 2024 was allowed the full yearly amount for the plan held that day, on condition of staying able to have an HSA through December 31, 2025. Answer Yes if more went in for 2024 than your own months allowed, counting each month by the plan of that month. That can be so if your plan began during 2024; if for part of 2024 you were someone's dependent or had other health coverage, counting a health FSA or HRA at work (also the extra months of a 2023 health FSA early in 2024, and your spouse's FSA); or if your plan, or a plan your spouse had, went from covering one person to covering more. Line 3 of your 2024 Form 8889 then shows the full yearly amount ($4,150 for a plan covering one person, $8,300 for more, before the extra $1,000 from age 55) although not every month of 2024 earned it. If you are not sure, answer Yes.

Shown on a one-person return:

> This is about the “last-month rule”. A person who could have an HSA on December 1, 2024 was allowed the full yearly amount for the plan held that day, on condition of staying able to have an HSA through December 31, 2025. Answer Yes if more went in for 2024 than your own months allowed, counting each month by the plan of that month. That can be so if your plan began during 2024; if for part of 2024 you were someone's dependent or had other health coverage, counting a health FSA or HRA at work (also the extra months of a 2023 health FSA early in 2024, and your spouse's FSA); or if your plan, or a plan your spouse had, went from covering one person to covering more. Line 3 of your 2024 Form 8889 then shows the full yearly amount ($4,150 for a plan covering one person, $8,300 for more, before the extra $1,000 from age 55) although not every month of 2024 earned it. If you are not sure, answer Yes.

Shown for you on a couple's return:

> This is about the “last-month rule”. A person who could have an HSA on December 1, 2024 was allowed the full yearly amount for the plan held that day, on condition of staying able to have an HSA through December 31, 2025. Answer Yes if more went in for 2024 than your own months allowed, counting each month by the plan of that month. That can be so if your plan began during 2024; if for part of 2024 you were someone's dependent or had other health coverage, counting a health FSA or HRA at work (also the extra months of a 2023 health FSA early in 2024, and your spouse's FSA); or if your plan, or a plan your spouse had, went from covering one person to covering more. Line 3 of your 2024 Form 8889 then shows the full yearly amount ($4,150 for a plan covering one person, $8,300 for more, before the extra $1,000 from age 55) although not every month of 2024 earned it. If you are not sure, answer Yes.

Shown for your spouse:

> This is about the “last-month rule”. A person who could have an HSA on December 1, 2024 was allowed the full yearly amount for the plan held that day, on condition of staying able to have an HSA through December 31, 2025. Answer Yes if more went in for 2024 than your spouse's own months allowed, counting each month by the plan of that month. That can be so if your spouse's plan began during 2024; if for part of 2024 your spouse was someone's dependent or had other health coverage, counting a health FSA or HRA at work (also the extra months of a 2023 health FSA early in 2024, and your FSA); or if your spouse's plan, or a plan you had, went from covering one person to covering more. Line 3 of your spouse's 2024 Form 8889 then shows the full yearly amount ($4,150 for a plan covering one person, $8,300 for more, before the extra $1,000 from age 55) although not every month of 2024 earned it. If your spouse is not sure, answer Yes.

## `f8889.disabled`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you stop being able to have an HSA in 2025 because you became disabled?

Shown on a one-person return:

> Did you stop being able to have an HSA in 2025 because you became disabled?

Shown for you on a couple's return:

> About you — Did you stop being able to have an HSA in 2025 because you became disabled?

Shown for your spouse:

> About your spouse — Did your spouse stop being able to have an HSA in 2025 because your spouse became disabled?

**Help, as stored**

> Losing it for any other reason, such as Medicare at 65 or a new job's ordinary health plan, means No.

Shown on a one-person return:

> Losing it for any other reason, such as Medicare at 65 or a new job's ordinary health plan, means No.

Shown for you on a couple's return:

> Losing it for any other reason, such as Medicare at 65 or a new job's ordinary health plan, means No.

Shown for your spouse:

> Losing it for any other reason, such as Medicare at 65 or a new job's ordinary health plan, means No.

## `f8889.mfs_spouse_hsa`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Does your husband or wife have a health savings account (HSA) of their own?

Shown on a one-person return:

> Does your husband or wife have a health savings account (HSA) of their own?

Shown for you on a couple's return:

> About you — Does your husband or wife have a health savings account (HSA) of their own?

Shown for your spouse:

> About your spouse — Does your spouse's husband or wife have a health savings account (HSA) of their own?

**Help, as stored**

> Count an HSA in their name even if nothing was put into it for 2025. A Yes ends the interview here.

Shown on a one-person return:

> Count an HSA in their name even if nothing was put into it for 2025. A Yes ends the interview here.

Shown for you on a couple's return:

> Count an HSA in their name even if nothing was put into it for 2025. A Yes ends the interview here.

Shown for your spouse:

> Count an HSA in their name even if nothing was put into it for 2025. A Yes ends the interview here.

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

> Add the balances of all your HSAs on December 31, 2025 (box 5 of each 2025 Form 5498-SA, or the account statements), and anything you put in during 2026 for 2025.

Shown on a one-person return:

> Add the balances of all your HSAs on December 31, 2025 (box 5 of each 2025 Form 5498-SA, or the account statements), and anything you put in during 2026 for 2025.

Shown for you on a couple's return:

> Add the balances of all your HSAs on December 31, 2025 (box 5 of each 2025 Form 5498-SA, or the account statements), and anything you put in during 2026 for 2025.

Shown for your spouse:

> Add the balances of all your spouse's HSAs on December 31, 2025 (box 5 of each 2025 Form 5498-SA, or the account statements), and anything your spouse put in during 2026 for 2025.

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

> Some costs count here that Schedule A does not take, among them nonprescription medicines, menstrual care products, condoms, COVID-19 home tests, and masks and hand sanitizer bought to keep COVID-19 from spreading. These costs cannot also be deducted on Schedule A.

Shown on a one-person return:

> Some costs count here that Schedule A does not take, among them nonprescription medicines, menstrual care products, condoms, COVID-19 home tests, and masks and hand sanitizer bought to keep COVID-19 from spreading. These costs cannot also be deducted on Schedule A.

Shown for you on a couple's return:

> Some costs count here that Schedule A does not take, among them nonprescription medicines, menstrual care products, condoms, COVID-19 home tests, and masks and hand sanitizer bought to keep COVID-19 from spreading. These costs cannot also be deducted on Schedule A.

Shown for your spouse:

> Some costs count here that Schedule A does not take, among them nonprescription medicines, menstrual care products, condoms, COVID-19 home tests, and masks and hand sanitizer bought to keep COVID-19 from spreading. These costs cannot also be deducted on Schedule A.

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

## `$tipjob`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — At which employers did you get tips in 2025?

Shown on a one-person return:

> At which employers did you get tips in 2025?

Shown for you on a couple's return:

> About you — At which employers did you get tips in 2025?

Shown for your spouse:

> About your spouse — At which employers did your spouse get tips in 2025?

**Help, as stored**

> Name only the employers where you received tips. If you received none, leave the list empty.

Shown on a one-person return:

> Name only the employers where you received tips. If you received none, leave the list empty.

Shown for you on a couple's return:

> Name only the employers where you received tips. If you received none, leave the list empty.

Shown for your spouse:

> Name only the employers where your spouse received tips. If your spouse received none, leave the list empty.

## `$otjob`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Which employers paid you overtime in 2025?

Shown on a one-person return:

> Which employers paid you overtime in 2025?

Shown for you on a couple's return:

> About you — Which employers paid you overtime in 2025?

Shown for your spouse:

> About your spouse — Which employers paid your spouse overtime in 2025?

**Help, as stored**

> Name only the employers that paid you overtime. If none did, leave the list empty.

Shown on a one-person return:

> Name only the employers that paid you overtime. If none did, leave the list empty.

Shown for you on a couple's return:

> Name only the employers that paid you overtime. If none did, leave the list empty.

Shown for your spouse:

> Name only the employers that paid your spouse overtime. If none did, leave the list empty.

## `$sc`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — In 2025, did you work for yourself: freelance or gig work, a side business, or a business of your own? Add one entry for each business; leave the list empty if you did not.

Shown on a one-person return:

> In 2025, did you work for yourself: freelance or gig work, a side business, or a business of your own? Add one entry for each business; leave the list empty if you did not.

Shown for you on a couple's return:

> About you — In 2025, did you work for yourself: freelance or gig work, a side business, or a business of your own? Add one entry for each business; leave the list empty if you did not.

Shown for your spouse:

> About your spouse — In 2025, did your spouse work for himself or herself: freelance or gig work, a side business, or a business of your spouse's own? Add one entry for each business; leave the list empty if your spouse did not.

**Help, as stored**

> Pay reported to you on Form 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business. Any short label will do, such as “Tutoring”.

Shown on a one-person return:

> Pay reported to you on Form 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business. Any short label will do, such as “Tutoring”.

Shown for you on a couple's return:

> Pay reported to you on Form 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business. Any short label will do, such as “Tutoring”.

Shown for your spouse:

> Pay reported to your spouse on Form 1099-NEC, 1099-K or 1099-MISC for your spouse's own work is usually such a business. Any short label will do, such as “Tutoring”.

## `person.se_screen`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Does any of these apply to you: an approved exemption from self-employment tax on religious grounds (Form 4361 or Form 4029); fees as a company director, a fiduciary or a fee-basis government employee that are not in a business listed here; Conservation Reserve Program payments; a choice of the optional method of figuring self-employment earnings; or earnings exempt under a social security agreement with another country or from work for a foreign government?

Shown on a one-person return:

> Does any of these apply to you: an approved exemption from self-employment tax on religious grounds (Form 4361 or Form 4029); fees as a company director, a fiduciary or a fee-basis government employee that are not in a business listed here; Conservation Reserve Program payments; a choice of the optional method of figuring self-employment earnings; or earnings exempt under a social security agreement with another country or from work for a foreign government?

Shown for you on a couple's return:

> About you — Does any of these apply to you: an approved exemption from self-employment tax on religious grounds (Form 4361 or Form 4029); fees as a company director, a fiduciary or a fee-basis government employee that are not in a business listed here; Conservation Reserve Program payments; a choice of the optional method of figuring self-employment earnings; or earnings exempt under a social security agreement with another country or from work for a foreign government?

Shown for your spouse:

> About your spouse — Does any of these apply to your spouse: an approved exemption from self-employment tax on religious grounds (Form 4361 or Form 4029); fees as a company director, a fiduciary or a fee-basis government employee that are not in a business listed here; Conservation Reserve Program payments; a choice of the optional method of figuring self-employment earnings; or earnings exempt under a social security agreement with another country or from work for a foreign government?

**Help, as stored**

> A Yes is outside what this tool prepares and ends the interview here.

Shown on a one-person return:

> A Yes is outside what this tool prepares and ends the interview here.

Shown for you on a couple's return:

> A Yes is outside what this tool prepares and ends the interview here.

Shown for your spouse:

> A Yes is outside what this tool prepares and ends the interview here.

## `person.plan`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you put money into a SEP IRA or a SIMPLE IRA for yourself for 2025, as a self-employed person?

Shown on a one-person return:

> Did you put money into a SEP IRA or a SIMPLE IRA for yourself for 2025, as a self-employed person?

Shown for you on a couple's return:

> About you — Did you put money into a SEP IRA or a SIMPLE IRA for yourself for 2025, as a self-employed person?

Shown for your spouse:

> About your spouse — Did your spouse put money into a SEP IRA or a SIMPLE IRA for himself or herself for 2025, as a self-employed person?

**Help, as stored**

> Money put in after the end of 2025 counts if it was for 2025 and paid by the due date of this return.

Shown on a one-person return:

> Money put in after the end of 2025 counts if it was for 2025 and paid by the due date of this return.

Shown for you on a couple's return:

> Money put in after the end of 2025 counts if it was for 2025 and paid by the due date of this return.

Shown for your spouse:

> Money put in after the end of 2025 counts if it was for 2025 and paid by the due date of this return.

## `person.plan_screen`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Does any of these apply: a SARSEP; a SEP rate that is not a whole percent or is over 25%; a SIMPLE plan that allows the higher limits of the SECURE 2.0 Act; money put in for yourself to another plan of your business too, such as a solo 401(k); with a SIMPLE IRA, pay you put into a 401(k) or 403(b) at a job; Roth SEP or Roth SIMPLE contributions; or contributions above the most that can be deducted, including any carried over from an earlier year?

Shown on a one-person return:

> Does any of these apply: a SARSEP; a SEP rate that is not a whole percent or is over 25%; a SIMPLE plan that allows the higher limits of the SECURE 2.0 Act; money put in for yourself to another plan of your business too, such as a solo 401(k); with a SIMPLE IRA, pay you put into a 401(k) or 403(b) at a job; Roth SEP or Roth SIMPLE contributions; or contributions above the most that can be deducted, including any carried over from an earlier year?

Shown for you on a couple's return:

> About you — Does any of these apply: a SARSEP; a SEP rate that is not a whole percent or is over 25%; a SIMPLE plan that allows the higher limits of the SECURE 2.0 Act; money put in for yourself to another plan of your business too, such as a solo 401(k); with a SIMPLE IRA, pay you put into a 401(k) or 403(b) at a job; Roth SEP or Roth SIMPLE contributions; or contributions above the most that can be deducted, including any carried over from an earlier year?

Shown for your spouse:

> About your spouse — Does any of these apply: a SARSEP; a SEP rate that is not a whole percent or is over 25%; a SIMPLE plan that allows the higher limits of the SECURE 2.0 Act; money put in for himself or herself to another plan of your spouse's business too, such as a solo 401(k); with a SIMPLE IRA, pay your spouse put into a 401(k) or 403(b) at a job; Roth SEP or Roth SIMPLE contributions; or contributions above the most that can be deducted, including any carried over from an earlier year?

**Help, as stored**

> A Yes is outside what this tool prepares and ends the interview here.

Shown on a one-person return:

> A Yes is outside what this tool prepares and ends the interview here.

Shown for you on a couple's return:

> A Yes is outside what this tool prepares and ends the interview here.

Shown for your spouse:

> A Yes is outside what this tool prepares and ends the interview here.

## `person.sep_rate`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — What contribution rate does your SEP plan state, as a percent of pay (for example 10)?

Shown on a one-person return:

> What contribution rate does your SEP plan state, as a percent of pay (for example 10)?

Shown for you on a couple's return:

> About you — What contribution rate does your SEP plan state, as a percent of pay (for example 10)?

Shown for your spouse:

> About your spouse — What contribution rate does your spouse's SEP plan state, as a percent of pay (for example 10)?

## `person.sep_contrib`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much did you put into your SEP IRA for yourself for 2025, counting money paid in up to the due date of this return?

Shown on a one-person return:

> How much did you put into your SEP IRA for yourself for 2025, counting money paid in up to the due date of this return?

Shown for you on a couple's return:

> About you — How much did you put into your SEP IRA for yourself for 2025, counting money paid in up to the due date of this return?

Shown for your spouse:

> About your spouse — How much did your spouse put into your spouse's SEP IRA for himself or herself for 2025, counting money paid in up to the due date of this return?

## `person.simple_deferral`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much of your own earnings did you put into your SIMPLE IRA for 2025 (salary reduction contributions, including any catch-up contributions your plan allows), counting money paid in up to the due date of this return?

Shown on a one-person return:

> How much of your own earnings did you put into your SIMPLE IRA for 2025 (salary reduction contributions, including any catch-up contributions your plan allows), counting money paid in up to the due date of this return?

Shown for you on a couple's return:

> About you — How much of your own earnings did you put into your SIMPLE IRA for 2025 (salary reduction contributions, including any catch-up contributions your plan allows), counting money paid in up to the due date of this return?

Shown for your spouse:

> About your spouse — How much of your spouse's own earnings did your spouse put into your spouse's SIMPLE IRA for 2025 (salary reduction contributions, including any catch-up contributions your spouse's plan allows), counting money paid in up to the due date of this return?

## `person.simple_age_at_year_end`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How old were you at the end of 2025?

Shown on a one-person return:

> How old were you at the end of 2025?

Shown for you on a couple's return:

> About you — How old were you at the end of 2025?

Shown for your spouse:

> About your spouse — How old was your spouse at the end of 2025?

## `person.simple_kind`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Which employer contribution does your SIMPLE IRA plan use for 2025?

Shown on a one-person return:

> Which employer contribution does your SIMPLE IRA plan use for 2025?

Shown for you on a couple's return:

> About you — Which employer contribution does your SIMPLE IRA plan use for 2025?

Shown for your spouse:

> About your spouse — Which employer contribution does your spouse's SIMPLE IRA plan use for 2025?

## `person.simple_employer`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much did you put into your SIMPLE IRA for 2025 as the employer’s contribution for yourself, counting money paid in up to the due date of this return?

Shown on a one-person return:

> How much did you put into your SIMPLE IRA for 2025 as the employer’s contribution for yourself, counting money paid in up to the due date of this return?

Shown for you on a couple's return:

> About you — How much did you put into your SIMPLE IRA for 2025 as the employer’s contribution for yourself, counting money paid in up to the due date of this return?

Shown for your spouse:

> About your spouse — How much did your spouse put into your spouse’s SIMPLE IRA for 2025 as the employer’s contribution for himself or herself, counting money paid in up to the due date of this return?

## `person.sav_student`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you a full-time student during any part of five calendar months of 2025?

Shown on a one-person return:

> Were you a full-time student during any part of five calendar months of 2025?

Shown for you on a couple's return:

> About you — Were you a full-time student during any part of five calendar months of 2025?

Shown for your spouse:

> About your spouse — Was your spouse a full-time student during any part of five calendar months of 2025?

**Help, as stored**

> Technical, trade and mechanical schools count, and so does a full-time on-farm training course given by a school or a government agency. On-the-job training, correspondence schools and schools that teach only over the internet do not.

Shown on a one-person return:

> Technical, trade and mechanical schools count, and so does a full-time on-farm training course given by a school or a government agency. On-the-job training, correspondence schools and schools that teach only over the internet do not.

Shown for you on a couple's return:

> Technical, trade and mechanical schools count, and so does a full-time on-farm training course given by a school or a government agency. On-the-job training, correspondence schools and schools that teach only over the internet do not.

Shown for your spouse:

> Technical, trade and mechanical schools count, and so does a full-time on-farm training course given by a school or a government agency. On-the-job training, correspondence schools and schools that teach only over the internet do not.

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

> Answer Yes only if someone actually claims you on their 2025 return, not merely could.

Shown on a one-person return:

> Answer Yes only if someone actually claims you on their 2025 return, not merely could.

Shown for you on a couple's return:

> Answer Yes only if someone actually claims you on their 2025 return, not merely could.

Shown for your spouse:

> Answer Yes only if someone actually claims your spouse on their 2025 return, not merely could.

## `person.ira_owner`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you have an IRA (an individual retirement account) of any kind at any time in 2025, or do you have one now?

Shown on a one-person return:

> Did you have an IRA (an individual retirement account) of any kind at any time in 2025, or do you have one now?

Shown for you on a couple's return:

> About you — Did you have an IRA (an individual retirement account) of any kind at any time in 2025, or do you have one now?

Shown for your spouse:

> About your spouse — Did your spouse have an IRA (an individual retirement account) of any kind at any time in 2025, or does your spouse have one now?

**Help, as stored**

> Traditional, Roth, SEP and SIMPLE IRAs count, and so do an IRA you inherited and one opened in early 2026 for 2025. A 401(k) or a pension at work is not an IRA. If you are not sure, answer Yes.

Shown on a one-person return:

> Traditional, Roth, SEP and SIMPLE IRAs count, and so do an IRA you inherited and one opened in early 2026 for 2025. A 401(k) or a pension at work is not an IRA. If you are not sure, answer Yes.

Shown for you on a couple's return:

> Traditional, Roth, SEP and SIMPLE IRAs count, and so do an IRA you inherited and one opened in early 2026 for 2025. A 401(k) or a pension at work is not an IRA. If you are not sure, answer Yes.

Shown for your spouse:

> Traditional, Roth, SEP and SIMPLE IRAs count, and so do an IRA your spouse inherited and one opened in early 2026 for 2025. A 401(k) or a pension at work is not an IRA. If your spouse is not sure, answer Yes.

## `person.sav_trad`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you put money into a traditional IRA for 2025? Money put in by April 15, 2026 for 2025 counts; a rollover from another retirement account does not.

Shown on a one-person return:

> Did you put money into a traditional IRA for 2025? Money put in by April 15, 2026 for 2025 counts; a rollover from another retirement account does not.

Shown for you on a couple's return:

> About you — Did you put money into a traditional IRA for 2025? Money put in by April 15, 2026 for 2025 counts; a rollover from another retirement account does not.

Shown for your spouse:

> About your spouse — Did your spouse put money into a traditional IRA for 2025? Money put in by April 15, 2026 for 2025 counts; a rollover from another retirement account does not.

**Help, as stored**

> It counts whether or not you can deduct it. Do not count money that went into a SEP IRA or a SIMPLE IRA, whether an employer paid it or you paid it for yourself from your own business.

Shown on a one-person return:

> It counts whether or not you can deduct it. Do not count money that went into a SEP IRA or a SIMPLE IRA, whether an employer paid it or you paid it for yourself from your own business.

Shown for you on a couple's return:

> It counts whether or not you can deduct it. Do not count money that went into a SEP IRA or a SIMPLE IRA, whether an employer paid it or you paid it for yourself from your own business.

Shown for your spouse:

> It counts whether or not your spouse can deduct it. Do not count money that went into a SEP IRA or a SIMPLE IRA, whether an employer paid it or your spouse paid it for himself or herself from your spouse's own business.

## `person.ira_trad`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much did you put into your traditional IRAs for 2025, in 2025 or by the deadline for your 2025 return (April 15, 2026, for most people)?

Shown on a one-person return:

> How much did you put into your traditional IRAs for 2025, in 2025 or by the deadline for your 2025 return (April 15, 2026, for most people)?

Shown for you on a couple's return:

> About you — How much did you put into your traditional IRAs for 2025, in 2025 or by the deadline for your 2025 return (April 15, 2026, for most people)?

Shown for your spouse:

> About your spouse — How much did your spouse put into your spouse's traditional IRAs for 2025, in 2025 or by the deadline for your spouse's 2025 return (April 15, 2026, for most people)?

**Help, as stored**

> Form 5498 or a statement from the IRA's trustee shows it. Leave out rollovers, repayments of a reservist distribution, money you deducted on your 2024 return, anything you took back out with its earnings by the deadline for your return, trustee's fees billed separately, and SEP or SIMPLE contributions.

Shown on a one-person return:

> Form 5498 or a statement from the IRA's trustee shows it. Leave out rollovers, repayments of a reservist distribution, money you deducted on your 2024 return, anything you took back out with its earnings by the deadline for your return, trustee's fees billed separately, and SEP or SIMPLE contributions.

Shown for you on a couple's return:

> Form 5498 or a statement from the IRA's trustee shows it. Leave out rollovers, repayments of a reservist distribution, money you deducted on your 2024 return, anything you took back out with its earnings by the deadline for your return, trustee's fees billed separately, and SEP or SIMPLE contributions.

Shown for your spouse:

> Form 5498 or a statement from the IRA's trustee shows it. Leave out rollovers, repayments of a reservist distribution, money your spouse deducted on your spouse's 2024 return, anything your spouse took back out with its earnings by the deadline for your spouse's return, trustee's fees billed separately, and SEP or SIMPLE contributions.

## `person.ira_extra_left`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you put more into your IRAs for 2025 than you were allowed, and was the extra still there after the deadline for your 2025 return?

Shown on a one-person return:

> Did you put more into your IRAs for 2025 than you were allowed, and was the extra still there after the deadline for your 2025 return?

Shown for you on a couple's return:

> About you — Did you put more into your IRAs for 2025 than you were allowed, and was the extra still there after the deadline for your 2025 return?

Shown for your spouse:

> About your spouse — Did your spouse put more into your spouse's IRAs for 2025 than your spouse was allowed, and was the extra still there after the deadline for your spouse's 2025 return?

**Help, as stored**

> The limit for traditional and Roth IRAs together is $7,000 ($8,000 if you were 50 or older at the end of 2025), or your taxable pay if that is less (on a joint return, the couple's pay less the other spouse's IRA contributions); a Roth IRA has a lower limit at higher incomes. Count money an employer put in and a rollover that did not qualify. A Yes ends the interview here.

Shown on a one-person return:

> The limit for traditional and Roth IRAs together is $7,000 ($8,000 if you were 50 or older at the end of 2025), or your taxable pay if that is less (on a joint return, the couple's pay less the other spouse's IRA contributions); a Roth IRA has a lower limit at higher incomes. Count money an employer put in and a rollover that did not qualify. A Yes ends the interview here.

Shown for you on a couple's return:

> The limit for traditional and Roth IRAs together is $7,000 ($8,000 if you were 50 or older at the end of 2025), or your taxable pay if that is less (on a joint return, the couple's pay less the other spouse's IRA contributions); a Roth IRA has a lower limit at higher incomes. Count money an employer put in and a rollover that did not qualify. A Yes ends the interview here.

Shown for your spouse:

> The limit for traditional and Roth IRAs together is $7,000 ($8,000 if your spouse was 50 or older at the end of 2025), or your spouse's taxable pay if that is less (on a joint return, the couple's pay less the other spouse's IRA contributions); a Roth IRA has a lower limit at higher incomes. Count money an employer put in and a rollover that did not qualify. A Yes ends the interview here.

## `person.ira_recharacterized`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did you move a 2025 IRA contribution from a traditional IRA to a Roth IRA, or the other way (a "recharacterization")?

Shown on a one-person return:

> Did you move a 2025 IRA contribution from a traditional IRA to a Roth IRA, or the other way (a "recharacterization")?

Shown for you on a couple's return:

> About you — Did you move a 2025 IRA contribution from a traditional IRA to a Roth IRA, or the other way (a "recharacterization")?

Shown for your spouse:

> About your spouse — Did your spouse move a 2025 IRA contribution from a traditional IRA to a Roth IRA, or the other way (a "recharacterization")?

**Help, as stored**

> A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown on a one-person return:

> A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown for you on a couple's return:

> A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown for your spouse:

> A return with this is outside what this tool prepares; a Yes ends the interview here.

## `person.x_ira_prior_excess`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — At the end of 2025, did your IRA still hold money put in above the limit in an earlier year?

Shown on a one-person return:

> At the end of 2025, did your IRA still hold money put in above the limit in an earlier year?

Shown for you on a couple's return:

> About you — At the end of 2025, did your IRA still hold money put in above the limit in an earlier year?

Shown for your spouse:

> About your spouse — At the end of 2025, did your spouse's IRA still hold money put in above the limit in an earlier year?

**Help, as stored**

> This is an excess contribution from before 2025 that was never taken out or used up. A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown on a one-person return:

> This is an excess contribution from before 2025 that was never taken out or used up. A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown for you on a couple's return:

> This is an excess contribution from before 2025 that was never taken out or used up. A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown for your spouse:

> This is an excess contribution from before 2025 that was never taken out or used up. A return with this is outside what this tool prepares; a Yes ends the interview here.

## `person.age50_at_year_end`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you age 50 or older at the end of 2025?

Shown on a one-person return:

> Were you age 50 or older at the end of 2025?

Shown for you on a couple's return:

> About you — Were you age 50 or older at the end of 2025?

Shown for your spouse:

> About your spouse — Was your spouse age 50 or older at the end of 2025?

**Help, as stored**

> Age 50 or older at the end of 2025 raises the IRA contribution limit to $8,000, changes the IRA Deduction Worksheet's percentages, and allows catch-up contributions to a SIMPLE IRA.

Shown on a one-person return:

> Age 50 or older at the end of 2025 raises the IRA contribution limit to $8,000, changes the IRA Deduction Worksheet's percentages, and allows catch-up contributions to a SIMPLE IRA.

Shown for you on a couple's return:

> Age 50 or older at the end of 2025 raises the IRA contribution limit to $8,000, changes the IRA Deduction Worksheet's percentages, and allows catch-up contributions to a SIMPLE IRA.

Shown for your spouse:

> Age 50 or older at the end of 2025 raises the IRA contribution limit to $8,000, changes the IRA Deduction Worksheet's percentages, and allows catch-up contributions to a SIMPLE IRA.

## `person.ira_work_plan`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Were you covered by a retirement plan at work in 2025, such as a pension or a 401(k), even if you were not vested in it? If you were, the "Retirement plan" box in box 13 of your Form W-2 should be ticked.

Shown on a one-person return:

> Were you covered by a retirement plan at work in 2025, such as a pension or a 401(k), even if you were not vested in it? If you were, the "Retirement plan" box in box 13 of your Form W-2 should be ticked.

Shown for you on a couple's return:

> About you — Were you covered by a retirement plan at work in 2025, such as a pension or a 401(k), even if you were not vested in it? If you were, the "Retirement plan" box in box 13 of your Form W-2 should be ticked.

Shown for your spouse:

> About your spouse — Was your spouse covered by a retirement plan at work in 2025, such as a pension or a 401(k), even if your spouse was not vested in it? If your spouse was, the "Retirement plan" box in box 13 of your spouse's Form W-2 should be ticked.

**Help, as stored**

> If you are not sure, ask the employer. Social security and railroad retirement are not a plan. A SEP or SIMPLE IRA of a business of your own is taken from the answers about the business.

Shown on a one-person return:

> If you are not sure, ask the employer. Social security and railroad retirement are not a plan. A SEP or SIMPLE IRA of a business of your own is taken from the answers about the business.

Shown for you on a couple's return:

> If you are not sure, ask the employer. Social security and railroad retirement are not a plan. A SEP or SIMPLE IRA of a business of your own is taken from the answers about the business.

Shown for your spouse:

> If your spouse is not sure, ask the employer. Social security and railroad retirement are not a plan. A SEP or SIMPLE IRA of a business of your spouse's own is taken from the answers about the business.

## `person.ira_basis`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Your total basis in traditional IRAs (Form 8606 line 2): zero if this is the first year you are required to file Form 8606 (you made no nondeductible traditional IRA contributions before 2025); otherwise the amount the Total Basis Chart in the Form 8606 instructions gives for the last Form 8606 you filed (generally line 14 of that form)

Shown on a one-person return:

> Your total basis in traditional IRAs (Form 8606 line 2): zero if this is the first year you are required to file Form 8606 (you made no nondeductible traditional IRA contributions before 2025); otherwise the amount the Total Basis Chart in the Form 8606 instructions gives for the last Form 8606 you filed (generally line 14 of that form)

Shown for you on a couple's return:

> About you — Your total basis in traditional IRAs (Form 8606 line 2): zero if this is the first year you are required to file Form 8606 (you made no nondeductible traditional IRA contributions before 2025); otherwise the amount the Total Basis Chart in the Form 8606 instructions gives for the last Form 8606 you filed (generally line 14 of that form)

Shown for your spouse:

> About your spouse — Your spouse's total basis in traditional IRAs (Form 8606 line 2): zero if this is the first year your spouse is required to file Form 8606 (your spouse made no nondeductible traditional IRA contributions before 2025); otherwise the amount the Total Basis Chart in the Form 8606 instructions gives for the last Form 8606 your spouse filed (generally line 14 of that form)

**Help, as stored**

> Your basis is the total of your nondeductible contributions to traditional IRAs, less any nontaxable distributions; zero if you made no nondeductible contributions before 2025.

Shown on a one-person return:

> Your basis is the total of your nondeductible contributions to traditional IRAs, less any nontaxable distributions; zero if you made no nondeductible contributions before 2025.

Shown for you on a couple's return:

> Your basis is the total of your nondeductible contributions to traditional IRAs, less any nontaxable distributions; zero if you made no nondeductible contributions before 2025.

Shown for your spouse:

> Your spouse's basis is the total of your spouse's nondeductible contributions to traditional IRAs, less any nontaxable distributions; zero if your spouse made no nondeductible contributions before 2025.

## `person.ira_basis_adjusted`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Did your traditional IRA basis change other than by nondeductible contributions? That is: did the last Form 8606 you filed with Part I completed have a Line 15c Worksheet with an amount on line 6; or, since the last Form 8606 you filed (ever, if you have filed none), did you have a return of excess traditional IRA contributions, transfer or receive a traditional IRA incident to divorce, or roll over a nontaxable part of a qualified retirement plan to a traditional IRA that wasn't previously reported on Form 8606, line 2?

Shown on a one-person return:

> Did your traditional IRA basis change other than by nondeductible contributions? That is: did the last Form 8606 you filed with Part I completed have a Line 15c Worksheet with an amount on line 6; or, since the last Form 8606 you filed (ever, if you have filed none), did you have a return of excess traditional IRA contributions, transfer or receive a traditional IRA incident to divorce, or roll over a nontaxable part of a qualified retirement plan to a traditional IRA that wasn't previously reported on Form 8606, line 2?

Shown for you on a couple's return:

> About you — Did your traditional IRA basis change other than by nondeductible contributions? That is: did the last Form 8606 you filed with Part I completed have a Line 15c Worksheet with an amount on line 6; or, since the last Form 8606 you filed (ever, if you have filed none), did you have a return of excess traditional IRA contributions, transfer or receive a traditional IRA incident to divorce, or roll over a nontaxable part of a qualified retirement plan to a traditional IRA that wasn't previously reported on Form 8606, line 2?

Shown for your spouse:

> About your spouse — Did your spouse's traditional IRA basis change other than by nondeductible contributions? That is: did the last Form 8606 your spouse filed with Part I completed have a Line 15c Worksheet with an amount on line 6; or, since the last Form 8606 your spouse filed (ever, if your spouse has filed none), did your spouse have a return of excess traditional IRA contributions, transfer or receive a traditional IRA incident to divorce, or roll over a nontaxable part of a qualified retirement plan to a traditional IRA that wasn't previously reported on Form 8606, line 2?

**Help, as stored**

> Count only what happened since the last Form 8606 you filed (or ever, if you have filed none). Yes refuses the return (the Form 8606 line 2 adjustments are not prepared).

Shown on a one-person return:

> Count only what happened since the last Form 8606 you filed (or ever, if you have filed none). Yes refuses the return (the Form 8606 line 2 adjustments are not prepared).

Shown for you on a couple's return:

> Count only what happened since the last Form 8606 you filed (or ever, if you have filed none). Yes refuses the return (the Form 8606 line 2 adjustments are not prepared).

Shown for your spouse:

> Count only what happened since the last Form 8606 your spouse filed (or ever, if your spouse has filed none). Yes refuses the return (the Form 8606 line 2 adjustments are not prepared).

## `person.ira_dist`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — In 2025, did you take a distribution from a traditional IRA (including a SEP or SIMPLE IRA), or make a Roth IRA conversion? Do not count rollovers (but count a repayment, treated as a rollover, of a 2025 qualified disaster, birth or adoption, emergency personal expense, domestic abuse or terminal illness distribution), qualified charitable distributions, a one-time distribution to fund an HSA, recharacterizations, or returns of contributions made by the due date of the return.

Shown on a one-person return:

> In 2025, did you take a distribution from a traditional IRA (including a SEP or SIMPLE IRA), or make a Roth IRA conversion? Do not count rollovers (but count a repayment, treated as a rollover, of a 2025 qualified disaster, birth or adoption, emergency personal expense, domestic abuse or terminal illness distribution), qualified charitable distributions, a one-time distribution to fund an HSA, recharacterizations, or returns of contributions made by the due date of the return.

Shown for you on a couple's return:

> About you — In 2025, did you take a distribution from a traditional IRA (including a SEP or SIMPLE IRA), or make a Roth IRA conversion? Do not count rollovers (but count a repayment, treated as a rollover, of a 2025 qualified disaster, birth or adoption, emergency personal expense, domestic abuse or terminal illness distribution), qualified charitable distributions, a one-time distribution to fund an HSA, recharacterizations, or returns of contributions made by the due date of the return.

Shown for your spouse:

> About your spouse — In 2025, did your spouse take a distribution from a traditional IRA (including a SEP or SIMPLE IRA), or make a Roth IRA conversion? Do not count rollovers (but count a repayment, treated as a rollover, of a 2025 qualified disaster, birth or adoption, emergency personal expense, domestic abuse or terminal illness distribution), qualified charitable distributions, a one-time distribution to fund an HSA, recharacterizations, or returns of contributions made by the due date of the return.

**Help, as stored**

> Paying back a 2025 disaster, birth or adoption, emergency, domestic abuse or terminal illness withdrawal counts here too. Yes refuses the return (Form 8606 lines 4 to 13 are not prepared).

Shown on a one-person return:

> Paying back a 2025 disaster, birth or adoption, emergency, domestic abuse or terminal illness withdrawal counts here too. Yes refuses the return (Form 8606 lines 4 to 13 are not prepared).

Shown for you on a couple's return:

> Paying back a 2025 disaster, birth or adoption, emergency, domestic abuse or terminal illness withdrawal counts here too. Yes refuses the return (Form 8606 lines 4 to 13 are not prepared).

Shown for your spouse:

> Paying back a 2025 disaster, birth or adoption, emergency, domestic abuse or terminal illness withdrawal counts here too. Yes refuses the return (Form 8606 lines 4 to 13 are not prepared).

## `person.sav_able`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Is an ABLE account held for you, and did you put money into it for 2025, or get money out of it in 2023 or later?

Shown on a one-person return:

> Is an ABLE account held for you, and did you put money into it for 2025, or get money out of it in 2023 or later?

Shown for you on a couple's return:

> About you — Is an ABLE account held for you, and did you put money into it for 2025, or get money out of it in 2023 or later?

Shown for your spouse:

> About your spouse — Is an ABLE account held for your spouse, and did your spouse put money into it for 2025, or get money out of it in 2023 or later?

**Help, as stored**

> A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown on a one-person return:

> A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown for you on a couple's return:

> A return with this is outside what this tool prepares; a Yes ends the interview here.

Shown for your spouse:

> A return with this is outside what this tool prepares; a Yes ends the interview here.

## `person.sav_roth`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much did you put into a Roth IRA for 2025, in 2025 or by the deadline for your 2025 return? Do not count rollovers or conversions.

Shown on a one-person return:

> How much did you put into a Roth IRA for 2025, in 2025 or by the deadline for your 2025 return? Do not count rollovers or conversions.

Shown for you on a couple's return:

> About you — How much did you put into a Roth IRA for 2025, in 2025 or by the deadline for your 2025 return? Do not count rollovers or conversions.

Shown for your spouse:

> About your spouse — How much did your spouse put into a Roth IRA for 2025, in 2025 or by the deadline for your spouse's 2025 return? Do not count rollovers or conversions.

**Help, as stored**

> Leave out money you took back out with its earnings by the deadline, and paying back a disaster, birth or adoption, or emergency withdrawal. A contribution later moved to a traditional IRA (recharacterized) is a traditional IRA contribution.

Shown on a one-person return:

> Leave out money you took back out with its earnings by the deadline, and paying back a disaster, birth or adoption, or emergency withdrawal. A contribution later moved to a traditional IRA (recharacterized) is a traditional IRA contribution.

Shown for you on a couple's return:

> Leave out money you took back out with its earnings by the deadline, and paying back a disaster, birth or adoption, or emergency withdrawal. A contribution later moved to a traditional IRA (recharacterized) is a traditional IRA contribution.

Shown for your spouse:

> Leave out money your spouse took back out with its earnings by the deadline, and paying back a disaster, birth or adoption, or emergency withdrawal. A contribution later moved to a traditional IRA (recharacterized) is a traditional IRA contribution.

## `person.sav_voluntary`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — How much of your own after-tax money did you choose to put into a retirement plan at work for 2025? It may be shown in box 14 of your Form W-2.

Shown on a one-person return:

> How much of your own after-tax money did you choose to put into a retirement plan at work for 2025? It may be shown in box 14 of your Form W-2.

Shown for you on a couple's return:

> About you — How much of your own after-tax money did you choose to put into a retirement plan at work for 2025? It may be shown in box 14 of your Form W-2.

Shown for your spouse:

> About your spouse — How much of your spouse's own after-tax money did your spouse choose to put into a retirement plan at work for 2025? It may be shown in box 14 of your spouse's Form W-2.

**Help, as stored**

> Do not count Roth contributions, contributions your employer requires of you, or contributions your employer pays for you. The federal Thrift Savings Plan counts as a plan.

Shown on a one-person return:

> Do not count Roth contributions, contributions your employer requires of you, or contributions your employer pays for you. The federal Thrift Savings Plan counts as a plan.

Shown for you on a couple's return:

> Do not count Roth contributions, contributions your employer requires of you, or contributions your employer pays for you. The federal Thrift Savings Plan counts as a plan.

Shown for your spouse:

> Do not count Roth contributions, contributions your spouse's employer requires of your spouse, or contributions your spouse's employer pays for your spouse. The federal Thrift Savings Plan counts as a plan.

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

## `$k1s`

**Question, as stored**

> For this person (you, or your spouse on a joint return) — Which S corporations sent you a Schedule K-1 (Form 1120-S) for 2025?

Shown on a one-person return:

> Which S corporations sent you a Schedule K-1 (Form 1120-S) for 2025?

Shown for you on a couple's return:

> About you — Which S corporations sent you a Schedule K-1 (Form 1120-S) for 2025?

Shown for your spouse:

> About your spouse — Which S corporations sent your spouse a Schedule K-1 (Form 1120-S) for 2025?

**Help, as stored**

> Name each corporation once, as on its K-1. A K-1 from a partnership, an estate or a trust is not listed here. If you received none from an S corporation, leave the list empty.

Shown on a one-person return:

> Name each corporation once, as on its K-1. A K-1 from a partnership, an estate or a trust is not listed here. If you received none from an S corporation, leave the list empty.

Shown for you on a couple's return:

> Name each corporation once, as on its K-1. A K-1 from a partnership, an estate or a trust is not listed here. If you received none from an S corporation, leave the list empty.

Shown for your spouse:

> Name each corporation once, as on its K-1. A K-1 from a partnership, an estate or a trust is not listed here. If your spouse received none from an S corporation, leave the list empty.
