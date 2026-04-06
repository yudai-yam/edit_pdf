# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```sh
# Install dependencies
pip install -e .[dev]

# Run the PDF editor
python main.py

# Lint
tox -e ruff
# or directly:
ruff check .
```

## Architecture

This is a single-script tool (`main.py`) that redacts and replaces text in PDF files using PyMuPDF.

**Flow:** `config.json` → `main.py` → reads PDF from `files/` → for each replacement: search text → redact (white-box) → insert new text → save output to `files/`

**Key detail — two-pass per replacement:** Redaction and insertion use separate rect adjustments (`redaction.adjust_*` vs `insertion.adjust_*`) from config. The rect returned by `page.search_for()` is mutated in-place, so the insertion rect is the already-adjusted redaction rect further modified by insertion adjustments.

**`config.json` schema:**
- `pdf.page_number`: 0-based page index
- `font.color`: RGB tuple as array `[r, g, b]` with values 0–1
- `redaction`/`insertion` `adjust_x1`/`adjust_y1`: pixel offsets applied to the bounding rect of found text
- `insertion.align`: `"LEFT"`, `"CENTER"`, or `"RIGHT"`

Input/output PDFs live in `files/` (git-ignored). Custom fonts go in `fonts/` (e.g., `fonts/segoe_ui.ttf`). To use a custom font, pass `fontfile` and `fontname` to `page.insert_textbox()`.
