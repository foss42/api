---
protocol: grpc
title: gRPC Auth (SecureEcho)
desc: SecureEcho is an auth-protected unary call -- it accepts the request only when you send a valid Bearer token or API key as metadata, and fails UNAUTHENTICATED otherwise, so you can test API Dash's Auth tab and API-key auth.
path: grpc/auth
---

gRPC has no separate "auth" mechanism -- credentials travel as
[metadata](metadata.md) (the gRPC equivalent of HTTP headers). A server enforces
auth by reading that metadata and rejecting the call when it's missing or wrong.

`apidash.test.TestService/SecureEcho` is built for testing exactly this. It
behaves like [`Echo`](unary.md) -- echoes your `message` back with a server time
and sequence number -- but **only if the call carries valid credentials**.
Otherwise it fails with gRPC status **`16 UNAUTHENTICATED`**.

## What it tests

That API Dash can attach credentials to a gRPC call -- a **Bearer token** via
the Auth tab (which becomes an `authorization` metadata entry) or an **API key**
as a custom metadata header -- and that it surfaces the `UNAUTHENTICATED` status
when they're absent or wrong.

## Method

```
apidash.test.TestService/SecureEcho    # EchoRequest{message} -> EchoResponse{message, server_time, seq}
```

The request/response shapes are identical to `Echo`; the difference is the
credential check on the incoming metadata. On success the echoed `message` is
prefixed with `[authenticated]` so you can tell the two apart.

## Accepted credentials

The call is accepted if **EITHER** of these is present in the request metadata:

| Metadata key | Value | How to send it in API Dash |
| ----------- | ----------- | ----------- |
| `authorization` | `Bearer test-token` | Auth tab -> Bearer token = `test-token` |
| `x-api-key` | `test-apikey` | Add a metadata / header row `x-api-key` = `test-apikey` |

Anything else -- no credentials, a wrong token, a wrong key -- is rejected.

## Expected behavior

| You send | Result |
| ----------- | ----------- |
| Metadata `authorization: Bearer test-token` | Success -- `message` echoed as `[authenticated] <your message>` |
| Metadata `x-api-key: test-apikey` | Success -- same as above |
| No credentials | Call fails with status `16 UNAUTHENTICATED` |
| Wrong token / key (e.g. `Bearer nope`) | Call fails with status `16 UNAUTHENTICATED` |

The failure message is:
`missing or invalid credentials -- send 'authorization: Bearer test-token' or 'x-api-key: test-apikey'`.

## Test it in API Dash

1. **Reflect** against `localhost:9000` and pick
   `apidash.test.TestService/SecureEcho`.
2. Set the request to `{"message": "hello"}` and **Send** with no credentials.
   - **Expected:** the call fails and API Dash shows status
     **`16 UNAUTHENTICATED`** with the missing-credentials message.
3. Open the **Auth** tab, choose **Bearer** and enter the token `test-token`
   (API Dash puts `authorization: Bearer test-token` on the wire). **Send**.
   - **Expected:** success -- the response echoes
     `[authenticated] hello` with a `server_time` and `seq`.
4. Alternatively, instead of the Auth tab, add a metadata row `x-api-key` =
   `test-apikey` and **Send**.
   - **Expected:** the same success response.

## Sample Usage

### grpcurl

Pass credentials as metadata with `-H "key: value"`:

```
grpcurl -plaintext -d '{"message": "hi"}' \
  -H "authorization: Bearer test-token" \
  localhost:9000 apidash.test.TestService/SecureEcho
# {
#   "message": "[authenticated] hi",
#   "server_time": "2026-08-24T...Z",
#   "seq": 1
# }
```

With an API key instead:

```
grpcurl -plaintext -d '{"message": "hi"}' \
  -H "x-api-key: test-apikey" \
  localhost:9000 apidash.test.TestService/SecureEcho
# { "message": "[authenticated] hi", ... }
```

With no credentials it fails:

```
grpcurl -plaintext -d '{"message": "hi"}' \
  localhost:9000 apidash.test.TestService/SecureEcho
# ERROR:
#   Code: Unauthenticated
#   Message: missing or invalid credentials -- send 'authorization: Bearer test-token' or 'x-api-key: test-apikey'
```

For TLS use `localhost:9001` -- see [tls](tls.md). To just inspect which metadata
reaches the server (without the auth check), use [`EchoMetadata`](metadata.md).
