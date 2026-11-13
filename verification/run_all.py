#!/usr/bin/env python3
"""Reproduce the exact scientific results and check local Markdown file links.

Run from the repository root with:
    python verification/run_all.py

The calculation writes into a temporary directory. The checked-in result file
is read only. All scientific fields are compared exactly; only top-level
reproducibility metadata is excluded because versions and timing can change.
"""

from __future__ import annotations

import argparse
import difflib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
from urllib.parse import unquote, urlsplit


VERIFICATION = Path(__file__).resolve().parent
ROOT = VERIFICATION.parent
REFERENCE = VERIFICATION / "results" / "certified_results.json"


def scientific_fields(data: dict) -> dict:
    """Exclude environment metadata, retaining every scientific result field."""
    return {key: value for key, value in data.items() if key != "reproducibility"}


def compare_results(actual_path: Path) -> None:
    expected = scientific_fields(json.loads(REFERENCE.read_text()))
    actual = scientific_fields(json.loads(actual_path.read_text()))
    if actual == expected:
        print("PASS: all scientific JSON fields match the checked-in exact results.", flush=True)
        return
    expected_lines = json.dumps(expected, indent=2, sort_keys=True).splitlines()
    actual_lines = json.dumps(actual, indent=2, sort_keys=True).splitlines()
    difference = list(difflib.unified_diff(
        expected_lines, actual_lines,
        fromfile="checked-in scientific results", tofile="reproduced scientific results",
        lineterm="",
    ))
    print("FAIL: scientific results differ:", file=sys.stderr)
    print("\n".join(difference[:200]), file=sys.stderr)
    if len(difference) > 200:
        print(f"... {len(difference) - 200} further diff lines omitted.", file=sys.stderr)
    raise SystemExit(1)


def check_local_markdown_links() -> None:
    """Check relative file targets in Markdown prose; fragments are not parsed.

    The repository uses inline links. Fenced code is excluded so code examples
    are not treated as documentation links. External URLs and anchor-only
    links are outside this file-existence check.
    """
    missing = []
    checked = 0
    link_pattern = re.compile(r"!?\[[^\]\n]*\]\(([^\n]*?)\)")
    for page in sorted(ROOT.rglob("*.md")):
        if ".git" in page.relative_to(ROOT).parts:
            continue
        prose = []
        fence = None
        for line in page.read_text().splitlines():
            marker = re.match(r"^\s*(`{3,}|~{3,})", line)
            if marker:
                char = marker.group(1)[0]
                if fence is None:
                    fence = char
                elif fence == char:
                    fence = None
                continue
            if fence is None:
                prose.append(line)
        for match in link_pattern.finditer("\n".join(prose)):
            raw = match.group(1).strip()
            if raw.startswith("<") and ">" in raw:
                raw = raw[1:raw.index(">")]
            else:
                # Optional Markdown title text is separated by whitespace.
                raw = raw.split(maxsplit=1)[0] if raw else ""
            target = urlsplit(raw)
            if target.scheme or target.netloc or not target.path:
                continue
            path = unquote(target.path)
            destination = ((ROOT / path.lstrip("/")) if path.startswith("/")
                           else (page.parent / path)).resolve()
            checked += 1
            if not destination.exists():
                missing.append(f"{page.relative_to(ROOT)} -> {raw}")
    if missing:
        print("FAIL: missing local Markdown link targets:", file=sys.stderr)
        print("\n".join(missing), file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {checked} local Markdown file links resolve.", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    if sys.flags.optimize:
        raise SystemExit("Run without -O or PYTHONOPTIMIZE so all exact checks remain enabled.")
    started = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix="collective-work-verification-") as temporary:
        output = Path(temporary)
        command = [
            sys.executable, str(VERIFICATION / "certify_collective_work.py"),
            "--output-dir", str(output), "--skip-plot",
        ]
        print("Reproducing the exact calculation in a temporary directory.", flush=True)
        subprocess.run(command, cwd=ROOT, check=True)
        compare_results(output / "certified_results.json")
    check_local_markdown_links()
    print(f"Verification passed in {time.perf_counter() - started:.2f} seconds.", flush=True)


if __name__ == "__main__":
    main()
