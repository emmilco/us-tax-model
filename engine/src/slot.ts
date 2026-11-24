// The machine-wide check-all slots (tools/check_slot.py) for the engine commands that load the machine.
//
// A command of SLOT_COMMANDS started outside a check-all run (CHECK_ALL_SLOT unset: by hand, by an agent in a
// worktree, by a tool that is not a check step) first waits for one of the slots that check-all runs take, so that
// builds and test runs started beside the checks count against the same limit (tools/README.md, "Check-all slots").
// It takes the slot for its own process (check_slot.py --for-pid, which leaves a holder that frees the slot when this
// process exits, however it exits) and sets CHECK_ALL_SLOT and CHECK_ALL_MAX_RUNS, which its children inherit: a
// command it starts does not wait again, and the worker pools (pool.ts) size themselves to the runs holding slots.
// Inside a check-all run, release-prep or another holder the variable is already set, and nothing waits. A
// --self-test of these commands, and a tree without tools/check_slot.py, run at once. The slots decide only when a
// command starts, never what it does. main.ts imports this module before any other, so the wait comes before any
// work, the build cache's included.
import { spawnSync } from "node:child_process";
import { existsSync } from "node:fs";
import { join, resolve } from "node:path";
import { isMainThread } from "node:worker_threads";

export const SLOT_COMMANDS = new Set(["build", "test-fixtures", "test-integration", "test-serve", "interview-rules",
  "interview-length", "interview-coverage", "tick-groups", "mutate", "properties", "compare"]);

function takeSlot(command: string): void {
  const script = join(resolve(import.meta.dirname, "../.."), "tools", "check_slot.py");
  if (!existsSync(script)) return;
  const r = spawnSync("python3", [script, "--for-pid", String(process.pid), "--what", `node ${command}`],
    { stdio: ["ignore", "pipe", "inherit"], encoding: "utf-8" });
  if (r.error || r.status !== 0) {
    if (r.signal === "SIGINT" || r.signal === "SIGTERM") process.exit(130);
    console.error(`engine: no check-all slot taken (tools/check_slot.py: ${r.error?.message ?? `exit ${r.status}`}); running without one`);
    return;
  }
  for (const line of r.stdout.split("\n")) {
    const eq = line.indexOf("=");
    if (eq > 0) process.env[line.slice(0, eq)] = line.slice(eq + 1);
  }
}

const command = process.argv[2] ?? "";
if (isMainThread && SLOT_COMMANDS.has(command) && !process.env["CHECK_ALL_SLOT"] && !process.argv.includes("--self-test")) {
  takeSlot(command);
}
