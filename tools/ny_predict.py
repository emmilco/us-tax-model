#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Predict Form IT-201 (2025) values for a full-year New York City resident from the archived instructions,
independently of the encoding (forms/ny/2025/), for the New York fixtures (Phase 3 step 5, decision C6).

It reads no New York YAML, parameter or canonical file: every rule and amount below is transcribed here from
the archived IT-201-I (sources/ny/2025/ny_it201i.pdf and its web edition) and the archived tax-tables page, with
the quote beside it. The only inputs are federal amounts (from the federal return, which the New York return copies)
and the answers to the New York questions. Amounts are whole dollars as Fractions; money is returned in cents.

Used by tools/ny_fixtures.py; `--self-test` checks the predictor against the two official tax-table examples.
"""
import html.parser
import json
import re
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NYDIR = ROOT / "sources" / "ny" / "2025"


def r_dollar(x):
    """IT-201-I p. 2, Entering whole dollar amounts: "Drop amounts that are less than 50 cents ... Increase amounts
    that are 50 cents or more to the next dollar." (half-up; for negatives, by magnitude would differ only at .50,
    which whole-dollar federal inputs never produce)."""
    x = F(x)
    return int((x + F(1, 2)) // 1) if x >= 0 else -int((-x + F(1, 2)) // 1)


# --- New York State tax rate schedule (IT-201-I p. 33; web edition "New York State tax rate schedule") ---
RATES = [F(4, 100), F(45, 1000), F(525, 10000), F(55, 1000), F(6, 100), F(685, 10000), F(965, 10000), F(103, 1000), F(109, 1000)]
RS = {  # (over, base) per band; "but not over" is the next band's over
    "mfj": [(0, 0), (17150, 686), (23600, 976), (27900, 1202), (161550, 8553), (323200, 18252), (2155350, 143754), (5000000, 418263), (25000000, 2478263)],
    "single": [(0, 0), (8500, 340), (11700, 484), (13900, 600), (80650, 4271), (215400, 12356), (1077550, 71413), (5000000, 449929), (25000000, 2509929)],
    "hoh": [(0, 0), (12800, 512), (17650, 730), (20900, 901), (107650, 5672), (269300, 15371), (1616450, 107651), (5000000, 434163), (25000000, 2494163)],
}
GROUP = {"single": "single", "mfs": "single", "mfj": "mfj", "qss": "mfj", "hoh": "hoh"}


def schedule(amount, status, bands=RS, rates=RATES):
    """"<base> plus <rate> of the excess over <over>" for the band with over < amount <= but not over (the first band
    from 0); the product rounded to the whole dollar (decision C4)."""
    rows = bands[GROUP[status]]
    i = 0
    while i + 1 < len(rows) and amount > rows[i + 1][0]:
        i += 1
    over, base = rows[i]
    return base + r_dollar(rates[i] * (amount - over))


# --- New York City tax rate schedule (IT-201-I p. 40) ---
CITY_RATES = [F(3078, 100000), F(3762, 100000), F(3819, 100000), F(3876, 100000)]
CITY = {"mfj": [(0, 0), (21600, 665), (45000, 1545), (90000, 3264)],
        "single": [(0, 0), (12000, 369), (25000, 858), (50000, 1813)],
        "hoh": [(0, 0), (14400, 443), (30000, 1030), (60000, 2176)]}


class _Tables(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.cap, self.incap, self.cell, self.row, self.rows = None, False, None, None, {}

    def handle_starttag(self, tag, attrs):
        if tag == "caption":
            self.incap, self.cap = True, ""
        elif tag == "tr":
            self.row = []
        elif tag == "td" and self.row is not None:
            self.cell = ""

    def handle_endtag(self, tag):
        if tag == "caption":
            self.incap, self.cap = False, " ".join(self.cap.split())
        elif tag == "td" and self.cell is not None:
            self.row.append(self.cell)
            self.cell = None
        elif tag == "tr" and self.row is not None:
            if len(self.row) == 5:
                self.rows.setdefault(self.cap, []).append([int(re.sub(r"[^\d]", "", c)) for c in self.row])
            self.row = None

    def handle_data(self, d):
        if self.incap:
            self.cap += d
        elif self.cell is not None:
            self.cell += d


_TABLES = None


def tax_table(amount, status, city=False):
    """The 2025 New York State or City Tax Table (the archived web page, read directly from its HTML here, not from
    tables/ny/): the row "At least" <= amount < "But less than", the column "Single or Married filing separately",
    "Married filing jointly*" (with a qualifying surviving spouse) or "Head of a household"."""
    global _TABLES
    if _TABLES is None:
        p = _Tables()
        p.feed((NYDIR / "ny_it201_tax_tables.html").read_bytes().decode("utf-8"))
        _TABLES = p.rows
    rows = _TABLES["New York City Tax Table" if city else "New York State Tax Table"]
    col = {"single": 2, "mfs": 2, "mfj": 3, "qss": 3, "hoh": 4}[status]
    for row in rows:
        if row[0] <= amount < row[1]:
            return row[col]
    raise ValueError(amount)


# --- Tax computation worksheets (IT-201-I pp. 34-39) ---
FIRST = {"mfj": (F(55, 1000), 161550), "single": (F(6, 100), 215400), "hoh": (F(6, 100), 269300)}  # worksheets 1, 7, 12
LATER = {  # worksheets 2-5, 8-10, 13-15: (start, ti limit or None, recapture base, incremental benefit)
    "mfj": [(161550, 323200, 333, 807), (323200, 2155350, 1140, 2747), (2155350, 5000000, 3887, 60350), (5000000, None, 64237, 32500)],
    "single": [(215400, 1077550, 568, 1831), (1077550, 5000000, 2399, 30172), (5000000, None, 32571, 32500)],
    "hoh": [(269300, 1616450, 787, 2289), (1616450, 5000000, 3076, 45261), (5000000, None, 48337, 32500)],
}


def ratio4(part, whole):
    """"Divide ... by $50,000 and round the result to the fourth decimal place" (half-up, amb.ny.2025.fourth_decimal)."""
    return F(r_dollar(F(part, whole) * 10000), 10000)


def worksheet(agi, ti, status):
    g = GROUP[status]
    if agi > 25000000:  # worksheets 6, 11, 16: "Multiply line 1 by 10.9% (0.109)"
        return "top", r_dollar(F(109, 1000) * ti)
    rate, limit = FIRST[g]
    if ti <= limit:
        line3 = r_dollar(rate * ti)
        if agi >= 157650:  # "Stop: If the line 1 amount is $157,650 or more ... enter the line 3 amount on line 9"
            return "first-stop", line3
        line4 = schedule(ti, status)
        line5 = line3 - line4
        line7 = ratio4(agi - 107650, 50000)
        # line 8: the prorate atom rounds the product to the cent, then the line is rounded to the dollar
        return "first", line4 + r_dollar(F(r_dollar(line5 * line7 * 100), 100))
    for start, tlim, base, incr in LATER[g]:
        if tlim is None or ti <= tlim:
            line7 = min(agi - start, 50000)
            line8 = ratio4(line7, 50000)
            return f"later-{start}", schedule(ti, status) + base + r_dollar(F(r_dollar(incr * line8 * 100), 100))
    raise ValueError(ti)


def nys_tax(agi, ti, status):
    """Line 39 (p. 12): NY AGI $107,650 or less: the Tax Table below $65,000 of taxable income, else the rate
    schedule; above $107,650, the tax computation worksheets."""
    if agi <= 107650:
        return ("table", tax_table(ti, status)) if ti < 65000 else ("schedule", schedule(ti, status))
    return worksheet(agi, ti, status)


def nyc_tax(cti, status):
    """Line 47a (p. 13): "Is line 47 ... less than $65,000? • If Yes ... New York City Tax Table ... • If No ... New
    York City tax rate schedule"."""
    return tax_table(cti, status, city=True) if cti < 65000 else schedule(cti, status, CITY, CITY_RATES)


# --- household credits (pp. 12-14) ---
HH_STATE_1 = [(5000, 75), (6000, 60), (7000, 50), (20000, 45), (25000, 40), (28000, 20)]
HH_STATE_2 = [(5000, [90, 105, 120, 135, 150, 165, 180]), (6000, [75, 90, 105, 120, 135, 150, 165]), (7000, [65, 80, 95, 110, 125, 140, 155]),
              (20000, [60, 75, 90, 105, 120, 135, 150]), (22000, [60, 70, 80, 90, 100, 110, 120]), (25000, [50, 60, 70, 80, 90, 100, 110]),
              (28000, [40, 45, 50, 55, 60, 65, 70]), (32000, [20, 25, 30, 35, 40, 45, 50])]
HH_CITY_4 = [(10000, 15), (12500, 10)]
HH_CITY_5 = [(15000, [30, 60, 90, 120, 150, 180, 210]), (17500, [25, 50, 75, 100, 125, 150, 175]), (20000, [15, 30, 45, 60, 75, 90, 105]),
             (22500, [10, 20, 30, 40, 50, 60, 70])]


def household(fagi, status, people, item_c, city):
    """None when refused (married filing separately, or more than 7 people, within the credit rows)."""
    if item_c:
        return 0
    single_t, multi_t = (HH_CITY_4, HH_CITY_5) if city else (HH_STATE_1, HH_STATE_2)
    limit = multi_t[-1][0]
    if status == "mfs":
        return None if fagi <= limit else 0
    if status == "single":
        for notover, amt in single_t:
            if fagi <= notover:
                return amt
        return 0
    for notover, amts in multi_t:
        if fagi <= notover:
            return None if people > 7 else amts[people - 1]
    return 0


def sales_use(fagi, owes):
    """Line 59 (p. 18) chart; 0 when no use tax is owed (p. 19)."""
    if not owes:
        return 0
    for upto, amt in [(15000, 3), (30000, 6), (50000, 10), (75000, 15), (100000, 18), (150000, 26), (200000, 34)]:
        if fagi <= upto:
            return amt
    return min(r_dollar(F(175, 1000000) * fagi), 125)


def predict(fed, ny):
    """fed: federal amounts in cents (keys f1040.line1z ... f1040.line11a, s1.*, f1040.line27a, eic.limit) and the
    status; ny: the New York answers. Returns {line: value} with money in cents, or {"refused": gate}."""
    status = fed["status"]
    d = lambda k: F(fed.get(k, 0), 100)  # noqa: E731
    # Lines 65 and 70 (p. 19, p. 20): "Did you claim the federal earned income credit ... or could you have claimed it
    # based on your federal adjusted gross income?" Refused when the federal credit is more than zero or federal AGI is
    # under the federal credit's income limit (decision B9, amb.ny.2025.eic_could_claim).
    if fed.get("f1040.line27a", 0) > 0 or fed["f1040.line11a"] < fed["eic.limit"]:
        return {"refused": "eic"}
    out = {}
    L = {}
    for n, k in [(1, "f1040.line1z"), (2, "f1040.line2b"), (3, "f1040.line3b"), (4, "s1.line1"), (5, "s1.line2a"), (6, "s1.line3"),
                 (7, "f1040.line7a"), (9, "f1040.line4b"), (10, "f1040.line5b"), (14, "s1.line7"), (15, "f1040.line6b"), (16, "s1.line9"), (18, "s1.line26")]:
        L[n] = r_dollar(d(k))
    L[8] = L[11] = L[13] = 0
    L[17] = sum(L[n] for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16))
    L[19] = L[17] - L[18]
    L[24] = L[19]
    L[27] = L[15]
    L[32] = L[27]
    L[33] = L[24] - L[32]
    item_c = ny.get("item_c", False)
    L[34] = 3100 if (status == "single" and item_c) else {"single": 8000, "mfs": 8000, "mfj": 16050, "qss": 16050, "hoh": 11200}[status]
    L[35] = max(L[33] - L[34], 0)
    deps = ny.get("dependents", 0)
    L[36] = 1000 * deps
    L[37] = max(L[35] - L[36], 0)
    L[38] = L[37]
    method, L[39] = nys_tax(L[33], L[38], status)
    people = deps + 1 + (1 if status == "mfj" else 0)
    hs = household(max(L[19], 0), status, people, item_c, False)
    hc = household(max(L[19], 0), status, people, item_c, True)
    if hs is None or hc is None:
        return {"refused": "household"}
    L[40], L[48] = hs, hc
    L[43] = L[40]
    L[44] = max(L[39] - L[43], 0)
    L[46] = L[44]
    L[47] = L[38]
    L["47a"] = nyc_tax(L[47], status)
    L[49] = max(L["47a"] - L[48], 0)
    L[52] = L[49]
    L[54] = L[52]
    L[58] = L[54]
    L[59] = sales_use(max(L[19], 0), ny.get("owes_use_tax", False))
    L[61] = L[46] + L[58] + L[59]
    L[62] = L[61]
    stc_income = L[19] - L[9]
    L[69] = 0 if item_c or stc_income > 250000 else (125 if status in ("mfj", "qss") else 63)
    # Line 63 (p. 19): "Do you have at least one qualifying child? (A qualifying child must be less than 17 years old on
    # December 31st of the tax year.)" With one, Form IT-213 is needed: refused; lines 76 to 80 read it.
    if ny.get("under17", 0) > 0:
        out = {f"ny_it201.line{k}": v * 100 for k, v in L.items()}
        out["refused"] = "child_credit"
        out["_method"] = method
        return out
    # Line 70a (p. 21; IT-270-I p. 1): with a dependent on item H and federal AGI no more than $5,000 above the highest
    # income threshold ($91,902 joint, $88,361 others), the NYC income tax elimination credit may apply: refused
    # (decision B10); the lines that read it (76 to 80) are refused too.
    if deps > 0 and L[19] <= (91902 if status in ("mfj", "qss") else 88361) + 5000:
        out = {f"ny_it201.line{k}": v * 100 for k, v in L.items()}
        out["refused"] = "it270"
        out["_method"] = method
        return out
    if not item_c and (stc_income > 500000 or L[47] > 500000):
        # Line 69a refuses (decision B7); the lines that read it (76 to 80) are refused too. The rest stands.
        out = {f"ny_it201.line{k}": v * 100 for k, v in L.items()}
        out["refused"] = "stc_rr"
        out["_method"] = method
        return out
    over, base = {"mfj": (21600, 37), "qss": (21600, 37), "single": (12000, 21), "mfs": (12000, 21), "hoh": (14400, 25)}[status]
    L["69a"] = 0 if item_c else (r_dollar(F(171, 100000) * L[47]) if L[47] <= over else base + r_dollar(F(228, 100000) * (L[47] - over)))
    L[72] = sum(r_dollar(F(w, 100)) for w in ny.get("state_withheld", []))
    L[73] = sum(r_dollar(F(w, 100)) for w in ny.get("city_withheld", []))
    L[75] = r_dollar(F(ny.get("line75", 0), 100))
    L[76] = L[69] + L["69a"] + L[72] + L[73] + L[75]
    due = max(L[62] - L[76], 0)
    prior = F(ny.get("prior_year_tax", 0), 100) * (F(11, 10) if ny.get("prior_agi_high") else 1)
    if due > 0 and (L[72] + L[73] + L[75]) < prior:
        return {"refused": "estimated_penalty"}
    L[77] = max(L[76] - L[62], 0)
    L[79] = r_dollar(F(ny.get("line79", 0), 100))
    if L[79] > L[77]:
        return {"refused": "line79"}
    L[78] = L[77] - L[79]
    L["78b"] = L[78]
    L[80] = due
    for k, v in L.items():
        out[f"ny_it201.line{k}"] = v * 100
    out["_method"] = method
    return out


def self_test():
    ok = tax_table(38275, "mfj") == 1773 and tax_table(38275, "mfj", city=True) == 1292
    print("ny_predict self-test, the official tax-table examples ($38,275, married filing jointly: State $1,773, City $1,292): "
          + ("reproduced" if ok else "WRONG"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    print(json.dumps(predict(json.loads(sys.argv[1]), json.loads(sys.argv[2]))))
