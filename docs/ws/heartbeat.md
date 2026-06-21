---
method: get
title: WebSocket Heartbeat
desc: A WebSocket endpoint that periodically sends a heartbeat to the client and responds to client pings.
path: ws/heartbeat
---

This is a WebSocket endpoint that demonstrates bidirectional heartbeat communication. The server automatically sends a JSON heartbeat message every 5 seconds. Additionally, it listens for incoming JSON messages from the client. If the client sends a `ping` message, the server will immediately reply with a `pong` message.

It is intended for testing WebSocket clients that require heartbeat handling or keep-alive mechanisms.

## Connection URL

Connect to the endpoint using the WebSocket scheme. Use `wss://` against the deployed (TLS) API, or `ws://` against a local server.

```
wss://api.foss42.com/ws/heartbeat
```

When running the API locally:

```
ws://127.0.0.1:8000/ws/heartbeat
```

## Behavior

| Event | Result |
| ----------- | ----------- |
| Server timer (every 5s) | Server sends: `{"type": "heartbeat", "message": "ping"}` |
| Client sends `{"message": "ping"}` | Server replies: `{"type": "heartbeat", "message": "pong"}` |
| Client sends other JSON | Server replies: `{"type": "message", "data": <original_json>}` |
| Client sends invalid JSON | Server replies: `{"type": "error", "message": "Invalid JSON"}` |

## Sample Usage

### Example: JavaScript (browser `WebSocket`)

```javascript
const ws = new WebSocket("wss://api.foss42.com/ws/heartbeat");

ws.onopen = () => {
    // Send a ping message
    ws.send(JSON.stringify({ message: "ping" }));
};

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log("Received from server:", data);
    
    // Example output:
    // Received from server: {type: 'heartbeat', message: 'pong'}
    // Received from server: {type: 'heartbeat', message: 'ping'} (every 5s)
};
```
