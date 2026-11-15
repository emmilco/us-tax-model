"""Lane 8b scratch, applied once after f5695_model.py: lines 6b and 11 are read only when something was installed in
2025, so that a filer whose only Part I amount is the 2024 carryforward is not asked about business use, a home under
construction or a fuel cell (the three refusals of lines 6a and 11 concern 2025 costs).
Run from the worktree root: python3 docs/provisional/lanes/l8b_work/f5695_model2.py"""
from pathlib import Path
P = Path('forms/2025/f5695.yaml'); t = P.read_text()
assert 'f5695.line6b_if_any' not in t, 'already applied'
old = "      op: sum\n      of:\n      - f5695.line6b\n      - f5695.line11\n      - f5695.line12_if_carry\n"
assert t.count(old) == 1
t = t.replace(old, "      op: sum\n      of:\n      - f5695.line6b_if_any\n      - f5695.line11_if_any\n      - f5695.line12_if_carry\n")
def gate(i, of, what):
    return f"""  - id: {i}
    printed: (gate)
    label: "{what}, read only when something was installed in 2025 (zero otherwise)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
      - guard:
          op: test
          eq:
          - f5695.any
          - const: true
        then: {of}
      - guard:
          op: test
          eq:
          - f5695.any
          - const: false
        then: f5695.zero
    cite:
      doc: f5695
      locator: Form 5695 (2025), line 13, "Add lines 6b, 11, and 12"

"""
a = t.index("  - id: f5695.line13\n")
t = t[:a] + gate('f5695.line6b_if_any', 'f5695.line6b', 'Line 6b') + gate('f5695.line11_if_any', 'f5695.line11', 'Line 11') + t[a:]
P.write_text(t)
