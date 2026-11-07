// Tests of the web UI server (`serve`), on synthetic returns in temporary directories: the returns-directory
// refusals, file modes, the Host and Origin checks, that the server and the CLI give the same state on the same
// log, that a rejected answer appends nothing, roster removal and re-adding, the forms a question names and their
// quoted purposes, and fixture interview paths replayed through the server against the fixtures' expected values.
import assert from "node:assert/strict";
import { spawn, spawnSync, type ChildProcess } from "node:child_process";
import { chmodSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, statSync, symlinkSync } from "node:fs";
import { request } from "node:http";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { isDeepStrictEqual } from "node:util";
import { loadCanonical } from "./canonical.js";
import { interviewView, loadInterview, replay, type Event } from "./interview.js";
import { renderValuesSheetText } from "./output.js";
import { resolveInputs } from "./fixture-inputs.js";
import { nyPath, YEAR_ARGS, yearPath } from "./year.js";
import type { Inputs } from "./types.js";
import { mapPool, poolSize } from "./pool.js";
import { docNames, questionForms } from "./serve.js";
import { namedDesignations } from "./form-refs.js";

const MAIN = resolve(import.meta.dirname, "main.js");
const ROOT = resolve(import.meta.dirname, "../..");

interface Reply { status: number; body: any }
function http(port: number, method: string, path: string, opts: { host?: string; origin?: string | null; body?: unknown } = {}): Promise<Reply> {
  const host = opts.host ?? `127.0.0.1:${port}`;
  const origin = opts.origin === undefined ? (method === "GET" ? null : `http://${host}`) : opts.origin;
  const payload = opts.body === undefined ? undefined : JSON.stringify(opts.body);
  return new Promise((done, fail) => {
    const req = request({ host: "127.0.0.1", port, method, path, headers: { Host: host, ...(origin ? { Origin: origin } : {}), ...(payload ? { "Content-Type": "application/json" } : {}) } }, (res) => {
      const chunks: Buffer[] = [];
      res.on("data", (c: Buffer) => chunks.push(c));
      res.on("end", () => {
        const text = Buffer.concat(chunks).toString("utf8");
        let body: unknown = text;
        try { body = JSON.parse(text); } catch { /* a static file */ }
        done({ status: res.statusCode ?? 0, body });
      });
    });
    req.on("error", fail);
    req.end(payload);
  });
}

function startServer(dir: string): Promise<{ proc: ChildProcess; port: number }> {
  const proc = spawn(process.execPath, [MAIN, ...YEAR_ARGS, "serve", "--dir", dir, "--port", "0"], { stdio: ["ignore", "pipe", "pipe"] });
  let out = "";
  return new Promise((done, fail) => {
    proc.stdout!.on("data", (d: Buffer) => { out += d; const m = out.match(/http:\/\/127\.0\.0\.1:(\d+)\//); if (m) done({ proc, port: Number(m[1]) }); });
    proc.stderr!.on("data", (d: Buffer) => { out += d; });
    proc.on("exit", (code) => fail(new Error(`server exited ${code}: ${out}`)));
  });
}

export async function serveChecks(): Promise<void> {
  const tmp = mkdtempSync(join(tmpdir(), "serve-check-"));
  let server: ChildProcess | undefined;
  const extra: Promise<{ proc: ChildProcess; port: number }>[] = [];
  let checks = 0;
  const ok = (cond: unknown, message: string) => { assert.ok(cond, message); checks++; };
  try {
    // The returns directory: required, existing, outside the repository (through symlinks), private.
    const refuse = (args: string[], pattern: RegExp) => {
      const p = spawnSync(process.execPath, [MAIN, ...YEAR_ARGS, "serve", ...args, "--port", "0"], { encoding: "utf8", timeout: 60_000 });
      ok(p.status !== 0 && pattern.test(p.stderr), `serve ${args.join(" ")}: expected a refusal matching ${pattern}, got ${p.status}: ${p.stderr.slice(0, 300)}`);
    };
    refuse([], /requires --dir/);
    refuse(["--dir", join(tmp, "missing")], /no such directory/);
    refuse(["--dir", join(ROOT, "engine")], /inside the repository/);
    symlinkSync(ROOT, join(tmp, "link"));
    refuse(["--dir", join(tmp, "link")], /inside the repository/);
    for (const mode of [0o750, 0o705]) {
      const d = join(tmp, `open-${mode.toString(8)}`);
      mkdirSync(d); chmodSync(d, mode);
      refuse(["--dir", d], /lets others read it/);
      ok(readdirSync(d).length === 0, "a refused directory is left empty");
    }

    const dir = join(tmp, "returns");
    mkdirSync(dir, { mode: 0o700 });
    // The fixture walks at the end are independent of one another and of everything before them, so they are
    // spread over several servers (each with its own returns directory, on a port the system picks); the others
    // start now, while the checks on the first run.
    for (let i = 1; i < poolSize(); i++) {
      const d = join(tmp, `returns-${i}`);
      mkdirSync(d, { mode: 0o700 });
      extra.push(startServer(d));
    }
    const started = await startServer(dir);
    server = started.proc;
    const port = started.port;
    const get = (path: string, host?: string) => http(port, "GET", path, host ? { host } : {});
    const post = (path: string, body: unknown, opts: { host?: string; origin?: string | null } = {}) => http(port, "POST", path, { ...opts, body });

    // Host and Origin.
    ok((await get("/api/returns", `evil.example:${port}`)).status === 403, "a request for another Host is refused");
    ok((await get("/api/returns", `127.0.0.1:${port + 1}`)).status === 403, "a request for another port is refused");
    ok((await get("/api/returns", `localhost:${port}`)).status === 200, "localhost:<port> is accepted");
    ok((await post("/api/returns", { name: "x" }, { origin: "http://evil.example" })).status === 403, "a POST from another origin is refused");
    ok((await post("/api/returns", { name: "x" }, { origin: null })).status === 403, "a POST without an Origin is refused");
    ok((await post("/api/returns", { name: "x" }, { host: `localhost:${port}`, origin: `http://127.0.0.1:${port}` })).status === 403, "a POST whose Origin is not its Host is refused");
    ok(readdirSync(dir).length === 0, "refused requests create nothing");
    const page = await get("/");
    ok(page.status === 200 && /<title>/.test(page.body as string), "the page is served");
    ok((await get("/app.js")).status === 200, "the script is served");

    // Creating a return: mode 0600 in a 0700 directory; never overwritten.
    ok((await post("/api/returns", { name: "../escape" })).status === 400, "a name with a path is refused");
    const created = await post("/api/returns", { name: "synthetic" });
    ok(created.status === 201 && created.body.status === "incomplete", `create: ${JSON.stringify(created.body).slice(0, 200)}`);
    const log = join(dir, "synthetic.jsonl");
    ok((statSync(log).mode & 0o777) === 0o600, `the log is mode 0600, not ${(statSync(log).mode & 0o777).toString(8)}`);
    ok((statSync(dir).mode & 0o777) === 0o700, "the returns directory is mode 0700");
    const header = readFileSync(log, "utf8");
    ok((await post("/api/returns", { name: "synthetic" })).status === 409 && readFileSync(log, "utf8") === header, "an existing return is not overwritten");
    const listing = (await get("/api/returns")).body;
    ok(isDeepStrictEqual(listing.returns, ["synthetic"]) && /New York/.test(listing.scope) && listing.standingNotices.length > 0, "the returns are listed, with the scope and notices");

    // The CLI and the server give the same state on the same log.
    const data = loadCanonical();
    const config = loadInterview("ny");
    // Every document a question cites has a title for the page to show as its source.
    const untitled = [...new Set(config.questions.map((q) => q.cite.doc))].filter((doc) => typeof listing.docTitles?.[doc] !== "string");
    ok(untitled.length === 0, `every cited document has a title in the source catalogs; missing: ${untitled.join(", ")}`);
    // A document's designation is served beside its title: a federal form and a New York form carry theirs; a statute has none.
    ok(listing.docDesignations?.f1040 === "Form 1040" && listing.docTitles.f1040 === "U.S. Individual Income Tax Return"
      && listing.docDesignations.ny_it201 === "Form IT-201" && listing.docDesignations["usc-26-72"] === undefined
      && Object.keys(listing.docDesignations).every((doc) => typeof listing.docTitles[doc] === "string"),
      "designations are served for the documents that print one, each with a title");

    // The forms a question names: read from its wording by designation, lists and parent forms included.
    const named = (text: string) => namedDesignations(text).map((d) => d.designation);
    ok(isDeepStrictEqual(named("Forms 1099-INT and 1099-OID, or Form 2555 or Form 4563"), ["Form 1099-INT", "Form 1099-OID", "Form 2555", "Form 4563"]), "a list of forms names each");
    ok(isDeepStrictEqual(named("Schedules C, E, and F (Form 1040 or 1040-SR), and Schedule A (Form 8971)"),
      ["Schedule C (Form 1040)", "Schedule E (Form 1040)", "Schedule F (Form 1040)", "Schedule A (Form 8971)"]), "a list of schedules takes its parent form");
    ok(isDeepStrictEqual(named("Form 1040, Filing Status; Form 2441, Part II; Form 1040 line 16; Pub. 501"), ["Form 1040", "Form 2441", "Form 1040"]), "words after a form are not form numbers");
    const names = docNames(config.tax_year);
    const byQuestion = questionForms(config, names.forms);
    const formsOf = (input: string) => byQuestion.get(input)!.map((f) => `${f.designation}${f.id === null ? "?" : f.purpose ? "+" : ""}`);
    ok(isDeepStrictEqual(formsOf("scope.other_line16"), ["Form 1040", "Form 8814?", "Form 8615?", "Form 8621?", "Form 8960+", "Form 4972?", "Form 8978?", "Schedule J?"]),
      `scope.other_line16 names Form 8814 and Schedule J, which the catalogs lack, and Form 8960, glossed: ${formsOf("scope.other_line16")}`);
    ok(isDeepStrictEqual(formsOf("interest.penalty"), ["Form 1099-INT+", "Form 1099-OID?", "Schedule 1 (Form 1040)+"]), `a bare "Schedule 1" is Schedule 1 (Form 1040), the catalogs' only Schedule 1: ${formsOf("interest.penalty")}`);
    ok(formsOf("gift.special").includes("Schedule K-1?"), "a bare Schedule K-1, of three parent forms in the catalogs, stays unresolved");
    ok(isDeepStrictEqual(formsOf("ny_it2.state_withheld"), ["Form W-2", "Form IT-2+"]), `a New York question names Form W-2 and Form IT-2: ${formsOf("ny_it2.state_withheld")}`);
    // As served: only the forms the catalogs hold, each purpose the catalog's own.
    const firstForms = created.body.pending[0].forms as { designation: string; id: string; title?: string; purpose?: { text: string; doc: string; page: number } }[];
    const catalogPurpose = (id: string) => names.forms.find((f) => f.id === id)!.purpose;
    ok(created.body.pending[0].input === "$person" && isDeepStrictEqual(firstForms.map((f) => f.id), ["fw2", "f1099r"])
      && firstForms[0]!.title === "Wage and Tax Statement" && firstForms[0]!.purpose === undefined
      && firstForms[1]!.purpose?.doc === "f1099r" && firstForms[1]!.purpose?.page === 5
      && firstForms.every((f) => isDeepStrictEqual(f.purpose, catalogPurpose(f.id))),
      `the first question's forms are served with their titles and purposes: ${JSON.stringify(firstForms).slice(0, 300)}`);
    ok(created.body.pending.every((q: any) => Array.isArray(q.forms) && q.forms.every((f: any) => typeof f.id === "string")), "every pending question carries its catalogued forms");
    const cli = (args: string[], expectOk = true) => {
      const p = spawnSync(process.execPath, [MAIN, ...YEAR_ARGS, "interview", ...args, "--log", log], { encoding: "utf8", maxBuffer: 256 * 1024 * 1024 });
      assert.equal(p.status === 0, expectOk, `interview ${args.join(" ")}: ${p.stderr}`);
      return expectOk ? JSON.parse(p.stdout) : null;
    };
    const same = (served: any, label: string) => {
      const c = cli(["advance"]);
      for (const k of ["status", "refusal", "question", "reachableInputs", "scope", "notices", "values"]) ok(isDeepStrictEqual(served[k], c[k]), `${label}: ${k} differs between the server and the CLI`);
      const pending = served.pending.map(({ type: _t, values: _v, forms: _f, ...q }: any) => q);
      ok(isDeepStrictEqual(pending, c.pending), `${label}: pending differs between the server and the CLI`);
      const hints: Record<string, RegExp> = { Bool: /^true or false/, NonNegDollars: /^integer cents/, Dollars: /^integer cents, negative/, Count: /^a whole number/,
        Enum: /^one of: "/, Roster: /^(?:one of: \[|a JSON list of distinct entry keys)/ };
      ok(served.pending.every((q: any) => hints[q.type]!.test(q.entry) && /null asks for help$/.test(q.entry)), `${label}: the CLI's entry hint matches each input's type`);
      const events = readFileSync(log, "utf8").trim().split("\n").map((l) => JSON.parse(l) as Event);
      const view = interviewView(data, config, replay(config, events));
      ok(renderValuesSheetText(view.sheet) === c.sheet, `${label}: the structured sheet does not render to the CLI's text sheet`);
      const sections = JSON.parse(JSON.stringify(view.sheet.sections)) as typeof view.sheet.sections; // as served
      ok(isDeepStrictEqual([...served.sheets.federal, ...served.sheets.newYork], [...sections.filter((s) => !s.doc.startsWith("ny_")), ...sections.filter((s) => s.doc.startsWith("ny_"))]), `${label}: the served sheets are not the engine's sections`);
      ok(served.sheets.newYork.every((s: any) => s.doc.startsWith("ny_")) && served.sheets.federal.every((s: any) => !s.doc.startsWith("ny_")), `${label}: sheets split by jurisdiction`);
    };
    same(created.body, "new return");

    const fixtures = (file: string) => (JSON.parse(readFileSync(file, "utf8")) as { cases: { id: string; inputs: Inputs; expect?: Record<string, unknown> }[] }).cases
      .map((c) => ({ ...c, inputs: resolveInputs(c.inputs, data.params, c.id) }));
    const nyCases = fixtures(join(nyPath("fixtures"), "it201.json"));
    const answer = (name: string, input: string, value: unknown) => post(`/api/returns/${name}/answer`, { input, value });
    const unchanged = async (name: string, input: unknown, value: unknown, label: string, body?: unknown) => {
      const before = readFileSync(join(dir, `${name}.jsonl`), "utf8");
      const r = await post(`/api/returns/${name}/answer`, body ?? { input, value });
      ok(r.status === 400 && typeof r.body.error === "string", `${label}: expected 400, got ${r.status}`);
      ok(readFileSync(join(dir, `${name}.jsonl`), "utf8") === before, `${label}: a rejected answer changed the log`);
      return r.body.error as string;
    };

    // A synthetic New York return refused part-year: a help request, rejected answers, a provisional refusal that
    // becomes final once nothing is pending, and roster removal and re-adding.
    const base = nyCases.find((c) => c.id === "ny.refuse.part_year_state")!;
    let state = created.body;
    const first = state.pending[0].input;
    ok(first === "$person" && state.pending[0].type === "Roster", `the first question is the person roster, not ${first}`);
    ok(isDeepStrictEqual(state.pending[0].choices.map((c: any) => c.value), [["taxpayer"], ["taxpayer", "spouse"]]), "the person roster is a selector of two choices");
    ok(/^one of: \["taxpayer"\] \(Just me\)/.test(state.pending[0].entry), `the person roster's entry hint: ${state.pending[0].entry}`);
    state = (await answer("synthetic", first, null)).body;
    ok(state.pending[0].input === first && state.pending[0].helpRequested === true, "a help request leaves the question pending, marked");
    same(state, "help request");
    // Labels: only on a roster answer, one non-empty label for each listed entry.
    const labelled = (input: string, value: unknown, labels: unknown) => post("/api/returns/synthetic/answer", { input, value, labels });
    for (const [labels, what] of [[{}, "a missing label"], [{ taxpayer: " " }, "a blank label"], [{ taxpayer: "You", spouse: "x" }, "a label for an unlisted entry"], [["You"], "labels as a list"]] as const) {
      const before = readFileSync(log, "utf8");
      ok((await labelled("$person", ["taxpayer"], labels)).status === 400 && readFileSync(log, "utf8") === before, `${what} is refused and writes nothing`);
    }
    const choice = state.pending[0].choices[0];
    state = (await labelled("$person", choice.value, choice.labels)).body;
    ok(state.entryLabels["person[taxpayer]"] === "You", "the chosen answer's labels name the entry");
    ok(JSON.parse(readFileSync(log, "utf8").trim().split("\n").at(-1)!).labels?.taxpayer === "You", "the labels are saved on the roster answer's event");
    same(state, "person chosen with labels");
    await unchanged("synthetic", "$person", ["taxpayer", "taxpayer"], "duplicate roster keys");
    await unchanged("synthetic", "$person", ["tax payer"], "a roster key outside the key pattern");
    await unchanged("synthetic", "f1040.line1a", 100, "an unreachable input");
    await unchanged("synthetic", "no.such_input", 1, "an undeclared input");
    await unchanged("synthetic", undefined, undefined, "an answer without a value", { input: "$person" });
    let sawProvisional = false, steps = 0, checkedMid = false;
    for (;;) {
      const q = state.pending.find((p: any) => p.input in base.inputs && !state.answered.some((a: any) => a.input === p.input && a.value !== null));
      if (!q) break;
      if (q.type === "NonNegDollars" && !checkedMid) {
        await unchanged("synthetic", q.input, -1, "a negative amount");
        await unchanged("synthetic", q.input, 12.5, "a fractional amount");
        await unchanged("synthetic", q.input, "100", "an amount as text");
        checkedMid = true;
      }
      if (q.type === "Bool") ok(typeof base.inputs[q.input] === "boolean", `${q.input}: Bool metadata`);
      if (q.type === "Enum") ok(q.values.includes(base.inputs[q.input]), `${q.input}: the enum values include the answer`);
      const v = base.inputs[q.input];
      const r = q.type === "Roster" && Array.isArray(v)
        ? await labelled(q.input, v, Object.fromEntries((v as string[]).map((k, i) => [k, i === 0 ? "Acme Corp" : `Acme Corp ${i + 1}`])))
        : await answer("synthetic", q.input, v);
      assert.equal(r.status, 200, `${q.input}: ${JSON.stringify(r.body)}`);
      state = r.body;
      if (state.status === "refused" && state.pending.length > 0) {
        if (!sawProvisional) same(state, "provisional refusal");
        ok(state.refusalFinal === false, "a refusal with questions pending is provisional");
        sawProvisional = true;
      }
      assert.ok(++steps < 400, "the walk did not end");
    }
    ok(sawProvisional, "the walk passed a provisional refusal");
    ok(state.entryLabels["person[taxpayer].w2[emp_a]"] === "Acme Corp" && state.entryLabels["person[taxpayer].w2[emp_b]"] === "Acme Corp 2", "roster labels name their entries");
    ok(state.status === "refused" && state.pending.length === 0 && state.refusalFinal === true, `the refusal is final when nothing is pending (${state.status}, ${state.pending.length} pending)`);
    ok(state.refusal.gate === "ny_it201.gate.part_year_state", `refusal gate ${state.refusal.gate}`);
    same(state, "final refusal");
    for (const [key, expected] of Object.entries(base.expect ?? {})) if (key in state.values) ok(isDeepStrictEqual(state.values[key].value, expected), `${base.id}: ${key}`);

    // Corrections: clearing the refusal; then a roster entry removed and re-added, as the CLI does.
    const gate = "ny_it201.ask.state_resident";
    ok(base.inputs[gate] === false, "the synthetic return is refused as not a full-year resident");
    state = (await answer("synthetic", gate, true)).body;
    ok(state.status !== "refused" || state.refusal.gate !== "ny_it201.gate.part_year_state", "correcting the answer clears the refusal");
    const roster = "$w2@person[taxpayer]";
    const entries = base.inputs[roster] as string[];
    ok(entries.length >= 2, "the synthetic return has two employers");
    const full = state.values;
    state = (await answer("synthetic", roster, entries.slice(0, 1))).body;
    ok(!isDeepStrictEqual(state.values["f1040.line1a"], full["f1040.line1a"]), "removing an employer changes line 1a");
    ok(!state.answered.some((a: any) => a.input.includes(`w2[${entries[1]}]`)), "a removed entry's answers are inactive");
    same(state, "roster entry removed");
    state = (await answer("synthetic", roster, entries)).body;
    ok(isDeepStrictEqual(state.values, full), "re-adding the entry restores its answers");
    ok(state.changed.includes("f1040.line1a"), "the lines the answer changed are listed");
    same(state, "roster entry re-added");
    const reloaded = (await get("/api/returns/synthetic")).body;
    ok(isDeepStrictEqual(reloaded.changed, state.changed) && isDeepStrictEqual(reloaded.values, state.values), "a reload gives the same state and changed lines");
    // An answer written by the CLI is read by the server.
    cli(["answer", "--input", gate, "--value", "false"]);
    ok((await get("/api/returns/synthetic")).body.refusal?.gate === "ny_it201.gate.part_year_state", "the server reads the CLI's answer");
    cli(["answer", "--input", gate, "--value", "\"yes\""], false);

    // Fixture interview paths replayed through the server: the federal Stage 5 cases (the federal questions; their
    // fixtures have no New York answers) and a sample of the New York cases. Each walk answers the first pending
    // question the fixture answers, until none is left; every expected value the profile's targets reach must match.
    const fed = fixtures(yearPath("fixtures", "stage5.json"));
    const sample = [...nyCases.filter((_, i) => i % 9 === 0), ...nyCases.filter((c) => c.id.startsWith("ny.refuse.")).slice(0, 2)];
    const all = [...fed, ...sample];
    const walkers = [{ port }, ...(await Promise.all(extra))];
    const idle = walkers.map((_, i) => i);
    const counts = await mapPool(all, async (c, walk) => {
      const lane = idle.shift()!;
      try {
        const post2 = (path: string, body: unknown) => http(walkers[lane]!.port, "POST", path, { body });
        const name = `fx-${walk}`;
        let s = (await post2("/api/returns", { name })).body;
        for (let step = 0; ; step++) {
          assert.ok(step < 800, `${c.id}: the walk did not end`);
          const q = s.pending.find((p: any) => p.input in c.inputs && !s.answered.some((a: any) => a.input === p.input));
          if (!q) break;
          const r = await post2(`/api/returns/${name}/answer`, { input: q.input, value: c.inputs[q.input] });
          assert.equal(r.status, 200, `${c.id} ${q.input}: ${JSON.stringify(r.body)}`);
          s = r.body;
        }
        let compared = 0, unreached = 0;
        for (const [key, expected] of Object.entries(c.expect ?? {})) {
          if (!(key in s.values)) { unreached++; continue; }
          assert.deepEqual(s.values[key].value, expected, `${c.id}: ${key} through the server`);
          compared++;
        }
        return { compared, unreached };
      } finally { idle.push(lane); }
    }, walkers.length);
    const walks = all.length;
    const compared = counts.reduce((n, c) => n + c.compared, 0), unreached = counts.reduce((n, c) => n + c.unreached, 0);
    ok(compared > 0, "fixture values compared");
    console.log(`serve: ${checks} checks passed; ${walks} fixture paths replayed through the server (${fed.length} federal, ${sample.length} New York), ${compared} expected values matched, ${unreached} not reached by the profile's targets`);
  } finally {
    server?.kill();
    for (const p of extra) p.then((x) => x.proc.kill(), () => {});
    rmSync(tmp, { recursive: true, force: true });
  }
}
