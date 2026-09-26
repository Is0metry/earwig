import asyncio
import websockets

async def test_ws():
    uri = "ws://localhost:8000/player/ws"
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected!")
            message = await websocket.recv()
            print(f"Received: {message}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_ws())
