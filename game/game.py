# game/game.py
import asyncio
import websockets
import json

async def listen():
    uri = "ws://localhost:8080"  # Address of your Node.js server
    async with websockets.connect(uri) as websocket:
        print("Connected to Node.js WebSocket server")

        while True:
            try:
                message = await websocket.recv()
                data = json.loads(message)

                if data["type"] == "Key Input":
                    print(f"Received from user {data['id']}: {data['content']}")
                else:
                    print("Other message:", data)

            except websockets.exceptions.ConnectionClosed:
                print("Connection closed")
                break
            except Exception as e:
                print("Error:", e)

asyncio.run(listen())
