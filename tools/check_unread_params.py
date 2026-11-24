#!/usr/bin/env python3
"""Every parameter of params/<year>.yaml and params/ny/<year>.yaml (the keys of `values`) is read by something.

    check_unread_params.py [--year N]
    check_unread_params.py --self-test        (tools/test_check_unread_params.py)

A parameter is read when its key stands as a whole name (not inside a longer id: `x.key`, `key_more` and
`key.more` are other names) in a file of the readers: forms/<year>/, forms/ny/<year>/, interview/<year>/,
interview/ny/<year>/, the next year's prepared operations (changes/<year+1>/, changes/ny/<year+1>/), and the code
under engine/src, tools, ui and lean (build output and dependencies left out; tools/unread_params_allow.json
itself is not a reader). A mention in a comment counts as a read.

A parameter that code reads by a name it builds (`eic.earned_amount${k}`) is listed in
tools/unread_params_allow.json, {"allow": {key: {"built": prefix, "in": [file, ...], "reason": text}}}: the entry
holds while the key is a parameter, no reader names it whole, and each file of `in` builds a name from `prefix`
(`prefix` followed by `${` or `{`). An unread parameter that is not listed fails the check, and so does an entry
that no longer holds. A parameter that nothing reads is removed, with its staged next-year value
(research/ty<year+1>/), rather than listed.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

ALLOW = Path("tools") / "unread_params_allow.json"
CODE_DIRS = ("engine/src", "tools", "ui", "lean")
CODE_SUFFIXES = {".ts", ".tsx", ".mjs", ".js", ".py", ".sh", ".lean", ".json", ".yaml", ".yml"}
SKIP_DIRS = {"node_modules", "dist", ".lake", "build", "__pycache__"}


def param_keys(root, year):
    """{key: params file} of the parameters of both jurisdictions for `year`."""
    import yaml
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    out = {}
    for rel in (Path("params") / f"{year}.yaml", Path("params") / "ny" / f"{year}.yaml"):
        p = root / rel
        if p.exists():
            data = (yaml.load(p.read_text(encoding="utf-8"), Loader=loader) or {}).get("params") or {}
            for k in data.get("values") or {}:
                out[k] = rel.as_posix()
    return out


def reader_files(root, year):
    """[path] of the files that count as readers (module doc)."""
    year = int(year)
    out = []
    for rel in (f"forms/{year}", f"forms/ny/{year}", f"interview/{year}", f"interview/ny/{year}",
                f"changes/{year + 1}", f"changes/ny/{year + 1}"):
        d = root / rel
        if d.is_dir():
            out += [p for p in d.rglob("*") if p.is_file() and p.suffix in (".yaml", ".yml", ".json")]
    for rel in CODE_DIRS:
        d = root / rel
        if d.is_dir():
            out += [p for p in d.rglob("*") if p.is_file() and p.suffix in CODE_SUFFIXES
                    and not SKIP_DIRS.intersection(p.relative_to(d).parts[:-1])]
    allow = (root / ALLOW).resolve()
    return sorted(p for p in out if p.resolve() != allow)


def whole_name(keys):
    return re.compile(r"(?<![A-Za-z0-9_.])(" + "|".join(map(re.escape, sorted(keys, key=len, reverse=True)))
                      + r")(?![A-Za-z0-9_]|\.[A-Za-z0-9_])")


def check(root=ROOT, year=None):
    """(problems, {key: reason} of the listed parameters, count of parameters)."""
    if year is None:
        from taxyear import Y
        year = Y
    root = Path(root)
    keys = param_keys(root, year)
    if not keys:
        return [f"no parameters found for {year}"], {}, 0
    texts = {p: p.read_text(encoding="utf-8", errors="replace") for p in reader_files(root, year)}
    rx = whole_name(keys)
    read = set()
    for text in texts.values():
        read.update(rx.findall(text))
    allow_path = root / ALLOW
    allow = json.loads(allow_path.read_text(encoding="utf-8")).get("allow", {}) if allow_path.exists() else {}
    problems = []
    for key in sorted(k for k in keys if k not in read and k not in allow):
        problems.append(f"{key} ({keys[key]}): read by no form, interview, change file, engine source or tool; remove "
                        f"it (and its staged next-year value), or list it in {ALLOW} if code reads it by a built name")
    for key, entry in sorted(allow.items()):
        prefix, files = entry.get("built"), entry.get("in") or []
        if key not in keys:
            problems.append(f"{key}: listed in {ALLOW} but not a parameter of {year}; remove the entry")
        elif key in read:
            problems.append(f"{key}: listed in {ALLOW} but read by name; remove the entry")
        elif not isinstance(prefix, str) or not key.startswith(prefix) or not files or not entry.get("reason"):
            problems.append(f"{key}: the entry in {ALLOW} needs `built` (a prefix of the key), `in` and `reason`")
        else:
            built = re.compile(re.escape(prefix) + r"\$?\{")
            for f in files:
                text = texts.get(root / f)
                if text is None and (root / f).exists():
                    text = (root / f).read_text(encoding="utf-8", errors="replace")
                if text is None or not built.search(text):
                    problems.append(f"{key}: {f} builds no name from {prefix} (listed in {ALLOW}); fix the entry")
    return problems, {k: allow[k].get("reason", "") for k in allow if k in keys}, len(keys)


def main(argv):
    if argv == ["--self-test"]:
        import test_check_unread_params
        return test_check_unread_params.main()
    from taxyear import Y
    problems, listed, n = check(ROOT, Y)
    if problems:
        print(f"unread parameters: {len(problems)} problem(s) among {n} parameters of {Y}:")
        for p in problems:
            print("  " + p)
        return 1
    print(f"unread parameters: every one of {n} parameters of {Y} is read ({len(listed)} by a built name, "
          f"listed in {ALLOW})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
