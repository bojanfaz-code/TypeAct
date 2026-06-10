#!/bin/bash
# TypeAct – Automatic installer
# Run this file ONCE on your Mac.

DIR="$(cd "$(dirname "$0")" && pwd)"
clear

echo ""
echo "╔════════════════════════════════════════════════════╗"
echo "║          TypeAct  –  Installer                     ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""
echo "  Setting up TypeAct on your Mac..."
echo ""

# ── 1. Install Homebrew + Python (required for menu bar support) ───────────
echo "  [1/4]  Checking Homebrew + Python..."
if [ ! -f "/opt/homebrew/bin/python3" ]; then
    echo "       Installing Homebrew (required for menu bar support)..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    echo "       Installing Python via Homebrew..."
    /opt/homebrew/bin/brew install python3
fi
PYTHON="/opt/homebrew/bin/python3"
PIP="/opt/homebrew/bin/pip3"
echo "       ✓  $($PYTHON --version) found"
echo ""

# ── 2. Install pynput ─────────────────────────────────────────────────────
echo "  [2/4]  Installing pynput..."
if "$PYTHON" -c "import pynput" 2>/dev/null; then
    echo "       ✓  pynput already installed"
else
    "$PIP" install pynput --break-system-packages -q 2>/dev/null
    if "$PYTHON" -c "import pynput" 2>/dev/null; then
        echo "       ✓  pynput installed"
    else
        echo "  ❌  pynput installation failed."
        read; exit 1
    fi
fi
echo ""

# ── 3. Install rumps ──────────────────────────────────────────────────────
echo "  [3/4]  Installing rumps (menu bar support)..."
if "$PYTHON" -c "import rumps" 2>/dev/null; then
    echo "       ✓  rumps already installed"
else
    "$PIP" install rumps --break-system-packages -q 2>/dev/null
    if "$PYTHON" -c "import rumps" 2>/dev/null; then
        echo "       ✓  rumps installed"
    else
        echo "  ❌  rumps installation failed."
        read; exit 1
    fi
fi
echo ""

# ── 4. File permissions ───────────────────────────────────────────────────
echo "  [4/4]  Setting file permissions..."
chmod +x "$DIR/INSTALLA.command"
chmod +x "$DIR/avvia.command"
echo "       ✓  Files ready"
echo ""

# ── Open Accessibility settings ───────────────────────────────────────────
echo "════════════════════════════════════════════════════════"
echo ""
echo "  ✅  Installation complete!"
echo ""
echo "  ┌─────────────────────────────────────────────────┐"
echo "  │  REQUIRED FINAL STEP – macOS Permission         │"
echo "  ├─────────────────────────────────────────────────┤"
echo "  │                                                 │"
echo "  │  Opening System Settings...                     │"
echo "  │                                                 │"
echo "  │  You must add 'Terminal' to the Accessibility   │"
echo "  │  list. Without this step TypeAct won't work.    │"
echo "  │                                                 │"
echo "  │  HOW TO:                                        │"
echo "  │  1. Click the lock 🔒 at the bottom left        │"
echo "  │  2. Enter your Mac password                     │"
echo "  │  3. Click '+' and find Terminal                 │"
echo "  │  4. Enable the toggle next to Terminal          │"
echo "  │                                                 │"
echo "  │  Open GUIDE.html for the full visual guide.     │"
echo "  └─────────────────────────────────────────────────┘"
echo ""

open "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility" 2>/dev/null \
|| open "/System/Library/PreferencePanes/Security.prefPane"

echo "  Once done, double-click avvia.command to start TypeAct."
echo ""
echo "  Press Enter to close this window."
read
