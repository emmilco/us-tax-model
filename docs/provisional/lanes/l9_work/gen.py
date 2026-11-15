#!/usr/bin/env python3
"""Lane 9: build the taken-apart scope screens from one table (scratch tool of the provisional redraft).

Run from the worktree root:  python3 docs/provisional/lanes/l9_work/gen.py
It rewrites, always starting from the files as they were at BASE (so it can be run again after the table changes):
  forms/2025/scope.yaml           the three screens become derived lines over the item inputs below
  interview/2025/questions.yaml   the three bank entries become one entry per item (order, seq, help)
  fixtures/2025/defaults.json     a closed default per item
  interview/2025/{sales,stage4}.yaml   the profiles' question lists
  fixtures/**                     inputs only, through refix.py (the map is written to l9_work/refix_map.json)
"""
import json, subprocess, sys

BASE = "100b132c"
CITE = "Form 1040 (2025), lines 8, 10, 13b, 16, 19–20 and 27–31"
SP = "(or, on a joint return, your spouse)"
END = "A Yes ends the interview here: this tool cannot prepare a return with it."
WISH = "This is a choice. A Yes ends the interview here; to go on without it, answer No."

# id, screen (s1 = scope.schedule1, oi = scope.other_income, l16 = scope.other_line16, None = a parent that refuses
# nothing), gate (None, another item's id, or W2 / SC / NOTJOINT / an existing input of another form), order, seq,
# question, help.
ITEMS = [
 # 113: about you
 ("noncitizen", None, None, 113, 1,
  f"At any time in 2025, were you {SP} not a U.S. citizen?", None),
 ("nonresident", "oi", "noncitizen", 113, 2,
  f"For any part of 2025, were you {SP} a nonresident alien, that is, neither a U.S. citizen nor a U.S. resident for tax?",
  "A person who held a green card for all of 2025 was a resident all year. " + END),
 ("chapter11", "oi", None, 113, 3,
  f"At any time in 2025, were you {SP} in a chapter 11 bankruptcy case?",
  "Chapter 11 is the kind of bankruptcy that reorganizes debts; chapter 7 and chapter 13 cases do not count. " + END),
 ("armed_forces", None, None, 113, 4,
  f"Since the start of 2022, did you {SP} serve in the U.S. armed forces, the reserves or the National Guard?", None),
 ("reservist_expenses", "s1", "armed_forces", 113, 5,
  "In 2025, did you travel more than 100 miles from home for reserve or National Guard duty and pay costs that were not paid back?",
  END),
 ("military_move", "s1", "armed_forces", 113, 6,
  "In 2025, did you move to a new permanent post under military orders and pay moving costs that were not paid back?",
  END),
 ("reservist_repaid", "oi", "armed_forces", 113, 7,
  "In 2025, did you put back into an IRA money you had taken out of a retirement plan when you were called to active duty as a reservist?",
  END),
 ("under24", None, "NOTJOINT", 113, 8,
  "Were you under 24 at the end of 2025?", None),
 ("unearned_2700", None, "under24", 113, 9,
  "In 2025, did you have more than $2,700 of income that was not pay for work, such as interest, dividends or gains from investments?",
  "Count everything that is not wages, tips or earnings from your own work: also unemployment pay, taxable scholarships, pensions and income from a trust."),
 ("f8615", "l16", "unearned_2700", 113, 10,
  "At the end of 2025, was a parent of yours alive, and were you either under 18, or 18 (or a full-time student aged 19 to 23) with pay for work of no more than half of what it cost to support you?",
  "This is the tax on a child's investment income (Form 8615), which applies only to a person who has to file a return. " + END),
 # 127: children
 ("f8814", "l16", None, 127, 1,
  f"Are you {SP} reporting a child's 2025 interest or dividends on your own return instead of filing a return for the child?",
  "This is the choice made on Form 8814. A Yes ends the interview here; to go on without it, answer No and file a return for the child."),
 ("adoption_benefits", "oi", "s3.adoption_any", 127, 2,
  f"Did an employer pay or repay any of the adoption costs for you {SP}? Box 12 of a W-2 shows it with the code T.",
  END),
 # 130: income this tool cannot prepare
 ("rental", "s1", None, 130, 1,
  f"In 2025, did you {SP} rent out, or offer for rent, anything you own, such as a house, a room, land, a vehicle or equipment, or receive royalties?",
  END),
 ("k1", "s1", None, 130, 2,
  f"In 2025, did you {SP} have income or a loss from a partnership, an S corporation, an estate or a trust? A paper called Schedule K-1 reports it.",
  END),
 ("farm", "s1", None, 130, 3,
  f"In 2025, did you {SP} have income or a loss from farming?",
  "Count a farm you run and a share of crops or livestock from land you let a farmer use. " + END),
 # 145: jobs, asked of everyone
 ("pay_no_w2", "oi", None, 145, 1,
  f"In 2025, did you {SP} have wages, tips or strike benefits that are not on a W-2?",
  "For example pay for work in someone's home with no W-2, tips you did not report to your employer (or shown only in box 8), pay from a firm that treated you as a contractor although you were its employee, or strike pay from a union. " + END),
 ("medicaid_waiver", "oi", None, 145, 2,
  f"In 2025, did a state Medicaid program pay you {SP} to care for someone who lives in your home?",
  "These are Medicaid waiver payments, also called difficulty of care payments. " + END),
 ("religious_work", None, None, 145, 3,
  f"In 2025, were you {SP} paid for work by a church or other religious body, or for work as clergy (a minister, priest, rabbi or imam)?",
  "Count work for a school, hospital or charity that a church controls, and work as a chaplain."),
 ("clergy", "s1", "religious_work", 145, 4,
  "Was that work as a minister or other clergy (a chaplain too), as a member of a religious order who has not taken a vow of poverty, or as a Christian Science practitioner?",
  END),
 ("church_exempt_wages", "s1", "religious_work", 145, 5,
  "Did a church or church organization pay you wages with no social security or Medicare tax taken out (boxes 4 and 6 of its W-2 are empty)?",
  END),
 # 146: jobs, asked only when a W-2 is listed
 ("w2_marks", "s1", "W2", 146, 1,
  "On any W-2 for 2025, is the 'Statutory employee' box in box 13 ticked, or does box 12 show the code H?",
  END),
 ("artist_official", None, "W2", 146, 2,
  f"In 2025, did you {SP} work as a performing artist, or as a state or local government official who is paid from fees?", None),
 ("performer_expenses", "s1", "artist_official", 146, 3,
  "Did you pay costs for that work that were not paid back, which the rules for a 'qualified performing artist' or an official paid by fees let you deduct?",
  END),
 # 158: care benefits
 ("care_benefits_other", "oi", "f2441.benefits", 158, 1,
  "Were any of those care benefits not shown in box 10 of a W-2 (for example from your own business or a partnership), or carried into 2025 from a 2024 plan under a grace period?",
  END),
 # 168: other money
 ("recovery", "s1", None, 168, 1,
  f"In 2025, were you {SP} paid back an amount you had deducted on an earlier year's return, other than a state income tax refund?",
  "For example a refund of property tax or sales tax, mortgage interest refunded (Form 1098 box 4), a medical bill repaid by insurance, or payment of a bad debt. " + END),
 # 175: retirement money
 ("disaster_distribution", "oi", None, 175, 1,
  f"Did you {SP} take money from a retirement plan in 2023 or 2024 because of a disaster, and spread its tax over three years or pay any of it back in 2025?",
  "This is a qualified disaster recovery distribution (Form 8915-F). " + END),
 # 187: saving for retirement, asked only when a W-2 is listed
 ("excess_deferral", "oi", "W2", 187, 1,
  f"In 2025, did you {SP} put more of your pay into retirement plans at work than the yearly limit ($23,500 for most people)?",
  "The limit is for each person and counts all of that person's jobs together; it is higher from age 50. Box 12 of each W-2 shows the amounts. " + END),
 # 191: health accounts
 ("archer_msa", "s1", None, 191, 1,
  f"In 2025, did you {SP} put money into an Archer MSA (an older kind of medical savings account, not a health savings account)?",
  END),
 # 248: education
 ("education_recapture", "l16", None, 248, 1,
  f"In 2025, were you {SP} refunded tuition, or given tax-free aid, for a year for which an education credit had already been claimed?",
  END),
 # 265: the business, asked only when a business is listed
 ("se_plan_other", "s1", "SC", 265, 1,
  f"In 2025, did you {SP} put money into a retirement plan of your own business other than a SEP or a SIMPLE, such as a solo 401(k)?",
  END),
 ("income_averaging", "l16", "SC", 265, 2,
  f"Is your business fishing, and do you {SP} choose to figure your tax by averaging its income over three years (Schedule J)?",
  WISH),
 # 287: foreign shares
 ("foreign_shares", None, None, 287, 1,
  f"In 2025, did you {SP} own shares of a company or a fund set up outside the United States, other than through a U.S. mutual fund or ETF?",
  "Count shares held for you by a partnership, a trust or another company you own."),
 ("pfic", "l16", "foreign_shares", 287, 2,
  "Was any of it a foreign investment fund, such as a mutual fund or ETF set up outside the United States (a 'passive foreign investment company')?",
  END),
 ("cfc", "l16", "foreign_shares", 287, 3,
  "Was any of it a foreign company in which U.S. owners together hold more than half (a 'controlled foreign corporation')?",
  END),
 # 295: rare situations
 ("reforestation", "s1", None, 295, 1,
  f"Do you {SP} own timber land on which you paid to plant or replant trees, in 2025 or in the seven years before?",
  END),
 ("attorney_fees", "s1", None, 295, 2,
  f"In 2025, did you {SP} pay a lawyer or court costs to win a claim of unlawful discrimination or a whistleblower award?",
  END),
 ("business_before", None, None, 295, 3,
  f"In any year before 2025, did you {SP} own a business, a farm, a rental property, or a share of a partnership or an S corporation?", None),
 ("nol", "s1", "business_before", 295, 4,
  "Are you carrying a loss from an earlier year into 2025 as a 'net operating loss' deduction?",
  "Answer Yes too for such a loss that came from a casualty or theft. " + END),
 ("passive", "oi", "business_before", 295, 5,
  "In 2025, did you have income or a loss from, or sell your share of, a business or rental that you owned but did not help run (a 'passive activity')?",
  END),
 ("f8978", "l16", "business_before", 295, 6,
  "Did a partnership you were in send you a Form 8986 about changes made by an audit?",
  END),
]

SCREENS = {
 "s1": ("scope.schedule1", "Any income or adjustment requiring Schedule 1 other than the ones this tool computes (true when any of the Schedule 1 screening questions is answered Yes)"),
 "oi": ("scope.other_income", "Nonresident alien status, or other income or return treatment outside this tool (true when any of the other-income screening questions is answered Yes)"),
 "l16": ("scope.other_line16", "An additional Form 1040 line 16 tax or filing outside this tool (true when any of the line 16 screening questions is answered Yes)"),
}
GATE_NAME = {"W2": "w2", "SC": "business", "NOTJOINT": "not_joint", "s3.adoption_any": "adoption", "f2441.benefits": "benefits"}
GATE_WORDS = {"W2": "a Form W-2 is listed", "SC": "a business (Schedule C) is listed", "NOTJOINT": "the return is not a joint return",
              "s3.adoption_any": "there was an adoption or adoption costs since the start of 2024", "f2441.benefits": "dependent care benefits were received"}
byid = {i[0]: i for i in ITEMS}


def q(s): return json.dumps(s, ensure_ascii=False)


def scr(item):
    """The screens an item belongs to (most belong to one)."""
    return () if item[1] is None else (item[1],) if isinstance(item[1], str) else item[1]


def gate_id(item):
    g = item[2]
    return None if g is None else f"scope.{item[0]}_if_{GATE_NAME.get(g, g)}"


def reads(item):
    """The line a reader of this item reads: its gate line when it has one."""
    return gate_id(item) or f"scope.{item[0]}"


def test_eq(ref, val, ind):
    c = "true" if val is True else "false" if val is False else val
    return f"{ind}op: test\n{ind}eq:\n{ind}  - {ref}\n{ind}  - const: {c}\n"


def cite(): return f"      cite:\n        doc: f1040\n        locator: {q(CITE)}\n"


def lines():
    out = []
    out.append("    - id: scope.no\n      printed: (helper)\n      type: Bool\n      label: Year parameter household.no (false)\n"
               "      expr:\n        op: param\n        ref: household.no\n" + cite())
    out.append("    - id: scope.w2_count\n      printed: (helper)\n      type: Count\n      label: Number of Forms W-2 on the return\n"
               "      expr:\n        op: sum_over\n        collection: person\n        field: person.employers\n" + cite())
    out.append("    - id: scope.has_w2\n      printed: (helper)\n      type: Bool\n      label: The return has a Form W-2\n"
               "      expr:\n        op: test\n        gt:\n          - scope.w2_count\n          - const: 0\n            type: Count\n" + cite())
    for it in ITEMS:
        name, screen, g, order, seq, text, help_ = it
        gid = gate_id(it)
        s = f"    - id: scope.{name}\n      printed: (helper)\n      type: Bool\n"
        # Nor is the care-benefits child: marking it would make `f2441.benefits` an existence gate that interview-rules
        # opens alone, and that walk fails on a question of Form 2441 itself (see the lane notes).
        # A question hidden by the filing status is not marked: the marker is for existence gates, which the minimal
        # return (interview-rules) keeps closed, and a single filer's status opens this one.
        if gid and g not in ("NOTJOINT", "f2441.benefits"): s += f"      gated_by: {gid}\n"
        s += f"      label: {q(text)}\n      expr:\n        op: input\n        source: {q(text)}\n" + cite()
        out.append(s)
        if not gid: continue
        s = f"    - id: {gid}\n      printed: (gate)\n      type: Bool\n"
        cond = GATE_WORDS.get(g) or f"the question {('scope.' + g)} is answered Yes"
        s += f"      label: {q('The answer to scope.' + name + ', asked only when ' + cond + ' (false otherwise)')}\n"
        s += "      expr:\n        op: choose\n        alternatives:\n"
        def alt(ref, val, then):
            return "        - guard:\n" + test_eq(ref, val, "            ") + f"          then: {then}\n"
        me = f"scope.{name}"
        if g == "NOTJOINT":
            for st in ("single", "hoh", "qss", "mfs"): s += alt("f1040.status", st, me)
            s += alt("f1040.status", "mfj", "scope.no")
        else:
            ref = {"W2": "scope.has_w2", "SC": "s1.has_sc"}.get(g) or (g if "." in g else reads(byid[g]))
            s += alt(ref, True, me) + alt(ref, False, "scope.no")
        out.append(s + cite())
    for key, (sid, label) in SCREENS.items():
        s = f"    - id: {sid}\n      printed: (helper)\n      type: Bool\n      label: {q(label)}\n      expr:\n        op: test\n        any:\n"
        for it in ITEMS:
            if key in scr(it): s += "          - " + test_eq(reads(it), True, "            ").lstrip()
        out.append(s + cite())
    return "".join(out)


def ready(tail):
    """scope.ready: each screen's refusal on a line of its own, and the credits refusals together on a fourth.

    A line's refusal entries are tried in order and an unanswered gate stops the list (eval.ts), so with the three
    screens first on one line a Yes to an item of one screen would wait for every item of the screens before it, and
    every later refusal (married filing separately, the credits) for every item of all three. `all` over lines passes
    a refusal on at once whatever else is unanswered. The entries themselves (gate, form, remedy, citation) are
    unchanged, and the first refusing operand is the one the single list would have reported.
    """
    head, rest = tail.split("      refuses:\n", 1)
    entries = ["        - when: " + e for e in rest.split("        - when: ")[1:]]
    c = head[head.index("      cite:\n"):]
    assert entries[0].startswith("        - when: scope.schedule1\n") and entries[1].startswith("        - when: scope.other_income\n") and entries[2].startswith("        - when: scope.other_line16\n")
    def helper(name, label, es):
        return (f"    - id: scope.{name}\n      printed: (helper)\n      type: Bool\n      label: {q(label)}\n"
                "      expr:\n        op: test\n        eq:\n          - const: true\n          - const: true\n" + c + "      refuses:\n" + "".join(es))
    out = helper("ready_schedule1", "The Schedule 1 screening questions passed", entries[0:1])
    out += helper("ready_other_income", "The other-income screening questions passed", entries[1:2])
    out += helper("ready_other_line16", "The line 16 screening questions passed", entries[2:3])
    out += helper("ready_credits", "The filing status and credits screening questions passed", entries[3:])
    out += ("    - id: scope.ready\n      printed: (helper)\n      type: Bool\n      label: All declared scope screens passed\n"
            "      expr:\n        op: test\n        all:\n")
    for n in ("ready_schedule1", "ready_other_income", "ready_other_line16", "ready_credits"):
        out += "          - " + test_eq("scope." + n, True, "            ").lstrip()
    return out + c


def base(path): return subprocess.run(["git", "show", f"{BASE}:{path}"], capture_output=True, text=True, check=True).stdout


def main():
    inputs = [f"scope.{i[0]}" for i in ITEMS]
    # the form
    s = base("forms/2025/scope.yaml")
    a = s.index("    - id: scope.schedule1\n"); b = s.index("    - id: scope.ready\n")
    open("forms/2025/scope.yaml", "w").write(s[:a] + lines() + ready(s[b:]))
    # the bank
    s = base("interview/2025/questions.yaml")
    a = s.index("  - input: scope.schedule1\n"); b = s.index("  - input: sd.other_forms\n")
    bank = ""
    for name, screen, g, order, seq, text, help_ in ITEMS:
        bank += f"  - input: scope.{name}\n    order: {order}\n    seq: {seq}\n"
        if help_: bank += f"    help: {q(help_)}\n"
    open("interview/2025/questions.yaml", "w").write(s[:a] + bank + s[b:])
    # defaults
    d = json.loads(base("fixtures/2025/defaults.json"))
    reason = next(x["reason"] for x in d["defaults"] if x["input"] == "scope.schedule1")
    old = {v[0] for v in SCREENS.values()}
    at = next(i for i, x in enumerate(d["defaults"]) if x["input"] in old)
    d["defaults"] = [x for x in d["defaults"] if x["input"] not in old]
    d["defaults"][at:at] = [{"input": i, "value": False, "reason": reason} for i in sorted(inputs)]
    open("fixtures/2025/defaults.json", "w").write(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
    # profiles
    for p in ("interview/2025/sales.yaml", "interview/2025/stage4.yaml"):
        s = base(p); done = False; out = []
        for ln in s.split("\n"):
            if ln.strip()[2:] in old and ln.startswith("  - "):
                if not done: out += [f"  - {i}" for i in inputs]; done = True
                continue
            out.append(ln)
        if p.endswith("sales.yaml") and "  - s3.adoption_any" not in out: out.insert(out.index(f"  - {inputs[0]}"), "  - s3.adoption_any")
        open(p, "w").write("\n".join(out))
    # fixtures
    # A screen left unanswered (null) in a fixture: its own items are unanswered. The plain parents are shared by
    # items of several screens, so they keep their defaults (an item beneath a parent answered No is then false).
    def allof(k): return [f"scope.{i[0]}" for i in ITEMS if k in scr(i)]
    yes = lambda *names: {f"scope.{n}": True for n in names}
    m = {"parents": [f"scope.{i[0]}" for i in ITEMS if i[1] is None],
         "set_inputs": {"mutation.t2.no_itemize_f8960_9a": {"s3.adoption_any": False}},
         "rename_unknown": {"stage9.eic.refuse.other_income.schedule1_unanswered": {"scope.schedule1": "scope.rental"}},
         "screens": {
            "scope.schedule1": {"items": allof("s1"), "default_true": yes("rental")},
            "scope.other_income": {"items": allof("oi"), "default_true": yes("chapter11")},
            "scope.other_line16": {"items": allof("l16"), "default_true": yes("f8814")}},
         "drop_nulls": ["stage4.refuse.scope.schedule1", "stage4.refuse.scope.other_income", "stage4.refuse.scope.other_line16", "stage5.refuse.other_income"],
         "cases": {
            "stage9.eic.refuse.clergy_schedule1": {"scope.schedule1": yes("religious_work", "clergy")},
            "stage9.eic.refuse.clergy_schedule1.step5": {"scope.schedule1": yes("religious_work", "clergy")},
            "stage9.eic.refuse.other_income": {"scope.other_income": yes("medicaid_waiver")},
            "stage9.eic.refuse.other_income.schedule1_unanswered": {"scope.other_income": yes("noncitizen", "nonresident")},
            "stage5.refuse.other_income": {"scope.other_income": yes("noncitizen", "nonresident")},
            "stage4.refuse.scope.other_income": {"scope.other_income": yes("noncitizen", "nonresident")},
            "stage12.refuse.tips_trade_or_business": {"scope.schedule1": yes("k1")},
            "stage12.refuse.overtime_nonemployee": {"scope.schedule1": yes("k1")},
            "stage8.refuse.s8812.schedule1": {"scope.schedule1": yes("farm")},
            "stage10.ss.refuse.schedule1": {"scope.schedule1": yes("archer_msa")},
            "scope.ch11.wage_only_debtor": {"scope.other_income": yes("chapter11")},
            "scope.ch11.mfj_spouse_debtor": {"scope.other_income": yes("chapter11")},
            "stage9.eic.refuse.form8814": {"scope.other_line16": yes("f8814")},
            "t264.eic.step2_schedule1": {"scope.schedule1": yes("rental")},
         }}
    json.dump(m, open("docs/provisional/lanes/l9_work/refix_map.json", "w"), indent=1)
    fx = subprocess.run(["git", "ls-tree", "-r", "--name-only", BASE, "fixtures/"], capture_output=True, text=True, check=True).stdout.split()
    subprocess.run(["git", "checkout", BASE, "--"] + [f for f in fx if not f.endswith("defaults.json")], check=True)
    subprocess.run(["git", "reset", "-q", "--"] + fx, check=True)
    print(subprocess.run([sys.executable, "docs/provisional/lanes/l9_work/refix.py", "docs/provisional/lanes/l9_work/refix_map.json", "--write"], capture_output=True, text=True).stdout)
    n = [i for i in ITEMS if i[2] is None]
    print(len(ITEMS), "inputs;", len(n), "asked of everyone,", sum(len(i[5].split()) for i in n), "words")


main()
