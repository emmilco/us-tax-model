// Two-evaluator agreement: run every fixture case and a deterministic set of
// generated inputs through the TypeScript evaluator and the Lean reference
// evaluator, and fail on any difference (spec section 6.3 / design 2.6).

import { existsSync, mkdtempSync, readFileSync, rmSync, writeFileSync, mkdirSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { loadCanonical } from "./canonical.js";
import { evaluate } from "./eval.js";
import { loadCases } from "./fixtures.js";
import type { Inputs } from "./types.js";
import type { Value } from "./eval.js";

const ROOT = resolve(import.meta.dirname, "../..");
const LEAN_BIN = join(ROOT, "lean", ".lake", "build", "bin", "taxeval");
const CANON = join(ROOT, "canonical", "2025");
const FIXTURES = join(ROOT, "fixtures", "2025", "stage1.json");

interface Case {
  id: string;
  inputs: Inputs;
}

function fixtureCases(): Case[] {
  const file = loadCases();
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
    const standard: Record<string, number> = { single: 1575000, mfj: 3150000, mfs: 1575000, hoh: 2362500, qss: 3150000 };
    const line7a = rnd() < 0.3 ? Math.floor(rnd() * 3000000) : 0;
    const sdFiled = rnd() < 0.25;
    const inputs: Inputs = {
      "f1040.status": status,
      "f1040.line3a": line3a,
      "sd.distributions": line7a,
      "$sales": [], "sd.other_forms": false, "sd.carryover": false,
      "qbi.dividends":0,"div.box2b":0,"div.box2c":0,"div.box2d":0,"div.box2e":0,"div.box2f":0,"div.box3":0,"div.box9":0,"div.box10":0,"div.box13":0,"div.basis_reconciled":true, "f4952.line1": 0, "f4952.line4g": 0,
      "f4952.carryover": false, "f4952.unsupported": false, "f4952.alternative_allocation": false, "$interest": [], "sb.ordinary_dividends": line3a, "sb.unsupported": false, "sb.line7a": false, "sb.fbar_required": false, "sb.form8938": false, "sb.line8": false,
    };
    inputs["$person"] = ["taxpayer"];
    inputs["person[taxpayer].role"] = "taxpayer";
    inputs["$w2@person[taxpayer]"] = ["a"];
    inputs["person[taxpayer].w2[a].box1"] = Math.max(0, line15 + standard[status]! - 2 * line3a);
    inputs["scope.schedule1"] = false;
    inputs["scope.other_income"] = false;
    inputs["sa.unsupported"] = false; inputs["sa.charity_limited"] = false; inputs["sa.excluded_income"] = false;
    inputs["sa.dependent"] = false; inputs["sa.spouse_extra"] = false; inputs["person[taxpayer].age65"] = false; inputs["person[taxpayer].blind"] = false;
    inputs["sa.spouse_itemizes"] = false; inputs["sa.elect_itemize"] = false;
    // A joint return has an entry for each spouse; the generated spouse has no income.
    if (status === "mfj") {
      inputs["$person"] = ["taxpayer", "spouse"];
      inputs["person[spouse].role"] = "spouse";
      inputs["$w2@person[spouse]"] = [];
      inputs["person[spouse].age65"] = false; inputs["person[spouse].blind"] = false;
    }
    inputs["sa.line1"] = 0; inputs["sa.line5a"] = 0; inputs["sa.line5b"] = 0; inputs["sa.line5c"] = 0; inputs["sa.line8a"] = 0; inputs["sa.line11"] = 0;
    inputs["$gift"] = [];
    inputs["qbi.unsupported"] = false;
    if (sdFiled) {
      inputs["$sales"] = ["generated"];
      Object.assign(inputs, Object.fromEntries(Object.entries({box:"D", route:"detail", code:"none", special:false,
        proceeds:Math.floor(rnd()*5000000), reported_basis:Math.floor(rnd()*5000000)}).map(([k,v])=>[`sales[generated].${k}`,v])));
    }
    const stage2: Inputs = { ...inputs, "person[taxpayer].rrta": false, ...(status === "mfj" ? { "person[spouse].rrta": false } : {}),
      "$w2@person[taxpayer]": ["a", "b"], "s3.line9": 0, "s3.line10": 0, "s3.line12": 0, "s3.line14": 0 };
    for (const employer of ["a", "b"]) {
      stage2[`person[taxpayer].w2[${employer}].box3`] = Math.floor(rnd() * 17610001);
      stage2[`person[taxpayer].w2[${employer}].box7`] = 0;
      stage2[`person[taxpayer].w2[${employer}].box4`] = Math.floor(rnd() * 1200000);
      if (employer === "b") stage2[`person[taxpayer].w2[b].box1`] = 0;
    }
    cases.push({id: `collections.${i}`, inputs: stage2});
    cases.push({ id: `generated.${String(i).padStart(3, "0")}`, inputs });
    const salesInputs:Inputs={...inputs,"$sales":[]};
    for(const key of Object.keys(salesInputs)) if(key.startsWith("sales["))delete salesInputs[key];
    const keys=Array.from({length:Math.floor(rnd()*5)},(_,j)=>`row${j}`);
    salesInputs["$sales"]=keys;
    for(const key of keys) {
      const box="ABCDEF"[Math.floor(rnd()*6)]!;
      const code=["none","B","W","BW"][Math.floor(rnd()*4)]!;
      const route=(box==="A"||box==="D")&&code==="none"&&rnd()<0.5?"aggregate":"detail";
      const fields={box,code,route,special:false,aggregate_eligible:true,
        proceeds:Math.floor(rnd()*1000000),reported_basis:Math.floor(rnd()*1000000),
        correct_basis:Math.floor(rnd()*1000000),wash_loss:Math.floor(rnd()*100000)};
      for(const [field,value] of Object.entries(fields))salesInputs[`sales[${key}].${field}`]=value;
    }
    cases.push({id:`sales-generated.${i}`,inputs:salesInputs});
  }
  return cases;
}

function normalize(v: Value | Record<string, unknown>): string {
  const val = v as { kind?: string; cents?: number; value?: unknown };
  if (val.kind === "refusal") { const r = v as Record<string, unknown>; return `refusal:${r.gate}:${r.form}:${r.remedy}:${JSON.stringify(Object.entries(r.cite as Record<string, unknown>).sort())}`; }
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
  const targets = data.forms.filter(d => !d.collection).flatMap((doc) => doc.lines.map((l) => l.id));
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
      const proc = spawnSync(LEAN_BIN, ["--canonical", CANON, "--inputs", inputsPath, "--out", outPath], { encoding: "utf-8", maxBuffer: 256 * 1024 * 1024 });
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
      for (const [key, der] of ts.derivations) if (key.includes("[")) tsValues[key] = der.value;
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
  report.push("Every fixture case and deterministic sets of 200 ordinary-income and 200 collection inputs were evaluated");
  report.push("by both independently written evaluators; every root form line and reached collection entry was compared");
  report.push("(money cents, counts, booleans, enums, full refusals; unknowns compared by kind).");
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
