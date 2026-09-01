"""
Integration tests for the local gRPC test rig (grpc/docker-compose.yml).

These talk to a REAL gRPC server over HTTP/2 (grpcio against localhost:9000),
which is the only way to genuinely exercise reflection, the three streaming
modes, metadata / auth-via-metadata and gRPC status codes -- the same reason we
ship a Dockerized `apidash.test.TestService` (grpc/server.py) rather than a
hand-rolled FastAPI route.

The Protobuf stubs are generated ON THE FLY at import time from
`grpc/proto/apidash_test.proto` (via grpc_tools.protoc) into a temp dir that is
put on sys.path -- so nothing generated is committed, exactly like the Docker
image builds them at build time.

The whole module SKIPS gracefully when:
  - grpcio is not installed, or
  - grpcio-tools is not installed (can't generate the stubs), or
  - no server is reachable at GRPC_HOST:GRPC_PORT (default localhost:9000),
so CI without a server still passes. To run them for real:

    docker compose -f grpc/docker-compose.yml up --build -d
    pip install -r grpc/requirements-dev.txt
    pytest grpc/tests

Each test is independent and hits one feature of the service.
"""

import os
import socket
import sys
import tempfile

import pytest

# Skip cleanly if grpcio / grpcio-tools are not installed.
grpc = pytest.importorskip("grpc", reason="grpcio not installed")
protoc = pytest.importorskip(
    "grpc_tools.protoc", reason="grpcio-tools not installed (needed to gen stubs)"
)

GRPC_HOST = os.environ.get("GRPC_HOST", "localhost")
GRPC_PORT = int(os.environ.get("GRPC_PORT", "9000"))
GRPC_TARGET = f"{GRPC_HOST}:{GRPC_PORT}"


def _server_reachable(host, port, timeout=1.0):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def _find_repo_root(start):
    """Walk up from `start` until we find grpc/proto/apidash_test.proto."""
    d = os.path.abspath(start)
    while True:
        if os.path.isfile(os.path.join(d, "grpc", "proto", "apidash_test.proto")):
            return d
        parent = os.path.dirname(d)
        if parent == d:  # reached the filesystem root
            return None
        d = parent


_REPO_ROOT = _find_repo_root(os.path.dirname(__file__))
if _REPO_ROOT is None:
    pytest.skip(
        "Could not locate grpc/proto/apidash_test.proto relative to this test.",
        allow_module_level=True,
    )

# Skip the entire module if there is no server to talk to. This keeps CI green
# when no gRPC server is running.
if not _server_reachable(GRPC_HOST, GRPC_PORT):
    pytest.skip(
        f"No gRPC server reachable at {GRPC_TARGET} "
        "(start it with `docker compose -f grpc/docker-compose.yml up --build`)",
        allow_module_level=True,
    )


def _generate_stubs(repo_root):
    """Run grpc_tools.protoc to generate the pb2 stubs into a temp dir on sys.path."""
    proto_dir = os.path.join(repo_root, "grpc", "proto")
    proto_file = os.path.join(proto_dir, "apidash_test.proto")
    out_dir = tempfile.mkdtemp(prefix="apidash_grpc_stubs_")
    rc = protoc.main(
        [
            "grpc_tools.protoc",
            f"-I{proto_dir}",
            f"--python_out={out_dir}",
            f"--grpc_python_out={out_dir}",
            proto_file,
        ]
    )
    if rc != 0:
        raise RuntimeError(f"grpc_tools.protoc failed with exit code {rc}")
    if out_dir not in sys.path:
        sys.path.insert(0, out_dir)
    return out_dir


_generate_stubs(_REPO_ROOT)

# These import names come from the generated stubs (put on sys.path above).
import apidash_test_pb2 as pb  # noqa: E402
import apidash_test_pb2_grpc as pb_grpc  # noqa: E402


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #
@pytest.fixture(scope="module")
def channel():
    """A plaintext gRPC channel to the test server, ready before any test runs."""
    ch = grpc.insecure_channel(GRPC_TARGET)
    try:
        grpc.channel_ready_future(ch).result(timeout=5)
    except grpc.FutureTimeoutError:  # pragma: no cover - guarded by socket check
        ch.close()
        pytest.skip(f"gRPC channel to {GRPC_TARGET} never became ready")
    yield ch
    ch.close()


@pytest.fixture
def stub(channel):
    return pb_grpc.TestServiceStub(channel)


# --------------------------------------------------------------------------- #
# Tests
# --------------------------------------------------------------------------- #
def test_reflection_lists_service(channel):
    """Server reflection advertises apidash.test.TestService."""
    reflection_pb2 = pytest.importorskip(
        "grpc_reflection.v1alpha.reflection_pb2",
        reason="grpcio-reflection not installed",
    )
    reflection_pb2_grpc = pytest.importorskip(
        "grpc_reflection.v1alpha.reflection_pb2_grpc",
        reason="grpcio-reflection not installed",
    )

    refl_stub = reflection_pb2_grpc.ServerReflectionStub(channel)
    request = reflection_pb2.ServerReflectionRequest(list_services="")
    responses = refl_stub.ServerReflectionInfo(iter([request]))

    service_names = []
    for resp in responses:
        service_names.extend(s.name for s in resp.list_services_response.service)

    assert "apidash.test.TestService" in service_names


def test_echo_unary(stub):
    """Echo echoes the message back, with a server time and a sequence number."""
    resp = stub.Echo(pb.EchoRequest(message="hello-grpc"), timeout=10)
    assert resp.message == "hello-grpc"
    assert resp.server_time  # non-empty ISO-8601 timestamp
    assert resp.seq >= 1


def test_get_random_user_populated(stub):
    """GetRandomUser returns a fully populated mock user."""
    user = stub.GetRandomUser(pb.Empty(), timeout=10)
    assert user.id
    assert user.name
    assert "@" in user.email
    assert 18 <= user.age <= 80
    assert user.country


def test_stream_ticks_yields_n(stub):
    """StreamTicks with count=N yields exactly N ticks, numbered 1..N."""
    n = 5
    ticks = list(
        stub.StreamTicks(pb.TickRequest(count=n, interval_ms=10), timeout=30)
    )
    assert len(ticks) == n
    assert [t.seq for t in ticks] == list(range(1, n + 1))
    assert all(t.ts for t in ticks)


def test_sum_numbers_client_stream(stub):
    """SumNumbers folds a stream of numbers into sum / count / average."""
    numbers = [1.5, 2.5, 4.0, 12.0]

    def gen():
        for value in numbers:
            yield pb.NumberRequest(value=value)

    resp = stub.SumNumbers(gen(), timeout=10)
    assert resp.count == len(numbers)
    assert resp.sum == pytest.approx(sum(numbers))
    assert resp.average == pytest.approx(sum(numbers) / len(numbers))


def test_chat_bidi_echoes_each_message(stub):
    """Chat (bidi) echoes each message back, stamped with a server timestamp."""
    outgoing = [("alice", "hi"), ("bob", "hey"), ("alice", "bye")]

    def gen():
        for user, text in outgoing:
            yield pb.ChatMessage(user=user, text=text)

    replies = list(stub.Chat(gen(), timeout=10))
    assert len(replies) == len(outgoing)
    for (user, text), reply in zip(outgoing, replies):
        assert reply.user == user
        assert reply.text == text
        assert reply.ts  # server stamps the echo


def test_echo_metadata_request_and_response(stub):
    """EchoMetadata reflects request metadata into the body AND returns
    initial (x-server) + trailing (x-trailer) response metadata."""
    request_md = (
        ("authorization", "Bearer test-token"),
        ("x-request-id", "abc123"),
    )
    response, call = stub.EchoMetadata.with_call(
        pb.Empty(), metadata=request_md, timeout=10
    )

    echoed = dict(response.metadata)
    assert echoed.get("authorization") == "Bearer test-token"
    assert echoed.get("x-request-id") == "abc123"

    initial = dict(call.initial_metadata())
    assert initial.get("x-server") == "apidash-grpc-test"

    trailing = dict(call.trailing_metadata())
    assert trailing.get("x-trailer") == "ok"


def test_secure_echo_requires_credentials(stub):
    """SecureEcho: no metadata -> UNAUTHENTICATED."""
    with pytest.raises(grpc.RpcError) as excinfo:
        stub.SecureEcho(pb.EchoRequest(message="hi"), timeout=10)
    assert excinfo.value.code() == grpc.StatusCode.UNAUTHENTICATED


def test_secure_echo_accepts_bearer_token(stub):
    """SecureEcho: valid Bearer token -> success."""
    resp = stub.SecureEcho(
        pb.EchoRequest(message="hi"),
        metadata=(("authorization", "Bearer test-token"),),
        timeout=10,
    )
    assert "hi" in resp.message
    assert resp.message.startswith("[authenticated]")


def test_secure_echo_accepts_api_key(stub):
    """SecureEcho: valid x-api-key -> success."""
    resp = stub.SecureEcho(
        pb.EchoRequest(message="viakey"),
        metadata=(("x-api-key", "test-apikey"),),
        timeout=10,
    )
    assert "viakey" in resp.message
    assert resp.message.startswith("[authenticated]")


def test_secure_echo_rejects_wrong_token(stub):
    """SecureEcho: wrong credentials -> UNAUTHENTICATED."""
    with pytest.raises(grpc.RpcError) as excinfo:
        stub.SecureEcho(
            pb.EchoRequest(message="hi"),
            metadata=(("authorization", "Bearer wrong"),),
            timeout=10,
        )
    assert excinfo.value.code() == grpc.StatusCode.UNAUTHENTICATED


def test_raise_error_maps_code(stub):
    """RaiseError with code=5 fails with NOT_FOUND."""
    with pytest.raises(grpc.RpcError) as excinfo:
        stub.RaiseError(pb.ErrorRequest(code=5, message="nope"), timeout=10)
    assert excinfo.value.code() == grpc.StatusCode.NOT_FOUND
