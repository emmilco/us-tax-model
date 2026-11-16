"""Insert the person-level sums over k1p into forms/2025/person.yaml (idempotent)."""
import sys, yaml

WT = sys.argv[1]
P = f"{WT}/forms/2025/person.yaml"
BEGIN, END = "  # --- k1p sums (lane x2-k1p) ---\n", "  # --- end k1p sums ---\n"
CITE = {"doc": "i1065sk1", "locator": 'p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E"'}
DISPLAY = "The partnership K-1 total that Schedule E Part II, Form 8582 and the Form 1040 lines read for this person."
WHERE = {"op": "test", "eq": ["k1p.screened", {"const": True}]}

SUMS = [  # person suffix, k1p field, type, label
    ("passive_income", "col_h", "NonNegDollars", "Schedule E line 28 column (h), all partnership K-1s"),
    ("nonpassive_income", "col_k", "NonNegDollars", "Schedule E line 28 column (k), all partnership K-1s"),
    ("nonpassive_loss", "col_i", "NonNegDollars", "Schedule E line 28 column (i), all partnership K-1s (as a positive amount)"),
    ("nonpassive", "nonpassive_net", "Dollars", "Nonpassive income less nonpassive loss, all partnership K-1s"),
    ("p4_income", "p4_income", "NonNegDollars", "Form 8582 Part IV column (a), partnership K-1s"),
    ("p4_loss", "p4_loss", "NonNegDollars", "Form 8582 Part IV column (b), partnership K-1s"),
    ("p4_prior", "p4_prior", "NonNegDollars", "Form 8582 Part IV column (c), partnership K-1s"),
    ("p5_income", "p5_income", "NonNegDollars", "Form 8582 Part V column (a), partnership K-1s"),
    ("p5_loss", "p5_loss", "NonNegDollars", "Form 8582 Part V column (b), partnership K-1s"),
    ("p5_prior", "p5_prior", "NonNegDollars", "Form 8582 Part V column (c), partnership K-1s"),
    ("p6_loss", "p6_loss", "NonNegDollars", "Form 8582 Part VI column (a), partnership K-1s"),
    ("prior", "prior_total", "NonNegDollars", "Prior years unallowed losses, partnership K-1s"),
    ("interest", "box5_if_any", "NonNegDollars", "Interest income (K-1 box 5), all partnership K-1s"),
    ("ord_div", "box6a_if_any", "NonNegDollars", "Ordinary dividends (K-1 box 6a), all partnership K-1s"),
    ("qual_div", "box6b_if_any", "NonNegDollars", "Qualified dividends (K-1 box 6b), all partnership K-1s"),
    ("st_gain", "box8_if_any", "Dollars", "Net short-term capital gain or loss (K-1 box 8), all partnership K-1s"),
    ("lt_gain", "box9a_if_any", "Dollars", "Net long-term capital gain or loss (K-1 box 9a), all partnership K-1s"),
    ("collectibles", "box9b_if_any", "NonNegDollars", "Collectibles (28%) gain (K-1 box 9b), all partnership K-1s"),
    ("unrecap_1250", "box9c_if_any", "NonNegDollars", "Unrecaptured section 1250 gain (K-1 box 9c), all partnership K-1s"),
    ("se_earnings", "box14a_if_any", "Dollars", "Net earnings from self-employment (K-1 box 14, code A), all partnership K-1s"),
    ("se_pos", "se_pos", "NonNegDollars", "Positive net earnings from self-employment (K-1 box 14, code A), all partnership K-1s"),
    ("backup_wh", "box15o_if_any", "NonNegDollars", "Backup withholding (K-1 box 15, code O), all partnership K-1s"),
    ("taxexempt_int", "box18a_if_any", "NonNegDollars", "Tax-exempt interest (K-1 box 18, code A), all partnership K-1s"),
    ("qbi_stmt", "box20z_if_any", "Dollars", "QBI or loss from the section 199A statements (K-1 box 20, code Z), all partnership K-1s"),
]
COUNTS = [  # person suffix, Bool where-line (or None), label
    ("count", None, "Number of partnership K-1s"),
    ("count_sche", "sche_row", "Number of partnership K-1s with a row on Schedule E line 28"),
    ("count_passive_loss", "passive_loss", "Number of partnership K-1s with a passive net loss or held-back loss"),
    ("count_inv", "has_b20ab", "Number of partnership K-1s with box 20, code A or B"),
    ("count_general", "general", "Number of partnership K-1s held as a general partner"),
]
lines = []
for suf, field, typ, label in SUMS:
    lines.append({"id": f"person.k1p_total_{suf}", "printed": "(helper)", "type": typ, "label": label,
                  "expr": {"op": "sum_over", "collection": "k1p", "field": f"k1p.{field}", "where": WHERE},
                  "cite": CITE, "display": DISPLAY})
for suf, where, label in COUNTS:
    w = WHERE if where is None else {"op": "test", "all": [WHERE, {"op": "test", "eq": [f"k1p.{where}", {"const": True}]}]}
    lines.append({"id": f"person.k1p_{suf}", "printed": "(helper)", "type": "Count", "label": label,
                  "expr": {"op": "sum_over", "collection": "k1p", "field": "k1p.one", "where": w}, "cite": CITE,
                  "display": DISPLAY})
block = yaml.safe_dump(lines, sort_keys=False, allow_unicode=True, width=116)
block = "".join("    " + l if l.strip() else l for l in block.splitlines(True))
text = open(P).read()
if BEGIN in text:
    a = text.index(BEGIN); b = text.index(END) + len(END)
    text = text[:a] + text[b:]
anchor = "  # --- end Stage 21 ---\n  collection:\n"
assert anchor in text
text = text.replace(anchor, "  # --- end Stage 21 ---\n" + BEGIN + block + END + "  collection:\n")
open(P, "w").write(text)
print("person: inserted", len(lines), "lines")
