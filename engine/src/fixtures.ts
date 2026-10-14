// Fixtures: covering cases over the Stage 1 slice.
//
// `record-fixtures` fills each case's expected values from the evaluator (a
// convenience for recording; the values are then frozen in the file).
// `test-fixtures` runs every case THROUGH THE COMMAND-LINE PROGRAM and
// compares. `coverage` reports which case takes each choose-guard.

import { mkdtempSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { isDeepStrictEqual } from "node:util";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { loadCanonical } from "./canonical.js";
import { evaluate } from "./eval.js";
import type { Inputs } from "./types.js";
import type { Value } from "./eval.js";

const ROOT = resolve(import.meta.dirname, "../..");
const CASES_PATH = join(ROOT, "fixtures", "2025", "stage1.json");
const DIST_MAIN = join(ROOT, "engine", "dist", "main.js");

export interface FixtureCase {
  id: string;
  covers: string[];
  evidence: string;
  evidence_note?: string;
  inputs: Inputs;
  expect?: Record<string, Value>;
}

export interface FixtureFile {
  tax_year: number;
  cases: FixtureCase[];
}

export function loadCases(): FixtureFile {
  const dir = join(ROOT, "fixtures", "2025");
  return { tax_year: 2025, cases: readdirSync(dir).filter(f => /^stage[0-9]+\.json$/.test(f)).sort().flatMap(f => (JSON.parse(readFileSync(join(dir,f),"utf8")) as FixtureFile).cases) };
}

function saveCases(file: FixtureFile): void {
  writeFileSync(CASES_PATH, JSON.stringify(file, null, 2) + "\n");
}

const VALUE_KINDS = new Set(["money", "bool", "enum"]);

export function recordFixtures(): void {
  const data = loadCanonical();
  const file = JSON.parse(readFileSync(CASES_PATH, "utf8")) as FixtureFile;
  const targets = data.forms.filter(d => !d.collection).flatMap((doc) => doc.lines.map((l) => l.id));
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
        } else if (!isDeepStrictEqual(actual, expected)) {
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
  const targets = data.forms.filter(d => !d.collection).flatMap((doc) => doc.lines.map((l) => l.id));
  // (lineKey, guardIndex) -> case ids
  const taken = new Map<string, string[]>();
  const branches = new Map<string, Set<string>>();
  const evidence = new Map<string, Set<string>>();
  const template = (key: string) => key.includes("[") ? key.replace(/(?:[a-zA-Z0-9_]+\[[^\]]+\]\.)+/g, m => m.split(".").filter(Boolean).at(-1)!.split("[")[0]+".") : key;
  const mark = (key: string, c: FixtureCase) => { const set=branches.get(key)??new Set();set.add(c.id);branches.set(key,set); };

  for (const c of file.cases) {
    const result = evaluate(data, c.inputs, targets);
    for (const der of result.derivations.values()) {
      const id=template(der.line);
      if (der.value.kind !== "unknown" && c.expect && der.line in c.expect) { const set=evidence.get(id)??new Set();set.add(c.evidence);evidence.set(id,set); }
      if (der.value.kind === "bool") mark(`${id}:${der.value.value}`,c);
      if (["subtract_floor0","smaller_of","larger_of"].includes(der.op)) {
        const values=der.operands.filter(o=>o.value.kind==="money").map(o=>(o.value as {cents:number}).cents);
        if (values.length>=2) mark(`${id}:${der.op==="subtract_floor0" ? (values[0]!>values[1]! ? "positive":"floor") : ((der.op==="larger_of" ? values[0]!>=values[1]! : values[0]!<=values[1]!) ? "left":"right")}`,c);
      }
      if (der.op === "choose" && der.takenGuardIndex !== undefined) {
        const key = `${der.line.includes("[") ? der.line.replace(/(?:[a-zA-Z0-9_]+\[[^\]]+\]\.)+/g, m => m.split(".").filter(Boolean).at(-1)!.split("[")[0]+".") : der.line}#${der.takenGuardIndex}`;
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
  out.push("# Branch coverage — all stage fixtures");
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

  out.push("## Gates and arithmetic branches", "");
  for (const doc of data.forms) for (const line of doc.lines) {
    const sides = line.type === "Bool" ? ["false","true"] : line.expr.op === "subtract_floor0" ? ["floor","positive"] : ["smaller_of","larger_of"].includes(line.expr.op) ? ["left","right"] : [];
    for (const side of sides) {
      if (line.id === "sd.screen" && side === "true") { out.push("- sd.screen true: unreachable by Count non-negativity; structural propagation gate, not a tax branch."); continue; }
      const cases=branches.get(`${line.id}:${side}`);
      out.push(`- ${line.id} ${side}: ${cases ? [...cases].join(", ") : "**UNOBSERVED**"}`);
      if (!cases) uncovered++;
    }
  }
  out.push("", "## Evidence by line", "", "Synthetic regressions are not class B; independent human hand-work remains pending.", "", "| Line | Evidence labels on asserted expectations |", "| --- | --- |");
  for(const doc of [...data.forms,...data.defs]) for(const line of doc.lines) {
    const labels=evidence.get(line.id);
    out.push(`| ${line.id} | ${labels ? [...labels].sort().join(", ") : doc.kind === "def" ? "See bound instances above" : "unobserved"} |`);
  }
  const outPath = join(ROOT, "reports", "2025", "coverage.md");
  writeFileSync(outPath, out.join("\n"));
  console.log(`coverage: ${taken.size} guards observed; ${uncovered} guards unobserved`);
  console.log(`report: reports/2025/coverage.md`);
}

/** Review packet: fixture expectations remain candidate answers, not class B. */
export function reviewStage2(): void {
  const cases=loadCases().cases.filter(c=>c.id.startsWith("ss."));
  const out=["# Stage 2 review packet", "", "Status: owner approved proceeding after Stage 2; detailed reviewer annotations and independent hand-work were not supplied. See reviews/2025/stage2.md.", "",
    "## Source transcription", "", "Read rendered/2025/w2.md, rendered/2025/person.md, rendered/2025/s3.md and the added Form 1040 line 31 against the archived sources below. Helper labels are authored explanations, not verbatim IRS lines.", "",
    "- i1040gi.pdf, printed p. 117, Schedule 3 line 11.", "- iw2w3.pdf, printed p. 18, boxes 3, 4 and 7; pp. 12–13 for the railroad exclusion.", "- fw2.pdf, employee and employer identity and boxes 3, 4 and 7.", "- f1040s3.pdf, lines 9–15; f1040.pdf, line 31.", "",
    "Record reviewer, date, snapshot hashes and corrections in reviews/2025/stage2.md (preserved, not generated). Owner response is recorded in that file.", "",
    "## Candidate fixture answers — not class B", "",
    "Use integer cents below. Work each case independently on the archived instructions before comparing the candidate answer. Synthetic boundary inputs can deliberately contain unusual withholding; they test the encoded instructions, not payroll plausibility.", "",
    "| Case | Status | Per-employer (box 3; box 7; box 4), cents | Candidate line 11 |", "| --- | --- | --- | --- |"];
  for(const c of cases){
    const prefixes = new Set(Object.keys(c.inputs).filter(k=>/\.box[347]$/.test(k)).map(k=>k.slice(0,-5)));
    const entries = [...prefixes].sort().map(k=>`${k}: ${c.inputs[k+".box3"] ?? "unknown"}; ${c.inputs[k+".box7"] ?? "unknown"}; ${c.inputs[k+".box4"] ?? "unknown"}`);
    const v=c.expect?.["s3.line11"];
    out.push(`| ${c.id} | ${c.inputs["f1040.status"]} | ${entries.join(" / ") || "none"} | ${v?.kind==="money"?v.cents:v?.kind==="refusal"?`refusal: ${v.form}`:"unknown"} |`);
  }
  out.push("", "RRTA case has the railroad answer true. Other Schedule 3 components are zero except ss.other.components: lines 9, 10, 12 and 14 are 123, 500, 7 and 20 cents; line 15 and Form 1040 line 31 should be 148830 cents.", "",
    "ss.person.separation is a generic engine test with two people, one employer each. It is not an enabled interview path.", "",
    "The additional qdcg.table.minimum.regression covers the previously unobserved final minimum: taxable income $50,010, qualified dividends $1, Single; both ordinary and full income use the $50,000–$50,050 Tax Table cell ($5,920). The candidate preferred calculation is $5,920.15, so the ordinary tax wins. This is also pending human review.", "",
    "## Remaining limits", "", "- This is a slice, not a complete return. Non-Social-Security Schedule 3 components are explicitly supplied subtotals; their underlying forms are not prepared.",
    "- One person is reachable through the interview. Married filing statuses and RRTA are refused.",
    "- Whole-dollar return-wide rounding remains deferred; the slice operates in cents.",
    "- Build-time interview checks enumerate finite enum/Boolean answers over fixture amounts and roster sizes. They are not a proof for unbounded collections.",
    "- Lean proves the added aggregation non-negativity and fixed-filter monotonicity. Evaluator agreement is testing, not a proof of the TypeScript evaluator or of the IRS transcription.",
    "- Stage 1 human review remains outstanding. Stage 3 has not started.", "");
  writeFileSync(join(ROOT,"reports","2025","stage2-review.md"),out.join("\n"));
  const tmp=mkdtempSync(join(tmpdir(),"review-"));
  try {
    for(const id of ["ss.multi","ss.single.over"]){
      const c=cases.find(c=>c.id===id)!;
      const path=join(tmp,"inputs.json");writeFileSync(path,JSON.stringify(c.inputs));
      const proc=spawnSync(process.execPath,[DIST_MAIN,"eval","--inputs",path,"--target","f1040.line31"],{encoding:"utf8"});
      if(proc.status!==0)throw new Error(proc.stderr);
      writeFileSync(join(ROOT,"reports","2025",`${id}.txt`),proc.stdout);
    }
  } finally {rmSync(tmp,{recursive:true,force:true});}
  console.log("review packet: reports/2025/stage2-review.md; synthetic values sheets: ss.multi.txt, ss.single.over.txt");
}

export function reviewStage3(): void {
  const dir=join(ROOT,"reports","2025");
  const selected=["sales.official.basis","sales.mixed_columns","sales.refuse.digital.G","sales.select.sdtw.election"];
  const tmp=mkdtempSync(join(tmpdir(),"stage3-review-"));
  try {
    for(const id of selected) {
      const fixture=loadCases().cases.find(c=>c.id===id)!;
      const input=join(tmp,"inputs.json");writeFileSync(input,JSON.stringify(fixture.inputs));
      const proc=spawnSync(process.execPath,[DIST_MAIN,"eval","--inputs",input,"--target","f1040.line7a,f1040.line16"],{encoding:"utf8"});
      if(proc.status!==0)throw new Error(proc.stderr);
      writeFileSync(join(dir,id+".txt"),proc.stdout);
    }
    writeFileSync(join(dir,"stage3-review.md"),[
      "# Stage 3 review packet", "",
      "Read rendered/2025/sales.md and sd.md alongside archived i8949 pp. 7–11, i1040sd pp. 10–11 and f1040sd. Check the Form 1040 selector against i1040sd p. 15 and i1040gi p. 36.", "",
      "Official arithmetic: i8949 p. 11 examples 1–4 and the repeated Schedule D column-(h) examples; i1040sd pp. 10–11 aggregate example and its two-transaction continuation. The adjustment example supplies no code: the fixture's B routing is synthetic scaffolding, not official evidence. Example 4 explicitly supplies code B. Official digital-asset examples 5–6 and the main-home EH example are outside scope; digital boxes and unsupported codes are refused, not claimed computed.", "",
      "Review choices: exact cents (whole-dollar mode deferred); supplied A–F classification (holding periods, dates, descriptions and basis determination not computed); code W takes a supplied correct disallowed loss; corrected broker wash loss may require a statement. See ambiguities/2025.yaml for rounding and Form 4952 worksheet selection.", "",
      "Schedule D lines 18/19 and Form 4952 amounts remain supplied subtotals. A required Schedule D Tax Worksheet is refused until Stage 4. Capital-loss carryovers and additional source forms are refused. This is not a complete return.", "",
      "The synthetic cases are regressions, not class B. No independent human hand-work is claimed. Stage 3 interview build checks cover fixture paths and answer-order invariance; they are not exhaustive over all finite domains or roster sizes.", "",
      "Earlier fixture inputs were migrated from supplied Form 1040 line 7a/QDCG net-gain inputs to actual sales and distribution inputs. Existing tax expectations were retained. The Schedule-D fixture's line 7a now reflects its $3,000 computed gain; the old zero was an inconsistent placeholder. Obsolete trace aliases now point to the distribution input.", "",
      ...selected.map(id=>`- [${id}](${id}.txt)`), "",
      "See coverage.md, mutation.md and evaluator_agreement.md for generated verification evidence. Record owner observations in reviews/2025/stage3.md.", ""
    ].join("\n"));
  } finally {rmSync(tmp,{recursive:true,force:true});}
  console.log("review: reports/2025/stage3-review.md and four CLI values sheets");
}
