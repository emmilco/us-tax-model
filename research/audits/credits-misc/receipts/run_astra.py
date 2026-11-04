"""Run the fixed GPT-6 Astra prompt in an empty scratch directory; save the reply next to the prompt."""
import subprocess
import tempfile
from pathlib import Path

here = Path(__file__).resolve().parent
prompt = (here / "astra_prompt.txt").read_text()
with tempfile.TemporaryDirectory() as d:
    out = subprocess.run(["codex", "exec", "--skip-git-repo-check", "--ignore-user-config", "-s", "read-only",
                          "-m", "gpt-6-astra", prompt], cwd=d, capture_output=True, text=True, timeout=900)
(here / "astra_response.txt").write_text(out.stdout + ("\n--- stderr ---\n" + out.stderr if out.stderr else ""))
print("exit", out.returncode)
