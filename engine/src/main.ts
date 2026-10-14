// Command-line entry: `node engine/dist/main.js build|render`.
// The build is the build-time checker: it fails on any error.

import { runBuild } from "./build.js";
import { renderAll } from "./render.js";

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
} else {
  console.error("usage: main.js build | render");
  process.exit(2);
}
