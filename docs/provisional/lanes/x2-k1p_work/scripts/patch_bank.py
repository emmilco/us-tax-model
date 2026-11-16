"""Add the k1p frame, groups and bank entries to interview/2025/questions.yaml (idempotent, text-level)."""
import sys, yaml

WT = sys.argv[1]
P = f"{WT}/interview/2025/questions.yaml"
text = open(P).read()
BEGIN, END = "  # --- k1p (lane x2-k1p) ---\n", "  # --- end k1p ---\n"
GB, GE = "  # --- k1p groups (lane x2-k1p) ---\n", "  # --- end k1p groups ---\n"
for b, e in ((BEGIN, END), (GB, GE)):
    if b in text:
        text = text[:text.index(b)] + text[text.index(e) + len(e):]
FRAME = "    k1p: 'On this Schedule K-1 (Form 1065) — '\n"
if FRAME not in text:
    anchor = "    f1095a: 'On this Form 1095-A — '\n"
    assert anchor in text
    text = text.replace(anchor, anchor + FRAME)

GROUPS = [
    ("k1p_income", "Which of boxes 1 to 4 of this Schedule K-1 show an amount?"),
    ("k1p_portfolio", "Which of boxes 5 to 9 show an amount?"),
    ("k1p_boxes_10", "Which of boxes 10 to 13 show an amount?"),
    ("k1p_boxes_14", "Which of boxes 14 to 17 show an amount or a check?"),
    ("k1p_boxes_18", "Which of boxes 18 to 20 show an amount?"),
    ("k1p_facts", "Is any of these true of this Schedule K-1 or your share?"),
    ("k1p_part_other", "Is any of these true of your work in this business?"),
    ("k1p_prior", "Which part of the partnership was that loss held back from?"),
]
REFUSE = "A Yes ends the interview here."
Q = []


def add(inp, seq, help=None, group=None, tick=None, prompt=None):
    e = {"input": inp, "order": 264, "seq": seq}
    if group:
        e["group"] = group
        e["tick"] = tick
    if help:
        e["help"] = help
    if prompt:
        e["prompt"] = prompt
    Q.append(e)


add("$k1p", 1, prompt="For this person (you, or your spouse on a joint return) — Which partnerships or LLCs sent you a Schedule K-1 (Form 1065) for 2025?",
    help="List each Schedule K-1 (Form 1065) once, by the partnership's name in item B. A Schedule K-1 from an S corporation (Form 1120-S) or from an estate or trust (Form 1041) is not listed here.")
add("k1p.ptp", 2, help="Item D is near the top left of the page. Units of a partnership bought on a stock exchange (often called an MLP) are outside what this tool prepares; " + REFUSE)
add("k1p.general", 3, help="Item G is in Part II, on the left. Answer No if the second box, limited partner or other LLC member, is checked.")
add("k1p.has_b1", 10, group="k1p_income", tick="Box 1: ordinary business income (loss)")
add("k1p.has_b2", 11, group="k1p_income", tick="Box 2: net rental real estate income (loss)")
add("k1p.has_b3", 12, group="k1p_income", tick="Box 3: other net rental income (loss)")
add("k1p.has_b4a", 13, group="k1p_income", tick="Box 4a: guaranteed payments for services")
add("k1p.r_b4b", 14, group="k1p_income", tick="Box 4b: guaranteed payments for capital", help=REFUSE)
add("k1p.box1", 15)
add("k1p.box2", 16)
add("k1p.box3", 17)
add("k1p.box4a", 18)
add("k1p.has_b5", 20, group="k1p_portfolio", tick="Box 5: interest income")
add("k1p.has_b6a", 21, group="k1p_portfolio", tick="Box 6a: ordinary dividends")
add("k1p.r_b7", 22, group="k1p_portfolio", tick="Box 7: royalties", help=REFUSE)
add("k1p.has_b8", 23, group="k1p_portfolio", tick="Box 8: net short-term capital gain (loss)")
add("k1p.has_b9a", 24, group="k1p_portfolio", tick="Box 9a: net long-term capital gain (loss)")
add("k1p.box5", 25)
add("k1p.box6a", 26)
add("k1p.box6b", 27, help="Qualified dividends are part of the ordinary dividends in box 6a, never more.")
add("k1p.box8", 28)
add("k1p.box9a", 29)
add("k1p.has_b9bc", 30, help="Both are parts of the gain in box 9a.")
add("k1p.box9b", 31)
add("k1p.box9c", 32, help="If box 9c says STMT, the statement splits it into kinds; that is outside what this tool prepares.")
add("k1p.r_b10", 35, group="k1p_boxes_10", tick="Box 10: net section 1231 gain (loss)", help=REFUSE)
add("k1p.r_b11", 36, group="k1p_boxes_10", tick="Box 11: other income (loss)", help=REFUSE)
add("k1p.r_b12", 37, group="k1p_boxes_10", tick="Box 12: section 179 deduction", help=REFUSE)
add("k1p.r_b13", 38, group="k1p_boxes_10", tick="Box 13: a code other than AE", help="Code AE (deductions, portfolio income) can be left out: it is not deducted on your return. " + REFUSE)
add("k1p.has_b14a", 40, group="k1p_boxes_14", tick="Box 14, code A: net earnings from self-employment")
add("k1p.r_b14bc", 41, group="k1p_boxes_14", tick="Box 14, code B or C", help=REFUSE)
add("k1p.has_b15o", 42, group="k1p_boxes_14", tick="Box 15, code O: backup withholding")
add("k1p.r_b15", 43, group="k1p_boxes_14", tick="Box 15: a code other than O", help=REFUSE)
add("k1p.r_b16", 44, group="k1p_boxes_14", tick="Box 16 checked: Schedule K-3 attached", help=REFUSE)
add("k1p.r_b17", 45, group="k1p_boxes_14", tick="Box 17: alternative minimum tax items", help=REFUSE)
add("k1p.box14a", 46, help="Use the amount shown with code A, before any change; a loss is a negative amount.")
add("k1p.box15o", 47)
add("k1p.has_b18a", 50, group="k1p_boxes_18", tick="Box 18, code A: tax-exempt interest income")
add("k1p.has_b19", 51, group="k1p_boxes_18", tick="Box 19: distributions")
add("k1p.has_b20ab", 52, group="k1p_boxes_18", tick="Box 20, code A or B: investment income or expenses")
add("k1p.has_b20z", 53, group="k1p_boxes_18", tick="Box 20, code Z: section 199A information")
add("k1p.r_b20", 54, group="k1p_boxes_18", tick="Box 20: a code other than A, B, N, Z or AG", help=REFUSE)
add("k1p.box18a", 55)
add("k1p.b19_other", 56, help="Code A is money (cash and some marketable securities). Other codes are property, or pay for services. " + REFUSE)
add("k1p.dist_over", 57, help="Your basis is what you put in, plus your share of its income and debts, less losses and money taken out earlier. The worksheet in the instructions for Schedule K-1 figures it. " + REFUSE)
add("k1p.box20z", 58, help="The statement for code Z gives each business's qualified business income (QBI); enter their total. Enter 0 if it shows none.")
add("k1p.z_other", 59, help=REFUSE)
add("k1p.r_b21", 60, group="k1p_facts", tick="Box 21 shows foreign taxes paid or accrued", help=REFUSE)
add("k1p.r_b2223", 61, group="k1p_facts", tick="Box 22 or box 23 is checked", help=REFUSE)
add("k1p.r_foreign", 62, group="k1p_facts", tick="It is a foreign partnership", help=REFUSE)
add("k1p.r_disposed", 63, group="k1p_facts", tick="You sold or gave up any of your share in 2025", help=REFUSE)
add("k1p.trader", 70, help="A fund that buys and sells stocks for its partners is one; a business that sells goods or services is not. " + REFUSE)
add("k1p.work", 71, help="Count work in running the business. Reading its reports or checking on it as an investor does not count.")
add("k1p.hours500", 72, help="Count your own hours and, on a joint return, your spouse's hours in it together.")
add("k1p.most_hours", 73)
add("k1p.nearly_all", 74)
add("k1p.five_of_ten", 75, help="Your earlier returns show it: the business's income or loss was in column (i) or (k) of Schedule E, not (g) or (h).")
add("k1p.t6", 76, group="k1p_part_other", tick="A service business you took part in for 3 earlier years", help=REFUSE)
add("k1p.t4", 77, group="k1p_part_other", tick="Over 500 hours in all your businesses of over 100 hours", help=REFUSE)
add("k1p.t7", 78, group="k1p_part_other", tick="Regular, continuous and substantial work, over 100 hours", help=REFUSE)
add("k1p.decisions", 80)
add("k1p.tenth", 81, help="The partnership's records or item J show your share. Answer No if it was less than a tenth at any time in 2025.")
add("k1p.prior_any", 85, help="A 2024 Form 8582 (Part VII, column (c)) lists such a loss.")
add("k1p.prior_b1_any", 86, group="k1p_prior", tick="The business (box 1)")
add("k1p.prior_b2_any", 87, group="k1p_prior", tick="Rental real estate (box 2)")
add("k1p.prior_b3_any", 88, group="k1p_prior", tick="Other rentals (box 3)")
add("k1p.prior_b1", 89)
add("k1p.prior_b2", 90)
add("k1p.prior_b3", 91)
add("k1p.prior_not_active", 92, help=REFUSE)
add("k1p.basis_short", 95, help="Most partners with a loss have basis to cover it. The worksheet for a partner's basis in the instructions for Schedule K-1 figures it. " + REFUSE)
add("k1p.not_at_risk", 96, help="A partner who put in cash, or is liable for the partnership's loans, is at risk. " + REFUSE)

gtext = yaml.safe_dump([{"id": g, "heading": h} for g, h in GROUPS], sort_keys=False, allow_unicode=True, width=116)
gtext = "".join("  " + l for l in gtext.splitlines(True))
qtext = yaml.safe_dump(Q, sort_keys=False, allow_unicode=True, width=116)
qtext = "".join("  " + l for l in qtext.splitlines(True))
anchor = "  questions:\n"
assert text.count(anchor) == 1
text = text.replace(anchor, GB + gtext + GE + anchor + BEGIN + qtext + END)
open(P, "w").write(text)
print("bank:", len(Q), "entries,", len(GROUPS), "groups")
