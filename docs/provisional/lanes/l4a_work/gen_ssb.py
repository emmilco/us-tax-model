#!/usr/bin/env python3
"""Lane 4a: rewrite forms/2025/ssb.yaml. ssb.benefits sits beneath ssb.any; ssb.pub915 becomes a derived line over
two questions (the other four items of the old question are asked elsewhere); the lump-sum election is asked only
after ssb.prior_year_pay (the input is ssb.lump_elect, and ssb.lump_sum stays as its gate line so the refusal's
gate id is unchanged). Run once from the worktree root."""
import re, sys
PATH = "forms/2025/ssb.yaml"
s = open(PATH).read()
if "ssb.any" in s:
    sys.exit("already applied")
C31 = "    cite:\n      doc: i1040gi\n      locator: p. 31, Lines 6a and 6b, Exception\n"
C6C = "    cite:\n      doc: i1040gi\n      locator: p. 31, Line 6c; p. 32, Social Security Benefits Worksheet, TIP\n"
C1 = "    cite:\n      doc: i1040gi\n      locator: p. 32, Social Security Benefits Worksheet, line 1; p. 31, Lines 6a and 6b\n"
def q(t): return "'" + t.replace("'", "''") + "'"
def inp(id, text, cite, gated_by=None):
    return (f"  - id: ssb.{id}\n    printed: (helper)\n    label: {q(text)}\n    type: Bool\n" + (f"    gated_by: ssb.{gated_by}\n" if gated_by else "")
            + f"    expr:\n      op: input\n      source: {q(text)}\n" + cite)
def choose(id, label, typ, guard, then, other, cite, printed="(gate)"):
    return (f"  - id: ssb.{id}\n    printed: {printed}\n    label: {q(label)}\n    type: {typ}\n    expr:\n      op: choose\n      alternatives:\n"
            f"      - guard:\n          op: test\n          eq:\n          - ssb.{guard}\n          - const: true\n        then: ssb.{then}\n"
            f"      - guard:\n          op: test\n          eq:\n          - ssb.{guard}\n          - const: false\n        then: ssb.{other}\n" + cite)
ANY = "Did you (or, on a joint return, your spouse) get social security benefits, or railroad retirement benefits treated as social security, in 2025? Form SSA-1099 or Form RRB-1099 reports them."
IRA = "Did you (or, on a joint return, your spouse) put money into a traditional IRA for 2025 while covered by a retirement plan at work or through self-employment?"
REPAID = "On any of your (or, on a joint return, your spouse's) Forms SSA-1099 or RRB-1099, is box 4 (benefits repaid) more than box 3 (benefits paid)?"
PRIOR = "Did the 2025 benefits paid to you (or, on a joint return, your spouse) include a payment for an earlier year? The Form SSA-1099 says so in its description of the amount in box 3."
ELECT = "Do you want to figure the tax on that earlier year's payment with the lump-sum election method?"
head = (inp("any", ANY, C1)
        + "  - id: ssb.no\n    printed: (helper)\n    label: Year parameter s3.no (false)\n    type: Bool\n    expr:\n      op: param\n      ref: s3.no\n" + C1)
# benefits beneath ssb.any
s = s.replace("  - id: ssb.benefits\n    printed: (helper)\n", head + "  - id: ssb.benefits\n    printed: (helper)\n    gated_by: ssb.benefits_if_any\n", 1)
m = re.search(r"  - id: ssb\.pub915\n.*?(?=  - id: ssb\.terror_disability\n)", s, re.S); assert m
new = (inp("ira_covered", IRA, C31) + inp("repaid_more", REPAID, C31)
       + f"  - id: ssb.pub915\n    printed: (helper)\n    label: {q('A situation in which the Social Security Benefits Worksheet of the Form 1040 instructions does not apply: a traditional IRA contribution for 2025 by a person covered by a retirement plan, or repayments (box 4) that are more than the benefits (box 3). The excluded income of Forms 2555 and 4563 and of Puerto Rico, the savings bond interest of Form 8815 and employer adoption benefits are asked about at their own questions.')}\n    type: Bool\n    expr:\n      op: test\n      any:\n      - op: test\n        eq:\n        - ssb.ira_covered\n        - const: true\n      - op: test\n        eq:\n        - ssb.repaid_more\n        - const: true\n" + C31
       + inp("prior_year_pay", PRIOR, C6C)
       + inp("lump_elect", ELECT, C6C, gated_by="lump_sum")
       + choose("lump_sum", "The lump-sum election method is chosen for a benefit payment that was for an earlier year (asked only when the benefits include such a payment; false otherwise)", "Bool", "prior_year_pay", "lump_elect", "no", C6C))
s = s[:m.start()] + new + s[m.end():]
old = "      op: copy\n      from: ssb.benefits\n"; assert old in s
s = s.replace(old, "      op: copy\n      from: ssb.benefits_if_any\n")
s = s.replace("  - id: ssb.line1\n", choose("benefits_if_any", "Net benefits, asked only of a filer who got social security or railroad retirement benefits (none otherwise)", "NonNegDollars", "any", "benefits", "zero", C1) + "  - id: ssb.line1\n", 1)
open(PATH, "w").write(s)
print("ok")
