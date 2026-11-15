#!/usr/bin/env python3
"""Replace each birth-year literal of a form line by its age parameter (params/2025.yaml, age.cut_*), restating the
comparison where the parameter is one more than the literal (le N -> lt N+1, gt N -> ge N+1). Run once."""
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
CUT = {"age.cut_65": 1961, "age.cut_25": 2001, "age.cut_24": 2002, "age.cut_19": 2007, "age.cut_18": 2008,
       "age.cut_16": 2010, "age.cut_50": 1976, "age.cut_55": 1971, "age.cut_60": 1966, "age.cut_64": 1962,
       "age.cut_73": 1953, "age.turning_65": 1960}
BY_YEAR = {v: k for k, v in CUT.items()}
# a literal one below a cut: N <= lit  ==  N < lit+1 ;  N > lit  ==  N >= lit+1
SHIFT = {"le": "lt", "gt": "ge"}
NEXT = {"lt": None, "ge": None}  # literal one above a cut used with ge/lt: ge lit == gt lit-1 ; lt lit == le lit-1
LOW = {"ge": "gt", "lt": "le"}
for name in ("forms/2025/person.yaml", "forms/2025/f8889.yaml"):
    path = ROOT / name
    L = path.read_text().split("\n")
    i = 0
    n = 0
    while i < len(L):
        m = re.match(r"(\s*)- const: ((?:19|20)\d\d)$", L[i])
        if m and L[i + 1].strip() == "type: Count":
            year = int(m.group(2))
            j = i - 1
            while not re.match(r"\s*(eq|ne|lt|le|gt|ge):$", L[j]):
                j -= 1
            op = L[j].strip()[:-1]
            ind = re.match(r"\s*", L[j]).group()
            if year in BY_YEAR:
                param, newop = BY_YEAR[year], op
            elif year + 1 in BY_YEAR and op in SHIFT:
                param, newop = BY_YEAR[year + 1], SHIFT[op]
            elif year - 1 in BY_YEAR and op in LOW:
                param, newop = BY_YEAR[year - 1], LOW[op]
            else:
                raise SystemExit(f"{name}:{i + 1}: no parameter for {op} {year}")
            L[j] = f"{ind}{newop}:"
            L[i] = f"{m.group(1)}- param: {param}"
            del L[i + 1]
            n += 1
        i += 1
    path.write_text("\n".join(L))
    print(name, n, "literals replaced")
