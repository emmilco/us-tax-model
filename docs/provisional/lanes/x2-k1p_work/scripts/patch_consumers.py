"""Rule the k1p consumer pairs (verdict same) in reviews/2025/consumers.json; idempotent."""
import sys, json, re
WT = sys.argv[1]; P = f"{WT}/reviews/2025/consumers.json"
d = json.load(open(P))
pairs = sorted(set(re.findall(r"consumer: (k1p\.[a-z0-9_]+@[a-z0-9]+:p\d+)", open("/tmp/x2-k1p/chk_consumers.log").read())))
import yaml
form = yaml.safe_load(open(f"{WT}/forms/2025/k1p.yaml"))["form"]
src = {l["id"]: l["expr"].get("source", "") for l in form["lines"]}
SRC_PHRASE = {
    ("i1065sk1", "14"): ("The tip of the line 28 instructions, cited by k1p.screened (the line that carries the K-1's refusals): "
                         "\"report items from each partnership's Schedule K-1 on a separate line 28 of Schedule E\""),
    ("i1065sk1", "9"): "Material participation: \"You must determine if you materially participated (a) in each trade or business activity held through the partnership\"; Limited partners: \"you must meet item 1, 5, or 6\"",
    ("i1065sk1", "11"): "Special allowance for a rental real estate activity: \"Limited partners can't actively participate\"; Special rules: \"Trading personal property for the account of owners of interests in the activity\"",
    ("i1065sk1", "16"): "Box 9b. Collectibles (28%) Gain (Loss); Box 9c. Unrecaptured Section 1250 Gain (parts of the box 9a gain)",
    ("i1065sk1", "30"): "Code Z, Section 199A dividends: \"your distributive share of the partnership's net section 199A dividends\"",
    ("i8582", "10"): "Part IV and Part V: prior-year unallowed losses \"in Part VII, column (c), of your 2024 Form 8582\" for each activity",
}
REASON = {
    ("i1065sk1", "14"): "The input is the screen of one K-1 box or fact and the reading line only refuses on it; the page's rule (one row per K-1) puts no other meaning on it.",
    ("i1065sk1", "9"): "The input (a box shows an amount, or the item G box checked) is the K-1 fact the material participation rules are applied to: box 1 is the trade or business activity, item G decides which tests apply.",
    ("i1065sk1", "11"): "Box 2 with an amount and the general partner box are exactly the facts the page conditions active participation and the trading rule on.",
    ("i1065sk1", "16"): "Box 9a with an amount is the gain boxes 9b and 9c are parts of; the reading gate asks them only then.",
    ("i1065sk1", "30"): "Box 20 code Z is the statement the section 199A dividends are reported on.",
    ("i8582", "10"): "A box 1, 2 or 3 amount is an activity of the K-1; the prior-year loss is asked per activity, as the page enters it per activity.",
}
for p in pairs:
    inp, rest = p.split("@"); doc, page = rest.split(":p")
    key = f"consumer:{p}"
    q = src.get(inp, "")
    d["rulings"][key] = {"verdict": "same", "question_phrase": q[:200], "source_phrase": SRC_PHRASE[(doc, page)],
                         "reason": REASON[(doc, page)]}
json.dump(d, open(P, "w"), indent=2, ensure_ascii=False); open(P, "a").write("\n")
print(len(pairs), "ruled")
