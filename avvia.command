#!/bin/bash
# TypingDemo – avvio con doppio click
# Questo file si apre direttamente in Terminale

DIR="$(cd "$(dirname "$0")" && pwd)"

echo ""
echo "────────────────────────────────────────"
echo "  Avvio TypingDemo..."
echo "────────────────────────────────────────"
echo ""

# Installa pynput se non c'è
python3 -c "import pynput" 2>/dev/null || {
    echo "Installazione dipendenza pynput..."
    pip3 install pynput -q 2>/dev/null || pip install pynput -q 2>/dev/null || python3 -m pip install pynput -q
}

python3 "$DIR/typing_demo.py"

echo ""
echo "Premi Invio per chiudere questa finestra."
read
