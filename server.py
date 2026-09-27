#!/usr/bin/env python3
"""
HTML Server GUI
---------------
Pick an HTML file with a file dialog and serve its containing folder
over HTTP so the page can use fetch()/local JSON files without hitting
the file:// CORS restrictions.

Requires: Python 3.8+ (stdlib only - no pip installs needed).
"""

import http.server
import os
import socket
import socketserver
import sys
import threading
import webbrowser
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    """SimpleHTTPRequestHandler with less console noise and correct MIME types."""

    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".js":   "application/javascript",
        ".mjs":  "application/javascript",
        ".json": "application/json",
        ".css":  "text/css",
        ".svg":  "image/svg+xml",
        ".wasm": "application/wasm",
    }

    def log_message(self, fmt, *args):
        # Keep the console usable; comment this out to see every request.
        sys.stderr.write("[server] %s - %s\n" % (self.address_string(), fmt % args))

    def end_headers(self):
        # Disable caching so edits to the HTML/JSON are picked up on reload.
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True


def find_free_port(preferred: int = 8000) -> int:
    """Return `preferred` if free, otherwise an arbitrary free port."""
    for port in [preferred] + list(range(preferred + 1, preferred + 50)):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
    # Last resort: ask the OS for any free port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class ServerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("HTML Local Server")
        self.root.geometry("640x260")
        self.root.resizable(False, False)

        self.html_path: Path | None = None
        self.httpd: ThreadedTCPServer | None = None
        self.server_thread: threading.Thread | None = None
        self.port: int | None = None

        self._build_ui()

    # ------------------------------------------------------------------ UI --
    def _build_ui(self):
        pad = {"padx": 12, "pady": 6}
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        header = ttk.Label(
            self.root,
            text="Select an HTML file and serve its folder over HTTP",
            font=("Segoe UI", 11, "bold"),
        )
        header.pack(anchor="w", **pad)

        row = ttk.Frame(self.root)
        row.pack(fill="x", **pad)

        self.path_var = tk.StringVar(value="(no file selected)")
        entry = ttk.Entry(row, textvariable=self.path_var, state="readonly")
        entry.pack(side="left", fill="x", expand=True)

        browse_btn = ttk.Button(row, text="Browse...", command=self.choose_file)
        browse_btn.pack(side="left", padx=(8, 0))

        opts = ttk.Frame(self.root)
        opts.pack(fill="x", **pad)

        ttk.Label(opts, text="Port:").pack(side="left")
        self.port_var = tk.StringVar(value="8000")
        ttk.Entry(opts, textvariable=self.port_var, width=8).pack(side="left", padx=(4, 16))

        self.open_browser_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(opts, text="Open in browser", variable=self.open_browser_var).pack(side="left")

        btns = ttk.Frame(self.root)
        btns.pack(fill="x", **pad)

        self.start_btn = ttk.Button(btns, text="Start server", command=self.start_server)
        self.start_btn.pack(side="left")

        self.stop_btn = ttk.Button(btns, text="Stop server", command=self.stop_server, state="disabled")
        self.stop_btn.pack(side="left", padx=(8, 0))

        self.open_btn = ttk.Button(btns, text="Open in browser", command=self.open_in_browser, state="disabled")
        self.open_btn.pack(side="left", padx=(8, 0))

        copy_btn = ttk.Button(btns, text="Copy URL", command=self.copy_url)
        copy_btn.pack(side="left", padx=(8, 0))

        self.status_var = tk.StringVar(value="Ready.")
        status = ttk.Label(self.root, textvariable=self.status_var, foreground="#333")
        status.pack(anchor="w", **pad)

        self.url_var = tk.StringVar(value="")
        url_label = ttk.Label(self.root, textvariable=self.url_var, foreground="#0B3D91")
        url_label.pack(anchor="w", padx=12)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    # ------------------------------------------------------------- actions --
    def choose_file(self):
        path = filedialog.askopenfilename(
            title="Select an HTML file",
            filetypes=[
                ("HTML files", "*.html *.htm"),
                ("All files", "*.*"),
            ],
        )
        if not path:
            return
        self.html_path = Path(path)
        self.path_var.set(str(self.html_path))
        self.status_var.set(f"Selected: {self.html_path.name}")

    def start_server(self):
        if self.html_path is None:
            messagebox.showwarning("No file", "Please select an HTML file first.")
            return
        if not self.html_path.is_file():
            messagebox.showerror("File not found", f"{self.html_path} no longer exists.")
            return

        # Pick port
        try:
            preferred = int(self.port_var.get().strip() or "8000")
            if not (1 <= preferred <= 65535):
                raise ValueError
        except ValueError:
            messagebox.showerror("Bad port", "Port must be a number between 1 and 65535.")
            return

        self.port = find_free_port(preferred)
        if self.port != preferred:
            self.status_var.set(f"Port {preferred} busy, using {self.port} instead.")

        # Serve the folder that contains the chosen HTML file
        serve_dir = str(self.html_path.parent)
        handler = lambda *a, **kw: QuietHandler(*a, directory=serve_dir, **kw)

        try:
            self.httpd = ThreadedTCPServer(("127.0.0.1", self.port), handler)
        except OSError as e:
            messagebox.showerror("Server error", f"Could not start server:\n{e}")
            return

        self.server_thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.server_thread.start()

        # Build the URL. URL-encode spaces etc. so the browser doesn't choke.
        from urllib.parse import quote
        rel = self.html_path.name
        url = f"http://127.0.0.1:{self.port}/{quote(rel)}"
        self.url_var.set(url)
        self.status_var.set(f"Serving '{serve_dir}' on port {self.port}")

        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.open_btn.config(state="normal")

        if self.open_browser_var.get():
            webbrowser.open(url)

    def stop_server(self):
        if self.httpd is not None:
            try:
                self.httpd.shutdown()
                self.httpd.server_close()
            except Exception:
                pass
            self.httpd = None
        self.server_thread = None
        self.url_var.set("")
        self.status_var.set("Server stopped.")
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.open_btn.config(state="disabled")

    def open_in_browser(self):
        url = self.url_var.get()
        if url:
            webbrowser.open(url)

    def copy_url(self):
        url = self.url_var.get()
        if not url:
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(url)
        self.status_var.set("URL copied to clipboard.")

    def on_close(self):
        self.stop_server()
        self.root.destroy()


def main():
    root = tk.Tk()
    app = ServerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
