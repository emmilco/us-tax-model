"""Offline tests of tools/new_bug.py and tools/task_row.py on temporary copies."""
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent


def run(script, *args, stdin=None):
    return subprocess.run([sys.executable, str(TOOLS / script), *map(str, args)],
                          capture_output=True, text=True, input=stdin)


class TempCase(unittest.TestCase):
    def setUp(self):
        self.dir = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.dir, True)


class NewBug(TempCase):
    def setUp(self):
        super().setUp()
        self.f = self.dir / "BUG_INVENTORY.md"
        shutil.copy(ROOT / "BUG_INVENTORY.md", self.f)
        self.before = self.f.read_bytes()
        self.n = len(re.findall(r"^## BUG-\d{4} ", self.before.decode(), re.M))

    def test_append_is_exact_and_prefix_identical(self):
        r = run("new_bug.py", "--file", self.f, "A title",
                "--field", "Caught by=a test", "--field", "Tags=tool change")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout.strip(), f"BUG-{self.n + 1:04d}")
        after = self.f.read_bytes()
        self.assertTrue(after.startswith(self.before))
        self.assertEqual(after[len(self.before):].decode(),
                         f"\n## BUG-{self.n + 1:04d} — A title\n\n- **Caught by:** a test\n- **Tags:** tool change\n")

    def test_ids_stay_gapless_and_increment(self):
        for k in range(3):
            r = run("new_bug.py", "--file", self.f, f"t{k}", "--field", "Symptom=s")
            self.assertEqual(r.stdout.strip(), f"BUG-{self.n + 1 + k:04d}")
        ids = [int(x) for x in re.findall(r"^## BUG-(\d{4}) ", self.f.read_text(), re.M)]
        self.assertEqual(ids, list(range(1, self.n + 4)))

    def test_body_from_stdin(self):
        r = run("new_bug.py", "--file", self.f, "Body", "--body-file", "-", stdin="- **Symptom:** x\n\n\n")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(self.f.read_text().endswith(f"## BUG-{self.n + 1:04d} — Body\n\n- **Symptom:** x\n"))

    def test_refusals_leave_file_untouched(self):
        cases = [
            ["  ", "--field", "A=b"],
            ["T"],
            ["T", "--field", "noequals"],
            ["T", "--field", "A="],
            ["T", "--field", "A=b", "--body-file", "-"],
            ["T", "--field", "A=line\nbreak"],
        ]
        for c in cases:
            r = run("new_bug.py", "--file", self.f, *c, stdin="")
            self.assertNotEqual(r.returncode, 0, c)
            self.assertEqual(self.f.read_bytes(), self.before, c)

    def test_refuses_gapped_file(self):
        self.f.write_text("# x\n\n## BUG-0001 — a\n\n## BUG-0003 — c\n")
        self.assertNotEqual(run("new_bug.py", "--file", self.f, "T", "--field", "A=b").returncode, 0)

    def test_check_bug_inventory_passes(self):
        # check_bug_inventory.py reads the repository file; apply its id rule to the copy.
        run("new_bug.py", "--file", self.f, "T", "--field", "A=b")
        ids = [int(x) for x in re.findall(r"^## BUG-(\d{4}) ", self.f.read_text(), re.M)]
        self.assertEqual(ids, list(range(1, len(ids) + 1)))


P = "BUG-" + "NEW-"  # built, so that this file cites no placeholder


class PendingBugs(TempCase):
    """--pending and --assign in a temporary repository: two lanes' entries assigned at a merge."""

    def setUp(self):
        super().setUp()
        self.f = self.dir / "BUG_INVENTORY.md"
        self.f.write_text("# Bug inventory\n\n---\n\n## BUG-0001 — one\n\n- **Symptom:** s\n")
        subprocess.run(["git", "init", "-q", "-b", "lane-x"], cwd=self.dir, check=True)

    def git_add(self):
        subprocess.run(["git", "add", "-A"], cwd=self.dir, check=True)

    def test_pending_names_and_assign(self):
        r = run("new_bug.py", "--file", self.f, "First", "--pending", "--field", "Symptom=see later")
        self.assertEqual((r.returncode, r.stdout.strip()), (0, P + "lane-x-01"), r.stderr)
        r = run("new_bug.py", "--file", self.f, "Second", "--pending", "--field", f"Symptom=after {P}lane-x-01")
        self.assertEqual(r.stdout.strip(), P + "lane-x-02")
        r = run("new_bug.py", "--file", self.f, "Other lane", "--pending", "b", "--field", "Symptom=s")
        self.assertEqual(r.stdout.strip(), P + "b-01")
        for k in range(3, 11):
            run("new_bug.py", "--file", self.f, f"n{k}", "--pending", "--field", "Symptom=s")
        self.assertEqual((self.dir / "bug_pending" / "lane-x-02.md").read_text(),
                         f"## {P}lane-x-02 — Second\n\n- **Symptom:** after {P}lane-x-01\n")
        (self.dir / "TASKS.md").write_text(f"| T-1 | fix {P}lane-x-10 and {P}b-01 |\n")
        self.git_add()
        before = self.f.read_text()
        r = run("new_bug.py", "--file", self.f, "--assign")
        self.assertEqual(r.returncode, 0, r.stderr)
        lines = r.stdout.split("\n")
        # Name order with numbers compared as numbers: b-01, lane-x-01 .. lane-x-10.
        self.assertEqual(lines[0], f"{P}b-01 -> BUG-0002")
        self.assertEqual(lines[10], f"{P}lane-x-10 -> BUG-0012")
        after = self.f.read_text()
        self.assertTrue(after.startswith(before))
        self.assertIn("## BUG-0004 — Second\n\n- **Symptom:** after BUG-0003\n", after)
        self.assertEqual(re.findall(r"^## BUG-(\d{4}) ", after, re.M), [f"{k:04d}" for k in range(1, 13)])
        self.assertEqual((self.dir / "TASKS.md").read_text(), "| T-1 | fix BUG-0012 and BUG-0002 |\n")
        self.assertEqual(list((self.dir / "bug_pending").glob("*.md")), [])

    def test_refusals(self):
        bad = self.dir / "bug_pending"
        bad.mkdir()
        (bad / "z-1.md").write_text("## BUG-0009 — numbered\n")
        before = self.f.read_bytes()
        r = run("new_bug.py", "--file", self.f, "--assign")
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(self.f.read_bytes(), before)
        self.assertNotEqual(run("new_bug.py", "--file", self.f, "T", "--pending", "Bad_Prefix",
                                "--field", "A=b").returncode, 0)
        self.assertNotEqual(run("new_bug.py", "--file", self.f, "T", "--assign").returncode, 0)


class PendingMergeFlow(TempCase):
    """Two lanes record pending entries; each is merged onto main with --assign, in either order, and
    check_bug_inventory.py (the working check and --merge, as pre-commit runs it) accepts every step."""

    def git(self, *args, check=True):
        return subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *args], cwd=self.dir,
                              capture_output=True, text=True, check=check)

    def tool(self, script, *args):
        return subprocess.run([sys.executable, f"tools/{script}", *args], cwd=self.dir, capture_output=True, text=True)

    def setUp(self):
        super().setUp()
        (self.dir / "tools").mkdir()
        for f in ("check_bug_inventory.py", "new_bug.py"):
            shutil.copy(TOOLS / f, self.dir / "tools" / f)
        (self.dir / "BUG_INVENTORY.md").write_text("# Bug inventory\n\n---\n\n## BUG-0001 — one\n\n- **S:** s\n")
        self.git("init", "-q", "-b", "main")
        self.git("add", "-A")
        self.git("commit", "-qm", "base")
        for lane in ("a", "b"):
            self.git("checkout", "-q", "-b", f"lane-{lane}", "main")
            self.tool("new_bug.py", f"from {lane}", "--pending", "--field", "S=s")
            self.tool("new_bug.py", f"second {lane}", "--pending", "--field", f"S=after {P}lane-{lane}-01")
            (self.dir / f"notes-{lane}.txt").write_text(f"see {P}lane-{lane}-02\n")
            self.git("add", "-A")
            r = self.tool("check_bug_inventory.py")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.git("commit", "-qm", f"lane {lane}")
        self.git("checkout", "-q", "main")

    def merge(self, lane, assign=True):
        self.git("merge", "-q", "--no-ff", "--no-commit", f"lane-{lane}")
        if assign:
            self.assertEqual(self.tool("new_bug.py", "--assign").returncode, 0)
        self.git("add", "-A")
        tree = self.git("write-tree").stdout.strip()
        return self.tool("check_bug_inventory.py", "--merge", tree, "HEAD", f"lane-{lane}")

    def test_either_order(self):
        results = {}
        for order in (("a", "b"), ("b", "a")):
            self.git("checkout", "-q", "-B", "trial", "main")
            for lane in order:
                r = self.merge(lane)
                self.assertEqual(r.returncode, 0, (order, r.stderr))
                self.git("commit", "-qm", f"merge {lane}")
                r = self.tool("check_bug_inventory.py")
                self.assertEqual(r.returncode, 0, (order, r.stderr))
            inv = (self.dir / "BUG_INVENTORY.md").read_text()
            self.assertEqual(re.findall(r"^## BUG-(\d{4}) ", inv, re.M), ["0001", "0002", "0003", "0004", "0005"])
            first, second = order
            self.assertIn(f"## BUG-0003 — second {first}\n\n- **S:** after BUG-0002\n", inv)
            self.assertIn(f"## BUG-0005 — second {second}\n\n- **S:** after BUG-0004\n", inv)
            self.assertEqual((self.dir / f"notes-{second}.txt").read_text(), "see BUG-0005\n")
            self.assertFalse((self.dir / "bug_pending").exists())
            results[order] = sorted(re.findall(r"^## BUG-\d{4} — (.*)$", inv, re.M))
        self.assertEqual(results[("a", "b")], results[("b", "a")])

    def test_merge_dropping_pending_is_refused(self):
        self.git("merge", "-q", "--no-ff", "--no-commit", "lane-a")
        r = self.git("rm", "-q", "-r", "-f", "bug_pending", check=False)
        self.assertEqual(r.returncode, 0, r.stderr)
        tree = self.git("write-tree").stdout.strip()
        r = self.tool("check_bug_inventory.py", "--merge", tree, "HEAD", "lane-a")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("not the parents' pending entries", r.stderr)

    def test_merge_without_assign_keeps_pending(self):
        self.assertEqual(self.merge("a", assign=False).returncode, 0)


HEADER = "# Tasks\n\n| Id | Task | Source | Due when | Status |\n| --- | --- | --- | --- | --- |\n"
DONE_HEADER = "# Tasks done\n\n| Id | Task | Source | Due when | Status |\n| --- | --- | --- | --- | --- |\n"


class TaskRow(TempCase):
    def setUp(self):
        super().setUp()
        self.t = self.dir / "TASKS.md"
        self.d = self.dir / "TASKS-DONE.md"
        self.t.write_text(HEADER + "| T-002 | Two | s | now | open |\n| T-005 | Five `a\\|b` | s | later | check |\n")
        self.d.write_text(DONE_HEADER + "| T-007 | Seven | s | x | done (abc) |\n")

    def test_add_uses_max_over_both_files_and_appends_exactly(self):
        before = self.t.read_text()
        r = run("task_row.py", "--file", self.t, "add", "--task", "New | task", "--source", "src", "--due", "any time")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout.strip(), "T-008")
        self.assertEqual(self.t.read_text(), before + "| T-008 | New \\| task | src | any time | open |\n")

    def test_status_updates_only_status_cell(self):
        r = run("task_row.py", "--file", self.t, "status", "T-005", "in progress")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.t.read_text(), HEADER + "| T-002 | Two | s | now | open |\n| T-005 | Five `a\\|b` | s | later | in progress |\n")

    def test_done_moves_row_with_text_unchanged(self):
        r = run("task_row.py", "--file", self.t, "done", "T-005", "done 2026-11-05 (abc1234)")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.t.read_text(), HEADER + "| T-002 | Two | s | now | open |\n")
        self.assertEqual(self.d.read_text(), DONE_HEADER + "| T-007 | Seven | s | x | done (abc) |\n"
                         "| T-005 | Five `a\\|b` | s | later | done 2026-11-05 (abc1234) |\n")
        r = run("task_row.py", "--file", self.t, "add", "--task", "n", "--source", "s", "--due", "d")
        self.assertEqual(r.stdout.strip(), "T-008")

    def test_refusals_leave_files_untouched(self):
        tb, db = self.t.read_bytes(), self.d.read_bytes()
        cases = [
            ["add", "--task", " ", "--source", "s", "--due", "d"],
            ["add", "--task", "a\nb", "--source", "s", "--due", "d"],
            ["status", "T-999", "open"],
            ["status", "T-002", " "],
            ["status", "bogus", "open"],
            ["done", "T-007", "done"],      # only in the done file
            ["done", "T-999", "done"],
        ]
        for c in cases:
            r = run("task_row.py", "--file", self.t, *c)
            self.assertNotEqual(r.returncode, 0, c)
            self.assertEqual((self.t.read_bytes(), self.d.read_bytes()), (tb, db), c)

    def test_done_refuses_id_collision_in_done_file(self):
        self.d.write_text(self.d.read_text() + "| T-005 | dup | s | x | done |\n")
        tb = self.t.read_bytes()
        r = run("task_row.py", "--file", self.t, "done", "T-005", "done")
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(self.t.read_bytes(), tb)

    def test_real_registers_parse(self):
        # Read-only: the next id on copies of the real registers exceeds every existing id.
        shutil.copy(ROOT / "TASKS.md", self.t)
        shutil.copy(ROOT / "TASKS-DONE.md", self.d)
        top = max(int(x) for p in (self.t, self.d) for x in re.findall(r"^\| T-(\d+) \|", p.read_text(), re.M))
        r = run("task_row.py", "--file", self.t, "add", "--task", "x", "--source", "s", "--due", "d")
        self.assertEqual(r.stdout.strip(), f"T-{top + 1:03d}")


if __name__ == "__main__":
    unittest.main()
