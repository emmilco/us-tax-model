// Fixtures: covering cases over the Stage 1 slice.
//
// `record-fixtures` fills each case's expected values from the evaluator (a
// convenience for recording; the values are then frozen in the file).
// `test-fixtures` runs every case THROUGH THE COMMAND-LINE PROGRAM and
// compares. `coverage` reports which case takes each choose-guard.

import { mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { loadCanonical } from "./canonical.js";
import { evaluate } from "./eval.js";
import type { Value } from "./eval.js";

const ROOT = resolve(import.meta.dirname, "../..");
const CASES_PATH = join(ROOT, "fixtures", "2025", "stage1.json");
const DIST_MAIN = join(ROOT, "engine", "dist", "main.js");

export interface FixtureCase {
  id: string;
  covers: string[];
  evidence: string;
  evidence_note?: string;
  inputs: Record<string, number | boolean | string>;
  expect?: Record<string, Value>;
}

export interface FixtureFile {
  tax_year: number;
  cases: FixtureCase[];
}

function loadCases(): FixtureFile {
  return JSON.parse(readFileSync(CASES_PATH, "utf-8")) as FixtureFile;
}

function saveCases(file: FixtureFile): void {
  writeFileSync(CASES_PATH, JSON.stringify(file, null, 2) + "\n");
}

const VALUE_KINDS = new Set(["money", "bool", "enum"]);

export function recordFixtures(): void {
  const data = loadCanonical();
  const file = loadCases();
  const targets = data.forms.flatMap((doc) => doc.lines.map((l) => l.id));
  for (const c of file.cases) {
    const result = evaluate(data, c.inputs, targets);
    const expect: Record<string, Value> = {};
    for (const [key, der] of [...result.derivations.entries()].sort((a, b) => (a[0] < b[0] ? -1 : 1))) {
      if (VALUE_KINDS.has(der.value.kind)) {
        expect[key] = der.value;
      }
    }
    // Keep only lines belonging to f1040 and qdcg (the Stage 1 slice facets).
    const filtered: Record<string, Value> = {};
    for (const [key, value] of Object.entries(expect)) {
      if (key.startsWith("f1040.") || key.startsWith("qdcg.")) filtered[key] = value;
    }
    c.expect = filtered;
  }
  saveCases(file);
  console.log(`recorded expected values for ${file.cases.length} cases in fixtures/2025/stage1.json`);
}

export function testFixtures(): number {
  const file = loadCases();
  const tmp = mkdtempSync(join(tmpdir(), "fixture-"));
  let failures = 0;
  let cases = 0;
  try {
    for (const c of file.cases) {
      cases++;
      const inputsPath = join(tmp, `${c.id}.json`);
      writeFileSync(inputsPath, JSON.stringify(c.inputs));
      const proc = spawnSync(process.execPath, [DIST_MAIN, "eval", "--inputs", inputsPath, "--json"], {
        encoding: "utf-8",
      });
      if (proc.status !== 0) {
        console.error(`FAIL ${c.id}: eval exited ${proc.status}\n${proc.stderr.slice(0, 400)}`);
        failures++;
        continue;
      }
      const parsed = JSON.parse(proc.stdout) as { values: Record<string, { value: Value }> };
      const got = new Map(Object.entries(parsed.values).map(([k, v]) => [k, v.value]));
      const problems: string[] = [];
      for (const [key, expected] of Object.entries(c.expect ?? {})) {
        const actual = got.get(key);
        if (!actual) {
          problems.push(`${key}: not evaluated`);
        } else if (JSON.stringify(actual) !== JSON.stringify(expected)) {
          problems.push(`${key}: expected ${JSON.stringify(expected)} got ${JSON.stringify(actual)}`);
        }
      }
      if (problems.length > 0) {
        console.error(`FAIL ${c.id}:\n  ${problems.slice(0, 5).join("\n  ")}${problems.length > 5 ? `\n  … ${problems.length - 5} more` : ""}`);
        failures++;
      } else {
        console.log(`ok   ${c.id} (${Object.keys(c.expect ?? {}).length} values)`);
      }
    }
  } finally {
    rmSync(tmp, { recursive: true, force: true });
  }
  console.log(`\nfixtures: ${cases - failures}/${cases} passed through the command-line program`);
  return failures;
}

export function coverageReport(): void {
  const data = loadCanonical();
  const file = loadCases();
  const targets = data.forms.flatMap((doc) => doc.lines.map((l) => l.id));
  // (lineKey, guardIndex) -> case ids
  const taken = new Map<string, string[]>();
  for (const c of file.cases) {
    const result = evaluate(data, c.inputs, targets);
    for (const der of result.derivations.values()) {
      if (der.op === "choose" && der.takenGuardIndex !== undefined) {
        const key = `${der.line}#${der.takenGuardIndex}`;
        taken.set(key, [...(taken.get(key) ?? []), c.id]);
      }
    }
  }

  // Enumerate all choose lines statically for non-def documents; def-internal
  // choices are reported per instance below (their guards are
  // binding-independent; each observed instance exercises the wiring).
  const chooseLines: { key: string; count: number }[] = [];
  for (const doc of data.forms) {
    for (const line of doc.lines) {
      if (line.expr.op === "choose") {
        chooseLines.push({ key: line.id, count: line.expr.alternatives.length });
      }
    }
  }

  const out: string[] = [];
  out.push("# Branch coverage — Stage 1 fixtures");
  out.push("");
  out.push("Which fixture case takes each choose-guard. Def lines appear per instance binding;");
  out.push("because guard predicates depend only on the bound amount, each def's guards are");
  out.push("covered once across instances rather than once per instance.");
  out.push("");
  let uncovered = 0;
  for (const { key, count } of chooseLines) {
    const rows: string[] = [];
    for (let i = 0; i < count; i++) {
      const cases = taken.get(`${key}#${i}`) ?? [];
      if (cases.length === 0) uncovered++;
      rows.push(`- guard ${i}: ${cases.length > 0 ? cases.join(", ") : "**UNOBSERVED**"}`);
    }
    out.push(`## ${key} (${count} guards)`);
    out.push(...rows);
    out.push("");
  }
  // Instance-owned choices observed in derivations.
  const instanceKeys = new Set<string>();
  for (const k of taken.keys()) {
    const lineKey = k.slice(0, k.lastIndexOf("#"));
    if (lineKey.includes("|inst:")) instanceKeys.add(lineKey);
  }
  for (const instKey of [...instanceKeys].sort()) {
    const defMatch = /inst:([a-z_]+)#/.exec(instKey);
    const lineMatch = /\}\.([a-z0-9_]+)$/.exec(instKey);
    const defId = defMatch?.[1];
    const lineId = lineMatch?.[1];
    const def = defId ? data.defs.find((d) => d.id === defId) : undefined;
    const line = lineId ? def?.lines.find((l) => l.id === lineId) : undefined;
    const count = line && line.expr.op === "choose" ? line.expr.alternatives.length : 0;
    const shortKey = `${defId}.${lineId} [${instKey}${instKey.includes("#") ? "" : ""}]`;
    out.push(`## ${shortKey} (${count} guards)`);
    for (let i = 0; i < count; i++) {
      const cases = taken.get(`${instKey}#${i}`) ?? [];
      if (cases.length === 0) uncovered++;
      out.push(`- guard ${i}: ${cases.length > 0 ? cases.join(", ") : "**UNOBSERVED**"}`);
    }
    out.push("");
  }

  const outPath = join(ROOT, "reports", "2025", "coverage.md");
  writeFileSync(outPath, out.join("\n"));
  console.log(`coverage: ${taken.size} guards observed; ${uncovered} guards unobserved`);
  console.log(`report: reports/2025/coverage.md`);
}
