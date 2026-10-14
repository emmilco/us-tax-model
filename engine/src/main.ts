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
import { renderValuesSheet, resultToJson } from "./output.js";
import { runConjecture } from "./conjecture.js";
import { coverageReport, recordFixtures, testFixtures } from "./fixtures.js";
import { compareEvaluators } from "./compare.js";
import { runMutation } from "./mutate.js";

const command = process.argv[2];

if (command === "build") {
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
  let targetsOverride: string[] | null = null;
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--inputs") inputsPath = args[++i] ?? null;
    else if (args[i] === "--json") json = true;
    else if (args[i] === "--target") targetsOverride = (args[++i] ?? "").split(",").filter(Boolean);
    else {
      console.error(`eval: unknown argument '${args[i]}'`);
      process.exit(2);
    }
  }
  if (!inputsPath) {
    console.error("eval: --inputs <file.json> is required");
    process.exit(2);
  }
  const data = loadCanonical();
  const inputs = JSON.parse(readFileSync(inputsPath, "utf-8")) as Record<string, number | boolean | string>;
  const targets =
    targetsOverride ??
    [...data.forms].flatMap((doc) => doc.lines.map((l) => l.id));
  const result = evaluate(data, inputs, targets);
  if (json) {
    console.log(resultToJson(result));
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
    "usage: main.js build | render | eval --inputs <file> [--json] | conjecture | record-fixtures | test-fixtures | coverage",
  );
  process.exit(2);
}
