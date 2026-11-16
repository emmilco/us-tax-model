"""Lane v2-k1s: fixture cases for BUG-0882 and the k1s siblings, appended to the b/ copy of fixtures/2025/k1s.json."""
import json
import yaml

B = "/tmp/nightplan/scratch/v2-k1s/b/"
SNAP = {"i1120ssk": "fb6194da1d1f9e898385f4a5b3df1355f04c478f9422d969b182d4dc04f2a355",
        "i1040se": "ad71de356a6250383ab08097582e982c3c3964792be2d4f5e4bd851816867975",
        "i8995": "875843baead68f6fa9aa7c3f6f27d6c1f37cb971ac334bcf414acdb4c1487684"}
lines = {l["id"]: l for l in yaml.safe_load(open(B + "forms/2025/k1s.yaml"))["form"]["lines"]}
REF = {r["when"]: r for lid in ("k1s.ok", "k1s.qbi") for r in lines[lid]["refuses"]}
P = "person[taxpayer].k1s[acme]."


def refusal(when):
    r = REF[when]
    return {"kind": "refusal", "gate": P + when.split(".", 1)[1], "form": r["form"], "remedy": r["remedy"],
            "cite": {"doc": r["cite"]["doc"], "locator": r["cite"]["locator"], "revision": "2025",
                     "snapshot": SNAP[r["cite"]["doc"]], "tax_year": 2025}}


def case(cid, note, inputs, expect, f7203=None, extra=None):
    ins = {"$k1s@person[taxpayer]": ["acme"]}
    if f7203 is not None:
        ins["$f7203@person[taxpayer].k1s[acme]"] = ["form"]
    ins.update({P + k: v for k, v in inputs.items()})
    if f7203 is not None:
        ins.update({P + "f7203[form]." + k: v for k, v in f7203.items()})
    ins.update(extra or {})
    return {"id": cid, "covers": ["k1s", "f7203"], "evidence": "synthetic refusal regression" if any(
        e.get("kind") == "refusal" for e in expect.values()) else "synthetic regression (not class B)",
            "evidence_note": "Lane v2-k1s, predicted by hand from the source before recording: " + note,
            "inputs": ins, "expect": expect}


money = lambda c: {"kind": "money", "cents": c}
boolean = lambda v: {"kind": "bool", "value": v}

cases = [
    case("k1s.refuse_trader",
         "Box 1 income $5,000 from a corporation whose business is trading investments for its owners: nonpassive "
         "(i1120ssk p. 5), refused at k1s.ok, as k1p.trader is.",
         {"box1_any": True, "box1": 500000, "trader": True}, {P + "col_h": refusal("k1s.trader_if_b1")}),
    case("k1s.refuse_re_pro",
         "Box 2 income $3,000, no rental of the filer's own (scope.rental No), a real estate professional: box 2 may be "
         "nonpassive (i1120ssk p. 6, Box 2), refused as on Schedule E Part I.",
         {"box2_any": True, "box2": 300000, "re_pro": True}, {P + "col_h": refusal("k1s.re_pro_if_b2")}),
    case("k1s.re_pro_asked_on_sche",
         "Box 2 income $3,000 and a rental of the filer's own listed (scope.rental Yes): the real estate professional "
         "question is asked once, on Schedule E Part I, so the K-1 does not ask it; box 2 income is passive, column (h) "
         "$3,000.",
         {"box2_any": True, "box2": 300000},
         {P + "re_pro_if_b2": boolean(False), P + "col_h": money(300000)}, extra={"scope.rental": True}),
    case("k1s.refuse_dwelling_box3",
         "Box 3 income $2,000 from renting a home a shareholder used personally for more than the greater of 14 days or "
         "10% of the fair-rental days: nonpassive (i1120ssk p. 5), refused.",
         {"box3_any": True, "box3": 200000, "dwelling": True}, {P + "col_h": refusal("k1s.dwelling_if_rent")}),
    case("k1s.refuse_interest_buy",
         "Box 1 income $5,000 and interest paid on money borrowed to buy the shares (i1040se p. 9, S Corporations, a "
         "separate Schedule E line): refused.",
         {"box1_any": True, "box1": 500000, "interest_buy": True}, {P + "col_h": refusal("k1s.interest_buy")}),
    case("k1s.refuse_qbi_passive_loss",
         "Box 1 loss $10,000, no work in 2025 and no earlier-years test (passive), code V QBI loss $10,000, stock basis "
         "$20,000 so nothing is carried by basis (k1s.qbi_cut false). The passive loss may be partly held back on Form "
         "8582, and only the allowed part is QBI (i8995 p. 3): refused at k1s.qbi_passive.",
         {"box1_any": True, "box1": -1000000, "box17_any": True, "box17v_any": True, "qbi_stmt": -1000000},
         {P + "qbi_cut": boolean(False), P + "qbi": refusal("k1s.qbi_passive")},
         f7203={"line1": 2000000, "line2": 0}),
    case("k1s.qbi_material_loss_kept",
         "As k1s.refuse_qbi_passive_loss but more than 500 hours of work in 2025 (test 1): box 1 is nonpassive, so no "
         "passive limit applies and the QBI loss of $10,000 is used as stated; column (i) $10,000.",
         {"box1_any": True, "box1": -1000000, "work": True, "hours500": True, "box17_any": True, "box17v_any": True,
          "qbi_stmt": -1000000},
         {P + "qbi_passive": boolean(False), P + "qbi": money(-1000000), P + "col_i": money(1000000)},
         f7203={"line1": 2000000, "line2": 0}),
]

p = B + "fixtures/2025/k1s.json"
d = json.load(open(p))
d["cases"].extend(cases)
open(p, "w").write(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
print(len(cases), "cases added")
