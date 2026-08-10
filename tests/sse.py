"""Reading an event stream, with every event stamped as it arrives.

Arrival times are part of the result because a buffering proxy delivers a
correct answer all at once: "a delta carrying text arrived" is true of the
failure and the success alike, so only the gap between the first delta and the
end of the stream tells them apart.
"""

import json
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field


@dataclass
class StreamResult:
    status: int
    headers: dict
    text: str = ""
    events: list = field(default_factory=list)
    first_delta_at: float | None = None
    ended_at: float = 0.0

    @property
    def event_names(self):
        return [name for _, name in self.events]

    @property
    def gap(self):
        """Seconds between the first delta and the end. None when no delta arrived."""
        return None if self.first_delta_at is None else self.ended_at - self.first_delta_at


def post(url, body, origin=None, timeout=180):
    """POST a JSON body and read the reply as an event stream.

    A non-2xx is returned rather than raised, because several contract cases are
    about the status.
    """
    headers = {"Content-Type": "application/json", "Accept": "text/event-stream"}
    if origin:
        headers["Origin"] = origin
    request = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")

    started = time.monotonic()
    try:
        response = urllib.request.urlopen(request, timeout=timeout)
    except urllib.error.HTTPError as refused:
        return StreamResult(
            status=refused.code,
            headers=dict(refused.headers),
            text=refused.read().decode(errors="replace"),
            ended_at=time.monotonic() - started,
        )

    with response:
        result = StreamResult(status=response.status, headers=dict(response.headers))
        name, data = "", []
        for raw in response:
            line = raw.decode(errors="replace").rstrip("\r\n")
            if line.startswith("event:"):
                name = line[6:].strip()
            elif line.startswith("data:"):
                data.append(line[5:].strip())
            elif line == "" and name:
                at = time.monotonic() - started
                result.events.append((at, name))
                if name == "response.output_text.delta":
                    result.first_delta_at = result.first_delta_at or at
                    result.text += _delta_of("\n".join(data))
                name, data = "", []
        result.ended_at = time.monotonic() - started
    return result


def _delta_of(payload):
    try:
        return json.loads(payload).get("delta", "")
    except json.JSONDecodeError:
        return ""
