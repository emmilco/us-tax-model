#!/usr/bin/env python3
"""Render the roadmap page, reports/roadmap.html, from the coverage estimate.

The ladder is the greedy order in reports/2025/filer_coverage.json (spec 2.4);
the open tasks are the rows of TASKS.md whose status is "open". Run after
tools/coverage/estimate.py, or whenever a stage completes or TASKS.md changes.

    python3 tools/coverage/roadmap.py
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ESTIMATE = ROOT / "reports" / "2025" / "filer_coverage.json"
TASKS = ROOT / "TASKS.md"
OUT = ROOT / "reports" / "roadmap.html"

# Build stages completed, in order: (stage, title, what it covers).
DONE = [
    ("Stage 0", "Ground the premises", "Every premise checked in writing; IRS sources archived"),
    ("Stage 1", "Tax on ordinary income", "Tax Table, Tax Computation and Qualified Dividends worksheets; the Lean reference evaluator"),
    ("Stage 2", "Excess Social Security", "Per-person collections across employers"),
    ("Stage 3", "Investment sales", "Form 8949 and Schedule D"),
    ("Stage 4", "The remaining forms", "Schedules A and B, Forms 4952, 8283, 8959, 8960, 8995, the simple foreign tax credit"),
    ("Stage 5", "Whole return", "Wiring, the full interview and the evidence reports"),
    ("Stage 7", "Integrity stack", "Independent reviews, the bug inventory, engine comparison, the commit guard"),
    ("Stage 8", "Dependents", "Qualifying child and relative, head of household, the child tax credit"),
    ("Stage 9", "Earned income credit", "EIC worksheets and table"),
    ("Stage 10", "Retirement income", "Form 1099-R and Social Security benefits"),
    ("Stage 11", "Unemployment and Schedule 1", "Educator expenses, HSA, student loan interest"),
    ("Stage 12", "Schedule 1-A deductions", "Tips, overtime, car loan interest, the enhanced deduction for seniors"),
]
WAITING = [("Stage 6", "Tax year 2026", "Refetch, year diff, rerun every check; waits on the IRS final 2026 documents (T-011)")]
FIRST_LADDER_STAGE = 13
SHORT = {
    "schedule1a": "Schedule 1-A deductions", "married": "Married filers", "self_employment": "Self-employment",
    "other_credits": "Other credits", "schedule1_misc": "Other Schedule 1 items", "schedule_e": "Schedule E and K-1s",
    "premium_tax_credit": "Premium tax credit", "education": "Education credits",
    "capital_loss_carryover": "Capital loss carryover", "retirement_penalty": "Form 5329 additional tax",
    "farm": "Farm income", "other_earned_income": "Wages not on Form W-2", "schedule2_misc": "AMT and other Schedule 2",
}


def open_tasks():
    rows = []
    for line in TASKS.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.split("|")]
        if len(cells) > 5 and cells[1].startswith("T-") and cells[5].startswith("open"):
            first = cells[2].split(". ")[0].split(": ")[0]
            rows.append((cells[1], first[:160] + ("…" if len(first) > 160 else ""), cells[4]))
    return rows


def ladder_svg(cov, steps):
    W, left, right, row, top = 980, 290, 60, 30, 46
    plot = W - left - right
    x = lambda share: left + plot * share
    H = top + row * (len(steps) + 1) + 34
    parts = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Coverage after each stage">']
    for tick in range(0, 101, 20):
        parts.append(f'<line class="grid" x1="{x(tick/100):.1f}" x2="{x(tick/100):.1f}" y1="{top-6}" y2="{H-30}"/>'
                     f'<text class="tick" x="{x(tick/100):.1f}" y="{H-12}" text-anchor="middle">{tick}%</text>')
    band = f'<rect class="band" x="{x(.90):.1f}" y="{top-6}" width="{x(.95)-x(.90):.1f}" height="{H-30-top+6}"/>'
    parts.append(band)
    parts.append(f'<line class="ref" x1="{x(.80):.1f}" x2="{x(.80):.1f}" y1="{top-14}" y2="{H-30}"/>'
                 f'<text class="reflabel" x="{x(.80):.1f}" y="{top-18}" text-anchor="middle">80% baseline</text>'
                 f'<text class="reflabel" x="{x(.925):.1f}" y="{top-32}" text-anchor="middle">90–95% goal</text>')
    rows = [("Today", "Coverage now", None, cov["central"], "now")] + [
        (f"Stage {FIRST_LADDER_STAGE + i}", SHORT.get(s["group"], s["label"]), prev, s["coverage_after"], "next" if i == 0 else "later")
        for i, (s, prev) in enumerate(zip(steps, [cov["central"]] + [s["coverage_after"] for s in steps]))]
    for i, (stage, label, before, after, status) in enumerate(rows):
        y = top + i * row
        mark = {"now": "", "next": "▶ ", "later": ""}[status]
        full = label if status == "now" else steps[i - 1]["label"]
        tip = html.escape(f"{stage}: {full}. Coverage after: {after*100:.1f}%" + ("" if before is None else f" (+{(after-before)*100:.1f} points)"))
        parts.append(f'<g class="row {status}" tabindex="0" data-tip="{tip}">'
                     f'<rect class="hit" x="0" y="{y-2}" width="{W}" height="{row}"/>'
                     f'<text class="stage" x="8" y="{y+17}">{html.escape(stage)}</text>'
                     f'<text class="label" x="86" y="{y+17}">{mark}{html.escape(label)}</text>')
        base = after if before is None else before
        parts.append(f'<rect class="before" x="{left}" y="{y+4}" width="{max(x(base)-left-1, 0):.1f}" height="18" rx="0"/>')
        if before is not None:
            parts.append(f'<rect class="gain" x="{x(before)+1:.1f}" y="{y+4}" width="{max(x(after)-x(before)-1, 2):.1f}" height="18" rx="4"/>')
        parts.append(f'<text class="value" x="{x(after)+6:.1f}" y="{y+18}">{after*100:.0f}%</text></g>')
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    est = json.loads(ESTIMATE.read_text())
    cov, steps = est["coverage"], est["greedy_order"]
    baseline_step = next((i for i, s in enumerate(steps) if s["coverage_after"] >= 0.80), None)
    goal_step = next((i for i, s in enumerate(steps) if s["coverage_after"] >= 0.90), None)
    stage_no = lambda i: f"Stage {FIRST_LADDER_STAGE + i}" if i is not None else "beyond the ladder"
    card = lambda k, t, d, cls, badge: (f'<div class="step {cls}" tabindex="0"><div class="k"><span>{k}</span><span class="badge">{badge}</span></div>'
                                        f'<div class="t">{html.escape(t)}</div><div class="d">{html.escape(d)}</div></div>')
    done = "".join(card(k, t, d, "done", "✓ Done") for k, t, d in DONE)
    waiting = "".join(card(k, t, d, "wait", "⏸ Waiting") for k, t, d in WAITING)
    tasks = "".join(f"<tr><td>{html.escape(i)}</td><td>{html.escape(d)}</td><td>{html.escape(g)}</td></tr>" for i, d, g in open_tasks())
    unmeasured = len(est["gates_unmeasured"])
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Tax formalization: roadmap</title>
<style>
:root{{--surface:#fcfcfb;--card:#fff;--line:#e4e3df;--ink:#0b0b0b;--ink2:#52514e;--muted:#8a8984;
--before:#9ec5f4;--gain:#2a78d6;--done:#0ca30c;--next:#fab219;--wait:#ec835a;--band:rgba(12,163,12,.08);--ref:#52514e}}
@media (prefers-color-scheme:dark){{:root{{--surface:#1a1a19;--card:#222220;--line:#383835;--ink:#f0efec;--ink2:#c3c2b7;--muted:#8f8e88;
--before:#184f95;--gain:#3987e5;--band:rgba(12,163,12,.14);--ref:#c3c2b7}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--surface);color:var(--ink);font:15px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}}
main{{max-width:1040px;margin:0 auto;padding:32px 24px 64px}}h1{{font-size:24px;margin:0 0 4px}}h2{{font-size:17px;margin:40px 0 4px}}
.sub{{color:var(--ink2);margin:0 0 4px}}.note{{color:var(--muted);font-size:13px;margin:0 0 14px}}code{{font-size:12px}}
.tiles{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:20px}}
.tile{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:14px 16px}}
.tile .num{{font-size:30px;font-weight:600}}.tile .num small{{font-size:15px;color:var(--ink2);font-weight:500}}.tile .lbl{{color:var(--ink2);font-size:13px}}
.legend{{display:flex;gap:18px;flex-wrap:wrap;font-size:13px;color:var(--ink2);margin:6px 0 8px}}.legend span{{display:inline-flex;align-items:center;gap:6px}}
.sw{{width:14px;height:10px;border-radius:2px;display:inline-block}}
svg text{{fill:var(--ink2);font-size:13px}}svg .stage{{fill:var(--muted);font-size:12px}}svg .label{{fill:var(--ink)}}svg .value{{fill:var(--ink);font-size:12px;font-variant-numeric:tabular-nums}}
svg .tick{{fill:var(--muted);font-size:11px}}svg .grid{{stroke:var(--line);stroke-width:1}}svg .band{{fill:var(--band)}}
svg .ref{{stroke:var(--ref);stroke-width:1.5;stroke-dasharray:4 3}}svg .reflabel{{fill:var(--ink2);font-size:11px}}
svg .before{{fill:var(--before)}}svg .gain{{fill:var(--gain)}}svg .hit{{fill:transparent}}
svg .row:hover .hit,svg .row:focus .hit{{fill:var(--line);opacity:.45}}svg .row{{outline:none}}
svg .next .label{{font-weight:600}}svg .now .before{{fill:var(--gain)}}
.track{{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:8px}}
.step{{position:relative;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 12px 10px 16px}}
.step::before{{content:"";position:absolute;left:0;top:0;bottom:0;width:5px;border-radius:8px 0 0 8px;background:var(--c)}}
.step.done{{--c:var(--done)}}.step.wait{{--c:var(--wait)}}
.step .k{{font-size:12px;color:var(--ink2);display:flex;justify-content:space-between}}.step .t{{font-weight:600;margin-top:2px}}.step .d{{font-size:13px;color:var(--ink2);margin-top:3px}}
.badge{{font-size:11px;font-weight:600}}
table{{border-collapse:collapse;width:100%;font-size:13px;background:var(--card);border:1px solid var(--line)}}
th,td{{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}}th{{color:var(--ink2)}}
#tip{{position:fixed;pointer-events:none;background:var(--ink);color:var(--surface);font-size:12px;padding:6px 9px;border-radius:6px;max-width:320px;opacity:0}}
@media (max-width:720px){{.tiles{{grid-template-columns:repeat(2,1fr)}}}}
</style></head><body><main>
<h1>Tax formalization: roadmap</h1>
<p class="sub">A verified, cited federal return built from the IRS's own instructions. The goal (spec 2.4) is coverage of all individual returns: 80% as the baseline, then on toward 90–95%, short of the genuinely exotic.</p>
<p class="note">Generated by <code>tools/coverage/roadmap.py</code> from <code>reports/2025/filer_coverage.json</code> and <code>TASKS.md</code>. A return counts as covered only when nothing on it is refused.</p>
<div class="tiles">
<div class="tile"><div class="num">{cov['central']*100:.0f}%</div><div class="lbl">of returns covered today (estimate; range {cov['low']*100:.0f}–{cov['high']*100:.0f}%)</div></div>
<div class="tile"><div class="num">80% <small>at {stage_no(baseline_step)}</small></div><div class="lbl">baseline, {baseline_step + 1 if baseline_step is not None else '?'} stages from now</div></div>
<div class="tile"><div class="num">90% <small>at {stage_no(goal_step)}</small></div><div class="lbl">start of the 90–95% goal</div></div>
<div class="tile"><div class="num">{len(DONE)}</div><div class="lbl">build stages done; Stage 6 (tax year 2026) waits on the IRS</div></div>
</div>

<h2>The ladder: coverage after each stage</h2>
<p class="note">Each stage is the group of refused situations that gains the most coverage once the stages above it are done.</p>
<div class="legend"><span><i class="sw" style="background:var(--before)"></i>Covered before the stage</span><span><i class="sw" style="background:var(--gain)"></i>Gained by the stage</span><span>▶ Next stage</span><span><i class="sw" style="background:var(--band);border:1px solid var(--line)"></i>90–95% goal</span></div>
{ladder_svg(cov, steps)}
<p class="note">Limits: IRS counts are for tax year 2023. {unmeasured} refusal gates are not yet measured, so 100% here means 100% of the measured situations. Details: <code>reports/2025/filer_coverage.md</code>, task T-034.</p>

<h2>Done</h2>
<div class="track">{done}{waiting}</div>

<h2>Open tasks</h2>
<table><thead><tr><th>Task</th><th>What it is</th><th>Waiting for</th></tr></thead><tbody>{tasks}</tbody></table>
</main><div id="tip" role="tooltip"></div>
<script>
const tip=document.getElementById("tip");
document.addEventListener("mousemove",e=>{{const t=e.target.closest("[data-tip]");if(!t){{tip.style.opacity=0;return}}
tip.textContent=t.dataset.tip;tip.style.opacity=1;tip.style.left=Math.min(e.clientX+14,innerWidth-tip.offsetWidth-8)+"px";tip.style.top=(e.clientY+16)+"px"}});
document.addEventListener("focusin",e=>{{const t=e.target.closest("[data-tip]");if(t){{const r=t.getBoundingClientRect();tip.textContent=t.dataset.tip;tip.style.opacity=1;tip.style.left=r.left+300+"px";tip.style.top=r.bottom+"px"}}}});
document.addEventListener("focusout",()=>tip.style.opacity=0);
</script></body></html>
"""
    OUT.write_text(page, encoding="utf-8")
    print(f"roadmap: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
