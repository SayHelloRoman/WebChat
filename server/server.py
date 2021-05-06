from typing import Optional

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from starlette.websockets import WebSocketDisconnect

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    async def broadcast(self, data: str):
        for connection in self.connections:
            await connection.send_text(data)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    while True:
        try:
            data = await websocket.receive_text()
            await manager.broadcast(data)

        except RuntimeError and WebSocketDisconnect:
            manager.connections.remove(websocket)
            break