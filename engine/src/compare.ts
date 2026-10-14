// Two-evaluator agreement: run every fixture case and a deterministic set of
// generated inputs through the TypeScript evaluator and the Lean reference
// evaluator, and fail on any difference (spec section 6.3 / design 2.6).

import { existsSync, mkdtempSync, readFileSync, rmSync, writeFileSync, mkdirSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { loadCanonical } from "./canonical.js";
import { evaluate } from "./eval.js";
import type { Value } from "./eval.js";

const ROOT = resolve(import.meta.dirname, "../..");
const LEAN_BIN = join(ROOT, "lean", ".lake", "build", "bin", "taxeval");
const CANON = join(ROOT, "canonical", "2025");
const FIXTURES = join(ROOT, "fixtures", "2025", "stage1.json");

interface Case {
  id: string;
  inputs: Record<string, number | boolean | string>;
}

function fixtureCases(): Case[] {
  const file = JSON.parse(readFileSync(FIXTURES, "utf-8")) as { cases: Case[] };
  return file.cases.map((c) => ({ id: c.id, inputs: c.inputs }));
}

function generatedCases(n: number): Case[] {
  let s = 20261014;
  const rnd = () => {
    s = (s * 1103515245 + 12345) % 2147483648;
    return s / 2147483648;
  };
  const statuses = ["single", "mfj", "mfs", "hoh", "qss"];
  const cases: Case[] = [];
  for (let i = 0; i < n; i++) {
    const status = statuses[Math.floor(rnd() * statuses.length)]!;
    const line15 = Math.floor(rnd() * 120000000); // up to $1.2M
    const line3a = rnd() < 0.6 ? Math.floor(rnd() * line15) : 0;
    const line7a = rnd() < 0.3 ? Math.floor(rnd() * 3000000) : 0;
    const sdFiled = rnd() < 0.25;
    const inputs: Record<string, number | boolean | string> = {
      "f1040.status": status,
      "f1040.line15": line15,
      "f1040.line3a": line3a,
      "f1040.line7a": line7a,
    };
    if (line3a > 0 || line7a > 0 || sdFiled) {
      inputs["qdcg.schedule_d_filed"] = sdFiled;
      if (sdFiled) inputs["qdcg.schedule_d_net_gain"] = Math.floor(rnd() * 5000000);
    }
    cases.push({ id: `generated.${String(i).padStart(3, "0")}`, inputs });
  }
  return cases;
}

function normalize(v: Value | Record<string, unknown>): string {
  const val = v as { kind?: string; cents?: number; value?: unknown };
  if (val.kind === "unknown") return "unknown";
  if (val.kind === "money") return `money:${val.cents}`;
  return `${val.kind}:${JSON.stringify(val.value)}`;
}

export function compareEvaluators(): number {
  if (!existsSync(LEAN_BIN)) {
    console.error(`lean binary not found at ${LEAN_BIN}; run: cd lean && lake build`);
    return 2;
  }
  const data = loadCanonical();
  const targets = data.forms.flatMap((doc) => doc.lines.map((l) => l.id));
  const cases = [...fixtureCases(), ...generatedCases(200)];
  const tmp = mkdtempSync(join(tmpdir(), "compare-"));
  let failures = 0;
  let comparedLines = 0;
  const failureDetails: string[] = [];

  try {
    for (const c of cases) {
      const inputsPath = join(tmp, `${c.id}.inputs.json`);
      const outPath = join(tmp, `${c.id}.lean.json`);
      writeFileSync(inputsPath, JSON.stringify(c.inputs));
      const proc = spawnSync(LEAN_BIN, ["--canonical", CANON, "--inputs", inputsPath, "--out", outPath], {
        encoding: "utf-8",
      });
      if (proc.status !== 0) {
        failures++;
        failureDetails.push(`${c.id}: lean evaluator exited ${proc.status}: ${proc.stderr.slice(0, 200)}`);
        continue;
      }
      const leanValues = JSON.parse(readFileSync(outPath, "utf-8")) as Record<string, Record<string, unknown>>;
      const ts = evaluate(data, c.inputs, targets);
      // Compare the authored target lines of f1040 and qdcg (the same set the
      // Lean evaluator emits); internal aliases for cross-form references are
      // not part of the compared surface.
      const tsValues: Record<string, Value> = {};
      for (const target of targets) {
        const der = ts.derivations.get(target);
        if (der) tsValues[target] = der.value;
      }
      const tsKeys = Object.keys(tsValues).sort();
      const leanKeys = Object.keys(leanValues).sort();
      const problems: string[] = [];
      if (JSON.stringify(tsKeys) !== JSON.stringify(leanKeys)) {
        const missingInLean = tsKeys.filter((k) => !leanKeys.includes(k));
        const missingInTs = leanKeys.filter((k) => !tsKeys.includes(k));
        problems.push(`key sets differ (missing in lean: ${missingInLean.join(",")}; missing in ts: ${missingInTs.join(",")})`);
      }
      for (const key of tsKeys) {
        if (!(key in leanValues)) continue;
        comparedLines++;
        const a = normalize(tsValues[key]!);
        const b = normalize(leanValues[key]!);
        if (a !== b) problems.push(`${key}: ts=${a} lean=${b}`);
      }
      if (problems.length > 0) {
        failures++;
        failureDetails.push(`${c.id}: ${problems.slice(0, 4).join("; ")}${problems.length > 4 ? ` … +${problems.length - 4}` : ""}`);
      }
    }
  } finally {
    rmSync(tmp, { recursive: true, force: true });
  }

  const report: string[] = [];
  report.push("# Evaluator agreement — TypeScript engine vs Lean reference");
  report.push("");
  report.push("Every fixture case and a deterministic set of 200 generated inputs were evaluated");
  report.push("by both independently written evaluators; every line of f1040 and qdcg was compared");
  report.push("(money cents, booleans, enums; unknowns compared by kind).");
  report.push("");
  report.push("| Metric | Value |");
  report.push("| --- | --- |");
  report.push(`| Cases | ${cases.length} |`);
  report.push(`| Line values compared | ${comparedLines} |`);
  report.push(`| Cases with differences | ${failures} |`);
  report.push(`| Result | ${failures === 0 ? "**agreement on every value**" : "**DIFFERENCES FOUND**"} |`);
  if (failures > 0) {
    report.push("");
    report.push("Differences:");
    for (const d of failureDetails.slice(0, 50)) report.push(`- ${d}`);
  }
  report.push("");
  const outDir = join(ROOT, "reports", "2025");
  mkdirSync(outDir, { recursive: true });
  writeFileSync(join(outDir, "evaluator_agreement.md"), report.join("\n"));
  console.log(`compare: ${cases.length} cases, ${comparedLines} line values, ${failures} differing case(s)`);
  console.log(`report: reports/2025/evaluator_agreement.md`);
  return failures === 0 ? 0 : 1;
}
