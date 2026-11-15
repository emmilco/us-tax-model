"""Lane m3: the table of mutation cases, written to cases.json for gen_cases.mjs.

One case per item of each derived screen (a filer with that item alone Yes, every other item No, expecting the
refusal the screen gives), plus the cases for the gate lines. Each row: id, base case, inputs set and dropped,
expected lines with the value predicted by hand from the line and the source, the covered lines, and the note.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
rows = []

B0 = "mutation.sb.form5471_refuses"   # single, two W-2s, interest and dividends, every scope screen No
B0_OFF = {"sb.account_any": False, "sb.company_any": False, "sb.form5471": False}
B0_DESC = ("inputs of mutation.sb.form5471_refuses (single, two Forms W-2, interest and dividends) with the "
           "foreign-account and foreign-company screens answered No (no foreign account, no Form 5471), so every "
           "Schedule B and scope screen is No")
BIZ = "mutation.t2.person.ira_se_comp"  # single, one Schedule C, every scope screen No
BIZ_DESC = "inputs of mutation.t2.person.ira_se_comp (single, one Schedule C business), every scope screen No"
CARE = "mutation.t2.hoh_no_s1a_parts"   # head of household, dependent care benefits received
CARE_DESC = ("inputs of mutation.t2.hoh_no_s1a_parts (head of household, dependent care benefits on Form W-2 box 10), "
             "every scope screen No")

SCREEN = {
    "scope.schedule1": ("scope.ready_schedule1", "Schedule 1 screen"),
    "scope.other_income": ("scope.ready_other_income", "other-income screen"),
    "scope.other_line16": ("scope.ready_other_line16", "line 16 screen"),
}


def scope_row(slug, screen, item, set_, base=B0, base_desc=B0_DESC, extra_expect=None, drop=None, why=""):
    ready, name = SCREEN[screen]
    s = dict(B0_OFF) if base == B0 else {}
    s.update(set_)
    expect = {ready: {"refusal": screen}}
    expect.update(extra_expect or {})
    answers = ", ".join(f"{k} {'Yes' if v is True else 'No' if v is False else v}" for k, v in set_.items())
    rows.append({
        "id": f"mutation.m3.scope.{slug}",
        "base": base,
        "set": s,
        "drop": drop or [],
        "covers": ["scope", screen],
        "expect": expect,
        "note": (f"Mutation fixture for the {name} ({screen}, a derived line true when any of its items is Yes): "
                 f"{base_desc}; then {answers}{why}. Predicted by hand from {screen}'s expression before running "
                 f"the evaluator: {item} is Yes, so {screen} is true and {ready} refuses on it, with the form, remedy "
                 f"and citation that line states; that is this tool's way of declining a return the instructions "
                 f"send to a form it does not prepare. A mutant that drops {item} from the screen gives no refusal."),
    })


# Schedule 1 screen items (the survivors' item positions 0, 1, 6, 7, 8, 9, 11, 12, 13, 14)
scope_row("s1_reservist_expenses", "scope.schedule1", "scope.reservist_expenses_if_armed_forces",
          {"scope.armed_forces": True, "scope.reservist_expenses": True})
scope_row("s1_military_move", "scope.schedule1", "scope.military_move_if_armed_forces",
          {"scope.armed_forces": True, "scope.military_move": True})
scope_row("s1_church_exempt_wages", "scope.schedule1", "scope.church_exempt_wages_if_religious_work",
          {"scope.religious_work": True, "scope.church_exempt_wages": True})
scope_row("s1_w2_marks", "scope.schedule1", "scope.w2_marks_if_w2", {"scope.w2_marks": True})
scope_row("s1_performer_expenses", "scope.schedule1", "scope.performer_expenses_if_artist_official",
          {"scope.artist_official": True, "scope.performer_expenses": True})
scope_row("s1_recovery", "scope.schedule1", "scope.recovery", {"scope.recovery": True})
scope_row("s1_se_plan_other", "scope.schedule1", "scope.se_plan_other_if_business",
          {"scope.se_plan_other": True}, base=BIZ, base_desc=BIZ_DESC)
scope_row("s1_reforestation", "scope.schedule1", "scope.reforestation", {"scope.reforestation": True})
scope_row("s1_attorney_fees", "scope.schedule1", "scope.attorney_fees", {"scope.attorney_fees": True})
scope_row("s1_nol", "scope.schedule1", "scope.nol_if_business_before",
          {"scope.business_before": True, "scope.nol": True})

# Other-income screen items (positions 2, 3, 4, 6, 7, 8, 9)
scope_row("oi_reservist_repaid", "scope.other_income", "scope.reservist_repaid_if_armed_forces",
          {"scope.armed_forces": True, "scope.reservist_repaid": True})
scope_row("oi_adoption_benefits", "scope.other_income", "scope.adoption_benefits_if_adoption",
          {"s3.adoption_any": True, "scope.adoption_benefits": True})
scope_row("oi_pay_no_w2", "scope.other_income", "scope.pay_no_w2", {"scope.pay_no_w2": True})
scope_row("oi_care_benefits_other", "scope.other_income", "scope.care_benefits_other_if_benefits",
          {"scope.care_benefits_other": True}, base=CARE, base_desc=CARE_DESC)
scope_row("oi_disaster_distribution", "scope.other_income", "scope.disaster_distribution",
          {"scope.disaster_distribution": True})
scope_row("oi_excess_deferral", "scope.other_income", "scope.excess_deferral_if_w2", {"scope.excess_deferral": True})
scope_row("oi_passive", "scope.other_income", "scope.passive_if_business_before",
          {"scope.business_before": True, "scope.passive": True})

# Line 16 screen items (positions 0, 2, 3, 4, 5, 6); the Form 8615 case also kills the single branch of
# scope.under24_if_not_joint.
scope_row("l16_f8615_single", "scope.other_line16", "scope.f8615_if_unearned_2700",
          {"person[taxpayer].birth_year": 2004, "scope.unearned_2700": True, "scope.f8615": True},
          why=" (born in 2004, so under 24 at the end of 2025, and filing single, so scope.under24_if_not_joint is true)")
scope_row("l16_education_recapture", "scope.other_line16", "scope.education_recapture",
          {"scope.education_recapture": True})
scope_row("l16_income_averaging", "scope.other_line16", "scope.income_averaging_if_business",
          {"scope.income_averaging": True}, base=BIZ, base_desc=BIZ_DESC)
scope_row("l16_pfic", "scope.other_line16", "scope.pfic_if_foreign_shares",
          {"scope.foreign_shares": True, "scope.pfic": True})
scope_row("l16_cfc", "scope.other_line16", "scope.cfc_if_foreign_shares",
          {"scope.foreign_shares": True, "scope.cfc": True})
scope_row("l16_f8978", "scope.other_line16", "scope.f8978_if_business_before",
          {"scope.business_before": True, "scope.f8978": True})

# scope.under24_if_not_joint: one case per status branch.
U24 = {"person[taxpayer].birth_year": 2004, "scope.unearned_2700": True, "scope.f8615": True}
scope_row("l16_f8615_hoh", "scope.other_line16", "scope.f8615_if_unearned_2700", U24, base=CARE, base_desc=CARE_DESC,
          why=" (born in 2004, so under 24 at the end of 2025, and filing as head of household, so scope.under24_if_not_joint is true)")
scope_row("l16_f8615_qss", "scope.other_line16", "scope.f8615_if_unearned_2700", U24, base="mutation.t2.qss_s1a_tips_ot_car",
          base_desc="inputs of mutation.t2.qss_s1a_tips_ot_car (qualifying surviving spouse), every scope screen No",
          why=" (born in 2004, so under 24 at the end of 2025, and filing as qualifying surviving spouse, so scope.under24_if_not_joint is true)")
scope_row("l16_f8615_mfs", "scope.other_line16", "scope.f8615_if_unearned_2700", U24, base="mutation.t2.mfs_sli_line5",
          base_desc="inputs of mutation.t2.mfs_sli_line5 (married filing separately), every scope screen No",
          why=" (born in 2004, so under 24 at the end of 2025, and filing separately, so scope.under24_if_not_joint is true)")

# scope.under24_if_not_joint, joint branch: never asked on a joint return, so the two questions beneath it are left
# unanswered; the line 16 screen is still complete (false), and the Schedule 1 refusal comes from the reservist item.
rows.append({
    "id": "mutation.m3.scope.l16_joint_unasked",
    "base": "mutation.t2.mfj_no_trad_ira",
    "set": {"scope.armed_forces": True, "scope.reservist_repaid": True},
    "drop": ["scope.unearned_2700", "scope.f8615"],
    "covers": ["scope", "scope.under24_if_not_joint", "scope.other_line16"],
    "expect": {"scope.ready_other_income": {"refusal": "scope.other_income"}, "scope.ready_other_line16": {"bool": True}},
    "note": ("Mutation fixture for the joint-return branch of scope.under24_if_not_joint: inputs of "
             "mutation.t2.mfj_no_trad_ira (married filing jointly), every scope screen No, then scope.armed_forces Yes "
             "and scope.reservist_repaid Yes; scope.unearned_2700 and scope.f8615 are left unanswered, as the interview "
             "never asks them on a joint return (they sit beneath scope.under24_if_not_joint, false for a joint return). "
             "Predicted by hand from the scope lines before running the evaluator: scope.other_income is true (a "
             "repayment of a qualified reservist distribution), so scope.ready_other_income refuses on it with the "
             "form, remedy and citation that line states; scope.other_line16 is false with every item known, so "
             "scope.ready_other_line16 is true. A mutant that reads another line than scope.no on the joint branch "
             "reaches the unanswered questions and leaves the line 16 screen unknown."),
})

# Schedule B: the foreign-accounts screen (sb.foreign_any) and the two narrower screens beneath it.
SB_ALL_NO = {"sb.account_any": False, "sb.asset_any": False, "sb.trust_any": False, "sb.company_any": False,
             "sb.territory_any": False, "sb.fbar_required": False, "sb.form8938": False, "sb.line8": False,
             "sb.form5471": False}
SB_SRC = ("i1040sb p. 2, Part III, lines 7a, 7b and 8, and the TIPs on Forms 114, 8938, 3520 and 5471")


def sb_row(slug, set_, expect, why, drop=()):
    s = dict(SB_ALL_NO)
    s.update(set_)
    rows.append({
        "id": f"mutation.m3.sb.{slug}",
        "base": B0,
        "set": s,
        "drop": list(drop),
        "covers": ["sb", "sb.foreign_any"],
        "expect": expect,
        "note": ("Mutation fixture for the Schedule B foreign screens: inputs of mutation.sb.form5471_refuses (single, "
                 "taxable interest of $1,200 from one payer, ordinary dividends) with " + why + ". Predicted by hand "
                 "from the Schedule B lines and " + SB_SRC + " before running the evaluator."),
    })


REF = lambda gate: {"sb.line2": {"refusal": gate}}
for item, what in [("sb.asset_any", "another foreign financial asset"), ("sb.trust_any", "a connection to a foreign trust"),
                   ("sb.company_any", "a role in or 10% of a foreign company"),
                   ("sb.territory_any", "an account, investment, company or trust in a U.S. territory")]:
    slug = item.split(".")[1].replace("_any", "") + "_8938"
    sb_row(slug, {item: True, "sb.form8938": True}, REF("sb.form8938_if_foreign"),
           f"only {item} Yes ({what}) of the five foreign screens and Form 8938 required Yes (every other Schedule B "
           f"question No): sb.foreign_any is true, so sb.form8938_if_foreign is the Form 8938 answer, Yes, and Schedule "
           f"B line 2 refuses on it (the form, remedy and citation are those the line states); a mutant that drops "
           f"{item} from sb.foreign_any leaves Form 8938 unread and line 2 at $1,200")
sb_row("account_only_unasked", {"sb.account_any": True}, {"sb.line2": {"money": 120000}},
       "only sb.account_any Yes (a foreign account) of the five foreign screens, FBAR and Form 8938 No, and the Form "
       "3520 question (line 8) and the Form 5471 question left unanswered, as the interview asks them only after a "
       "foreign trust, a foreign company or a U.S. territory answer: nothing refuses and Schedule B line 2 is the "
       "$1,200 of interest; a mutant that asks line 8 or Form 5471 of this filer leaves line 2 unknown",
       drop=["sb.line8", "sb.form5471"])
sb_row("trust_only_unasked", {"sb.trust_any": True}, {"sb.line2": {"money": 120000}},
       "only sb.trust_any Yes (a connection to a foreign trust), FBAR, Form 8938 and line 8 No, and the Form 5471 "
       "question left unanswered, as the interview asks it only after a foreign company or a U.S. territory answer: "
       "nothing refuses and Schedule B line 2 is $1,200; a mutant that asks Form 5471 of this filer leaves line 2 unknown",
       drop=["sb.form5471"])

# Schedule D "other forms" screen (sd.other_forms, a derived line over nine items); sd.count refuses on it.
SOLD = {"sd.business_property": False, "sd.installment": False, "sd.like_kind": False}
for item, set_, what in [
    ("sd.business_property_if_sold", {"sd.sold_other": True, **SOLD, "sd.business_property": True}, "business property sold (Form 4797)"),
    ("sd.installment_if_sold", {"sd.sold_other": True, **SOLD, "sd.installment": True}, "an installment sale (Form 6252)"),
    ("sd.like_kind_if_sold", {"sd.sold_other": True, **SOLD, "sd.like_kind": True}, "a like-kind exchange (Form 8824)"),
    ("sd.condemned", {"sd.condemned": True}, "property condemned or sold under threat of condemnation"),
    ("sd.small_business_stock", {"sd.small_business_stock": True}, "qualified small business stock"),
    ("sd.trader_election", {"sd.trader_election": True}, "a trader's mark-to-market election"),
    ("sd.f2439_if_dividends", {"sd.f2439": True}, "a Form 2439 (undistributed capital gains of a fund)"),
    ("sd.casualty", {"sd.casualty": True}, "a casualty or theft (Form 4684)"),
]:
    slug = item.split(".")[1].replace("_if_sold", "").replace("_if_dividends", "")
    rows.append({
        "id": f"mutation.m3.sd.other_forms_{slug}",
        "base": B0,
        "set": {**B0_OFF, **set_},
        "covers": ["sd", "sd.other_forms"],
        "expect": {"sd.count": {"refusal": "sd.other_forms"}},
        "note": (f"Mutation fixture for the Schedule D other-forms screen (sd.other_forms, a derived line true when any "
                 f"of its nine items is Yes): {B0_DESC}; then {item} Yes ({what}) and every other item of the screen No. "
                 f"Predicted by hand from sd.other_forms's expression before running the evaluator: the screen is true, "
                 f"so sd.count refuses on it, with the form, remedy and citation that line states (f1040sd, the gains "
                 f"belong on a source form this tool does not prepare). A mutant that drops {item} from the screen gives "
                 f"no refusal."),
    })

# Schedule B special treatment: nominee interest alone (sb.unsupported_if_income copies sb.unsupported).
sb_row("nominee", {"sb.nominee": True}, {"sb.line2": {"refusal": "sb.unsupported_if_income"}},
       "every foreign screen No and sb.nominee Yes (interest or dividends received as a nominee; taxable interest is "
       "above zero, so the question is asked): sb.unsupported is true through its nominee item and Schedule B line 2 "
       "refuses on sb.unsupported_if_income (i1040sb p. 1, Nominees; the form, remedy and citation are those the line "
       "states); a mutant that copies only the bond item gives no refusal")

# Form 1099-DIV boxes behind the box 1a and box 2a gates.
DIV_NOTE = ("Mutation fixture for the Form 1099-DIV gates: inputs of mutation.sb.form5471_refuses (single; ordinary "
            "dividends of $2,000 and no capital gain distributions, box 2a $0) with the foreign screens answered No, "
            "and the question 'does any Form 1099-DIV show an amount in box 2b, 2c, 2d, 2e, 2f, 3, 9, 10 or 13' "
            "answered Yes; {rest}. The capital-gain boxes 2b, 2c, 2d and 2f are left unanswered: the interview asks "
            "them only when box 2a is above zero (div.capital_gain_boxes). Predicted by hand from the div lines and "
            "the Form 1099-DIV instructions (i1099div boxes 2a to 3, 9, 10 and 13) before running the evaluator: {pred}")
DIV_BASE = {**B0_OFF, "div.other_boxes": True, "div.box2e": 0, "div.box3": 0, "div.box9": 0, "div.box10": 0, "div.box13": 0}
DIV_DROP = ["div.box2b", "div.box2c", "div.box2d", "div.box2f"]
rows.append({"id": "mutation.m3.div.boxes_no_capital_gain", "base": B0, "set": DIV_BASE, "drop": DIV_DROP + ["div.basis_reconciled"],
             "covers": ["div", "div.has_capital_gain"], "expect": {"div.screen": {"money": 0}},
             "note": DIV_NOTE.format(rest="boxes 2e, 3, 9, 10 and 13 are $0 and the basis question for box 3 is left "
                                     "unanswered (asked only when box 3 is above zero)",
                                     pred="no distribution needs a form this tool does not prepare, so the distribution "
                                     "screen div.screen is $0. A mutant that asks the capital-gain boxes at a $0 box 2a "
                                     "leaves it unknown.")})
rows.append({"id": "mutation.m3.div.return_of_capital_no_capital_gain", "base": B0,
             "set": {**DIV_BASE, "div.box3": 30000, "div.basis_reconciled": True}, "drop": DIV_DROP,
             "covers": ["div", "div.capital_gain_boxes"], "expect": {"div.screen": {"money": 0}},
             "note": DIV_NOTE.format(rest="a nondividend distribution (box 3) of $300, no more than the remaining basis, "
                                     "and boxes 2e, 9, 10 and 13 $0",
                                     pred="a return of capital within basis is not taxed and needs no other form "
                                     "(i1099div box 3), so div.screen is $0. A mutant that asks the capital-gain boxes "
                                     "because box 3 is above zero leaves it unknown.")})
rows.append({"id": "mutation.m3.div.box2e_no_capital_gain", "base": B0,
             "set": {**DIV_BASE, "div.box2e": 10000}, "drop": DIV_DROP + ["div.basis_reconciled"],
             "covers": ["div", "div.ordinary_boxes"], "expect": {"div.screen": {"refusal": "div.unsupported"}},
             "note": DIV_NOTE.format(rest="section 897 ordinary dividends (box 2e) of $100, boxes 3, 9, 10 and 13 $0 "
                                     "and the basis question for box 3 unanswered",
                                     pred="box 2e is asked (ordinary dividends are above zero) and is above zero, so "
                                     "div.unsupported is true and div.screen refuses on it (the form, remedy and "
                                     "citation are those the line states). A mutant that asks box 2e only with capital "
                                     "gain distributions leaves box 2e unread and gives no refusal.")})

# Form 1040 lines 25b to 25d.
rows.append({"id": "mutation.m3.f1040.withholding_25b_25c", "base": B0,
             "set": {**B0_OFF, "f1040.withheld_other_any": True, "f1040.line25b": 30000, "f1040.line25c_other": 20000},
             "covers": ["f1040.line25c", "f1040.line25d"],
             "expect": {"f1040.line25b_if_withheld_other": {"money": 30000}, "f1040.line25c": {"money": 20000},
                        "f1040.line25d": {"money": 1750000}},
             "note": ("Mutation fixture for Form 1040 lines 25b to 25d: inputs of mutation.sb.form5471_refuses "
                      "(single; Forms W-2 with federal income tax withheld of $12,000 and $5,000, social security and "
                      "Medicare wages of $120,000 in all) with the foreign screens answered No, tax withheld from a "
                      "payment other than wages Yes, $300 withheld on Forms 1099 (line 25b) and $200 on a Form W-2G "
                      "(other forms, line 25c). Predicted by hand from the archived i1040gi (p. 39, lines 25a to 25d; "
                      "Form 8959 line 24) before running the evaluator: line 25a is $17,000; line 25b $300; Form 8959 "
                      "line 24 is $0 (Medicare tax withheld, $1,740, is 1.45% of the $120,000 of Medicare wages, so no "
                      "additional Medicare tax was withheld), so line 25c is $200; line 25d is $17,500. A mutant that "
                      "swaps the 25b and 25c amounts gives $300 on line 25c or $17,400 on line 25d.")})

# State and local refund worksheet: no worksheet when the 2024 return deducted sales taxes.
rows.append({"id": "mutation.m3.refund.sales_tax_2024", "base": "mutation.t2.refund.single_blind",
             "set": {"refund.sales": True}, "covers": ["refund", "s1.line1"],
             "expect": {"refund.worksheet": {"bool": False}, "s1.line1": {"money": 0}},
             "note": ("Mutation fixture for the refund worksheet's sales-tax test: inputs of "
                      "mutation.t2.refund.single_blind (a $3,000 state refund, itemized for 2024, the refund for 2024 "
                      "and the 2024 tax paid in 2024) with 'On your 2024 Schedule A, did you deduct state and local "
                      "general sales taxes instead of state and local income taxes' answered Yes; the worksheet "
                      "answers of the base are kept and are not read. Predicted by hand from the archived i1040gi "
                      "before running the evaluator: p. 88, 'None of your refund is taxable if, in the year you paid "
                      "the tax, you either (a) didn't itemize deductions, or (b) elected to deduct state and local "
                      "general sales taxes', so the worksheet is not used and Schedule 1 line 1 is $0. A mutant that "
                      "tests another answer in place of the sales-tax one uses the worksheet and taxes the refund.")})

# Schedule 2: incentive stock options alone make Form 6251 required.
rows.append({"id": "mutation.m3.s2.iso_amt", "base": B0,
             "set": {**B0_OFF, "s2.options_any": True, "s2.iso": True, "s1.stock_options": False},
             "covers": ["s2", "s2.amt"], "expect": {"s2.line2": {"refusal": "s2.amt"}},
             "note": ("Mutation fixture for the Schedule 2 AMT screen (s2.amt, a derived line over two items): inputs "
                      "of mutation.sb.form5471_refuses with the foreign screens answered No, employer stock options "
                      "exercised Yes, incentive stock options exercised in 2025 with the stock kept Yes, and stock "
                      "option income not otherwise reported No; the AMT-owed question stays No. Predicted by hand from "
                      "the archived i6251 (p. 1, Who Must File, an adjustment for incentive stock options, line 2i) "
                      "before running the evaluator: s2.amt is true through the incentive stock option item and "
                      "Schedule 2 line 2 refuses on it (Form 6251; the form, remedy and citation are those the line "
                      "states). A mutant that drops that item from s2.amt gives no refusal.")})

# Mortgage-interest gates at line 8a $0 with a positive line 5c: the mortgage questions are not asked.
rows.append({"id": "mutation.m3.sa.no_mortgage_property_tax", "base": B0,
             "set": {**B0_OFF, "sa.personal_property_tax_any": True, "sa.line5c": 50000},
             "drop": ["sa.mortgage_over_limit", "sa.mortgage_other_use", "s2.mortgage_subsidy"],
             "covers": ["sa", "sa.has_mortgage_interest", "s2.has_mortgage_interest"],
             "expect": {"sa.line5c_if_taxed": {"money": 50000}, "sa.line8a": {"money": 0},
                        "sa.line15": {"money": 0}, "s2.line2": {"money": 0}},
             "note": ("Mutation fixture for the mortgage-interest gates of Schedules A and 2: inputs of "
                      "mutation.sb.form5471_refuses (single, owns no home or other real estate and pays no interest on "
                      "a loan secured by a home) with the foreign screens answered No and state and local personal "
                      "property tax of $500 paid. The three questions asked only when home mortgage interest is "
                      "entered (more than the Form 1098 limits, proceeds used otherwise, a subsidized mortgage on a "
                      "home sold) are left unanswered. Predicted by hand from the Schedule A and Schedule 2 lines "
                      "before running the evaluator: line 5c is $500, line 8a $0, so nothing refuses: Schedule A line "
                      "15 (casualty, none) is $0 and Schedule 2 line 2 is $0. A mutant that asks a mortgage question "
                      "at line 8a $0, or tests line 5c in place of line 8a, leaves those lines unknown.")})

# Schedule A medical premiums asked when costs were not said to be large; a charity carryover with no gifts.
rows.append({"id": "mutation.m3.sa.medical_premiums", "base": B0,
             "set": {**B0_OFF, "sa.medical_any": False, "sa.medical_premiums": True, "sa.line1": 300000},
             "covers": ["sa", "sa.medical_asked"], "expect": {"sa.line1_if_medical": {"money": 300000}},
             "note": ("Mutation fixture for the Schedule A medical questions: inputs of mutation.sb.form5471_refuses "
                      "(single, born in 1980) with the foreign screens answered No, medical and dental costs not said "
                      "to be more than 7.5% of income, health insurance paid with money already taxed Yes, and $3,000 "
                      "of medical and dental expenses. Predicted by hand from the Schedule A lines and i1040sca (p. 1, "
                      "Line 1, insurance premiums you paid) before running the evaluator: the expenses are asked and "
                      "Schedule A line 1 is $3,000. A mutant that tests the age question in place of the premiums "
                      "answer (the filer is under 65) gives line 1 $0.")})
rows.append({"id": "mutation.m3.sa.carryover_no_gifts", "base": B0,
             "set": {**B0_OFF, "sa.gifts": False, "sa.gift_carryover": True}, "drop": ["sa.charity_limited"],
             "covers": ["sa", "sa.line13", "sa.line15"],
             "expect": {"sa.line13": {"refusal": "sa.gift_carryover_if_no_gifts"}, "sa.line15": {"money": 0}},
             "note": ("Mutation fixture for the charitable carryover with no gifts in 2025: inputs of "
                      "mutation.sb.form5471_refuses with the foreign screens answered No, no gifts to charity in 2025 "
                      "and a charitable contribution carried over from an earlier year Yes; the question about income "
                      "limits on 2025 gifts is left unanswered (asked only with gifts). Predicted by hand from the "
                      "Schedule A lines and i1040sca (p. 13, Line 13, Carryover From Prior Year) before running the "
                      "evaluator: Schedule A line 13 refuses on sa.gift_carryover_if_no_gifts (the form, remedy and "
                      "citation are those the line states); line 15 (casualty and theft losses, none) does not refuse "
                      "on the carryover and is $0. Mutants that drop the carryover refusal from line 13, that test "
                      "another answer for it, or that copy line 13 onto line 15 change one of the two.")})

# Questions the scope screens ask only of some filers, left unanswered where they are not asked.
rows.append({"id": "mutation.m3.scope.over24_unasked", "base": B0, "set": dict(B0_OFF),
             "drop": ["scope.unearned_2700", "scope.f8615"],
             "covers": ["scope", "scope.under24", "scope.other_line16"],
             "expect": {"scope.ready_other_line16": {"bool": True}},
             "note": ("Mutation fixture for the under-24 gate of the Form 8615 questions: " + B0_DESC + " (born in "
                      "1980, so 45 at the end of 2025); the two Form 8615 questions (unearned income over $2,700, Form "
                      "8615 required) are left unanswered, as the interview asks them only of a filer under 24 who is "
                      "not filing jointly. Predicted by hand from the scope lines before running the evaluator: the "
                      "line 16 screen is false with every item it reads known, so scope.ready_other_line16 is true. A "
                      "mutant that counts another person or line as under 24, or tests the count at zero, reaches the "
                      "unanswered questions and leaves it unknown.")})
rows.append({"id": "mutation.m3.scope.no_w2_unasked", "base": BIZ, "set": {},
             "drop": ["scope.w2_marks", "scope.artist_official", "scope.performer_expenses", "scope.excess_deferral"],
             "covers": ["scope", "scope.has_w2"],
             "expect": {"scope.ready_schedule1": {"bool": True}, "scope.ready_other_income": {"bool": True}},
             "note": ("Mutation fixture for the Form W-2 gate of the scope screens: " + BIZ_DESC + ", and no Form W-2; "
                      "the four questions asked only of a filer with a Form W-2 (statutory employee or other box 13 "
                      "marks, qualified performing artist or fee-basis official and the expenses, deferrals over the "
                      "limit) are left unanswered. Predicted by hand from the scope lines before running the "
                      "evaluator: the Schedule 1 and other-income screens are false with every item they read known, "
                      "so scope.ready_schedule1 and scope.ready_other_income are true. A mutant that asks the W-2 "
                      "questions with no Form W-2 leaves them unknown.")})

json.dump(rows, open(os.path.join(HERE, "cases.json"), "w"), indent=2, ensure_ascii=False)
print(len(rows), "rows")
