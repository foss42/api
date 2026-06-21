---
method: get
title: WebSocket Timeout
desc: A WebSocket endpoint that enforces an idle timeout if the client stops sending messages.
path: ws/timeout/{timeout}
---

This is a WebSocket endpoint that enforces a strict idle timeout. The connection remains open as long as the client sends valid JSON messages. If the client stops sending messages and the `timeout` period (in seconds) elapses, the server will forcefully close the connection with closure code `1008 (Policy Violation)`.

It is intended for testing WebSocket clients and verifying that they can correctly implement keep-alive mechanisms and handle unexpected server closures.

## Connection URL

Connect to the endpoint using the WebSocket scheme and specify the timeout in seconds as a path parameter.

```
wss://api.foss42.com/ws/timeout/10
```

When running the API locally:

```
ws://127.0.0.1:8000/ws/timeout/10
```

## Behavior

| Event | Result |
| ----------- | ----------- |
| Client sends `{"message": "ping"}` | Server replies: `{"type": "heartbeat", "message": "pong"}`, and resets the idle timer. |
| Client sends other JSON | Server replies: `{"type": "message", "data": <original_json>}`, and resets the idle timer. |
| Client sends invalid JSON | Server replies: `{"type": "error", "message": "Invalid JSON"}` |
| Client is idle for `{timeout}` seconds | Server closes connection with code `1008` |

## Sample Usage

### Example: JavaScript (browser `WebSocket`)

```javascript
// Connect with a 5-second timeout
const ws = new WebSocket("wss://api.foss42.com/ws/timeout/5");

ws.onopen = () => {
    // Keep the connection alive by pinging every 3 seconds
    setInterval(() => {
        if (ws.readyState === WebSocket.OPEN) {
            ws.send(JSON.stringify({ message: "ping" }));
        }
    }, 3000);
};

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log("Received from server:", data);
};

ws.onclose = (event) => {
    console.log("Connection closed", event.code, event.reason);
};
```
