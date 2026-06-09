#!/usr/bin/env python3
"""
TypingDemo - Snippet expander con effetto di scrittura per macOS
------------------------------------------------
Digita un trigger (es. /1) in qualsiasi app e lo script
lo cancellerà e riscriverà il testo predefinito carattere
per carattere, simulando una vera digitazione.

REQUISITI:
  pip install pynput

PERMESSI RICHIESTI:
  Sistema → Privacy e sicurezza → Accessibilità
  → aggiungere Terminal (o Python) all'elenco
"""

import json
import time
import threading
import os
import sys
import random

# ── Installa pynput se mancante ────────────────────────────────────────────
try:
    from pynput import keyboard
    from pynput.keyboard import Key, Controller
except ImportError:
    print("pynput non trovato. Installazione in corso...")
    os.system(f'"{sys.executable}" -m pip install pynput -q')
    from pynput import keyboard
    from pynput.keyboard import Key, Controller

# ── Carica configurazione ──────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "snippets.json")

try:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)
except FileNotFoundError:
    print(f"❌  File snippets.json non trovato in:\n    {SCRIPT_DIR}")
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"❌  Errore nel file snippets.json: {e}")
    sys.exit(1)

SNIPPETS      = config.get("snippets", {})
TYPING_DELAY  = config.get("typing_delay", 0.045)   # secondi base tra un carattere e l'altro
DELETE_DELAY  = config.get("delete_delay", 0.02)    # secondi tra un backspace e l'altro

# ── Parametri variazione naturale (leggibili da snippets.json) ────────────
_PUNCT_BASE   = { ".": 4.5, "!": 4.0, "?": 4.0, ",": 2.2, ";": 2.5, ":": 2.0 }
SPACE_PAUSE   = 1.4
VARIATION        = config.get("variation",       0.55)
PUNCT_SCALE      = config.get("punct_scale",     1.0)
HESITATION_PROB  = config.get("hesitation_prob", 0.04)
HESITATION_EXTRA = (0.15, 0.40)


def human_delay(base: float, next_char: str = "") -> float:
    """Restituisce un delay realistico con variazione casuale."""
    # Variazione gaussiana centrata sul base delay
    d = random.gauss(base, base * VARIATION * 0.5)
    d = max(base * 0.3, min(base * 2.2, d))  # clamp tra 30% e 220%

    # Pausa extra dopo punteggiatura
    if next_char in _PUNCT_BASE:
        d *= _PUNCT_BASE[next_char] * PUNCT_SCALE
    elif next_char == " ":
        d *= SPACE_PAUSE

    # Micro-pausa casuale
    if random.random() < HESITATION_PROB:
        d += random.uniform(*HESITATION_EXTRA)

    return d

# ── Stato globale ──────────────────────────────────────────────────────────
kb         = Controller()
buffer     = ""
is_typing  = False
_lock      = threading.Lock()


# ── Logica di espansione ───────────────────────────────────────────────────
def expand_snippet(trigger: str, text: str) -> None:
    """Cancella il trigger e riscrive il testo con effetto typing."""
    global is_typing, buffer

    with _lock:
        is_typing = True
        buffer = ""

    try:
        time.sleep(0.06)  # piccola pausa prima di cancellare

        # Cancella i caratteri del trigger
        for _ in trigger:
            kb.tap(Key.backspace)
            time.sleep(DELETE_DELAY)

        time.sleep(0.08)  # pausa prima di iniziare a scrivere

        # Scrivi il testo un carattere alla volta con ritmo naturale
        for i, char in enumerate(text):
            kb.type(char)
            next_char = text[i + 1] if i + 1 < len(text) else ""
            time.sleep(human_delay(TYPING_DELAY, next_char))

    finally:
        with _lock:
            is_typing = False


# ── Listener tastiera ──────────────────────────────────────────────────────
def on_press(key) -> None:
    global buffer

    with _lock:
        if is_typing:
            return  # ignora input mentre stiamo scrivendo noi

    try:
        char = key.char
        if char is None:
            return

        buffer += char

        # Mantieni il buffer a 40 caratteri al massimo
        if len(buffer) > 40:
            buffer = buffer[-40:]

        # Controlla se il buffer termina con uno dei trigger
        for trigger, text in SNIPPETS.items():
            if buffer.endswith(trigger):
                t = threading.Thread(
                    target=expand_snippet,
                    args=(trigger, text),
                    daemon=True,
                )
                t.start()
                return

    except AttributeError:
        # Tasti speciali: aggiorna il buffer di conseguenza
        if key == Key.backspace:
            buffer = buffer[:-1] if buffer else ""
        elif key in (Key.space, Key.enter, Key.tab, Key.esc):
            buffer = ""


# ── Avvio ──────────────────────────────────────────────────────────────────
def main() -> None:
    W = 58
    print("\033[1m" + "─" * W + "\033[0m")
    print("\033[1m  TypingDemo  –  Snippet Expander con effetto scrittura\033[0m")
    print("\033[1m" + "─" * W + "\033[0m")

    if not SNIPPETS:
        print("\n⚠️   Nessuno snippet trovato in snippets.json!\n")
    else:
        print(f"\n\033[32m✓  {len(SNIPPETS)} snippet caricati:\033[0m\n")
        for trigger, text in SNIPPETS.items():
            preview = text[:55] + "…" if len(text) > 55 else text
            print(f"   \033[33m{trigger:6s}\033[0m  →  {preview}")

    print(f"\n   Velocità: {TYPING_DELAY * 1000:.0f} ms/carattere")
    print("\n\033[90m   In ascolto… digita un trigger in qualsiasi app.\033[0m")
    print("\033[90m   Premi Ctrl+C per uscire.\033[0m\n")

    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n\033[90mTypingDemo fermato.\033[0m\n")


if __name__ == "__main__":
    main()
