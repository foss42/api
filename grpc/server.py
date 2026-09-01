#!/usr/bin/env python3
"""
Custom gRPC test server for API Dash's gRPC client.

This is the gRPC analogue of the MQTT rig's `publisher.py`: instead of pointing
at a third-party image (the old rig ran `moul/grpcbin`), we serve OUR OWN
`apidash.test.TestService` so every gRPC feature has a concrete, reproducible
method returning mock/random data.

One small service (see `proto/apidash_test.proto`) exercises all four gRPC call
types plus the cross-cutting features:

  Echo           unary          echo back + server time + a server sequence no.
  GetRandomUser  unary          MOCK/RANDOM data (name/email/age/country)
  StreamTicks    server stream  N random "ticks" (a price/sensor-style feed)
  SumNumbers     client stream  sum / count / average of the numbers you send
  Chat           bidi stream    echoes each message back, stamped server-side
  EchoMetadata   unary          reflects request metadata + sends response metadata
  SecureEcho     unary          like Echo, but requires auth-via-metadata credentials
  RaiseError     unary          fails with the gRPC status code you request

Two listeners are opened (same service on both, only the transport differs):

  localhost:9000   plaintext gRPC / HTTP-2 cleartext (h2c)
  localhost:9001   gRPC over TLS  / HTTP-2 (h2), self-signed cert

Server reflection is enabled, so API Dash's Reflect button (and grpcurl)
discovers every method with no `.proto` file needed.

Configuration (environment variables):
  GRPC_PLAINTEXT_PORT   plaintext listen port          (default: 9000)
  GRPC_TLS_PORT         TLS listen port                (default: 9001)
  GRPC_TLS_CERT         PEM certificate for the TLS port (default: /certs/server.crt)
  GRPC_TLS_KEY          PEM private key for the TLS port (default: /certs/server.key)
  GRPC_MAX_WORKERS      thread-pool size               (default: 10)
  GRPC_MAX_TICKS        hard cap on StreamTicks count  (default: 1000)

If the TLS cert/key are missing, the TLS port is skipped with a warning rather
than crashing -- so this file runs natively (point the env vars at a locally
generated cert) as well as in Docker (the entrypoint mints the cert first).

Everything here is intentionally simple and heavily commented -- it is a
testing fixture, not production code.
"""

import os
import random
import signal
import string
import threading
import uuid
from concurrent import futures
from datetime import datetime, timezone

import grpc
from grpc_reflection.v1alpha import reflection

# Generated from proto/apidash_test.proto by grpc_tools.protoc. The Dockerfile
# (and the native-verification steps) generate these next to this file before
# starting the server, so the import below resolves at runtime.
import apidash_test_pb2 as pb
import apidash_test_pb2_grpc as pb_grpc

# --- Configuration from the environment -------------------------------------
PLAINTEXT_PORT = int(os.environ.get("GRPC_PLAINTEXT_PORT", "9000"))
TLS_PORT = int(os.environ.get("GRPC_TLS_PORT", "9001"))
TLS_CERT = os.environ.get("GRPC_TLS_CERT", "/certs/server.crt")
TLS_KEY = os.environ.get("GRPC_TLS_KEY", "/certs/server.key")
MAX_WORKERS = int(os.environ.get("GRPC_MAX_WORKERS", "10"))
MAX_TICKS = int(os.environ.get("GRPC_MAX_TICKS", "1000"))

# --- Stream defaults / caps (mirrored in docs/grpc/server_streaming.md) ------
DEFAULT_TICK_COUNT = 10
DEFAULT_TICK_INTERVAL_MS = 500
MAX_TICK_INTERVAL_MS = 10_000  # keep a single stream from hanging for minutes

# --- Mock data for GetRandomUser (hand-rolled, like a fixtures file) ---------
FIRST_NAMES = [
    "Ada", "Grace", "Alan", "Linus", "Margaret", "Dennis", "Katherine",
    "Guido", "Barbara", "Ken", "Radia", "Tim",
]
LAST_NAMES = [
    "Lovelace", "Hopper", "Turing", "Torvalds", "Hamilton", "Ritchie",
    "Johnson", "van Rossum", "Liskov", "Thompson", "Perlman", "Berners-Lee",
]
COUNTRIES = [
    "India", "United States", "Germany", "Japan", "Brazil", "Kenya",
    "Canada", "Finland", "Australia", "France",
]
EMAIL_DOMAINS = ["example.com", "test.dev", "mail.invalid", "apidash.dev"]

# --- Accepted credentials for SecureEcho (auth-via-metadata) -----------------
# The call is accepted if EITHER of these matches. Fixed test values -- this is
# a fixture, not a real credential store. (See docs/grpc/auth.md.)
VALID_BEARER = "Bearer test-token"  # metadata "authorization"
VALID_API_KEY = "test-apikey"       # metadata "x-api-key"


def log(msg):
    """Timestamped stdout logging (see `docker compose logs server`)."""
    print(f"[{datetime.now(timezone.utc).isoformat()}] {msg}", flush=True)


def now_iso():
    return datetime.now(timezone.utc).isoformat()


class TestService(pb_grpc.TestServiceServicer):
    """Implements every method in apidash.test.TestService with mock/random data.

    gRPC dispatches each call on a worker thread from the pool, so the only
    shared mutable state -- the Echo sequence counter -- is guarded by a lock.
    """

    def __init__(self):
        self._seq_lock = threading.Lock()
        self._seq = 0

    def _next_seq(self):
        with self._seq_lock:
            self._seq += 1
            return self._seq

    # --- Unary: echo + server time + sequence number ------------------------
    def Echo(self, request, context):
        seq = self._next_seq()
        log(f"Echo(seq={seq}) message={request.message!r}")
        return pb.EchoResponse(
            message=request.message,
            server_time=now_iso(),
            seq=seq,
        )

    # --- Unary: mock/random user -------------------------------------------
    def GetRandomUser(self, request, context):
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        # A short random local-part so repeated calls don't collide.
        handle = (first[0] + last).lower().replace(" ", "").replace("-", "")
        suffix = "".join(random.choices(string.digits, k=3))
        user = pb.User(
            id=str(uuid.uuid4()),
            name=f"{first} {last}",
            email=f"{handle}{suffix}@{random.choice(EMAIL_DOMAINS)}",
            age=random.randint(18, 80),
            country=random.choice(COUNTRIES),
        )
        log(f"GetRandomUser -> {user.name} ({user.country}, {user.age})")
        return user

    # --- Server streaming: a random tick feed -------------------------------
    def StreamTicks(self, request, context):
        # Sane defaults when the client leaves fields at 0, plus hard caps so a
        # bad request can't make the server stream forever.
        count = request.count if request.count > 0 else DEFAULT_TICK_COUNT
        count = min(count, MAX_TICKS)
        interval_ms = (
            request.interval_ms if request.interval_ms > 0 else DEFAULT_TICK_INTERVAL_MS
        )
        interval_ms = min(interval_ms, MAX_TICK_INTERVAL_MS)
        log(f"StreamTicks(count={count}, interval_ms={interval_ms})")

        for i in range(1, count + 1):
            # Stop early if the client cancelled / disconnected.
            if not context.is_active():
                log(f"StreamTicks: client went away after {i - 1} ticks")
                return
            yield pb.Tick(
                seq=i,
                value=round(random.uniform(0, 100), 4),
                ts=now_iso(),
            )
            # Don't sleep after the final tick.
            if i < count:
                # context.time_remaining()-aware wait would be nicer, but a plain
                # sleep is fine for a fixture; is_active() above catches cancels.
                _interruptible_sleep(interval_ms / 1000.0, context)

    # --- Client streaming: sum / count / average ----------------------------
    def SumNumbers(self, request_iterator, context):
        total = 0.0
        count = 0
        for req in request_iterator:  # blocks until the client half-closes
            total += req.value
            count += 1
        average = (total / count) if count else 0.0
        log(f"SumNumbers: count={count} sum={total} avg={average}")
        return pb.SumResponse(sum=total, count=count, average=average)

    # --- Bidirectional streaming: timestamped echo --------------------------
    def Chat(self, request_iterator, context):
        # Full-duplex: read each incoming message and immediately echo it back
        # with a server timestamp. The response stream ends when the client
        # half-closes its request stream.
        for msg in request_iterator:
            log(f"Chat: {msg.user!r} -> {msg.text!r}")
            yield pb.ChatMessage(
                user=msg.user,
                text=msg.text,
                ts=now_iso(),  # server stamps the reply
            )

    # --- Unary: echo request metadata + send response metadata --------------
    def EchoMetadata(self, request, context):
        # invocation_metadata() is the gRPC equivalent of request headers. This
        # is how auth-via-metadata (e.g. an `authorization` token) is tested:
        # whatever the client sent comes straight back in the response body.
        out = {}
        for key, value in context.invocation_metadata():
            # Binary metadata keys end in "-bin" and carry bytes; render those
            # readably so the map<string,string> response stays valid.
            if isinstance(value, bytes):
                value = value.decode("utf-8", "replace")
            out[key] = value

        # Also send metadata BACK (server -> client) so the response-metadata /
        # headers view is testable: initial metadata is delivered with the
        # response headers, trailing metadata with the final trailers.
        context.send_initial_metadata(
            [("x-server", "apidash-grpc-test"), ("x-echoed-count", str(len(out)))]
        )
        context.set_trailing_metadata([("x-trailer", "ok")])

        log(f"EchoMetadata: {len(out)} metadata entrie(s)")
        return pb.MetadataResponse(metadata=out)

    # --- Unary: auth-protected echo (auth-via-metadata) ---------------------
    def SecureEcho(self, request, context):
        # gRPC has no built-in auth; credentials travel as metadata. Accept the
        # call if EITHER a Bearer token OR an API key matches; otherwise abort
        # UNAUTHENTICATED. This exercises API Dash's Auth tab (Bearer token ->
        # `authorization` metadata) and API-key auth.
        md = dict(context.invocation_metadata())
        authorized = (
            md.get("authorization") == VALID_BEARER
            or md.get("x-api-key") == VALID_API_KEY
        )
        if not authorized:
            log("SecureEcho: DENIED (missing or invalid credentials)")
            context.abort(
                grpc.StatusCode.UNAUTHENTICATED,
                "missing or invalid credentials -- send 'authorization: Bearer "
                "test-token' or 'x-api-key: test-apikey'",
            )

        seq = self._next_seq()
        log(f"SecureEcho(seq={seq}) message={request.message!r} [authenticated]")
        return pb.EchoResponse(
            message=f"[authenticated] {request.message}",
            server_time=now_iso(),
            seq=seq,
        )

    # --- Unary: fail with the requested gRPC status code --------------------
    def RaiseError(self, request, context):
        # Map the requested numeric code to a grpc.StatusCode. Anything out of
        # range (or 0/OK, which wouldn't be an error) becomes UNKNOWN.
        code = _status_code_from_int(request.code)
        message = request.message or f"requested error with status code {request.code}"
        log(f"RaiseError -> {code.name} ({code.value[0]}): {message!r}")
        # context.abort() raises, terminating the RPC with this status; the line
        # after it never runs.
        context.abort(code, message)
        return pb.Empty()  # unreachable; keeps linters/type-checkers happy


def _interruptible_sleep(seconds, context):
    """Sleep, but wake early if the client cancels the streaming call."""
    # Poll in small slices so a cancelled StreamTicks stops promptly instead of
    # blocking the worker thread for the full interval.
    slice_s = 0.1
    waited = 0.0
    while waited < seconds:
        if not context.is_active():
            return
        step = min(slice_s, seconds - waited)
        _real_sleep(step)
        waited += step


# Wrapped so tests/fixtures could monkeypatch it; plain time.sleep otherwise.
def _real_sleep(seconds):
    import time

    time.sleep(seconds)


def _status_code_from_int(code):
    """Map an int gRPC status code (0-16) to grpc.StatusCode; UNKNOWN if bad."""
    for status in grpc.StatusCode:
        # status.value is a (int_code, str_name) tuple, e.g. (5, 'not found').
        if status.value[0] == code:
            # Never abort with OK -- that isn't an error. Fall through to UNKNOWN.
            if status is grpc.StatusCode.OK:
                break
            return status
    return grpc.StatusCode.UNKNOWN


def _load_server_credentials():
    """Build TLS server credentials from the configured cert/key, or None if
    they aren't present (in which case the TLS port is skipped)."""
    if not (os.path.exists(TLS_CERT) and os.path.exists(TLS_KEY)):
        return None
    with open(TLS_KEY, "rb") as f:
        key = f.read()
    with open(TLS_CERT, "rb") as f:
        cert = f.read()
    # require_client_auth=False -> ordinary server-side TLS (self-signed here).
    return grpc.ssl_server_credentials([(key, cert)])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    pb_grpc.add_TestServiceServicer_to_server(TestService(), server)

    # --- Server reflection --------------------------------------------------
    # Advertise our service (plus the reflection service itself) so clients can
    # discover every method with no .proto import. This is what powers API
    # Dash's Reflect button and `grpcurl ... list`.
    service_names = (
        pb.DESCRIPTOR.services_by_name["TestService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(service_names, server)

    # --- Plaintext listener (h2c) ------------------------------------------
    server.add_insecure_port(f"[::]:{PLAINTEXT_PORT}")
    log(f"plaintext gRPC listening on 0.0.0.0:{PLAINTEXT_PORT}")

    # --- TLS listener (h2) --------------------------------------------------
    creds = _load_server_credentials()
    if creds is not None:
        server.add_secure_port(f"[::]:{TLS_PORT}", creds)
        log(f"TLS gRPC listening on 0.0.0.0:{TLS_PORT} (cert={TLS_CERT})")
    else:
        log(
            f"TLS cert/key not found ({TLS_CERT} / {TLS_KEY}); skipping TLS port "
            f"{TLS_PORT}. Generate a self-signed cert to enable it."
        )

    log("advertised services: " + ", ".join(service_names))
    server.start()

    # --- Graceful shutdown on SIGTERM/SIGINT --------------------------------
    stop_event = threading.Event()

    def handle_signal(signum, _frame):
        log(f"signal {signum} received; shutting down")
        stop_event.set()

    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)

    stop_event.wait()  # block the main thread until a signal arrives
    server.stop(grace=2).wait()
    log("stopped")


if __name__ == "__main__":
    serve()
