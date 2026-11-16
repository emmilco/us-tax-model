"""Place k1p's refusal gates in tools/coverage/tree.json (topic 'k1_partnership'); idempotent."""
import sys, json
WT = sys.argv[1]; P = f"{WT}/tools/coverage/tree.json"
d = json.load(open(P))
Q = {
 "k1p.ptp": "Is the Schedule K-1 from a publicly traded partnership (item D checked)?",
 "k1p.r_b4b": "Does a partnership K-1 show guaranteed payments for capital (box 4b)?",
 "k1p.r_b7": "Does a partnership K-1 show royalties (box 7)?",
 "k1p.r_b10": "Does a partnership K-1 show a net section 1231 gain or loss (box 10)?",
 "k1p.r_b11": "Does a partnership K-1 show other income or loss (box 11)?",
 "k1p.r_b12": "Does a partnership K-1 show a section 179 deduction (box 12)?",
 "k1p.r_b13": "Does a partnership K-1 show other deductions with a code other than AE (box 13)?",
 "k1p.r_b14bc": "Does a partnership K-1 show box 14 code B or C (farm or nonfarm optional methods)?",
 "k1p.r_b15": "Does a partnership K-1 show credits other than backup withholding (box 15)?",
 "k1p.r_b16": "Is a Schedule K-3 attached to a partnership K-1 (box 16)?",
 "k1p.r_b17": "Does a partnership K-1 show alternative minimum tax items (box 17)?",
 "k1p.r_b20": "Does a partnership K-1 show box 20 codes other than A, B, N, Z or AG?",
 "k1p.r_b21": "Does a partnership K-1 show foreign taxes (box 21)?",
 "k1p.r_b2223": "Does a partnership K-1 report more than one activity (box 22 or 23)?",
 "k1p.r_foreign": "Is the partnership a foreign partnership?",
 "k1p.r_disposed": "Did you sell or give up any of your share of a partnership in 2025?",
 "k1p.b19_other_if_any": "Did a partnership distribute property other than money to you (box 19, other codes)?",
 "k1p.dist_over_if_any": "Did you take money out of a partnership above your basis in it?",
 "k1p.z_other_if_z": "Does a partnership's section 199A statement show section 199A dividends or cooperative items?",
 "k1p.trader_if_b1": "Is the partnership's business trading investments for its owners?",
 "k1p.t6_if_asked": "Did you materially participate in a partnership business only by the personal service test?",
 "k1p.t4_if_gp": "Did you materially participate in a partnership business only by the significant participation test?",
 "k1p.t7_if_gp": "Did you materially participate in a partnership business only by the facts and circumstances test?",
 "k1p.basis_short_if_loss": "Were your losses from a partnership more than your basis in it?",
 "k1p.not_at_risk_if_loss": "Is any of your investment in a partnership with a loss not at risk?",
 "k1p.se_loss_not_material": "Does a partnership K-1 show a self-employment loss from a business you did not materially participate in?",
 "k1p.former_passive": "Do you have a held-back loss from a partnership business you now materially participate in?",
 "k1p.prior_not_active_if": "Did a held-back partnership rental loss arise in a year without active participation?",
}
text = open(P).read()
lines = [l for l in text.split("\n") if '"gate": "k1p.' not in l]
text = "\n".join(lines)
topic = '  "k1_partnership": {"title": "Partnership Schedules K-1"}'
if topic not in text:
    a = '  "ptc": {"title": "Premium tax credit"}\n },'
    assert a in text
    text = text.replace(a, '  "ptc": {"title": "Premium tax credit"},\n' + topic + '\n },')
new = ",\n".join("  " + json.dumps({"gate": g, "topic": "k1_partnership", "kind": "situation", "question": q}, ensure_ascii=False) for g, q in Q.items())
end = "\n ]\n}\n"
assert text.endswith(end)
text = text[:-len(end)] + ",\n" + new + end
open(P, "w").write(text); json.loads(text)
print(len(Q), "placed")
