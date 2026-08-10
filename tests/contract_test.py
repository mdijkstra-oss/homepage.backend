"""What this repository's configuration produces, checked against the built image.

Chancery has its own suite and this is not a second one. It exists because the
image is the unit of version: the pinned chancery release, the baked `config/`
and the port it binds are only exercised together here. What it pins is the
three values `models.yaml` and the agent's frontmatter put in the outbound body,
and the route table they produce.

    contract_test.py --chancery '<command>'

`RESPONSES_BASE_URL` and `PORT` are set in the command's environment, so a plain
binary needs no placeholders. `{base_url}` and `{port}` are available for a
`docker run` template, which has to forward them across the container boundary
itself.
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
MODEL_ID = "deepseek-v4-flash"
MAX_TOKENS = 1200

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
def backend(chancery_command):
    """The stub with a chancery in front of it."""
    stub_port, chancery_port = free_port(), free_port()
    workdir = tempfile.mkdtemp()
    recorded = os.path.join(workdir, "composed.json")
    # A file rather than a pipe: nothing drains a pipe while chancery runs, and a
    # full one would block the process being tested.
    log_path = os.path.join(workdir, "chancery.log")

    stub = subprocess.Popen([sys.executable, os.path.join(HERE, "stub_backend.py"), str(stub_port), recorded])
    settings = {
        "RESPONSES_BASE_URL": f"http://host.docker.internal:{stub_port}"
        if "docker" in chancery_command
        else f"http://127.0.0.1:{stub_port}",
        "PORT": str(chancery_port),
    }
    # Set in the environment for a plain binary, and offered as placeholders so a
    # `docker run` template can forward the same values across the boundary.
    command = chancery_command.format(base_url=settings["RESPONSES_BASE_URL"], port=chancery_port)
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
        yield f"http://127.0.0.1:{chancery_port}", recorded
    finally:
        stop(chancery)
        stub.terminate()
        stub.wait(timeout=30)


def status_of(url, body):
    request = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"}, method="POST")
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

    check("model is the bare DeepSeek id", body.get("model") == MODEL_ID, body.get("model"))
    check("max_output_tokens is the agent's ceiling", body.get("max_output_tokens") == MAX_TOKENS,
          body.get("max_output_tokens"))
    check("reasoning.effort is low", body.get("reasoning", {}).get("effort") == "low", body.get("reasoning"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--chancery", required=True, help="shell command carrying {base_url} and {port}")
    arguments = parser.parse_args()

    with backend(arguments.chancery) as (base, recorded):
        check("the image serves /health", health_ok(int(base.split(":")[-1])))

        reply = sse.post(f"{base}/cv", {"input": [{"type": "message", "role": "user", "content": "hi"}], "stream": True})
        check("POST /cv answers 200", reply.status == 200, reply.status)
        check("the provider's deltas reach the caller", reply.text == "stub answer", repr(reply.text))

        check_composition(recorded)

        for path in ["/cv.fast", "/nope"]:
            actual = status_of(f"{base}{path}", b'{"input":"hi"}')
            check(f"POST {path} answers 404", actual == 404, actual)

    failed = [name for name, passed in results if not passed]
    print(f"\n{len(results) - len(failed)}/{len(results)} passed")
    if failed:
        print("failed: " + "; ".join(failed))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
