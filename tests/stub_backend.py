"""An `openai-responses` backend that answers with a fixed event sequence.

Chancery needs exactly one thing from the outside — something serving that
format at RESPONSES_BASE_URL — so this is the whole of the isolation harness.
It records the body chancery composed, which is the only place that body can be
inspected.

    stub_backend.py PORT RECORD_PATH
"""

import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

EVENTS = [
    ("response.created", {"type": "response.created"}),
    ("response.output_text.delta", {"type": "response.output_text.delta", "delta": "stub "}),
    ("response.output_text.delta", {"type": "response.output_text.delta", "delta": "answer"}),
    ("response.completed", {"type": "response.completed", "response": {"usage": {}}}),
]


class Backend(BaseHTTPRequestHandler):
    record_path = None

    def do_POST(self):
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        if Backend.record_path:
            with open(Backend.record_path, "wb") as recorded:
                recorded.write(body)

        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.end_headers()
        for name, payload in EVENTS:
            self.wfile.write(f"event: {name}\ndata: {json.dumps(payload)}\n\n".encode())
            self.wfile.flush()

    def log_message(self, *_):
        pass


def main():
    port = int(sys.argv[1])
    Backend.record_path = sys.argv[2] if len(sys.argv) > 2 else None
    # Every interface, not loopback: a containerised chancery reaches the host
    # over the bridge gateway, which is not 127.0.0.1. Binding loopback works on
    # Docker Desktop and fails on a Linux runner, where it reads as a 503.
    HTTPServer(("", port), Backend).serve_forever()


if __name__ == "__main__":
    main()
