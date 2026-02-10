# PDF Edit Tool

## Contents
- [General Information](#general-information)
- [Short Description / Background](#short-description--background)
- [Project Structure](#project-structure)
- [Files Directory](#files-directory)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## General Information
- Source Code: https://github.com/yudai-yam/edit_pdf

## Short Description / Background
This repository provides a tool to redact and replace text in PDF files using PyMuPDF. It supports configurable font, page, and replacement settings via a JSON configuration file. The tool is intended for batch or script-based PDF editing, such as anonymizing or updating documents.

## Project Structure

```
edit_pdf
├── main.py
├── config.json
├── pyproject.toml
├── tox.ini
├── segoe_font/
├── files/
│   └── .gitkeep
└── README.md
```

- `main.py`: Main script for PDF editing
- `config.json`: Configuration file for input/output, font, and replacements
- `segoe_font/`: Directory for font files (.ttf)
- `files/`: Directory for input/output PDFs (ignored by git except for .gitkeep)

## Files Directory
This is where you should place your input PDF files. The tool will read from and write to this directory as specified in `config.json`.

## Installation
Install the project dependencies using pip:

```sh
pip install -e .[dev]
```

For linting and testing, install tox and ruff:

```sh
pip install tox ruff
```

## Usage
1. Place your input PDF in the `files/` directory.
2. Edit `config.json` to specify the input/output file names, font, and replacements.
3. Run the script:

```sh
python main.py
```

To run linting:

```sh
tox -e ruff
```

## Configuration
Edit `config.json` to control:
- Input/output PDF file names and page number
- Font file, name, and size
- Text replacements (find/replace pairs)
- Redaction and insertion adjustments

Example `config.json`:

```json
{
  "pdf": {
    "input_file": "noriko.pdf",
    "output_file": "replaced.pdf",
    "page_number": 0
  },
  "font": {
    "fontfile": "segoe_ui.ttf",
    "fontname": "SegoeUI",
    "fontsize": 11
  },
  "replacements": [
    { "find": "25", "replace": "26" }
  ],
  "redaction": {
    "adjust_x1": 10,
    "adjust_y1": 6.1
  },
  "insertion": {
    "adjust_x1": 10,
    "adjust_y1": 0.6,
    "align": "CENTER"
  }
}
```

---

For more details, see the code and comments in `main.py`.
