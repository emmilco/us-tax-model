#!/usr/bin/env python3
"""Lane 4a: write interview/2025/coverage/retirement.yaml. One row for each situation the old retirement.special,
retirement.code_screen, ssb.pub915 and ssb.lump_sum covered, each ending in the refusal it ended in before (or, for
the items the box 7 code now catches, at retirement.bad_code). A row answers the questions its filer meets, in the
interview's order, up to the one that ends the walk. Rerun after changing a path."""
E = "person[taxpayer].retirement[r]"
# The questions a form meets, in asking order (seq), with the answer of a filer who has nothing special.
# The order is the one the engine asks today: the questions retirement.special reads come first (it is the first
# refusal entry on the lines that read the boxes), then the code check, then the boxes. When the asking-order fix
# lands (docs/provisional/lanes/order.md) the boxes and `under59` will come where their `seq` puts them (after
# `account` and after `code`); move them in these lists then and rerun.
FLAT_PLAN = [("rollover_any", False), ("disaster", False), ("loan_offset", False), ("disability", False), ("pso_exclusion", False), ("born_1936", False)]
PLAN7 = [("account", "plan"), ("box6", False), ("code", "normal_7")] + FLAT_PLAN + [("cost_any", False), ("under59", False), ("box1", 2400000), ("box5", 0)]
IRA7 = [("account", "traditional_ira"), ("code", "normal_7"), ("rollover_any", False), ("charity_hsa", False), ("ira_returned", False),
        ("ira_basis", False), ("disaster", False), ("under59", False), ("box1", 900000)]
PLAN4 = [("account", "plan"), ("box6", False), ("code", "death_4")] + FLAT_PLAN + [("death_exclusion", False), ("ben_before_retire", False),
         ("ben_guaranteed", False), ("ben_shared", False), ("cost_any", False), ("not_beneficiary", False), ("box1", 2400000), ("box5", 0)]
PLAN2 = [("account", "plan"), ("box6", False), ("code", "early_exception_2")] + FLAT_PLAN + [("cost_any", False), ("code2_partial", False)]
PLAN_OTHER = [("account", "plan"), ("box6", False), ("code", "other")] + FLAT_PLAN + [("cost_any", False)]
IRA_OTHER = [("account", "traditional_ira"), ("code", "other"), ("rollover_any", False), ("charity_hsa", False), ("ira_returned", False), ("ira_basis", False), ("disaster", False)]
ROLL = [("roth_moved", False), ("rollover_property", False), ("rollover_qdro", False), ("levy_returned", False)]
DIS = [("dis_early", False), ("dis_terror", False), ("dis_military", False)]
COST = [("own_annuity", False), ("csrs_alt", False), ("start_1996", False), ("general_rule", False), ("lump_at_start", False)]

def path(base, upto, opened=None, child=None):
    """base up to and including `upto` (set to True when it is the parent of `opened`), then the opened children up to `child`."""
    out = []
    for k, v in base:
        if k == upto:
            out.append((k, True)); break
        out.append((k, v))
    else:
        raise SystemExit("not on path: " + upto)
    if opened:
        for k, v in opened:
            if k == child:
                out.append((k, True)); break
            out.append((k, v))
        else:
            raise SystemExit("not a child: " + str(child))
    return out

rows = []
def row(id, design, situation, answers, expect, pre=None):
    rows.append((id, design, situation, pre or [], answers, expect))
SPECIAL = f"refused: {E}.special"
def special(id, item, situation, base, upto, opened=None, child=None):
    row("retirement." + id, f"retirement.special: {item}", situation, path(base, upto, opened, child), SPECIAL)

special("roth", "a conversion; a rollover to a Roth IRA or designated Roth account", "A person moved pension money into a Roth IRA.", PLAN7, "rollover_any", ROLL, "roth_moved")
special("rollover_property", "a rollover of property other than cash", "A plan paid out shares, which the person sold before rolling over the money.", PLAN7, "rollover_any", ROLL, "rollover_property")
special("rollover_qdro", "a rollover of a distribution under a qualified domestic relations order", "A person rolled over money received from a former spouse's plan under a court order.", PLAN7, "rollover_any", ROLL, "rollover_qdro")
special("levy_returned", "a distribution the IRS wrongfully levied, returned and contributed back", "The IRS returned a levied amount, which the person put back into the plan.", PLAN7, "rollover_any", ROLL, "levy_returned")
special("charity_hsa", "a qualified charitable distribution or HSA funding distribution", "An IRA owner had part of a withdrawal sent straight to a charity.", IRA7, "charity_hsa")
special("ira_returned", "an IRA contribution returned; excess contributions for an earlier year returned in 2025", "An IRA paid back a contribution that was over the yearly limit.", IRA7, "ira_returned")
special("ira_basis", "nondeductible contributions to any traditional IRA", "An IRA owner made contributions in earlier years that were not deducted.", IRA7, "ira_basis")
special("box6", "a distribution of employer securities with net unrealized appreciation (an amount in box 6)", "A plan's Form 1099-R shows an amount in box 6.", PLAN7, "box6")
special("loan_offset", "a plan loan offset", "An unpaid plan loan was taken off the balance when the person left the job.", PLAN7, "loan_offset")
special("dis_early", "a disability pension received before minimum retirement age", "A person of 60 draws a disability pension from a plan whose minimum retirement age is 62.", PLAN7, "disability", DIS, "dis_early")
special("dis_terror", "a pension partly excludable because of disability from a terrorist attack", "A disability pension for injuries in a terrorist attack.", PLAN7, "disability", DIS, "dis_terror")
special("dis_military", "a military disability pension", "A disability pension for service in the armed forces.", PLAN7, "disability", DIS, "dis_military")
special("pso_exclusion", "the retired public safety officer premium exclusion", "A retired firefighter wants to leave out the pension money that paid health insurance premiums.", PLAN7, "pso_exclusion")
special("lump_sum", "a lump-sum distribution you may report on Form 4972", "A person born in 1935 was paid the whole balance of a plan in 2025.", PLAN7, "born_1936", [("lump_sum", False)], "lump_sum")
special("death_exclusion", "a death benefit exclusion", "The beneficiary of an employee who died before August 21, 1996.", PLAN4, "death_exclusion")
special("ben_before_retire", "an annuity received as the beneficiary of an employee who died before retiring", "A widow draws the pension of a husband who died while still working.", PLAN4, "ben_before_retire")
special("ben_guaranteed", "guaranteed payments received as the beneficiary of a retiree under a life annuity contract", "A son receives the rest of the ten years of payments his late father's pension guaranteed.", PLAN4, "ben_guaranteed")
special("ben_shared", "an annuity shared among more than one beneficiary", "Two children share their late mother's pension.", PLAN4, "ben_shared")
special("own_annuity", "a nonqualified annuity", "A person draws an annuity bought from an insurance company with their own money.", PLAN7, "cost_any", COST, "own_annuity")
special("csrs_alt", "U.S. Civil Service retirement benefits under the alternative annuity option", "A federal retiree who took the lump-sum payment of contributions at retirement.", PLAN7, "cost_any", COST, "csrs_alt")
special("start_1996", "an annuity with after-tax cost whose starting date was before November 19, 1996", "A pension with after-tax contributions that began in 1994.", PLAN7, "cost_any", COST, "start_1996")
special("general_rule", "an annuity with after-tax cost for which the Simplified Method does not apply (the General Rule)", "A pension begun at 76 with ten years of payments guaranteed.", PLAN7, "cost_any", COST, "general_rule")
special("lump_at_start", "a nonperiodic payment on or after the annuity starting date of an annuity with after-tax cost", "A partial lump sum was paid when a pension with after-tax contributions began.", PLAN7, "cost_any", COST, "lump_at_start")
special("disaster", "a qualified disaster recovery distribution, a repayment or a recontribution (Form 8915-F)", "A person took money out of a 401(k) after a federally declared disaster.", PLAN7, "disaster")
special("disaster_ira", "the same, from an IRA", "An IRA owner took money out after a federally declared disaster.", IRA7, "disaster")

BAD = f"refused: {E}.bad_code"
for id, item, sit in [
    ("code_corrective", "a corrective distribution of excess deferrals or contributions (box 7 code 8, P or E)", "A 401(k) paid back excess deferrals; box 7 shows code 8."),
    ("code_loan_offset", "a plan loan offset (box 7 code M or L)", "A qualified plan loan offset; box 7 shows code M."),
    ("code_nonqualified", "a nonqualified annuity (box 7 shows D with another code)", "A commercial annuity's Form 1099-R shows the codes 7D."),
    ("code_rrb", "a Form RRB-1099-R (no code in box 7)", "A railroad retiree's Form RRB-1099-R, which has no distribution code."),
]:
    row("retirement." + id, "retirement.special: " + item + ", now ended by the code", sit, PLAN_OTHER, BAD)
row("retirement.code_recharacterized", "retirement.special: a recharacterization (box 7 code N or R), now ended by the code", "An IRA contribution was recharacterized; box 7 shows code R.", IRA_OTHER, BAD)

SCREEN = f"refused: {E}.screen_refused"
row("retirement.code7_under59", "retirement.code_screen: code 7 although under age 59½", "A person of 57 whose Form 1099-R wrongly shows code 7.", path(PLAN7, "under59") + [("sec457", False)], SCREEN)
row("retirement.code7_under59_457", "retirement.code_screen: code 7 under age 59½ from a section 457 plan (not an error)", "A person of 57 paid from a state's section 457 plan, which rightly shows code 7.", path(PLAN7, "under59") + [("sec457", True)], f"asks: {E}.box1")
row("retirement.code2_partial", "retirement.code_screen: code 2 and the exception does not cover all of it", "A code 2 distribution of which only part meets the exception.", path(PLAN2, "code2_partial"), SCREEN)
row("retirement.code4_not_beneficiary", "retirement.code_screen: code 4 although not a beneficiary", "A Form 1099-R wrongly shows code 4.", path(PLAN4, "not_beneficiary"), SCREEN)
row("retirement.ordinary_pension", "the common case", "A retiree with an ordinary pension (code 7, no after-tax contributions) meets none of the special situations and goes on to the amounts.", PLAN7[:-2],
    f"asks: {E}.box1\n      not_asked: ['{E}.rollover', '{E}.annuity', '{E}.roth_moved', '{E}.dis_early', '{E}.lump_sum', '{E}.own_annuity', '{E}.death_exclusion', '{E}.charity_hsa', '{E}.ira_basis', '{E}.sec457']")
row("retirement.ordinary_ira", "the common case", "A retiree with an ordinary withdrawal from a traditional IRA (code 7) goes on to the amount.", IRA7[:-1],
    f"asks: {E}.box1\n      not_asked: ['{E}.rollover', '{E}.box6', '{E}.loan_offset', '{E}.disability', '{E}.cost_any', '{E}.annuity', '{E}.born_1936', '{E}.roth_moved']")

def fmt(v):
    return "true" if v is True else "false" if v is False else str(v)
out = ["# Coverage rows for retirement money received (Form 1099-R) and social security. See opening.yaml for how a row is read.\n"
       "# Written by docs/provisional/lanes/l4a_work/coverage.py; change the paths there.\n"
       "tax_year: 2025\npart: Retirement money received, and social security\nprofile: full\nrows:\n"]
for id, design, sit, pre, answers, expect in rows:
    out.append(f"  - id: {id}\n    design: \"{design}\"\n    situation: \"{sit}\"\n    answers:\n      $retirement@person[taxpayer]: [r]\n")
    for k, v in answers:
        out.append(f"      {E}.{k}: {fmt(v)}\n")
    out.append(f"    expect:\n      {expect}\n")

# f1040.tax_exempt_interest (lane 5a) still has an old order number, so it is asked as soon as there are benefits;
# when it moves to its topic, take it out of S.
S = [("ssb.any", True), ("ssb.benefits", 2000000), ("f1040.tax_exempt_interest", 0), ("ssb.repaid_more", False), ("ssb.ira_covered", False), ("ssb.prior_year_pay", False), ("ssb.terror_disability", False)]
def srow(id, design, sit, answers, expect):
    out.append(f"  - id: {id}\n    design: \"{design}\"\n    situation: \"{sit}\"\n    answers:\n" + "".join(f"      {k}: {fmt(v)}\n" for k, v in answers) + f"    expect:\n      {expect}\n")
srow("ssb.repaid_more", "ssb.pub915: repayments (box 4) more than benefits (box 3)", "A person repaid more social security in 2025 than they were paid.", S[:3] + [("ssb.repaid_more", True)], "refused: ssb.pub915")
srow("ssb.ira_covered", "ssb.pub915: a traditional IRA contribution by a person covered by a retirement plan", "A person with benefits still works, is covered by the employer's plan and put money into a traditional IRA.", S[:4] + [("ssb.ira_covered", True)], "refused: ssb.pub915")
srow("ssb.lump_elect", "ssb.lump_sum: the lump-sum election", "Back benefits for 2023 were paid in 2025 and the person wants the lump-sum election method.", S[:5] + [("ssb.prior_year_pay", True), ("ssb.lump_elect", True)], "refused: ssb.lump_sum")
srow("ssb.lump_not_elected", "ssb.lump_sum: an earlier year's payment without the election", "Back benefits were paid in 2025 and the person does not ask for the election.", S[:5] + [("ssb.prior_year_pay", True), ("ssb.lump_elect", False)], "asks: ssb.terror_disability")
srow("ssb.terror_disability", "ssb.terror_disability", "Social security disability payments for injuries in a terrorist attack.", S[:6] + [("ssb.terror_disability", True)], "refused: ssb.terror_disability")
srow("ssb.none", "ssb.any: no benefits", "A person with no social security benefits is asked for no amount.", [("ssb.any", False)], "proceeds: {ssb.any: false}\n      not_asked: [ssb.benefits, ssb.repaid_more, ssb.prior_year_pay, ssb.terror_disability, ssb.ira_covered]")
srow("ssb.ordinary", "the common case", "A retiree with benefits and none of the special situations.", S, "proceeds: {ssb.any: true}\n      not_asked: [ssb.lump_elect]")
open("interview/2025/coverage/retirement.yaml", "w").write("".join(out))
print(len(rows) + 7, "rows")
