#!/usr/bin/env python3
"""Send one tiny fixed prompt through the hosted DeepSeek transport of transcribe.call_model and
print the model the service reported and its token usage, nothing else. A deliberate network step;
the API key is read from the macOS keychain inside the transport and is never printed.

Usage: transport_check.py [--model deepseek-flash]
"""
import argparse, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from transcribe import MissingCredential, call_model  # noqa: E402

PROMPT = "Reply with the single word ok."
SYSTEM = "You answer exactly as instructed."


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="deepseek-flash")
    a = ap.parse_args()
    if not a.model.startswith("deepseek"):
        sys.exit(f"transport_check: {a.model!r} does not name a DeepSeek model")
    try:
        text, meta = call_model(PROMPT, a.model, timeout=120, system=SYSTEM)
    except MissingCredential as ex:
        sys.exit(f"transport_check: {ex}")
    except RuntimeError as ex:
        sys.exit(f"transport_check: {ex}")
    print(f"model requested: {a.model}")
    print(f"model reported: {', '.join(meta.get('model_reported', [])) or '-'}")
    print(f"usage: {json.dumps(meta.get('usage'), sort_keys=True)}")
    print(f"reply: {text.strip()[:40]!r}")


if __name__ == "__main__":
    main()
