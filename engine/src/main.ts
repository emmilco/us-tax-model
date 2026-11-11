// Command-line entry: the backend of the system. Every command takes
// --year N (default: the newest adopted year in years.json; see year.ts).
//
//   node engine/dist/main.js build                 build + check the data
//   node engine/dist/main.js render                render worksheets for review
//   node engine/dist/main.js render --check        fail unless rendered/ is what the canonical data renders to
//   node engine/dist/main.js eval --inputs F [--json]
//                                                  evaluate a return from inputs
//   node engine/dist/main.js eval --batch F        evaluate many returns ([{id, inputs}]) as JSON
//   node engine/dist/main.js conjecture            test the Tax Table conjecture
//   node engine/dist/main.js properties            check the data-level properties over generated returns
//   node engine/dist/main.js properties --ny       the refusal properties over generated returns with New York answers
//   node engine/dist/main.js classm-jobs [--docs a,b] write the class M hand-work jobs (branch-covering cases)
//   node engine/dist/main.js check-self-test       test check rules against constructed violations
//   node engine/dist/main.js interview-rules       the interview rules over profiles, fixture paths and generated returns
//   node engine/dist/main.js interview-length [--write]
//                                                  questions asked per return in today's order, at the floor any
//                                                  order can reach, and in an order by expected pruning
//   node engine/dist/main.js serve --dir D [--port N]
//                                                  the web UI (ui/) on 127.0.0.1, return logs in D
//   node engine/dist/main.js test-serve            the web UI server's tests (synthetic returns, temporary dirs)
//   node engine/dist/main.js spouse-wording --self-test
//                                                  the spouse phrase's rewording for display, on constructed texts and the built questions

import { readFileSync } from "node:fs";
import { NY_MODE } from "./year.js";
import { readDefaultsFile, resolveCase, tableOf } from "./fixture-inputs.js";
import { runBuild } from "./build.js";
import { renderAll } from "./render.js";
import { loadCanonical } from "./canonical.js";
import { allTargets, evaluate } from "./eval.js";
import { renderValuesSheet, renderValuesHtml, resultToJson, standingNotices } from "./output.js";
import { runConjecture, runEicConjecture } from "./conjecture.js";
import { coverageReport, evidenceReport, testFixtures, reviewStage2, reviewStage3, reviewStage4, reviewStage5 } from "./fixtures.js";
import { differential } from "./differential.js";
import { compareEvaluators } from "./compare.js";
import { runMutation } from "./mutate.js";
import { runProperties } from "./properties.js";
import { classmJobs } from "./classm.js";

import { integrationChecks } from "./integration.js";
import { runChecks } from "./check.js";
import { runCheckSelfTest } from "./check-selftest.js";
import type { CanonicalData } from "./types.js";
import { runInterview } from "./interview.js";
import { runServe } from "./serve.js";
import { serveChecks } from "./serve-check.js";
import { interviewRules } from "./interview-rules.js";
import { interviewLength } from "./interview-length.js";
import { spouseWordingSelfTest } from "./spouse-wording.js";

const command = process.argv[2];

if (command === "review-stage5") {
  reviewStage5();
} else if (command === "review-stage4") {
  reviewStage4();
} else if (command === "review-stage3") {
  reviewStage3();
} else if (command === "review-stage2") {
  reviewStage2();
} else if (command === "test-integration") {
  await integrationChecks();
} else if (command === "check") {
  const result = runChecks(JSON.parse(readFileSync(process.argv[3]!, "utf8")) as CanonicalData);
  console.log(JSON.stringify(result));
  process.exit(result.errors.length ? 1 : 0);
} else if (command === "interview") {
  runInterview(process.argv.slice(3));
} else if (command === "serve") {
  await runServe(process.argv.slice(3));
} else if (command === "test-serve") {
  try { await serveChecks(); }
  catch (e) { console.error(`test-serve FAILED: ${e instanceof Error ? e.stack ?? e.message : String(e)}`); process.exit(1); }
} else if (command === "build") {
  const { errors, stats } = runBuild();
  for (const line of stats) console.log(line);
  if (errors.length > 0) {
    console.error(`\nBUILD FAILED with ${errors.length} error(s):`);
    for (const error of errors) console.error(`  - ${error}`);
    process.exit(1);
  }
  console.log("\nbuild OK");
} else if (command === "render") {
  process.exit(renderAll(process.argv.slice(3)));
} else if (command === "eval") {
  const args = process.argv.slice(3);
  let inputsPath: string | null = null;
  let batchPath: string | null = null;
  let json = false;
  let html = false;
  let targetsOverride: string[] | null = null;
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--inputs") inputsPath = args[++i] ?? null;
    else if (args[i] === "--batch") batchPath = args[++i] ?? null;
    else if (args[i] === "--json") json = true;
    else if (args[i] === "--html") html = true;
    else if (args[i] === "--target") targetsOverride = (args[++i] ?? "").split(",").filter(Boolean);
    else {
      console.error(`eval: unknown argument '${args[i]}'`);
      process.exit(2);
    }
  }
  if (json && html) throw new Error("select either --json or --html");
  if (batchPath) {
    // Batch mode: a JSON array of { id, inputs }; emits { notices, cases: { id: <eval json> } }, or
    // { error } for a case whose inputs the data rejects (the others are still evaluated).
    const data = loadCanonical();
    const cases = JSON.parse(readFileSync(batchPath, "utf-8")) as { id: string; inputs: Record<string, number | boolean | string> }[];
    // Written one case at a time: the whole document is larger than the longest string V8
    // allows. Written without process.exit so a large payload is not truncated on a pipe.
    process.stdout.write(`{"notices":${JSON.stringify(standingNotices())},"cases":{`);
    cases.forEach((c, i) => {
      let out: string;
      try { out = resultToJson(evaluate(data, c.inputs, targetsOverride ?? allTargets(data, c.inputs)), false); }
      catch (e) { out = JSON.stringify({ error: (e as Error).message }); }
      process.stdout.write(`${i ? "," : ""}${JSON.stringify(c.id)}:${out}`);
    });
    process.stdout.write("}}\n");
  } else {
  if (!inputsPath) {
    console.error("eval: --inputs <file.json> is required");
    process.exit(2);
  }
  const data = loadCanonical();
  const inputs = JSON.parse(readFileSync(inputsPath, "utf-8")) as Record<string, number | boolean | string>;
  const result = evaluate(data, inputs, targetsOverride ?? allTargets(data, inputs));
  if (json) {
    console.log(resultToJson(result));
  } else if (html) {
    console.log(renderValuesHtml(data, result, data.forms.map(f=>f.id)));
  } else {
    console.log(renderValuesSheet(data, result, [...data.forms].map((f) => f.id)));
  }
  }
} else if (command === "conjecture") {
  runConjecture();
  runEicConjecture();
} else if (command === "fixture-inputs") {
  // The inputs fixture cases are evaluated on, for tools outside the engine (tools/fixtures_year.py resolve_cases):
  // --cases <file> holds [{id, file, inputs}] as a fixture file states them (`file`: the case file's name, which decides
  // whether the case takes the defaults); prints {"cases": {<id>: <inputs>}}. --ny adds the New York defaults;
  // --defaults <file> (repeatable) reads those defaults files instead of the year's.
  const args = process.argv.slice(3);
  let casesPath: string | null = null;
  const defaultsFiles: string[] = [];
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--cases") casesPath = args[++i] ?? null;
    else if (args[i] === "--defaults") defaultsFiles.push(args[++i] ?? "");
    else { console.error(`fixture-inputs: unknown argument ${args[i]}`); process.exit(2); }
  }
  if (!casesPath) { console.error("usage: main.js fixture-inputs --cases <file> [--ny] [--defaults <file> ...]"); process.exit(2); }
  const data = loadCanonical();
  const j = NY_MODE ? "ny" : "federal";
  const table = defaultsFiles.length ? tableOf(...defaultsFiles.map(readDefaultsFile)) : undefined;
  const cases = JSON.parse(readFileSync(casesPath, "utf8")) as { id: string; file: string; inputs: Record<string, unknown> }[];
  const out: Record<string, unknown> = {};
  try {
    for (const c of cases) out[c.id] = resolveCase(c, c.file, data, j, table);
  } catch (e) { console.error(String(e instanceof Error ? e.message : e)); process.exit(1); }
  process.stdout.write(JSON.stringify({ cases: out }) + "\n");
} else if (command === "test-fixtures") {
  process.exit(await testFixtures() === 0 ? 0 : 1);
} else if (command === "coverage") {
  coverageReport();
} else if (command === "evidence") {
  const at = process.argv.indexOf("--engine-release");
  evidenceReport(at > 0 ? process.argv[at + 1] ?? "none" : undefined);
} else if (command === "differential") {
  process.exit(differential() === 0 ? 0 : 1);
} else if (command === "compare") {
  process.exit(compareEvaluators());
} else if (command === "mutate") {
  process.exit(await runMutation());
} else if (command === "properties") {
  process.exit(runProperties());
} else if (command === "classm-jobs") {
  classmJobs(process.argv.slice(3));
} else if (command === "interview-rules") {
  process.exit(await interviewRules(process.argv.slice(3)));
} else if (command === "interview-length") {
  process.exit(await interviewLength(process.argv.slice(3)));
} else if (command === "spouse-wording" && process.argv.includes("--self-test")) {
  process.exit(spouseWordingSelfTest());
} else if (command === "check-self-test") {
  runCheckSelfTest();
} else {
  console.error(
    "usage: main.js [--year N] build | render | eval --inputs <file> [--json|--html] [--target <lines>] | eval --batch <file> | interview start|advance|answer --log <file> | serve --dir <dir> [--port N] | test-serve | conjecture | fixture-inputs --cases <file> [--ny] [--defaults <file> ...] | test-fixtures | test-integration | coverage | properties [--ny] | mutate | compare | check-self-test | interview-rules | interview-length [--write] | spouse-wording --self-test",
  );
  process.exit(2);
}
