"""Sync Spyder-friendly .py notes into paired .ipynb notebooks via Jupytext.

Usage:
  python tools/sync_notes.py

It will:
- find docs/notes/*.py
- create/update matching .ipynb with paired formats (py:percent + ipynb)
- keep .py as the primary source of truth
"""

from __future__ import annotations
from pathlib import Path
import subprocess
import sys

NOTES_DIR = Path(__file__).resolve().parents[1] / "docs" / "notes"

def run(cmd: list[str]) -> None:
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        print(p.stdout)
        print(p.stderr, file=sys.stderr)
        raise SystemExit(p.returncode)

def main() -> None:
    if not NOTES_DIR.exists():
        print(f"Notes dir not found: {NOTES_DIR}")
        return

    py_files = sorted(NOTES_DIR.glob("*.py"))
    if not py_files:
        print("No .py notes found.")
        return

    for py in py_files:
        # Ensure paired format is set
        run([sys.executable, "-m", "jupytext", "--set-formats", "py:percent,ipynb", str(py)])
        # Sync paired notebook
        run([sys.executable, "-m", "jupytext", "--sync", str(py)])
        print(f"Synced: {py.name} -> {py.with_suffix('.ipynb').name}")

if __name__ == "__main__":
    main()
