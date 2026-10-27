// Executable triage of transcription disagreements: evaluate the project's line and the model's
// validated candidate line on the same inputs and report where their values differ.
// Agreement on these inputs is observed equivalence on a sample, not a proof.
// No model-generated JavaScript, commands, tools, paths or network calls are executed.
import { readFileSync } from 'node:fs';
import { executableCandidate } from './candidate_runtime.mjs';
import { evaluate, allTargets } from '../../engine/dist/eval.js';
import { loadCases } from '../../engine/dist/fixtures.js';
import { sampleReturns } from '../../engine/dist/generate.js';
import { loadInterview } from '../../engine/dist/interview.js';

const { context, form, lines, pairs, ownInputs, generated, seed, partialBases, maxWitnesses, explain } = JSON.parse(readFileSync(0, 'utf8'));
const { runtime, errors } = executableCandidate(context, form, lines);
// Output is written once at the end; exiting right after a large piped write can truncate it.
main: {
if (errors.length) {
  process.stdout.write(JSON.stringify({ state: 'invalid', errors }));
  break main;
}
const isDef = context.defs.some(doc => doc.id === form);
// The whole-return interview's targets: a return is refused only when one of them is refused, so
// a refusal on a helper the interview never reaches does not stand in for a refused return.
const returnTargets = loadInterview('full').targets;
function returnState(inputs) {
  const values = evaluate(context, inputs, returnTargets).values;
  const states = returnTargets.map(target => values.get(target)?.kind ?? 'unknown');
  return states.includes('refusal') ? 'refused' : states.includes('unknown') ? 'incomplete' : 'completed';
}

// A value key names a line of the reviewed document when its prefix is the document itself, one
// of its collection entries, or an invocation of the shared definition. Local ids may contain dots.
const escaped = form.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
function ownPrefix(prefix) {
  if (prefix === form || new RegExp(`(^|\\.)${escaped}\\[[^\\]]*\\]$`).test(prefix)) return true;
  const instance = prefix.lastIndexOf('|inst:');
  return instance >= 0 && prefix.startsWith(`|inst:${form}#`, instance);
}

const localOf = id => id.startsWith(`${form}.`) ? id.slice(form.length + 1) : id;
const byProject = new Map(pairs.map(pair => [localOf(pair.project), pair]));
const byCandidate = new Map(pairs.filter(pair => pair.candidate).map(pair => [localOf(pair.candidate), pair]));

function targets(data, inputs) {
  const all = allTargets(data, inputs);
  const mine = new RegExp(`(^|\\.)${escaped}(\\[[^\\]]*\\])?\\.[^\\[\\]]+$`);
  return isDef ? all : all.filter(key => mine.test(key));
}

function collect(values, index) {
  const locals = [...index.keys()].sort((a, b) => b.length - a.length);
  const found = new Map();
  for (const [key, value] of values) {
    for (const local of locals) {
      if (!key.endsWith(`.${local}`)) continue;
      const prefix = key.slice(0, key.length - local.length - 1);
      if (!ownPrefix(prefix)) continue;
      found.set(`${index.get(local).handle}\u0000${prefix}`, value);
      break;
    }
  }
  return found;
}

const blank = v => v && ((v.kind === 'money' && v.cents === 0) || (v.kind === 'bool' && !v.value) || (v.kind === 'count' && v.value === 0));
function shape(value) {
  if (!value) return { kind: 'absent' };
  if (value.kind === 'refusal') return { kind: 'refusal' };
  if (value.kind === 'unknown') return { kind: 'unknown' };
  return value;
}

const same = (a, b) => a?.kind === 'hidden' ? blank(b) || b?.kind === 'hidden' : JSON.stringify(shape(a)) === JSON.stringify(shape(b));
// Kinds name the side that is narrower: a refusal outranks an unknown, as in the evaluator.
const difference = (a, b) => {
  if (a?.kind === 'hidden') return b?.kind === 'refusal' ? 'candidate-refuses' : b?.kind === 'unknown' ? 'candidate-unknown' : 'candidate-shows-skipped';
  const [x, y] = [shape(a).kind, shape(b).kind];
  if (x === 'refusal' || y === 'refusal') return x === 'refusal' && y === 'refusal' ? 'value' : x === 'refusal' ? 'project-refuses' : 'candidate-refuses';
  if (x === 'unknown' || y === 'unknown') return x === 'unknown' ? 'project-unknown' : 'candidate-unknown';
  return 'value';
};

function operands(derivations, key) {
  const d = derivations.get(key);
  return d ? d.operands.slice(0, 12).map(op => ({ ref: op.ref, value: op.value })) : [];
}

const stats = new Map(pairs.map(pair => [pair.handle, { handle: pair.handle, project: pair.project, candidate: pair.candidate, shown_when: pair.shown_when ?? null,
  compared: 0, agree: 0, differ: 0, absent: 0, in_scope: 0, in_scope_agree: 0, kinds: {}, kinds_by_return: {}, sources: {}, witnesses: [] }]));
const known = value => value && !['refusal', 'unknown'].includes(value.kind);

function run(source, inputs) {
  let project, model;
  try {
    project = evaluate(context, inputs, targets(context, inputs));
    model = evaluate(runtime, inputs, targets(runtime, inputs));
  } catch (error) {
    return { reached: false, error: String(error.message ?? error).slice(0, 300) };
  }
  const p = collect(project.values, byProject), m = collect(model.values, byCandidate);
  // A project line hidden by its shown_when shows no amount: compare what the filer sees.
  for (const [key, value] of p) {
    const [handle, prefix] = key.split('\u0000');
    const cond = stats.get(handle).shown_when;
    if (!cond) continue;
    const c = project.values.get(`${prefix}.${localOf(cond)}`);
    if (c?.kind === 'bool' && !c.value) p.set(key, { kind: 'hidden' });
  }
  let reached = false, whole = null;
  for (const key of new Set([...p.keys(), ...m.keys()])) {
    const [handle, prefix] = key.split('\u0000');
    const s = stats.get(handle);
    const a = p.get(key), b = m.get(key);
    if (!a || !b) { s.absent += 1; continue; }
    if (known(a) || a.kind === 'hidden') reached = true;
    s.compared += 1;
    s.sources[source.kind] = (s.sources[source.kind] ?? 0) + 1;
    const inScope = a.kind !== 'refusal' && b.kind !== 'refusal';
    if (inScope) s.in_scope += 1;
    if (same(a, b)) { s.agree += 1; if (inScope) s.in_scope_agree += 1; continue; }
    s.differ += 1;
    const kind = difference(a, b);
    s.kinds[kind] = (s.kinds[kind] ?? 0) + 1;
    whole ??= returnState(inputs);
    s.kinds_by_return[whole] ??= {};
    s.kinds_by_return[whole][kind] = (s.kinds_by_return[whole][kind] ?? 0) + 1;
    const sameKind = s.witnesses.filter(w => w.kind === kind).length;
    if (sameKind < maxWitnesses) {
      const pair = stats.get(handle);
      s.witnesses.push({ kind, source, instance: prefix, project_return: whole, project: a, candidate: b,
        project_operands: operands(project.derivations, `${prefix}.${localOf(pair.project)}`),
        candidate_operands: operands(model.derivations, `${prefix}.${localOf(pair.candidate)}`) });
    }
  }
  return { reached };
}

// Explain one witness: rebuild its inputs and print both derivation trees for the disputed line.
function witnessInputs(source, fixtures) {
  if (source.kind === 'fixture') return fixtures.find(test => test.id === source.id).inputs;
  if (source.kind === 'generated') return sampleReturns(context, source.index + 1, source.seed)[source.index];
  const base = /^generated (\d+)\/(\d+)$/.exec(source.base);
  const inputs = base ? sampleReturns(context, Number(base[2]) + 1, Number(base[1]))[Number(base[2])]
    : fixtures.find(test => test.id === source.base).inputs;
  const { [source.withheld]: _, ...rest } = inputs;
  return rest;
}
function tree(derivations, key, depth, budget, used) {
  const d = derivations.get(key);
  if (!d) return { line: key, value: 'not evaluated' };
  const node = { line: key, op: d.op, value: d.value };
  if (d.op === 'input') used.add(key);
  if (d.notes?.length) node.notes = d.notes;
  if (d.takenGuardIndex !== undefined) node.taken_guard = d.takenGuardIndex;
  if (depth > 0 && budget.left > 0 && d.operands.length) {
    node.operands = d.operands.filter(op => derivations.has(op.ref) || op.ref.includes('.') || op.ref.includes('[')).map(op => { budget.left -= 1; return budget.left > 0 ? tree(derivations, op.ref, depth - 1, budget, used) : { line: op.ref, value: op.value }; });
  }
  return node;
}
if (explain) {
  const fixtures = loadCases().cases;
  const inputs = witnessInputs(explain.source, fixtures);
  const pair = pairs.find(p => p.handle === explain.handle);
  const project = evaluate(context, inputs, targets(context, inputs));
  const model = evaluate(runtime, inputs, targets(runtime, inputs));
  const usedP = new Set(), usedM = new Set();
  const closure = (derivations, key, used, seen = new Set()) => {
    if (seen.has(key)) return;
    seen.add(key);
    const d = derivations.get(key);
    if (!d) return;
    if (d.op === 'input') used.add(key);
    for (const op of d.operands) closure(derivations, op.ref, used, seen);
  };
  const out = { handle: explain.handle, source: explain.source, instance: explain.instance,
    project: tree(project.derivations, `${explain.instance}.${localOf(pair.project)}`, explain.depth ?? 6, { left: 400 }, usedP),
    candidate: tree(model.derivations, `${explain.instance}.${localOf(pair.candidate)}`, explain.depth ?? 6, { left: 400 }, usedM) };
  closure(project.derivations, `${explain.instance}.${localOf(pair.project)}`, usedP);
  closure(model.derivations, `${explain.instance}.${localOf(pair.candidate)}`, usedM);
  out.inputs_read = Object.fromEntries([...new Set([...usedP, ...usedM])].sort().map(key => [key, key in inputs ? inputs[key] : '(not supplied)']));
  process.stdout.write(JSON.stringify(out, null, 1));
  break main;
}

const failures = [];
const reachedBases = [];
const fixtures = loadCases().cases;
for (const test of fixtures) {
  const result = run({ kind: 'fixture', id: test.id }, test.inputs);
  if (result.error) failures.push({ source: test.id, error: result.error });
  else if (result.reached) reachedBases.push({ id: test.id, inputs: test.inputs });
}
const sample = sampleReturns(context, generated, seed);
sample.forEach((inputs, index) => {
  const result = run({ kind: 'generated', seed, index }, inputs);
  if (result.error) failures.push({ source: `generated ${index}`, error: result.error });
  else if (result.reached && reachedBases.length < 4 * partialBases) reachedBases.push({ id: `generated ${seed}/${index}`, inputs });
});
// Partial records: withhold one answer the reviewed document asks, from returns that reach it.
const own = new Set(ownInputs.map(localOf));
const ownKey = key => {
  const parts = new RegExp(`^(?:.*\\.)?${escaped}(?:\\[[^\\]]*\\])?\\.([^\\[\\]]+)$`).exec(key);
  return parts && own.has(parts[1]);
};
let partials = 0;
for (const base of reachedBases.filter((_, i) => i % 4 === 0).slice(0, partialBases)) {
  for (const key of Object.keys(base.inputs).filter(ownKey)) {
    const { [key]: _, ...inputs } = base.inputs;
    partials += 1;
    const result = run({ kind: 'partial', base: base.id, withheld: key }, inputs);
    if (result.error) failures.push({ source: `${base.id} without ${key}`, error: result.error });
  }
}
process.stdout.write(JSON.stringify({ state: 'evaluated', errors: [],
  bank: { fixtures: fixtures.length, generated, seed, partial_bases: partialBases, partial_records: partials, evaluation_failures: failures.length },
  failures: failures.slice(0, 20), lines: [...stats.values()] }));
}
