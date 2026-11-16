"""Generate forms/2025/k1p.yaml (lane x2-k1p). Run: python3 gen_k1p.py <worktree>."""
import sys, yaml

WT = sys.argv[1]
L = []  # lines


def cite(doc, loc):
    return {"doc": doc, "locator": loc}


def line(id, printed, label, typ, expr, c, **kw):
    d = {"id": "k1p." + id, "printed": printed, "label": label, "type": typ, "expr": expr, "cite": c}
    d.update(kw)
    L.append(d)


def inp(id, label, typ, source, c, gated_by=None, printed="(helper)"):
    kw = {}
    if gated_by:
        kw["gated_by"] = "k1p." + gated_by
    line(id, printed, label, typ, {"op": "input", "source": source}, c, **kw)


def eqt(a, v):
    return {"op": "test", "eq": [a if "." in a else "k1p." + a, {"const": v}]}


def cmp(op, a, v):
    return {"op": "test", op: [a if "." in a else "k1p." + a, {"const": v}]}


def q(x):
    return x if "." in x else "k1p." + x


def gate(id, label, typ, cond, then, els, c, cond_true=True):
    """choose: cond == cond_true -> then; else -> els."""
    line(id, "(gate)", label, typ, {"op": "choose", "alternatives": [
        {"guard": eqt(cond, cond_true), "then": q(then)},
        {"guard": eqt(cond, not cond_true), "then": q(els)}]}, c)


def choose_bool(id, label, typ, cond, then, els, c, printed="(helper)"):
    line(id, printed, label, typ, {"op": "choose", "alternatives": [
        {"guard": eqt(cond, True), "then": q(then)},
        {"guard": eqt(cond, False), "then": q(els)}]}, c)


def all_(id, label, tests, c):
    line(id, "(helper)", label, "Bool", {"op": "test", "all": tests}, c)


def any_(id, label, tests, c):
    line(id, "(helper)", label, "Bool", {"op": "test", "any": tests}, c)


def pos(id, label, x, c, printed="(helper)"):
    line(id, printed, label, "NonNegDollars", {"op": "subtract_floor0", "from": q(x), "take": "k1p.zero"}, c)


def neg(id, label, x, c, printed="(helper)"):
    line(id, printed, label, "NonNegDollars", {"op": "subtract_floor0", "from": "k1p.zero", "take": q(x)}, c)


def sum_(id, label, xs, c, typ="NonNegDollars", printed="(helper)"):
    line(id, printed, label, typ, {"op": "sum", "of": [q(x) for x in xs]}, c)


# ---------------------------------------------------------------- citations
C_FORM = cite("f1065sk1", 'p. 1, Part III, "Partner’s Share of Current Year Income"')
C_LINE28 = cite("i1065sk1", 'p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E"')
C_D = cite("i1065sk1", 'p. 11, Item D, "If the box in item D is checked, you’re a partner in a PTP"')
C_PTP = cite("i1065sk1", 'p. 10, Publicly traded partnerships (PTPs), "Don’t report passive income, gains, or losses from a PTP on Form 8582"')
C_GP = cite("i1065sk1", 'p. 2, General Partner, "A general partner is a partner who is personally liable for partnership debts"')
C_B1 = cite("i1065sk1", 'p. 14, Box 1. Ordinary Business Income (Loss), "The amount reported in box 1 is your share of the ordinary income (loss) from trade or business activities of the partnership"')
C_B1_MP = cite("i1065sk1", 'p. 14, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from partnership trade or business activities in which you materially participated in column (i) or (k)"')
C_B1_NMP = cite("i1065sk1", 'p. 14, Box 1. Ordinary Business Income (Loss), "If income is reported in box 1, report the income in column (h)"')
C_B2 = cite("i1065sk1", 'p. 14, Box 2. Net Rental Real Estate Income (Loss), "Generally, the income (loss) reported in box 2 is a passive activity amount for all partners"')
C_B3 = cite("i1065sk1", 'p. 14, Box 3. Other Net Rental Income (Loss), "The amount in box 3 is a passive activity amount for all partners"')
C_B4A = cite("i1065sk1", 'p. 15, Box 4a. Guaranteed Payments for Services, "you should report them in column (k) of Schedule E (Form 1040), line 28"')
C_B4B = cite("i1065sk1", 'p. 15, Box 4b. Guaranteed Payments for Capital, "These are guaranteed payments other than for services"')
C_B5 = cite("i1065sk1", 'p. 15, Box 5. Interest Income, "Report interest income on Form 1040 or 1040-SR, line 2b"')
C_B6A = cite("i1065sk1", 'p. 15, Box 6a. Ordinary Dividends, "Report ordinary dividends on Form 1040 or 1040-SR, line 3b"')
C_B6B = cite("i1065sk1", 'p. 15, Box 6b. Qualified Dividends, "Report any qualified dividends on Form 1040 or 1040-SR, line 3a"')
C_B7 = cite("i1065sk1", 'p. 15, Box 7. Royalties, "Report royalties on Schedule E (Form 1040), line 4"')
C_B8 = cite("i1065sk1", 'p. 15, Box 8. Net Short-Term Capital Gain (Loss), "Report the net short-term capital gain (loss) on Schedule D (Form 1040), line 5"')
C_B9A = cite("i1065sk1", 'p. 15, Box 9a. Net Long-Term Capital Gain (Loss), "Report the net long-term capital gain (loss) on Schedule D (Form 1040), line 12"')
C_B9B = cite("i1065sk1", 'p. 16, Box 9b. Collectibles (28%) Gain (Loss), "Report collectibles gain or loss on line 4 of the 28% Rate Gain Worksheet"')
C_B9C = cite("i1065sk1", 'p. 16, Box 9c. Unrecaptured Section 1250 Gain, "If the partnership reports only unrecaptured section 1250 gain from the sale or exchange of its business assets, it’ll enter a dollar amount in box 9c"')
C_B10 = cite("i1065sk1", 'p. 16, Box 10. Net Section 1231 Gain (Loss), "report it in column (g) of Form 4797, line 2"')
C_B11 = cite("i1065sk1", 'p. 16, Box 11. Other Income (Loss), "Code A. Other portfolio income (loss)"')
C_B12 = cite("i1065sk1", 'p. 18, Box 12. Section 179 Deduction, "to complete Part I of Form 4562"')
C_B13 = cite("i1065sk1", 'p. 18, Box 13. Other Deductions, "Codes A through G"')
C_B13AE = cite("i1065sk1", 'p. 21, Code AE. Deductions—portfolio income, "For taxpayers other than individuals"')
C_B14 = cite("i1065sk1", 'p. 21, Box 14. Self-Employment Earnings (Loss), "each of you must complete and file your own Schedule SE"')
C_B14A = cite("i1065sk1", 'p. 22, Code A. Net earnings (loss) from self-employment, "If the amount in this box is a loss, enter only the deductible amount on Schedule SE"')
C_B14BC = cite("i1065sk1", 'p. 22, Code B. Gross farming or fishing income, "Also use this amount to figure net earnings from self-employment under the farm optional method"')
C_B15 = cite("i1065sk1", 'p. 22, Box 15. Credits, "you must complete Form 8582-CR"')
C_B15O = cite("i1065sk1", 'p. 23, Code O. Backup withholding, "Include this amount in the total you enter on Form 1040 or 1040-SR, line 25c"')
C_B16 = cite("i1065sk1", 'p. 24, Box 16. International Transactions, "If the partnership checked the box, see the attached Schedule K-3"')
C_B17 = cite("i1065sk1", 'p. 24, Box 17. Alternative Minimum Tax (AMT) Items, "to prepare your Form 6251"')
C_B18A = cite("i1065sk1", 'p. 25, Code A. Tax-exempt interest income, "Individual partners include this amount on Form 1040 or 1040-SR, line 2a"')
C_B19 = cite("i1065sk1", 'p. 25, Box 19. Distributions, "Code A. Cash and marketable securities other than for services"')
C_B19GAIN = cite("i1065sk1", 'p. 25, Box 19. Distributions, "exceed the adjusted basis of your partnership interest immediately before the distribution, the excess is treated as gain from the sale or exchange of your partnership interest"')
C_B20AB = cite("i1065sk1", 'p. 27, Code A. Investment income, "Report this amount on Form 4952, Part II, line 4a"')
C_B20Z = cite("i1065sk1", 'p. 29, Code Z. Section 199A information, "The partnership will provide the information you need to figure your deduction"')
C_B20Z_OTHER = cite("i1065sk1", 'p. 30, Section 199A dividends, "The amount reported reflects your distributive share of the partnership’s net section 199A dividends"')
C_B21 = cite("i1065sk1", 'p. 32, Box 21. Foreign Taxes Paid or Accrued, "Foreign taxes paid or accrued reduce a partner’s basis"')
C_B2223 = cite("i1065sk1", 'p. 9, Material participation, "If the partnership had more than one activity, it’ll attach a statement to your Schedule K-1 that identifies each activity"')
C_FOREIGN = cite("i1040se", 'p. 9, Foreign Partnerships, "you may have to file Form 8865"')
C_SALE = cite("i1065sk1", 'p. 2, Sale or Exchange of Partnership Interest, "Generally, a partner who sells or exchanges a partnership interest"')
C_LIMITS = cite("i1065sk1", 'p. 3, Limitations on Losses, Deductions, and Credits, "the basis limitations, the at-risk limitations, the passive activity limitations, and the excess business loss limitations"')
C_BASIS = cite("i1065sk1", 'p. 3, Basis Limitations, "a partner may only claim their share of a partnership loss (including a capital loss) to the extent it doesn’t exceed their adjusted basis in the partnership"')
C_ATRISK = cite("i1065sk1", 'p. 8, At-Risk Limitations, "you’ll have to complete Form 6198, At-Risk Limitations, to figure your allowable loss for the activity"')
C_MP = cite("i1065sk1", 'p. 9, Material participation, "You must determine if you materially participated (a) in each trade or business activity held through the partnership"')
C_MP_WORK = cite("i1065sk1", 'p. 9, Work counted toward material participation, "any work that you or your spouse does in connection with an activity held through a partnership"')
C_MP1 = cite("i1065sk1", 'p. 9, Individuals (other than limited partners), "You participated in the activity for more than 500 hours during the tax year"')
C_MP2 = cite("i1065sk1", 'p. 9, Individuals (other than limited partners), "constituted substantially all the participation in the activity of all individuals"')
C_MP3 = cite("i1065sk1", 'p. 9, Individuals (other than limited partners), "You participated in the activity for more than 100 hours during the tax year, and your participation in the activity for the tax year wasn’t less than the participation in the activity of any other individual"')
C_MP4 = cite("i1065sk1", 'p. 9, Individuals (other than limited partners), "The activity was a significant participation activity for the tax year"')
C_MP5 = cite("i1065sk1", 'p. 9, Individuals (other than limited partners), "You materially participated in the activity for any 5 tax years (whether or not consecutive) during the 10 tax years that immediately precede the tax year"')
C_MP6 = cite("i1065sk1", 'p. 9, Individuals (other than limited partners), "The activity was a personal service activity and you materially participated in the activity for any 3 tax years"')
C_MP7 = cite("i1065sk1", 'p. 9, Individuals (other than limited partners), "Based on all the facts and circumstances, you participated in the activity on a regular, continuous, and substantial basis during the tax year"')
C_LP = cite("i1065sk1", 'p. 9, Limited partners, "If you’re a limited partner, you must meet item 1, 5, or 6 above to qualify as having materially participated"')
C_EFFECT = cite("i1065sk1", 'p. 9, Effect of determination, "If you determine that you didn’t materially participate in a trade or business activity of the partnership"')
C_TRADER = cite("i1065sk1", 'p. 11, Special rules for certain other activities, "Trading personal property for the account of owners of interests in the activity"')
C_ACTIVE = cite("i1065sk1", 'p. 11, Special allowance for a rental real estate activity, "Management decisions that can count as active participation include approving new tenants, deciding rental terms, approving capital or repair expenditures"')
C_TENTH = cite("i1065sk1", 'p. 11, Special allowance for a rental real estate activity, "your interest (including your spouse’s interest) in the activity was less than 10% (by value) of all interests in the activity"')
C_LPACTIVE = cite("i1065sk1", 'p. 11, Special allowance for a rental real estate activity, "Limited partners can’t actively participate unless future regulations provide an exception"')
C_PART4 = cite("i8582", 'p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV"')
C_PART5 = cite("i8582", 'p. 9, Part V, "Use Part V for all other passive activities"')
C_COLS = cite("i8582", 'p. 10, Part IV, "You find these amounts in Part VII, column (c), of your 2024 Form 8582"')
C_COLDE = cite("i8582", 'p. 10, Columns (d) and (e), "Combine income and losses in columns (a) through (c) for each activity"')
C_PRIOR_ACTIVE = cite("i8582", 'p. 10, Part IV, "Don’t enter a prior-year unallowed loss in column (c) of Part IV unless you actively participated in the activity in both the year the loss arose and the current tax year"')
C_FORMER = cite("i8582", 'p. 8, Former Passive Activities, "A prior-year unallowed loss from a former passive activity is allowed to the extent of current year income from the activity"')
C_PASSIVE_INC = cite("i1065sk1", 'p. 9, Effect of determination, "Report passive income (losses), deductions, and credits as follows"')
C_QBI = cite("i8995", 'p. 3, Line 1, "Losses and deductions retain their status"')
C_E28 = cite("i1040se", 'p. 10, Line 28, "For nonpassive income or loss and passive income or losses for which you are not filing Form 8582"')

# ---------------------------------------------------------------- helpers
line("zero", "(helper)", "Zero", "NonNegDollars", {"op": "param", "ref": "sales.zero"}, C_FORM)
line("no", "(helper)", "No (false)", "Bool", {"op": "param", "ref": "household.no"}, C_FORM)
line("yes", "(helper)", "Yes (true)", "Bool", {"op": "param", "ref": "hsa.yes"}, C_FORM)
line("one", "(helper)", "One Schedule K-1", "Count", {"op": "param", "ref": "person.one"}, C_LINE28)

# ---------------------------------------------------------------- item D, item G
inp("ptp", "Publicly traded partnership (item D checked)", "Bool",
    "Is the box in item D checked, for a publicly traded partnership (PTP)?", C_D)
inp("general", "General partner or LLC member-manager (item G)", "Bool",
    "In item G, is the first box checked: general partner or LLC member-manager?", C_GP)

# ---------------------------------------------------------------- box screens (tick boxes) and amounts
BOXES = [  # id, tick label (label), amount type, amount source, cite, printed
    ("b1", "Box 1 shows an amount: ordinary business income (loss)", "Dollars",
     "The amount in box 1, ordinary business income (loss). Enter a loss as a negative amount.", C_B1, "1"),
    ("b2", "Box 2 shows an amount: net rental real estate income (loss)", "Dollars",
     "The amount in box 2, net rental real estate income (loss). Enter a loss as a negative amount.", C_B2, "2"),
    ("b3", "Box 3 shows an amount: other net rental income (loss)", "Dollars",
     "The amount in box 3, other net rental income (loss). Enter a loss as a negative amount.", C_B3, "3"),
    ("b4a", "Box 4a shows an amount: guaranteed payments for services", "NonNegDollars",
     "The amount in box 4a, guaranteed payments for services.", C_B4A, "4a"),
    ("b5", "Box 5 shows an amount: interest income", "NonNegDollars",
     "The amount in box 5, interest income.", C_B5, "5"),
    ("b6a", "Box 6a shows an amount: ordinary dividends", "NonNegDollars",
     "The amount in box 6a, ordinary dividends.", C_B6A, "6a"),
    ("b8", "Box 8 shows an amount: net short-term capital gain (loss)", "Dollars",
     "The amount in box 8, net short-term capital gain (loss). Enter a loss as a negative amount.", C_B8, "8"),
    ("b9a", "Box 9a shows an amount: net long-term capital gain (loss)", "Dollars",
     "The amount in box 9a, net long-term capital gain (loss). Enter a loss as a negative amount.", C_B9A, "9a"),
    ("b14a", "Box 14 shows an amount with code A: net earnings from self-employment", "Dollars",
     "The amount in box 14 with code A, net earnings (loss) from self-employment. Enter a loss as a negative amount.", C_B14A, "14 A"),
    ("b15o", "Box 15 shows an amount with code O: backup withholding", "NonNegDollars",
     "The amount in box 15 with code O, backup withholding.", C_B15O, "15 O"),
    ("b18a", "Box 18 shows an amount with code A: tax-exempt interest income", "NonNegDollars",
     "The amount in box 18 with code A, tax-exempt interest income.", C_B18A, "18 A"),
    ("b20z", "Box 20 shows code Z: section 199A information", "Dollars",
     "From the statement for box 20, code Z (section 199A information): the qualified business income (QBI) or loss, all trades or businesses together. Enter a loss as a negative amount.", C_B20Z, "20 Z"),
]
TICK_SRC = {
    "b1": "Does box 1 (ordinary business income or loss) show an amount?",
    "b2": "Does box 2 (net rental real estate income or loss) show an amount?",
    "b3": "Does box 3 (other net rental income or loss) show an amount?",
    "b4a": "Does box 4a (guaranteed payments for services) show an amount?",
    "b5": "Does box 5 (interest income) show an amount?",
    "b6a": "Does box 6a (ordinary dividends) show an amount?",
    "b8": "Does box 8 (net short-term capital gain or loss) show an amount?",
    "b9a": "Does box 9a (net long-term capital gain or loss) show an amount?",
    "b14a": "Does box 14 show an amount with code A (net earnings from self-employment)?",
    "b15o": "Does box 15 show an amount with code O (backup withholding)?",
    "b18a": "Does box 18 show an amount with code A (tax-exempt interest income)?",
    "b20z": "Does box 20 show code Z (section 199A information)?",
}
for bid, lab, typ, src, c, printed in BOXES:
    inp("has_" + bid, lab, "Bool", TICK_SRC[bid], c)
    amt = "box" + bid[1:]
    zero = "zero" if typ == "NonNegDollars" else "zero"
    inp(amt, lab.split(": ", 1)[1].capitalize() if ": " in lab else lab, typ, src, c,
        gated_by=amt + "_if_any", printed=printed)
    gate(amt + "_if_any", f"Box {printed}, asked only when the box shows an amount (zero otherwise)", typ,
         "has_" + bid, amt, "zero", c)

# box 6b under 6a; boxes 9b, 9c under 9a
inp("box6b", "Qualified dividends", "NonNegDollars",
    "The amount in box 6b, qualified dividends (0 if the box is blank).", C_B6B,
    gated_by="box6b_if_any", printed="6b")
gate("box6b_if_any", "Box 6b, asked only when box 6a shows an amount (zero otherwise)", "NonNegDollars",
     "has_b6a", "box6b", "zero", C_B6B)
inp("has_b9bc", "Box 9b or 9c shows an amount", "Bool",
    "Does box 9b (collectibles 28% gain) or box 9c (unrecaptured section 1250 gain) show an amount?", C_B9B,
    gated_by="has_b9bc_if_9a")
gate("has_b9bc_if_9a", "Asked only when box 9a shows an amount (false otherwise)", "Bool",
     "has_b9a", "has_b9bc", "no", C_B9B)
inp("box9b", "Collectibles (28%) gain", "NonNegDollars",
    "The amount in box 9b, collectibles (28%) gain (0 if the box is blank).", C_B9B,
    gated_by="box9b_if_any", printed="9b")
gate("box9b_if_any", "Box 9b, asked only when box 9b or 9c shows an amount (zero otherwise)", "NonNegDollars",
     "has_b9bc_if_9a", "box9b", "zero", C_B9B)
inp("box9c", "Unrecaptured section 1250 gain", "NonNegDollars",
    "The amount in box 9c, unrecaptured section 1250 gain (0 if the box is blank).", C_B9C,
    gated_by="box9c_if_any", printed="9c")
gate("box9c_if_any", "Box 9c, asked only when box 9b or 9c shows an amount (zero otherwise)", "NonNegDollars",
     "has_b9bc_if_9a", "box9c", "zero", C_B9C)

# box 19, box 20 A/B (yes/no facts)
inp("has_b19", "Box 19 shows an amount: distributions", "Bool",
    "Does box 19 (distributions) show an amount?", C_B19)
inp("has_b20ab", "Box 20 shows code A or B: investment income or expenses", "Bool",
    "Does box 20 show code A (investment income) or code B (investment expenses)?", C_B20AB)

# refusing box screens (asked of every K-1)
RARE = [
    ("r_b4b", "Box 4b shows an amount: guaranteed payments for capital",
     "Does box 4b (guaranteed payments for capital) show an amount?", C_B4B,
     "Schedule K-1 (Form 1065) box 4b (guaranteed payments for capital)"),
    ("r_b7", "Box 7 shows an amount: royalties", "Does box 7 (royalties) show an amount?", C_B7,
     "Schedule K-1 (Form 1065) box 7 (royalties on Schedule E, line 4)"),
    ("r_b10", "Box 10 shows an amount: net section 1231 gain (loss)",
     "Does box 10 (net section 1231 gain or loss) show an amount?", C_B10,
     "Schedule K-1 (Form 1065) box 10 (Form 4797)"),
    ("r_b11", "Box 11 shows an amount: other income (loss)",
     "Does box 11 (other income or loss) show an amount?", C_B11,
     "Schedule K-1 (Form 1065) box 11 (other income or loss)"),
    ("r_b12", "Box 12 shows an amount: section 179 deduction",
     "Does box 12 (section 179 deduction) show an amount?", C_B12,
     "Schedule K-1 (Form 1065) box 12 (section 179 deduction, Form 4562)"),
    ("r_b13", "Box 13 shows an amount with a code other than AE",
     "Does box 13 (other deductions) show an amount with any code other than AE?", C_B13,
     "Schedule K-1 (Form 1065) box 13 (other deductions)"),
    ("r_b14bc", "Box 14 shows an amount with code B or C",
     "Does box 14 show an amount with code B (gross farming or fishing income) or code C (gross nonfarm income)?", C_B14BC,
     "Schedule K-1 (Form 1065) box 14, codes B and C (optional methods of Schedule SE)"),
    ("r_b15", "Box 15 shows an amount with a code other than O",
     "Does box 15 (credits) show an amount with any code other than O?", C_B15,
     "Schedule K-1 (Form 1065) box 15 (credits; Form 8582-CR, Form 3800)"),
    ("r_b16", "Box 16 is checked: Schedule K-3 is attached",
     "Is box 16 checked, showing that a Schedule K-3 is attached?", C_B16,
     "Schedule K-3 (international items)"),
    ("r_b17", "Box 17 shows an amount: alternative minimum tax items",
     "Does box 17 (alternative minimum tax items) show an amount?", C_B17,
     "Schedule K-1 (Form 1065) box 17 (Form 6251)"),
    ("r_b20", "Box 20 shows a code other than A, B, N, Z or AG",
     "Does box 20 show any code other than A, B, N, Z or AG?", C_B20Z,
     "Schedule K-1 (Form 1065) box 20, other information"),
    ("r_b21", "Box 21 shows an amount: foreign taxes paid or accrued",
     "Does box 21 (foreign taxes paid or accrued) show an amount?", C_B21,
     "Schedule K-1 (Form 1065) box 21 (foreign taxes; Form 1116)"),
    ("r_b2223", "Box 22 or box 23 is checked: more than one activity",
     "Is box 22 or box 23 checked, showing more than one activity (with a statement attached)?", C_B2223,
     "A partnership with more than one activity (boxes 22 and 23)"),
    ("r_foreign", "The partnership is a foreign partnership",
     "Is it a foreign partnership (one not created or organized in the United States)?", C_FOREIGN,
     "Schedule E, line 28, column (c) (foreign partnership; Form 8865)"),
    ("r_disposed", "You sold or gave up any of your share in 2025",
     "In 2025, did you sell, trade or give up any of your share of this partnership?", C_SALE,
     "Sale or other disposition of a partnership interest (Form 8949, section 751)"),
]
for rid, lab, src, c, form in RARE:
    inp(rid, lab, "Bool", src, c)

# box 19 code and basis; 20 Z detail
inp("b19_other", "Box 19 shows a code other than A", "Bool",
    "Does box 19 show any code other than A (cash and marketable securities)?", C_B19, gated_by="b19_other_if_any")
gate("b19_other_if_any", "Asked only when box 19 shows an amount (false otherwise)", "Bool",
     "has_b19", "b19_other", "no", C_B19)
inp("dist_over", "Distributions more than basis", "Bool",
    "Was the money you took out of it in 2025 (box 19) more than your basis in it just before you took it out?",
    C_B19GAIN, gated_by="dist_over_if_any")
gate("dist_over_if_any", "Asked only when box 19 shows an amount (false otherwise)", "Bool",
     "has_b19", "dist_over", "no", C_B19GAIN)
inp("z_other", "Section 199A statement shows section 199A dividends or a cooperative", "Bool",
    "Does the statement for code Z show section 199A dividends, or payments from a farm or garden cooperative?",
    C_B20Z_OTHER, gated_by="z_other_if_z")
gate("z_other_if_z", "Asked only when box 20 shows code Z (false otherwise)", "Bool",
     "has_b20z", "z_other", "no", C_B20Z_OTHER)

# ---------------------------------------------------------------- trading, material participation (box 1)
inp("trader", "The partnership's business is trading investments", "Bool",
    "Is the partnership's business trading stocks, commodities or other investments for its owners?", C_TRADER,
    gated_by="trader_if_b1")
gate("trader_if_b1", "Asked only when box 1 shows an amount (false otherwise)", "Bool",
     "has_b1", "trader", "no", C_TRADER)
inp("work", "Worked in the business in 2025", "Bool",
    "In 2025, did you (or, on a joint return, your spouse) do any work in the partnership's business?", C_MP_WORK, gated_by="work_if_b1")
gate("work_if_b1", "Asked only when box 1 shows an amount (false otherwise)", "Bool",
     "has_b1", "work", "no", C_MP_WORK)
inp("hours500", "More than 500 hours (test 1)", "Bool",
    "Did that work add up to more than 500 hours in 2025?", C_MP1, gated_by="hours500_if_work")
gate("hours500_if_work", "Asked only of a partner who worked in the business (false otherwise)", "Bool",
     "work_if_b1", "hours500", "no", C_MP1)
all_("under500", "Worked in the business, 500 hours or less",
     [eqt("work_if_b1", True), eqt("hours500_if_work", False)], C_MP)
all_("gp_under500", "A general partner who worked 500 hours or less",
     [eqt("under500", True), eqt("general", True)], C_LP)
inp("most_hours", "More than 100 hours and no one worked more (test 3)", "Bool",
    "Did you (or, on a joint return, your spouse) work in it more than 100 hours in 2025, and at least as many hours as anyone else, employees included?",
    C_MP3, gated_by="most_hours_if_gp")
gate("most_hours_if_gp", "Asked only of a general partner who worked 500 hours or less (false otherwise)", "Bool",
     "gp_under500", "most_hours", "no", C_MP3)
all_("ask_nearly_all", "A general partner who worked 500 hours or less and less than someone else",
     [eqt("gp_under500", True), eqt("most_hours_if_gp", False)], C_MP2)
inp("nearly_all", "Substantially all the work (test 2)", "Bool",
    "Did you (and, on a joint return, your spouse) do nearly all of the work in it in 2025, counting the work of employees and anyone else?",
    C_MP2, gated_by="nearly_all_if_asked")
gate("nearly_all_if_asked", "Asked only when test 3 is not met (false otherwise)", "Bool",
     "ask_nearly_all", "nearly_all", "no", C_MP2)
all_("ask_five", "Worked 500 hours or less and tests 2 and 3 not met",
     [eqt("under500", True), eqt("most_hours_if_gp", False), eqt("nearly_all_if_asked", False)], C_MP5)
inp("five_of_ten", "Materially participated in 5 of the 10 preceding years (test 5)", "Bool",
    "In at least 5 of the years 2015 to 2024, did you materially participate in this business (its income or loss was nonpassive on your return)?",
    C_MP5, gated_by="five_of_ten_if_asked")
gate("five_of_ten_if_asked", "Asked only when tests 1 to 3 are not met (false otherwise)", "Bool",
     "ask_five", "five_of_ten", "no", C_MP5)
all_("ask_other", "Worked in the business but met none of tests 1, 2, 3 and 5",
     [eqt("ask_five", True), eqt("five_of_ten_if_asked", False)], C_MP)
inp("t6", "Personal service activity, 3 earlier years (test 6)", "Bool",
    "Is it a business of services in health, law, engineering, architecture, accounting, actuarial science, performing arts or consulting, in which you materially participated in any 3 years before 2025?",
    C_MP6, gated_by="t6_if_asked")
gate("t6_if_asked", "Asked only when tests 1, 2, 3 and 5 are not met (false otherwise)", "Bool",
     "ask_other", "t6", "no", C_MP6)
all_("ask_other_gp", "A general partner who met none of tests 1, 2, 3 and 5",
     [eqt("ask_other", True), eqt("general", True)], C_LP)
inp("t4", "Significant participation activities over 500 hours (test 4)", "Bool",
    "In 2025, did your work in it and in other businesses where you worked more than 100 hours add up to more than 500 hours?",
    C_MP4, gated_by="t4_if_gp")
gate("t4_if_gp", "Asked only of a general partner who met none of tests 1, 2, 3 and 5 (false otherwise)", "Bool",
     "ask_other_gp", "t4", "no", C_MP4)
inp("t7", "Regular, continuous and substantial participation (test 7)", "Bool",
    "Did you work in it in 2025 on a regular, continuous and substantial basis, for more than 100 hours?",
    C_MP7, gated_by="t7_if_gp")
gate("t7_if_gp", "Asked only of a general partner who met none of tests 1, 2, 3 and 5 (false otherwise)", "Bool",
     "ask_other_gp", "t7", "no", C_MP7)
any_("material", "Materially participated in the trade or business (box 1) by test 1, 2, 3 or 5",
     [eqt("hours500_if_work", True), eqt("most_hours_if_gp", True), eqt("nearly_all_if_asked", True),
      eqt("five_of_ten_if_asked", True)], C_MP)

# ---------------------------------------------------------------- active participation (box 2)
all_("ask_active", "Box 2 shows an amount and the partner is a general partner",
     [eqt("has_b2", True), eqt("general", True)], C_LPACTIVE)
inp("decisions", "Helped make management decisions for the rental real estate", "Bool",
    "Did you (or, on a joint return, your spouse) help make decisions for its rental real estate in 2025, such as approving tenants, rents or repairs?",
    C_ACTIVE, gated_by="decisions_if_asked")
gate("decisions_if_asked", "Asked only of a general partner with an amount in box 2 (false otherwise)", "Bool",
     "ask_active", "decisions", "no", C_ACTIVE)
inp("tenth", "Owned at least 10% by value all year", "Bool",
    "All through 2025, did you (and, on a joint return, your spouse) own at least a tenth (by value) of all the interests in that rental real estate?",
    C_TENTH, gated_by="tenth_if_decisions")
gate("tenth_if_decisions", "Asked only when the partner helped make management decisions (false otherwise)", "Bool",
     "decisions_if_asked", "tenth", "no", C_TENTH)
all_("active", "Actively participated in the rental real estate activity (box 2): Part IV of Form 8582",
     [eqt("decisions_if_asked", True), eqt("tenth_if_decisions", True)], C_PART4)

# ---------------------------------------------------------------- prior-year unallowed losses
any_("has_activity", "Box 1, 2 or 3 shows an amount",
     [eqt("has_b1", True), eqt("has_b2", True), eqt("has_b3", True)], C_COLS)
inp("prior_any", "A loss from this partnership held back on an earlier return", "Bool",
    "Was a loss from this partnership held back (not deducted) on your 2024 return or an earlier one, because of the passive activity rules?",
    C_COLS, gated_by="prior_any_if_activity")
gate("prior_any_if_activity", "Asked only when box 1, 2 or 3 shows an amount (false otherwise)", "Bool",
     "has_activity", "prior_any", "no", C_COLS)
PRIOR = [("1", "the business (box 1)"), ("2", "rental real estate (box 2)"), ("3", "other rentals (box 3)")]
for n, what in PRIOR:
    inp(f"prior_b{n}_any", f"Held-back loss from {what}", "Bool",
        f"Was any of that held-back loss from {what}?", C_COLS, gated_by=f"prior_b{n}_any_if")
    gate(f"prior_b{n}_any_if", "Asked only when a loss was held back (false otherwise)", "Bool",
         "prior_any_if_activity", f"prior_b{n}_any", "no", C_COLS)
    inp(f"prior_b{n}", f"Prior years unallowed loss, {what}", "NonNegDollars",
        f"The loss held back from {what}, from your 2024 Form 8582, Part VII, column (c)", C_COLS,
        gated_by=f"prior_b{n}_if")
    gate(f"prior_b{n}_if", "Asked only when a loss was held back from it (zero otherwise)", "NonNegDollars",
         f"prior_b{n}_any_if", f"prior_b{n}", "zero", C_COLS)
all_("former_passive", "A held-back loss from a business (box 1) the partner now materially participates in",
     [eqt("prior_b1_any_if", True), eqt("material", True)], C_FORMER)
all_("ask_prior_active", "A held-back rental real estate loss with active participation this year",
     [eqt("prior_b2_any_if", True), eqt("active", True)], C_PRIOR_ACTIVE)
inp("prior_not_active", "Part of the held-back rental loss arose in a year without active participation", "Bool",
    "Did any of the held-back rental real estate loss come from a year when you did not help make decisions for it, or owned less than a tenth of it?",
    C_PRIOR_ACTIVE, gated_by="prior_not_active_if")
gate("prior_not_active_if", "Asked only of a held-back rental loss with active participation (false otherwise)", "Bool",
     "ask_prior_active", "prior_not_active", "no", C_PRIOR_ACTIVE)

# ---------------------------------------------------------------- losses: basis and at-risk
any_("any_loss", "A loss in box 1, 2, 3, 8, 9a or 14 (code A)",
     [cmp("lt", "box1_if_any", 0), cmp("lt", "box2_if_any", 0), cmp("lt", "box3_if_any", 0),
      cmp("lt", "box8_if_any", 0), cmp("lt", "box9a_if_any", 0), cmp("lt", "box14a_if_any", 0)], C_LIMITS)
inp("basis_short", "Losses more than basis", "Bool",
    "Were your 2025 losses from it more than your basis in it at the end of its year? Basis is what you put in, plus your share of its income and debts, less losses and money taken out.",
    C_BASIS, gated_by="basis_short_if_loss")
gate("basis_short_if_loss", "Asked only when the K-1 shows a loss (false otherwise)", "Bool",
     "any_loss", "basis_short", "no", C_BASIS)
inp("not_at_risk", "Some investment not at risk", "Bool",
    "Was any of what you have in it protected from loss: money borrowed on a loan you are not personally liable for (other than a qualified real estate loan), or covered by a guarantee or stop-loss agreement?",
    C_ATRISK, gated_by="not_at_risk_if_loss")
gate("not_at_risk_if_loss", "Asked only when the K-1 shows a loss (false otherwise)", "Bool",
     "any_loss", "not_at_risk", "no", C_ATRISK)
all_("se_loss_not_material", "A self-employment loss (box 14, code A) without material participation in box 1",
     [cmp("lt", "box14a_if_any", 0), eqt("material", False)], C_B14A)

# ---------------------------------------------------------------- activities (Form 8582 Parts IV and V columns)
line("b1_passive", "(helper)", "Box 1 is passive (no material participation)", "Bool",
     {"op": "test", "eq": ["k1p.material", {"const": False}]}, C_EFFECT)
for n in "123":
    c = {"1": C_B1, "2": C_B2, "3": C_B3}[n]
    pos(f"b{n}_pos", f"Box {n} income", f"box{n}_if_any", c)
    neg(f"b{n}_neg", f"Box {n} loss", f"box{n}_if_any", c)
choose_bool("b1_net_income", "Box 1 passive net income: Form 8582 column (a)", "NonNegDollars",
            "b1_passive", "b1_pos", "zero", C_B1_NMP, printed="V (a)")
choose_bool("b1_net_loss", "Box 1 passive net loss: Form 8582 column (b)", "NonNegDollars",
            "b1_passive", "b1_neg", "zero", C_B1_NMP, printed="V (b)")
for n in "23":
    line(f"b{n}_net_income", "IV/V (a)" if n == "2" else "V (a)", f"Box {n} net income: Form 8582 column (a)",
         "NonNegDollars", {"op": "copy", "from": f"k1p.b{n}_pos"}, {"2": C_B2, "3": C_B3}[n])
    line(f"b{n}_net_loss", "IV/V (b)" if n == "2" else "V (b)", f"Box {n} net loss: Form 8582 column (b)",
         "NonNegDollars", {"op": "copy", "from": f"k1p.b{n}_neg"}, {"2": C_B2, "3": C_B3}[n])
for n in "123":
    sum_(f"b{n}_loss_sum", f"Box {n} activity: net loss plus prior years unallowed loss",
         [f"b{n}_net_loss", f"prior_b{n}_if"], C_COLDE)
    line(f"b{n}_overall_loss", "(e)", f"Box {n} activity: overall loss, Form 8582 column (e)", "NonNegDollars",
         {"op": "subtract_floor0", "from": f"k1p.b{n}_loss_sum", "take": f"k1p.b{n}_net_income"}, C_COLDE,
         **({} if n == "2" else {"display": "The activity's overall loss, which Form 8582 Part VII column (a) takes for a Part V activity."}))
# Part IV (box 2 with active participation) and Part V
choose_bool("p4_income", "Part IV column (a): box 2 net income with active participation", "NonNegDollars",
            "active", "b2_net_income", "zero", C_PART4, printed="IV (a)")
choose_bool("p4_loss", "Part IV column (b): box 2 net loss with active participation", "NonNegDollars",
            "active", "b2_net_loss", "zero", C_PART4, printed="IV (b)")
choose_bool("p4_prior", "Part IV column (c): box 2 prior years unallowed loss with active participation", "NonNegDollars",
            "active", "prior_b2_if", "zero", C_PART4, printed="IV (c)")
choose_bool("p6_loss", "Part VI column (a): box 2 overall loss with active participation", "NonNegDollars",
            "active", "b2_overall_loss", "zero", cite("i8582", 'p. 12, Part VI, "Enter the overall loss from column (e) of Part IV for each activity"'),
            printed="VI (a)")
choose_bool("p5_b2_income", "Box 2 net income without active participation (Part V)", "NonNegDollars",
            "active", "zero", "b2_net_income", C_PART5)
choose_bool("p5_b2_loss", "Box 2 net loss without active participation (Part V)", "NonNegDollars",
            "active", "zero", "b2_net_loss", C_PART5)
choose_bool("p5_b2_prior", "Box 2 prior years unallowed loss without active participation (Part V)", "NonNegDollars",
            "active", "zero", "prior_b2_if", C_PART5)
sum_("p5_income", "Part V column (a): net income of the passive activities other than Part IV",
     ["b1_net_income", "p5_b2_income", "b3_net_income"], C_PART5, printed="V (a)")
sum_("p5_loss", "Part V column (b): net loss of the passive activities other than Part IV",
     ["b1_net_loss", "p5_b2_loss", "b3_net_loss"], C_PART5, printed="V (b)")
sum_("p5_prior", "Part V column (c): prior years unallowed loss of the passive activities other than Part IV",
     ["prior_b1_if", "p5_b2_prior", "prior_b3_if"], C_PART5, printed="V (c)")
sum_("prior_total", "Prior years unallowed losses of this K-1", ["prior_b1_if", "prior_b2_if", "prior_b3_if"], C_COLS)
any_("passive_loss", "A passive activity of this K-1 has a net loss or a prior years unallowed loss",
     [cmp("gt", "b1_loss_sum", 0), cmp("gt", "b2_loss_sum", 0), cmp("gt", "b3_loss_sum", 0)],
     cite("i1065sk1", 'p. 9, Effect of determination, "If you have an overall loss (the excess of deductions and losses, including any prior-year unallowed loss, over income) or credits from a passive activity"'))

# ---------------------------------------------------------------- Schedule E line 28 columns (h), (i), (k)
sum_("col_h", "Passive income from Schedule K-1: Schedule E line 28 column (h)",
     ["b1_net_income", "b2_net_income", "b3_net_income"], C_B1_NMP, printed="28 (h)")
choose_bool("np_b1_income", "Box 1 income with material participation", "NonNegDollars",
            "b1_passive", "zero", "b1_pos", C_B1_MP)
sum_("col_k", "Nonpassive income from Schedule K-1: Schedule E line 28 column (k)",
     ["np_b1_income", "box4a_if_any"], C_B1_MP, printed="28 (k)")
choose_bool("col_i", "Nonpassive loss allowed: Schedule E line 28 column (i) (as a positive amount)", "NonNegDollars",
            "b1_passive", "zero", "b1_neg", C_B1_MP, printed="28 (i)")
line("nonpassive_net", "(helper)", "Nonpassive income less nonpassive loss (column (k) less column (i))", "Dollars",
     {"op": "subtract", "from": "k1p.col_k", "take": "k1p.col_i"}, C_B1_MP)
any_("sche_row", "The K-1 puts a row on Schedule E line 28 (an amount in box 1, 2, 3 or 4a, or a held-back loss)",
     [cmp("ne", "box1_if_any", 0), cmp("ne", "box2_if_any", 0), cmp("ne", "box3_if_any", 0),
      cmp("gt", "box4a_if_any", 0), cmp("gt", "prior_total", 0)], C_E28)
pos("se_pos", "Positive net earnings from self-employment (box 14, code A)", "box14a_if_any", C_B14A)

# ---------------------------------------------------------------- the screened line: every refusal of a K-1
REF = []


def ref(when, form, remedy, c):
    REF.append({"when": "k1p." + when, "form": form, "remedy": remedy, "cite": c})


ref("ptp", "Publicly traded partnership (Schedule K-1 item D)",
    "A Schedule K-1 from a publicly traded partnership is outside this tool.", C_PTP)
for rid, lab, src, c, form in RARE[:13]:
    ref(rid, form, f"A Schedule K-1 with this item is outside this tool.", c)
ref("r_foreign", RARE[13][4], "A Schedule K-1 from a foreign partnership is outside this tool.", C_FOREIGN)
ref("r_disposed", RARE[14][4], "A sale or other disposition of a partnership interest is outside this tool.", C_SALE)
ref("b19_other_if_any", "Schedule K-1 (Form 1065) box 19, codes other than A (distributions of property)",
    "A distribution of property other than money is outside this tool.", C_B19)
ref("dist_over_if_any", "Gain on a distribution above basis (Form 8949)",
    "Money taken out of a partnership above your basis is outside this tool.", C_B19GAIN)
ref("z_other_if_z", "Section 199A dividends or cooperative items from a partnership (Form 8995-A)",
    "Section 199A dividends or cooperative items from a partnership are outside this tool.", C_B20Z_OTHER)
ref("trader_if_b1", "A partnership trading investments for its owners (nonpassive trading activity)",
    "A partnership that trades investments for its owners is outside this tool.", C_TRADER)
ref("t6_if_asked", "Material participation by test 6 (personal service activity)",
    "Material participation by the personal service test is outside this tool.", C_MP6)
ref("t4_if_gp", "Material participation by test 4 (significant participation activities)",
    "Material participation by the significant participation test is outside this tool.", C_MP4)
ref("t7_if_gp", "Material participation by test 7 (facts and circumstances)",
    "Material participation by the facts and circumstances test is outside this tool.", C_MP7)
ref("basis_short_if_loss", "Partnership losses above basis (basis limitation)",
    "Losses from a partnership above your basis in it are outside this tool.", C_BASIS)
ref("not_at_risk_if_loss", "Form 6198 (at-risk limitations)",
    "A partnership loss with an amount not at risk is outside this tool.", C_ATRISK)
ref("se_loss_not_material", "Schedule K-1 box 14, code A loss without material participation",
    "A self-employment loss from a partnership business you did not materially participate in is outside this tool.", C_B14A)
ref("former_passive", "Form 8582, former passive activity (held-back loss from a business you now materially participate in)",
    "A held-back loss from a business you now materially participate in is outside this tool.", C_FORMER)
ref("prior_not_active_if", "Form 8582, Part IV (prior-year loss from a year without active participation)",
    "A held-back rental loss from a year without active participation is outside this tool.", C_PRIOR_ACTIVE)
line("screened", "(gate)", "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)", "Bool",
     {"op": "copy", "from": "k1p.yes"}, C_LINE28, refuses=REF)

AMB = {'p5_income': 'k1p_activity_per_box', 'basis_short_if_loss': 'k1p_basis_by_filer', 'sche_row': 'k1p_portfolio_no_sche', 'box9c_if_any': 'k1p_box9c_business', 'prior_any_if_activity': 'k1p_prior_with_activity', 'material': 'k1p_material_tests'}
for l in L:
    a = AMB.get(l['id'][4:])
    if a:
        l['ambiguity'] = 'amb.2025.' + a

form = {"form": {
    "id": "k1p", "kind": "form",
    "title": "Schedule K-1 (Form 1065) — one partner's share from one partnership",
    "tax_year": 2025,
    "note": ("One entry per Schedule K-1 (Form 1065) a person received. Boxes 1 to 3 are each one activity; box 1 is "
             "passive unless the partner materially participated (tests 1, 2, 3 or 5), boxes 2 and 3 are passive, and box 2 "
             "goes in Part IV of Form 8582 when a general partner actively participated and owned a tenth. The Form 8582 "
             "columns (a) to (c) and (e) of each activity, the Schedule E line 28 columns (h), (i) and (k), and the portfolio, "
             "self-employment, withholding and section 199A amounts are figured here and totalled on the person. Refused: "
             "publicly traded partnerships, boxes 4b, 7, 10 to 13 (other than 13 AE), 14 B and C, 15 (other than O), 16, 17, "
             "20 (codes other than A, B, N, Z, AG), 21, 22 and 23, foreign partnerships, a sale of the interest, property "
             "distributions and distributions above basis, trading partnerships, material participation by tests 4, 6 or 7, "
             "losses above basis or not at risk, and the held-back losses Form 8582 does not take here."),
    "lines": L,
    "collection": {"parent": "person", "cite": C_LINE28},
}}
out = f"{WT}/forms/2025/k1p.yaml"
with open(out, "w") as f:
    yaml.safe_dump(form, f, sort_keys=False, allow_unicode=True, width=120)
print("wrote", out, len(L), "lines")
