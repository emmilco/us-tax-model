#!/usr/bin/env python3
"""Unit tests of tools/check_unread_params.py on a small tree of its own: parameters read by a form, a change file
and a tool; read only inside a longer name; unread; read by a built name and listed; and stale list entries."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_unread_params as C  # noqa: E402

PARAMS = "params:\n  tax_year: 2025\n  values:\n" + "".join(
    f"    {k}:\n      type: Count\n      value: 1\n"
    for k in ("a.form", "a.change", "a.tool", "a.inside", "a.unread", "b.amount0", "b.amount1"))
NY = "params:\n  values:\n    ny.read:\n      type: Count\n      value: 1\n    ny.unread:\n      type: Count\n      value: 1\n"


class Tree(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.root = Path(self.dir.name)
        self.write("params/2025.yaml", PARAMS)
        self.write("params/ny/2025.yaml", NY)
        self.write("forms/2025/a.yaml", "lines:\n  - expr: {op: param, ref: a.form}\n    x: a.inside_more x.a.inside\n")
        self.write("forms/ny/2025/n.yaml", "lines:\n  - expr: {param: ny.read}\n")
        self.write("changes/2026/a.yaml", "ops:\n  - to: '{param: a.change}'\n")
        self.write("tools/t.py", 'P("a.tool")\nfor k in range(2): P(f"b.amount{k}")\n')
        self.write("tools/node_modules/m/x.js", '"a.unread"\n')
        self.allow({})

    def tearDown(self):
        self.dir.cleanup()

    def write(self, rel, text):
        (self.root / rel).parent.mkdir(parents=True, exist_ok=True)
        (self.root / rel).write_text(text, encoding="utf-8")

    def allow(self, entries):
        self.write("tools/unread_params_allow.json", json.dumps({"allow": entries}))

    def problems(self):
        return sorted(p.split(":")[0].split(" ")[0] for p in C.check(self.root, 2025)[0])

    def test_unread_and_built(self):
        self.assertEqual(self.problems(), ["a.inside", "a.unread", "b.amount0", "b.amount1", "ny.unread"])

    def test_listed_built_names(self):
        entry = {"built": "b.amount", "in": ["tools/t.py"], "reason": "r"}
        self.allow({"b.amount0": entry, "b.amount1": entry})
        self.assertEqual(self.problems(), ["a.inside", "a.unread", "ny.unread"])

    def test_stale_entries(self):
        self.allow({"a.tool": {"built": "a.", "in": ["tools/t.py"], "reason": "r"},
                    "gone.key": {"built": "gone.", "in": ["tools/t.py"], "reason": "r"},
                    "b.amount0": {"built": "b.amount", "in": ["forms/2025/a.yaml"], "reason": "r"},
                    "b.amount1": {"built": "b.amount", "in": ["tools/t.py"]}})
        found = C.check(self.root, 2025)[0]
        for key, words in (("a.tool", "read by name"), ("gone.key", "not a parameter"),
                           ("b.amount0", "builds no name"), ("b.amount1", "needs `built`")):
            self.assertTrue(any(p.startswith(key + ":") and words in p for p in found), (key, found))

    def test_the_list_is_not_a_reader(self):
        self.allow({"b.amount0": {"built": "b.amount", "in": ["tools/t.py"], "reason": "a.unread is mentioned here"}})
        self.assertIn("a.unread", self.problems())


def main():
    result = unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__]))
    ok = result.wasSuccessful()
    print(f"unread parameters self-test: {'ok' if ok else 'FAILED'} ({result.testsRun} tests)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
