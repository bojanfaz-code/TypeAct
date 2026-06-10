#!/bin/bash
# TypeAct – Launch menu bar app

DIR="$(cd "$(dirname "$0")" && pwd)"

# Use Homebrew Python if available (required for menu bar support), fallback to system
if [ -f "/opt/homebrew/bin/python3" ]; then
    PYTHON="/opt/homebrew/bin/python3"
    PIP="/opt/homebrew/bin/pip3"
else
    PYTHON="python3"
    PIP="pip3"
fi

echo ""
echo "────────────────────────────────────────"
echo "  Starting TypeAct..."
echo "────────────────────────────────────────"
echo ""

# Install dependencies if missing
"$PYTHON" -c "import pynput" 2>/dev/null || {
    echo "Installing pynput..."
    "$PIP" install pynput --break-system-packages -q 2>/dev/null || "$PYTHON" -m pip install pynput -q
}
"$PYTHON" -c "import rumps" 2>/dev/null || {
    echo "Installing rumps..."
    "$PIP" install rumps --break-system-packages -q 2>/dev/null || "$PYTHON" -m pip install rumps -q
}

# Launch the menu bar app in the background
"$PYTHON" "$DIR/typeact_app.py" &
disown

echo "  ✅ TypeAct is running!"
echo "     Look for the  TA ●  icon in your menu bar (top right)."
echo ""
echo "  You can close this window now."
echo ""
echo "  Press Enter to close."
read
