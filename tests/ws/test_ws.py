import json

def test_websocket_echo_text(client):
    with client.websocket_connect("/ws/echo") as websocket:
        websocket.send_text("Hello WebSocket")
        data = websocket.receive_text()
        assert data == "Hello WebSocket"

def test_websocket_echo_json(client):
    with client.websocket_connect("/ws/echo") as websocket:
        json_msg = json.dumps({"message": "Hello WebSocket"})
        websocket.send_text(json_msg)
        data = websocket.receive_text()
        assert json.loads(data) == {"message": "Hello WebSocket"}

def test_websocket_heartbeat_ping(client):
    with client.websocket_connect("/ws/heartbeat") as websocket:
        websocket.send_json({"message": "ping"})
        data = websocket.receive_json()
        assert data == {"type": "heartbeat", "message": "pong"}

def test_websocket_heartbeat_message(client):
    with client.websocket_connect("/ws/heartbeat") as websocket:
        websocket.send_json({"message": "hello world"})
        data = websocket.receive_json()
        assert data == {"type": "message", "data": {"message": "hello world"}}

from starlette.websockets import WebSocketDisconnect
import pytest

def test_websocket_strict_heartbeat_timeout(client):
    with pytest.raises(WebSocketDisconnect) as exc:
        with client.websocket_connect("/ws/timeout/1") as websocket:
            websocket.receive_json()
    assert exc.value.code == 1008

def test_websocket_strict_heartbeat_success(client):
    with client.websocket_connect("/ws/timeout/1") as websocket:
        websocket.send_json({"message": "ping"})
        data = websocket.receive_json()
        assert data == {"type": "heartbeat", "message": "pong"}
