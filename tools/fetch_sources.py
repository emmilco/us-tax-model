#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Deliberately archive public IRS sources, and Treasury regulations as printed in
the Federal Register (GovInfo, the Government Publishing Office edition); never
accepts return data.

Spreadsheets (`"format": "xls"`, the IRS Statistics of Income tables) are archived
as published, with their hash and no derived text.

Each archived PDF has three derived files beside it: `<id>.txt` (pdftotext -layout,
the geometry-preserving text), `<id>.cols.txt` (reading-order text from line boxes,
tools/extract_text.py) and `<id>.pages.json` (that tool's per-page classification).
The manifest records a hash for every file; `--derive` (re)builds the reading-order
pair for every archived PDF and records the hashes; with no flag the archive is
verified offline, every hash included.
"""
import argparse
import datetime
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import YEAR, Y  # noqa: E402
EXTRACT = ROOT / "tools" / "extract_text.py"
DERIVED = [("file", "sha256"), ("text_file", "text_sha256"), ("cols_file", "cols_sha256"), ("pages_file", "pages_sha256")]
ARCHIVE = ROOT / "sources" / Y
CATALOG = Path(__file__).with_name(f"sources-{Y}.json")
HOSTS = ("www.irs.gov", "www.govinfo.gov")


class ReadableHTML(HTMLParser):
    """Produce a search aid; the original HTML remains the cited snapshot."""

    def __init__(self):
        super().__init__()
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.hidden += 1
        if tag in ("p", "div", "li", "tr", "h1", "h2", "h3", "h4", "br"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)
        if tag in ("p", "div", "li", "tr", "h1", "h2", "h3", "h4"):
            self.parts.append("\n")
        if tag in ("td", "th"):
            self.parts.append(" | ")

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)

    def text(self):
        return "\n".join(" ".join(line.split()) for line in "".join(self.parts).splitlines() if line.strip()) + "\n"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def derive_reading_order(pdf, cols, pages):
    """Run the reading-order extractor; returns its tool version."""
    subprocess.run([sys.executable, str(EXTRACT), str(pdf), "--out", str(cols), "--pages", str(pages)], check=True, stdout=subprocess.DEVNULL)
    return json.loads(pages.read_text(encoding="utf-8"))["tool_version"]


def verify(entry):
    for file_key, hash_key in DERIVED:
        if file_key in entry and digest(ARCHIVE / entry[file_key]) != entry[hash_key]:
            raise ValueError(f"hash mismatch: {entry[file_key]}")


def write_manifest(manifest_path, manifest, existing):
    manifest["documents"] = sorted(existing.values(), key=lambda row: row["id"])
    temporary_manifest = manifest_path.with_suffix(".json.tmp")
    temporary_manifest.write_text(json.dumps(manifest, indent=2) + "\n")
    temporary_manifest.replace(manifest_path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true", help="explicitly allow network retrieval")
    parser.add_argument("--only", nargs="+", help="catalog IDs to fetch")
    parser.add_argument("--derive", action="store_true", help="(re)build the reading-order text and page classification of every archived PDF and record their hashes")
    args = parser.parse_args()
    catalog = json.loads(CATALOG.read_text())
    manifest_path = ARCHIVE / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {"tax_year": YEAR, "documents": []}
    existing = {entry["id"]: entry for entry in manifest["documents"]}
    if args.only and set(args.only) - {item["id"] for item in catalog}:
        parser.error("unknown source ID")
    if args.derive:
        if args.fetch or args.only:
            parser.error("--derive runs offline on the archive")
        for entry in existing.values():
            if entry.get("format", "pdf") != "pdf":
                continue
            if digest(ARCHIVE / entry["file"]) != entry["sha256"]:
                raise ValueError(f"hash mismatch: {entry['file']}")
            cols, pages = ARCHIVE / (entry["id"] + ".cols.txt"), ARCHIVE / (entry["id"] + ".pages.json")
            version = derive_reading_order(ARCHIVE / entry["file"], cols, pages)
            entry.update({"cols_file": cols.name, "cols_sha256": digest(cols), "pages_file": pages.name,
                          "pages_sha256": digest(pages), "extract_tool_version": version})
            print(f"Derived {entry['id']} (extract_text {version})", flush=True)
        write_manifest(manifest_path, manifest, existing)
        return
    if not args.fetch:
        if args.only:
            parser.error("--only requires --fetch")
        if not existing:
            parser.error("no archive; use --fetch deliberately")
        underived = []
        for entry in existing.values():
            verify(entry)
            if entry.get("format", "pdf") == "pdf" and "cols_file" not in entry:
                underived.append(entry["id"])
        missing = sorted({item["id"] for item in catalog} - set(existing))
        print(f"Verified {len(existing)} archived documents offline.")
        if underived:
            raise SystemExit("No reading-order text yet (run --derive): " + ", ".join(underived))
        if missing:
            raise SystemExit("Not yet archived: " + ", ".join(missing))
        return
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    for item in catalog:
        if args.only and item["id"] not in args.only:
            continue
        if item["id"] in existing:
            verify(existing[item["id"]])
            print(f"Preserved {item['id']}", flush=True)
            continue
        url = item["url"]
        if urlparse(url).scheme != "https" or urlparse(url).hostname not in HOSTS:
            raise ValueError("catalog must use HTTPS addresses on " + " or ".join(HOSTS))
        kind = item.get("format", "pdf")
        if kind not in ("pdf", "html", "xls"):
            raise ValueError("unsupported source format")
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / ("source." + kind)
            result = subprocess.run([
                "curl", "--fail", "--silent", "--show-error", "--location",
                "--proto", "=https", "--proto-redir", "=https", "--retry", "2",
                "--connect-timeout", "20", "--max-time", "120", "--output", str(source),
                "--write-out", "%{url_effective}", url,
            ], stdout=subprocess.PIPE, text=True, check=True)
            if urlparse(result.stdout).hostname not in HOSTS:
                raise ValueError("unexpected redirect host")
            txt = Path(temp) / "source.txt"
            if kind == "xls":
                if not source.read_bytes().startswith((b"\xd0\xcf\x11\xe0", b"PK\x03\x04")):
                    raise ValueError("source is not a spreadsheet")
            elif kind == "pdf":
                if not source.read_bytes().startswith(b"%PDF-"):
                    raise ValueError("source is not a PDF")
                subprocess.run(["pdftotext", "-layout", str(source), str(txt)], check=True)
            else:
                html = source.read_text(encoding="utf-8")
                if "<html" not in html.lower():
                    raise ValueError("source is not HTML")
                parser = ReadableHTML()
                parser.feed(html)
                txt.write_text(parser.text(), encoding="utf-8")
            entry = dict(item)
            entry.update({
                "resolved_url": result.stdout,
                "fetched_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "file": item["id"] + "." + kind, "sha256": digest(source),
                "revision": None,
                "revision_status": "Pending inspection of archived document; not cleared for encoding",
            })
            targets = [(source, ARCHIVE / entry["file"])]
            if kind != "xls":
                entry.update({"text_file": item["id"] + ".txt", "text_sha256": digest(txt)})
                targets.append((txt, ARCHIVE / entry["text_file"]))
            if kind == "pdf":
                cols, pages = Path(temp) / "source.cols.txt", Path(temp) / "source.pages.json"
                version = derive_reading_order(source, cols, pages)
                entry.update({"cols_file": item["id"] + ".cols.txt", "cols_sha256": digest(cols),
                              "pages_file": item["id"] + ".pages.json", "pages_sha256": digest(pages),
                              "extract_tool_version": version})
                targets += [(cols, ARCHIVE / entry["cols_file"]), (pages, ARCHIVE / entry["pages_file"])]
            for _, target in targets:
                if target.exists():
                    raise ValueError(f"refusing to overwrite unmanifested file: {target}")
            for origin, target in targets:
                target.write_bytes(origin.read_bytes())
            existing[entry["id"]] = entry
            write_manifest(manifest_path, manifest, existing)
            print(f"Archived {item['id']}", flush=True)


if __name__ == "__main__":
    main()
