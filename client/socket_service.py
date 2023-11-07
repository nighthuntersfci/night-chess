import socketio
import data

sio = socketio.Client()

def set_username(name):
	sio.emit("set_name", name)

@sio.event
def update_rooms(rooms):
    print("Update rooms!")
    data.rooms = rooms
    
    if data.rooms_window != None:
        data.rooms_window.refresh()

@sio.event
def create_room_id(id):
	print("Created Room ID " + str(id))
	data.current_room = id

@sio.event
def update_opponent_name(name):
    data.room_window.update_opponent_name(name);

def start():
	sio.connect("http://localhost:7777")
	sio.wait()
