"""
Apizza Tech Systems - Marquee Console
Desktop launcher (wraps index.html in a native window via pywebview)

Run with:
    pip install -r requirements.txt
    python app.py
"""

import os
import sys
import webview


class Api:
    """Exposed to the page as window.pywebview.api"""

    def exit_app(self):
        if _window is not None:
            _window.destroy()


def resource_path(relative_path):
    """Resolve path correctly whether running from source or a PyInstaller bundle."""
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


_window = None

if __name__ == "__main__":
    index_path = resource_path("index.html")
    _window = webview.create_window(
        "Apizza Tech Systems - Marquee Console",
        index_path,
        js_api=Api(),
        width=1180,
        height=820,
        min_size=(900, 640),
        background_color="#000000",
    )
    webview.start()
