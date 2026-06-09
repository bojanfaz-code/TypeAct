#!/bin/bash
# TypeAct – Automatic installer
# Run this file ONCE on your Mac.

DIR="$(cd "$(dirname "$0")" && pwd)"
clear

echo ""
echo "╔════════════════════════════════════════════════════╗"
echo "║          TypeAct  –  Installer                  ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""
echo "  Setting up TypeAct on your Mac..."
echo ""

# ── 1. Check Python 3 ─────────────────────────────────────────────────────
echo "  [1/3]  Checking Python 3..."
if ! command -v python3 &>/dev/null; then
    echo ""
    echo "  ❌  Python 3 not found on your Mac."
    echo ""
    echo "  Download it from: https://www.python.org/downloads/"
    echo "  After installing, run this script again."
    echo ""
    echo "  Press Enter to close."
    read; exit 1
fi
echo "       ✓  $(python3 --version) found"
echo ""

# ── 2. Install pynput ─────────────────────────────────────────────────────
echo "  [2/3]  Installing pynput dependency..."
if python3 -c "import pynput" 2>/dev/null; then
    echo "       ✓  pynput already installed"
else
    pip3 install pynput -q 2>/dev/null \
        || python3 -m pip install pynput -q 2>/dev/null \
        || pip install pynput -q 2>/dev/null

    if python3 -c "import pynput" 2>/dev/null; then
        echo "       ✓  pynput installed successfully"
    else
        echo ""
        echo "  ❌  pynput installation failed."
        echo "      Open Terminal and type:"
        echo "      pip3 install pynput"
        echo ""
        echo "  Press Enter to close."
        read; exit 1
    fi
fi
echo ""

# ── 3. File permissions ───────────────────────────────────────────────────
echo "  [3/3]  Setting file permissions..."
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
echo "  │  list. Without this step TypeAct won't work. │"
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

echo "  Once done, open GUIDE.html to learn how to use TypeAct."
echo ""
echo "  Press Enter to close this window."
read
