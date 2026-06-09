#!/bin/bash
# TypingDemo – Installazione automatica
# Esegui questo file UNA SOLA VOLTA sul tuo Mac.

DIR="$(cd "$(dirname "$0")" && pwd)"
clear

echo ""
echo "╔════════════════════════════════════════════════════╗"
echo "║          TypingDemo  –  Installazione              ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""
echo "  Configuro TypingDemo sul tuo Mac..."
echo ""

# ── 1. Verifica Python 3 ───────────────────────────────────────────────────
echo "  [1/3]  Verifica Python 3..."
if ! command -v python3 &>/dev/null; then
    echo ""
    echo "  ❌  Python 3 non trovato sul tuo Mac."
    echo ""
    echo "  Scaricalo da: https://www.python.org/downloads/"
    echo "  Dopo averlo installato, riavvia questo script."
    echo ""
    echo "  Premi Invio per chiudere."
    read; exit 1
fi
echo "       ✓  $(python3 --version) trovato"
echo ""

# ── 2. Installa pynput ────────────────────────────────────────────────────
echo "  [2/3]  Installazione dipendenza pynput..."
if python3 -c "import pynput" 2>/dev/null; then
    echo "       ✓  pynput già installato"
else
    pip3 install pynput -q 2>/dev/null \
        || python3 -m pip install pynput -q 2>/dev/null \
        || pip install pynput -q 2>/dev/null

    if python3 -c "import pynput" 2>/dev/null; then
        echo "       ✓  pynput installato con successo"
    else
        echo ""
        echo "  ❌  Installazione pynput fallita."
        echo "      Prova ad aprire il Terminale e digitare:"
        echo "      pip3 install pynput"
        echo ""
        echo "  Premi Invio per chiudere."
        read; exit 1
    fi
fi
echo ""

# ── 3. Permessi file ─────────────────────────────────────────────────────
echo "  [3/3]  Impostazione permessi..."
chmod +x "$DIR/INSTALLA.command"
chmod +x "$DIR/avvia.command"
echo "       ✓  File pronti"
echo ""

# ── Apertura Accessibilità ────────────────────────────────────────────────
echo "════════════════════════════════════════════════════════"
echo ""
echo "  ✅  Installazione completata!"
echo ""
echo "  ┌─────────────────────────────────────────────────┐"
echo "  │  PASSO FINALE OBBLIGATORIO – Permesso macOS     │"
echo "  ├─────────────────────────────────────────────────┤"
echo "  │                                                 │"
echo "  │  Sto aprendo le Impostazioni di Sistema...      │"
echo "  │                                                 │"
echo "  │  Devi aggiungere 'Terminal' all'elenco          │"
echo "  │  Accessibilità. Senza questo passaggio          │"
echo "  │  TypingDemo non funzionerà.                     │"
echo "  │                                                 │"
echo "  │  COME FARE:                                     │"
echo "  │  1. Clicca sul lucchetto 🔒 in basso a sinistra │"
echo "  │  2. Inserisci la password del Mac               │"
echo "  │  3. Clicca '+' e cerca Terminal                 │"
echo "  │  4. Attiva il toggle accanto a Terminal         │"
echo "  │                                                 │"
echo "  │  Per le istruzioni visive apri: GUIDA.html      │"
echo "  └─────────────────────────────────────────────────┘"
echo ""

# Apre direttamente il pannello Accessibilità
open "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility" 2>/dev/null \
|| open "/System/Library/PreferencePanes/Security.prefPane"

echo "  Quando hai finito, apri GUIDA.html per sapere"
echo "  come usare TypingDemo."
echo ""
echo "  Premi Invio per chiudere questa finestra."
read
