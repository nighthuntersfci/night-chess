import socketio
import data

sio = socketio.Client()

def set_username(name):
	sio.emit("set_name", name)

@sio.event
def update_rooms(rooms):
	print("Update rooms!")
	data.rooms = rooms

@sio.event
def create_room_id(id):
	print("Created Room ID " + str(id))
	data.current_room = id

def start():
	sio.connect("http://localhost:7777")
	sio.wait()