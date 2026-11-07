// An interview-rules worker: loads the data once, then does the tasks the main thread posts (runTask in
// interview-rules.ts), one at a time, answering each with its result, and ends when it is sent null. The tax year
// comes from the main thread, put on the command line before year.ts loads.
import { parentPort, workerData } from "node:worker_threads";

const { year } = workerData as { year: number };
process.argv.push("--year", String(year));
const { loadContext, runTask } = await import("./interview-rules.js");
const context = loadContext();
parentPort!.on("message", (task: Parameters<typeof runTask>[1] | null) => {
  if (task === null) { parentPort!.close(); return; }
  try {
    parentPort!.postMessage({ ok: true, result: runTask(context, task) });
  } catch (e) {
    parentPort!.postMessage({ ok: false, error: e instanceof Error ? e.stack ?? e.message : String(e) });
  }
});
