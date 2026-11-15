#!/usr/bin/env python3
"""Lane 4a: write the bank entries of the retirement and social security topics into interview/2025/questions.yaml.
Every entry of `$retirement`, `retirement.*` and `ssb.*` is removed and the block below put where `$retirement` stood.
Rerun after editing ENTRIES; the result is the same whatever the bank held for these ids."""
import re
PATH = "interview/2025/questions.yaml"
REFUSE = "A return with this is outside what this tool prepares; a Yes ends the interview here."
WISH = "A return with this is outside what this tool prepares. To go on without it, answer No."
R, P = 170, 178   # order numbers: retirement money received; social security
# (input, order, extra yaml lines)
E = []
def e(input, order, seq, help=None, prompt=None, extra=""):
    def fold(key, text):
        if "\n" in text:
            return f"    {key}: |-\n" + "".join(("      " + l if l else "") + "\n" for l in text.split("\n"))
        return f"    {key}: " + ("'" + text.replace("'", "''") + "'") + "\n"
    out = f"  - input: {input}\n    order: {order}\n    seq: {seq}\n"
    if help: out += fold("help", help)
    if prompt: out += fold("prompt", prompt)
    E.append((input, out + extra))

e("$retirement", R, 1,
  prompt="For this person (you, or your spouse on a joint return) — In 2025, did you take money from a pension, an annuity, a 401(k) or an IRA? List each Form 1099-R you received (for example by payer), or leave the list empty.",
  help="List a Form RRB-1099-R too. Do not list a Form SSA-1099 or RRB-1099 (social security benefits); they are asked about separately.")
e("retirement.account", R, 2, prompt="What kind of account did this money come from?",
  help="The form has a small box marked “IRA/SEP/SIMPLE” next to box 7.",
  extra="    value_labels:\n"
        "      plan: A pension, an annuity, or a 401(k), 403(b) or 457(b) plan (the box “IRA/SEP/SIMPLE” is not ticked)\n"
        "      traditional_ira: A traditional IRA, a SEP IRA or a SIMPLE IRA (the box “IRA/SEP/SIMPLE” is ticked)\n"
        "      roth_ira: A Roth IRA\n")
e("retirement.box1", R, 3)
e("retirement.box5", R, 4)
e("retirement.box6", R, 5, help=REFUSE)
e("retirement.code", R, 6, prompt="Which code is in box 7 of this form?",
  extra="    value_labels:\n"
        "      normal_7: 7 (normal distribution)\n"
        "      early_1: 1 (early distribution, no known exception)\n"
        "      early_exception_2: 2 (early distribution, exception applies)\n"
        "      disability_3: 3 (disability)\n"
        "      death_4: 4 (death)\n"
        "      direct_rollover_G: G (direct rollover)\n"
        "      qualified_roth_Q: Q (qualified distribution from a Roth IRA)\n"
        "      simple_S: S (early distribution from a SIMPLE IRA in its first 2 years)\n"
        "      other: Any other code, two codes together (such as 7D or 4G), or no code at all (a Form RRB-1099-R has none)\n")
e("retirement.under59", R, 7)
e("retirement.sec457", R, 8, help="If you answer No, the code on the form does not fit and the interview ends here: this tool does not figure the extra tax that may then be due.")
e("retirement.code2_partial", R, 9, help=REFUSE)
e("retirement.not_beneficiary", R, 10, help=REFUSE)
e("retirement.exception", R, 11)
e("retirement.early_screen", R, 12, help=REFUSE, prompt="""Is any of these true of this early withdrawal?

- it is one of a series of substantially equal periodic payments that was later changed
- it is from an annuity contract or a modified endowment contract
- it repays a birth or adoption, terminal illness, domestic abuse or emergency personal expense distribution
- it is an emergency personal expense distribution within 3 years after an earlier one you have not repaid
- it is a qualified long-term care distribution made December 30 or 31, 2025
- more than one exception to the 10% additional tax applies to it""")
e("retirement.exc_amount", R, 13)
e("retirement.rollover_any", R, 14, help="Money moved into a Roth IRA counts. If all of it stayed with you, answer No.")
e("retirement.roth_moved", R, 15, help=REFUSE)
e("retirement.rollover", R, 16,
  prompt="How much of this money did you put into a pension, a 401(k) or similar plan, or an IRA within 60 days of receiving it?",
  help="Do not count a required minimum distribution, a hardship withdrawal, or one of a series of regular payments for your life or for ten years or more: those cannot be rolled over. A later deposit counts only under an IRS waiver.")
e("retirement.rollover_property", R, 17, help=REFUSE)
e("retirement.rollover_qdro", R, 18, help=REFUSE)
e("retirement.levy_returned", R, 19, help=REFUSE)
e("retirement.charity_hsa", R, 20, help=REFUSE)
e("retirement.ira_returned", R, 21, help=REFUSE)
e("retirement.ira_basis", R, 22, help="If any of your earlier tax returns includes Form 8606, answer Yes. " + REFUSE)
e("retirement.loan_offset", R, 24, help=REFUSE)
e("retirement.disability", R, 25)
e("retirement.dis_early", R, 26, help=REFUSE)
e("retirement.dis_terror", R, 27, help=REFUSE)
e("retirement.dis_military", R, 28, help=REFUSE)
e("retirement.pso_exclusion", R, 29, help=WISH)
e("retirement.born_1936", R, 30)
e("retirement.lump_sum", R, 31, help=REFUSE)
e("retirement.death_exclusion", R, 32, help=REFUSE)
e("retirement.ben_before_retire", R, 33, help=REFUSE)
e("retirement.ben_guaranteed", R, 34, help=REFUSE)
e("retirement.ben_shared", R, 35, help=REFUSE)
e("retirement.cost_any", R, 36, help="If you are not sure, answer Yes.")
e("retirement.own_annuity", R, 37, help=REFUSE)
e("retirement.csrs_alt", R, 38, help=REFUSE)
e("retirement.start_1996", R, 39, help=REFUSE)
e("retirement.general_rule", R, 40, help=REFUSE)
e("retirement.lump_at_start", R, 41, help=REFUSE)
e("retirement.annuity", R, 42,
  prompt="Is this pension or annuity paid in regular payments (monthly, yearly or the like)? If this form shows only a one-time payment, answer No.",
  help="With regular payments, the next questions figure the part of each payment that is tax free (the Simplified Method).")
for i, n in enumerate(["cost", "used_last_year", "last_line4", "joint_life", "age", "combined_age", "months", "recovered"]):
    e("retirement." + n, R, 43 + i)
e("retirement.disaster", R, 23, help="Count money taken out to buy or build a home that a disaster then stopped, if you put it back. " + REFUSE)
e("ssb.any", P, 1)
e("ssb.benefits", P, 2)
e("ssb.repaid_more", P, 3, help=REFUSE)
e("ssb.prior_year_pay", P, 5)
e("ssb.lump_elect", P, 6, help=WISH)
e("ssb.terror_disability", P, 7,
  prompt="Are any of these benefits disability payments for injuries from a terrorist attack against the United States or its allies?",
  help="For the September 11 attacks, count any injury eligible for coverage by the September 11 Victim Compensation Fund, whether or not you made a claim. " + REFUSE)
e("ssb.ira_covered", P, 4, help=REFUSE)
e("ssb.lived_apart", 179, 1)
for i, n in enumerate(["sav_military", "sav_404k", "sav_inherited"]):
    e("retirement." + n, 317, 1 + i)

s = open(PATH).read()
head, body = s.split("  questions:\n", 1)
entries = re.split(r"(?m)^(?=  - input: )", body)
mine = {i for i, _ in E}
out, placed = [], False
for en in entries:
    m = re.match(r"  - input: (\S+)\n", en)
    if m and (m.group(1) == "$retirement" or m.group(1).startswith(("retirement.", "ssb."))):
        if m.group(1) == "$retirement":
            out.append("".join(t for _, t in E)); placed = True
        continue
    out.append(en)
assert placed
open(PATH, "w").write(head + "  questions:\n" + "".join(out))
print(len(E), "entries")
