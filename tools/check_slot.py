#!/usr/bin/env python3
"""Machine-wide limit on concurrent check-all runs.

    tools/check_slot.py [--tier T] [--tree TREE] [--what TEXT] -- COMMAND [ARGS...]
    tools/check_slot.py --for-pid PID [--what TEXT]

waits for a free slot, then replaces itself with COMMAND, which runs holding the slot. With --for-pid, it takes the
slot for the running process PID instead: it leaves a holder process that keeps the slot until PID exits, prints
the two variables below as NAME=VALUE lines for PID to set, and exits (engine/src/slot.ts: an engine command that
loads the machine, started outside a check-all run, takes a slot this way before it starts its work).
Across every worktree of the clone (the slot files live in the repository's common git dir,
check-all-slots/), waiting runs start in arrival order, and at once hold slots:

- with CHECK_ALL_MAX_RUNS set, at most that many runs;
- without it, FLOOR (2) runs always, and up to cap() runs while the machine has room for one
  more: a run beyond the floor starts only while the one-minute load average is at most the core
  count less RUN_CORES, and the memory available (free, inactive and speculative pages) is at
  least RUN_MEM. The constants are a light run's measured demand. The slot is an flock on a slot file, inherited
by the command and its children: it is released when the last of them exits, whether
they finish, fail, are interrupted or are killed, so no stale slot outlives its run. A
waiter's place is a ticket file named by arrival time and pid; tickets of dead pids are
dropped, so a run killed while waiting leaves no place held. The command gets
CHECK_ALL_MAX_RUNS and CHECK_ALL_SLOT (the slot file) in its environment; the worker
pools of engine/src/pool.ts size themselves from the first, which is the limit when one is
set, else the number of runs holding slots when this one started (at least FLOOR). The
slots decide only when a run starts, never what it checks.

    tools/check_slot.py --status       who holds the slots, who waits
    tools/check_slot.py --self-test
"""
import fcntl, json, os, shutil, signal, subprocess, sys, tempfile, time

POLL = 0.2
FLOOR = 2
# A light check-all run's demand, measured on this machine (18 cores, 64 GB, pools sized for two runs): the cores it
# keeps busy on average (its CPU time over its wall time, 5.0) and the memory its processes hold at their peak (5.0 GB),
# with a margin.
RUN_CORES = 5
RUN_MEM = 6 << 30


def fixed_runs():
    """CHECK_ALL_MAX_RUNS when it is set to a positive whole number, else None."""
    try:
        n = int(os.environ.get("CHECK_ALL_MAX_RUNS", ""))
    except ValueError:
        return None
    return n if n > 0 else None


def total_memory():
    try:
        return int(subprocess.run(["sysctl", "-n", "hw.memsize"], capture_output=True, text=True, check=True).stdout)
    except (OSError, ValueError, subprocess.CalledProcessError):
        return os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")


def cap():
    """The most runs at once without a set limit: as many as the cores and the memory hold, at least FLOOR."""
    cores = os.cpu_count() or 2
    return max(FLOOR, min(cores // RUN_CORES, total_memory() // RUN_MEM))


def max_runs():
    return fixed_runs() or cap()


def available_memory():
    """Bytes of memory available now: free, inactive and speculative pages (vm_stat), or MemAvailable on Linux."""
    try:
        out = subprocess.run(["vm_stat"], capture_output=True, text=True, check=True).stdout
        page = int(out.split("page size of ")[1].split(" ")[0])
        pages = {k.strip(): int(v.strip().rstrip(".")) for k, v in (l.split(":", 1) for l in out.splitlines()[1:] if ":" in l)
                 if v.strip().rstrip(".").isdigit()}
        return page * sum(pages.get(k, 0) for k in ("Pages free", "Pages inactive", "Pages speculative"))
    except (OSError, IndexError, ValueError, subprocess.CalledProcessError):
        try:
            for line in open("/proc/meminfo"):
                if line.startswith("MemAvailable:"):
                    return int(line.split()[1]) * 1024
        except OSError:
            pass
    return 0


def measure():
    """(one-minute load average, bytes available). A file named by CHECK_ALL_SLOT_MEASURE, holding "<load> <bytes>",
    stands in for the machine (the self-test)."""
    planted = os.environ.get("CHECK_ALL_SLOT_MEASURE")
    if planted:
        load, mem = open(planted).read().split()
        return float(load), int(mem)
    return os.getloadavg()[0], available_memory()


def room():
    """Whether the machine has room for one more run beyond the floor, and why not."""
    load, mem = measure()
    cores = os.cpu_count() or 2
    if load > cores - RUN_CORES:
        return False, f"load {load:.1f} on {cores} cores"
    if mem < RUN_MEM:
        return False, f"{mem / (1 << 30):.1f} GB available"
    return True, ""


def slot_dir():
    d = os.environ.get("CHECK_ALL_SLOT_DIR")
    if not d:
        common = subprocess.run(["git", "rev-parse", "--git-common-dir"], capture_output=True, text=True, check=True).stdout.strip()
        d = os.path.join(os.path.abspath(common), "check-all-slots")
    os.makedirs(os.path.join(d, "queue"), exist_ok=True)
    return d


def alive(pid):
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def tickets(d):
    """Live tickets in arrival order, as (name, pid); tickets of dead pids are removed."""
    out = []
    for name in sorted(os.listdir(os.path.join(d, "queue"))):
        try:
            pid = int(name.rsplit("-", 1)[1])
        except (IndexError, ValueError):
            continue
        if alive(pid):
            out.append((name, pid))
        else:
            try:
                os.unlink(os.path.join(d, "queue", name))
            except FileNotFoundError:
                pass
    return out


def holders(d, n):
    """Info of the slots currently held (a held slot's file names its holder; a free slot's is ignored)."""
    out = []
    for i in range(n):
        path = os.path.join(d, f"slot-{i}")
        try:
            fd = os.open(path, os.O_RDWR)
        except FileNotFoundError:
            continue
        try:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                fcntl.flock(fd, fcntl.LOCK_UN)
                continue  # free
            except BlockingIOError:
                pass
            try:
                info = json.loads(os.read(fd, 4096) or b"{}")
            except ValueError:
                info = {}
            info["slot"] = i
            out.append(info)
        finally:
            os.close(fd)
    return out


def describe(h):
    bits = [f"pid {h.get('pid', '?')}"]
    if h.get("what"):
        bits.append(h["what"])
    if h.get("tier"):
        bits.append(f"{h['tier']} tier")
    if h.get("tree"):
        bits.append(f"tree {h['tree'][:12]}")
    if h.get("worktree"):
        bits.append(h["worktree"])
    return ", ".join(bits)


def try_slot(d, n, info, floor=None):
    """Take a free slot of the first n; one at or beyond `floor` only while the machine has room (room())."""
    measured = None
    for i in range(n):
        if floor is not None and i >= floor:
            if measured is None:
                measured = room()[0]
            if not measured:
                return None
        fd = os.open(os.path.join(d, f"slot-{i}"), os.O_RDWR | os.O_CREAT, 0o644)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            os.close(fd)
            continue
        os.ftruncate(fd, 0)
        os.write(fd, json.dumps(info).encode())
        return fd, os.path.join(d, f"slot-{i}")
    return None


def acquire(d, n, info, say, floor=None):
    """Wait at the back of the queue; only the head tries the slots, so runs start in arrival order."""
    name = f"{time.time_ns():020d}-{os.getpid()}"
    ticket = os.path.join(d, "queue", name)
    open(ticket, "w").close()
    last = None
    try:
        while True:
            queue = tickets(d)
            if queue and queue[0][0] == name:
                got = try_slot(d, n, info, floor)
                if got:
                    return got
            ahead = sum(1 for nm, _ in queue if nm < name)
            held = holders(d, n)
            limit = f"at most {n} runs at once" if floor is None else f"{floor} runs at once, up to {n} while the machine has room"
            why = room()[1] if floor is not None and len(held) >= floor else ""
            state = (tuple(h["slot"] for h in held), ahead, bool(why))
            if state != last:
                last = state
                who = "; ".join(describe(h) for h in held) or "none"
                say(f"check-all: waiting for a slot ({limit}{'; no room: ' + why if why else ''}; {ahead} ahead of this one); running: {who}")
            time.sleep(POLL)
    finally:
        try:
            os.unlink(ticket)
        except FileNotFoundError:
            pass


def status():
    d, n = slot_dir(), max_runs()
    hs = holders(d, n)
    if fixed_runs():
        print(f"{len(hs)} of {n} check-all slots held")
    else:
        ok, why = room()
        print(f"{len(hs)} check-all slots held ({FLOOR} always, up to {n} while the machine has room: {'room now' if ok else 'no room, ' + why})")
    for h in hs:
        print("  running: " + describe(h))
    for _, pid in tickets(d):
        print(f"  waiting: pid {pid}")


def hold_for(fd, pid):
    """Fork a holder that keeps the slot's lock until process `pid` exits, then return. The holder keeps no other
    file open, so a caller reading this process's output sees it end when this process exits."""
    if os.fork():
        return
    os.setsid()
    null = os.open(os.devnull, os.O_RDWR)
    for std in (0, 1, 2):
        os.dup2(null, std)
    os.closerange(3, fd)
    os.closerange(fd + 1, 4096)
    while alive(pid):
        time.sleep(POLL)
    os._exit(0)


def run(argv):
    tier = tree = what = ""
    for_pid = None
    while argv and argv[0] != "--":
        if argv[0] == "--tier":
            tier = argv[1]
            argv = argv[2:]
        elif argv[0] == "--tree":
            tree = argv[1]
            argv = argv[2:]
        elif argv[0] == "--for-pid":
            for_pid = int(argv[1])
            argv = argv[2:]
        elif argv[0] == "--what":
            what = argv[1]
            argv = argv[2:]
        else:
            sys.exit(f"check_slot: unknown argument {argv[0]}")
    cmd = argv[1:]
    if not cmd and for_pid is None:
        sys.exit("check_slot: no command")
    d, n, fixed = slot_dir(), max_runs(), fixed_runs()
    info = {"pid": for_pid or os.getpid(), "what": what, "tier": tier, "tree": tree, "worktree": os.getcwd(),
            "started": time.strftime("%Y-%m-%d %H:%M:%S")}
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(143))  # runs the ticket cleanup
    fd, path = acquire(d, n, info, lambda m: print(m, file=sys.stderr, flush=True), None if fixed else min(FLOOR, n))
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    # The pools share the cores among the runs that may hold slots now: the set limit, or the runs holding slots.
    runs = str(fixed or max(FLOOR, len(holders(d, n))))
    if for_pid is not None:
        hold_for(fd, for_pid)
        print(f"CHECK_ALL_SLOT={path}\nCHECK_ALL_MAX_RUNS={runs}", flush=True)
        os._exit(0)
    os.set_inheritable(fd, True)
    os.environ["CHECK_ALL_MAX_RUNS"] = runs
    os.environ["CHECK_ALL_SLOT"] = path
    os.execvp(cmd[0], cmd)


def self_test():
    me = os.path.abspath(__file__)
    tmp = tempfile.mkdtemp(prefix="slot-test.")
    sd = os.path.join(tmp, "slots")
    env = dict(os.environ, CHECK_ALL_SLOT_DIR=sd, CHECK_ALL_MAX_RUNS="2")
    procs = []

    def fail(msg):
        for p in procs:
            if p.poll() is None:
                p.kill()
        sys.exit(f"check_slot self-test: {msg}")

    def start(name):
        """A run that touches started-NAME, then waits for release-NAME."""
        script = (f"import os,time;open({tmp!r}+'/runs-{name}','w').write(os.environ['CHECK_ALL_MAX_RUNS']);"
                  f"open({tmp!r}+'/started-{name}','w').close()\n"
                  f"while not os.path.exists({tmp!r}+'/release-{name}'): time.sleep(0.05)")
        p = subprocess.Popen([sys.executable, me, "--", sys.executable, "-c", script], env=env, stderr=subprocess.DEVNULL)
        procs.append(p)
        return p

    def started(name):
        return os.path.exists(f"{tmp}/started-{name}")

    def release(name):
        open(f"{tmp}/release-{name}", "w").close()

    def until(cond, what, t=20):
        end = time.time() + t
        while time.time() < end:
            if cond():
                return
            time.sleep(0.05)
        fail(what)

    def stays_false(cond, what, t=1.0):
        end = time.time() + t
        while time.time() < end:
            if cond():
                fail(what)
            time.sleep(0.05)

    start("a")
    until(lambda: started("a"), "first run did not start")
    start("b")
    until(lambda: started("b"), "second run did not start")
    start("c")
    stays_false(lambda: started("c"), "a third run started while two held slots")
    start("d")
    stays_false(lambda: started("c") or started("d"), "a waiting run started with both slots held")
    release("a")
    until(lambda: started("c"), "the third run did not start when a slot freed")
    stays_false(lambda: started("d"), "the fourth run started out of order or beyond the limit")
    release("b")
    until(lambda: started("d"), "the fourth run did not start when a second slot freed")
    release("c")
    release("d")
    for p in procs:
        if p.wait(timeout=20) != 0:
            fail("a run exited non-zero")
    procs.clear()

    # A holder killed outright (no cleanup) frees its slot; a dead pid's ticket at the head of
    # the queue blocks no one.
    hold = [subprocess.Popen([sys.executable, me, "--", "sleep", "300"], env=env) for _ in range(2)]
    procs.extend(hold)
    os.environ["CHECK_ALL_SLOT_DIR"] = sd
    until(lambda: len(holders(sd, 2)) == 2, "the held slots are not reported as held")
    dead = subprocess.Popen(["true"])
    dead.wait()
    open(os.path.join(sd, "queue", f"{1:020d}-{dead.pid}"), "w").close()
    e = start("e")
    stays_false(lambda: started("e"), "a run started with both slots held")
    hold[0].kill()
    hold[0].wait()
    until(lambda: started("e"), "the slot of a killed holder was not reclaimed")
    if os.listdir(os.path.join(sd, "queue")):
        fail("tickets left in the queue")
    # A waiter terminated while waiting leaves no ticket.
    f = start("f")
    time.sleep(0.8)
    f.terminate()
    f.wait(timeout=10)
    if os.listdir(os.path.join(sd, "queue")):
        fail("a terminated waiter left its ticket")
    release("e")
    e.wait(timeout=20)
    hold[1].kill()
    hold[1].wait()
    # A limit of one serializes.
    env["CHECK_ALL_MAX_RUNS"] = "1"
    start("g")
    until(lambda: started("g"), "run g did not start")
    h = start("h")
    stays_false(lambda: started("h"), "a second run started with a limit of one")
    release("g")
    until(lambda: started("h"), "run h did not start after g")
    release("h")
    h.wait(timeout=20)
    # --for-pid: the slot is held for another process until it exits, and the call returns once it is taken.
    owner = subprocess.Popen(["sleep", "300"])
    procs.append(owner)
    try:
        got = subprocess.run([sys.executable, me, "--for-pid", str(owner.pid), "--what", "node build"], env=env,
                             capture_output=True, text=True, timeout=20)
    except subprocess.TimeoutExpired:
        fail("--for-pid did not return once it held the slot")
    if got.returncode != 0 or got.stdout.split() != [f"CHECK_ALL_SLOT={sd}/slot-0", "CHECK_ALL_MAX_RUNS=1"]:
        fail(f"--for-pid printed {got.stdout!r} (exit {got.returncode})")
    if "node build" not in subprocess.run([sys.executable, me, "--status"], env=env, capture_output=True, text=True).stdout:
        fail("--status does not name what holds the slot")
    m = start("m")
    stays_false(lambda: started("m"), "a run started while the slot was held for another process")
    owner.kill()
    owner.wait()
    until(lambda: started("m"), "the slot held for a process was not freed when it exited")
    release("m")
    m.wait(timeout=20)
    # Without a set limit: FLOOR runs always; one more only while the planted load and memory leave room for it, with
    # the pools sized to the runs holding slots.
    measured = ""
    if cap() >= FLOOR + 1:
        del env["CHECK_ALL_MAX_RUNS"]
        os.environ.pop("CHECK_ALL_MAX_RUNS", None)
        plant = os.path.join(tmp, "measure")
        env["CHECK_ALL_SLOT_MEASURE"] = plant
        cores = os.cpu_count() or 2
        with open(plant, "w") as f:
            f.write(f"{cores} {RUN_MEM * 4}")
        start("i")
        start("j")
        until(lambda: started("i") and started("j"), f"the first {FLOOR} runs did not start without a set limit")
        start("k")
        stays_false(lambda: started("k"), "a run beyond the floor started with the load at the core count")
        with open(plant, "w") as f:
            f.write(f"0.5 {RUN_MEM * 4}")
        until(lambda: started("k"), "a run beyond the floor did not start with room for it")
        runs_k = open(f"{tmp}/runs-k").read()
        if runs_k != str(FLOOR + 1):
            fail(f"the run beyond the floor sized its pools to {runs_k} runs, not {FLOOR + 1}")
        with open(plant, "w") as f:
            f.write(f"0.5 {RUN_MEM // 2}")
        start("l")
        stays_false(lambda: started("l"), "a run beyond the floor started with too little memory available")
        release("i")
        until(lambda: started("l"), "a run did not start in a slot of the floor")
        for x in ("j", "k", "l"):
            release(x)
        for p in procs:
            p.wait(timeout=20)
        measured = f"; beyond the floor of {FLOOR}, a run starts only with room for it"
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"check_slot self-test: ok{measured}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--self-test"]:
        self_test()
    elif a == ["--status"]:
        status()
    else:
        run(a)
