#!/bin/bash
# TypeAct – Start script

DIR="$(cd "$(dirname "$0")" && pwd)"

echo ""
echo "────────────────────────────────────────"
echo "  Starting TypeAct..."
echo "────────────────────────────────────────"
echo ""

# Install pynput if missing
python3 -c "import pynput" 2>/dev/null || {
    echo "Installing pynput dependency..."
    pip3 install pynput -q 2>/dev/null || pip install pynput -q 2>/dev/null || python3 -m pip install pynput -q
}

python3 "$DIR/typing_demo.py"

echo ""
echo "Press Enter to close this window."
read
