// Fixtures: covering cases over the Stage 1 slice.
//
// `record-fixtures` fills each case's expected values from the evaluator (a
// convenience for recording; the values are then frozen in the file).
// `test-fixtures` runs every case THROUGH THE COMMAND-LINE PROGRAM and
// compares. `coverage` reports which case takes each choose-guard.

import { existsSync, mkdirSync, mkdtempSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { isDeepStrictEqual } from "node:util";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { loadCanonical } from "./canonical.js";
import { branchKeys, templateKey } from "./branches.js";
import { allTargets, evaluate } from "./eval.js";
import { differentialClassC } from "./differential.js";
import type { FormDoc, Inputs, Line, LineRef } from "./types.js";
import type { Value } from "./eval.js";
import { YEAR, YEAR_ARGS, yearPath } from "./year.js";
import { resolveInputs } from "./fixture-inputs.js";

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

// Every fixture of the year, its inputs resolved (parameter-relative ones: fixture-inputs.ts).
export function loadCases(): FixtureFile {
  const dir = yearPath("fixtures");
  const params = loadCanonical().params;
  const cases = readdirSync(dir).filter(f => /^(stage[0-9]+|classm|classm\.[a-z]+)\.json$/.test(f)).sort().flatMap(f => (JSON.parse(readFileSync(join(dir,f),"utf8")) as FixtureFile).cases);
  return { tax_year: YEAR, cases: cases.map(c => ({ ...c, inputs: resolveInputs(c.inputs, params, c.id) })) };
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

// The engine differential's summary (tools/engines/compare.py), read for the E column.
interface EngineLineStats { project_line: string | null; compared: number; compared_nonzero: number; excluded: number; excluded_nonzero: number; unexplained: number }
interface EngineSummary { cases: number; engines: Record<string, { version: string; pass_through: { lines: string[]; components: Record<string, string> }; lines: Record<string, EngineLineStats> }> }

const ENGINE_SHORT: Record<string, string> = { "PolicyEngine-US": "PE", "Tax-Calculator": "TC" };
const ENGINE_MIN_NONZERO = 50;

// An engine asserts a line when it computes the line rather than taking it whole as an input, the
// project value was nonzero on at least ENGINE_MIN_NONZERO compared returns, and fewer than half of
// the nonzero returns the engine reached (compared or excluded) were excluded under a limitation.
function engineAsserts(stats: EngineLineStats, passThroughLines: string[], mapped: string): boolean {
  if (stats.project_line === null || passThroughLines.includes(mapped)) return false;
  const reached = stats.compared_nonzero + stats.excluded_nonzero;
  return stats.compared_nonzero >= ENGINE_MIN_NONZERO && stats.excluded_nonzero * 2 < reached;
}

// The model a class M fixture records in its note, or undefined when the note names none.
function classMModel(note: string | undefined): string | undefined {
  return note?.match(/Class M: ([^;]+);/)?.[1]?.trim();
}

export function evidenceReport(): void {
  const data = loadCanonical();
  const file = loadCases();
  // H is a source reading, not a human-computed expected value (class B).
  // The same validator runs in check_logs.py; stale, unresolved or unsigned
  // readings cannot silently acquire credit when this command runs alone.
  interface HumanCredit { reader: string; log: string; via: string }
  interface HumanReadings { lines: Record<string, HumanCredit[]>; pending: string[]; problems: string[] }
  const humanRun = spawnSync("python3", [join(ROOT, "tools/human_review/logs.py"), ...YEAR_ARGS],
    { encoding: "utf-8", maxBuffer: 16 * 1024 * 1024 });
  if (humanRun.status !== 0) throw new Error(`human reading validation failed: ${humanRun.stderr}`);
  const human = JSON.parse(humanRun.stdout) as HumanReadings;
  if (human.problems.length) throw new Error(`human reading validation failed:\n${human.problems.join("\n")}`);
  const template = (key: string) => key.includes("[") ? key.replace(/(?:[a-zA-Z0-9_]+\[[^\]]+\]\.)+/g, m => m.split(".").filter(Boolean).at(-1)!.split("[")[0]+".") : key;
  interface Classes { A: Set<string>; B: Set<string>; C: Set<string>; M: Set<string>; R: Set<string> }
  const coverage = new Map<string, Classes>();
  // Class M fixtures whose recorded model is not a Claude model, per line.
  const secondFamilyM = new Map<string, Set<string>>();
  for (const doc of [...data.forms, ...data.defs]) {
    for (const line of doc.lines) { coverage.set(line.id, { A: new Set(), B: new Set(), C: new Set(), M: new Set(), R: new Set() }); secondFamilyM.set(line.id, new Set()); }
  }
  const unknownKeys = new Set<string>();
  const supplied = new Map<string, number>();
  const isInput = new Map<string, boolean>();
  const isComputed = new Map<string, boolean>();
  for (const doc of [...data.forms, ...data.defs]) for (const line of doc.lines) {
    isInput.set(line.id, line.expr.op === "input");
    isComputed.set(line.id, line.expr.op !== "input" && line.expr.op !== "param" && line.expr.op !== "copy");
  }
  // A copy's value equals its source's exactly, so an outside-family assertion (B, second-family M or E)
  // on a copy line is also credited to the first non-copy line along its copy chain. A string reference
  // resolves within the line's own document, then in the document named by the id's prefix before the
  // first dot (as the evaluator does); a def-instance reference, or a name that is a def parameter rather
  // than a line, has no single line and leaves the chain unresolved, as does a cycle.
  const docs = [...data.forms, ...data.defs];
  const byDocId = new Map(docs.map(d => [d.id, d] as const));
  const resolveRef = (from: FormDoc, ref: LineRef): { line: Line; doc: FormDoc } | undefined => {
    if (typeof ref !== "string") return undefined;
    const own = from.lines.find(l => l.id === ref);
    if (own) return { line: own, doc: from };
    const dot = ref.indexOf(".");
    const target = dot > 0 ? byDocId.get(ref.slice(0, dot)) : undefined;
    const line = target?.lines.find(l => l.id === ref);
    return line && target ? { line, doc: target } : undefined;
  };
  // The copy lines walked (the asserted line first) and the non-copy line reached, or null when unresolved.
  const copySource = (line: Line, doc: FormDoc): { path: string[]; source: string | null } => {
    const path: string[] = [];
    const seen = new Set<string>();
    let cur: { line: Line; doc: FormDoc } | undefined = { line, doc };
    while (cur && cur.line.expr.op === "copy") {
      if (seen.has(cur.line.id)) return { path, source: null };
      seen.add(cur.line.id);
      path.push(cur.line.id);
      cur = resolveRef(cur.doc, cur.line.expr.from);
    }
    return { path, source: cur ? cur.line.id : null };
  };
  for (const c of file.cases) {
    const ev = (c.evidence ?? "").trim();
    const first = ev.charAt(0);
    const cls: keyof Classes = first === "A" || first === "B" || first === "C" || first === "M" ? first : "R";
    const model = cls === "M" ? classMModel(c.evidence_note) : undefined;
    const secondFamily = model !== undefined && !/^claude/i.test(model);
    for (const key of Object.keys(c.inputs ?? {})) {
      if (key.startsWith("$")) continue;
      const id = template(key);
      supplied.set(id, (supplied.get(id) ?? 0) + 1);
    }
    for (const key of Object.keys(c.expect ?? {})) {
      if (key.startsWith("$")) continue;
      const id = template(key);
      const bucket = coverage.get(id);
      if (!bucket) { unknownKeys.add(key); continue; }
      bucket[cls].add(c.id);
      if (secondFamily) secondFamilyM.get(id)!.add(c.id);
    }
  }
  for (const [key, who] of differentialClassC()) {
    const bucket = coverage.get(template(key));
    if (bucket) for (const w of who) bucket.C.add(w);
  }
  // Engine differential: per line, the cell text and whether any engine asserts it.
  const summaryPath = yearPath("reports", "engine_differential.json");
  const summary: EngineSummary | null = existsSync(summaryPath) ? JSON.parse(readFileSync(summaryPath, "utf8")) as EngineSummary : null;
  const engineCells = new Map<string, string[]>();
  const engineAsserted = new Set<string>();
  // Per line, the short names of the engines that assert it.
  const engineAssertedBy = new Map<string, string[]>();
  const passThroughNotes: string[] = [];
  const virtualLines: string[] = [];
  if (summary) {
    for (const [name, eng] of Object.entries(summary.engines)) {
      const short = ENGINE_SHORT[name] ?? name;
      for (const [mapped, stats] of Object.entries(eng.lines)) {
        if (stats.project_line === null) { virtualLines.push(`${mapped} (${short})`); continue; }
        if (!coverage.has(stats.project_line)) { unknownKeys.add(mapped); continue; }
        const asserts = engineAsserts(stats, eng.pass_through.lines, mapped);
        if (asserts) { engineAsserted.add(stats.project_line); engineAssertedBy.set(stats.project_line, [...(engineAssertedBy.get(stats.project_line) ?? []), short]); }
        const counts = `${stats.compared} compared (${stats.compared_nonzero} nonzero), ${stats.excluded} excluded${stats.unexplained > 0 ? `, ${stats.unexplained} UNEXPLAINED` : ""}`;
        const cells = engineCells.get(stats.project_line) ?? [];
        cells.push(asserts ? `${short}: ${counts}` : `${short} below rule: ${counts}`);
        engineCells.set(stats.project_line, cells);
      }
      for (const line of eng.pass_through.lines) passThroughNotes.push(`${name} takes ${line} whole as an input`);
      for (const [line, note] of Object.entries(eng.pass_through.components)) passThroughNotes.push(`${name} ${line}: ${note}`);
    }
  }
  // Credits through copies: source line id -> "via" label (the copy chain walked) -> what is credited.
  const creditB = new Map<string, Map<string, Set<string>>>();
  const creditM2 = new Map<string, Map<string, Set<string>>>();
  const creditE = new Map<string, Map<string, string[]>>();
  let creditedB = 0, creditedM2 = 0, creditedE = 0, unresolvedAssertions = 0;
  const unresolvedCopies: string[] = [];
  const eSourcesGained: string[] = [];
  for (const doc of docs) for (const l of doc.lines) {
    if (l.expr.op !== "copy") continue;
    const b = coverage.get(l.id)!.B, m2 = secondFamilyM.get(l.id)!, e = engineAssertedBy.get(l.id) ?? [];
    const n = b.size + m2.size + e.length;
    if (n === 0) continue;
    const { path, source } = copySource(l, doc);
    if (source === null) { unresolvedAssertions += n; unresolvedCopies.push(l.id); continue; }
    const via = path.join(" → ");
    if (b.size) { creditedB += b.size; const m = creditB.get(source) ?? new Map<string, Set<string>>(); m.set(via, b); creditB.set(source, m); }
    if (m2.size) { creditedM2 += m2.size; const m = creditM2.get(source) ?? new Map<string, Set<string>>(); m.set(via, m2); creditM2.set(source, m); }
    if (e.length) {
      creditedE += e.length;
      if (!engineAsserted.has(source) && !creditE.has(source)) eSourcesGained.push(source);
      const m = creditE.get(source) ?? new Map<string, string[]>(); m.set(via, e); creditE.set(source, m);
    }
  }
  const creditedOutside = (id: string) => creditB.has(id) || creditM2.has(id) || creditE.has(id);
  // Scoreboard: computed lines with at least one assertion from outside the Claude family.
  let computedN = 0, outside = 0, bLines = 0, hLines = 0, m2Lines = 0, eLines = 0;
  for (const doc of docs) for (const l of doc.lines) {
    if (!isComputed.get(l.id)) continue;
    computedN++;
    const hasB = coverage.get(l.id)!.B.size > 0 || creditB.has(l.id), hasM2 = secondFamilyM.get(l.id)!.size > 0 || creditM2.has(l.id), hasE = engineAsserted.has(l.id) || creditE.has(l.id);
    if (hasB) bLines++;
    const hasH = (human.lines[l.id]?.length ?? 0) > 0;
    if (hasH) hLines++;
    if (hasM2) m2Lines++;
    if (hasE) eLines++;
    if (hasB || hasH || hasM2 || hasE) outside++;
  }
  const pct = computedN === 0 ? "0.0" : (100 * outside / computedN).toFixed(1);
  const linesWith = (cls: keyof Classes) => [...coverage.values()].filter(b => b[cls].size > 0).length;
  const noneYet = (n: number) => n === 0 ? "none yet" : `${n} lines`;
  const scoreboard = `Share of computed lines with at least one outside-family assertion: ${outside} of ${computedN} (${pct}%). H (human source reading): ${hLines}, B (human worked values): ${bLines}, second-family M: ${m2Lines}, E: ${eLines}.`;
  const out: string[] = [];
  out.push("# Evidence coverage per line", "");
  out.push(`**Scoreboard.** ${scoreboard}`, "");
  out.push("A computed line is one whose atom is not `input`, `param` or `copy`. An outside-family assertion is a signed human source reading (H), a class B fixture (human worked values), a class M fixture whose recorded model is not a Claude model (second-family M), or an engine assertion (E) under the rule below. The sub-counts overlap: a line with several kinds counts once in the share. H checks the encoded rule against IRS text; B and M check worked values. Second-family transcription and render readings are reported separately in second_family.md and do not yet enter this scoreboard. Class A, Claude-family M, C and R do not move it.", "");
  out.push("H — a MATCH verdict and a reason in the reader's own words, with a current per-line receipt covering the displayed reading, folded helpers, dependencies and sources. The log's exact contents must have been committed by its named reader. A guided question credits only its own computation. Other packets credit their printed line and helpers actually expanded in the reading; referenced amounts do not receive credit. See the linked human logs for the scope of each reading. H supplies no hand-calculated expected value and never fills the B column.", "");
  if (human.pending.length) out.push("Optional human readings pending or ineligible (no H credit; original findings retained): " + human.pending.join("; ") + ".", "");
  out.push(`Fixtures that assert each line, by evidence class, as a count of cases (ids listed when two or fewer). A — official IRS worked example, cited. B — human hand-work recorded with the worker and the document revision; ${noneYet(linesWith("B"))}. C — a named, versioned calculator or engine record in fixtures/${YEAR}/differential/ (spec 6.1); ${noneYet(linesWith("C"))}. M — isolated model hand-work with the model, prompt hash and snapshot recorded (fixtures/${YEAR}/classm.json, reviews/${YEAR}/classm/); second-family M fixtures are those whose recorded model does not start with "claude". E — the engine differential (tools/engines; reports/${YEAR}/engine_differential.md and .json): ${summary ? Object.keys(summary.engines).map((n) => ENGINE_SHORT[n] ? `${n} (${ENGINE_SHORT[n]})` : n).join(", ") : "the engines"} run over ${summary ? summary.cases : "no"} generated returns. A line gets an E assertion only when, for at least one engine, the engine computes the line rather than taking it whole as an input, the project value was nonzero on at least ${ENGINE_MIN_NONZERO} compared returns, and fewer than half of the nonzero returns the engine reached (compared plus excluded) were excluded under an engine limitation; the cell prints each engine's compared, nonzero and excluded counts, and an engine that falls short of the rule is marked "below rule" and asserts nothing. R — recorded regression from the project's own evaluator, no class claimed; agreement with the Lean reference evaluator (reports/${YEAR}/evaluator_agreement.md) is evaluator agreement over the same data, not an independent engine, and earns no class.`, "");
  out.push(`An outside-family assertion (B, second-family M or E) on a line whose atom is \`copy\` also credits the first line along its copy chain whose atom is not \`copy\`, because a copy's value equals its source's exactly, so agreement on the copy is agreement on the source; the table marks each such credit "via <copy line>" (the chain walked, when longer than one copy), the copy line keeps its own cell, and the sub-counts above include credited lines. In this report ${creditedB + creditedM2 + creditedE === 0 ? "no assertion is" : `${creditedB + creditedM2 + creditedE} assertions are`} credited through copies (B cases: ${creditedB}; second-family M cases: ${creditedM2}; engine-line assertions: ${creditedE}); ${unresolvedAssertions === 0 ? "every asserted copy line resolved to a source" : `${unresolvedAssertions} assertions on ${unresolvedCopies.length} copy lines could not be resolved statically and stay on the copy line only (${unresolvedCopies.join(", ")})`}.`, "");
  if (summary) {
    out.push(`Engine ids with no line of their own (never an E assertion): ${virtualLines.length ? virtualLines.join(", ") : "none"}. Mapped lines taken whole from the generator's facts: ${summary && Object.values(summary.engines).some(e => e.pass_through.lines.length) ? Object.entries(summary.engines).flatMap(([n, e]) => e.pass_through.lines.map(l => `${n} ${l}`)).join(", ") : "none"}. Components of compared lines that enter the engine as generator facts rather than the engine's own form arithmetic (the line still counts as engine-computed; the component does not): ${passThroughNotes.length ? passThroughNotes.join("; ") : "none"}.`, "");
  } else {
    out.push(`The engine differential summary (reports/${YEAR}/engine_differential.json) is not present, so no line carries an E assertion in this report.`, "");
  }
  const fmt = (s: Set<string>) => s.size === 0 ? "—" : `${s.size}${s.size <= 2 ? " (" + [...s].join(", ") + ")" : ""}`;
  // A class cell: the line's own cases, then each credit through a copy.
  const fmtWith = (own: Set<string>, credits: Map<string, Set<string>> | undefined) => {
    const parts = own.size ? [fmt(own)] : [];
    for (const [via, ids] of credits ?? []) parts.push(`via ${via}: ${fmt(ids)}`);
    return parts.length ? parts.join("; ") : "—";
  };
  let totalGaps = 0; const allGaps: string[] = [];
  for (const doc of [...data.forms, ...data.defs]) {
    if (doc.lines.length === 0 || !coverage.has(doc.lines[0]!.id)) continue;
    out.push(`## ${doc.title ?? doc.id}`, "");
    out.push("| line | A | B | C | M | H | E | R |", "| --- | --- | --- | --- | --- | --- | --- | --- |");
    const gaps: string[] = [];
    for (const l of doc.lines) {
      const b = coverage.get(l.id)!;
      const asserted = b.A.size + b.B.size + b.C.size + b.M.size + b.R.size > 0 || engineAsserted.has(l.id) || creditedOutside(l.id);
      if (!asserted && !isInput.get(l.id)) { gaps.push(l.id); allGaps.push(l.id); }
      const e = [...(engineCells.get(l.id) ?? []), ...[...(creditE.get(l.id) ?? [])].map(([via, engines]) => `E via ${via} (${engines.join(", ")})`)];
      const h = human.lines[l.id]?.map(c => `[${c.reader.replaceAll("|", "\\|")}](${c.log.replace(`reviews/${YEAR}/`, `../../reviews/${YEAR}/`)})${c.via === l.id ? "" : ` via ${c.via} (folded)`}`).join("; ") ?? "—";
      out.push(`| ${l.id} | ${fmt(b.A)} | ${fmtWith(b.B, creditB.get(l.id))} | ${fmt(b.C)} | ${fmtWith(b.M, creditM2.get(l.id))} | ${h} | ${e.length ? e.join("; ") : "—"} | ${fmt(b.R)} |`);
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
  console.log(`evidence: ${scoreboard}`);
  console.log(`evidence: credited through copies — B cases ${creditedB}, second-family M cases ${creditedM2}, engine-line assertions ${creditedE}; source lines gaining E: ${eSourcesGained.length ? eSourcesGained.join(", ") : "none"}; unresolved copy references: ${unresolvedCopies.length ? unresolvedCopies.join(", ") : "none"}`);
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
