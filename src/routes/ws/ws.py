import asyncio
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

@ws_router.websocket("/heartbeat")
async def websocket_heartbeat(websocket: WebSocket):
    await websocket.accept()
    
    async def send_heartbeat():
        try:
            while True:
                await asyncio.sleep(5)
                await websocket.send_json({"type": "heartbeat", "message": "ping"})
        except asyncio.CancelledError:
            pass

    async def receive_messages():
        try:
            while True:
                try:
                    data = await websocket.receive_json()
                    if data.get("message") == "ping":
                        await websocket.send_json({"type": "heartbeat", "message": "pong"})
                    else:
                        await websocket.send_json({"type": "message", "data": data})
                except json.JSONDecodeError:
                    await websocket.send_json({"type": "error", "message": "Invalid JSON"})
        except WebSocketDisconnect:
            pass
        except asyncio.CancelledError:
            pass

    heartbeat_task = asyncio.create_task(send_heartbeat())
    receive_task = asyncio.create_task(receive_messages())
    
    done, pending = await asyncio.wait(
        [heartbeat_task, receive_task],
        return_when=asyncio.FIRST_COMPLETED,
    )
    
    for task in pending:
        task.cancel()

@ws_router.websocket("/timeout/{timeout}")
async def websocket_strict_heartbeat(websocket: WebSocket, timeout: int):
    await websocket.accept()
    try:
        while True:
            try:
                data = await asyncio.wait_for(websocket.receive_json(), timeout=timeout)
                if data.get("message") == "ping":
                    await websocket.send_json({"type": "heartbeat", "message": "pong"})
                else:
                    await websocket.send_json({"type": "message", "data": data})
            except asyncio.TimeoutError:
                await websocket.close(code=1008, reason="Heartbeat timeout")
                break
            except json.JSONDecodeError:
                await websocket.send_json({"type": "error", "message": "Invalid JSON"})
    except WebSocketDisconnect:
        pass
