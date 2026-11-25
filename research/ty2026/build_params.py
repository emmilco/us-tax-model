#!/usr/bin/env python3
"""Write research/ty2026/params-2026.proposed.yaml: the 2026 value of each parameter of params/2025.yaml
that an archived 2026 source prints, with its 2026 cite and `source: final|draft`; parameters with no 2026
source keep no value (`value: null`, `source: none`) and are listed. The values below were read from the
cited pages by hand (TY2026 step 4); a parameter not read by hand takes the mechanical proposal
(reports/2026/params_proposal_from_2025.yaml, tools/propose_params.py; rerun it first) where that found a
value, including the derived ones (`derived`: the `age.*` years moved with the year, `source: derived`, and
the Tax Computation Worksheet subtraction amounts from the rate tables). check_params.py checks each quote
against its page and that it prints the amount. `enums.changed` holds each enumeration whose 2026 values or
citation differ. Not read by the build."""
import json, re, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
P25 = yaml.safe_load((ROOT / "params/2025.yaml").read_text())["params"]
MAN = {e["id"]: e for e in json.loads((ROOT / "sources/2026/manifest.json").read_text())["documents"]}

D = lambda dollars: int(round(dollars * 100))          # dollars -> cents
R = lambda n, d: {"num": n, "den": d}
ST = lambda single, mfj, mfs, hoh, qss=None: {"single": D(single), "mfj": D(mfj), "mfs": D(mfs), "hoh": D(hoh),
                                               "qss": D(mfj if qss is None else qss)}

# Rev. Proc. 2025-32 prints its section 4 as "SECTION 4. 2026 ADJUSTED ITEMS" and then each subsection as ".NN <heading>",
# so "section 4.NN" is not printed text: a locator anchors on the printed ".NN <heading>" (citations.py checks the
# anchor on the cited page or the IN_FORCE pages before it), the section number kept after it.
RP_HEADINGS = {"01": "Tax Rate Tables", "03": "Maximum Capital Gains Rate", "05": "Child Tax Credit",
               "06": "Earned Income Credit", "10": "Exemption Amounts for Alternative Minimum Tax", "12": "Certain Expenses of Elementary and Secondary School Teachers",
               "14": "Standard Deduction", "23": "Gross Income Limitation for a Qualifying Relative",
               "24": "Election to Expense Certain Depreciable Assets", "26": "Qualified Business Income",
               "29": "Interest on Education Loans", "31": "Threshold for Excess Business Loss"}

def printed_anchor(doc, heading):
    """A locator heading "section 4.NN[(k)][, rest]" of Rev. Proc. 2025-32 led by the printed ".NN <heading>"."""
    m = re.fullmatch(r"section 4\.(\d\d)(\(\d+\))?(?:, (.*))?", heading)
    if doc != "rp-25-32" or not m:
        return heading
    nn, sub, rest = m.groups()
    printed = RP_HEADINGS[nn]
    return ", ".join([f".{nn} {printed}", f"section 4.{nn}{sub or ''}"] + ([rest] if rest and rest != printed else []))

# id -> (value, doc, page, locator heading, quote, note)
V = {}
def put(pid, value, doc, page, heading, quote, note=None):
    assert pid in P25["values"], pid
    V[pid] = (value, doc, page, printed_anchor(doc, heading), quote, note)

# ---- Rev. Proc. 2025-32 (final) ----
RP = "rp-25-32"
# Tax Computation Worksheet rows: the bracket boundaries and rates of the 2026 rate tables (section 4.01).
tcw = {
 "mfj":    (10, [(100800, 211400), (211400, 403550), (403550, 512450), (512450, 768700)], 768700),
 "hoh":    (11, [(67450, 105700), (105700, 201750), (201750, 256200), (256200, 640600)], 640600),
 "single": (11, [(50400, 105700), (105700, 201775), (201775, 256225), (256225, 640600)], 640600),
 "mfs":    (12, [(50400, 105700), (105700, 201775), (201775, 256225), (256225, 384350)], 384350),
}
rates = [22, 24, 32, 35]
for st, (pg, rows, top) in tcw.items():
    for i, (lo, hi) in enumerate(rows, 1):
        p = pg
        if st == "mfs" and i == 1: p = 11
        if st == "hoh" and i == 1: p = 10
        put(f"tcw.{st}.b{i}.upper", D(hi), RP, p, "section 4.01, Tax Rate Tables",
            f"Over ${lo:,} but not over ${hi:,}",
            "the row's upper limit is the bracket boundary of the rate table; the 2026 Tax Computation Worksheet itself is in the Form 1040 instructions (not posted): confirm the row against it")
        put(f"tcw.{st}.b{i}.rate", R(rates[i - 1], 100), RP, p if not (st == 'mfs' and i == 1) else 11,
            "section 4.01, Tax Rate Tables", f"plus {rates[i - 1]}% of the excess over ${lo:,}")
    put(f"tcw.{st}.b5.rate", R(37, 100), RP, pg if st != "single" else 11, "section 4.01, Tax Rate Tables",
        f"plus 37% of the excess over ${top:,}")
put("qdcg.zero_rate_ceiling", ST(49450, 98900, 49450, 66200), RP, 13, "section 4.03, Maximum Capital Gains Rate",
    "Married Individuals Filing Joint Returns and $98,900 $613,700 Surviving Spouse Married Individuals Filing Separate Returns $49,450 $306,850 Heads of Household $66,200 $579,600 All Other Individuals $49,450 $545,500",
    "the maximum zero rate amounts; the QDCG worksheet (Form 1040 instructions) is not posted")
put("qdcg.fifteen_rate_ceiling", ST(545500, 613700, 306850, 579600), RP, 13, "section 4.03, Maximum Capital Gains Rate",
    "Married Individuals Filing Joint Returns and $98,900 $613,700 Surviving Spouse Married Individuals Filing Separate Returns $49,450 $306,850 Heads of Household $66,200 $579,600 All Other Individuals $49,450 $545,500",
    "the maximum 15 percent rate amounts")
put("sa.standard_base", ST(16100, 32200, 16100, 24150), RP, 18, "section 4.14(1), Standard Deduction",
    "Married Individuals Filing Joint Returns and Surviving Spouses $32,200 (§ 1(j)(2)(A)) Heads of Households (§ 1(j)(2)(B)) $24,150 Unmarried Individuals (other than Surviving Spouses and Heads of $16,100 Households) (§ 1(j)(2)(C)) Married Individuals Filing Separate Returns (§ 1(j)(2)(D)) $16,100")
put("sa.standard_extra", {"single": D(2050), "hoh": D(2050), "mfs": D(1650), "mfj": D(1650), "qss": D(1650)}, RP, 18,
    "section 4.14(3), Aged or blind",
    "the additional standard deduction amount under § 63(f) for the aged or the blind is $1,650. The additional standard deduction amount is increased to $2,050 if the individual is also unmarried and not a surviving spouse.")
put("ctc.per_child", D(2200), RP, 14, "section 4.05(1), Child Tax Credit, maximum amount", "the maximum amount of the credit allowed under § 24(a) is $2,200.")
put("actc.per_child", D(1700), RP, 14, "section 4.05(2), Refundable portion",
    "§ 24(d)(1)(A) to determine the amount of the credit under § 24 that may be refundable is $1,700.")
eic = {"earned_amount": ("Earned Income Amount $13,020 $18,290 $18,290 $8,680", [13020, 18290, 18290, 8680]),
       "maximum": ("Maximum Amount of Credit $4,427 $7,316 $8,231 $664", [4427, 7316, 8231, 664])}
for key, (q, vals) in eic.items():
    for n, amt in zip([1, 2, 3, 0], vals):
        put(f"eic.{key}{n}", D(amt), RP, 15, "section 4.06(1), Earned Income Credit (columns One, Two, Three or More, None)", q)
lim = {"joint": ("Completed Phaseout $58,863 $65,899 $70,244 $26,820", [58863, 65899, 70244, 26820]),
       "other": ("Completed Phaseout $51,593 $58,629 $62,974 $19,540", [51593, 58629, 62974, 19540])}
for who, (q, vals) in lim.items():
    for n, amt in zip([1, 2, 3, 0], vals):
        put(f"eic.limit{n}.{who}", D(amt), RP, 15,
            f"section 4.06(1), Completed Phaseout Amount ({'Married Filing Jointly' if who == 'joint' else 'All other filing statuses'})", q,
            "the completed phaseout amount; the Form 1040 instructions' EIC Step 1 (not posted) prints the 'less than' amounts")
thr = {"joint": ("Threshold Phaseout Amount $31,160 $31,160 $31,160 $18,140", 31160, 18140),
       "other": ("Threshold Phaseout Amount $23,890 $23,890 $23,890 $10,860", 23890, 10860)}
for who, (q, one, none) in thr.items():
    put(f"eic.ws_threshold1.{who}", D(one), RP, 15, "section 4.06(1), Threshold Phaseout Amount", q,
        "EIC Worksheet A line 5 (Form 1040 instructions, not posted) prints the same amount in 2025")
    put(f"eic.ws_threshold0.{who}", D(none), RP, 15, "section 4.06(1), Threshold Phaseout Amount", q)
put("eic.investment_limit", D(12200), RP, 15, "section 4.06(2), Excessive Investment Income",
    "investment income exceeds $12,200.")
put("s1.educator_max", D(350), RP, 17, "section 4.12, Certain Expenses of Elementary and Secondary School Teachers",
    "supplementary materials used by the eligible educator in the classroom is $350.")
put("qr.gross_income_limit", D(5300), RP, 20, "section 4.23, Gross Income Limitation for a Qualifying Relative",
    "the exemption amount referred to in § 152(d)(1)(B) is $5,300.")
put("s179.max", D(2560000), RP, 21, "section 4.24, Election to Expense Certain Depreciable Assets",
    "the aggregate cost of any § 179 property that a taxpayer elects to treat as an expense cannot exceed $2,560,000")
put("s179.suv_limit", D(32000), RP, 21, "section 4.24", "the cost of any sport utility vehicle that may be taken into account under § 179 cannot exceed $32,000.")
put("s179.threshold", D(4090000), RP, 21, "section 4.24", "the cost of § 179 property placed in service during the 2026 taxable year exceeds $4,090,000.")
put("qbi.threshold", {"single": D(201750), "hoh": D(201750), "qss": D(201750), "mfs": D(201775), "mfj": D(403500)}, RP, 22,
    "section 4.26, Qualified Business Income",
    "Married Individuals Filing Joint Returns $403,500 ... Married Individuals Filing Separate $201,775 ... All Other Returns $201,750",
    "the threshold amounts under section 199A(e)(2); the Form 8995 draft (p. 2, line 1 caption) prints the same amounts. The 2025 value used one amount for married filing separately and single; 2026 does not")
put("sli.base_other", D(85000), RP, 23, "section 4.29, Interest on Education Loans",
    "modified adjusted gross income in excess of $85,000 ($175,000 for joint returns)")
put("sli.base_joint", D(175000), RP, 23, "section 4.29, Interest on Education Loans",
    "modified adjusted gross income in excess of $85,000 ($175,000 for joint returns)")
put("sli.max", D(2500), RP, 23, "section 4.29, Interest on Education Loans", "the $2,500 maximum deduction for interest paid on qualified education loans")
put("s1.ebl_threshold", ST(256000, 512000, 256000, 256000, 256000), RP, 23, "section 4.31, Threshold for Excess Business Loss",
    "the amount under § 461(l)(3)(A)(ii)(II) is $256,000 ($512,000 for joint returns).")

# ---- Notice 2025-67 (final) ----
N = "n-25-67"
put("ira.limit", D(7500), N, 4, "IRA deductible amount, section 219(b)(5)(A)", "is increased from $7,000 to $7,500.")
put("ira.line2", {"single": D(91000), "hoh": D(91000), "mfs": D(10000), "mfj": D(149000), "qss": D(149000)}, N, 4,
    "section 219(g) phase-out ranges",
    "adjusted gross incomes (as defined in section 219(g)(3)(A)) between $81,000 and $91,000 ... the income phase-out range is between $129,000 and $149,000 ... remains $0 to $10,000.",
    "the upper ends of the phase-out ranges, which the 2025 IRA Deduction Worksheet line 2 printed; the 2026 worksheet (Form 1040 instructions) is not posted; the qualifying-surviving-spouse amount follows section 219(g)(3)(B)(i) ('a joint return or as a qualifying widow(er)')")
put("ira.line2_not_covered", D(252000), N, 4, "section 219(g)(7)(A)", "the deduction is phased out if the couple’s income is between $242,000 and $252,000")
put("ira.roth_start_joint", D(242000), N, 5, "section 408A(c)(3)(A)",
    "the adjusted gross income phase-out range for taxpayers making contributions to a Roth IRA is between $242,000 and $252,000 for married couples filing jointly")
put("ira.roth_start_other", D(153000), N, 5, "section 408A(c)(3)(A)",
    "For singles and heads of household, the income phase-out range is between $153,000 and $168,000")
put("savers.agi_limit", {"single": D(40250), "mfs": D(40250), "qss": D(40250), "hoh": D(60375), "mfj": D(80500)}, "f8880", 2,
    "Form 8880 (2026), caution", "is more than $40,250 ($60,375 if head of household; $80,500 if married filing jointly).",
    "draft form; the same limits are in n-25-67 p. 3-4 (final)")
put("ret.comp_limit", D(360000), N, 2, "sections 401(a)(17), 404(l), 408(k)(3)(C)", "is increased from $350,000 to $360,000.")
put("ret.sep_dollar_limit", D(72000), N, 1, "section 415(c)(1)(A)", "increased in 2026 from $70,000 to $72,000.")
put("ret.simple_limit", D(17000), N, 2, "section 408(p)(2)(E)(i)(III)",
    "contributions under a SIMPLE retirement account or elective contributions under a SIMPLE 401(k) plan is increased from $16,500 to $17,000.",
    "the notice also raises the section 408(p)(2)(E)(i)(I) or (II) limit to $18,100 for certain plans; the 2025 encoding refuses or does not distinguish those plans: check at adoption (p560 2026 not posted)")

# ---- HSA ----
put("hsa.self_only", D(4400), "rp-25-19", 2, "section 3, HSA annual limitation, self-only coverage", "is $4,400")
put("hsa.family", D(8750), "rp-25-19", 2, "section 3, HSA annual limitation, family coverage", "is $8,750")
put("hsa.self_only_55", D(5400), "i8889", 7, "Line 3 Limitation Chart, self-only coverage", "If you were age 55 or older at the end of 2026, enter $5,400 for the month.")
put("hsa.family_55", D(9750), "i8889", 7, "Line 3 Limitation Chart, family coverage", "you were unmarried and age 55 or older, enter $9,750 for the month.")

# ---- Social security wage base (final) ----
put("ss.base", D(184500), "p15", 2, "Social security and Medicare taxes for 2026", "The social security wage base limit is $184,500.")
put("ss.limit", D(11439), "iw2w3", 19, "Box 4—Social security tax withheld", "For 2026, the amount should not exceed $11,439 ($184,500 × 6.2%).")
put("se.wage_base", D(184500), "f1040sse", 1, "Schedule SE (2026), line 7", "earnings subject to social security tax or $184,500")

# ---- SALT (statute, final; the draft Schedule A prints the same) ----
put("sa.salt_base", D(40400), "plaw-119-21", 99, "section 70120, section 164(b)(7)(A)(ii)",
    "in the case of any taxable year beginning in calendar year 2026, $40,400")
put("sa.salt_threshold", {"single": D(505000), "hoh": D(505000), "qss": D(505000), "mfj": D(505000), "mfs": D(252500)}, "plaw-119-21", 99,
    "section 70120, section 164(b)(7)(B)",
    "the threshold amount (half the threshold amount in the case of a married individual filing a separate return) ... in the case of any taxable year beginning in calendar year 2026, $505,000",
    "the married-filing-separately amount is half the printed $505,000; the Schedule A draft (p. 2, line 5e) prints \"$505,000 ($252,500 if married filing separately)\"")
put("sa.salt_floor", D(10000), "plaw-119-21", 99, "section 164(b)(7)(B)(iii)", "shall not result in the applicable limitation amount being less than $10,000.")
put("sa.salt_rate", R(3, 10), "plaw-119-21", 99, "section 164(b)(7)(B)(i)", "the applicable limitation amount shall be reduced by 30 percent of the excess")
put("sa.half", R(1, 2), "plaw-119-21", 99, "section 164(b)(7)(B)(i)", "half the threshold amount in the case of a married individual filing a separate return",
    "the 2025 parameter halves the limitation; the statute halves both the limitation and the threshold: the encoding's use of sa.half must be checked against the 2026 Schedule A instructions")

# ---- Drafts with a changed amount ----
put("dc.exclusion_max", D(7500), "i2441", 7, "Line 21",
    "The maximum amount is increased to $7,500 (previously $5,000). For married employees filing separate returns",
    "the instruction for the line that reads it (lane O4); What's New (p. 2) prints the same amount")
put("f5329.cap_abuse", D(10500), N, 5, "section 72(t)(2)(K)(ii)(I), distributions to victims of domestic abuse",
    "domestic abuse from applicable eligible retirement plans is increased from $10,300 to $10,500",
    "Pub. 590-B (2026, draft) p. 29 prints the same amount")
put("ctc.threshold", ST(200000, 400000, 200000, 200000, 200000), "f1040s8812", 1, "Schedule 8812 (2026), line 9",
    "Married filing jointly—$400,000 . . . . . . . . . . . . . . . . . . . . . . • All other filing statuses—$200,000")
put("ptc.months", 12, "i1095a", 2, "Part III", "Add the amounts on lines 21 through 32 and enter on line 33.", "structural: twelve monthly lines")
put("s1a.tips_max", D(25000), "f1040s1a", 2, "Schedule 1-A (2026), Part II", "Enter the smaller of the amount on line 8 or $25,000",
    "Schedule 1-A is renumbered in 2026 (SCHED section of the change map)")
put("s1a.ot_max_other", D(12500), "f1040s1a", 3, "Schedule 1-A (2026), Part III", "Enter the smaller of the amount on line 20 or $12,500 ($25,000 if married filing jointly)")
put("s1a.ot_max_joint", D(25000), "f1040s1a", 3, "Schedule 1-A (2026), Part III", "Enter the smaller of the amount on line 20 or $12,500 ($25,000 if married filing jointly)")
put("s1a.car_max", D(10000), "f1040s1a", 4, "Schedule 1-A (2026), Part IV", "Enter the smaller of the amount on line 29 or $10,000")
put("s1a.senior_amount", D(6000), "f1040s1a", 4, "Schedule 1-A (2026), Part V", "Subtract line 40 from $6,000.")
put("s1a.senior_rate", R(6, 100), "f1040s1a", 4, "Schedule 1-A (2026), Part V", "Multiply line 39 by 6% (0.06)")
put("medicare.threshold", {"single": D(200000), "hoh": D(200000), "qss": D(200000), "mfj": D(250000), "mfs": D(125000)}, "f8959", 2,
    "Form 8959 (2026), lines 5, 9 and 14",
    "jointly . . . . . . . . . . . . . . . $250,000 Married filing separately . . . . . . . . . . . . . . $125,000 5 Single, Head of household, or Qualifying surviving spouse . . . $200,000")
put("medicare.additional_rate", R(9, 1000), "f8959", 2, "Form 8959 (2026), line 7", "Multiply line 6 by 0.9% (0.009).")
put("medicare.regular_rate", R(145, 10000), "f8959", 2, "Form 8959 (2026), line 21", "Multiply line 20 by 1.45% (0.0145).")
put("niit.threshold", {"single": D(200000), "hoh": D(200000), "mfs": D(125000), "mfj": D(250000), "qss": D(250000)}, "i8960", 3,
    "Application to Individuals", "Married filing jointly or Qualifying surviving spouse is $250,000. • Married filing separately is $125,000. • Single or Head of household is $200,000.")
put("niit.rate", R(38, 1000), "i8960", 3, "Application to Individuals", "must pay 3.8% of the smaller of")
put("qbi.rate", R(1, 5), "f8995", 2, "Form 8995 (2026), line 5", "Qualified business income component. Multiply line 4 by 20% (0.20)")
put("ftc.limit", {"single": D(300), "hoh": D(300), "qss": D(300), "mfs": D(300), "mfj": D(600)}, "i1116", 3,
    "Election To Claim the Foreign Tax Credit Without Filing Form 1116", "Your total creditable foreign taxes aren’t more than $300 ($600 if married filing a joint return).")
put("sd.loss_limit", {"single": -D(3000), "mfj": -D(3000), "mfs": -D(1500), "hoh": -D(3000), "qss": -D(3000)}, "f1040sd", 3,
    "Schedule D (2026), line 21", "($3,000), or if married filing separately, ($1,500)")
put("sa.medical_rate", R(75, 1000), "f1040sa", 2, "Schedule A (2026), line 3", "Multiply line 2 by 7.5% (0.075)")
put("f5329.cap_emergency", D(1000), "p590b", 29, "Emergency personal expense distributions", "must not exceed the lesser of $1,000 or your total interest in the IRA minus $1,000.")

put("sc.ho_rate", D(5), "i1040sc", 14, "Simplified Method Worksheet, line 3a", "3a. Maximum allowable amount . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3a. $5")

put("ira.limit_50", D(8600), "i1099r", 22, "IRA regular contribution limit",
    "The annual IRA regular contribution limit of $7,500 is increased to $8,600 for participants age 50 or older",
    "the 2025 value cites the IRA Deduction Worksheet (Form 1040 instructions, not posted); n-25-67 (final) prints the parts ($7,500 and the $1,100 catch-up), the i8606 draft (p. 6) the same $8,600")
KBH = "combined taxable compensation of both you and your spouse is less than $15,000 ($16,100 if one spouse is age 50 or older at the end of 2026; $17,200 if both spouses are age 50 or older at the end of 2026"
put("ira.kbh_none", D(15000), "i8606", 6, "Kay Bailey Hutchison Spousal IRA limit", KBH)
put("ira.kbh_one", D(16100), "i8606", 6, "Kay Bailey Hutchison Spousal IRA limit", KBH)
put("ira.kbh_both", D(17200), "i8606", 6, "Kay Bailey Hutchison Spousal IRA limit", KBH)

# ---- IRA deduction reduction (Pub. 590-A Worksheet 1-2, draft; the encoded worksheet is the Form 1040 instructions'
# IRA Deduction Worksheet, not posted, which figures the same reduction) ----
IRA_NOTE = ("Pub. 590-A Worksheet 1-2 figures the same reduction as the IRA Deduction Worksheet the 2025 value cites "
            "(Form 1040 instructions, not posted): confirm against that worksheet")
put("ira.full_narrow", D(10000), "p590a", 19, "Worksheet 1-2, Figuring Your Reduced IRA Deduction for 2026, line 3",
    "Subtract line 2 from line 1. If line 3 is $10,000 or more ($20,000 or more if married filing jointly or qualifying surviving spouse and you are covered by an employer plan), stop here.", IRA_NOTE)
put("ira.full_joint", D(20000), "p590a", 19, "Worksheet 1-2, Figuring Your Reduced IRA Deduction for 2026, line 3",
    "Subtract line 2 from line 1. If line 3 is $10,000 or more ($20,000 or more if married filing jointly or qualifying surviving spouse and you are covered by an employer plan), stop here.", IRA_NOTE)
IRA_RATE = ("the rate is the 2026 contribution limit over the phase-out range ($7,500 or $8,600 over $10,000 or $20,000), "
            "so it changes with ira.limit; the parameter's name keeps the 2025 rate. " + IRA_NOTE)
put("ira.rate_70", R(75, 100), "p590a", 19, "Worksheet 1-2, line 4", "All others, multiply line 3 by 75% (0.75) (by 86% (0.86) if you are age 50 or older).", IRA_RATE)
put("ira.rate_80", R(86, 100), "p590a", 19, "Worksheet 1-2, line 4", "All others, multiply line 3 by 75% (0.75) (by 86% (0.86) if you are age 50 or older).", IRA_RATE)
put("ira.rate_35", R(375, 1000), "p590a", 19, "Worksheet 1-2, line 4", "multiply line 3 by 37.5% (0.375) (by 43% (0.43) if you are age 50", IRA_RATE)
put("ira.rate_40", R(43, 100), "p590a", 19, "Worksheet 1-2, line 4", "multiply line 3 by 37.5% (0.375) (by 43% (0.43) if you are age 50", IRA_RATE)
put("ira.min", D(200), "p590a", 19, "Worksheet 1-2, line 4", "However, if the result is less than $200, enter $200.", IRA_NOTE)
put("ira.line2_apart", D(91000), "p590a", 15, "Table 1-2, single or head of household, and its footnote",
    "$91,000 or more ... If you didn’t live with your spouse at any time during the year, your filing status is considered Single for this purpose",
    "the single upper limit, which applies to a separate filer who lived apart all year; n-25-67 p. 4 (final) prints the same $91,000. " + IRA_NOTE)

# ---- Social security benefits (Pub. 915 Worksheet 1, final; the encoded worksheet is the Form 1040 instructions', not posted) ----
SSB_NOTE = "Pub. 915 Worksheet 1 is the worksheet the Form 1040 instructions (not posted) reproduce: confirm against them"
SSB_BASE = "Married filing jointly, enter $32,000; or ... apart from your spouse for all of 2026, enter $25,000"
SSB_ADJ = "Enter $12,000 if married filing jointly; or $9,000 if single, head of household, qualifying surviving spouse, or"
put("ssb.base_single", D(25000), "p915", 17, "Worksheet 1, Figuring Your Taxable Benefits, line 9", SSB_BASE, SSB_NOTE)
put("ssb.base_joint", D(32000), "p915", 17, "Worksheet 1, Figuring Your Taxable Benefits, line 9", SSB_BASE, SSB_NOTE)
put("ssb.adjust_single", D(9000), "p915", 17, "Worksheet 1, Figuring Your Taxable Benefits, line 11", SSB_ADJ, SSB_NOTE)
put("ssb.adjust_joint", D(12000), "p915", 17, "Worksheet 1, Figuring Your Taxable Benefits, line 11", SSB_ADJ, SSB_NOTE)
put("ssb.half", R(1, 2), "p915", 17, "Worksheet 1, Figuring Your Taxable Benefits, lines 2 and 14", "Multiply line 13 by 50% (0.50)", SSB_NOTE)
put("ssb.rate85", R(85, 100), "p915", 17, "Worksheet 1, Figuring Your Taxable Benefits, lines 16 and 18", "Multiply line 12 by 85% (0.85)", SSB_NOTE)

# ---- Alternative minimum tax (C-LAW-02; Form 6251 2026 not posted) ----
put("amt.exemption", ST(90100, 140200, 70100, 90100), RP, 16, "section 4.10, Exemption Amounts for Alternative Minimum Tax",
    "Joint Returns or Surviving Spouses $140,200 Unmarried Individuals (other than Surviving Spouses) $90,100 Married Individuals Filing Separate Returns $70,100",
    "i6251 p. 10 (draft), Exemption Worksheet line 1, prints the same amounts")
put("amt.bracket", ST(244500, 244500, 122250, 244500), RP, 16, "section 4.10, the excess taxable income above which the 28 percent rate applies",
    "Married Individuals Filing Separate Returns $122,250 All Other Taxpayers $244,500",
    "i6251 p. 11 (draft), Line 7, prints the same amounts")
put("amt.phaseout_start", ST(500000, 1000000, 500000, 500000), RP, 17, "section 4.10, Threshold Phaseout Amount",
    "Joint Returns or Surviving Spouses $1,000,000 $1,280,400 Unmarried Individuals (other than $500,000 $680,200 Surviving Spouses) Married Individuals Filing Separate $500,000 $640,200",
    "the threshold phaseout amounts (section 55(d)(2) as amended by P.L. 119-21 section 70107); i6251 p. 10 (draft), Exemption Worksheet line 3, prints the same amounts")
put("amt.bracket_subtract", ST(4890, 4890, 2445, 4890), "i6251", 11, "Line 7",
    "multiplying line 6 by 28% (0.28) and subtracting $4,890 ($2,445 if married filing separately)",
    "2% of amt.bracket ($244,500; $122,250), as in 2025")
put("amt.rate_26", R(26, 100), "i6251", 11, "Line 7", "multiplying line 6 by 26% (0.26)")
put("amt.rate_28", R(28, 100), "i6251", 11, "Line 7", "multiplying line 6 by 28% (0.28)")
put("amt.rate_25", R(25, 100), "f6251", 3, "Form 6251 (2026), line 37", "Multiply line 36 by 25% (0.25)",
    "Form 6251 line 37, read after C-LAW-02's operations by s2.amt_l37_rate alone (the exemption phase-out and the "
    "separate-return add-back read amt.phaseout_rate); the 2026 i6251 draft does not print line 37's rate; P.L. 119-21 "
    "section 70107 amends section 55(d) only")

# ---- Other parameters read by hand from the refreshed archive ----
put("sa.dep_min", D(1350), RP, 18, "section 4.14(2), Standard deduction for a dependent",
    "cannot exceed the greater of (1) $1,350, or (2) the sum of $450 and",
    "the 2025 value cites the Standard Deduction Worksheet for Dependents (Form 1040 instructions, not posted), which applies this rule")
put("sa.dep_add", D(450), RP, 18, "section 4.14(2), Standard deduction for a dependent",
    "cannot exceed the greater of (1) $1,350, or (2) the sum of $450 and",
    "the 2025 value cites the Standard Deduction Worksheet for Dependents (Form 1040 instructions, not posted), which applies this rule")
put("ctc.age_limit", 17, "f1040s8812", 1, "Schedule 8812 (2026), line 4",
    "Number of qualifying children under age 17 with the required social security number",
    "the 2025 value cites the Form 1040 instructions' Step 3 (not posted); the i1040s8812 draft (p. 3) prints \"under age 17 at the end of 2026\"")
put("f1116.exception_ceiling", {"single": D(201775), "mfs": D(201775), "hoh": D(201750), "mfj": D(403550), "qss": D(403550)},
    "i1116", 11, "Adjustment exception (qualified dividends)",
    "a. $403,550 if married filing jointly or qualifying ... b. $201,775 if married filing separately, ... c. $201,775 if single, or ... d. $201,750 if head of household.",
    "the head-of-household amount differs from the single amount in 2026 (the 2026 rate tables' 32% bracket starts, rp-25-32 pp. 10-12); in 2025 they were equal")
put("f8582.special_max", {"single": D(25000), "mfj": D(25000), "mfs": D(12500), "hoh": D(25000), "qss": D(25000)}, "i8582", 5,
    "Special allowance for rental real estate activities",
    "The maximum special allowance is: • $25,000 for single individuals and married individuals filing a joint return for the tax year; • $12,500 for married individuals who file separate returns",
    "f8582 p. 2 (draft), line 8, prints \"Do not enter more than $25,000\"")
put("f8582.phaseout_end", {"single": D(150000), "mfj": D(150000), "mfs": D(75000), "hoh": D(150000), "qss": D(150000)}, "i8582", 12,
    "Line 5", "enter $75,000 on line 5 instead of $150,000", "f8582 p. 2 (draft), line 5, prints \"Enter $150,000\"")
put("dc.exclusion_max_mfs", D(3750), "i2441", 7, "Line 21",
    "married employees filing separate returns, the maximum amount is increased to $3,750 (previously $2,500)",
    "What's New (p. 2) prints the same amount; the separate-return half of dc.exclusion_max ($7,500)")
put("dc.providers_listed", 3, "i2441", 4, "Lines 1a through 1e", "If you have more than three care providers, check the box at the top of Part I",
    "Form 2441 Part I is relaid out as lines 1a to 1e in 2026 (draft); the count of providers it lists is unchanged")
put("dc.persons_listed", 3, "i2441", 4, "Line 2", "If you have more than three qualifying persons, check the box on line 2",
    "Form 2441 (2026, draft) line 2 prints the same count")
put("dc.one", 1, "i2441", 4, "Lines 1a through 1e", "Complete lines 1a through 1e for each person or organization that provided the care.",
    "one entry per care provider, as in 2025; Form 2441 Part I is relaid out as lines 1a to 1e in 2026 (draft)")
put("f8919.rate_062", R(62, 1000), "f8919", 1, "Form 8919 (2026), line 11", "Multiply line 10 by 0.062 (social security tax rate)")
put("f8919.rate_0145", R(145, 10000), "f8919", 1, "Form 8919 (2026), line 12", "Multiply line 6 by 0.0145 (Medicare tax rate)")
put("f4137.rate_062", R(62, 1000), "f4137", 2, "Form 4137 (2026), line 11", "Multiply line 10 by 0.062 (social security tax rate)")
put("f4137.rate_0145", R(145, 10000), "f4137", 2, "Form 4137 (2026), line 12", "Multiply line 6 by 0.0145 (Medicare tax rate)")
put("s1a.hundred_per_thousand", R(1, 10), "f1040s1a", 2, "Schedule 1-A (2026), lines 13 and 14",
    "Divide line 12 by $1,000. ... Multiply line 13 by $100",
    "$100 for each whole $1,000; lines 25 and 26 (p. 3) print the same for overtime")
put("s1a.two_hundred_per_thousand", R(1, 5), "f1040s1a", 4, "Schedule 1-A (2026), line 35", "Multiply line 34 by $200",
    "$200 for each $1,000 (line 34, rounded up)")
put("f1116.high_tax_rate", R(37, 100), RP, 11, "section 4.01, Tax Rate Tables (the highest rate of section 1)",
    "plus 37% of the excess over $640,600",
    "the highest rate of tax specified in section 1 (cfr-26-1-904-4); the 2025 value cites the Form 1040 instructions' Tax Computation Worksheet (not posted)")

put("f5329.simple_rate", R(25, 100), "f5329", 1, "Form 5329 (2026), line 4",
    "include 25% of that amount on line 4 instead of 10%",
    "the i5329 draft (p. 6, Line 4) prints \"you must multiply that amount by 25% instead of 10%.\"")

# ---- Values a final source fixes (audit of 2026-11-22) ----
put("sdtw.ordinary_ceiling", ST(201775, 403550, 201775, 201750), RP, 11, "section 4.01, Tax Rate Tables",
    "Over $105,700 but not over $201,750 ... Over $105,700 but not over $201,775",
    "the top of the 24% bracket, the Schedule D Tax Worksheet's ceiling in 2025 as well (i1040sd 2026 not posted): Table 2 (head of household, "
    "p. 11) $201,750; Table 3 (single, p. 11) and Table 4 (married filing separately, p. 12) $201,775; Table 1 (joint and surviving spouse, "
    "p. 10, \"Over $211,400 but not over $403,550\") $403,550. Head of household is $25 below single in 2026 (equal in 2025). The i1116 "
    "draft p. 11 prints the same four amounts (f1116.exception_ceiling)")
put("sli.divisor_other", D(15000), RP, 23, "section 4.29, Interest on Education Loans",
    "in excess of $85,000 ($175,000 for joint returns), and is completely phased out for taxpayers with modified adjusted gross income of $100,000 or more ($205,000 or more for joint returns)",
    "the width of the phase-out range, $100,000 less $85,000 (the worksheet that prints the divisor is in the Form 1040 instructions, not posted)")
put("sli.divisor_joint", D(30000), RP, 23, "section 4.29, Interest on Education Loans",
    "in excess of $85,000 ($175,000 for joint returns), and is completely phased out for taxpayers with modified adjusted gross income of $100,000 or more ($205,000 or more for joint returns)",
    "the width of the joint phase-out range, $205,000 less $175,000")
put("clcw.prior_limit", D(3000), "f1040sd", 3, "Schedule D (2026), line 21", "($3,000), or if married filing separately, ($1,500)",
    "the capital loss limit of section 1211(b), not indexed: the Capital Loss Carryover Worksheet (i1040sd 2026, not posted) reads the prior year's limit, the same $3,000; the quote sd.loss_limit cites")
put("clcw.prior_limit_mfs", D(1500), "f1040sd", 3, "Schedule D (2026), line 21", "($3,000), or if married filing separately, ($1,500)",
    "as clcw.prior_limit, for married filing separately")

# Values not printed as one figure in their quote: check_params.py checks the quote on its page, not the amount.
DERIVED_V = {
 "sdtw.ordinary_ceiling": "the top of the 24% bracket of each 2026 rate table (rp-25-32 section 4.01 Tables 1 to 4, pp. 10-12); the quote prints the head-of-household and single rows",
 "sli.divisor_other": "the width of the printed phase-out range ($100,000 less $85,000)",
 "sli.divisor_joint": "the width of the printed joint phase-out range ($205,000 less $175,000)",
 "sa.salt_threshold": "married filing separately: half the printed threshold amount ($505,000 / 2)",
}

# ---- Structural counts and rates whose 2025 quote is printed unchanged in 2026 (filled from the auto-match) ----
AUTO = json.loads((Path(__file__).with_name("params_auto.json")).read_text()) if Path(__file__).with_name("params_auto.json").exists() else {}

# ---- Catch-up age bands (Enum values; the 2025 cite is p560, whose 2026 edition is not posted) ----
for pid, quote in (("ret.catchup_under50", "that generally applies for individuals aged 50 or over is increased from $7,500 to $8,000"),
                   ("ret.catchup_age50", "that generally applies for individuals aged 50 or over is increased from $7,500 to $8,000"),
                   ("ret.catchup_age60_63", "age 60, 61, 62, or 63 in 2026 remains $11,250")):
    put(pid, P25["values"][pid]["value"], N, 1 if "aged 50" in quote else 2, "sections 414(v)(2)(B)(i) and 414(v)(2)(E)(i), catch-up contributions",
        quote, "the age bands are unchanged: catch-up from age 50, the higher limit for ages 60 to 63 in the year; p560 (2026, not posted) restates them")

# ---- Parameters known to have no 2026 source ----
NONE_NOTES = {
 "refund.std_single": ("i1040gi 2026 not posted (the State and Local Income Tax Refund Worksheet). Inferred, not checked "
                       "against a 2026 worksheet: the 2026 worksheet prints the prior year's (2025) standard deduction, "
                       "$15,750 (single or married filing separately), as the 2025 worksheet printed 2024's; rp-25-32 p. 10"),
 "refund.std_joint": "as refund.std_single; inferred $31,500 (married filing jointly or qualifying surviving spouse, the 2025 amount)",
 "refund.std_hoh": "as refund.std_single; inferred $23,625 (head of household, the 2025 amount)",
 "refund.box_married": "as refund.std_single; inferred $1,600 per box (the 2025 additional amount for the married, params/2025.yaml sa.standard_extra)",
 "refund.box_unmarried": "as refund.std_single; inferred $2,000 per box (the 2025 additional amount for the unmarried, params/2025.yaml sa.standard_extra)",
 "qc.age_limit": "i1040gi 2026 not posted; the ages 19 and 24 printed in the 2026 Form 8814 and 8615 instructions belong to other rules",
 "qc.student_age_limit": "as qc.age_limit",
}

# ---- Parameters new in 2026 (no 2025 counterpart), and 2025 parameters they replace ----
# id -> (type, value, doc, page, locator heading, quote, note)
NEW = {
 "sc.mileage_rate_h1": ("Rate", R(725, 1000), "n-26-10", 3, "section 3, business standard mileage rate",
     "The standard mileage rate for transportation or travel expenses for 2026 is 72.5 cents per mile for all miles of business use",
     "dollars per mile, exact (owner decision 2026-11-04: an exact rate, rounded at the line); business miles January 1 to June 30, 2026; replaces sc.mileage_rate (C-BUS-01)"),
 "sc.mileage_rate_h2": ("Rate", R(76, 100), "irb26-29", 13, "Announcement 2026-11, revised standard mileage rates",
     "The revised standard mileage rates are: (1) Business 76 cents per mile",
     "dollars per mile; business miles July 1 to December 31, 2026 (the same page: \"on or after July 1, 2026\"); replaces sc.mileage_rate (C-BUS-01)"),
 "sa.gift_floor_rate": ("Rate", R(5, 1000), "plaw-119-21", 165, "section 70425, section 170(b)(1)(I), 0.5-percent floor",
     "shall be allowed only to the extent that the aggregate of such contributions exceeds 0.5 percent of the taxpayer’s contribution base",
     "owner decision 2026-11-04: encode the floor from the statute now; recheck against the 2026 Schedule A instructions (Charitable Contribution Limitation Worksheet) when they post (C-PRI-15)"),
 "sa.gambling_rate": ("Rate", R(9, 10), "plaw-119-21", 96, "section 70114, section 165(d)(1)(A), gambling losses",
     "shall be equal to 90 percent of the amount of such losses during such taxable year",
     "read by sa.gambling_90 (C-PRI-17)"),
 "sa.limit_screen": ("Dollars", D(384350), "f1040sa", 3, "Schedule A (2026), line 18 (draft)",
     "minus the amounts on lines 13a and 13b of that form, more than $384,350?",
     "read by f1040.limit_screen (C-PRI-07): the screen above which itemized deductions may be limited (section 68); equal to the start of the 37% bracket for married filing separately (rp-25-32, rate table D, \"Over $384,350\")"),
 "sc.bonus_rate_phase_down": ("Rate", R(20, 100), "rp-26-15", 2, "section 2, the phase-down of the special depreciation allowance",
     "placed in service during calendar year 2026 is 20 percent",
     "read by asset.rate40 and scveh.rate40 (C-BUS-04, lane O9); property acquired before January 20, 2025; replaces sc.bonus_rate_40"),
 "qbi.min_deduction": ("NonNegDollars", D(400), "i8995", 2, "What's New, Minimum deduction for active qualified business income",
     "there is a minimum qualified business income deduction of $400 for taxpayers whose aggregate qualified business income for such taxable year is at least $1,000",
     "section 199A(i)(1)(B); read by the 2026 QBI operations (lane O7)"),
 "qbi.min_active": ("NonNegDollars", D(1000), "i8995", 2, "What's New, Minimum deduction for active qualified business income",
     "there is a minimum qualified business income deduction of $400 for taxpayers whose aggregate qualified business income for such taxable year is at least $1,000",
     "section 199A(i)(2)(A); read by the 2026 QBI operations (lane O7)"),
 "niit.s68_threshold": ("NonNegDollars", {"single": D(640600), "hoh": D(640600), "mfs": D(384350), "mfj": D(768700), "qss": D(768700)},
     "i8960", 21, "Worksheet for the section 68 limitation, line 2",
     "Enter $768,700 if married filing jointly or qualifying surviving spouse; $640,600 if head of household or single; $384,350 if married filing separately",
     "where the 37% bracket begins (rp-25-32 pp. 10-12, final, prints the same amounts); read by the 2026 NIIT operations (lane O7)"),
 "amt.phaseout_rate": ("Rate", R(50, 100), "i6251", 10, "Exemption Worksheet—Line 5, line 5",
     "Multiply line 4 by 50% (0.50)",
     "the rate of the exemption phase-out (Exemption Worksheet line 5) and of the married-filing-separately add-back "
     "(i6251 p. 10, Line 4: \"include 50% of the excess of the amount on line 4 over $640,200\"); P.L. 119-21 section "
     "70107(c) (plaw-119-21 p. 93, final) substitutes 50 percent for 25 percent for taxable years beginning after "
     "December 31, 2025; read by s2.amt_mfs_phaseout_part, s2.amt_ex_cut, s2.amt_h_mfs_phaseout_part and s2.amt_h_ex_cut "
     "(changes/2026/s2.yaml, C-LAW-02, BUG-1031); Form 6251 line 37 keeps amt.rate_25"),
}
# The joint-return 12% row the 2026 Tax Computation Worksheet needs ($100,000 to $100,800; changes/2026/tcw.yaml,
# BUG-0647): the first rate-table row over the Tax Table boundary, by the D8 rule of tools/propose_params.py.
sys.path.insert(0, str(ROOT / "tools"))
import propose_params as PP, extract_printed_tables as EPT  # noqa: E402
_mfj = PP.tcw_rows(EPT.rate_schedule(EPT.Archive(2026))[0]["schedules"]["mfj"], P25["values"]["ordinary.table_boundary"]["value"])[0]
assert _mfj["rate"] == {"num": 12, "den": 100} and _mfj["upper"] == D(100800), _mfj
for _f, _t, _q in (("upper", "Dollars", "Over $24,800 but not over $100,800"),
                   ("rate", "Rate", "$2,480 plus 12% of the excess over $24,800"),
                   ("subtract", "Dollars", "$2,480 plus 12% of the excess over $24,800")):
    NEW[f"tcw.mfj.b0.{_f}"] = (_t, PP.tcw_cell(_mfj, _f), RP, 10, "section 4.01, Table 1 (married filing jointly and surviving spouses)", _q,
        "Tax Computation Worksheet Section B row for $100,000 to $100,800 (changes/2026/tcw.yaml, BUG-0647)"
        + ("; derived: rate x lower limit ($24,800) less base ($2,480)" if _f == "subtract" else "")
        + "; the 2026 worksheet (Form 1040 instructions, not posted) is to confirm the row")

RETIRED = {"sc.mileage_rate":"replaced by sc.mileage_rate_h1 (72.5 cents) and sc.mileage_rate_h2 (76 cents), Rate values in dollars per mile (C-BUS-01; owner decision 2026-11-04)",
           "ptc.repay_200": "the repayment limitation of section 36B(f)(2)(B) is removed for taxable years beginning after 2025 (rp-25-32 p. 4, section 2.04, final); the 2026 operations remove its Form 8962 lines, so no 2026 line reads it (C-PEOP-12, lane O6)",
           "ptc.repay_300": "as ptc.repay_200",
           "ptc.repay_400": "as ptc.repay_200",
           "sc.bonus_rate_40": "replaced by sc.bonus_rate_phase_down (20% in 2026, rp-26-15 p. 2); no 2026 line reads it (C-BUS-04, lane O9)"}
for _p in ("f5695.rce_rate", "f5695.eehi_rate", "f5695.insulation_max", "f5695.door_max", "f5695.doors_max", "f5695.windows_max",
           "f5695.item_max", "f5695.audit_max", "f5695.annual_max", "f5695.heat_pump_max"):
    RETIRED[_p] = ("no 2026 line reads it: Form 5695 keeps only carryforwards in 2026, and the operations of lane O3a (C-CRED-01 to -09) "
                   "remove its readers (checked by applying them in memory)")

# ---- Enumerations whose 2026 values or citations differ from params/2025.yaml ----
E25 = yaml.safe_load((ROOT / "params/2025.yaml").read_text())["params"]["enums"]
ENUMS = {
 "retirement_account": {"values": E25["retirement_account"]["values"] + ["trump"],
     "cite": {"doc": "f1099r", "locator": "Form 1099-R (2026), box 7c, \"Trump account\" (draft); Instructions for Recipient, code G, "
              "\"a direct rollover of the entire balance of a Trump account to an ABLE account\"; i1040gi pp. 26-28, lines 4a, 4b, 5a and 5b (2025)"},
     "note": "gains trump (read by the gate retirement.trump, C-PEOP-04+C-PEOP-11, lane O2)"},
 "early_exception": {"values": E25["early_exception"]["values"],
     "cite": {"doc": "i5329", "locator": "p. 5, Line 2, \"enter the applicable exception number (01–24)\" (draft); none when no exception "
              "applies (more than one exception is refused by the entry screen)"},
     "note": "the instructions number exceptions 01 to 24; exception 24 stays refused, so no e24 (C-PEOP-05, lane O2 decision 2)"},
 "bonus_choice": {"values": [v for v in E25["bonus_choice"]["values"] if v != "forty"],
     "cite": E25["bonus_choice"]["cite"],
     "note": "loses forty: the 40% election is not offered in 2026 (C-BUS-04, lane O9); the cite stays i4562 (2025) until the 2026 edition posts"},
 "carloan_kind": {"values": E25["carloan_kind"]["values"],
     "cite": {"doc": "fr-2026-18219", "locator": "p. 24, § 1.163-16(d)(4) (refinancing of an SPVL) and (d)(5) (whether the SPVL "
              "was incurred by the taxpayer; change in obligor by reason of death)"},
     "note": "values unchanged; the cite moves from the proposed regulations (fr-2025-24154) to the final, T.D. 10054 (C-SCHED-40)"},
 "placed_year": {"values": E25["placed_year"]["values"] + ["y2026"], "cite": E25["placed_year"]["cite"],
     "extends_with_year": True, "note": "gains y2026 at adoption (tools/year_diff.py --adopt, extends_with_year)"},
}
for k, e in ENUMS.items():
    assert k in E25, k

# ---- The mechanical proposal (tools/propose_params.py --from 2025 --to 2026 --write) for the rest ----
PROP = yaml.safe_load((ROOT / "reports/2026/params_proposal_from_2025.yaml").read_text())["proposal"]
sys.path.insert(0, str(Path(__file__).parent))
from check_quotes import norm, pages as doc_pages


def page_of(doc, text):
    """The first page of the 2026 edition of doc that prints the text (either layer), or None."""
    n = norm(text)
    found = sorted({i + 1 for layer in doc_pages(2026, doc) for i, t in enumerate(layer) if n in t})
    return found[0] if found else None


def mechanical(pid, p25):
    """The staged entry of a parameter the proposal found, or None."""
    r = PROP.get(pid)
    if not r or r["status"] not in ("changed", "unchanged"):
        return None
    e = {"type": p25["type"], "value": r["value"]}
    if "moves_with_year" in p25:
        e["moves_with_year"] = p25["moves_with_year"]
    ev = (r.get("evidence") or [None])[0]
    if r.get("derived") and (ev is None or ev.get("how") != "derived"):
        # a year moved with the tax year: no 2026 document; the 2025 citation, to re-verify when its 2026 edition posts
        e.update(cite=p25["cite"], source="derived", derived=r["derived"],
                 note=f"{p25['cite']['doc']} 2025 citation (no 2026 reading); re-verify when the 2026 edition posts")
        return e
    if r.get("derived"):
        # a Tax Computation Worksheet row from the rate tables: cited at the hand-read rate of the same row
        rate = V.get(re.sub(r"\.(upper|subtract)$", ".rate", pid))
        _v, doc, page, heading, quote, _n = rate
        e.update(cite={"doc": doc, "locator": f"p. {page}, {heading}", "quote": quote},
                 source="draft" if MAN.get(doc, {}).get("draft") else "final", derived=r["derived"],
                 note=f"{ev['read']} (tools/propose_params.py); the 2026 Tax Computation Worksheet (Form 1040 instructions, "
                      "not posted) is to confirm the row" + ("; " + "; ".join(r["notes"]) if r.get("notes") else ""))
        return e
    quote = ev["read"][0]
    page = page_of(ev["doc"], quote)
    if page is None:
        # a word the layer text breaks ("ex ceed"): the quote's two sides of it, joined by an omission
        words = quote.split()
        cut = next((i for i in range(1, len(words)) if page_of(ev["doc"], " ".join(words[:i + 1])) is None), None)
        if cut is not None and cut + 1 < len(words):
            pre, post = " ".join(words[:cut]), " ".join(words[cut + 1:])
            pages_pre = {i + 1 for layer in doc_pages(2026, ev["doc"]) for i, t in enumerate(layer)
                         if norm(pre) in t and norm(post) in t}
            if pages_pre:
                quote, page = f"{pre} ... {post}", min(pages_pre)
    if page is None:
        return None
    e.update(cite={"doc": ev["doc"], "locator": f"p. {page}, read by tools/propose_params.py", "quote": quote},
             source="draft" if ev.get("draft") else "final",
             note="read by tools/propose_params.py at the place the 2025 citation names")
    return e

def fmt_value(t, v):
    return v

out_vals, unsourced = {}, []
for pid, p25 in P25["values"].items():
    if pid in RETIRED:
        continue
    if pid in V:
        value, doc, page, heading, quote, note = V[pid]
        status = "draft" if MAN.get(doc, {}).get("draft") else "final"
        e = {"type": p25["type"], "value": value, "cite": {"doc": doc, "locator": f"p. {page}, {heading}", "quote": quote},
             "source": status}
        if note: e["note"] = note
    elif pid in AUTO:
        a = AUTO[pid]
        status = "draft" if MAN.get(a["doc"], {}).get("draft") else "final"
        heading = a["heading"].replace("(2025)", "(2026)")
        e = {"type": p25["type"], "value": p25["value"], "cite": {"doc": a["doc"], "locator": f"p. {a['page']}, {heading}", "quote": a["quote"]},
             "source": status, "note": "2025 quote printed unchanged in the 2026 edition"}
    elif pid not in NONE_NOTES and mechanical(pid, p25):
        e = mechanical(pid, p25)
    else:
        e = {"type": p25["type"], "value": None, "source": "none",
             "note": NONE_NOTES.get(pid, f"2025 source `{p25['cite']['doc']}` has no 2026 edition archived and no other archived 2026 source prints this value")}
        unsourced.append(pid)
    out_vals[pid] = e

for pid, (t, value, docid, page, heading, quote, note) in NEW.items():
    assert pid not in P25["values"], pid
    status = "draft" if MAN.get(docid, {}).get("draft") else "final"
    out_vals[pid] = {"type": t, "value": value, "cite": {"doc": docid, "locator": f"p. {page}, {printed_anchor(docid, heading)}", "quote": quote},
                     "source": status, "new_in_2026": True, "note": note}
    if pid == "tcw.mfj.b0.subtract":
        out_vals[pid]["derived"] = "the 2026 rate table row at the worksheet row's rate (upper limit; rate; rate x lower limit less base)"

for pid, rule in DERIVED_V.items():
    out_vals[pid]["derived"] = rule

doc ={"params": {"tax_year": 2026, "status": "proposed (research/ty2026; not read by the build)",
                  "enums": {"note": "every enumeration of params/2025.yaml unchanged except those below (each in full, with its "
                                    "2026 citation) and the Form 5695 enumerations, which follow the operations of C-CRED-01 to -08",
                            "changed": ENUMS},
                  "values": out_vals,
                  "unsourced": unsourced,
                  "retired": RETIRED}}
header = ("# Proposed 2026 parameters (TY2026 step 4). Generated by research/ty2026/build_params.py; checked by\n"
          "# research/ty2026/check_params.py. source: final (a final 2026 document or the statute as printed), draft\n"
          "# (an IRS 2026 draft: re-verify against the final), none (no archived 2026 source prints the value), derived\n"
          "# (moved with the year from the 2025 value, `moves_with_year`). `derived` on an entry names the rule.\n"
          "# Amounts are in cents, as in params/2025.yaml. Not read by the build; nothing here is adopted.\n")
(ROOT / "research/ty2026/params-2026.proposed.yaml").write_text(header + yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=120))
import collections
c = collections.Counter(e["source"] for e in out_vals.values())
print(dict(c), "unsourced:", len(unsourced))
