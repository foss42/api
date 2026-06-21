from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json

ws_router = APIRouter(tags=["WebSockets"])


@ws_router.websocket("/echo")
async def websocket_echo(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            try:
                # If it's valid JSON, echo it back as text (re-serialized).
                json_data = json.loads(data)
                await websocket.send_text(json.dumps(json_data))
            except json.JSONDecodeError:
                # Otherwise, echo the raw string unchanged.
                await websocket.send_text(data)
    except WebSocketDisconnect:
        pass
