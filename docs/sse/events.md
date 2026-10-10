---
method: get
title: SSE Events
desc: A Server-Sent Events (SSE) endpoint that streams a fixed number of events, one per second, for testing SSE clients.
path: sse/events/{count}
---

This is a Server-Sent Events (SSE) endpoint that streams `count` events back to the client, one per second, over a single HTTP connection. Each event is sent as a standard `text/event-stream` frame in the form `data: eventN`, where `N` goes from `1` to `count`. After all requested events have been sent, the stream ends.

It is intended as a self-hosted SSE endpoint for testing SSE clients (such as API Dash) without relying on public endpoints.

## Path Parameters

| Parameter | Data Type | Required | Description |
|-----------|-----------|----------|-------------|
| `count` | `integer` | Yes | Number of events to stream. Must not exceed `100`. |

## HTTP Response Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Stream started successfully |
| 400 | `count` exceeds the maximum allowed value (`100`) |
| 422 | `count` is not a valid integer |

## Sample Usage

### Example #1: Stream 3 events

#### API Request

Open the API request in a browser to view the streamed events as they arrive.

```text
{{ site_api }}/sse/events/3
```

#### cURL Request

The `-N` flag disables cURL's output buffering so events are printed as they arrive rather than all at once at the end.

```bash
curl -N '{{ site_api }}/sse/events/3'
```

#### Response

The events are streamed one per second:

```text
data: event1

data: event2

data: event3
```

### Example #2: `count` exceeds the limit

#### API Request

```text
{{ site_api }}/sse/events/150
```

#### cURL Request

```bash
curl -N '{{ site_api }}/sse/events/150'
```

#### Response (400 Bad Request)

```json
{
  "detail": "Count cannot exceed 100"
}
```

### Example #3: JavaScript (browser `EventSource`)

```javascript
const source = new EventSource("{{ site_api }}/sse/events/5");

source.onmessage = (event) => {
  console.log(event.data); // event1, event2, ...

  if (event.data === "event5") {
    source.close();
  }
};
```

### Example #4: Python (`httpx`)

```python
import httpx

with httpx.stream("GET", "{{ site_api }}/sse/events/5") as response:
    for line in response.iter_lines():
        if line.startswith("data:"):
            print(line)  # data: event1, data: event2, ...
```
