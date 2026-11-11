#!/usr/bin/env python3
"""news-summary-01 entry (Python 3.13, standard library only).

Writes the summary of Wednesday 11 November 2026 world news held in
summary.txt to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The summary is 1-2000 UTF-8 characters, deterministic, no network.
Built by an AI coding agent (Muse) in a single session on 2026-11-12;
facts verified against Nov 11 2026 editions of BBC/AFP via Just Security
Early Edition, Rest of the World Report, and vietnam.vn before writing.
"""
import os
from pathlib import Path

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
summary = (Path(__file__).resolve().parent / "summary.txt").read_text(encoding="utf-8")
assert 1 <= len(summary) <= 2000, f"summary is {len(summary)} chars"
assert summary.strip(), "summary must not be only whitespace"
(out_dir / "entry.txt").write_text(summary, encoding="utf-8")
