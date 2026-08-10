"""Reading an event stream."""

import json
import urllib.error
import urllib.request
from dataclasses import dataclass, field


@dataclass
class StreamResult:
    status: int
    headers: dict
    text: str = ""
    event_names: list = field(default_factory=list)


def post(url, body, timeout=180):
    """POST a JSON body and read the reply as an event stream.

    A non-2xx is returned rather than raised, because a caller may be asking
    about the status.
    """
    headers = {"Content-Type": "application/json", "Accept": "text/event-stream"}
    request = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")

    try:
        response = urllib.request.urlopen(request, timeout=timeout)
    except urllib.error.HTTPError as refused:
        return StreamResult(refused.code, dict(refused.headers), refused.read().decode(errors="replace"))

    with response:
        result = StreamResult(response.status, dict(response.headers))
        name, data = "", []
        for raw in response:
            line = raw.decode(errors="replace").rstrip("\r\n")
            if line.startswith("event:"):
                name = line[6:].strip()
            elif line.startswith("data:"):
                data.append(line[5:].strip())
            elif line == "" and name:
                result.event_names.append(name)
                if name == "response.output_text.delta":
                    result.text += _delta_of("\n".join(data))
                name, data = "", []
    return result


def _delta_of(payload):
    try:
        return json.loads(payload).get("delta", "")
    except json.JSONDecodeError:
        return ""
