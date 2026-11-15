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

# id -> (value, doc, page, locator heading, quote, note)
V = {}
def put(pid, value, doc, page, heading, quote, note=None):
    assert pid in P25["values"], pid
    V[pid] = (value, doc, page, heading, quote, note)

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
put("qbi.threshold", {"single": D(201750), "hoh": D(201750), "qss": D(201750), "mfs": D(201775), "mfj": D(403500)}, "f8995", 2,
    "Form 8995 (2026), line 1 caption", "is at or below $201,750 ($201,775 if married filing separately; $403,500 if married filing jointly)",
    "draft form; the same amounts are in rp-25-32 section 4.26 (final). The 2025 value used one amount for married filing separately and single; 2026 does not")
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
put("sa.salt_threshold", {"single": D(505000), "hoh": D(505000), "qss": D(505000), "mfj": D(505000), "mfs": D(252500)}, "f1040sa", 2,
    "Schedule A (2026), line 5e", "$505,000 ($252,500 if married filing separately)",
    "draft form; the statute (plaw-119-21 p. 99, final) prints '$505,000' and 'half the threshold amount in the case of a married individual filing a separate return'")
put("sa.salt_floor", D(10000), "plaw-119-21", 99, "section 164(b)(7)(B)(iii)", "shall not result in the applicable limitation amount being less than $10,000.")
put("sa.salt_rate", R(3, 10), "plaw-119-21", 99, "section 164(b)(7)(B)(i)", "the applicable limitation amount shall be reduced by 30 percent of the excess")
put("sa.half", R(1, 2), "plaw-119-21", 99, "section 164(b)(7)(B)(i)", "half the threshold amount in the case of a married individual filing a separate return",
    "the 2025 parameter halves the limitation; the statute halves both the limitation and the threshold: the encoding's use of sa.half must be checked against the 2026 Schedule A instructions")

# ---- Drafts with a changed amount ----
put("dc.exclusion_max", D(7500), "i2441", 7, "Line 21",
    "The maximum amount is increased to $7,500 (previously $5,000). For married employees filing separate returns",
    "the instruction for the line that reads it (lane O4); What's New (p. 2) prints the same amount")
put("f5329.cap_abuse", D(10500), "p590b", 29, "Distributions to domestic abuse victims", "must not exceed the lesser of $10,500 for 2026 or 50% of the present value of the IRA.")
put("ctc.threshold", ST(200000, 400000, 200000, 200000, 200000), "f1040s8812", 1, "Schedule 8812 (2026), line 9",
    "Married filing jointly—$400,000 . . . . . . . . . . . . . . . . . . . . . . • All other filing statuses—$200,000")
put("ptc.months", 12, "i1095a", 3, "Part III", "Add the amounts on lines 21 through 32 and enter on line 33.", "structural: twelve monthly lines")
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

put("ira.limit_50", D(8600), "i8606", 6, "IRA contribution limit", "the smaller of $7,500 ($8,600 if age 50 or older at the end of 2026) or your taxable compensation",
    "the 2025 value cites the IRA Deduction Worksheet (Form 1040 instructions, not posted)")
KBH = "combined taxable compensation of both you and your spouse is less than $15,000 ($16,100 if one spouse is age 50 or older at the end of 2026; $17,200 if both spouses are age 50 or older at the end of 2026"
put("ira.kbh_none", D(15000), "i8606", 6, "Kay Bailey Hutchison Spousal IRA limit", KBH)
put("ira.kbh_one", D(16100), "i8606", 6, "Kay Bailey Hutchison Spousal IRA limit", KBH)
put("ira.kbh_both", D(17200), "i8606", 6, "Kay Bailey Hutchison Spousal IRA limit", KBH)

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
 "sli.divisor_other": "rp-25-32 section 4.29 prints the range ($85,000 to $100,000) but not its width, which the worksheet (Form 1040 instructions, not posted) prints",
 "sli.divisor_joint": "as sli.divisor_other ($175,000 to $205,000)",
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
    elif mechanical(pid, p25):
        e = mechanical(pid, p25)
    else:
        e = {"type": p25["type"], "value": None, "source": "none",
             "note": NONE_NOTES.get(pid, f"2025 source `{p25['cite']['doc']}` has no 2026 edition archived and no other archived 2026 source prints this value")}
        unsourced.append(pid)
    out_vals[pid] = e

for pid, (t, value, docid, page, heading, quote, note) in NEW.items():
    assert pid not in P25["values"], pid
    status = "draft" if MAN.get(docid, {}).get("draft") else "final"
    out_vals[pid] = {"type": t, "value": value, "cite": {"doc": docid, "locator": f"p. {page}, {heading}", "quote": quote},
                     "source": status, "new_in_2026": True, "note": note}
    if pid == "tcw.mfj.b0.subtract":
        out_vals[pid]["derived"] = "the 2026 rate table row at the worksheet row's rate (upper limit; rate; rate x lower limit less base)"

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
