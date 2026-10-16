// Stage 5 differential: independent-calculator records (class C) for the whole-return
// cases, plus the entry sheets used to produce them outside the repository.
//
// The calculators run outside the repository; a person enters each case and records
// the lines below. Recorded values are compared with the computed values here; an
// unexplained difference fails the run. A difference with a cited cause goes in the
// record's `investigations` map, never silently.
import { readFileSync, writeFileSync, readdirSync, existsSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { loadCanonical } from "./canonical.js";
import { evaluate } from "./eval.js";
import type { Inputs } from "./types.js";
import type { Value } from "./eval.js";

const ROOT = join(import.meta.dirname, "../..");
const DIR = join(ROOT, "fixtures", "2025", "differential");

interface DifferentialRecord {
  calculator: string;
  version: string;
  case: string;
  values: Record<string, number>;
  investigations?: Record<string, string>;
}

interface CaseFixture { id: string; inputs: Inputs; expect?: Record<string, Value> }

const FIELD_LABELS: [RegExp, (m: RegExpMatchArray) => string][] = [
  [/^f1040\.status$/, () => "Filing status"],
  [/^person\[taxpayer\]\.w2\[(.+)\]\.box1$/, (m) => `W-2 (${m[1]}) box 1 — wages, tips, other compensation`],
  [/^person\[taxpayer\]\.w2\[(.+)\]\.box2$/, (m) => `W-2 (${m[1]}) box 2 — federal income tax withheld`],
  [/^person\[taxpayer\]\.w2\[(.+)\]\.box3$/, (m) => `W-2 (${m[1]}) box 3 — social security wages`],
  [/^person\[taxpayer\]\.w2\[(.+)\]\.box4$/, (m) => `W-2 (${m[1]}) box 4 — social security tax withheld`],
  [/^person\[taxpayer\]\.w2\[(.+)\]\.box5$/, (m) => `W-2 (${m[1]}) box 5 — Medicare wages and tips`],
  [/^person\[taxpayer\]\.w2\[(.+)\]\.box6$/, (m) => `W-2 (${m[1]}) box 6 — Medicare tax withheld`],
  [/^person\[taxpayer\]\.w2\[(.+)\]\.box7$/, (m) => `W-2 (${m[1]}) box 7 — social security tips`],
  [/^interest\[(.+)\]\.amount$/, (m) => `1099-INT (${m[1]}) box 1 — taxable interest`],
  [/^sb\.ordinary_dividends$/, () => "1099-DIV box 1a — total ordinary dividends"],
  [/^f1040\.line3a$/, () => "1099-DIV box 1b — qualified dividends"],
  [/^sd\.distributions$/, () => "1099-DIV box 2a — total capital gain distributions"],
  [/^qbi\.dividends$/, () => "1099-DIV box 5 — section 199A dividends"],
  [/^ftc\.taxes$/, () => "1099-DIV box 7 — foreign tax paid"],
  [/^f4952\.line1$/, () => "Investment interest expense paid (Form 4952 line 1)"],
  [/^sa\.line1$/, () => "Medical and dental expenses paid"],
  [/^sa\.line5a$/, () => "State and local income taxes paid"],
  [/^sa\.line8a$/, () => "Home mortgage interest from Form 1098"],
  [/^sa\.line11$/, () => "Gifts to charity by cash or check"],
  [/^gift\[(.+)\]\.deduction$/, (m) => `Noncash gift (${m[1]}) — fair market value`],
  [/^sales\[(.+)\]\.proceeds$/, (m) => `Sale (${m[1]}) — proceeds (Form 1099-B)`, ],
  [/^sales\[(.+)\]\.reported_basis$/, (m) => `Sale (${m[1]}) — cost or other basis`],
  [/^sales\[(.+)\]\.box$/, (m) => `Sale (${m[1]}) — Form 8949 box (A–F)`],
  [/^sales\[(.+)\]\.route$/, (m) => `Sale (${m[1]}) — routed detail or aggregate`],
  [/^sales\[(.+)\]\.code$/, (m) => `Sale (${m[1]}) — adjustment code`],
  [/^f1040\.line26$/, () => "Estimated tax payments"],
  [/^f1040\.line35a$/, () => "Refund amount you want refunded (whole overpayment if equal to line 34)"],
];

function dollars(cents: number): string { return (cents / 100).toFixed(2); }

function entrySheet(data: ReturnType<typeof loadCanonical>, c: CaseFixture, expect: Record<string, Value>): string {
  const out: string[] = [];
  out.push(`# Calculator entry sheet — ${c.id}`, "");
  out.push("Enter this case in FreeTaxUSA (2025) and OLT (2025), then read the lines below back into a record. Synthetic data only.", "");
  out.push("## Enter", "", "| field | value |", "| --- | --- |");
  for (const [key, value] of Object.entries(c.inputs)) {
    if (key.startsWith("$") || key === "f1040.status") continue;
    if (typeof value === "boolean" && value === false) continue;
    if (value === 0 || (Array.isArray(value) && value.length === 0)) continue;
    for (const [re, fmt] of FIELD_LABELS) {
      const m = key.match(re);
      if (m) { out.push(`| ${fmt(m)} | ${typeof value === "number" ? dollars(value) : String(value)} |`); break; }
    }
  }
  const zeroBool = (cond: boolean) => cond;
  out.push("", "Screening questions (answer No unless noted): Schedule 1 income, Schedule 1-A deductions, dependent/other credits, other income treatment, Form 1040 line 16 additional taxes, AMT, digital assets, foreign accounts.", "");
  out.push("| field | value |", "| --- | --- |");
  const boolRows: [string, unknown][] = [
    ["div.basis_reconciled", c.inputs["div.basis_reconciled"]],
    ["ftc.all_passive", c.inputs["ftc.all_passive"]],
    ["ftc.statements", c.inputs["ftc.statements"]],
    ["ftc.eligible", c.inputs["ftc.eligible"]],
    ["ftc.elect", c.inputs["ftc.elect"]],
  ];
  for (const [k, v] of boolRows) if (v === true) out.push(`| ${k} | yes |`);
  out.push("", "## Read back (record each line the calculators show)", "", "| line | description |", "| --- | --- |");
  const byId = new Map(data.forms.flatMap((d) => d.lines.map((l) => [l.id, l])));
  for (const key of Object.keys(expect)) {
    const line = byId.get(key);
    out.push(`| ${key} | ${line?.label ?? ""} |`);
  }
  out.push("", "## Record format", "", "Save as `fixtures/2025/differential/<calculator>." + c.id + ".json`:", "", "```json",
    JSON.stringify({ calculator: "FreeTaxUSA", version: "2025, accessed YYYY-MM-DD", case: c.id, values: { "f1040.line15": 0 }, investigations: {} }, null, 2), "```", "");
  out.push("Only include lines the calculator actually shows; absent lines are simply not compared. Any difference from the computed value needs a cited cause in `investigations`.", "");
  return out.join("\n");
}

export function differential(): number {
  const data = loadCanonical();
  const cases = (JSON.parse(readFileSync(join(ROOT, "fixtures", "2025", "stage5.json"), "utf8")) as { cases: CaseFixture[] }).cases;
  mkdirSync(join(ROOT, "reports", "2025"), { recursive: true });
  const returnCases = cases.filter((c) => c.id.startsWith("stage5.return."));
  for (const c of returnCases) {
    writeFileSync(join(ROOT, "reports", "2025", `differential.${c.id}.md`), entrySheet(data, c, c.expect ?? {}));
  }
  console.log(`differential: entry sheets written for ${returnCases.length} whole-return cases (reports/2025/differential.<case>.md)`);
  if (!existsSync(DIR)) { console.log("differential: no calculator records yet; comparison pending."); return 0; }
  const files = readdirSync(DIR).filter((f) => f.endsWith(".json")).sort();
  if (files.length === 0) { console.log("differential: no calculator records yet; comparison pending."); return 0; }
  const lines: string[] = [];
  lines.push("# Differential comparison — recorded independent calculators", "");
  lines.push("Class C evidence: whole-return cases compared against named, versioned calculators run outside the repository. Only lines present in a record are compared. An unexplained difference fails the build; an investigated difference carries its cited cause.", "");
  let mismatches = 0;
  for (const f of files) {
    const rec = JSON.parse(readFileSync(join(DIR, f), "utf8")) as DifferentialRecord;
    const c = cases.find((x) => x.id === rec.case);
    if (!c) { lines.push(`## ${f}`, "", `Unknown case \`${rec.case}\` — not in stage5.json.`, ""); mismatches++; continue; }
    const result = evaluate(data, c.inputs, Object.keys(rec.values));
    lines.push(`## ${rec.calculator} — ${rec.case}`, "");
    lines.push(`Recorded version: ${rec.version}. Lines compared: ${Object.keys(rec.values).length}.`, "");
    lines.push("| line | computed | recorded | result |", "| --- | --- | --- | --- |");
    for (const [key, cents] of Object.entries(rec.values)) {
      const v = result.derivations.get(key)?.value;
      const computed = v && v.kind === "money" ? v.cents : null;
      const match = computed === cents;
      const inv = rec.investigations?.[key];
      if (!match && !inv) mismatches++;
      const res = match ? "match" : inv ? `explained: ${inv}` : "**MISMATCH**";
      lines.push(`| ${key} | ${computed === null ? "?" : dollars(computed)} | ${dollars(cents)} | ${res} |`);
    }
    lines.push("");
  }
  writeFileSync(join(ROOT, "reports", "2025", "differential.md"), lines.join("\n"));
  if (mismatches > 0) { console.log(`differential: ${mismatches} unexplained difference(s) — reports/2025/differential.md`); return mismatches; }
  console.log("differential: all recorded calculator values agree; report: reports/2025/differential.md");
  return 0;
}

export function differentialClassC(): Map<string, Set<string>> {
  const coverage = new Map<string, Set<string>>();
  if (!existsSync(DIR)) return coverage;
  for (const f of readdirSync(DIR).filter((x) => x.endsWith(".json"))) {
    const rec = JSON.parse(readFileSync(join(DIR, f), "utf8")) as DifferentialRecord;
    for (const key of Object.keys(rec.values)) {
      const set = coverage.get(key) ?? new Set<string>();
      set.add(`${rec.calculator} ${rec.case}`);
      coverage.set(key, set);
    }
  }
  return coverage;
}
