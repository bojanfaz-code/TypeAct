# TypeAct

Typing effect snippet expander for macOS — simulate real-time typing during demos.

Type a short trigger (e.g. `/1`) in any app and the text appears character by character, as if you were typing it yourself. TypeAct runs silently as a **menu bar icon** — no Terminal window to keep open.

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

- macOS 10.15 Catalina or later (Apple Silicon recommended)
- Homebrew + Python 3 — **installed automatically** by `INSTALLA.command`
- Google Chrome (for the snippet management interface)

---

## Quick install

1. Download and unzip (link above)
2. Open Terminal and run:
```bash
chmod +x ~/Downloads/TypeAct-main/INSTALLA.command ~/Downloads/TypeAct-main/avvia.command
```
3. Double-click **`INSTALLA.command`** — installs Homebrew, Python 3 and all dependencies automatically *(takes a few minutes on first run)*
4. Follow the on-screen instructions to grant Accessibility permission
5. Open **`GUIDE.html`** in Chrome for the full visual guide

> ⚠️ The `chmod` step is required after downloading from GitHub — macOS strips executable permissions from ZIP archives.

> ⚠️ If macOS shows **"Not Opened — Apple could not verify..."**, don't click Move to Bin. Instead: **right-click → Open**. You only need to do this once per file.

> ⚠️ Accessibility permission is required. Without it, TypeAct cannot simulate keyboard input.

---

## Usage

**Before the demo:** double-click `avvia.command` — the **TA ●** icon appears in your menu bar. You can close the Terminal window.

**During the demo:** click in any text field and type a trigger — the text appears character by character.

**Menu bar controls:**

| Action | How |
|--------|-----|
| See loaded snippets | Click **TA ●** |
| Pause detection | **TA ●** → Pause → icon becomes **TA ○** |
| Resume detection | **TA ○** → Resume |
| Edit snippets | **TA ●** → Manage Snippets |
| Quit completely | **TA ●** → Quit TypeAct |

---

## Managing snippets

Open `gestisci_snippet.html` in Chrome, load your `snippets.json`, add or edit snippets and save with ⌘S. Restart `avvia.command` to reload.

---

## File overview

| File | Description |
|------|-------------|
| `INSTALLA.command` | Automatic installer — run once |
| `avvia.command` | Launches the menu bar app — run before each demo |
| `gestisci_snippet.html` | Visual snippet manager |
| `GUIDE.html` | Step-by-step visual guide |
| `typeact_app.py` | Menu bar app — do not edit |
| `typing_demo.py` | Typing engine — do not edit |
| `snippets.json` | Snippet configuration and speed settings |
