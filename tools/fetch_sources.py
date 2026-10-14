#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Deliberately archive public IRS sources; never accepts return data."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "sources" / "2025"
CATALOG = Path(__file__).with_name("sources-2025.json")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true", help="explicitly allow network retrieval")
    parser.add_argument("--only", nargs="+", help="catalog IDs to fetch")
    args = parser.parse_args()
    catalog = json.loads(CATALOG.read_text())
    manifest_path = ARCHIVE / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {"tax_year": 2025, "documents": []}
    existing = {entry["id"]: entry for entry in manifest["documents"]}
    if args.only and set(args.only) - {item["id"] for item in catalog}:
        parser.error("unknown source ID")
    if not args.fetch:
        if args.only:
            parser.error("--only requires --fetch")
        if not existing:
            parser.error("no archive; use --fetch deliberately")
        for entry in existing.values():
            for file_key, hash_key in [("file", "sha256"), ("text_file", "text_sha256")]:
                if file_key in entry and digest(ARCHIVE / entry[file_key]) != entry[hash_key]:
                    raise ValueError(f"hash mismatch: {entry[file_key]}")
        missing = sorted({item["id"] for item in catalog} - set(existing))
        print(f"Verified {len(existing)} archived documents offline.")
        if missing:
            raise SystemExit("Not yet archived: " + ", ".join(missing))
        return
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    for item in catalog:
        if args.only and item["id"] not in args.only:
            continue
        if item["id"] in existing:
            entry = existing[item["id"]]
            if digest(ARCHIVE / entry["file"]) != entry["sha256"]:
                raise ValueError(f"hash mismatch: {entry['file']}")
            print(f"Preserved {item['id']}", flush=True)
            continue
        url = item["url"]
        if urlparse(url).scheme != "https" or urlparse(url).hostname != "www.irs.gov":
            raise ValueError("catalog must use HTTPS www.irs.gov addresses")
        with tempfile.TemporaryDirectory() as temp:
            pdf = Path(temp) / "source.pdf"
            result = subprocess.run([
                "curl", "--fail", "--silent", "--show-error", "--location",
                "--proto", "=https", "--proto-redir", "=https", "--retry", "2",
                "--connect-timeout", "20", "--max-time", "120", "--output", str(pdf),
                "--write-out", "%{url_effective}", url,
            ], stdout=subprocess.PIPE, text=True, check=True)
            if urlparse(result.stdout).hostname != "www.irs.gov":
                raise ValueError("unexpected redirect host")
            if not pdf.read_bytes().startswith(b"%PDF-"):
                raise ValueError("source is not a PDF")
            txt = Path(temp) / "source.txt"
            subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True)
            entry = dict(item)
            entry.update({
                "resolved_url": result.stdout,
                "fetched_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "file": item["id"] + ".pdf", "sha256": digest(pdf),
                "text_file": item["id"] + ".txt", "text_sha256": digest(txt),
                "revision": None,
                "revision_status": "Pending inspection of archived document; not cleared for encoding",
            })
            for source, key in [(pdf, "file"), (txt, "text_file")]:
                target = ARCHIVE / entry[key]
                if target.exists():
                    raise ValueError(f"refusing to overwrite unmanifested file: {target}")
                target.write_bytes(source.read_bytes())
            existing[entry["id"]] = entry
            manifest["documents"] = sorted(existing.values(), key=lambda row: row["id"])
            temporary_manifest = manifest_path.with_suffix(".json.tmp")
            temporary_manifest.write_text(json.dumps(manifest, indent=2) + "\n")
            temporary_manifest.replace(manifest_path)
            print(f"Archived {item['id']}", flush=True)


if __name__ == "__main__":
    main()
