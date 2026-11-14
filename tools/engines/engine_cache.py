#!/usr/bin/env python3
"""Reuse of the outside engines' records in the engine differential.

run_engines.py runs each outside engine through `Cache.record`: the engine's record for engines.json is
stored under .engines/cache/<engine>/<key>.json and reused while its key is unchanged. The key is the
sha256 of everything that determines the record:

- the generated cases: the bytes of the cases file (every case's facts and features);
- the tax year;
- the adapter code: every file under tools/engines/ except NOT_READ (the files the engine run neither
  imports nor reads), tools/taxyear.py, and canonical/<year>/params.json, from which the OpenTaxSolver and
  UsTaxes adapters take the amounts they supply;
- the engine as installed (the `identity` run_engines.py gives for it): for PolicyEngine-US and
  Tax-Calculator the interpreter's version, every distribution installed beside them with its version, and
  the bytes of the engine's own packages; for OpenTaxSolver the bytes of the extracted package and the
  version it reports; for UsTaxes the bytes of the clone (its .git directory left out, its commit read
  instead) and of its runtime packages, and the Node version.

ENGINE_CACHE selects the mode:

    use      (the default) reuse the stored record whose key matches; otherwise run the engine and store its record
    verify   run every engine; where a record is stored under the same key, it must equal the fresh one, or the run
             fails naming the engine and the first differences (the stored record is kept aside as <key>.stale);
             the fresh record is stored
    off      run every engine, reading and storing nothing

The project's own evaluation of the cases and the line-by-line comparison are not cached: run.sh runs them
every time. A stored record is reused only if the components stored with it hash to its key. After the engines
have run, `check_modules` requires every module the process loaded from the repository to be among the hashed
files, so an adapter that comes to import a file the key leaves out fails the run rather than reading an old
record. The newest KEEP records of each engine are kept.

    engine_cache.py --self-test     the key, the modes and the module check on planted cases, in a temporary folder
"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE_DIR = ROOT / ".engines" / "cache"
MODES = ("use", "verify", "off")
KEEP = 6
# Files under tools/engines/ that the engine run neither imports nor reads: the comparison and its tests, the case
# generator (its output, the cases file, is hashed whole), the scripts that call the run, the installs' recipe
# (the installs themselves are each engine's identity), the New York engine run and the documentation.
NOT_READ = {"compare.py", "test_compare.py", "generate_cases.py", "run.sh", "setup.sh", "requirements.txt",
            "ny_policyengine.py", "README.md"}


def tree_digest(base, skip_dirs=("__pycache__", ".git")):
    """sha256 over every file under `base`, by path relative to it and contents, in path order; None when absent."""
    base = Path(base)
    if not base.exists():
        return None
    h = hashlib.sha256()
    files = [base] if base.is_file() else sorted(p for p in base.rglob("*") if p.is_file() and not set(p.relative_to(base).parts) & set(skip_dirs))
    for p in files:
        h.update(str(p.relative_to(base) if p != base else p.name).encode() + b"\0")
        h.update(hashlib.sha256(p.read_bytes()).digest())
    return h.hexdigest()


def adapter_files(root, year):
    """The repository files the key hashes: tools/engines/ less NOT_READ, tools/taxyear.py, canonical/<year>/params.json."""
    engines = Path(root) / "tools" / "engines"
    files = sorted(p for p in engines.rglob("*") if p.is_file() and "__pycache__" not in p.parts
                   and not (p.parent == engines and p.name in NOT_READ))
    return files + [Path(root) / "tools" / "taxyear.py", Path(root) / "canonical" / str(year) / "params.json"]


def adapter_digest(root, year):
    """{relative path: sha256} of adapter_files; a missing file is recorded as None."""
    out = {}
    for p in adapter_files(root, year):
        out[str(p.relative_to(root))] = hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
    return out


def key_of(components):
    return hashlib.sha256(json.dumps(components, sort_keys=True).encode()).hexdigest()


def normal(record):
    """The record as engines.json holds it (tuples become lists)."""
    return json.loads(json.dumps(record))


def differences(stored, fresh, path="", out=None, limit=5):
    """Up to `limit` paths at which two JSON values differ, each with both values."""
    out = [] if out is None else out
    if len(out) >= limit:
        return out
    if isinstance(stored, dict) and isinstance(fresh, dict):
        for k in sorted(set(stored) | set(fresh)):
            if k not in stored or k not in fresh:
                out.append(f"{path}/{k}: {'absent' if k not in stored else 'present'} in the stored record, "
                           f"{'absent' if k not in fresh else 'present'} in the fresh one")
            else:
                differences(stored[k], fresh[k], f"{path}/{k}", out, limit)
            if len(out) >= limit:
                break
    elif isinstance(stored, list) and isinstance(fresh, list) and len(stored) == len(fresh):
        for i, (a, b) in enumerate(zip(stored, fresh)):
            differences(a, b, f"{path}[{i}]", out, limit)
            if len(out) >= limit:
                break
    elif stored != fresh:
        out.append(f"{path or '/'}: stored {json.dumps(stored)[:80]}, fresh {json.dumps(fresh)[:80]}")
    return out


class StaleRecord(Exception):
    pass


class Cache:
    """The records of one run: `base` holds the components every engine shares (cases, year, adapter code)."""

    def __init__(self, base, mode=None, folder=CACHE_DIR, log=print, keep=KEEP):
        self.base, self.folder, self.log, self.keep = base, Path(folder), log, keep
        self.mode = mode if mode is not None else os.environ.get("ENGINE_CACHE", "use") or "use"
        if self.mode not in MODES:
            raise SystemExit(f"ENGINE_CACHE={self.mode}: expected one of {', '.join(MODES)}")
        self.stale = []

    def path(self, engine, key):
        return self.folder / engine.replace(" ", "_") / f"{key}.json"

    def stored(self, engine, components, key):
        """The record stored under `key`, if its stored components hash to the key and equal ours."""
        p = self.path(engine, key)
        if not p.exists():
            return None
        try:
            entry = json.loads(p.read_text())
        except (OSError, ValueError):
            self.log(f"{engine}: the stored record {p.name} does not read as JSON; ignored")
            return None
        if entry.get("key") != key or key_of(entry.get("components")) != key or entry.get("components") != components:
            self.log(f"{engine}: the stored record {p.name} does not match its key; ignored")
            return None
        return entry["record"]

    def store(self, engine, components, key, record):
        p = self.path(engine, key)
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_name(f".{p.name}.{os.getpid()}.tmp")
        tmp.write_text(json.dumps({"key": key, "components": components, "record": record}))
        os.replace(tmp, p)
        kept = sorted((q for q in p.parent.glob("*.json")), key=lambda q: q.stat().st_mtime, reverse=True)
        for q in kept[self.keep:]:
            q.unlink(missing_ok=True)

    def record(self, engine, identity, run):
        """The engine's record: stored under the key of (base, engine, identity) or produced by `run()`.
        `run` returns None when the engine is not installed; nothing is stored then."""
        if self.mode == "off" or identity is None:
            return run()
        components = {**self.base, "engine": engine, "identity": identity}
        key = key_of(components)
        stored = self.stored(engine, components, key)
        if self.mode == "use" and stored is not None:
            os.utime(self.path(engine, key))
            self.log(f"{engine}: stored record reused (key {key[:12]}; ENGINE_CACHE=verify reruns and compares)")
            return stored
        t0 = time.monotonic()
        fresh = run()
        if fresh is None:
            return None
        fresh = normal(fresh)
        took = f"{time.monotonic() - t0:.0f} s"
        if self.mode == "verify":
            if stored is None:
                self.log(f"{engine}: verify: ran in {took}; no record stored under key {key[:12]}; the fresh one is stored")
            elif stored != fresh:
                diffs = differences(stored, fresh)
                self.stale.append(engine)
                p = self.path(engine, key)
                os.replace(p, p.with_name(f"{key}.stale"))
                self.log(f"{engine}: verify: ran in {took}; the stored record under key {key[:12]} differs from a fresh run: " + "; ".join(diffs)
                         + f"; it is kept as {p.with_name(key + '.stale')} and the fresh record stored")
            else:
                self.log(f"{engine}: verify: ran in {took}; the stored record under key {key[:12]} equals it")
        else:
            self.log(f"{engine}: ran in {took} (no record stored under key {key[:12]})")
        self.store(engine, components, key, fresh)
        return fresh

    def finish(self):
        """Raise when verify found a stored record that differs from a fresh run."""
        if self.stale:
            raise StaleRecord(f"engine cache: the stored records of {', '.join(self.stale)} differ from a fresh run under the same "
                              f"key, so the key misses an input (the stale records are kept as <key>.stale in {self.folder})")


def base_components(cases_bytes, year, root=ROOT):
    return {"cases": hashlib.sha256(cases_bytes).hexdigest(), "year": year, "adapter": adapter_digest(root, year)}


def check_modules(root, year, modules=None):
    """The modules loaded from `root` that adapter_files does not cover (empty when every one is hashed)."""
    hashed = {p.resolve() for p in adapter_files(root, year)}
    root = Path(root).resolve()
    out = []
    for name, mod in list((modules if modules is not None else sys.modules).items()):
        f = getattr(mod, "__file__", None)
        if not f:
            continue
        p = Path(f).resolve()
        if p.is_relative_to(root) and ".engines" not in p.relative_to(root).parts and p not in hashed:
            out.append(f"{name} ({p.relative_to(root)})")
    return sorted(out)


# ---------------------------------------------------------------------------------------------
# Engine identities


def python_identity(packages):
    """The interpreter, every installed distribution with its version, and the bytes of `packages`."""
    from importlib import metadata, util
    dists = sorted(f"{d.metadata['Name']}=={d.version}" for d in metadata.distributions())
    own = {}
    for name in packages:
        spec = util.find_spec(name)
        if spec is None:
            return None
        locations = list(spec.submodule_search_locations or []) or [spec.origin]
        own[name] = [tree_digest(loc) for loc in locations]
    return {"python": sys.version, "distributions": dists, "packages": own}


def node_version():
    try:
        return subprocess.run(["node", "--version"], capture_output=True, text=True).stdout.strip()
    except OSError:
        return None


# ---------------------------------------------------------------------------------------------
# Self-test


def self_test():
    problems, checks = [], 0
    with tempfile.TemporaryDirectory(prefix="engine-cache-test-") as tmp:
        root = Path(tmp) / "repo"
        (root / "tools" / "engines" / "ustaxes").mkdir(parents=True)
        (root / "canonical" / "2025").mkdir(parents=True)
        for name in ("run_engines.py", "ots_adapter.py", "compare.py", "generate_cases.py"):
            (root / "tools" / "engines" / name).write_text(f"# {name}\n")
        (root / "tools" / "engines" / "ustaxes" / "run.mjs").write_text("// runner\n")
        (root / "tools" / "taxyear.py").write_text("YEAR = 2025\n")
        params = root / "canonical" / "2025" / "params.json"
        params.write_text('{"params": {"values": {"a": {"value": 1}}}}')
        folder = Path(tmp) / "cache"
        cases = json.dumps([{"id": "c1", "facts": {"wages": 100}}]).encode()
        calls = []

        def engine(value):
            def run():
                calls.append(value)
                return {"version": "1.0", "lines": {"c1": {"f1040.line1a": value}}, "limits": ("a", "b")}
            return run

        def check(cond, what):
            nonlocal checks
            checks += 1
            if not cond:
                problems.append(what)

        log = []

        def cache(base, mode, folder, log):
            return Cache(base, mode, folder, log, keep=100)
        base = base_components(cases, 2025, root)
        ident = {"version": "1.0", "bytes": "aa"}
        c = cache(base, "use", folder, log.append)
        r1 = c.record("E", ident, engine(100))
        check(calls == [100] and r1["limits"] == ["a", "b"], "a cold cache did not run the engine once and return its record")
        r2 = cache(base, "use", folder, log.append).record("E", ident, engine(999))
        check(calls == [100] and r2 == r1, "a warm cache with an unchanged key ran the engine or returned another record")
        changed = base_components(json.dumps([{"id": "c1", "facts": {"wages": 101}}]).encode(), 2025, root)
        cache(changed, "use", folder, log.append).record("E", ident, engine(101))
        check(calls == [100, 101], "a changed case read the stored record")
        cache(base, "use", folder, log.append).record("E", {"version": "1.1", "bytes": "aa"}, engine(102))
        check(calls[-1] == 102, "a changed engine version read the stored record")
        cache(base, "use", folder, log.append).record("E", {"version": "1.0", "bytes": "ab"}, engine(103))
        check(calls[-1] == 103, "an engine reinstalled in place (same version, other bytes) read the stored record")
        cache(base_components(cases, 2024, root), "use", folder, log.append).record("E", ident, engine(104))
        check(calls[-1] == 104, "another tax year read the stored record")
        for rel, what in ((("tools", "engines", "ots_adapter.py"), "an adapter"), (("tools", "engines", "ustaxes", "run.mjs"), "the UsTaxes runner"),
                          (("tools", "taxyear.py"), "tools/taxyear.py"), (("canonical", "2025", "params.json"), "the parameters an adapter reads")):
            p = root.joinpath(*rel)
            before = p.read_bytes()
            p.write_bytes(before + b"\n")
            n = len(calls)
            cache(base_components(cases, 2025, root), "use", folder, log.append).record("E", ident, engine(105))
            check(len(calls) == n + 1, f"a change to {what} read the stored record")
            p.write_bytes(before)
        new = root / "tools" / "engines" / "new_adapter.py"
        new.write_text("# new\n")
        n = len(calls)
        cache(base_components(cases, 2025, root), "use", folder, log.append).record("E", ident, engine(106))
        check(len(calls) == n + 1, "a new file under tools/engines/ read the stored record")
        new.unlink()
        (root / "tools" / "engines" / "compare.py").write_text("# compare, changed\n")
        n = len(calls)
        cache(base_components(cases, 2025, root), "use", folder, log.append).record("E", ident, engine(107))
        check(len(calls) == n, "a change to the comparison (not read by the engine run) reran the engine")
        check(cache(base, "off", folder, log.append).record("E", ident, engine(108)) and calls[-1] == 108,
              "ENGINE_CACHE=off did not run the engine")
        check(cache(base, "use", folder, log.append).record("E", ident, engine(109))["lines"]["c1"]["f1040.line1a"] == 100,
              "ENGINE_CACHE=off changed the stored record")

        # verify: an equal stored record passes; a planted stale one under the same key fails the run.
        v = cache(base, "verify", folder, log.append)
        v.record("E", ident, engine(100))
        try:
            v.finish()
            check(True, "")
        except StaleRecord:
            check(False, "verify failed on a stored record equal to a fresh run")
        key = key_of({**base, "engine": "E", "identity": ident})
        entry = json.loads(v.path("E", key).read_text())
        entry["record"]["lines"]["c1"]["f1040.line1a"] = 99
        v.path("E", key).write_text(json.dumps(entry))
        used = cache(base, "use", folder, log.append).record("E", ident, engine(100))
        check(used["lines"]["c1"]["f1040.line1a"] == 99, "the planted stale record was not what the use mode read (the plant tests nothing)")
        v = cache(base, "verify", folder, log.append)
        out = v.record("E", ident, engine(100))
        try:
            v.finish()
            check(False, "verify passed a planted stale record")
        except StaleRecord as e:
            check("E" in str(e) and out["lines"]["c1"]["f1040.line1a"] == 100, "verify did not name the engine or return the fresh record")
        check(any("/lines/c1/f1040.line1a: stored 99, fresh 100" in line for line in log), "verify did not name the differing line")
        check(json.loads(v.path("E", key).with_name(f"{key}.stale").read_text())["record"]["lines"]["c1"]["f1040.line1a"] == 99
              and json.loads(v.path("E", key).read_text())["record"]["lines"]["c1"]["f1040.line1a"] == 100,
              "verify did not set the stale record aside and store the fresh one")
        entry = json.loads(v.path("E", key).read_text())

        # A record whose stored components do not hash to its key is not read.
        entry["components"]["cases"] = "0" * 64
        v.path("E", key).write_text(json.dumps(entry))
        n = len(calls)
        cache(base, "use", folder, log.append).record("E", ident, engine(100))
        check(len(calls) == n + 1, "a record whose components do not match its key was reused")
        # An engine that is not installed (identity None, or a run that returns None) stores nothing.
        n_files = len(list(folder.rglob("*.json")))
        check(cache(base, "use", folder, log.append).record("F", None, lambda: None) is None
              and cache(base, "use", folder, log.append).record("F", ident, lambda: None) is None
              and len(list(folder.rglob("*.json"))) == n_files, "an engine that is not installed stored a record")

        # Only the newest `keep` records of an engine are kept.
        small = Path(tmp) / "small"
        for v in (1, 2, 3):
            Cache({**base, "n": v}, "use", small, log.append, keep=2).record("E", ident, engine(v))
        check(len(list((small / "E").glob("*.json"))) == 2, "more than `keep` records were kept")

        # The module check: a module loaded from the repository outside the hashed files is reported.
        class M:
            def __init__(self, f):
                self.__file__ = str(f)
        mods = {"run_engines": M(root / "tools" / "engines" / "run_engines.py"), "taxyear": M(root / "tools" / "taxyear.py"),
                "json": M(Path(json.__file__))}
        check(check_modules(root, 2025, mods) == [], "the module check reported a hashed module")
        mods["compare"] = M(root / "tools" / "engines" / "compare.py")
        mods["coverage"] = M(root / "tools" / "coverage" / "__init__.py")
        check(len(check_modules(root, 2025, mods)) == 2, "the module check missed a module the key does not hash")
        check(check_modules(ROOT, 2025) == [], f"this process loaded unhashed repository modules: {check_modules(ROOT, 2025)}")
    for p in problems:
        print(f"engine cache self-test: {p}")
    print(f"engine cache self-test: {checks} checks, {len(problems)} problems (a planted stale record caught by verify)")
    return 1 if problems else 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        sys.exit(self_test())
    sys.exit(__doc__)
