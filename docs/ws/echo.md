---
method: get
title: WebSocket Echo
desc: A WebSocket endpoint that echoes back every message it receives, identically, for both plain text and JSON payloads.
path: ws/echo
---

This is a WebSocket endpoint that echoes back every message it receives, identically, for both plain text and JSON payloads. The connection is established through a standard HTTP `GET` upgrade handshake. Once connected, it is fully bidirectional: every text or JSON frame the server receives is sent straight back to the client unchanged. When the client disconnects, the server closes the connection cleanly.

It is intended as a self-hosted echo endpoint for testing WebSocket clients (such as API Dash) without relying on public endpoints.

## Connection URL

Connect to the endpoint using the WebSocket scheme. Use `wss://` against the deployed (TLS) API, or `ws://` against a local server.

```
wss://api.foss42.com/ws/echo
```

When running the API locally:

```
ws://127.0.0.1:8000/ws/echo
```

## Behavior

| Sent | Received |
| ----------- | ----------- |
| Plain text frame | The same text, unchanged |
| Valid JSON text frame | The same JSON, re-serialized and semantically identical |
| Client closes the connection | Server closes cleanly (normal closure) |

## Sample Usage

### Example #1: Python (`websockets`)

```python
import asyncio
import websockets


async def main():
    async with websockets.connect("wss://api.foss42.com/ws/echo") as ws:
        await ws.send("Hello, echo!")
        reply = await ws.recv()
        print(reply)  # Hello, echo!


asyncio.run(main())
```

### Example #2: JavaScript (browser `WebSocket`)

```javascript
const ws = new WebSocket("wss://api.foss42.com/ws/echo");

ws.onopen = () => ws.send(JSON.stringify({ msg: "Hello, echo!" }));
ws.onmessage = (event) => console.log(event.data); // {"msg": "Hello, echo!"}
```
