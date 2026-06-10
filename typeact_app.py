#!/usr/bin/env python3
"""
TypeAct – Menu Bar App
------------------------
Runs as a macOS menu bar icon. Click TA to:
  - See loaded snippets
  - Pause / Resume typing detection
  - Open the snippet manager
  - Quit the app completely

REQUIREMENTS:
  pip install rumps pynput
"""

import os
import subprocess
import sys

# ── Install rumps if missing ───────────────────────────────────────────────
try:
    import rumps
except ImportError:
    print("Installing rumps...")
    os.system(f'"{sys.executable}" -m pip install rumps -q')
    import rumps

from typing_demo import (
    start_listener,
    stop_listener,
    SNIPPETS,
    TYPING_DELAY,
    SCRIPT_DIR,
)


class TypeActApp(rumps.App):

    def __init__(self):
        super().__init__("TA ●", quit_button=None)
        # Hide Python icon from the Dock — run as a pure menu bar app
        import AppKit
        AppKit.NSApplication.sharedApplication().setActivationPolicy_(
            AppKit.NSApplicationActivationPolicyAccessory
        )
        self._running = False
        self._build_menu()
        self._start()   # auto-start on launch

    # ── Build menu ─────────────────────────────────────────────────────
    def _build_menu(self):
        items = []

        # Snippet preview list (read-only)
        if SNIPPETS:
            for trigger, text in SNIPPETS.items():
                preview = text[:48] + "…" if len(text) > 48 else text
                item = rumps.MenuItem(f"{trigger}   {preview}")
                item.set_callback(None)
                items.append(item)
        else:
            no_snip = rumps.MenuItem("No snippets loaded")
            no_snip.set_callback(None)
            items.append(no_snip)

        items.append(None)  # ── separator ──

        # Actions
        items.append(rumps.MenuItem("✏️  Manage Snippets", callback=self.open_manager))

        self._toggle_item = rumps.MenuItem("⏸  Pause", callback=self.toggle)
        items.append(self._toggle_item)

        items.append(None)  # ── separator ──

        items.append(rumps.MenuItem("✕  Quit TypeAct", callback=self.quit_app))

        self.menu = items

    # ── Controls ───────────────────────────────────────────────────────
    def _start(self):
        start_listener()
        self._running = True
        self.title = "TA ●"
        self._toggle_item.title = "⏸  Pause"

    def _pause(self):
        stop_listener()
        self._running = False
        self.title = "TA ○"
        self._toggle_item.title = "▶  Resume"

    def toggle(self, _):
        if self._running:
            self._pause()
        else:
            self._start()

    def open_manager(self, _):
        manager = os.path.join(SCRIPT_DIR, "gestisci_snippet.html")
        subprocess.run(["open", "-a", "Google Chrome", manager])

    def quit_app(self, _):
        stop_listener()
        rumps.quit_application()


# ── Entry point ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    TypeActApp().run()
