---
protocol: grpc
title: gRPC Test Server
desc: A one-command local gRPC server that serves our own apidash.test.TestService with mock/random data, for exercising API Dash's gRPC client -- reflection, unary, all three streaming types, metadata, errors and TLS.
path: grpc
---

This is a **local** gRPC test rig for API Dash's gRPC client. gRPC is not an
HTTP route, so unlike the WebSocket endpoints it cannot be hosted inside the
FastAPI app. Instead we ship a **custom, Dockerized gRPC server** that serves
**our own** `apidash.test.TestService` with mock/random data: a real,
spec-compliant gRPC server with **server reflection** and **every call type**
(unary, server-streaming, client-streaming, bidi) plus metadata-echo and error
methods -- the gRPC analogue of the Mosquitto broker + `publisher.py` in the
MQTT test rig (`mqtt/`).

Serving our own service (rather than a third-party image) means every gRPC
feature has a **concrete, reproducible** method returning known-shaped data, so
each scenario below has an exact "send this, expect that" recipe.

Running a real gRPC server is the only way to genuinely test reflection, the
three streaming modes, trailing metadata, gRPC status codes and TLS over
HTTP/2.

## Why this is different from the other test endpoints (and why Docker)

**Before -- HTTP / WebSocket / SSE:** every test endpoint is a FastAPI route
inside this app, served over its single HTTP(S) port. That works because HTTP,
WebSocket (an HTTP upgrade) and SSE all ride on HTTP -- and Azure App Service
exposes exactly one HTTP/HTTPS port, which is all those need. No extra process,
no extra infra.

**gRPC is fundamentally different.** It's an RPC protocol layered on **HTTP/2**,
with its own wire framing, Protobuf message encoding, **server reflection** and
**long-lived bidirectional streams**, and it needs a **real gRPC server** to
answer reflection requests and to hold those streams open. So:

- It **can't be a FastAPI route** like `/ws/echo` -- there is no plain HTTP
  request/response to answer; the client speaks the gRPC/HTTP-2 protocol and,
  for streaming, keeps the channel open in both directions.
- Azure App Service **can't host it** either. App Service's front end terminates
  HTTP/1.1 on a single port and does not proxy end-to-end HTTP/2 with gRPC
  trailers, so a gRPC server can't be reached through it. (The WS endpoints work
  there *only* because WS is an HTTP/1.1 upgrade over that same port.)
- Faking gRPC semantics (reflection descriptors, streaming, status codes,
  trailers) as a FastAPI endpoint would mean re-implementing a gRPC server, with
  poor fidelity -- not worth it.

**So to test locally we run a real gRPC server via Docker** -- one command, full
fidelity, no cloud needed. That is the "extra hassle": it buys you a
spec-compliant server to point the client at, instead of a fake HTTP shim.

**What about production?** A shared, always-on hosted gRPC test endpoint (the
equivalent of `api.apidash.dev/ws/echo`) is a **separate, maintainer-owned
decision** -- it needs a host *outside* App Service that can proxy end-to-end
HTTP/2. **This change intentionally covers local testing only;** the
Azure/production infra is wired up separately.

## What this adds

- `grpc/server.py` -- the custom gRPC server implementing `apidash.test.TestService`
  with mock/random data, server reflection enabled, on plaintext `9000` and TLS
  `9001`.
- `grpc/proto/apidash_test.proto` -- the service schema (human-readable; you
  don't need to import it because reflection covers it).
- `grpc/Dockerfile`, `grpc/entrypoint.sh`, `grpc/requirements.txt`,
  `grpc/docker-compose.yml` -- the image (generates the Protobuf stubs at build
  time and mints a self-signed TLS cert on first start) and the one-command rig.
- `docs/grpc/` -- this README plus per-scenario pages (reflection, unary, the
  three streaming modes, metadata, auth, errors, TLS).

## Run it

From the repository root:

```
docker compose -f grpc/docker-compose.yml up
```

This starts one service:

| Service | What it is |
| ----------- | ----------- |
| `server` | Our custom gRPC server (`apidash.test.TestService`) with reflection and every call type |

Stop it with `Ctrl-C`, or run detached with `-d` and stop via
`docker compose -f grpc/docker-compose.yml down`.

## Tests

A pytest round-trip suite (`tests/grpc/test_grpc.py`) exercises every method of
`apidash.test.TestService` against a running server -- the gRPC analogue of the
MQTT rig's `tests/mqtt/test_mqtt.py`. It covers reflection, unary (`Echo`,
`GetRandomUser`), all three streaming modes (`StreamTicks`, `SumNumbers`,
`Chat`), request/response metadata (`EchoMetadata`), auth-via-metadata
(`SecureEcho`) and error status codes (`RaiseError`).

The Protobuf stubs are generated on the fly at test-collection time from
`grpc/proto/apidash_test.proto` (via `grpc_tools.protoc`), so nothing generated
is committed. Run it:

```
docker compose -f grpc/docker-compose.yml up --build -d   # start the server
pip install -r requirements-dev.txt                       # grpcio + tools + reflection
pytest tests/grpc/test_grpc.py
```

The whole module **skips gracefully** (it does not fail) when grpcio /
grpcio-tools are missing or when no server is reachable at `localhost:9000`, so
CI without a server stays green. Point it elsewhere with the `GRPC_HOST` /
`GRPC_PORT` environment variables.

## Endpoints

| Transport | Address | TLS | Notes |
| ----------- | ----------- | ----------- | ----------- |
| gRPC (plaintext, h2c) | `localhost:9000` | no | Everyday testing |
| gRPC over TLS (h2) | `localhost:9001` | yes (self-signed) | Enable TLS + allow invalid certs -- [tls](tls.md) |

Both listeners serve the **same service and methods**; only the transport
differs. `9000` is plaintext for frictionless testing; `9001` is the encrypted
equivalent.

## Point API Dash at it

In API Dash's gRPC client, create a request to:

- **Server / address:** `localhost:9000`
- **TLS:** off (plaintext)
- Hit **Reflect** to list the available services and methods -- the server has
  reflection enabled, so you don't need a `.proto` file. See
  [reflection](reflection.md).

For the encrypted listener use:

- **Server / address:** `localhost:9001`
- **TLS:** **on** + **Allow Invalid Certificates** (the cert is self-signed) --
  see [tls](tls.md)

You can EITHER use **reflection** (recommended -- zero setup) OR **import**
`grpc/proto/apidash_test.proto` for the exact same methods. Reflection is the
easy path.

## Service & methods

The server exposes one application service, `apidash.test.TestService` (plus the
reflection service). The table below maps each **test scenario** to the method
that exercises it and the mock/random data it returns:

| Scenario | Method | Returns | Doc |
| ----------- | ----------- | ----------- | ----------- |
| Reflection | `grpc.reflection.v1alpha.ServerReflection` | Service/method descriptors | [reflection](reflection.md) |
| Unary | `apidash.test.TestService/Echo` | Your message + server time + a sequence number | [unary](unary.md) |
| Unary (random) | `apidash.test.TestService/GetRandomUser` | A randomly generated `User` (mock data) | [unary](unary.md) |
| Server streaming | `apidash.test.TestService/StreamTicks` | A stream of `Tick`s with random values | [server_streaming](server_streaming.md) |
| Client streaming | `apidash.test.TestService/SumNumbers` | `sum` / `count` / `average` of the numbers you send | [client_streaming](client_streaming.md) |
| Bidirectional streaming | `apidash.test.TestService/Chat` | Each message echoed back, server-timestamped | [bidi](bidi.md) |
| Metadata / auth-via-metadata | `apidash.test.TestService/EchoMetadata` | The request metadata echoed back, plus response initial + trailing metadata | [metadata](metadata.md) |
| Auth (Bearer / API key) | `apidash.test.TestService/SecureEcho` | Echoes your message only with valid credentials; else `UNAUTHENTICATED` | [auth](auth.md) |
| Errors / status codes | `apidash.test.TestService/RaiseError` | Fails with the gRPC status code you request | [errors](errors.md) |
| TLS transport | any method on `localhost:9001` | Same methods over TLS | [tls](tls.md) |

Full method list:

| Service | Methods |
| ----------- | ----------- |
| `apidash.test.TestService` | `Echo`, `GetRandomUser`, `StreamTicks`, `SumNumbers`, `Chat`, `EchoMetadata`, `SecureEcho`, `RaiseError` |
| `grpc.reflection.v1alpha.ServerReflection` | `ServerReflectionInfo` (used by **Reflect**) |

> **Reflection version note:** the server registers the standard **v1alpha**
> reflection service (`grpc.reflection.v1alpha.ServerReflection`), which is what
> the `grpc-reflection` package provides. API Dash tries the newer `v1`
> reflection first and falls back to `v1alpha`, so **Reflect** works either way.
> See [reflection](reflection.md).

## Reference pages

- [reflection](reflection.md) -- list services/methods with no `.proto`
- [unary](unary.md) -- `Echo` and `GetRandomUser` (single request -> single response)
- [server_streaming](server_streaming.md) -- `StreamTicks` (one request -> stream)
- [client_streaming](client_streaming.md) -- `SumNumbers` (stream -> one response)
- [bidi](bidi.md) -- `Chat` (bidirectional streaming echo)
- [metadata](metadata.md) -- `EchoMetadata` (custom request headers + response metadata)
- [auth](auth.md) -- `SecureEcho` (auth-protected: Bearer token / API key)
- [errors](errors.md) -- `RaiseError` (choose the gRPC status code)
- [tls](tls.md) -- gRPC over TLS on `9001`

## A note on grpcurl

The samples on the per-scenario pages use
[`grpcurl`](https://github.com/fullstorydev/grpcurl), the de-facto gRPC CLI (the
`curl` of gRPC). It is a handy way to cross-check what API Dash sees, but it is
**not required** -- API Dash's gRPC client does everything the samples show.
Install it from its releases page if you want to follow along on the command
line.

## Zero-setup alternative: grpcb.in

If you want a remote gRPC target without running anything at all, the public
[`grpcb.in`](https://grpcb.in/) instance (`grpcb.in:9000` plaintext /
`grpcb.in:9001` TLS) run by the grpcbin project is always available. It serves a
**different** set of services (`grpcbin.GRPCBin`, `hello.HelloService`,
`addsvc.Add`) with the same *kinds* of methods, so reflection and every call
type can be tried there too. Our custom server is the rig, though -- it returns
the known-shaped mock/random data the recipes below rely on.
