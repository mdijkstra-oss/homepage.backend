"""A scripted `openai-responses` backend, so the contract cases need no provider.

Chancery needs exactly one thing from the outside — something serving that
format at RESPONSES_BASE_URL — so this is the whole of the isolation harness.
It records the body chancery composed, which is the only place that body can be
inspected.

    stub_backend.py PORT MODE RECORD_PATH

Modes:
    stream     a fixed event sequence, flushed per event
    failed     a delta, then response.failed inside the already-sent 200
    ratelimit  429 with a Retry-After on every attempt, counting attempts
    stall      headers and one event, then silence
"""

import json
import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

STREAM_EVENTS = [
    ("response.created", {"type": "response.created"}),
    ("response.output_text.delta", {"type": "response.output_text.delta", "delta": "stub "}),
    ("response.output_text.delta", {"type": "response.output_text.delta", "delta": "answer"}),
    ("response.completed", {"type": "response.completed", "response": {"usage": {}}}),
]

FAILURE_MESSAGE = "the provider gave up"
FAILED_EVENTS = [
    ("response.output_text.delta", {"type": "response.output_text.delta", "delta": "half an "}),
    ("response.failed", {"type": "response.failed", "response": {"error": {"message": FAILURE_MESSAGE}}}),
]

RATE_LIMIT_EXPLANATION = b'{"error":{"message":"backend explanation that must not reach the caller"}}'
STALL_SECONDS = 300


class Backend(BaseHTTPRequestHandler):
    mode = "stream"
    record_path = None
    attempts = 0

    def do_POST(self):
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        if Backend.record_path:
            with open(Backend.record_path, "wb") as recorded:
                recorded.write(body)

        if Backend.mode == "ratelimit":
            self.answer_rate_limited()
        elif Backend.mode == "stall":
            self.answer_then_stall()
        elif Backend.mode == "failed":
            self.answer_events(FAILED_EVENTS)
        else:
            self.answer_events(STREAM_EVENTS)

    def answer_rate_limited(self):
        Backend.attempts += 1
        print(f"attempt {Backend.attempts}", flush=True)
        self.send_response(429)
        self.send_header("Content-Type", "application/json")
        self.send_header("Retry-After", "1")
        self.send_header("Content-Length", str(len(RATE_LIMIT_EXPLANATION)))
        self.end_headers()
        self.wfile.write(RATE_LIMIT_EXPLANATION)

    def answer_then_stall(self):
        self.begin_event_stream()
        self.write_event("response.output_text.delta", {"delta": "one"})
        time.sleep(STALL_SECONDS)

    def answer_events(self, events):
        self.begin_event_stream()
        for name, payload in events:
            self.write_event(name, payload)

    def begin_event_stream(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.end_headers()

    def write_event(self, name, payload):
        self.wfile.write(f"event: {name}\ndata: {json.dumps(payload)}\n\n".encode())
        self.wfile.flush()

    def log_message(self, *_):
        pass


def main():
    port, Backend.mode = int(sys.argv[1]), sys.argv[2]
    Backend.record_path = sys.argv[3] if len(sys.argv) > 3 else None
    # Every interface, not loopback: a containerised chancery reaches the host
    # over the bridge gateway, which is not 127.0.0.1. Binding loopback works on
    # Docker Desktop and fails on a Linux runner, where it reads as a 503.
    HTTPServer(("", port), Backend).serve_forever()


if __name__ == "__main__":
    main()
