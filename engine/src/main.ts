// Command-line entry: the backend of the system.
//
//   node engine/dist/main.js build                 build + check the data
//   node engine/dist/main.js render                render worksheets for review
//   node engine/dist/main.js eval --inputs F [--json]
//                                                  evaluate a return from inputs
//   node engine/dist/main.js conjecture            test the Tax Table conjecture

import { readFileSync } from "node:fs";
import { runBuild } from "./build.js";
import { renderAll } from "./render.js";
import { loadCanonical } from "./canonical.js";
import { evaluate } from "./eval.js";
import { renderValuesSheet, renderValuesHtml, resultToJson } from "./output.js";
import { runConjecture } from "./conjecture.js";
import { coverageReport, recordFixtures, testFixtures, reviewStage2, reviewStage3, reviewStage4 } from "./fixtures.js";
import { compareEvaluators } from "./compare.js";
import { runMutation } from "./mutate.js";

import { integrationChecks } from "./integration.js";
import { runChecks } from "./check.js";
import type { CanonicalData } from "./types.js";
import { runInterview } from "./interview.js";

const command = process.argv[2];

if (command === "review-stage4") {
  reviewStage4();
} else if (command === "review-stage3") {
  reviewStage3();
} else if (command === "review-stage2") {
  reviewStage2();
} else if (command === "test-integration") {
  integrationChecks();
} else if (command === "check") {
  const result = runChecks(JSON.parse(readFileSync(process.argv[3]!, "utf8")) as CanonicalData);
  console.log(JSON.stringify(result));
  process.exit(result.errors.length ? 1 : 0);
} else if (command === "interview") {
  runInterview(process.argv.slice(3));
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
  renderAll();
} else if (command === "eval") {
  const args = process.argv.slice(3);
  let inputsPath: string | null = null;
  let json = false;
  let html = false;
  let targetsOverride: string[] | null = null;
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--inputs") inputsPath = args[++i] ?? null;
    else if (args[i] === "--json") json = true;
    else if (args[i] === "--html") html = true;
    else if (args[i] === "--target") targetsOverride = (args[++i] ?? "").split(",").filter(Boolean);
    else {
      console.error(`eval: unknown argument '${args[i]}'`);
      process.exit(2);
    }
  }
  if (json && html) throw new Error("select either --json or --html");
  if (!inputsPath) {
    console.error("eval: --inputs <file.json> is required");
    process.exit(2);
  }
  const data = loadCanonical();
  const inputs = JSON.parse(readFileSync(inputsPath, "utf-8")) as Record<string, number | boolean | string>;
  const targets =
    targetsOverride ??
    [...data.forms].filter(d => !d.collection).flatMap((doc) => doc.lines.map((l) => l.id));
  const result = evaluate(data, inputs, targets);
  if (json) {
    console.log(resultToJson(result));
  } else if (html) {
    console.log(renderValuesHtml(data, result, data.forms.map(f=>f.id)));
  } else {
    console.log(renderValuesSheet(data, result, [...data.forms].map((f) => f.id)));
  }
} else if (command === "conjecture") {
  runConjecture();
} else if (command === "record-fixtures") {
  recordFixtures();
} else if (command === "test-fixtures") {
  process.exit(testFixtures() === 0 ? 0 : 1);
} else if (command === "coverage") {
  coverageReport();
} else if (command === "compare") {
  process.exit(compareEvaluators());
} else if (command === "mutate") {
  runMutation();
} else {
  console.error(
    "usage: main.js build | render | eval --inputs <file> [--json|--html] [--target <lines>] | interview start|advance|answer --log <file> | conjecture | record-fixtures | test-fixtures | test-integration | coverage | mutate | compare",
  );
  process.exit(2);
}
