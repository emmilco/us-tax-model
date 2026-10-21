// Fixtures: covering cases over the Stage 1 slice.
//
// `record-fixtures` fills each case's expected values from the evaluator (a
// convenience for recording; the values are then frozen in the file).
// `test-fixtures` runs every case THROUGH THE COMMAND-LINE PROGRAM and
// compares. `coverage` reports which case takes each choose-guard.

import { mkdirSync, mkdtempSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { isDeepStrictEqual } from "node:util";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { loadCanonical } from "./canonical.js";
import { branchKeys, templateKey } from "./branches.js";
import { allTargets, evaluate } from "./eval.js";
import { differentialClassC } from "./differential.js";
import type { Inputs } from "./types.js";
import type { Value } from "./eval.js";
import { YEAR, YEAR_ARGS, yearPath } from "./year.js";

const ROOT = resolve(import.meta.dirname, "../..");
const CASES_PATH = yearPath("fixtures", "stage1.json");
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
  const dir = yearPath("fixtures");
  return { tax_year: YEAR, cases: readdirSync(dir).filter(f => /^(stage[0-9]+|classm)\.json$/.test(f)).sort().flatMap(f => (JSON.parse(readFileSync(join(dir,f),"utf8")) as FixtureFile).cases) };
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
  console.log(`recorded expected values for ${file.cases.length} cases in fixtures/${YEAR}/stage1.json`);
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
      const proc = spawnSync(process.execPath, [DIST_MAIN, ...YEAR_ARGS, "eval", "--inputs", inputsPath, "--json"], { encoding: "utf-8", maxBuffer: 256 * 1024 * 1024 });
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

export function reviewStage5(): void {
  const dir=yearPath("reports");
  const selected=["stage5.return.owed","stage5.return.refund","stage5.return.itemized"];
  const tmp=mkdtempSync(join(tmpdir(),"stage5-review-"));
  try {
    mkdirSync(dir,{recursive:true});
    for(const id of selected) {
      const fixture=loadCases().cases.find(c=>c.id===id)!;
      const input=join(tmp,"inputs.json");writeFileSync(input,JSON.stringify(fixture.inputs));
      const proc=spawnSync(process.execPath,[DIST_MAIN, ...YEAR_ARGS,"eval","--inputs",input],{ encoding: "utf-8", maxBuffer: 256 * 1024 * 1024 });
      if(proc.status!==0)throw new Error(proc.stderr);
      writeFileSync(join(dir,id+".txt"),proc.stdout);
    }
    writeFileSync(join(dir,"stage5-review.md"),[
      "# Stage 5 review packet", "",
      "Stage 5 completes the single-person return: Form 1040 lines 1a\u201337 computed end to end \u2014 income, AGI, the standard-or-itemized choice, QBI, taxable income, tax through the QDCG/SDTW/table paths, Schedule 2 and 3 integration, payments, and refund/amount owed. AGI and taxable income are no longer supplied. The full interview (`--profile full`) walks this return; the three synthetic cases below double as the calculator-entry cases for the whole-return differential.", "",
      "## Review against archived sources", "",
      `Compare the three values sheets with the Form 1040 facsimile (sources/${YEAR}/f1040.txt, pages 1\u20132) for line labels and arithmetic, and with i1040gi for the instruction text: lines 1a\u201311b on pp. 23\u201334, the deduction lines on pp. 34\u201336, and the line 25\u201337 instructions. The QDCG and SDTW worksheets were reviewed at Stages 1 and 4; Stage 5 changes only what feeds them. Check that lines 13b, 19, 27a\u201330 refuse when their screens fire and that the scope screens propagate: a refused screen must refuse lines 8/10/13b/16/19 and everything downstream.`, "",
      "## Concrete checks", "",
      "Case `stage5.return.owed` (two employers): wages 120,000.00 + interest 1,200.00 + ordinary dividends 2,000.00 (of which 1,500.00 qualified; line 3a is a component of line 3b, not an addend of line 9) = total income 123,200.00; standard deduction 15,750.00; taxable income 107,450.00; QDCG path with 1,500.00 preferential: tax on 105,950.00 at the 2025 single rates = 17,651.00 + 24% \u00d7 2,600.00 = 18,275.00, plus 15% \u00d7 1,500.00 = 225.00, total 18,500.00; withheld 17,000.00; amount owed 1,500.00. The sheet reports exactly these.", "",
      "Case `stage5.return.refund` (one employer): wages 130,000.00; taxable income 114,250.00; tax = 17,651.00 + 24% \u00d7 10,900.00 = 20,267.00; withheld 20,000.00 plus 2,000.00 estimated = 22,000.00; overpaid 1,733.00, refunded 1,733.00.", "",
      "Case `stage5.return.itemized`: total income 102,500.00 = wages 90,000.00 + interest 1,000.00 + ordinary dividends 4,000.00 (of which 2,000.00 qualified) + capital gain 7,500.00 (a 6,000.00 long-term sale plus 1,500.00 of distributions); itemized deductions 27,300.00 = state and local taxes 10,000.00 + mortgage interest 10,000.00 + cash gifts 5,000.00 + noncash gift 800.00 + investment interest 1,500.00 (medical 3,000.00 is zero after the 7.5% floor); AGI 102,500.00; QBI deduction 60.00 (20% of the 300.00 section 199A dividends); taxable income 75,140.00; QDCG tax 10,777.00 = Tax Table on 65,640.00 ordinary (9,352.00) plus 15% \u00d7 9,500.00 (1,425.00); the 120.00 foreign tax credit reduces it (Form 1040 line 20) to 10,657.00; withheld 10,000.00; amount owed 657.00.", "",
      ...selected.map(id=>`- [${id}](${id}.txt)`), "",
      "## Migration record", "",
      "Every fixture that supplied `f1040.line15` or `sa.agi` was migrated to real income inputs that reproduce the fixture\u2019s intended value: 178 cases reconstructed with an income entry (one W-2 employer), verified against the original anchors; 79 cases (refusals, the Stage 2 cohort) kept answers only; three cases fund their target through an offsetting cash-gift deduction instead of wages (qdcg.l5.floor0, qdcg.20pct, stage4.sdtw.skip22); one case needed a manual anchor correction (stage4.ftc.regular_limit, whose credit limit is tested against a zero tax). The `qdcg.table.minimum.regression` fixture moved from stage2.json to stage1.json because the Stage 2 finite-domain check enumerates every Boolean in each fixture and its chain now reaches the whole return. The sales interview profile gained the base-chain questions its targets now reach (22 blocks copied from the Stage 4 profile); the Stage 4 profile gained w2.box1. Interview walk caps in the integration checks were raised (50 \u2192 150 steps) to match the deeper chain.", "",
      "## Limits and evidence", "",
      `Return-wide whole-dollar rounding remains deferred (standing ambiguity; exact cents throughout). Lines 25b, 25c, 26, 35a and 36 are supplied elections or totals read from the filer\u2019s records; nothing else on the return is supplied. The estimated tax penalty is not computed \u2014 the output states that the IRS will figure it. Joint and MFS returns are refused; Form 1116 and the other deferrals are unchanged from Stage 4. No human hand-work or source reading is claimed (spec 3, requirement 11); the independent constructions of spec 6.5 stand in for them. The whole-return differential (class C) is prepared \u2014 entry sheets at reports/${YEAR}/differential.<case>.md, records go to fixtures/${YEAR}/differential/. These two cases were corrected under BUG-0001 (BUG_INVENTORY.md), which an engine comparison caught. See evidence.md for per-line class coverage, and mutation.md, coverage.md, evaluator_agreement.md for the generated verification evidence.`, ""
    ].join("\n"));
  } finally {rmSync(tmp,{recursive:true,force:true});}
  console.log(`review: reports/${YEAR}/stage5-review.md and three whole-return values sheets`);
}

export function evidenceReport(): void {
  const data = loadCanonical();
  const file = loadCases();
  const template = (key: string) => key.includes("[") ? key.replace(/(?:[a-zA-Z0-9_]+\[[^\]]+\]\.)+/g, m => m.split(".").filter(Boolean).at(-1)!.split("[")[0]+".") : key;
  interface Classes { A: Set<string>; B: Set<string>; C: Set<string>; R: Set<string> }
  const coverage = new Map<string, Classes>();
  for (const doc of [...data.forms, ...data.defs]) {
    for (const line of doc.lines) coverage.set(line.id, { A: new Set(), B: new Set(), C: new Set(), R: new Set() });
  }
  const unknownKeys = new Set<string>();
  const supplied = new Map<string, number>();
  const isInput = new Map<string, boolean>();
  for (const doc of [...data.forms, ...data.defs]) for (const line of doc.lines) isInput.set(line.id, line.expr.op === "input");
  for (const c of file.cases) {
    const ev = (c.evidence ?? "").trim();
    const cls: keyof Classes = ev === "C" ? "C" : ev.startsWith("B") ? "B" : ev.startsWith("A") ? "A" : "R";
    for (const key of Object.keys(c.inputs ?? {})) {
      if (key.startsWith("$")) continue;
      const id = template(key);
      supplied.set(id, (supplied.get(id) ?? 0) + 1);
    }
    for (const key of Object.keys(c.expect ?? {})) {
      if (key.startsWith("$")) continue;
      const bucket = coverage.get(template(key));
      if (!bucket) { unknownKeys.add(key); continue; }
      bucket[cls].add(c.id);
    }
  }
  for (const [key, who] of differentialClassC()) {
    const bucket = coverage.get(template(key));
    if (bucket) for (const w of who) bucket.C.add(w);
  }
  const out: string[] = [];
  out.push("# Evidence coverage per line", "");
  out.push(`Fixtures that assert each line, by evidence class. A — official IRS example. B — human hand-work (pending; marked where recorded). C — recorded value also confirmed by the independently written Lean reference evaluator (running evaluator agreement, reports/${YEAR}/evaluator_agreement.md); the external-calculator comparison is the Stage 5 differential and remains pending. M — an isolated model worked the document by hand from its archived pages and the amounts flowing into it (reviews/${YEAR}/classm/). R — recorded synthetic regression, no class claimed, human review pending.`, "");
  const fmt = (s: Set<string>) => s.size === 0 ? "—" : `${s.size}${s.size <= 2 ? " (" + [...s].join(", ") + ")" : ""}`;
  let totalGaps = 0; const allGaps: string[] = [];
  for (const doc of [...data.forms, ...data.defs]) {
    if (doc.lines.length === 0 || !coverage.has(doc.lines[0]!.id)) continue;
    out.push(`## ${doc.title ?? doc.id}`, "");
    out.push("| line | A | B | C | R |", "| --- | --- | --- | --- | --- |");
    const gaps: string[] = [];
    for (const l of doc.lines) {
      const b = coverage.get(l.id)!;
      if (b.A.size + b.B.size + b.C.size + b.R.size === 0 && !isInput.get(l.id)) { gaps.push(l.id); allGaps.push(l.id); }
      out.push(`| ${l.id} | ${fmt(b.A)} | ${fmt(b.B)} | ${fmt(b.C)} | ${fmt(b.R)} |`);
    }
    if (gaps.length) out.push("", `Unasserted lines: ${gaps.join(", ")}`);
    out.push("");
    totalGaps += gaps.length;
  }
  const formLineIds = new Set(data.forms.flatMap(d => d.lines.map(l => l.id)));
  const neverSupplied = [...isInput.entries()].filter(([id, isIn]) => isIn && formLineIds.has(id) && (supplied.get(id) ?? 0) === 0).map(([id]) => id);
  out.push(`Unasserted computed lines across all documents: ${totalGaps}. (Supplied input lines are excluded; their correctness rests on reading the source document. Intermediate lines listed as unasserted are still exercised transitively; their detectability is tracked in reports/${YEAR}/mutation.md.)`);
  if (neverSupplied.length > 0) out.push("", `Input lines never supplied by any fixture: ${neverSupplied.join(", ")}.`);
  if (unknownKeys.size > 0) out.push(`Asserted keys not matching a line id: ${[...unknownKeys].slice(0, 40).join(", ")}${unknownKeys.size > 40 ? " …" : ""}`);
  writeFileSync(yearPath("reports", "evidence.md"), out.join("\n"));
  console.log(`evidence: per-line class coverage written; unasserted lines: ${totalGaps}`);
  console.log(`report: reports/${YEAR}/evidence.md`);
}

export function coverageReport(): void {
  const data = loadCanonical();
  const file = loadCases();
  // (lineKey, guardIndex) -> case ids
  const taken = new Map<string, string[]>();
  const branches = new Map<string, Set<string>>();
  const evidence = new Map<string, Set<string>>();
  const mark = (key: string, c: FixtureCase) => { const set=branches.get(key)??new Set();set.add(c.id);branches.set(key,set); };

  for (const c of file.cases) {
    const result = evaluate(data, c.inputs, allTargets(data, c.inputs));
    for (const der of result.derivations.values()) {
      const id=templateKey(der.line);
      if (der.value.kind !== "unknown" && c.expect && der.line in c.expect) { const set=evidence.get(id)??new Set();set.add(c.evidence);evidence.set(id,set); }
      const b = branchKeys(der);
      for (const key of b.sides) mark(key, c);
      for (const key of b.guards) taken.set(key, [...(taken.get(key) ?? []), c.id]);
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
      if ((["f8959.line12","f8959.line16"].includes(line.id) && side==="positive") || (line.id==="scope.ready" && side==="false")) {
        out.push(`- ${line.id} ${side}: unreachable in the supported slice; the source amount is structurally zero, or the scope gate returns a refusal instead.`); continue;
      }
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
  // The share of lines that escape the atom vocabulary (design Stage 8 stop condition).
  const allLines = [...data.forms, ...data.defs].flatMap((d) => d.lines);
  const opaqueLines = allLines.filter((l) => l.expr.op === "opaque");
  out.push("", "## Opaque escapes", "", `${opaqueLines.length} of ${allLines.length} lines use \`opaque\` (share ${(opaqueLines.length / allLines.length).toFixed(4)}); the design's stop condition is one in eight.${opaqueLines.length ? " Lines: " + opaqueLines.map((l) => l.id).join(", ") : ""}`, "");
  const outPath = yearPath("reports", "coverage.md");
  writeFileSync(outPath, out.join("\n"));
  console.log(`coverage: ${taken.size} guards observed; ${uncovered} guards unobserved`);
  console.log(`report: reports/${YEAR}/coverage.md`);
}

/** Review packet: fixture expectations remain candidate answers, not class B. */
export function reviewStage2(): void {
  const cases=loadCases().cases.filter(c=>c.id.startsWith("ss."));
  const out=["# Stage 2 review packet", "", `Status: owner approved proceeding after Stage 2; detailed reviewer annotations and independent hand-work were not supplied. See reviews/${YEAR}/stage2.md.`, "",
    "## Source transcription", "", `Read rendered/${YEAR}/w2.md, rendered/${YEAR}/person.md, rendered/${YEAR}/s3.md and the added Form 1040 line 31 against the archived sources below. Helper labels are authored explanations, not verbatim IRS lines.`, "",
    "- i1040gi.pdf, printed p. 117, Schedule 3 line 11.", "- iw2w3.pdf, printed p. 18, boxes 3, 4 and 7; pp. 12–13 for the railroad exclusion.", "- fw2.pdf, employee and employer identity and boxes 3, 4 and 7.", "- f1040s3.pdf, lines 9–15; f1040.pdf, line 31.", "",
    `Record reviewer, date, snapshot hashes and corrections in reviews/${YEAR}/stage2.md (preserved, not generated). Owner response is recorded in that file.`, "",
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
  writeFileSync(yearPath("reports", "stage2-review.md"),out.join("\n"));
  const tmp=mkdtempSync(join(tmpdir(),"review-"));
  try {
    for(const id of ["ss.multi","ss.single.over"]){
      const c=cases.find(c=>c.id===id)!;
      const path=join(tmp,"inputs.json");writeFileSync(path,JSON.stringify(c.inputs));
      const proc=spawnSync(process.execPath,[DIST_MAIN, ...YEAR_ARGS,"eval","--inputs",path,"--target","f1040.line31"],{ encoding: "utf-8", maxBuffer: 256 * 1024 * 1024 });
      if(proc.status!==0)throw new Error(proc.stderr);
      writeFileSync(yearPath("reports", `${id}.txt`),proc.stdout);
    }
  } finally {rmSync(tmp,{recursive:true,force:true});}
  console.log(`review packet: reports/${YEAR}/stage2-review.md; synthetic values sheets: ss.multi.txt, ss.single.over.txt`);
}

export function reviewStage3(): void {
  const dir=yearPath("reports");
  const selected=["sales.official.basis","sales.mixed_columns","sales.refuse.digital.G","sales.select.sdtw.election"];
  const tmp=mkdtempSync(join(tmpdir(),"stage3-review-"));
  try {
    for(const id of selected) {
      const fixture=loadCases().cases.find(c=>c.id===id)!;
      const input=join(tmp,"inputs.json");writeFileSync(input,JSON.stringify(fixture.inputs));
      const proc=spawnSync(process.execPath,[DIST_MAIN, ...YEAR_ARGS,"eval","--inputs",input,"--target","f1040.line7a,f1040.line16"],{ encoding: "utf-8", maxBuffer: 256 * 1024 * 1024 });
      if(proc.status!==0)throw new Error(proc.stderr);
      writeFileSync(join(dir,id+".txt"),proc.stdout);
    }
    writeFileSync(join(dir,"stage3-review.md"),[
      "# Stage 3 review packet", "",
      `Read rendered/${YEAR}/sales.md and sd.md alongside archived i8949 pp. 7–11, i1040sd pp. 10–11 and f1040sd. Check the Form 1040 selector against i1040sd p. 15 and i1040gi p. 36.`, "",
      "Official arithmetic: i8949 p. 11 examples 1–4 and the repeated Schedule D column-(h) examples; i1040sd pp. 10–11 aggregate example and its two-transaction continuation. The adjustment example supplies no code: the fixture's B routing is synthetic scaffolding, not official evidence. Example 4 explicitly supplies code B. Official digital-asset examples 5–6 and the main-home EH example are outside scope; digital boxes and unsupported codes are refused, not claimed computed.", "",
      `Review choices: exact cents (whole-dollar mode deferred); supplied A–F classification (holding periods, dates, descriptions and basis determination not computed); code W takes a supplied correct disallowed loss; corrected broker wash loss may require a statement. See ambiguities/${YEAR}.yaml for rounding and Form 4952 worksheet selection.`, "",
      "Stage 4 now computes Schedule D lines 18/19 from distribution feeders, Form 4952 amounts and the Schedule D Tax Worksheet; these regenerated examples reflect that extension. Capital-loss carryovers and additional source forms are refused. This is not a complete return.", "",
      "The synthetic cases are regressions, not class B. No independent human hand-work is claimed. Stage 3 interview build checks cover fixture paths and answer-order invariance; they are not exhaustive over all finite domains or roster sizes.", "",
      "Earlier fixture inputs were migrated from supplied Form 1040 line 7a/QDCG net-gain inputs to actual sales and distribution inputs. Existing tax expectations were retained. The Schedule-D fixture's line 7a now reflects its $3,000 computed gain; the old zero was an inconsistent placeholder. Obsolete trace aliases now point to the distribution input.", "",
      ...selected.map(id=>`- [${id}](${id}.txt)`), "",
      `See coverage.md, mutation.md and evaluator_agreement.md for generated verification evidence. Record owner observations in reviews/${YEAR}/stage3.md.`, ""
    ].join("\n"));
  } finally {rmSync(tmp,{recursive:true,force:true});}
  console.log(`review: reports/${YEAR}/stage3-review.md and four CLI values sheets`);
}

export function reviewStage4(): void {
  const dir=yearPath("reports");
  const selected=["stage4.sdtw.special_rates","stage4.deductions.combined","stage4.additional_taxes.combined","stage4.refuse.div.section1202","stage4.refuse.ftc.limit"];
  const targets="scope.ready,f1040.line7a,f1040.line16,sa.deduction,f4952.line8,qbi.deduction,s2.line21,f8959.line24,s3.line1";
  const tmp=mkdtempSync(join(tmpdir(),"stage4-review-"));
  try {
    mkdirSync(dir,{recursive:true});
    for(const id of selected) {
      const fixture=loadCases().cases.find(c=>c.id===id)!;
      const input=join(tmp,"inputs.json");writeFileSync(input,JSON.stringify(fixture.inputs));
      const proc=spawnSync(process.execPath,[DIST_MAIN, ...YEAR_ARGS,"eval","--inputs",input,"--target",targets],{ encoding: "utf-8", maxBuffer: 256 * 1024 * 1024 });
      if(proc.status!==0)throw new Error(proc.stderr);
      writeFileSync(join(dir,id+".txt"),proc.stdout);
    }
    writeFileSync(join(dir,"stage4-review.md"),[
      "# Stage 4 review packet", "",
      "Stage 4 implements additional form slices and their CLI interview. AGI and taxable income remain supplied subtotals; Stage 5 must connect a complete Form 1040. These sample values sheets are synthetic worksheet exercises, not complete returns.", "",
      "## Review against archived sources", "",
      `Compare rendered/${YEAR}/sa.md with f1040sa and i1040sca p. 7 (SALT); f4952.md with f4952; gift.md with i8283 pp. 1–3. Check standard deduction amounts and exceptions against i1040gi pp. 34–35. Compare sb.md with f1040sb and i1040sb.`, "",
      "Compare sdtw.md with i1040sd pp. 15–16, g28.md and u1250.md with pp. 11–14. The special-rates fixture asserts all 47 worksheet lines; independently hand-work those expectations, including the printed skip instructions.", "",
      "Compare f8959.md and f8960.md with their forms and instructions (NIIT deductions pp. 17–18 and MAGI p. 22). Compare qbi.md, f8995.md and f8995a.md with their forms, i8995-correction and i8995a. Compare ftc.md with i1116 pp. 1–2 and s2.md with f1040s2.", "",
      "## Concrete checks", "",
      "The combined-deductions case gives $2,500 medical + $9,000 taxes + $11,000 interest + $5,200 charity = $27,700 itemized deductions. The additional-taxes case gives $450 Additional Medicare Tax + $646 NIIT = $1,096 Schedule 2 line 21; additional withholding is separately $450. Check each amount and its source assumptions.", "",
      ...selected.map(id=>`- [${id}](${id}.txt)`), "",
      "## Limits and evidence", "",
      "1099-DIV box 2c remains a cited refusal because its inclusion conflicts with the code Q/Form 6251 exclusions. See amb.2025.box2c_scope; no owner decision to expand scope is recorded. Boxes 2b/2d feed the special-gain worksheets. Direct special-property sales remain refused.", "",
      "Eligibility screens rely on explicit answers. Charity valuation, basis reductions and income-limit checks, mortgage eligibility, NIIT allocation, REIT-dividend eligibility and simple FTC eligibility are supplied determinations. Form 8283 support groups amounts and routes Section A/B; dates, descriptions and donee records are not prepared. Per-spouse interviews remain refused. Exact-cent calculations continue; return-wide whole-dollar rounding is deferred.", "",
      "Official evidence added: i8959 p. 2 example 5 supplies $75,000 wages subject to additional tax; its married inputs are arithmetic scaffolding, not support for a married interview. Other i8959 examples require self-employment/RRTA, which are screened out. i8283 p. 2 supplies the $5,400 grouped-books Section B example. The i8960 rental allocation example is outside scope and is not claimed computed. Synthetic expectations remain regressions, not independently human-verified class B.", "",
      "All spec 2.2 refusal categories have cited screens and fixtures: FTC (ftc), other QBI (qbi), carryover/digital/unsupported adjustments/direct special-property sales (sd/sales), AMT (s2/div), Schedule 1/1-A and other credits (scope), excluded itemized deductions (sa/gift/f4952), special interest treatment and foreign reporting (sb), married per-spouse treatment (s3/scope). Screening is a target of the Stage 4 interview; individual form evaluations are not a whole-return acceptance decision.", "",
      `See coverage.md, mutation.md and evaluator_agreement.md for current counts and remaining gaps. Mutation survivors are published, including unresolved ones; coverage does not certify tax correctness. Interview fixture-path checks are representative, not exhaustive. Record source-review and hand-work observations in reviews/${YEAR}/stage4.md.`, ""
    ].join("\n"));
  } finally {rmSync(tmp,{recursive:true,force:true});}
  console.log(`review: reports/${YEAR}/stage4-review.md and five CLI values sheets`);
}
