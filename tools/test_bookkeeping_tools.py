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
