#!/usr/bin/env python3
"""Lane 9: write interview/2025/coverage/scope.yaml, one row for each item the three scope screens covered.

Run from the worktree root:  python3 docs/provisional/lanes/l9_work/gen_cov.py
A row: (id, MAP row, situation, answers, the gate it must end at, sets used). `Y(...)` answers the named scope
questions Yes. The sets hold the answers a filer with a W-2 (or a business, a Form 1099-R) gives on the way.
"""
import json

S1, OI, L16 = "scope.schedule1", "scope.other_income", "scope.other_line16"


def Y(*names, **more):
    a = {f"scope.{n}": True for n in names}
    a.update(more)
    return a


SETS = {
    "one_w2": ("A person with one job and one Form W-2.", {
        "$w2@person[taxpayer]": ["job"],
        "person[taxpayer].w2[job].box1": 5200000,
        "person[taxpayer].w2[job].box2": 520000,
        "person[taxpayer].w2[job].box4": 322400,
        "person[taxpayer].w2[job].box5": 5200000,
        "person[taxpayer].w2[job].box6": 75400,
    }),
}
# A person with one business: the answers of the credits row that walks furthest through a business, none refusing.
import yaml
_fuel = next(r for r in yaml.safe_load(open("interview/2025/coverage/credits.yaml"))["rows"] if r["id"] == "credits.business_fuel")["answers"]
_biz = {k: v for k, v in _fuel.items() if not k.endswith((".plan", ".hi_uses"))}; _biz["person[taxpayer].sc[shop].fuel_credit"] = False
_biz.update({"person[taxpayer].sc[shop].line1": 5000000, "person[taxpayer].sc[shop].tips_ot": False, "person[taxpayer].se_screen": False})
SETS["one_business"] = ("A person who runs one small business.", _biz)

ROWS = [
 # 2.1 scope.schedule1
 ("statutory_employee", "MAP 2.1 item 1", "A person's W-2 has the 'Statutory employee' box ticked in box 13.", Y("w2_marks"), S1, ["one_w2"]),
 ("clergy", "MAP 2.1 item 2", "A minister is paid by her church.", Y("religious_work", "clergy"), S1, []),
 ("church_employee", "MAP 2.1 item 3", "A church's bookkeeper is paid wages with no social security or Medicare tax taken out.", Y("religious_work", "church_exempt_wages", **{"scope.clergy": False}), S1, []),
 ("recovery", "MAP 2.1 item 4", "A person was refunded property tax deducted on an earlier year's return.", Y("recovery"), S1, []),
 ("business_property_sale", "MAP 2.1 item 5 (already caught by sd.other_forms)", "A person sold equipment used in a business (Form 4797).", {"sd.other_forms": True}, "sd.other_forms", []),
 ("nol", "MAP 2.1 item 6", "A person who closed a business in 2023 carries its loss into 2025.", Y("business_before", "nol"), S1, []),
 ("rental", "MAP 2.1 item 7", "A person rents out a house she owns.", Y("rental"), S1, []),
 ("royalties", "MAP 2.1 item 7 (royalties)", "A person receives royalties from a book.", Y("rental"), S1, []),
 ("k1", "MAP 2.1 item 8", "A person has a share of a partnership's income, reported on a Schedule K-1.", Y("k1"), S1, []),
 ("equipment_rental", "MAP 2.1 item 9", "A person rents out a trailer he owns.", Y("rental"), S1, []),
 ("farm", "MAP 2.1 item 10", "A person runs a farm.", Y("farm"), S1, []),
 ("reservist_expenses", "MAP 2.1 item 13", "A National Guard member paid to travel 150 miles to drills.", Y("armed_forces", "reservist_expenses"), S1, []),
 ("performing_artist", "MAP 2.1 item 14", "An actor with two employers deducts unreimbursed costs as a qualified performing artist.", Y("artist_official", "performer_expenses", **{"scope.w2_marks": False}), S1, ["one_w2"]),
 ("military_move", "MAP 2.1 item 15", "A soldier moved to a new permanent post and paid part of the move.", Y("armed_forces", "military_move", **{"scope.reservist_expenses": False}), S1, []),
 ("archer_msa", "MAP 2.1 item 16", "A person put money into an Archer MSA.", Y("archer_msa"), S1, []),
 ("reforestation", "MAP 2.1 item 17 (line 24d)", "A person replanted trees on timber land she owns.", Y("reforestation"), S1, []),
 ("code_h", "MAP 2.1 item 17 (line 24f)", "A person's W-2 shows the code H in box 12.", Y("w2_marks"), S1, ["one_w2"]),
 ("chaplain_403b", "MAP 2.1 item 17 (line 24g; a chaplain is clergy)", "A hospital chaplain paid into a 403(b) plan himself.", Y("religious_work", "clergy"), S1, []),
 ("attorney_fees", "MAP 2.1 item 17 (lines 24h and 24i)", "A person paid a lawyer in a job discrimination case that was settled in 2025.", Y("attorney_fees"), S1, []),
 ("estate_excess_deductions", "MAP 2.1 item 17 (line 24k)", "An heir's Schedule K-1 from an estate shows excess deductions.", Y("k1"), S1, []),
 ("solo_401k", "MAP 2.1 item 12", "A self-employed person pays into a solo 401(k).", Y("se_plan_other"), S1, ["one_business"]),
 # 2.2 scope.other_income
 ("nonresident", "MAP 2.2 item 1", "A person was a nonresident alien for part of 2025.", Y("noncitizen", "nonresident"), OI, []),
 ("green_card_all_year", "MAP 2.2 item 1 (the plain parent does not refuse)", "A person who is not a citizen held a green card all year: the nonresident question is asked and answered No, and the return is prepared.", Y("noncitizen", **{"scope.nonresident": False}), ("proceeds", '{"scope.nonresident": false}'), []),
 ("pay_no_w2", "MAP 2.2 item 2", "A person was paid cash wages for work in a household and got no W-2.", Y("pay_no_w2"), OI, []),
 ("medicaid_waiver", "MAP 2.2 item 3 and 2.1 item 11", "A state Medicaid program pays a person to care for her father in her home.", Y("medicaid_waiver"), OI, []),
 ("adoption_benefits", "MAP 2.2 item 4", "An employer repaid part of the cost of an adoption that became final in 2024.", Y("adoption_benefits", **{"s3.adoption_any": True, "s3.adoption": False, "s3.adoption_earlier": False}), OI, []),
 ("care_benefits_other", "MAP 2.2 item 5", "A person's dependent care benefits are not in box 10 of a W-2.", Y("care_benefits_other", **{"f2441.benefits": True, "f2441.student_disabled": False, "s8812.combat_pay": False, "f2441.employer_care": False, "f2441.line13": 0, "f2441.line14": 0, "f2441.paid_2026": 0, "f2441.plans_differ": False, "f2441.plan_max": 0, "$dcprov": []}), OI, []),
 ("excess_deferral", "MAP 2.2 item 6 (line 1h, excess elective deferrals)", "A person with two jobs put more into 401(k) plans than the yearly limit.", Y("excess_deferral", **{"scope.w2_marks": False, "scope.artist_official": False}), OI, ["one_w2"]),
 ("strike_benefits", "MAP 2.2 item 6 (line 1h)", "A person received strike benefits from a union.", Y("pay_no_w2"), OI, []),
 ("passive", "MAP 2.2 item 7", "A person who owned a rental before 2025 sold her share of a business she did not help run.", Y("business_before", "passive", **{"scope.nol": False}), OI, []),
 ("disaster_distribution", "MAP 2.2 item 8", "A person took a disaster distribution in 2023 and spread its tax over three years.", Y("disaster_distribution"), OI, []),
 ("reservist_repaid", "MAP 2.2 item 9", "A reservist put back into an IRA money taken out when called to active duty.", Y("armed_forces", "reservist_repaid", **{"scope.reservist_expenses": False, "scope.military_move": False}), OI, []),
 ("chapter11", "MAP 2.2 item 10", "A wage earner was in a chapter 11 bankruptcy case in 2025.", Y("chapter11"), OI, []),
 # 2.3 scope.other_line16
 ("f8814", "MAP 2.3 item 1", "A parent puts a child's dividends on the parent's own return.", Y("f8814"), L16, []),
 ("f8615", "MAP 2.3 item 2", "A 20-year-old full-time student with $5,000 of dividends, whose parents support her.", Y("under24", "unearned_2700", "f8615"), L16, []),
 ("under24_small_income", "MAP 2.3 item 2 (the plain parents do not refuse)", "A 22-year-old with no investment income: one more question, and the return is prepared.", Y("under24", **{"scope.unearned_2700": False}), ("proceeds", '{"scope.unearned_2700": false}'), []),
 ("couple_not_asked_age", "MAP 2.3 item 2 (not asked on a joint return)", "A couple filing together is not asked the age question; one of them was in a chapter 11 case.", Y("chapter11", **{"$person": ["taxpayer", "spouse"], "household.married": True}), OI, [], ["scope.under24"]),
 ("sec962", "MAP 2.3 item 3 (an owner of a controlled foreign corporation)", "A person who owns a foreign company makes a section 962 election.", Y("foreign_shares", "cfc", **{"scope.pfic": False}), L16, []),
 ("pfic", "MAP 2.3 items 4 and 5", "A person holds shares of a mutual fund set up in Ireland.", Y("foreign_shares", "pfic"), L16, []),
 ("cfc", "MAP 2.3 item 5", "A person owns shares of a foreign company mostly owned by Americans.", Y("foreign_shares", "cfc", **{"scope.pfic": False}), L16, []),
 ("foreign_shares_plain", "MAP 2.3 item 5 (the plain parent does not refuse)", "A person owns shares of a large foreign car maker: two more questions, and the return is prepared.", Y("foreign_shares", **{"scope.pfic": False, "scope.cfc": False}), ("proceeds", '{"scope.cfc": false}'), []),
 ("lump_sum", "MAP 2.3 item 6 (already caught by retirement.special)", "A person takes a lump-sum distribution reported on Form 4972.", {"$retirement@person[taxpayer]": ["plan"], "person[taxpayer].retirement[plan].account": "plan", "person[taxpayer].retirement[plan].special": True}, "person[taxpayer].retirement[plan].special", []),
 ("f8978", "MAP 2.3 item 7", "A former partner was sent a Form 8986 after an audit of the partnership.", Y("business_before", "f8978", **{"scope.nol": False, "scope.passive": False}), L16, []),
 ("education_recapture", "MAP 2.3 item 8", "A person was refunded tuition for which an education credit was claimed last year.", Y("education_recapture"), L16, []),
 ("income_averaging", "MAP 2.3 item 9", "A self-employed fisher chooses income averaging.", Y("income_averaging", **{"scope.se_plan_other": False}), L16, ["one_business"]),
 ("farm_income_averaging", "MAP 2.3 item 9 (a farmer is refused at the farm question)", "A farmer who would choose income averaging.", Y("farm"), S1, []),
]


def main():
    out = ["tax_year: 2025", "part: The scope screens taken apart", "profile: full", "sets:"]
    for name, (says, answers) in SETS.items():
        out += [f"  {name}:", f"    says: {json.dumps(says)}", "    answers:"]
        out += [f"      {json.dumps(k)}: {json.dumps(v)}" for k, v in answers.items()]
    out.append("rows:")
    for row in ROWS:
        rid, design, situation, answers, end, uses = row[:6]
        out += [f"- id: scope.{rid}", f"  design: {json.dumps(design)}", f"  situation: {json.dumps(situation)}"]
        if uses: out.append(f"  uses: [{', '.join(uses)}]")
        out.append("  answers:")
        out += [f"    {json.dumps(k)}: {json.dumps(v)}" for k, v in answers.items()]
        out.append("  expect:")
        if isinstance(end, tuple): out.append(f"    {end[0]}: {end[1]}")
        else: out.append(f"    refused: {end}")
        if len(row) > 6: out.append(f"    not_asked: [{', '.join(row[6])}]")
    open("interview/2025/coverage/scope.yaml", "w").write("\n".join(out) + "\n")
    print(len(ROWS), "rows")


main()
