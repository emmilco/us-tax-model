import sys, pathlib
B = pathlib.Path('/tmp/nightplan/scratch/inc-m34/b')
def rep(rel, old, new):
    p = B / rel
    t = p.read_text()
    n = t.count(old)
    if n != 1:
        sys.exit(f'{rel}: expected 1 match, found {n}: {old[:80]!r}')
    p.write_text(t.replace(old, new))

Q = 'interview/2025/questions.yaml'
# ---- M3: BUG-0830 div.other_boxes help
rep(Q, "    help: Most forms show amounts only in boxes 1a, 1b, 2a, 5, 7 and 12. If you have no Form 1099-DIV, answer No.\n",
       "    help: Most forms show amounts only in boxes 1a, 1b, 2a, 5, 7 and 12. Count your share of a form in another's name, and\n"
       "      a payment with no form, such as a return of capital or a payout when a company closed.\n")
# ---- M3: BUG-0833 f4952.line1, carryover, prior_7
rep(Q, "    prompt: How much interest did you pay in 2025 on money borrowed to buy investments? Leave out interest on a home loan,\n"
       "      and interest on money that went into tax-exempt bonds or a business.\n",
       "    prompt: How much interest did you pay in 2025 on money borrowed to buy investments? Leave out interest on money used to\n"
       "      buy, build or improve your home, and on money that went into tax-exempt bonds or a business.\n")
rep(Q, "    prompt: Does a 2024 Form 4952 of yours (or, on a joint return, of your spouse's), on a joint or a separate 2024 return,\n"
       "      show an amount on line 7 (investment interest that could not be deducted in 2024)?\n",
       "    prompt: Do you (or, on a joint return, your spouse) have investment interest from before 2025 that could not be deducted\n"
       "      and is still unused (line 7 of the latest Form 4952)?\n")
rep(Q, "    help: The amount on line 7 of the Form 4952 filed for 2024. If you and your spouse each filed one on a separate 2024\n"
       "      return, add the two amounts.\n",
       "    help: Line 7 of the Form 4952 filed for 2024. If none was filed for 2024 because you took the standard deduction, line\n"
       "      7 of the latest one filed. On separate 2024 returns, add the two amounts.\n")
# ---- M4: BUG-0901 s2.household_help tick and help
rep(Q, '    tick: "Someone you paid to work in your home: a nanny, housekeeper, gardener"\n'
       "    help: Count anyone you paid yourself, whatever the amount. Do not count a company you hired, such as a cleaning service\n"
       "      or a daycare center.\n",
       '    tick: "Someone you paid to work for your household: nanny, housekeeper, driver"\n'
       "    help: Count a worker you choose and direct even if a payroll service or registry handles the pay, a private driver,\n"
       "      and pay in 2025 for 2024 work. Do not count a company that sends and directs its own staff.\n")
# ---- M4: BUG-0900 s2.amt_boat prompt and help
rep(Q, '    prompt: "Is any of the mortgage interest you (or, on a joint return, your spouse) deduct for a boat, a motor home or another recreational vehicle that was not your main home?"\n'
       '    help: "A house, an apartment, a condominium or a mobile home is not one of these. The alternative minimum tax (Form 6251) then has to be figured; a Yes ends the interview here."\n',
       '    prompt: "Is any of the mortgage interest you (or, on a joint return, your spouse) deduct for a place, not your main home, that is a boat or RV, or a home rented out for short stays?"\n'
       '    help: "A camper, travel trailer or houseboat is an RV. Count a place that was your main home for only part of 2025. The alternative minimum tax (Form 6251) then has to be figured; a Yes ends the interview here."\n')
# ---- M4: BUG-0897 f1040.estimated_any; BUG-0894 + 0897 sibling f1040.line26
rep(Q, "    tick: Estimated tax payments, or a 2024 refund applied to 2025\n"
       "    prompt: Did you (or, on a joint return, your spouse) send the IRS estimated tax payments for 2025, or have a 2024\n"
       "      refund applied to your 2025 tax?\n"
       "    help: Estimated payments are ones you send yourself during the year, usually each quarter; they are not tax taken\n"
       "      out of your pay.\n",
       "    tick: Estimated tax payments, or an overpayment applied to 2025\n"
       "    prompt: Were estimated tax payments made for 2025 by you (or, on a joint return, your spouse), or an earlier\n"
       "      overpayment applied to your 2025 tax?\n"
       "    help: Count payments by mail, online or card, including the one due in January 2026; an overpayment from your 2024\n"
       "      return or an amended return applied to 2025; and joint payments with a spouse or former spouse.\n")
rep(Q, "    prompt: How much estimated tax did you (or, on a joint return, your spouse) pay for 2025 in all, counting any 2024\n"
       "      refund applied to 2025?\n"
       "    help: On a joint return add what each of you paid, even if you paid separately.\n",
       "    prompt: How much estimated tax did you (or, on a joint return, your spouse) pay for 2025 in all, counting any\n"
       "      overpayment applied to 2025?\n"
       '    help: "On a joint return, add what each of you paid. For joint payments made with a spouse or former spouse whose\n'
       '      return is separate from yours, enter your share: any split you both agree on, otherwise in proportion to your\n'
       '      separate 2025 taxes."\n')
# ---- M4: BUG-0899 refund.itemized help, rec.two_returns help
rep(Q, "    help: If you took the standard deduction for 2024, the answer is No, and none of the refund, or of other money paid back\n"
       "      for 2024 deductions you could take only by itemizing, is taxed.\n"
       "    prompt: Did you itemize deductions on your 2024 federal return? (A Schedule A was filed with it.)\n",
       "    help: On separate 2024 returns, answer for the return of the one who got the money back. If that return took the\n"
       "      standard deduction, the answer is No, and none of the refund or other money paid back is taxed.\n"
       "    prompt: Did you itemize deductions on your 2024 federal return? (A Schedule A was filed with it.)\n")
rep(Q, "    help: Answer No if only one of you got money back, or if you filed one joint return for 2024. A Yes ends the interview\n"
       "      here.\n"
       "    prompt: Was the money paid back for deductions on two 2024 returns, each of you filing your own?\n",
       "    help: Answer No if you filed one joint 2024 return, or only one of you got money back (the questions that follow are\n"
       "      then about that person's 2024 return). A state income tax refund counts. A Yes ends the interview here.\n"
       "    prompt: Was the money paid back for deductions on two 2024 returns, each of you filing your own?\n")
# ---- M4: BUG-0873 f8853c
rep(Q, "    prompt: Were any of the payments at a set amount per day or month, whatever the care cost (\"Per diem\" checked in box 3 of\n"
       "      Form 1099-LTC)?\n",
       "    prompt: Were any of the payments a set amount per day, week, month or other period, whatever the care cost (\"Per diem\"\n"
       "      checked in box 3 of Form 1099-LTC)?\n")
rep(Q, "    prompt: In 2025, was anyone besides you (or, on a joint return, your spouse) also paid at a set rate under a policy on\n"
       "      this person?\n",
       "    prompt: In 2025, was anyone besides you (or, on a joint return, your spouse) paid at a set rate under a long-term care\n"
       "      policy on this person, or paid a life insurance benefit early because this person was ill?\n")
rep(Q, "    prompt: How much of those care costs was paid back to you, by insurance or otherwise?\n",
       "    prompt: How much of those care costs was, or will be, paid by insurance or anyone else, to you or straight to the care\n"
       "      provider? Leave out the payments at a set rate.\n")
rep(Q, "    help: A Yes ends the interview here.\n"
       "    prompt: Was any of that paid back under a policy issued before August 1, 1996?\n",
       "    help: Count a policy first issued then even if it was later exchanged or changed. A Yes ends the interview here.\n"
       "    prompt: Was any of that amount paid, or due, under a policy first issued before August 1, 1996?\n")

# ---- forms: f4952
F = 'forms/2025/f4952.yaml'
rep(F, "      label: Do you (or, on a joint return, your spouse) have investment interest expense disallowed in 2024 and carried\n"
       "        forward (line 7 of a 2024 Form 4952 of either of you, on a joint or a separate return)?\n"
       "      expr:\n"
       "        op: input\n"
       "        source: Do you (or, on a joint return, your spouse) have investment interest expense that was disallowed in 2024 and\n"
       "          carried forward to 2025 (an amount on line 7 of a 2024 Form 4952 of either of you, on a joint or a separate 2024\n"
       "          return)?\n"
       "      cite:\n"
       "        doc: f4952\n"
       "        locator: p. 1, Part I, line 2, \"Disallowed investment interest expense from 2024 Form 4952, line 7\"\n",
       "      label: Do you (or, on a joint return, your spouse) have investment interest expense from before 2025 that was\n"
       "        disallowed and not yet deducted (line 7 of the latest Form 4952 of either of you, on a joint or a separate return)?\n"
       "      expr:\n"
       "        op: input\n"
       "        source: Do you (or, on a joint return, your spouse) have investment interest expense from before 2025 that was\n"
       "          disallowed and not yet deducted, carried forward to 2025 (an amount on line 7 of the latest Form 4952 of either of\n"
       "          you, on a joint or a separate return)?\n"
       "      cite:\n"
       "        doc: f4952\n"
       "        locator: p. 1, Part I, line 2, \"Disallowed investment interest expense from 2024 Form 4952, line 7\"; p. 3, Who\n"
       "          Must File, \"You don’t have any carryover of disallowed investment interest expense from 2024\"\n"
       "      ambiguity: amb.2025.f4952_latest_carryover\n")
rep(F, "      label: The amount on line 7 of the 2024 Form 4952 (on a joint return, both spouses' amounts if each filed one)\n"
       "      expr:\n"
       "        op: input\n"
       "        source: The amount on line 7 of the 2024 Form 4952 (disallowed investment interest expense carried forward to 2025);\n"
       "          on a joint return, add both spouses' amounts if each filed a separate 2024 return with one\n",
       "      label: The amount on line 7 of the 2024 Form 4952, or of the latest one filed if none was filed for 2024 (on a joint\n"
       "        return, both spouses' amounts if each filed one)\n"
       "      expr:\n"
       "        op: input\n"
       "        source: The amount on line 7 of the 2024 Form 4952 (disallowed investment interest expense carried forward to 2025),\n"
       "          or of the latest Form 4952 filed if none was filed for 2024 because the standard deduction was taken; on a joint\n"
       "          return, add both spouses' amounts if each filed a separate 2024 return with one\n")
# ---- forms: s2.amt_boat
S2 = 'forms/2025/s2.yaml'
rep(S2, '      label: "Is any of the home mortgage interest you (or, on a joint return, your spouse) deduct for a boat, a motor home or another recreational vehicle that was not your main home?"\n'
        '      expr:\n'
        '        op: input\n'
        '        source: "Is any of the home mortgage interest you (or, on a joint return, your spouse) deduct for a boat, a motor home or another recreational vehicle that was not your main home?"\n',
        '      label: "Is any of the home mortgage interest you (or, on a joint return, your spouse) deduct for a dwelling that was not your main home and is a boat, a motor home or another recreational vehicle, or a house, apartment, condominium or mobile home used on a transient basis (rented out for short stays)?"\n'
        '      expr:\n'
        '        op: input\n'
        '        source: "Is any of the home mortgage interest you (or, on a joint return, your spouse) deduct for a dwelling that was not your main home for all of 2025 and is a boat, a motor home or another recreational vehicle, or a house, apartment, condominium or mobile home used on a transient basis (rented out for short stays)?"\n')
rep(S2, "        locator: 'p. 8, Line 3, Mortgage Interest, \"If you deducted home mortgage interest on Schedule A for a dwelling that isn’t a principal residence (within the meaning of section 121) or qualified dwelling for AMT, include that deducted interest on line 3\", \"A qualified dwelling for AMT doesn’t include house boats and recreational vehicles\"'\n"
        "    - id: s2.amt_boat_ask\n",
        "        locator: 'p. 8, Line 3, Mortgage Interest, \"If you deducted home mortgage interest on Schedule A for a dwelling that isn’t a principal residence (within the meaning of section 121) or qualified dwelling for AMT, include that deducted interest on line 3\", \"A qualified dwelling for AMT is a house, apartment, condominium, or mobile home not used on a transient basis\", \"A qualified dwelling for AMT doesn’t include house boats and recreational vehicles\"'\n"
        "      ambiguity: amb.2025.amt_transient\n"
        "    - id: s2.amt_boat_ask\n")
print('ok')
