// Self-test of the check rules that have no failing case in the shipped data: each rule must
// flag a constructed violation and pass the corresponding clean case.
import assert from "node:assert/strict";
import { checkExpressionTypes, registerLinkProblems, tableBandMonoProblems } from "./check.js";
import { entrySyntax } from "./interview.js";
import { gateProblems } from "./gates.js";
import { evaluate } from "./eval.js";
import type { CanonicalData, Line, RegisterEntry, TableDoc } from "./types.js";
import { flatText, indentRest, parseStructured, textSummary } from "./text.js";
import { DEFAULTS_ALONE, consistencyProblems, defaultsProblems, resolveInputs, tableOf } from "./fixture-inputs.js";
import type { CheckedCase, DefaultEntry, DefaultsFile, Rule, Test } from "./fixture-inputs.js";

function table(bands: { at_least: number; less_than: number; tax: number[] }[]): TableDoc {
  return { id: "t", kind: "tax_table", title: "t", tax_year: 2025, cite: null as never, columns: [{ key: "a", statuses: [] }, { key: "b", statuses: [] }], bands };
}

function entry(id: string, extra: Partial<RegisterEntry> = {}): RegisterEntry {
  return { id, text_at_issue: "x", readings: ["x"], chosen: "x", reason: "x", cite: null as never, ...extra };
}

function data(entries: RegisterEntry[], links: string[]): CanonicalData {
  const lines = links.map((a, i) => ({ id: `f.l${i}`, printed: "1", label: "l", type: "Dollars", expr: { op: "input", source: "x" }, cite: null, ambiguity: a }));
  return { forms: [{ id: "f", kind: "form", tax_year: 2025, title: "f", lines }], defs: [], tables: [], params: { tax_year: 2025, enums: {}, values: {} }, register: { tax_year: 2025, entries } } as unknown as CanonicalData;
}


/** A document `g` with one gate: `g.box` takes `g.box_amount` when `g.any` is true and `g.zero` (parameter z, 0) when it
 * is false; `g.total` reads the gate line. `edit` changes the lines before the data is made. */
function gated(edit: (lines: Line[]) => void = () => {}): CanonicalData {
  const eq = (v: boolean) => ({ op: "test", eq: ["g.any", { const: v }] });
  const lines = [
    { id: "g.any", printed: "1", label: "any", type: "Bool", expr: { op: "input", source: "Any?" }, cite: null },
    { id: "g.box_amount", printed: "2", label: "amount", type: "NonNegDollars", expr: { op: "input", source: "Amount?" }, cite: null, gated_by: "g.box" },
    { id: "g.box", printed: "2", label: "box", type: "NonNegDollars", expr: { op: "choose", alternatives: [{ guard: eq(true), then: "g.box_amount" }, { guard: eq(false), then: "g.zero" }] }, cite: null },
    { id: "g.zero", printed: "zero", label: "zero", type: "NonNegDollars", expr: { op: "param", ref: "z" }, cite: null },
    { id: "g.total", printed: "3", label: "total", type: "NonNegDollars", expr: { op: "sum", of: ["g.box"] }, cite: null },
  ] as unknown as Line[];
  edit(lines);
  return { forms: [{ id: "g", kind: "form", tax_year: 2025, title: "g", lines }], defs: [], tables: [],
    params: { tax_year: 2025, enums: {}, values: { z: { type: "NonNegDollars", value: 0, cite: null } } }, register: { tax_year: 2025, entries: [] } } as unknown as CanonicalData;
}
const line = (lines: Line[], id: string) => lines.find((l) => l.id === id)!;

/** A document `c` of Bool and enum `choose` lines (enum `cv`: a, b, c), for the checker's typing rules here and for the
 * two evaluators' agreement (compare.ts). `c.bsel` takes the screened `c.yes` when `c.flag` is true and the false
 * parameter `c.no` when it is false; `c.esel` takes the input `c.pick` when `c.kind` is a and the enum parameter
 * `c.dflt` (a) otherwise; `c.nest` is a choose on `c.yes` whose true alternative is `c.bsel`; `c.allref` takes two
 * lines that both refuse when `c.bad` is true; `c.use` tests `c.bsel`, and `c.money` is a money choose on `c.esel`.
 * `edit` changes the lines before the data is made. */
export function typedChooseData(edit: (lines: Line[]) => void = () => {}): CanonicalData {
  const cite = { doc: "c", revision: "r", locator: "p. 1", snapshot: "s" };
  const eq = (ref: string, v: boolean | string) => ({ op: "test", eq: [ref, { const: v }] });
  const choose = (ref: string, alts: [boolean | string, string][]) => ({ op: "choose", alternatives: alts.map(([v, then]) => ({ guard: eq(ref, v), then })) });
  const l = (id: string, type: string, expr: unknown, extra: object = {}) => ({ id, printed: "1", label: id, type, expr, cite, ...extra });
  const screened = { refuses: [{ when: "c.bad", form: "Screened", remedy: "Outside the test.", cite }] };
  const lines = [
    l("c.flag", "Bool", { op: "input", source: "Flag?" }),
    l("c.yes", "Bool", { op: "input", source: "Yes?" }),
    l("c.bad", "Bool", { op: "input", source: "Bad?" }),
    l("c.kind", "Enum(cv)", { op: "input", source: "Kind?" }),
    l("c.pick", "Enum(cv)", { op: "input", source: "Pick?" }),
    l("c.amount", "NonNegDollars", { op: "input", source: "Amount?" }),
    l("c.no", "Bool", { op: "param", ref: "cno" }),
    l("c.dflt", "Enum(cv)", { op: "param", ref: "cdflt" }),
    l("c.zero", "NonNegDollars", { op: "param", ref: "z" }),
    l("c.yes_screened", "Bool", { op: "copy", from: "c.yes" }, screened),
    l("c.no_screened", "Bool", { op: "copy", from: "c.no" }, screened),
    l("c.bsel", "Bool", choose("c.flag", [[true, "c.yes_screened"], [false, "c.no"]])),
    l("c.esel", "Enum(cv)", choose("c.kind", [["a", "c.pick"], ["b", "c.dflt"], ["c", "c.dflt"]])),
    l("c.nest", "Bool", choose("c.yes", [[true, "c.bsel"], [false, "c.no"]])),
    l("c.allref", "Bool", choose("c.flag", [[true, "c.yes_screened"], [false, "c.no_screened"]])),
    l("c.use", "Bool", eq("c.bsel", true)),
    l("c.money", "NonNegDollars", choose("c.esel", [["a", "c.amount"], ["b", "c.zero"], ["c", "c.zero"]])),
  ] as unknown as Line[];
  edit(lines);
  return { forms: [{ id: "c", kind: "form", tax_year: 2025, title: "c", lines }], defs: [], tables: [],
    params: { tax_year: 2025, enums: { cv: { values: ["a", "b", "c"], cite } }, values: {
      cno: { type: "Bool", value: false, cite }, cdflt: { type: "Enum(cv)", value: "a", cite }, z: { type: "NonNegDollars", value: 0, cite } } },
    register: { tax_year: 2025, entries: [] } } as unknown as CanonicalData;
}

/** Inputs for `typedChooseData` and the values the evaluator gives its choose lines (a refusal by its gate). */
export const TYPED_CHOOSE_CASES: { inputs: Record<string, unknown>; expect: Record<string, string> }[] = [
  { inputs: {}, expect: { "c.bsel": "unknown", "c.esel": "unknown", "c.allref": "unknown", "c.money": "unknown" } },
  { inputs: { "c.flag": false }, expect: { "c.bsel": "bool:false", "c.use": "bool:false", "c.allref": "unknown" } },
  { inputs: { "c.flag": false, "c.bad": true }, expect: { "c.bsel": "bool:false", "c.allref": "refusal:c.bad" } },
  // An unknown guard: every way refuses, so the line refuses; one way is a value, so the line is the guard's unknown.
  { inputs: { "c.bad": true }, expect: { "c.allref": "refusal:c.bad", "c.bsel": "unknown" } },
  { inputs: { "c.flag": true, "c.yes": true }, expect: { "c.bsel": "unknown", "c.nest": "unknown" } },
  { inputs: { "c.flag": true, "c.yes": true, "c.bad": false }, expect: { "c.bsel": "bool:true", "c.use": "bool:true", "c.nest": "bool:true", "c.allref": "bool:true" } },
  { inputs: { "c.flag": true, "c.yes": false, "c.bad": true }, expect: { "c.bsel": "refusal:c.bad", "c.nest": "bool:false", "c.use": "refusal:c.bad" } },
  { inputs: { "c.kind": "b" }, expect: { "c.esel": "enum:a", "c.money": "unknown" } },
  { inputs: { "c.kind": "a", "c.pick": "c", "c.amount": 500 }, expect: { "c.esel": "enum:c", "c.money": "money:0" } },
  { inputs: { "c.kind": "a", "c.pick": "a", "c.amount": 500 }, expect: { "c.esel": "enum:a", "c.money": "money:500" } },
  { inputs: { "c.kind": "c", "c.amount": 7 }, expect: { "c.esel": "enum:a", "c.money": "money:7" } },
];

/** A value as the typed-choose cases state it. */
export function valueText(v: { kind: string; [k: string]: unknown }): string {
  if (v.kind === "refusal") return `refusal:${String(v["gate"])}`;
  if (v.kind === "unknown") return "unknown";
  if (v.kind === "money") return `money:${String(v["cents"])}`;
  return `${v.kind}:${String(v["value"])}`;
}

/** The fixtures' test-data defaults (fixture-inputs.ts) on a small document set: a form `h`, a collection `p` and a
 * collection `w` within each entry of `p` (and a second collection `q`, a New York form `ny_n`). Conditional withholding resolves as documented, each malformed condition
 * is named, and each kind of consistency violation is found. Returns the number of cases. */
function defaultsSelfTest(): number {
  const input = (id: string, type: string) => ({ id, printed: "1", label: id, type, expr: { op: "input", source: `${id}?` }, cite: null });
  const forms = [
    { id: "h", kind: "form", tax_year: 2025, title: "h", lines: [input("h.status", "Enum(st)"), input("h.married", "Bool"), input("h.unmarried", "Bool"), input("h.gate", "Bool"), input("h.amount", "NonNegDollars")] },
    { id: "p", kind: "form", tax_year: 2025, title: "p", collection: { cite: null }, lines: [input("p.a", "Bool"), input("p.b", "Bool"), input("p.c", "Bool")] },
    { id: "w", kind: "form", tax_year: 2025, title: "w", collection: { parent: "p", cite: null }, lines: [input("w.x", "Bool")] },
    { id: "q", kind: "form", tax_year: 2025, title: "q", collection: { cite: null }, lines: [input("q.z", "Bool")] },
    { id: "ny_n", kind: "form", tax_year: 2025, title: "n", lines: [input("ny_n.q", "Bool")] },
  ];
  const data = { forms, defs: [], tables: [], params: { tax_year: 2025, enums: { st: { values: ["single", "joint", "sep", "hoh"] } }, values: {} }, register: { tax_year: 2025, entries: [] } } as unknown as CanonicalData;
  const base: [string, unknown][] = [["h.status", "single"], ["h.married", false], ["h.unmarried", false], ["h.gate", false], ["h.amount", 0], ["$p", ["one"]], ["p.a", false], ["p.b", false], ["p.c", false], ["$w", []], ["w.x", false], ["$q", []], ["q.z", false]];
  const file = (withheld: Record<string, Test[]> = {}, consistency?: Rule[]): DefaultsFile => ({ tax_year: 2025, ...(consistency ? { consistency } : {}),
    defaults: base.map(([i, value]): DefaultEntry => ({ input: i, value, reason: "r", ...(withheld[i] ? { withheld: { when: withheld[i], reason: "r" } } : {}) })) });
  const ny: DefaultsFile = { tax_year: 2025, defaults: [{ input: "ny_n.q", value: false, reason: "r" }] };
  let n = 0;

  // Resolution: a default is withheld where its condition holds on the stated and defaulted answers, and only there.
  const when = {
    "h.married": [{ input: "h.status", in: ["joint", "sep"] }], "h.unmarried": [{ input: "h.status", not: "hoh" }],
    "p.b": [{ count: "$p", is: 1 }], "p.c": [{ input: "p.a", is: true }, { input: "h.gate", is: false }], "w.x": [{ input: "p.a", is: true }, { count: "$w", is: 2 }],
  };
  const table = tableOf(file(when));
  const resolved = (inputs: Record<string, unknown>) => resolveInputs(inputs, data, "self-test", "federal", table);
  const absent: [string, Record<string, unknown>, string[], string[]][] = [
    ["nothing stated", {}, ["h.unmarried", "p[one].b"], ["h.married", "p[one].c"]],
    ["a membership test on a stated answer", { "h.status": "joint" }, ["h.married", "h.unmarried"], []],
    ["a stated answer is never withheld", { "h.status": "sep", "h.married": false, "h.unmarried": true }, [], ["h.married", "h.unmarried"]],
    ["a test on an unknown answer does not hold", { "h.status": null }, ["h.status"], ["h.married", "h.unmarried"]],
    ["'not' on a known answer", { "h.status": "hoh" }, [], ["h.married", "h.unmarried"]],
    ["a count of the entry's own roster", { "$p": ["a", "b"] }, [], ["p[a].b", "p[b].b"]],
    ["tests on the same entry and on a top-level answer", { "$p": ["a", "b"], "p[a].a": true }, ["p[a].c"], ["p[b].c"]],
    ["all the tests must hold", { "p[one].a": true, "h.gate": true }, [], ["p[one].c"]],
    ["a test on the enclosing entry and a count of the nested roster", { "$p": ["a", "b"], "p[a].a": true, "$w@p[a]": ["x", "y"], "$w@p[b]": ["x", "y"] }, ["p[a].w[x].x", "p[a].w[y].x"], ["p[b].w[x].x", "p[b].w[y].x"]],
    ["the nested count is read per enclosing entry", { "p[one].a": true, "$w@p[one]": ["x"] }, [], ["p[one].w[x].x"]],
  ];
  for (const [name, inputs, gone, kept] of absent) {
    const out = resolved(inputs);
    for (const k of gone) assert.ok(!(k in out), `defaults: ${name}: ${k} should be left out`);
    for (const k of kept) assert.ok(k in out, `defaults: ${name}: ${k} should be given`);
    n++;
  }

  // Validation: each malformed condition or rule is named; the well-formed file has no problem.
  const problems = (f: DefaultsFile) => defaultsProblems(data, { federal: f, ny }).join("\n");
  assert.equal(problems(file(when, [{ never: [{ input: "p.a", is: true }, { input: "w.x", is: true }, { input: "h.gate", is: false }], reason: "r", open: { "some.case": "r" } }])), "");
  const bad: [string, DefaultsFile, RegExp][] = [
    ["an unknown input", file({ "h.married": [{ input: "h.nope", is: true }] }), /h\.married withheld: the test on h\.nope: h\.nope is not a declared input/],
    ["a roster named as an input", file({ "h.married": [{ input: "$p", is: 1 }] }), /\$p is not a declared input/],
    ["an input named as a count", file({ "h.married": [{ count: "p.a", is: 1 }] }), /p\.a is not a declared roster/],
    ["the default's own input", file({ "h.married": [{ input: "h.married", is: true }] }), /reads the default's own input/],
    ["an input whose default is conditional", file({ "h.married": [{ input: "h.status", is: "joint" }], "h.unmarried": [{ input: "h.married", is: true }] }), /h\.unmarried withheld: the test on h\.married reads an input whose own default is conditional, which is resolved later/],
    ["a value the enum does not have", file({ "h.married": [{ input: "h.status", in: ["joint", "widowed"] }] }), /"widowed": not a value of Enum\(st\); the test can never hold/],
    ["a value of the wrong type", file({ "h.married": [{ input: "h.gate", is: 1 }] }), /1: not a Bool; the test can never hold/],
    ["a count that is not a whole number", file({ "p.b": [{ count: "$p", is: -1 }] }), /a count is a whole number, 0 or more/],
    ["an answer tested twice", file({ "h.married": [{ input: "h.status", is: "joint" }, { input: "h.status", is: "sep" }] }), /is the second on that answer/],
    ["a count of 0 of the entry's own roster", file({ "p.b": [{ count: "$p", is: 0 }] }), /can never hold: the roster lists the entry itself/],
    ["an empty membership list", file({ "h.married": [{ input: "h.status", in: [] }] }), /"in" is a list of distinct values/],
    ["two comparisons in one test", file({ "h.married": [{ input: "h.status", is: "joint", not: "sep" }] }), /needs exactly one of "is", "in" and "not"/],
    ["no tests", file({ "h.married": [] }), /a condition is a list of at least one test/],
    ["an entry's answer read from a top-level default", file({ "h.married": [{ input: "p.a", is: true }] }), /reads an entry of p, which h\.married cannot be read beside/],
    ["a nested entry's answer read from the enclosing entry", file({ "p.b": [{ input: "w.x", is: true }] }), /reads an entry of w, which p\.b cannot be read beside/],
    ["a New York answer read from the federal defaults", file({ "h.married": [{ input: "ny_n.q", is: true }] }), /reads a New York answer from the federal defaults/],
    ["a roster's default withheld", file({ "$p": [{ input: "h.gate", is: true }] }), /\$p: a roster's default cannot be withheld/],
    ["a rule of one test", file({}, [{ never: [{ input: "h.gate", is: true }], reason: "r" }]), /consistency rule 1 needs at least two tests/],
    ["a rule without a reason", file({}, [{ never: [{ input: "h.gate", is: true }, { input: "h.amount", not: 0 }], reason: "" }]), /consistency rule 1 holds "never" \(the tests\), a one-line "reason"/],
    ["a rule whose open list is not reasons", file({}, [{ never: [{ input: "h.gate", is: true }, { input: "h.amount", not: 0 }], reason: "r", open: { c: "" } }]), /"open" maps a case id to a one-line reason/],
    ["a rule across two entries that are not nested", file({}, [{ never: [{ input: "p.a", is: true }, { input: "q.z", is: true }], reason: "r" }]), /consistency rule 1: the test on q\.z reads an entry of q, which the rule's other tests cannot be read beside/],
  ];
  for (const [name, f, re] of bad) { assert.match(problems(f), re, `defaults: not refused: ${name}`); n++; }
  const withReason = file(when);
  (withReason.defaults.find((d) => d.input === "h.married")!.withheld as { reason?: string }).reason = "";
  assert.match(problems(withReason), /h\.married: "withheld" holds "when" \(the tests\) and a one-line "reason"/);
  n++;

  // Consistency: a planted violation of each kind is found; what is stated on purpose, listed as open, or not read is not.
  const pair: Rule = { never: [{ input: "h.married", is: false }, { input: "h.unmarried", is: false }], reason: "married or unmarried." };
  const gate: Rule = { never: [{ input: "h.gate", is: false }, { input: "h.amount", not: 0 }], reason: "an amount needs its gate." };
  const group: Rule = { never: [{ input: "p.a", is: true }, { input: "p.b", is: false }, { input: "p.c", is: false }], reason: "a means b or c." };
  const alone: Rule = { never: [{ input: "p.a", is: false }, { input: "p.c", is: false }], reason: "a or c." };
  const kase = (id: string, inputs: Record<string, unknown>, f = "h.json"): CheckedCase => ({ id, file: f, j: "federal", inputs });
  const found = (rules: Rule[], cases: CheckedCase[], withheld: Record<string, Test[]> = {}) => consistencyProblems(data, { federal: file(withheld, rules), ny: null }, cases).join("\n");
  const unmarriedSingle = { "h.unmarried": [{ input: "h.status", is: "single" }] };
  const planted: [string, string, RegExp | null][] = [
    ["a pair: one stated, one a default", found([pair], [kase("c1", { "h.status": "joint", "h.married": false })], unmarriedSingle), /^c1: takes the default of h\.unmarried \(false\) against h\.married false; .*consistency rule 1: married or unmarried\./],
    ["a pair: both defaults, where a condition did not hold", found([pair], [kase("c1", { "h.status": null }), kase("c2", {})], unmarriedSingle), /^c1: takes the default of h\.married \(false\) and h\.unmarried \(false\) against its other defaults/],
    ["a pair: both stated is a scenario, not a default", found([pair], [kase("c1", { "h.status": "hoh", "h.married": false, "h.unmarried": false }), kase("c2", {})], unmarriedSingle), null],
    ["a gate: the amount stated, the gate a default", found([gate], [kase("c1", { "h.amount": 5 })]), /^c1: takes the default of h\.gate \(false\) against h\.amount 5; .*an amount needs its gate\./],
    ["a gate: answered in the case", found([gate], [kase("c1", { "h.amount": 5, "h.gate": true }), kase("c2", { "h.amount": 0 })]), null],
    ["a group, read entry by entry", found([group], [kase("c1", { "$p": ["x", "y"], "p[y].a": true })]), /^c1: takes the default of p\[y\]\.b \(false\) and p\[y\]\.c \(false\) against p\[y\]\.a true/],
    ["a case that takes no defaults is not read", found([gate], [kase("c1", { "h.amount": 5 }, "mutation.json")]), null],
    ["a case listed as open", found([{ ...gate, open: { c1: "known." } }], [kase("c1", { "h.amount": 5 })]), null],
    ["an open case that does not break the rule", found([{ ...gate, open: { c1: "known." } }], [kase("c1", {})]), /consistency rule 1: lists c1 as open, but no such case breaks the rule/],
    ["the defaults alone", found([alone], []), /consistency rule 1: the defaults alone break it \(p\.a, p\.c\): a or c\./],
    ["the defaults alone, listed as open; an entry of defaults only is not counted again", found([{ ...alone, open: { [DEFAULTS_ALONE]: "known." } }], [kase("c1", {})]), null],
    ["the defaults alone, open; a case that states one of the answers", found([{ ...alone, open: { [DEFAULTS_ALONE]: "known." } }], [kase("c1", { "p[one].a": false })]), /^c1: takes the default of p\[one\]\.c \(false\) against p\[one\]\.a false/],
    ["the defaults listed as open when they break nothing", found([{ ...gate, open: { [DEFAULTS_ALONE]: "known." } }], []), /lists \(defaults\) as open, but the defaults alone do not break the rule/],
    ["a withholding condition that holds in no case", found([], [kase("c1", { "h.status": "joint" })], unmarriedSingle), /^h\.unmarried: its withholding condition holds in no case that takes the default/],
    ["a withholding condition that holds in a case", found([], [kase("c1", {})], unmarriedSingle), null],
  ];
  for (const [name, got, re] of planted) {
    if (re === null) assert.equal(got, "", `defaults: wrongly refused: ${name}`); else assert.match(got, re, `defaults: not found: ${name}`);
    n++;
  }
  return n;
}

export function runCheckSelfTest(): void {
  // tableBand_mono's condition
  assert.deepEqual(tableBandMonoProblems(table([{ at_least: 0, less_than: 5, tax: [0, 0] }, { at_least: 5, less_than: 9, tax: [1, 0] }, { at_least: 9, less_than: 12, tax: [1, 2] }])), []);
  assert.match(tableBandMonoProblems(table([{ at_least: 0, less_than: 5, tax: [3, 0] }, { at_least: 5, less_than: 9, tax: [2, 1] }])).join("\n"), /column a falls to 2 at band 1/);
  // a fall below an earlier band that is not the adjacent one
  assert.match(tableBandMonoProblems(table([{ at_least: 0, less_than: 5, tax: [3, 0] }, { at_least: 5, less_than: 9, tax: [4, 0] }, { at_least: 9, less_than: 12, tax: [3, 0] }])).join("\n"), /falls to 3 at band 2/);
  assert.match(tableBandMonoProblems(table([{ at_least: 0, less_than: 6, tax: [0, 0] }, { at_least: 5, less_than: 9, tax: [0, 0] }])).join("\n"), /band 0 overlaps band 1/);
  assert.match(tableBandMonoProblems(table([{ at_least: 5, less_than: 5, tax: [0, 0] }])).join("\n"), /band 0 is empty or reversed/);

  // register links
  assert.deepEqual(registerLinkProblems(data([entry("amb.a"), entry("amb.b", { unlinked: "superseded by BUG-0000" })], ["amb.a"])), []);
  assert.match(registerLinkProblems(data([entry("amb.a"), entry("amb.b")], ["amb.a"])).join("\n"), /register amb\.b: no line links this entry/);
  assert.match(registerLinkProblems(data([entry("amb.b", { unlinked: "  " })], [])).join("\n"), /register amb\.b: no line links/);
  assert.match(registerLinkProblems(data([entry("amb.a", { unlinked: "superseded" })], ["amb.a"])).join("\n"), /carries an unlinked reason/);

  // Entry syntax in question wording: the forms the question bank used, and substance it must not flag.
  const syntax = [
    "Money is integer cents.", "In cents; zero if none.", "Answer true or false.", "Answer true/false for questions; a count is a whole number.",
    "Unknown may be null; do not guess.", "Enter a JSON array of distinct keys.", "Empty [] means none.",
    'Enter ["taxpayer"], or ["taxpayer","spouse"] if you are married filing jointly.', "List stable keys for taxable interest payers.",
    "Answer taxpayer for the entry keyed taxpayer and spouse for the entry keyed spouse.", "Integer cents.", "A whole number.",
  ];
  for (const s of syntax) assert.ok(entrySyntax(s), `entry syntax not flagged: ${s}`);
  const substance = [
    "Zero if none.", "Answer No if you have none.", "Yes refuses the return.", "Enter 0 if none; Yonkers tax is outside this tool.",
    "The percentage of this property's use that is for this business, from 1 to 100.", "List the employers that gave you a Form W-2, one entry per employer.",
    "Line 7 of your 2024 Schedule D; a loss (printed in parentheses) is entered as a negative amount.", "Box 12 holds up to four amounts, each with a code of one or two letters.",
  ];
  for (const s of substance) assert.equal(entrySyntax(s), null, `substance flagged as entry syntax: ${s}`);

  // Gate conventions (gates.ts): the clean gate, then one violation each.
  assert.deepEqual(gateProblems(gated()), []);
  const gateCases: [string, (lines: Line[]) => void, RegExp, string[]?][] = [
    ["a second reader", (ls) => { (line(ls, "g.total").expr as { of: string[] }).of.push("g.box_amount"); }, /read by g\.total; a gated input is read only by its gate line/],
    ["a refusal gate reading it", (ls) => { line(ls, "g.total").refuses = [{ when: "g.box_amount", form: "x", remedy: "x", cite: null as never }]; }, /read by g\.total/],
    ["an interview target", () => {}, /an interview target/, ["g.box_amount"]],
    ["no else", (ls) => { (line(ls, "g.box").expr as { alternatives: { then: string }[] }).alternatives[1]!.then = "g.box_amount"; }, /no else alternative/],
    ["an else that is not zero", (ls) => { (line(ls, "g.box").expr as { alternatives: { then: string }[] }).alternatives[1]!.then = "g.total"; }, /no else alternative/],
    ["a guard reading the input", (ls) => { ((line(ls, "g.box").expr as { alternatives: { guard: { eq: unknown[] } }[] }).alternatives[0]!.guard.eq)[0] = "g.box_amount"; }, /a guard of the gate reads the gated input/],
    ["a gate that is not a choose", (ls) => { line(ls, "g.box").expr = { op: "sum", of: ["g.box_amount"] }; }, /not a choose/],
    ["a missing gate line", (ls) => { line(ls, "g.box_amount").gated_by = "g.nowhere"; }, /no line g\.nowhere/],
    ["a marker on a computed line", (ls) => { line(ls, "g.total").gated_by = "g.box"; }, /only an input line can be gated/],
    ["two inputs on one gate", (ls) => { ls.push({ ...line(ls, "g.box_amount"), id: "g.other" }); }, /gates g\.box_amount, g\.other; a gate line gates one input/],
  ];
  for (const [name, edit, re, targets] of gateCases) assert.match(gateProblems(gated(edit), targets).join("\n"), re, `gate check missed: ${name}`);
  // The convention hides the gated input: unanswered gate, only the gate is asked; no, nothing; yes, the amount.
  const asked = (inputs: Record<string, unknown>) => [...new Set([...evaluate(gated(), inputs as never, ["g.total"]).derivations.values()]
    .flatMap((d) => d.value.kind === "unknown" && d.value.input ? [d.value.input] : []))];
  assert.deepEqual(asked({}), ["g.any"]);
  assert.deepEqual(asked({ "g.any": false }), []);
  assert.deepEqual(asked({ "g.any": true }), ["g.box_amount"]);

  // Typed choose: Bool and enum alternatives of one type check; mixed, other-enum, count and mistyped lines do not.
  const typeErrors = (edit?: (lines: Line[]) => void) => checkExpressionTypes(typedChooseData(edit), "c").map((e) => e.message).join("\n");
  assert.equal(typeErrors(), "");
  const alt = (ls: Line[], id: string, i: number) => (line(ls, id).expr as { alternatives: { then: string }[] }).alternatives[i]!;
  const chooseCases: [string, (lines: Line[]) => void, RegExp][] = [
    ["a Bool and a money alternative", (ls) => { alt(ls, "c.bsel", 1).then = "c.zero"; }, /c\.bsel: choose branch 'c\.zero' is money, but an earlier alternative is Bool; a choose's alternatives share one type/],
    ["a money and an enum alternative", (ls) => { alt(ls, "c.money", 0).then = "c.pick"; }, /c\.money: choose branch 'c\.zero' is money, but an earlier alternative is Enum\(cv\)/],
    ["alternatives of two enums", (ls) => { ls.push({ ...line(ls, "c.kind"), id: "c.other", type: "Enum(ov)" }); alt(ls, "c.esel", 1).then = "c.other"; }, /c\.esel: choose branch 'c\.other' is Enum\(ov\), but an earlier alternative is Enum\(cv\)/],
    ["a count alternative", (ls) => { ls.push({ ...line(ls, "c.amount"), id: "c.n", type: "Count" }); alt(ls, "c.money", 0).then = "c.n"; }, /choose branch 'c\.n' is a count; a choose's alternatives are money, Bool or enum/],
    ["a Bool choose declared money", (ls) => { line(ls, "c.bsel").type = "NonNegDollars"; }, /c\.bsel: declared money but the expression produces bool/],
    ["an enum choose declared another enum", (ls) => { line(ls, "c.esel").type = "Enum(ov)"; }, /c\.esel: declared Enum\(ov\) but the alternatives are Enum\(cv\)/],
  ];
  for (const [name, edit, re] of chooseCases) assert.match(typeErrors(edit), re, `choose typing missed: ${name}`);
  // Its evaluation, value by value (the Lean evaluator's agreement on the same cases is compare's self-test).
  for (const { inputs, expect } of TYPED_CHOOSE_CASES) {
    const values = evaluate(typedChooseData(), inputs as never, Object.keys(expect)).values;
    for (const [id, want] of Object.entries(expect)) assert.equal(valueText(values.get(id)!), want, `${id} on ${JSON.stringify(inputs)}`);
  }
  // A Bool or enum input gated with a false or enum parameter as its else; a money else for either is not one.
  const typedGate = (edit: (lines: Line[]) => void = () => {}) => typedChooseData((ls) => {
    for (const [input, gate] of [["c.yes", "c.bsel"], ["c.pick", "c.esel"]] as const) line(ls, input).gated_by = gate;
    alt(ls, "c.bsel", 0).then = "c.yes";
    ls.splice(ls.findIndex((x) => x.id === "c.nest"), 1); ls.splice(ls.findIndex((x) => x.id === "c.yes_screened"), 1);
    line(ls, "c.allref").expr = { op: "copy", from: "c.no_screened" } as never;
    edit(ls);
  });
  assert.deepEqual(gateProblems(typedGate()), []);
  assert.match(gateProblems(typedGate((ls) => { alt(ls, "c.bsel", 1).then = "c.zero"; })).join("\n"), /c\.yes \(gated_by c\.bsel\): the gate has no else alternative/);
  assert.match(gateProblems(typedGate((ls) => { alt(ls, "c.esel", 1).then = "c.zero"; })).join("\n"), /c\.pick \(gated_by c\.esel\): alternative c\.zero is neither the gated input nor a parameter of the input's type/);
  assert.match(gateProblems(typedGate((ls) => { line(ls, "c.no").expr = { op: "param", ref: "cdflt" } as never; })).join("\n"), /c\.yes \(gated_by c\.bsel\): the gate has no else alternative/);
  const typedAsked = (inputs: Record<string, unknown>) => [...new Set([...evaluate(typedGate(), inputs as never, ["c.bsel", "c.esel"]).derivations.values()]
    .flatMap((d) => d.value.kind === "unknown" && d.value.input ? [d.value.input] : []))].sort();
  assert.deepEqual(typedAsked({}), ["c.flag", "c.kind"]);
  assert.deepEqual(typedAsked({ "c.flag": false, "c.kind": "b" }), []);
  assert.deepEqual(typedAsked({ "c.flag": true, "c.kind": "a" }), ["c.pick", "c.yes"]);
  const typedCount = 1 + chooseCases.length + TYPED_CHOOSE_CASES.length + 4 + 3;
  // Structured text (text.ts): the subset parses to its blocks; everything else is a named problem; plain text is untouched.
  const good = "Any of these?\n\nWork:\n- wages (Form W-2)\n- tips, for example:\n  - cash tips\n\nA closing note, with a colon:\n\n- a list after a blank line";
  const parsed = parseStructured(good);
  assert.deepEqual(parsed.problems, []);
  assert.deepEqual(parsed.blocks, [{ kind: "paragraph", text: "Any of these?" },
    { kind: "list", heading: "Work:", items: [{ text: "wages (Form W-2)", items: [] }, { text: "tips, for example:", items: ["cash tips"] }] },
    { kind: "paragraph", text: "A closing note, with a colon:" }, { kind: "list", heading: null, items: [{ text: "a list after a blank line", items: [] }] }]);
  const plain = "  a plain *label*  with  `anything`, - kept as it is ";
  assert.deepEqual(parseStructured(plain).problems, []);
  assert.equal(indentRest(plain, "    "), plain);
  assert.equal(textSummary(plain), plain);
  assert.equal(flatText(plain), plain);
  assert.equal(indentRest(good, "  ").split("\n")[5], "    - cash tips");
  assert.equal(textSummary(good), "Any of these?");
  assert.equal(flatText("Q?\n\nH:\n- a\n  - b"), "Q? H: - a - b");
  const bad: [string, RegExp][] = [
    ["- a bullet first\n\nx", /first line must be the question/],
    ["Q?\nHeading:\n- a", /must follow a blank line/],
    ["Q?\n\nNo colon\n- a", /must end with ":"/],
    [`Q?\n\n${"h".repeat(81)}:\n- a`, /at most 80 characters/],
    ["Q?\n\n  - nested first", /nested bullet must follow a bullet/],
    ["Q?\n\n- a\nafter the list", /must follow a blank line/],
    ["Q?\n\n\nx", /two blank lines/],
    ["Q?\n\nx\n", /only allowed between blocks/],
    ["Q?\n\n### Heading", /block syntax/],
    ["Q?\n\n* star", /block syntax/],
    ["Q?\n\n1. one", /block syntax/],
    ["Q?\n\n- **bold**", /inline Markdown/],
    ["Q?\n\n- a _stressed_ word", /inline Markdown/],
    ["Q?\n\n- [a](b)", /inline Markdown/],
    ["Q?\n\n    - too deep", /indented line/],
    ["Q?\n\nx ", /trailing spaces/],
    ["Q?\n\n\tx", /tab/],
  ];
  for (const [text, re] of bad) assert.match(parseStructured(text).problems.join("\n"), re, `not flagged: ${JSON.stringify(text)}`);
  assert.deepEqual(parseStructured("Q?\n\n- employer_reported, an enum value").problems, []);
  console.log(`defaults self-test: ${defaultsSelfTest()} cases passed (conditional withholding, condition and rule validation, consistency violations)`);
  console.log(`check self-test: ${9 + syntax.length + substance.length + 1 + gateCases.length + 3 + typedCount + 10 + bad.length} cases passed (tableBand_mono condition, register links, entry syntax in question wording, gate conventions, Bool and enum choose, structured text)`);
}
