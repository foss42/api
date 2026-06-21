import asyncio
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

sse_router = APIRouter(tags=["SSE"])

async def sse_event_generator(count: int):
    for i in range(1, count + 1):
        yield f"data: event{i}\n\n"
        await asyncio.sleep(1)

@sse_router.get('/events/{count}')
async def sse_events(count: int):
    if count > 100:
        raise HTTPException(status_code=400, detail="Count cannot exceed 100")
    return StreamingResponse(sse_event_generator(count), 
        media_type="text/event-stream")
