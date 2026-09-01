---
protocol: grpc
title: gRPC Metadata & Auth
desc: EchoMetadata reflects the request metadata (gRPC headers) back to you AND sends response metadata (initial + trailing) back, so you can verify both custom request headers / auth-via-metadata and the response-metadata view.
path: grpc/metadata
---

gRPC carries key/value **metadata** (the gRPC equivalent of HTTP headers)
alongside every call. It's how clients send things like an `authorization`
token, a request id, or an API key -- gRPC has no separate "auth" mechanism, so
**auth is done via metadata**.

`apidash.test.TestService/EchoMetadata` is built for testing this in **both
directions**:

- **Request -> server:** it **returns the request metadata back to you** in the
  response body, so you can confirm exactly which headers API Dash put on the
  wire.
- **Server -> response:** it also **sends response metadata back** -- initial
  metadata (`x-server`, `x-echoed-count`) and trailing metadata (`x-trailer`) --
  so API Dash's **response metadata / headers view** is testable too.

## What it tests

That API Dash attaches custom metadata to a gRPC call (including an
`authorization` header for auth-via-metadata) and that the values arrive at the
server intact -- **and** that it surfaces the metadata the server sends back on
the response (initial + trailing).

> For an auth check that actually **rejects** calls without valid credentials
> (rather than just echoing whatever you send), see [auth](auth.md)
> (`SecureEcho`).

## Method

```
apidash.test.TestService/EchoMetadata    # Empty -> MetadataResponse{map<string,string> metadata}
```

The request body is empty; everything interesting travels as metadata. The
response's `metadata` map contains the key/value pairs the server received.

## Expected behavior

| You send | You get back |
| ----------- | ----------- |
| Metadata `authorization: Bearer test-token` | `metadata` includes `"authorization": "Bearer test-token"` |
| Metadata `x-request-id: abc123` | `metadata` includes `"x-request-id": "abc123"` |
| No custom metadata | Only the transport's own headers (e.g. `user-agent`) come back |

This makes it a quick way to prove an auth token or any custom header is actually
being sent -- if it comes back, the server received it. (Note gRPC lowercases
metadata keys on the wire, so `Authorization` comes back as `authorization`.)

## Response metadata (server -> client)

Besides echoing the request metadata into the response **body**, the server
attaches metadata to the **response** itself -- the mirror image of what you
send. These are surfaced in API Dash's response metadata / headers view, not in
the message body:

| Metadata | When it arrives | Value |
| ----------- | ----------- | ----------- |
| `x-server` | initial metadata (response headers) | `apidash-grpc-test` |
| `x-echoed-count` | initial metadata (response headers) | number of request metadata pairs the server received |
| `x-trailer` | trailing metadata (response trailers) | `ok` |

So a single `EchoMetadata` call exercises metadata in both directions:
request -> server (echoed in the body) **and** server -> response (the initial +
trailing metadata above).

## Test it in API Dash

1. **Reflect** against `localhost:9000` and pick
   `apidash.test.TestService/EchoMetadata`.
2. Add metadata rows to the request, e.g. `authorization` / `Bearer test-token`
   and `x-request-id` / `abc123`. Leave the request body empty.
3. **Send**.
   - **Expected (response body):** the response `metadata` map contains
     `authorization: Bearer test-token` and `x-request-id: abc123` (plus
     transport headers like `user-agent`). This is the pattern for testing
     **auth-via-metadata** against any real gRPC service.
   - **Expected (response metadata / headers view):** `x-server:
     apidash-grpc-test` and `x-echoed-count: <N>` in the initial metadata, and
     `x-trailer: ok` in the trailing metadata.

## Sample Usage

### grpcurl

Pass metadata with `-H "key: value"` (repeatable):

```
grpcurl -plaintext \
  -H "authorization: Bearer test-token" \
  -H "x-request-id: abc123" \
  localhost:9000 apidash.test.TestService/EchoMetadata
# {
#   "metadata": {
#     "authorization": "Bearer test-token",
#     "x-request-id": "abc123",
#     "user-agent": "grpc-...",
#     ...
#   }
# }
```

Add `-v` to also see the **response** metadata grpcurl received -- the server's
initial and trailing metadata:

```
grpcurl -plaintext -v \
  -H "authorization: Bearer test-token" \
  localhost:9000 apidash.test.TestService/EchoMetadata
# Response headers received:
#   x-server: apidash-grpc-test
#   x-echoed-count: 2
# ...
# Response trailers received:
#   x-trailer: ok
```

In API Dash: add metadata rows to the request, call `EchoMetadata`, and confirm
the same key/value pairs appear in the response body -- and that `x-server` /
`x-echoed-count` / `x-trailer` appear in the response metadata view. For TLS use
`localhost:9001` -- see [tls](tls.md). For an auth check that rejects invalid
credentials, see [auth](auth.md).
