#!/usr/bin/env python3
"""Lane 4a: rewrite forms/2025/retirement.yaml so that retirement.special and retirement.code_screen are derived
lines over short gated questions, retirement.rollover sits beneath retirement.rollover_any, and retirement.annuity
beneath retirement.cost_any. Run once from the worktree root on the file as it stood at 100b132c; it refuses to run
twice. The question texts are in ITEMS below."""
import re, sys

PATH = "forms/2025/retirement.yaml"
src = open(PATH).read()
if "retirement.rollover_any" in src:
    sys.exit("already applied")

CITE_SPECIAL = ("    cite:\n      doc: i1040gi\n      locator: 'pp. 27-30, lines 4a-5b: Exceptions 2-4, Lump-Sum "
                "Distributions, Insurance Premiums for Retired Public\n        Safety Officers, Simplified Method'\n")
CITE_CODE = ("    cite:\n      doc: i5329\n      locator: 'p. 5, Line 2, \"Enter on line 2 the amount that you can exclude.\"'\n")


def q(s):
    return "'" + s.replace("'", "''") + "'"


def inp(id, text, gated_by=None, cite=CITE_SPECIAL):
    out = f"  - id: retirement.{id}\n    printed: (helper)\n    label: {q(text)}\n    type: Bool\n"
    if gated_by:
        out += f"    gated_by: retirement.{gated_by}\n"
    out += f"    expr:\n      op: input\n      source: {q(text)}\n" + cite
    return out


def gate(id, child, guard, open_when, label, cite=CITE_SPECIAL):
    """choose: guard == open_when -> the child input; otherwise false."""
    o, c = ("true", "false") if open_when else ("false", "true")
    return (f"  - id: retirement.{id}\n    printed: (gate)\n    label: {q(label)}\n    type: Bool\n    expr:\n"
            f"      op: choose\n      alternatives:\n"
            f"      - guard:\n          op: test\n          eq:\n          - retirement.{guard}\n          - const: {o}\n"
            f"        then: retirement.{child}\n"
            f"      - guard:\n          op: test\n          eq:\n          - retirement.{guard}\n          - const: {c}\n"
            f"        then: retirement.no\n" + cite)


def test_any(id, label, lines, printed="(helper)", cite=CITE_SPECIAL):
    out = f"  - id: retirement.{id}\n    printed: {printed}\n    label: {q(label)}\n    type: Bool\n    expr:\n      op: test\n      any:\n"
    for l in lines:
        out += f"      - op: test\n        eq:\n        - retirement.{l}\n        - const: true\n"
    return out + cite


def test_all(id, label, pairs, cite=CITE_SPECIAL):
    out = f"  - id: retirement.{id}\n    printed: (helper)\n    label: {q(label)}\n    type: Bool\n    expr:\n      op: test\n      all:\n"
    for l, v in pairs:
        out += f"      - op: test\n        eq:\n        - retirement.{l}\n        - const: {v}\n"
    return out + cite


def test_eq(id, label, line, const, cite=CITE_SPECIAL):
    return (f"  - id: retirement.{id}\n    printed: (helper)\n    label: {q(label)}\n    type: Bool\n    expr:\n      op: test\n"
            f"      eq:\n      - retirement.{line}\n      - const: {const}\n" + cite)


# (id, guard line, guard value that opens it, refuses?, text). guard None = asked of every Form 1099-R.
PLAN = ("is_ira", False)
IRA = ("is_ira", True)
ITEMS = [
    # where the money went
    ("roth_moved", ("put_back", True), True, "Did any of this money go into a Roth IRA or another Roth account?"),
    ("rollover_property", ("put_back", True), True, "Did the plan or IRA pay out anything other than cash (such as shares) that you then sold, kept, or put only partly into the new account?"),
    ("rollover_qdro", ("put_back", True), True, "Did you get this money under a court order in a divorce or separation (a qualified domestic relations order)?"),
    ("levy_returned", ("put_back", True), True, "Was this money taken by the IRS under a levy and later returned to you?"),
    ("charity_hsa", IRA, True, "Did any of this money go straight from the IRA to a charity, or into a health savings account?"),
    ("ira_returned", IRA, True, "Was any of this a contribution of yours that the IRA paid back to you, for example because you had put in more than the yearly limit?"),
    ("ira_basis", ("is_trad", True), True, "Have you ever put money into a traditional IRA that you did not deduct on a tax return?"),
    # the paper, and the plan
    ("box6", PLAN, True, "Is there an amount in box 6 of this form (net unrealized appreciation in employer's securities)?"),
    ("loan_offset", PLAN, True, "Was any of this amount an unpaid loan from the plan that was taken off your balance, not money paid out (a plan loan offset)?"),
    ("disability", PLAN, False, "Do you get this pension because you became disabled?"),
    ("dis_early", ("disability_if_plan", True), True, "When any of this was paid, were you younger than the earliest age at which the plan would have let you retire without the disability (its minimum retirement age)?"),
    ("dis_terror", ("disability_if_plan", True), True, "Did the disability result from a terrorist attack?"),
    ("dis_military", ("disability_if_plan", True), True, "Is it a disability pension for service in the armed forces?"),
    ("pso_exclusion", PLAN, True, "Are you a retired police officer, firefighter or other public safety officer who wants to leave out of income the part of this pension that paid for health or long-term care insurance?"),
    ("born_1936", PLAN, False, "Was the person who earned this pension or plan balance (you, or the person you inherited it from) born before January 2, 1936?"),
    ("lump_sum", ("born_1936_if_plan", True), True, "Was this the whole of that person's balance in the plan, paid out within one year (a lump-sum distribution)?"),
    # a payment after a death (code 4 from a plan)
    ("death_exclusion", ("plan_death", True), True, "Did the employee die before August 21, 1996, so that a death benefit exclusion applies to these payments?"),
    ("ben_before_retire", ("plan_death", True), True, "Did the person who died do so before starting to draw this pension (before retiring)?"),
    ("ben_guaranteed", ("plan_death", True), True, "Are these payments ones the plan guaranteed for a set period after the retiree's pension began, not a survivor's pension paid for your own life?"),
    ("ben_shared", ("plan_death", True), True, "Is this pension shared among more than one beneficiary?"),
    # after-tax cost
    ("cost_any", PLAN, False, "Was any of the money paid into this pension or annuity already taxed when it went in (after-tax contributions)? An amount in box 5 or box 9b means yes."),
    ("own_annuity", ("cost_any_if_plan", True), True, "Is this an annuity you bought yourself from an insurance company, not through an employer's plan (a nonqualified annuity)?"),
    ("csrs_alt", ("cost_any_if_plan", True), True, "Is this a federal civil service pension for which you took a lump-sum payment of your own contributions when you retired (the alternative annuity option)?"),
    ("start_1996", ("cost_any_if_plan", True), True, "Did the regular payments from this pension or annuity start before November 19, 1996? (For a survivor, count from when the retiree's payments started.)"),
    ("general_rule", ("cost_any_if_plan", True), True, "When the regular payments started, were you (or, for a survivor, the retiree) 75 or older, with payments guaranteed for five years or more?"),
    ("lump_at_start", ("cost_any_if_plan", True), True, "Besides regular payments, does this form include a one-time payment that came with the start of the pension, closed it out, or made your later payments smaller?"),
    # a disaster
    ("disaster", None, True, "Did you take this money out, or put money back, because of a federally declared disaster (Form 8915-F)?"),
]
COND = {"put_back": "some of the money went into another retirement account", "is_ira": None, "is_trad": "a traditional IRA",
        "disability_if_plan": "a disability pension", "born_1936_if_plan": "a person born before January 2, 1936",
        "plan_death": "a payment from a plan after a death (code 4)", "cost_any_if_plan": "after-tax cost in the plan"}
SUFFIX = {"put_back": "put_back", "is_trad": "trad", "disability_if_plan": "disability", "born_1936_if_plan": "born_1936",
          "plan_death": "death", "cost_any_if_plan": "cost"}

new = []
new.append("  - id: retirement.no\n    printed: (helper)\n    label: Year parameter s3.no (false)\n    type: Bool\n    expr:\n      op: param\n      ref: s3.no\n" + CITE_SPECIAL)
new.append(inp("rollover_any", "Did any of this money go into a retirement account again (a rollover or a conversion), even if it was paid to you first?"))
new.append(test_eq("rolled_some", "The filer put some of this money into a retirement account (asked unless the form is a direct rollover, code G)", "rollover_any", "true"))
new.append("  - id: retirement.put_back\n    printed: (helper)\n    label: Some of the money went into another retirement account (a direct rollover, code G, or the filer says so)\n    type: Bool\n    expr:\n      op: choose\n      alternatives:\n"
           "      - guard:\n          op: test\n          eq:\n          - retirement.direct\n          - const: true\n        then: retirement.direct\n"
           "      - guard:\n          op: test\n          eq:\n          - retirement.direct\n          - const: false\n        then: retirement.rolled_some\n" + CITE_SPECIAL)
new.append("  - id: retirement.rollover_if_any\n    printed: (gate)\n    label: Amount rolled over, asked only when some of the money went into another retirement account (none otherwise)\n    type: NonNegDollars\n    expr:\n      op: choose\n      alternatives:\n"
           "      - guard:\n          op: test\n          eq:\n          - retirement.rollover_any\n          - const: true\n        then: retirement.rollover\n"
           "      - guard:\n          op: test\n          eq:\n          - retirement.rollover_any\n          - const: false\n        then: retirement.zero\n" + CITE_SPECIAL)
new.append(test_eq("is_trad", "A traditional, SEP or SIMPLE IRA", "account", "traditional_ira"))
new.append(test_eq("is_death", "Code 4 (death)", "code", "death_4"))
new.append(test_all("plan_death", "A payment from a plan to a beneficiary (code 4, not an IRA)", [("is_ira", "false"), ("is_death", "true")]))

refusing = []
for id, guard, refuses, text in ITEMS:
    if guard is None:
        new.append(inp(id, text))
        reader = id
    else:
        g, val = guard
        suffix = ("plan" if not val else "ira") if g == "is_ira" else SUFFIX[g]
        gid = f"{id}_if_{suffix}"
        cond = ("a pension, annuity or plan (not an IRA)" if not val else "an IRA") if g == "is_ira" else COND[g]
        new.append(inp(id, text, gated_by=gid))
        new.append(gate(gid, id, g, val, f"{text} Asked only with {cond} (false otherwise)"))
        reader = gid
    if refuses:
        refusing.append(reader)

new.append(test_any("special", "A Form 1099-R situation that needs a form or rule outside this tool (any of the situations asked about one by one: where the money went, the IRA's history, employer securities, a plan loan offset, a disability pension, the public safety officer exclusion, a lump-sum distribution, a payment after a death, after-tax cost outside the Simplified Method, a disaster)", refusing))

# 1. replace the special input block
m = re.search(r"  - id: retirement\.special\n.*?(?=  - id: retirement\.annuity\n)", src, re.S)
assert m
src = src[:m.start()] + "".join(new) + src[m.end():]

# 2. rollover beneath rollover_any
src = src.replace("  - id: retirement.rollover\n    printed: (helper)\n", "  - id: retirement.rollover\n    printed: (helper)\n    gated_by: retirement.rollover_if_any\n", 1)
assert src.count("        then: retirement.rollover\n") == 2
i = src.index("  - id: retirement.rolled\n")
j = src.index("        then: retirement.rollover\n", i)
src = src[:j] + "        then: retirement.rollover_if_any\n" + src[j + len("        then: retirement.rollover\n"):]

# 3. annuity beneath cost_any
src = src.replace("  - id: retirement.annuity\n    printed: (helper)\n", "  - id: retirement.annuity\n    printed: (helper)\n    gated_by: retirement.annuity_if_cost\n", 1)
head, tail = src.split("  - id: retirement.cost\n", 1)
tail = re.sub(r"(?m)^(\s+- )retirement\.annuity$", r"\1retirement.annuity_if_cost", tail)
src = head + gate("annuity_if_cost", "annuity", "cost_any_if_plan", True, "The Simplified Method applies, asked only with after-tax cost in the plan (false without it)") + "  - id: retirement.cost\n" + tail

# 4. code_screen derived
code_items = [
    inp("under59", "Were you under age 59½ when you received any of this money?", gated_by="under59_if_code7", cite=CITE_CODE),
    test_eq("is_code7", "Code 7 (normal distribution)", "code", "normal_7", cite=CITE_CODE),
    gate("under59_if_code7", "under59", "is_code7", True, "Under age 59½ when the money was received, asked only with code 7 (false otherwise)", cite=CITE_CODE),
    inp("sec457", "Is it from a section 457 plan (a deferred compensation plan of a state or local government or a tax-exempt employer), and not money that was rolled into that plan from another kind of plan?", gated_by="sec457_if_under59", cite=CITE_CODE),
    gate("sec457_if_under59", "sec457", "under59_if_code7", True, "A section 457 plan distribution not from a rollover, asked only with code 7 under age 59½ (false otherwise)", cite=CITE_CODE),
    test_all("code7_wrong", "Code 7 although under age 59½, other than a section 457 plan distribution not from a rollover", [("under59_if_code7", "true"), ("sec457_if_under59", "false")], cite=CITE_CODE),
    inp("code2_partial", "Code 2 means the payer knows of an exception to the extra tax on early withdrawals. Does that exception fail to cover all of this money (it covers only part of it, or none)?", gated_by="code2_partial_if_code2", cite=CITE_CODE),
    test_eq("is_code2", "Code 2 (early distribution, exception applies)", "code", "early_exception_2", cite=CITE_CODE),
    gate("code2_partial_if_code2", "code2_partial", "is_code2", True, "The code 2 exception does not cover the whole distribution, asked only with code 2 (false otherwise)", cite=CITE_CODE),
    inp("not_beneficiary", "Code 4 is for money paid to the beneficiary of a person who has died. Did you get this money some other way?", gated_by="not_beneficiary_if_death", cite=CITE_CODE),
    gate("not_beneficiary_if_death", "not_beneficiary", "is_death", True, "Code 4 although not a beneficiary, asked only with code 4 (false otherwise)", cite=CITE_CODE),
    test_any("code_screen", "A code 2, 4 or 7 distribution whose code does not fit", ["code2_partial_if_code2", "code7_wrong", "not_beneficiary_if_death"], printed="(gate)", cite=CITE_CODE),
]
m = re.search(r"  - id: retirement\.code_screen\n.*?(?=  - id: retirement\.screen_refused\n)", src, re.S)
assert m
src = src[:m.start()] + "".join(code_items) + src[m.end():]
open(PATH, "w").write(src)
print("ok", len(refusing), "refusing items")
