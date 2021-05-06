import websockets

import asyncio

async def main():
    async with websockets.connect("ws://127.0.0.1:8000/ws") as websocket:
        while True:
            await websocket.send(input())
            print(await websocket.recv())


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())