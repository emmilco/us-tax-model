// The fixture-defaults guard (owner decision; engine/src/fixture-inputs.ts). Adding a default for a new input needs
// only the normal tier. Changing the value of an existing default, or the condition under which it is withheld,
// changes the inputs of every case that takes it, so such a commit must carry the affected-cases report's
// acknowledgement in its message, one line per changed default:
//
//   Fixture-default-changed: <input template> (<n> cases)
//
// where <n> is the number of cases whose resolved inputs change, as this guard counts them. The guard prints the report
// (each changed default with the cases it changes) and refuses a commit whose message lacks a line, names a count
// other than the report's, or acknowledges a default that did not change.
//
//   node tools/defaults_guard.mjs --commit-msg <file>   compare the index with HEAD (tools/hooks/commit-msg)
//   node tools/defaults_guard.mjs --self-test           (in check-all)
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";

const ROOT = resolve(import.meta.dirname, "..");
const { loadCanonical } = await import(resolve(ROOT, "engine/dist/canonical.js"));
const FI = await import(resolve(ROOT, "engine/dist/fixture-inputs.js"));

const ACK = /^Fixture-default-changed: (\S+) \((\d+) cases?\)\s*$/;

/** What a default resolves by: its value and the tests under which it is withheld (null when it has none). */
const resolvesBy = (d) => ({ value: d.value, withheld_when: d.withheld?.when ?? null });

/** The defaults whose value or withholding condition differs between two lists of entries (inputs present in both);
 * `from` and `to` are the values, and `when` the old and new conditions where the condition differs. */
export function changedDefaults(before, after) {
  const old = new Map(before.map((d) => [d.input, resolvesBy(d)]));
  const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);
  return after.filter((d) => old.has(d.input) && !same(old.get(d.input), resolvesBy(d))).map((d) => {
    const [b, a] = [old.get(d.input), resolvesBy(d)];
    return { input: d.input, from: b.value, to: a.value, ...(same(b.withheld_when, a.withheld_when) ? {} : { when: [b.withheld_when, a.withheld_when] }) };
  });
}

/** For each changed default, the ids of the cases (taking defaults) whose resolved inputs it changes. `cases`:
 * [{id, file, j, inputs}] as stated; `tables`: {federal: [before, after], ny: [before, after]} default entries. */
export function affectedCases(data, cases, tables, changes) {
  const out = new Map(changes.map((c) => [c.input, []]));
  for (const ch of changes) {
    for (const c of cases) {
      if (!FI.takesDefaults(c.file)) continue;
      const [b, a] = [0, 1].map((i) => FI.tableOf({ defaults: tables.federal[i] }, ...(c.j === "ny" ? [{ defaults: tables.ny[i] }] : [])));
      // Only this default changed: the after table with every other change undone.
      for (const other of changes) if (other.input !== ch.input && a.has(other.input)) a.set(other.input, b.get(other.input));
      const r = (t) => JSON.stringify(Object.entries(FI.resolveInputs(c.inputs, data, c.id, c.j, t)).sort());
      if (r(b) !== r(a)) out.get(ch.input).push(c.id);
    }
  }
  return out;
}

/** The problems with a commit message's acknowledgements, given the affected cases of each changed default. */
export function ackProblems(message, affected) {
  const acks = new Map();
  for (const line of message.split("\n")) { const m = ACK.exec(line); if (m) acks.set(m[1], Number(m[2])); }
  const problems = [];
  for (const [input, ids] of affected) {
    if (!acks.has(input)) problems.push(`the default of ${input} changed (${ids.length} cases); acknowledge it with the line "Fixture-default-changed: ${input} (${ids.length} cases)"`);
    else if (acks.get(input) !== ids.length) problems.push(`${input}: the message acknowledges ${acks.get(input)} cases; the report counts ${ids.length}`);
  }
  for (const input of acks.keys()) if (!affected.has(input)) problems.push(`${input}: acknowledged, but its default did not change`);
  return problems;
}

function git(...args) { return execFileSync("git", args, { cwd: ROOT, encoding: "utf8", maxBuffer: 1 << 30 }); }
function show(rev, path) { try { return git("show", `${rev}:${path}`); } catch { return null; } }

function commitMsg(msgFile) {
  const year = JSON.parse(readFileSync(resolve(ROOT, "years.json"), "utf8")).adopted;
  const years = git("ls-files", "--cached", "fixtures").split("\n").map((p) => /^fixtures\/(?:ny\/)?(\d{4})\/defaults\.json$/.exec(p)?.[1]).filter(Boolean);
  const problems = [];
  for (const y of [...new Set([...years, ...year.map(String)])].sort()) {
    const paths = { federal: `fixtures/${y}/defaults.json`, ny: `fixtures/ny/${y}/defaults.json` };
    const entries = (rev, j) => JSON.parse(show(rev, paths[j]) ?? '{"defaults": []}').defaults;
    const tables = { federal: [entries("HEAD", "federal"), entries("", "federal")], ny: [entries("HEAD", "ny"), entries("", "ny")] };
    const changes = [...changedDefaults(...tables.federal), ...changedDefaults(...tables.ny)];
    if (!changes.length) continue;
    const data = loadCanonical(resolve(ROOT, "canonical", y));
    const cases = [];
    for (const [j, dir] of [["federal", `fixtures/${y}/`], ["ny", `fixtures/ny/${y}/`]]) {
      for (const p of git("ls-files", "--cached", dir).split("\n").filter((p) => p.endsWith(".json") && !p.slice(dir.length).includes("/") && !p.endsWith("/defaults.json"))) {
        for (const c of JSON.parse(show("", p)).cases ?? []) cases.push({ ...c, file: p.slice(dir.length), j });
      }
    }
    const affected = affectedCases(data, cases, tables, changes);
    console.log(`Fixture defaults changed in ${y} (affected-cases report):`);
    for (const ch of changes) {
      const ids = affected.get(ch.input);
      const what = [JSON.stringify(ch.from) === JSON.stringify(ch.to) ? [] : [`${JSON.stringify(ch.from)} -> ${JSON.stringify(ch.to)}`],
        ch.when ? [`withheld when ${JSON.stringify(ch.when[0])} -> ${JSON.stringify(ch.when[1])}`] : []].flat().join("; ");
      console.log(`  ${ch.input}: ${what}; ${ids.length} cases' inputs change${ids.length ? ": " + ids.slice(0, 20).join(", ") + (ids.length > 20 ? `, and ${ids.length - 20} more` : "") : ""}`);
    }
    problems.push(...ackProblems(readFileSync(msgFile, "utf8"), affected));
  }
  if (problems.length) {
    for (const p of problems) console.error(`defaults-guard: ${p}`);
    process.exit(1);
  }
}

function selfTest() {
  const data = loadCanonical(resolve(ROOT, "canonical", String(Math.max(...JSON.parse(readFileSync(resolve(ROOT, "years.json"), "utf8")).adopted))));
  const before = [{ input: "f1040.status", value: "single" }, { input: "$person", value: ["taxpayer"] }, { input: "person.tin", value: true }];
  const after = [{ input: "f1040.status", value: "mfj" }, { input: "$person", value: ["taxpayer"] }, { input: "person.tin", value: true }, { input: "f1040.new", value: false }];
  const changes = changedDefaults(before, after);
  assert.deepEqual(changes, [{ input: "f1040.status", from: "single", to: "mfj" }], "a changed value is found; an added default is not a change");
  const cases = [
    { id: "a", file: "f1040.json", j: "federal", inputs: {} },
    { id: "b", file: "f1040.json", j: "federal", inputs: { "f1040.status": "hoh" } },
    { id: "c", file: "f1040.json", j: "federal", inputs: { "f1040.status": null } },
    { id: "d", file: "mutation.json", j: "federal", inputs: {} },
  ];
  const affected = affectedCases(data, cases, { federal: [before, after], ny: [[], []] }, changes);
  assert.deepEqual(affected.get("f1040.status"), ["a"], "only a case that takes the default is affected (not one stating it, withholding it, or taking no defaults)");
  assert.deepEqual(ackProblems("x\nFixture-default-changed: f1040.status (1 case)\n", affected), []);
  assert.equal(ackProblems("x\n", affected).length, 1, "an unacknowledged change is refused");
  assert.equal(ackProblems("Fixture-default-changed: f1040.status (2 cases)", affected).length, 1, "a wrong count is refused");
  assert.equal(ackProblems("Fixture-default-changed: f1040.status (1 case)\nFixture-default-changed: person.tin (0 cases)", affected).length, 1, "acknowledging an unchanged default is refused");
  // A withholding condition added, changed or removed is a change too; its reason is not.
  const when = (status) => [{ input: "f1040.status", is: status }];
  const plain = [{ input: "f1040.status", value: "single" }, { input: "$person", value: ["taxpayer"] }, { input: "person.tin", value: true }];
  const conditional = (status, reason = "r") => plain.map((d) => d.input === "person.tin" ? { ...d, withheld: { when: when(status), reason } } : d);
  assert.deepEqual(changedDefaults(plain, conditional("mfj")), [{ input: "person.tin", from: true, to: true, when: [null, when("mfj")] }], "an added condition is a change");
  assert.deepEqual(changedDefaults(conditional("mfj"), conditional("hoh")).map((c) => c.input), ["person.tin"], "a changed condition is a change");
  assert.deepEqual(changedDefaults(conditional("mfj"), plain).map((c) => c.input), ["person.tin"], "a removed condition is a change");
  assert.deepEqual(changedDefaults(conditional("mfj"), conditional("mfj", "another reason")), [], "a condition's reason is not a change");
  const added = changedDefaults(plain, conditional("mfj"));
  const withheld = affectedCases(data, [...cases, { id: "e", file: "f1040.json", j: "federal", inputs: { "f1040.status": "mfj" } }, { id: "f", file: "f1040.json", j: "federal", inputs: { "f1040.status": "mfj", "person[taxpayer].tin": true } }],
    { federal: [plain, conditional("mfj")], ny: [[], []] }, added);
  assert.deepEqual(withheld.get("person.tin"), ["e"], "only a case in which the condition holds and which takes the default is affected");
  console.log("defaults-guard self-test: changed values and withholding conditions found, affected cases counted, acknowledgements checked");
}

const args = process.argv.slice(2);
if (args[0] === "--self-test") selfTest();
else if (args[0] === "--commit-msg" && args[1]) commitMsg(args[1]);
else { console.error("usage: defaults_guard.mjs --commit-msg <file> | --self-test"); process.exit(2); }
