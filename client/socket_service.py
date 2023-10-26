import socketio

sio = socketio.Client()

def set_username(name):
	sio.emit("set_name", name)

def start():
	sio.connect("http://localhost:8080", transports=['websocket'])
	sio.wait()