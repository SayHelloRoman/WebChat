import websockets

import asyncio

async def chat():
    async with websockets.connect("ws://127.0.0.1:8000/ws") as websocket:
        #while True:
        await websocket.send("Hello")

asyncio.get_event_loop().run_until_complete(chat())