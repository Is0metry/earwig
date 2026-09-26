import asyncio
import websockets

async def test_ws():
    uri = "ws://localhost:8000/player/ws"
    # The backend expects a cookie named 'cookie' based on the parameter name in get_cookie
    # But the backend sets 'earwigssession'. This is a likely mismatch.
    # Let's try sending 'earwigssession' first.
    headers = {
        "Cookie": "earwigssession=test_user"
    }
    try:
        async with websockets.connect(uri, extra_headers=headers) as websocket:
            print("Connected!")
            message = await websocket.recv()
            print(f"Received: {message}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_ws())
