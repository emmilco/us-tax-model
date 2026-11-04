#!/usr/bin/env python3
"""Unit test for review_yield.py: class reading, tallies and the rendered tables on a synthetic tree."""
import json, os, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import review_yield as ry  # noqa: E402


def write(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(obj if isinstance(obj, str) else json.dumps(obj))


def main():
    assert ry.classify("Ruling: model error; the reply format") == "model error"
    assert ry.classify("Ruling: interface gap and model error — x") == "interface gap"
    assert ry.classify("Ruling: finding, recorded (BUG-1)") == "finding"
    assert ry.classify("Ruling: scope/representation on returns") == "scope"
    assert ry.classify("something else") == "other"

    with tempfile.TemporaryDirectory() as root:
        r = os.path.join(root, "reviews", "2025")
        write(os.path.join(r, "transcription", "a.rulings.json"), {"rulings": [{"ruling": "Ruling: model error; x"}, {"ruling": "Ruling: scope; y"}]})
        write(os.path.join(r, "transcription", "a.deepseek.rulings.json"), {"family": "deepseek", "rulings": [{"ruling": "Ruling: model error; x"}]})
        write(os.path.join(r, "completeness", "rulings.json"), {"rulings": {"u#1": {"class": "real gap"}, "u#2": {"class": "covered"}, "u#3": {"class": "out of scope"}}})
        write(os.path.join(r, "screens", "rulings.json"), {"rulings": {"s": {"findings": [{"class": "defect"}, {"class": "model error"}, {"class": "covered"}]}}})
        write(os.path.join(root, "BUG_INVENTORY.md"),
              "# x\n\n## BUG-0001 — a\n\n- **Caught by:** the render comparison\n\n## BUG-0002 — b\n\n- **Caught by:** the standing screen review\n")
        items = list(ry.ruling_items(root))
        assert sum(1 for i in items if i[0] == "transcription" and i[1] == "deepseek") == 1
        bugs = list(ry.bug_entries(root))
        assert [b[0] for b in bugs] == ["render", "screen"]
        ev = ry.evidence_table(items, bugs, False)
        assert ev[("completeness", "claude")]["classes"]["finding"] == 1
        assert ev[("completeness", "claude")]["classes"]["model error"] == 1
        assert ev[("screen", "claude")]["classes"]["finding"] == 1 and ev[("screen", "claude")]["bugs"] == 1
        ledger = [{"kind": "completeness", "model_requested": "claude-opus-5-5", "estimated_cost_usd": 2.0, "outcome": "ok", "timestamp": "2026-11-04T02:00:00+00:00"},
                  {"kind": "completeness", "model_requested": "claude-opus-5-5", "estimated_cost_usd": None, "outcome": "error: x", "timestamp": "2026-11-04T02:01:00+00:00"}]
        c = ry.cost_table(ledger)[("completeness", "claude")]
        assert c == {"calls": 2, "failed": 1, "usd": 2.0}
        runs = [{"date": "2026-11-03", "subagent_tokens": 10, "tool_uses": 2, "duration_ms": 60000},
                {"date": "2026-11-03", "subagent_tokens": 5, "tool_uses": 1, "duration_ms": 60000}]
        assert ry.agent_table(runs)["2026-11-03"] == {"runs": 2, "tokens": 15, "tool_uses": 3, "minutes": 2.0}
        text = ry.render(ledger, runs, items, bugs, None)
        assert "| completeness | claude | 2 | 1 | 2.00 | 0 |" in text
        assert "| 2026-11-03 | 2 | 15 | 3 | 2 |" in text
        assert "No stamped ruling" in text

        # Exact join: a stamped ruling meets the call that returned the reply it rules.
        run_a, run_b, run_old = "a" * 64, "b" * 64, "c" * 64
        write(os.path.join(r, "transcription", "b.deepseek.rulings.json"), {"family": "deepseek", "rulings": [
            {"ruling": "Ruling: model error; x", "run": run_a, "date": "2026-11-05"},
            {"ruling": "Ruling: finding; y", "run": run_a, "date": "2026-11-05", "severity": "high"},
            {"ruling": "Ruling: scope; z", "run": run_old, "date": "2026-11-05"},
            {"ruling": "Ruling: scope; unstamped"}]})
        ledger2 = ledger + [
            {"kind": "transcription", "model_requested": "deepseek-flash", "estimated_cost_usd": 0.5, "outcome": "ok", "response_sha256": run_a},
            {"kind": "transcription", "model_requested": "deepseek-flash", "estimated_cost_usd": 0.25, "outcome": "ok", "response_sha256": run_b}]
        stamped = list(ry.stamped_items(root))
        assert len(stamped) == 3, stamped
        g = ry.exact_table(ledger2, stamped)[("transcription", "deepseek")]
        assert (g["calls"], g["usd"], len(g["ruled_calls"]), g["rulings"], g["unjoined"]) == (2, 0.75, 1, 2, 1), g
        assert g["severity"] == {"high": 1} and g["classes"]["finding"] == 1
        text = ry.render(ledger2, runs, items, bugs, None, stamped)
        assert "| transcription | deepseek | 2 | 0.75 | 1 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | high 1 | 0.75 | 1 |" in text, text
    print("test_review_yield: ok")


if __name__ == "__main__":
    main()
