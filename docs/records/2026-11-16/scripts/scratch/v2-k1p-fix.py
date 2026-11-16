"""Lane v2-k1p: fixture cases for BUG-0837, 0841, 0843, appended to the b/ copy of fixtures/2025/k1p.json.
Refusal cites are read from the b/ k1p.yaml so the expected text is the encoded text."""
import json
import yaml

B = "/tmp/nightplan/scratch/v2-k1p/b/"
SNAP = {"i1065sk1": "659063e0aaa36e445cc58409c164c3376054eeb05f9184ef142392942bf2cfbb",
        "i1040se": "ad71de356a6250383ab08097582e982c3c3964792be2d4f5e4bd851816867975"}
form = yaml.safe_load(open(B + "forms/2025/k1p.yaml"))["form"]
screened = next(l for l in form["lines"] if l["id"] == "k1p.screened")
REF = {r["when"]: r for r in screened["refuses"]}
P = "person[taxpayer].k1p[%s]."


def refusal(entry, when):
    r = REF[when]
    return {"kind": "refusal", "gate": (P % entry) + when.split(".", 1)[1], "form": r["form"], "remedy": r["remedy"],
            "cite": {"doc": r["cite"]["doc"], "locator": r["cite"]["locator"], "revision": "2025",
                     "snapshot": SNAP[r["cite"]["doc"]], "tax_year": 2025}}


def case(cid, note, entry, inputs, expect):
    return {"id": cid, "covers": ["k1p"], "evidence": "synthetic regression (not class B)",
            "evidence_note": "Lane v2-k1p, predicted by hand from the source before recording: " + note,
            "inputs": {"$k1p@person[taxpayer]": [entry], **{(P % entry) + k: v for k, v in inputs.items()}},
            "expect": expect}


def money(c):
    return {"kind": "money", "cents": c}


def boolean(v):
    return {"kind": "bool", "value": v}


cases = []
# BUG-0837
cases.append(case("x2k1p.retired_test5",
    "A limited partner who did no work in the business in 2025 (retired), box 1 $40,000, materially participated in 5 of "
    "the 10 years 2015 to 2024. Test 5 needs no work in 2025 and a limited partner may use it (i1065sk1 p. 9, Limited "
    "partners, item 1, 5 or 6): material participation, column (k) $40,000, column (h) zero. Boxes 2 and 3 are blank, so "
    "neither the real estate professional nor the personal-use question is asked.",
    "fund", {"has_b1": True, "box1": 4000000, "work": False, "five_of_ten": True},
    {P % "fund" + "ask_five": boolean(True), P % "fund" + "five_of_ten_if_asked": boolean(True),
     P % "fund" + "material": boolean(True), P % "fund" + "col_k": money(4000000), P % "fund" + "col_h": money(0),
     P % "fund" + "re_pro_if_b2": boolean(False), P % "fund" + "dwelling_if_rent": boolean(False)}))
cases.append(case("x2k1p.retired_gp_no_test4_test7",
    "A general partner who did no work in the business in 2025, box 1 $40,000, not test 5 or 6. Tests 4 and 7 need more "
    "than 100 hours of work in 2025 (i1065sk1 p. 9), so they are not asked; box 1 is passive, column (h) $40,000.",
    "llc", {"general": True, "has_b1": True, "box1": 4000000, "work": False, "five_of_ten": False, "t6": False},
    {P % "llc" + "ask_other": boolean(True), P % "llc" + "ask_other_gp": boolean(False),
     P % "llc" + "t4_if_gp": boolean(False), P % "llc" + "t7_if_gp": boolean(False),
     P % "llc" + "material": boolean(False), P % "llc" + "col_h": money(4000000), P % "llc" + "col_k": money(0)}))
cases.append(case("x2k1p.retired_test6_refuses",
    "A partner who did no work in 2025, box 1 $40,000, not test 5, but a personal service business in which they "
    "materially participated in 3 earlier years (test 6, i1065sk1 p. 9): refused, as test 6 is.",
    "fund", {"has_b1": True, "box1": 4000000, "work": False, "five_of_ten": False, "t6": True},
    {"person[taxpayer].k1p_total_passive_income": refusal("fund", "k1p.t6_if_asked")}))
# BUG-0841
for inp, why in [("upe", "expenses of the partnership the partner paid under the partnership agreement (i1040se p. 10)"),
                 ("interest_buy", "interest on money borrowed to buy into the partnership (i1040se p. 9)"),
                 ("basis_carry", "a loss carried from an earlier year by the basis limitation (i1065sk1 p. 13)"),
                 ("risk_carry", "a loss carried from an earlier year by the at-risk limitation (i1065sk1 p. 13)"),
                 ("fuel_2024", "a 2024 fuel tax credit from the partnership, taken into 2025 income (i1040se p. 9)")]:
    cases.append(case("x2k1p.refuse_" + inp, "box 1 $1,000 and " + why + ": refused at k1p.screened.",
                      "fund", {"has_b1": True, "box1": 100000, inp: True},
                      {"person[taxpayer].k1p_total_passive_income": refusal("fund", "k1p." + inp)}))
# BUG-0843
cases.append(case("x2k1p.refuse_re_pro",
    "A limited partner, box 2 loss $5,000, no rental of their own (scope.rental No), a real estate professional: box 2 "
    "may be nonpassive (i1065sk1 p. 14, Box 2), refused as on Schedule E Part I.",
    "fund", {"has_b2": True, "box2": -500000, "re_pro": True},
    {"person[taxpayer].k1p_total_p5_loss": refusal("fund", "k1p.re_pro_if_b2")}))
cases.append({**case("x2k1p.re_pro_asked_on_sche",
    "A limited partner, box 2 loss $5,000, who also listed a rental of their own (scope.rental Yes): the real estate "
    "professional question is asked once, on Schedule E Part I (sche.re_pro, whose Yes refuses the return), so the K-1 "
    "does not ask it; the box 2 loss is passive in Part V, $5,000 (as x2k1p.fk3_limited_rental_loss).",
    "fund", {"has_b2": True, "box2": -500000},
    {P % "fund" + "re_pro_if_b2": boolean(False), P % "fund" + "p5_loss": money(500000)})})
cases[-1]["inputs"]["scope.rental"] = True
cases.append(case("x2k1p.refuse_dwelling_box3",
    "Box 3 income $3,000 from renting a home that a partner used personally for more than the greater of 14 days or 10% "
    "of the fair-rental days: nonpassive (i1065sk1 p. 11, item 2), refused.",
    "fund", {"has_b3": True, "box3": 300000, "dwelling": True},
    {"person[taxpayer].k1p_total_passive_income": refusal("fund", "k1p.dwelling_if_rent")}))

p = B + "fixtures/2025/k1p.json"
d = json.load(open(p))
d["cases"].extend(cases)
open(p, "w").write(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
print(len(cases), "cases added")
