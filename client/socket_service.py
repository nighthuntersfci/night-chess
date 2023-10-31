import socketio
import data

sio = socketio.Client()

def set_username(name):
	sio.emit("set_name", name)

@sio.event
def update_rooms(rooms):
	print("Update rooms!")
	data.rooms = rooms

def start():
	sio.connect("http://localhost:7777")
	sio.wait()