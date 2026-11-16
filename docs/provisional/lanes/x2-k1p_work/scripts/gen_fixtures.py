"""Write fixtures/2025/k1p.json: hand-predicted cases for lane x2-k1p (values predicted from the source before running)."""
import sys, json

WT = sys.argv[1]
E = "synthetic regression (not class B)"
P = "person[taxpayer]"


def k(key, field):
    return f"{P}.k1p[{key}].{field}"


def money(c):
    return {"kind": "money", "cents": c}


def boolean(v):
    return {"kind": "bool", "value": v}


cases = []


def case(id, note, key, inputs, expect):
    inp = {f"$k1p@{P}": [key]}
    for f, v in inputs.items():
        inp[k(key, f) if not f.startswith(("person", "$", "f1040", "s1", "sc")) else f] = v
    exp = {}
    for f, v in expect.items():
        name = f if f.startswith("person.") is False and "." in f and not f.startswith("k1p") else f
        if f.startswith("person."):
            name = f"{P}." + f[len("person."):]
        else:
            name = k(key, f)
        exp[name] = v
    cases.append({"id": "x2k1p." + id, "covers": ["k1p"], "evidence": E,
                  "evidence_note": "Lane x2-k1p, predicted by hand from i1065sk1 and i8582 before recording: " + note,
                  "inputs": inp, "expect": exp})


case("fk2_general_material", "FK2. A general partner, box 1 $50,000, worked more than 500 hours (test 1, i1065sk1 p. 9), box 14 code A $50,000, "
     "box 20 code Z QBI $50,000. Box 1 is nonpassive income: column (k) $50,000 (p. 14 item 1); columns (h) and (i) zero; Form 8582 Part V "
     "columns zero; self-employment earnings $50,000 and QBI $50,000 totalled on the person; one Schedule E row.", "llc",
     {"general": True, "has_b1": True, "box1": 5000000, "work": True, "hours500": True, "has_b14a": True, "box14a": 5000000,
      "has_b20z": True, "box20z": 5000000},
     {"material": boolean(True), "col_k": money(5000000), "col_h": money(0), "col_i": money(0), "p5_income": money(0),
      "person.k1p_total_se_earnings": money(5000000), "person.k1p_total_se_pos": money(5000000),
      "person.k1p_total_qbi_stmt": money(5000000), "person.k1p_total_nonpassive": money(5000000),
      "person.k1p_count_sche": {"kind": "count", "value": 1}})
case("fk3_limited_rental_loss", "FK3. A limited partner, box 2 loss $12,000. Box 2 is passive and a limited partner cannot actively "
     "participate (p. 11), so Part V: column (b) $12,000, overall loss (e) $12,000, Part IV zero; column (h) zero.", "fund",
     {"has_b2": True, "box2": -1200000},
     {"active": boolean(False), "p5_loss": money(1200000), "p4_loss": money(0), "b2_overall_loss": money(1200000),
      "p6_loss": money(0), "col_h": money(0), "passive_loss": boolean(True),
      "person.k1p_total_p5_loss": money(1200000), "person.k1p_count_passive_loss": {"kind": "count", "value": 1}})
case("fk3b_general_active", "FK3b. As FK3 but a general partner who helped make management decisions and owned a tenth all year: "
     "Part IV (i8582 p. 10): column (b) $12,000, Part VI column (a) $12,000, Part V zero.", "fund",
     {"general": True, "has_b2": True, "box2": -1200000, "decisions": True, "tenth": True},
     {"active": boolean(True), "p4_loss": money(1200000), "p6_loss": money(1200000), "p5_loss": money(0),
      "person.k1p_total_p4_loss": money(1200000), "person.k1p_total_p6_loss": money(1200000)})
case("fk3c_general_under_tenth", "As FK3b but the partner owned less than a tenth at some time (p. 11, less than 10% by value): no active "
     "participation, Part V column (b) $12,000.", "fund",
     {"general": True, "has_b2": True, "box2": -1200000, "decisions": True, "tenth": False},
     {"active": boolean(False), "p4_loss": money(0), "p5_loss": money(1200000)})
case("fk3d_rental_income_active", "A general partner with box 2 income $4,000, active, owned a tenth: Part IV column (a) $4,000 and "
     "Schedule E column (h) $4,000.", "fund",
     {"general": True, "has_b2": True, "box2": 400000, "decisions": True, "tenth": True},
     {"p4_income": money(400000), "p5_income": money(0), "col_h": money(400000), "b2_overall_loss": money(0),
      "passive_loss": boolean(False), "person.k1p_total_p4_income": money(400000)})
case("fk7_portfolio_only", "FK7. A limited partner with box 5 $300, 6a $1,000, 6b $800, 9a $2,500 and box 20 codes A and B: portfolio "
     "only (p. 15), no Schedule E row.", "fund",
     {"has_b5": True, "box5": 30000, "has_b6a": True, "box6a": 100000, "box6b": 80000, "has_b9a": True, "box9a": 250000,
      "has_b20ab": True},
     {"sche_row": boolean(False), "person.k1p_total_interest": money(30000), "person.k1p_total_ord_div": money(100000),
      "person.k1p_total_qual_div": money(80000), "person.k1p_total_lt_gain": money(250000),
      "person.k1p_count_sche": {"kind": "count", "value": 0}, "person.k1p_count_inv": {"kind": "count", "value": 1}})
case("gains_withholding", "Box 8 loss $700, 9a $5,000 with 9b $1,000 and 9c $2,000, 15 O $240, 18 A $150: the totals carry each box "
     "(pp. 15, 16, 23, 25); the box 8 loss asks basis and at-risk (answered No).", "fund",
     {"has_b8": True, "box8": -70000, "has_b9a": True, "box9a": 500000, "has_b9bc": True, "box9b": 100000, "box9c": 200000,
      "has_b15o": True, "box15o": 24000, "has_b18a": True, "box18a": 15000},
     {"any_loss": boolean(True), "person.k1p_total_st_gain": money(-70000), "person.k1p_total_lt_gain": money(500000),
      "person.k1p_total_collectibles": money(100000), "person.k1p_total_unrecap_1250": money(200000),
      "person.k1p_total_backup_wh": money(24000), "person.k1p_total_taxexempt_int": money(15000)})
case("fk11_limited_box1_income", "FK11. A limited partner, box 1 $30,000, did not work in the business: passive income, column (h) "
     "$30,000 and Part V column (a) $30,000; column (k) zero.", "fund",
     {"has_b1": True, "box1": 3000000, "has_b20z": True, "box20z": 3000000},
     {"material": boolean(False), "col_h": money(3000000), "p5_income": money(3000000), "col_k": money(0),
      "nonpassive_net": money(0), "person.k1p_total_passive_income": money(3000000)})
case("loss_material_with_gp", "A general partner, box 1 loss $10,000, worked 300 hours and no one worked more (test 3, p. 9), "
     "box 4a $20,000: column (i) $10,000, column (k) $20,000, nonpassive net $10,000; basis and at-risk asked (No).", "llc",
     {"general": True, "has_b1": True, "box1": -1000000, "has_b4a": True, "box4a": 2000000, "work": True, "hours500": False,
      "most_hours": True},
     {"material": boolean(True), "col_i": money(1000000), "col_k": money(2000000), "nonpassive_net": money(1000000),
      "p5_loss": money(0), "passive_loss": boolean(False), "person.k1p_total_nonpassive_loss": money(1000000)})
case("test2_nearly_all", "A general partner, box 1 $20,000, worked under 500 hours, less than someone else's hours but nearly all of "
     "the work (test 2): nonpassive, column (k) $20,000.", "llc",
     {"general": True, "has_b1": True, "box1": 2000000, "work": True, "hours500": False, "most_hours": False, "nearly_all": True},
     {"material": boolean(True), "col_k": money(2000000), "col_h": money(0)})
case("test5_five_of_ten", "A general partner, box 1 $40,000, worked under 500 hours, tests 2 and 3 not met, materially participated "
     "in 5 of the 10 earlier years (test 5): column (k) $40,000.", "llc",
     {"general": True, "has_b1": True, "box1": 4000000, "work": True, "hours500": False, "most_hours": False,
      "nearly_all": False, "five_of_ten": True},
     {"material": boolean(True), "col_k": money(4000000)})
case("limited_worked_passive", "A limited partner, box 1 $8,000, worked 200 hours (tests 2 and 3 do not apply to a limited partner, "
     "p. 9 Limited partners), not test 5 or 6: passive, column (h) $8,000.", "fund",
     {"has_b1": True, "box1": 800000, "work": True, "hours500": False, "five_of_ten": False},
     {"material": boolean(False), "col_h": money(800000), "col_k": money(0)})
case("prior_box1_partly_used", "A limited partner, box 1 $5,000 not materially participated, held-back loss from the business $8,000 "
     "(2024 Form 8582 Part VII column (c)): column (a) $5,000, (c) $8,000, overall loss (e) = 8,000 - 5,000 = $3,000; Part V "
     "column (c) $8,000.", "fund",
     {"has_b1": True, "box1": 500000, "prior_any": True, "prior_b1_any": True, "prior_b1": 800000},
     {"b1_net_income": money(500000), "b1_loss_sum": money(800000), "b1_overall_loss": money(300000),
      "p5_prior": money(800000), "passive_loss": boolean(True), "sche_row": boolean(True),
      "person.k1p_total_prior": money(800000), "person.k1p_total_p5_prior": money(800000)})
case("prior_box2_active", "A general partner with box 2 income $3,000, active, a tenth, held-back rental loss $5,000 from years of "
     "active participation: Part IV columns (a) $3,000, (c) $5,000; overall loss $2,000; Part VI column (a) $2,000.", "fund",
     {"general": True, "has_b2": True, "box2": 300000, "decisions": True, "tenth": True, "prior_any": True,
      "prior_b2_any": True, "prior_b2": 500000, "prior_not_active": False},
     {"p4_income": money(300000), "p4_prior": money(500000), "b2_overall_loss": money(200000), "p6_loss": money(200000),
      "p5_prior": money(0)})


def refusal(id, note, key, inputs, line, gate_field):
    cases.append({"id": "x2k1p.refuse_" + id, "covers": ["k1p"], "evidence": E,
                  "evidence_note": "Lane x2-k1p, refusal predicted from the source: " + note,
                  "inputs": dict({f"$k1p@{P}": [key]}, **{k(key, f): v for f, v in inputs.items()}),
                  "expect": {f"{P}.{line}": {"kind": "refusal", "gate": k(key, gate_field), "PENDING": True}}})


refusal("ptp", "item D checked (i1065sk1 p. 11).", "mlp", {"ptp": True}, "k1p_total_interest", "ptp")
refusal("box10", "box 10 section 1231 gain (Form 4797 not encoded).", "fund", {"r_b10": True}, "k1p_total_interest", "r_b10")
refusal("multi", "box 23 checked (more than one activity).", "fund", {"r_b2223": True}, "k1p_count_sche", "r_b2223")
refusal("disposed", "sale of the interest.", "fund", {"r_disposed": True}, "k1p_total_lt_gain", "r_disposed")
refusal("dist_over", "money taken out above basis (box 19, p. 25).", "fund",
        {"has_b19": True, "b19_other": False, "dist_over": True}, "k1p_total_interest", "dist_over_if_any")
refusal("trader", "a trading partnership (p. 11).", "fund", {"has_b1": True, "box1": 100000, "trader": True},
        "k1p_total_passive_income", "trader_if_b1")
refusal("basis", "box 1 loss above basis (p. 3).", "fund", {"has_b1": True, "box1": -500000, "basis_short": True},
        "k1p_total_p5_loss", "basis_short_if_loss")
refusal("at_risk", "box 2 loss with an amount not at risk (p. 8).", "fund", {"has_b2": True, "box2": -500000, "not_at_risk": True},
        "k1p_total_p5_loss", "not_at_risk_if_loss")
refusal("test4", "a general partner under 500 hours meeting only test 4.", "llc",
        {"general": True, "has_b1": True, "box1": 100000, "work": True, "hours500": False, "t4": True},
        "k1p_total_nonpassive_income", "t4_if_gp")
refusal("former_passive", "a held-back box 1 loss on a business now materially participated in (i8582 p. 4).", "llc",
        {"general": True, "has_b1": True, "box1": 900000, "work": True, "hours500": True, "prior_any": True,
         "prior_b1_any": True, "prior_b1": 100000}, "k1p_total_nonpassive_income", "former_passive")
refusal("prior_not_active", "a held-back rental loss from a year without active participation (i8582 p. 10).", "fund",
        {"general": True, "has_b2": True, "box2": 100000, "decisions": True, "tenth": True, "prior_any": True,
         "prior_b2_any": True, "prior_b2": 100000, "prior_not_active": True}, "k1p_total_p4_prior", "prior_not_active_if")
refusal("se_loss_passive", "a box 14 code A loss on a business not materially participated in.", "fund",
        {"has_b1": True, "box1": -100000, "has_b14a": True, "box14a": -100000}, "k1p_total_se_earnings", "se_loss_not_material")

json.dump({"tax_year": 2025, "cases": cases}, open(f"{WT}/fixtures/2025/k1p.json", "w"), indent=1, ensure_ascii=False)
print(len(cases), "cases")
