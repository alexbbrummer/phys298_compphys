# PHYS 298 — Course Website (MkDocs)

This repo builds a GitHub Pages course website using MkDocs + Material.

## Quick start (local)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# (Optional) sync .py lecture notes into .ipynb before serving
python tools/sync_notes.py

mkdocs serve
```

Open the local URL printed in your terminal.

## Publishing (GitHub Pages)

This repo includes a GitHub Action that deploys automatically on each push to `main`.

Steps in GitHub:
1. Settings → Pages
2. Source: Deploy from a branch
3. Branch: `gh-pages` / root

## Workflow for teaching notes (Spyder-friendly)

- Live-code notes: edit the `docs/notes/*.py` files (cell format using `# %%` and `# %% [markdown]`).
- Before publishing: run `python tools/sync_notes.py` (generates/updates paired `.ipynb` files).
- Commit + push.

MkDocs renders the resulting notebooks as nice HTML pages under the **Notes** section.
