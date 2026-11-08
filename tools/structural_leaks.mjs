#!/usr/bin/env node
// Prototype, not part of check-all: a static check for inputs that some answering order can leave reachable and
// unanswered when the interview reports a return complete (the leak the sampled `interview-rules` completion check
// finds by random traversal).
//
// Where the evaluator reads past an unknown operand to a known value (spec 4.7.2, 4.7.5):
//   - `all` / `any`: an unknown conjunct is remembered and evaluation goes on; a later deciding conjunct (`false`
//     for all, `true` for any) ends the test with a known value, and what the earlier conjunct read stays reachable.
//   - a comparison of a Count `sum_over` (or a sum or copy of one) with a constant, decided from the lower bound of
//     the known entries while an entry's field or `where` test is unknown.
// A `choose` with an unknown guard restores the memo (4.7.3), and every other atom, gate and comparison is unknown
// when an operand is unknown, so none of them leaves an input reachable past a known value.
//
// A read of line L by line R is *skippable* when it sits in conjunct i of an `all`/`any` (at any nesting level of
// the test) that has a later conjunct j not reading L, even transitively: answer j so that it decides, and the test
// is known while L is unknown. The left operand of a lower-bound count comparison is skippable the same way. Every
// other read is *strict*: L unknown makes R unknown. A read in a `choose` alternative's `then` is counted strict
// too (marked `branch`), although it needs L only where the alternative is taken; treating it as not needing L lists
// four times as many inputs, most of them reached only through a line that does need L, so it is left out.
// A line can be left unknown at completion when it is not an interview target and every read of it is skippable or
// is a strict read by a line that can itself be left unknown (the greatest such set). An input in that set that the
// targets reach is reported: an answering order that decides the skippable reads first leaves it reachable and
// unanswered while every target is known. The result is structural: whether the fixtures' answers make the later
// conjunct decide is not checked.
//
// Separately, a def instance evaluates every binding in the caller's frame, whether or not the instance's line
// reads that parameter (4.7.4). An input bound to a parameter the line does not read is reached and never needed
// there; where its other reads are on branches not taken (for example Form 8863 line 30 when the American
// opportunity credit is not claimed) it is left reachable at completion. These are listed as `binding` reads.
//
//   node tools/structural_leaks.mjs [--json] [--broad] [--why <input>]   (after a build: reads canonical/<year>/)
//   --broad   also count every input read (directly or through lines) at a skippable read: the raw
//             over-approximation, with no target or other-reader analysis.
//   --why     print, for one input template, the chain of reads from it to the skippable read that releases it,
//             or the reads that need it.
import { readFileSync } from "node:fs";
import { resolve } from "node:path";

const ROOT = resolve(import.meta.dirname, "..");
const { loadCanonical, CANON_DIR } = await import(resolve(ROOT, "engine/dist/canonical.js"));

const args = process.argv.slice(2);
const asJson = args.includes("--json");
const broad = args.includes("--broad");
const why = args.includes("--why") ? args[args.indexOf("--why") + 1] : undefined;

const data = loadCanonical();
const lines = new Map();
for (const doc of data.forms) for (const l of doc.lines) lines.set(l.id, { doc: doc.id, line: l });
const defs = new Map(data.defs.map((d) => [d.id, d]));
const isInput = (id) => lines.get(id)?.line.expr?.op === "input";

const targets = new Set();
for (const profile of ["full", "ny"]) {
  const cfg = JSON.parse(readFileSync(resolve(CANON_DIR, `interview-${profile}.json`), "utf8"));
  for (const t of cfg.targets) targets.add(t);
}

/** Line ids an expression names (strings that are line ids, anywhere in the tree), and the defs it instantiates. */
function refsOf(expr, out = new Set(), defIds = new Set()) {
  if (typeof expr === "string") { if (lines.has(expr)) out.add(expr); return { out, defIds }; }
  if (Array.isArray(expr)) { for (const x of expr) refsOf(x, out, defIds); return { out, defIds }; }
  if (expr && typeof expr === "object") {
    if (typeof expr.def === "string") defIds.add(expr.def);
    for (const v of Object.values(expr)) refsOf(v, out, defIds);
  }
  return { out, defIds };
}

/** Global lines a def's own lines name (a def reads its bindings, passed by the caller, plus any global line). */
const defMemo = new Map();
function defReads(id, seen = new Set()) {
  if (defMemo.has(id)) return defMemo.get(id);
  if (seen.has(id)) return new Set();
  seen.add(id);
  const out = new Set();
  for (const l of defs.get(id)?.lines ?? []) {
    const { out: r, defIds } = refsOf([l.expr, (l.refuses ?? []).map((x) => x.when)]);
    for (const x of r) out.add(x);
    for (const d of defIds) for (const x of defReads(d, seen)) out.add(x);
  }
  defMemo.set(id, out);
  return out;
}

/** Every line a line reads on some route: its gates and its expression, every choose alternative included. */
const directMemo = new Map();
function directReads(id) {
  if (directMemo.has(id)) return directMemo.get(id);
  const l = lines.get(id)?.line;
  const out = new Set();
  if (l) {
    const { out: r, defIds } = refsOf([l.expr, (l.refuses ?? []).map((x) => x.when)]);
    for (const x of r) out.add(x);
    for (const d of defIds) for (const x of defReads(d)) out.add(x);
    out.delete(id);
  }
  directMemo.set(id, out);
  return out;
}

const closureMemo = new Map();
/** Every line a line reads transitively, itself included. */
function closure(id) {
  if (closureMemo.has(id)) return closureMemo.get(id);
  const out = new Set([id]);
  const stack = [id];
  while (stack.length) for (const r of directReads(stack.pop())) if (!out.has(r)) { out.add(r); stack.push(r); }
  closureMemo.set(id, out);
  return out;
}
function closureOfExpr(expr) {
  const { out, defIds } = refsOf(expr);
  const s = new Set();
  for (const r of out) for (const x of closure(r)) s.add(x);
  for (const d of defIds) for (const r of defReads(d)) for (const x of closure(r)) s.add(x);
  return s;
}

/** The def-local lines (parameters included) a def's line reads transitively, itself included. */
function localClosure(defId, lineId) {
  const def = defs.get(defId);
  const local = new Map((def?.lines ?? []).map((l) => [l.id, l]));
  const out = new Set();
  const stack = [lineId];
  while (stack.length) {
    const id = stack.pop();
    if (out.has(id) || !local.has(id)) continue;
    out.add(id);
    const l = local.get(id);
    const names = [];
    const visit = (x) => { if (typeof x === "string") names.push(x); else if (Array.isArray(x)) x.forEach(visit); else if (x && typeof x === "object") { if (typeof x.def === "string") for (const v of Object.values(x.bind ?? {})) visit(v); else Object.values(x).forEach(visit); } };
    visit([l.expr, (l.refuses ?? []).map((r) => r.when)]);
    for (const n of names) if (local.has(n)) stack.push(n);
  }
  return out;
}

function countLine(id, depth = 0) {
  const l = lines.get(id)?.line;
  if (!l || depth > 6 || l.type !== "Count") return false;
  const e = l.expr;
  if (e?.op === "sum_over") return true;
  if (e?.op === "copy") return countLine(e.from ?? e.of, depth + 1);
  if (e?.op === "sum") return (e.of ?? []).some((x) => countLine(x, depth + 1));
  return false;
}

// Read sites: for each line L, every (reader, skippable, where) at which a line's gates or expression name it.
const sites = new Map();
const addSite = (l, s) => { if (!sites.has(l)) sites.set(l, []); sites.get(l).push(s); };
function walk(node, reader, levels, where, branch = false) {
  if (typeof node === "string") {
    if (!lines.has(node) || node === reader) return;
    const by = levels.find(({ ops, idx }) => ops.slice(idx + 1).some((t) => !closureOfExpr(t).has(node)));
    addSite(node, { reader, skippable: !!by, blocks: !by, kind: by ? by.kind : branch ? "branch" : "strict", where, conjunct: by ? `${by.idx}` : undefined });
    return;
  }
  if (Array.isArray(node)) { node.forEach((x) => walk(x, reader, levels, where, branch)); return; }
  if (!node || typeof node !== "object") return;
  if (node.op === "test") {
    for (const kind of ["all", "any"]) if (Array.isArray(node[kind])) {
      node[kind].forEach((t, idx) => walk(t, reader, [...levels, { ops: node[kind], idx, kind }], where, branch));
      return;
    }
    for (const k of ["gt", "ge", "lt", "le", "eq", "ne"]) {
      const pair = node[k];
      if (Array.isArray(pair) && typeof pair[0] === "string" && pair[1] && typeof pair[1] === "object" && "const" in pair[1] && countLine(pair[0])) {
        addSite(pair[0], { reader, skippable: true, blocks: false, kind: "count", where });
        walk(pair.slice(1), reader, levels, where, branch);
        return;
      }
    }
  }
  if (node.op === "choose" && Array.isArray(node.alternatives)) {
    // A guard is read when its alternative is visited; a `then` only when its alternative is taken (or is a way).
    for (const alt of node.alternatives) { walk(alt.guard, reader, levels, where, branch); walk(alt.then, reader, levels, where, true); }
    return;
  }
  if (typeof node.def === "string") {
    for (const r of defReads(node.def)) addSite(r, { reader, skippable: false, blocks: true, kind: branch ? "branch" : "strict", where: `${where} def ${node.def}` });
    // A binding is evaluated in the caller's frame whether or not the instance's line reads its parameter (4.7.4).
    const used = localClosure(node.def, node.line);
    for (const [param, v] of Object.entries(node.bind ?? {})) {
      if (used.has(param)) walk(v, reader, levels, where, branch);
      else if (typeof v === "string" && lines.has(v)) addSite(v, { reader, skippable: true, blocks: false, kind: "binding", where: `${where} def ${node.def}.${node.line} binding ${param}` });
    }
    return;
  }
  for (const [k, v] of Object.entries(node)) if (k !== "def" && k !== "line") walk(v, reader, levels, where, branch);
}
for (const [id, { line }] of lines) {
  walk(line.expr, id, [], "expr");
  (line.refuses ?? []).forEach((r, i) => walk(r.when, id, [], `refuses[${i}]`));
}

// The greatest set of lines that can be left unknown at completion.
const free = new Set([...lines.keys()].filter((id) => !targets.has(id)));
for (let changed = true; changed;) {
  changed = false;
  for (const id of [...free]) {
    if ((sites.get(id) ?? []).some((s) => s.blocks && !free.has(s.reader))) { free.delete(id); changed = true; }
  }
}

// Lines the targets reach on some route.
const reached = new Set();
for (const t of targets) for (const x of closure(t)) reached.add(x);

/** One chain of reads from a line to a skippable read: what releases it. */
function release(id, seen = new Set()) {
  if (seen.has(id)) return undefined;
  seen.add(id);
  const ss = (sites.get(id) ?? []).filter((s) => reached.has(s.reader));
  const skip = ss.find((s) => s.skippable);
  if (skip) return [`${id} read by ${skip.reader} (${skip.kind}${skip.conjunct !== undefined ? ` conjunct ${skip.conjunct}` : ""}, ${skip.where})`];
  for (const s of ss) {
    const r = release(s.reader, seen);
    if (r) return [`${id} read by ${s.reader} (${s.where})`, ...r];
  }
  return undefined;
}

const leaks = [...free].filter((id) => isInput(id) && reached.has(id) && (sites.get(id) ?? []).length > 0).sort();
const rows = leaks.map((id) => {
  const chain = release(id) ?? [];
  const at = chain.length ? chain[chain.length - 1].split(" read by ")[1].split(" ")[0] : "";
  return { input: id, releasedAt: at, kind: chain.length && / \(count/.test(chain[chain.length - 1]) ? "count" : "conjunction", chain };
});

if (why) {
  const r = rows.find((x) => x.input === why);
  if (!r) {
    const bad = (sites.get(why) ?? []).filter((s) => s.blocks && !free.has(s.reader));
    console.log(`${why}: not reported${!reached.has(why) ? " (the targets do not reach it)" : ""}${bad.length ? `; needed by ${bad.slice(0, 5).map((s) => `${s.reader} (${s.where})`).join(", ")}` : ""}`);
  } else console.log(r.chain.join("\n  "));
} else if (!asJson) {
  console.log(`structural leaks: ${rows.length} inputs can be left reachable and unanswered at completion (${rows.filter((r) => r.kind === "count").length} through a count lower bound); targets ${targets.size}, lines ${lines.size}`);
  for (const r of rows) console.log(`${r.input.padEnd(44)} released at ${r.releasedAt} (${r.kind}; ${r.chain.length - 1} line(s) between)`);
}

const bindings = [];
for (const [id, ss] of sites) for (const x of ss) if (x.kind === "binding" && reached.has(x.reader)) for (const i of closure(id)) if (isInput(i)) bindings.push({ input: i, reader: x.reader, where: x.where });
if (!asJson && !why) {
  console.log(`binding reads: ${new Set(bindings.map((b) => b.input)).size} inputs bound to a def parameter the instance's line does not read`);
  for (const b of bindings) console.log(`${b.input.padEnd(44)} at ${b.reader} (${b.where})`);
}

if (broad) {
  const raw = new Set();
  for (const [id, ss] of sites) if (isInput(id) && ss.some((s) => s.skippable && s.kind !== "count")) raw.add(id);
  for (const [id, ss] of sites) if (!isInput(id) && ss.some((s) => s.skippable)) for (const x of closure(id)) if (isInput(x)) raw.add(x);
  console.log(`broad: ${raw.size} inputs read (directly or through lines) at a skippable read`);
}
if (asJson && !why) console.log(JSON.stringify({ conjunctions: rows, bindings }, null, 1));
