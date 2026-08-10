"""The contract cases that need no provider and no deployment.

Each case runs against a real chancery serving this repository's `config/`,
wired to the scripted stub in `stub_backend.py`. Nothing is mocked: the stub is
a socket, and the only thing faked is the provider on the far side of it.

    contract_test.py --chancery '<command>' [--slow]

`RESPONSES_BASE_URL`, `PORT` and `CORS_ORIGINS` are set in the command's
environment, so a plain binary needs no placeholders. `{base_url}`, `{port}` and
`{origin}` are available for a `docker run` template, which has to forward them
across the container boundary itself. `--slow` adds the stalled-stream case,
which takes 90 seconds by design.
"""

import argparse
import json
import os
import shlex
import signal
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from contextlib import contextmanager

import sse

HERE = os.path.dirname(os.path.abspath(__file__))
ALLOWED_ORIGIN = "https://site.example"
AGENT_PROMPT_OPENING = "<identity>"
MODEL_ID = "deepseek-v4-flash"
MAX_TOKENS = 1200
BODY_LIMIT_BYTES = 10 * 1024 * 1024
STALL_TIMEOUT_SECONDS = 90

results = []


def check(name, passed, detail=""):
    results.append((name, passed))
    print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f"   -> {detail}" if detail else ""))


def free_port():
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return probe.getsockname()[1]


def wait_for(predicate, seconds=60):
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        if predicate():
            return True
        time.sleep(0.2)
    return False


def health_ok(port):
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=1) as answer:
            return answer.read().strip() == b"ok"
    except (urllib.error.URLError, OSError):
        return False


def accepting(port):
    with socket.socket() as probe:
        probe.settimeout(1)
        return probe.connect_ex(("127.0.0.1", port)) == 0


def stop(process):
    """SIGTERM the whole group, because `go run` and `docker run` both wrap a child."""
    try:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    except (ProcessLookupError, PermissionError):
        process.terminate()
    try:
        process.wait(timeout=30)
    except subprocess.TimeoutExpired:
        process.kill()


@contextmanager
def backend(chancery_command, mode):
    """A stub in the given mode with a chancery in front of it."""
    stub_port, chancery_port = free_port(), free_port()
    workdir = tempfile.mkdtemp()
    recorded = os.path.join(workdir, "composed.json")
    # A file rather than a pipe: nothing drains a pipe while chancery runs, and a
    # full one would block the process being tested.
    log_path = os.path.join(workdir, "chancery.log")

    stub = subprocess.Popen(
        [sys.executable, os.path.join(HERE, "stub_backend.py"), str(stub_port), mode, recorded],
        stdout=subprocess.PIPE,
        text=True,
    )
    settings = {
        "RESPONSES_BASE_URL": f"http://host.docker.internal:{stub_port}"
        if "docker" in chancery_command
        else f"http://127.0.0.1:{stub_port}",
        "PORT": str(chancery_port),
        "CORS_ORIGINS": ALLOWED_ORIGIN,
    }
    # Set in the environment for a plain binary, and offered as placeholders so a
    # `docker run` template can forward the same three values across the boundary.
    command = chancery_command.format(
        base_url=settings["RESPONSES_BASE_URL"], port=chancery_port, origin=ALLOWED_ORIGIN
    )
    with open(log_path, "wb") as log:
        chancery = subprocess.Popen(
            shlex.split(command),
            env={**os.environ, **settings},
            stdout=log,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    try:
        # Chancery answers /health before it has ever called the backend, so waiting
        # on health alone races the stub's bind and shows up as a 503.
        if not wait_for(lambda: accepting(stub_port), seconds=30):
            raise SystemExit("the stub never bound its port")
        # Exiting early is the common failure — a bad command, a port in use, a
        # missing variable — so it is checked alongside health rather than waited out.
        started = wait_for(lambda: health_ok(chancery_port) or chancery.poll() is not None)
        if not started or chancery.poll() is not None:
            stub.terminate()
            reason = "exited" if chancery.poll() is not None else "never became healthy"
            raise SystemExit(f"chancery {reason}\n  command: {command}\n{open(log_path).read()}")
        yield f"http://127.0.0.1:{chancery_port}", recorded, stub
    finally:
        stop(chancery)
        stub.terminate()
        stub.wait(timeout=30)


def status_of(url, body=b"{}", method="POST"):
    request = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"}, method=method)
    try:
        with urllib.request.urlopen(request, timeout=30) as answer:
            return answer.status
    except urllib.error.HTTPError as refused:
        return refused.code


def check_composition(recorded):
    """The stub is the only place the body chancery composed can be inspected."""
    if not os.path.exists(recorded):
        check("the stub recorded the composed body", False, "no request reached the backend")
        return
    body = json.load(open(recorded))
    instructions = body.get("instructions", "")

    check("model is the bare DeepSeek id", body.get("model") == MODEL_ID, body.get("model"))
    check("max_output_tokens is the agent's ceiling", body.get("max_output_tokens") == MAX_TOKENS,
          body.get("max_output_tokens"))
    check("reasoning.effort is low", body.get("reasoning", {}).get("effort") == "low", body.get("reasoning"))
    check("a caller's own reasoning key survives", body.get("reasoning", {}).get("summary") == "detailed")
    check("the agent's prompt leads instructions", instructions.startswith(AGENT_PROMPT_OPENING))
    check("the caller's instructions are kept behind it", instructions.rstrip().endswith("CALLER"))
    check("store is absent", "store" not in body, body.get("store", "<absent>"))
    check("an unknown key passes through", body.get("unknown_key") == "kept")


def run_stream_cases(base, recorded):
    reply = sse.post(
        f"{base}/cv",
        {
            "input": [{"type": "message", "role": "user", "content": "hi"}],
            "stream": True,
            "max_output_tokens": 100000,
            "instructions": "CALLER",
            "reasoning": {"summary": "detailed"},
            "unknown_key": "kept",
        },
        origin=ALLOWED_ORIGIN,
    )
    check("a streamed request answers 200", reply.status == 200, reply.status)
    check("the reply is an event stream", "text/event-stream" in reply.headers.get("Content-Type", ""))
    check("deltas are relayed", reply.text == "stub answer", repr(reply.text))
    check("an allowed origin is echoed back",
          reply.headers.get("Access-Control-Allow-Origin") == ALLOWED_ORIGIN,
          reply.headers.get("Access-Control-Allow-Origin"))

    check_composition(recorded)

    for path, expected in [("/cv", 200), ("/cv/responses", 200), ("/cv.fast", 404), ("/nope", 404)]:
        actual = status_of(f"{base}{path}", b'{"input":"hi"}')
        check(f"POST {path} answers {expected}", actual == expected, actual)
    check("GET /health answers 200", status_of(f"{base}/health", None, "GET") == 200)

    check("a body that is not a JSON object is 400", status_of(f"{base}/cv", b'"a string"') == 400)
    # Chancery always supplies instructions and the provider needs only one of
    # the two, so an empty body is answered and billed. A 400 here would give the
    # site a status it has no rendering for.
    check("a body with no input still streams", status_of(f"{base}/cv", b'{"stream":true}') == 200)
    oversized = b'{"input":"' + b"x" * (BODY_LIMIT_BYTES + 1000) + b'","stream":true}'
    check("a body over 10 MB is 400, not 413", status_of(f"{base}/cv", oversized) == 400)

    # CORS stops a browser and nothing else. The second half has to pass, or the
    # exposure this deployment accepts is being described wrongly.
    refused = sse.post(f"{base}/cv", {"input": "hi", "stream": True}, origin="https://evil.example")
    check("a disallowed origin gets no allow-origin header",
          refused.headers.get("Access-Control-Allow-Origin") is None)
    check("and the same request still succeeds, because curl ignores CORS", refused.status == 200, refused.status)


def run_failure_cases(base):
    """A backend failure arrives as an event inside a 200, never as a status."""
    reply = sse.post(f"{base}/cv", {"input": "hi", "stream": True})

    check("a mid-stream failure still answers 200", reply.status == 200, reply.status)
    check("the deltas before it are relayed", reply.text == "half an ", repr(reply.text))
    check("response.failed reaches the caller", "response.failed" in reply.event_names, reply.event_names)
    check("no terminal completion follows it", "response.completed" not in reply.event_names)


def run_ratelimit_cases(base, stub):
    reply = sse.post(f"{base}/cv", {"input": "hi", "stream": True})
    stub.terminate()
    attempts = sum(1 for line in stub.stdout if line.startswith("attempt"))

    check("a rate-limited backend reaches the caller as 429", reply.status == 429, reply.status)
    check("the body is the status text", reply.text.strip() == "Too Many Requests", repr(reply.text.strip()))
    check("the backend's own explanation never travels", "backend explanation" not in reply.text)
    check("three attempts were made", attempts == 3, attempts)


def run_stall_case(base):
    reply = sse.post(f"{base}/cv", {"input": "hi", "stream": True}, timeout=STALL_TIMEOUT_SECONDS + 60)
    terminal = {"response.completed", "response.failed", "response.incomplete"}

    check("a stalled stream is ended", reply.ended_at >= STALL_TIMEOUT_SECONDS, f"{reply.ended_at:.1f}s")
    check("with no terminal event, which a client must treat as failure",
          not terminal.intersection(reply.event_names), reply.event_names)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--chancery", required=True, help="shell command carrying {base_url} and {port}")
    parser.add_argument("--slow", action="store_true", help="include the 90-second stalled-stream case")
    arguments = parser.parse_args()

    with backend(arguments.chancery, "stream") as (base, recorded, _):
        run_stream_cases(base, recorded)
    with backend(arguments.chancery, "failed") as (base, _, _stub):
        run_failure_cases(base)
    with backend(arguments.chancery, "ratelimit") as (base, _, stub):
        run_ratelimit_cases(base, stub)
    if arguments.slow:
        with backend(arguments.chancery, "stall") as (base, _, _stub):
            run_stall_case(base)
    else:
        print("SKIP  the stalled-stream case — pass --slow to include it")

    failed = [name for name, passed in results if not passed]
    print(f"\n{len(results) - len(failed)}/{len(results)} passed")
    if failed:
        print("failed: " + "; ".join(failed))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
