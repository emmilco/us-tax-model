#!/usr/bin/env python3
"""Machine-wide limit on concurrent check-all runs.

    tools/check_slot.py [--tier T] [--tree TREE] -- COMMAND [ARGS...]

waits for a free slot, then replaces itself with COMMAND, which runs holding the slot.
At most CHECK_ALL_MAX_RUNS (default 2) commands hold slots at once, across every worktree
of the clone (the slot files live in the repository's common git dir, check-all-slots/),
and waiting runs start in arrival order. The slot is an flock on a slot file, inherited
by the command and its children: it is released when the last of them exits, whether
they finish, fail, are interrupted or are killed, so no stale slot outlives its run. A
waiter's place is a ticket file named by arrival time and pid; tickets of dead pids are
dropped, so a run killed while waiting leaves no place held. The command gets
CHECK_ALL_MAX_RUNS and CHECK_ALL_SLOT (the slot file) in its environment; the worker
pools of engine/src/pool.ts size themselves from the first.

    tools/check_slot.py --status       who holds the slots, who waits
    tools/check_slot.py --self-test
"""
import fcntl, json, os, shutil, signal, subprocess, sys, tempfile, time

POLL = 0.2


def max_runs():
    try:
        n = int(os.environ.get("CHECK_ALL_MAX_RUNS", ""))
    except ValueError:
        return 2
    return n if n > 0 else 2


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
    if h.get("tier"):
        bits.append(f"{h['tier']} tier")
    if h.get("tree"):
        bits.append(f"tree {h['tree'][:12]}")
    if h.get("worktree"):
        bits.append(h["worktree"])
    return ", ".join(bits)


def try_slot(d, n, info):
    for i in range(n):
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


def acquire(d, n, info, say):
    """Wait at the back of the queue; only the head tries the slots, so runs start in arrival order."""
    name = f"{time.time_ns():020d}-{os.getpid()}"
    ticket = os.path.join(d, "queue", name)
    open(ticket, "w").close()
    last = None
    try:
        while True:
            queue = tickets(d)
            if queue and queue[0][0] == name:
                got = try_slot(d, n, info)
                if got:
                    return got
            ahead = sum(1 for nm, _ in queue if nm < name)
            held = holders(d, n)
            state = (tuple(h["slot"] for h in held), ahead)
            if state != last:
                last = state
                who = "; ".join(describe(h) for h in held) or "none"
                say(f"check-all: waiting for a slot (at most {n} runs at once; {ahead} ahead of this one); running: {who}")
            time.sleep(POLL)
    finally:
        try:
            os.unlink(ticket)
        except FileNotFoundError:
            pass


def status():
    d, n = slot_dir(), max_runs()
    hs = holders(d, n)
    print(f"{len(hs)} of {n} check-all slots held")
    for h in hs:
        print("  running: " + describe(h))
    for _, pid in tickets(d):
        print(f"  waiting: pid {pid}")


def run(argv):
    tier = tree = ""
    while argv and argv[0] != "--":
        if argv[0] == "--tier":
            tier = argv[1]
            argv = argv[2:]
        elif argv[0] == "--tree":
            tree = argv[1]
            argv = argv[2:]
        else:
            sys.exit(f"check_slot: unknown argument {argv[0]}")
    cmd = argv[1:]
    if not cmd:
        sys.exit("check_slot: no command")
    d, n = slot_dir(), max_runs()
    info = {"pid": os.getpid(), "tier": tier, "tree": tree, "worktree": os.getcwd(), "started": time.strftime("%Y-%m-%d %H:%M:%S")}
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(143))  # runs the ticket cleanup
    fd, path = acquire(d, n, info, lambda m: print(m, file=sys.stderr, flush=True))
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    os.set_inheritable(fd, True)
    os.environ["CHECK_ALL_MAX_RUNS"] = str(n)
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
        script = (f"import os,time;open({tmp!r}+'/started-{name}','w').close()\n"
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
    shutil.rmtree(tmp, ignore_errors=True)
    print("check_slot self-test: ok")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--self-test"]:
        self_test()
    elif a == ["--status"]:
        status()
    else:
        run(a)
