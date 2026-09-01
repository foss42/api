"""
Integration tests for the local MQTT test rig (mqtt/docker-compose.yml).

These talk to a REAL broker over TCP (paho-mqtt against localhost:1883), which
is the only way to genuinely exercise QoS handshakes, retained messages,
wildcards and MQTT v5 -- the same reason we ship a Dockerized Mosquitto rather
than a hand-rolled FastAPI route.

The whole module SKIPS gracefully when:
  - paho-mqtt is not installed, or
  - no broker is reachable at MQTT_HOST:MQTT_PORT (default localhost:1883),
so CI without a broker still passes. To run them for real:

    docker compose -f mqtt/docker-compose.yml up -d
    pytest mqtt/tests

The echo request->response test additionally needs the `publisher` service
running; it skips (rather than fails) if no echo reply arrives.
"""

import os
import socket
import threading
import time
import uuid
from queue import Empty, Queue

import pytest

# Skip cleanly if paho-mqtt is not installed.
mqtt = pytest.importorskip("paho.mqtt.client", reason="paho-mqtt not installed")

MQTT_HOST = os.environ.get("MQTT_HOST", "localhost")
MQTT_PORT = int(os.environ.get("MQTT_PORT", "1883"))


def _broker_reachable(host, port, timeout=1.0):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


# Skip the entire module if there is no broker to talk to. This keeps CI green
# when no MQTT broker is running.
if not _broker_reachable(MQTT_HOST, MQTT_PORT):
    pytest.skip(
        f"No MQTT broker reachable at {MQTT_HOST}:{MQTT_PORT} "
        "(start one with `docker compose -f mqtt/docker-compose.yml up`)",
        allow_module_level=True,
    )


def _make_raw_client():
    cid = f"pytest-{uuid.uuid4().hex[:8]}"
    try:
        return mqtt.Client(
            callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
            client_id=cid,
            protocol=mqtt.MQTTv5,
        )
    except AttributeError:
        # paho-mqtt 1.x fallback.
        return mqtt.Client(client_id=cid, protocol=mqtt.MQTTv5)


def _topic():
    """A unique topic per test, so tests never interfere with one another."""
    return f"apidash/test/pytest/{uuid.uuid4().hex}"


@pytest.fixture
def client_factory():
    """Returns a factory that builds connected clients; all are cleaned up."""
    created = []

    def _factory():
        client = _make_raw_client()
        messages = Queue()
        subacks = Queue()
        connected = threading.Event()

        client.on_message = lambda cl, ud, msg: messages.put(msg)
        client.on_subscribe = lambda *args: subacks.put(True)
        client.on_connect = lambda *args: connected.set()

        client.connect(MQTT_HOST, MQTT_PORT, keepalive=30)
        client.loop_start()
        if not connected.wait(timeout=5):
            pytest.fail(f"Timed out connecting to {MQTT_HOST}:{MQTT_PORT}")

        # Stash the queues on the client for the helpers below.
        client._messages = messages
        client._subacks = subacks
        created.append(client)
        return client

    yield _factory

    for client in created:
        try:
            client.loop_stop()
            client.disconnect()
        except Exception:
            pass


def _subscribe(client, topic, qos=0, timeout=5):
    """Subscribe and block until the SUBACK arrives (avoids lost messages)."""
    client.subscribe(topic, qos=qos)
    try:
        client._subacks.get(timeout=timeout)
    except Empty:
        pytest.fail(f"No SUBACK for '{topic}'")


def _next_message(client, timeout=5):
    try:
        return client._messages.get(timeout=max(0.01, timeout))
    except Empty:
        return None


def _wait_for_payload(client, payload, timeout=5):
    """Drain messages until one matches `payload` (ignores unrelated traffic)."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        msg = _next_message(client, timeout=deadline - time.time())
        if msg is None:
            return None
        if msg.payload == payload:
            return msg
    return None


# --------------------------------------------------------------------------- #
# Tests
# --------------------------------------------------------------------------- #
def test_connect_publish_subscribe_roundtrip(client_factory):
    topic = _topic()
    sub = client_factory()
    _subscribe(sub, topic, qos=0)

    pub = client_factory()
    pub.publish(topic, payload="hello-mqtt", qos=0)

    msg = _next_message(sub)
    assert msg is not None, "did not receive published message"
    assert msg.topic == topic
    assert msg.payload == b"hello-mqtt"


def test_retained_delivered_on_subscribe(client_factory):
    topic = _topic()

    # Publish a retained message BEFORE anyone is subscribed.
    pub = client_factory()
    pub.publish(topic, payload="i-am-retained", qos=1, retain=True).wait_for_publish(5)

    # A brand-new subscriber must receive it immediately on subscribe.
    sub = client_factory()
    _subscribe(sub, topic, qos=1)
    msg = _next_message(sub)
    assert msg is not None, "retained message not delivered on subscribe"
    assert msg.payload == b"i-am-retained"
    assert msg.retain is True

    # Cleanup: clear the retained message (empty payload + retain=True).
    pub.publish(topic, payload=b"", qos=1, retain=True).wait_for_publish(5)


def test_wildcard_multi_level_hash(client_factory):
    base = _topic()
    sub = client_factory()
    _subscribe(sub, f"{base}/#", qos=0)

    pub = client_factory()
    pub.publish(f"{base}/a/b/c", payload="deep", qos=0)

    msg = _next_message(sub)
    assert msg is not None, "'#' wildcard did not match nested topic"
    assert msg.topic == f"{base}/a/b/c"
    assert msg.payload == b"deep"


def test_wildcard_single_level_plus(client_factory):
    base = _topic()
    sub = client_factory()
    _subscribe(sub, f"{base}/+/leaf", qos=0)

    pub = client_factory()
    pub.publish(f"{base}/x/leaf", payload="match", qos=0)
    msg = _next_message(sub)
    assert msg is not None, "'+' wildcard did not match single level"
    assert msg.topic == f"{base}/x/leaf"

    # A topic with an EXTRA level must NOT match `+/leaf`.
    pub.publish(f"{base}/x/y/leaf", payload="nomatch", qos=0)
    extra = _next_message(sub, timeout=1)
    assert extra is None, "'+' wildcard wrongly matched an extra level"


def test_qos1_delivery(client_factory):
    topic = _topic()
    sub = client_factory()
    _subscribe(sub, topic, qos=1)

    pub = client_factory()
    pub.publish(topic, payload="qos1", qos=1).wait_for_publish(5)

    msg = _next_message(sub)
    assert msg is not None, "QoS 1 message not delivered"
    assert msg.payload == b"qos1"
    assert msg.qos == 1


def test_qos2_delivery(client_factory):
    topic = _topic()
    sub = client_factory()
    _subscribe(sub, topic, qos=2)

    pub = client_factory()
    pub.publish(topic, payload="qos2", qos=2).wait_for_publish(5)

    msg = _next_message(sub)
    assert msg is not None, "QoS 2 message not delivered"
    assert msg.payload == b"qos2"
    assert msg.qos == 2


def test_echo_request_response(client_factory):
    """Exercises the publisher service (mqtt/publisher.py).

    Skips (rather than fails) when the publisher is not running.
    """
    sub = client_factory()
    _subscribe(sub, "apidash/test/echo/response", qos=1)

    pub = client_factory()
    payload = f"echo-{uuid.uuid4().hex}".encode()
    pub.publish("apidash/test/echo/request", payload=payload, qos=1)

    msg = _wait_for_payload(sub, payload, timeout=5)
    if msg is None:
        pytest.skip(
            "No echo response -- the `publisher` service is not running "
            "(start it with `docker compose -f mqtt/docker-compose.yml up`)"
        )
    assert msg.payload == payload
