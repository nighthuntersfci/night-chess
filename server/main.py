import data
import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
	print("User Connected: " + sid)
	sio.emit("update_rooms", data.rooms, room=sid)

@sio.event
def set_name(sid, name):
	print("Socket " + sid + " name set: " + name)
	data.usernames[sid] = name

@sio.event
def create_room(sid):
	sio.emit("create_room_id", len(data.rooms) - 1, room=sid)
	
	data.rooms.append({
		"name": data.usernames[sid],
        "players": [
            {
                "name": data.usernames[sid],
                "id": sid,
                "color": "W"
            },
        ]
	})
	
	sio.emit("update_rooms", data.rooms)

	print("Created room!")

if __name__ == "__main__":
	eventlet.wsgi.server(eventlet.listen(('', 7777)), app)
