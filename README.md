# TypeAct

Typing effect snippet expander for macOS — simulate real-time typing during demos.

Type a short trigger (e.g. `/1`) in any app and the text appears character by character, as if you were typing it yourself.

Works everywhere: Slack, browser, Teams, PowerPoint, and any other text field.

---

## ⬇️ Download

**[Download latest version (ZIP)](https://github.com/bojanfaz-code/TypeAct/archive/refs/heads/main.zip)**

or clone the repository:
```bash
git clone https://github.com/bojanfaz-code/TypeAct.git
```

---

## Requirements

- macOS (10.15 Catalina or later)
- Python 3 (already included on macOS, or from [python.org](https://www.python.org/downloads/))
- Google Chrome (for the snippet management interface)

---

## Quick install

1. Download and unzip (link above)
2. Double-click **`INSTALLA.command`**
3. Follow the on-screen instructions to grant Accessibility permission
4. Open **`GUIDE.html`** in Chrome for the full visual guide

> ⚠️ Accessibility permission is required. Without it, the script cannot simulate keyboard input.

---

## Usage

**Before the demo:** double-click `avvia.command` and minimise the window.

**During the demo:** type a trigger (e.g. `/1`) in any text field — the script replaces it with the full text, character by character.

---

## Managing snippets

Open `gestisci_snippet.html` in Chrome to add, edit or delete snippets through a visual interface. Save with ⌘S.

The `snippets.json` file holds your configuration (snippets + speed settings).

---

## File overview

| File | Description |
|------|-------------|
| `INSTALLA.command` | Automatic installer — run once |
| `avvia.command` | Starts the script — run before each demo |
| `gestisci_snippet.html` | Visual snippet manager |
| `GUIDE.html` | Step-by-step visual guide |
| `typing_demo.py` | Main script (do not edit) |
| `snippets.json` | Snippet configuration and speed settings |
