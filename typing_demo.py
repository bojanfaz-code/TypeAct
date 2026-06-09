#!/usr/bin/env python3
"""
TypeAct - Typing effect snippet expander for macOS
------------------------------------------------------
Type a trigger (e.g. /1) in any app and the script
deletes it and retypes the predefined text character
by character, simulating real human typing.

REQUIREMENTS:
  pip install pynput

PERMISSIONS REQUIRED:
  System Settings → Privacy & Security → Accessibility
  → add Terminal (or Python) to the list
"""

import json
import time
import threading
import os
import sys
import random

# ── Install pynput if missing ──────────────────────────────────────────────
try:
    from pynput import keyboard
    from pynput.keyboard import Key, Controller
except ImportError:
    print("pynput not found. Installing...")
    os.system(f'"{sys.executable}" -m pip install pynput -q')
    from pynput import keyboard
    from pynput.keyboard import Key, Controller

# ── Load configuration ─────────────────────────────────────────────────────
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "snippets.json")

try:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)
except FileNotFoundError:
    print(f"❌  snippets.json not found in:\n    {SCRIPT_DIR}")
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"❌  Error in snippets.json: {e}")
    sys.exit(1)

SNIPPETS     = config.get("snippets", {})
TYPING_DELAY = config.get("typing_delay", 0.045)   # base delay between characters (seconds)
DELETE_DELAY = config.get("delete_delay", 0.02)    # delay between backspaces (seconds)

# ── Natural variation parameters (configurable in snippets.json) ───────────
_PUNCT_BASE      = { ".": 4.5, "!": 4.0, "?": 4.0, ",": 2.2, ";": 2.5, ":": 2.0 }
SPACE_PAUSE      = 1.4
VARIATION        = config.get("variation",       0.55)   # rhythm variation (0=robotic, 1=chaotic)
PUNCT_SCALE      = config.get("punct_scale",     1.0)    # punctuation pause multiplier
HESITATION_PROB  = config.get("hesitation_prob", 0.04)   # random micro-pause probability
HESITATION_EXTRA = (0.15, 0.40)                          # micro-pause duration range (seconds)


def human_delay(base: float, next_char: str = "") -> float:
    """Return a realistic delay with natural random variation."""
    # Gaussian variation around the base delay
    d = random.gauss(base, base * VARIATION * 0.5)
    d = max(base * 0.3, min(base * 2.2, d))  # clamp between 30% and 220%

    # Extra pause after punctuation
    if next_char in _PUNCT_BASE:
        d *= _PUNCT_BASE[next_char] * PUNCT_SCALE
    elif next_char == " ":
        d *= SPACE_PAUSE

    # Random micro-pause (simulates thinking)
    if random.random() < HESITATION_PROB:
        d += random.uniform(*HESITATION_EXTRA)

    return d


# ── Global state ───────────────────────────────────────────────────────────
kb        = Controller()
buffer    = ""
is_typing = False
_lock     = threading.Lock()


# ── Snippet expansion ──────────────────────────────────────────────────────
def expand_snippet(trigger: str, text: str) -> None:
    """Delete the trigger and retype the text with typing effect."""
    global is_typing, buffer

    with _lock:
        is_typing = True
        buffer = ""

    try:
        time.sleep(0.06)  # short pause before deleting

        # Delete trigger characters
        for _ in trigger:
            kb.tap(Key.backspace)
            time.sleep(DELETE_DELAY)

        time.sleep(0.08)  # pause before starting to type

        # Type text one character at a time with natural rhythm
        for i, char in enumerate(text):
            kb.type(char)
            next_char = text[i + 1] if i + 1 < len(text) else ""
            time.sleep(human_delay(TYPING_DELAY, next_char))

    finally:
        with _lock:
            is_typing = False


# ── Keyboard listener ──────────────────────────────────────────────────────
def on_press(key) -> None:
    global buffer

    with _lock:
        if is_typing:
            return  # ignore input while we are typing

    try:
        char = key.char
        if char is None:
            return

        buffer += char

        # Keep buffer at max 40 characters
        if len(buffer) > 40:
            buffer = buffer[-40:]

        # Check if buffer ends with any trigger
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
        # Special keys: update buffer accordingly
        if key == Key.backspace:
            buffer = buffer[:-1] if buffer else ""
        elif key in (Key.space, Key.enter, Key.tab, Key.esc):
            buffer = ""


# ── Entry point ────────────────────────────────────────────────────────────
def main() -> None:
    W = 58
    print("\033[1m" + "─" * W + "\033[0m")
    print("\033[1m  TypeAct  –  Typing Effect Snippet Expander\033[0m")
    print("\033[1m" + "─" * W + "\033[0m")

    if not SNIPPETS:
        print("\n⚠️   No snippets found in snippets.json!\n")
    else:
        print(f"\n\033[32m✓  {len(SNIPPETS)} snippet(s) loaded:\033[0m\n")
        for trigger, text in SNIPPETS.items():
            preview = text[:55] + "…" if len(text) > 55 else text
            print(f"   \033[33m{trigger:6s}\033[0m  →  {preview}")

    print(f"\n   Speed: {TYPING_DELAY * 1000:.0f} ms/character")
    print("\n\033[90m   Listening… type a trigger in any app.\033[0m")
    print("\033[90m   Press Ctrl+C to quit.\033[0m\n")

    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n\033[90mTypeAct stopped.\033[0m\n")


if __name__ == "__main__":
    main()
