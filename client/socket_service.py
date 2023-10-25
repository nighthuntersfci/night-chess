import socketio

sio = socketio.AsyncClient()

async def start():
	await sio.connect("http://localhost:8080")
	await sio.wait()