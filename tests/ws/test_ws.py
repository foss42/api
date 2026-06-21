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
