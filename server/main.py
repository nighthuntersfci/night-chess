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
	sio.emit("create_room_id", len(data.rooms), room=sid)
	
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

@sio.event
def join(sid, room_id):
    data.rooms[room_id]["players"].append({
        "name": data.usernames[sid],
        "id": sid,
        "color": "B"
    })
    sio.emit("update_opponent_name", data.usernames[sid], room=data.rooms[room_id]["players"][0]["id"])

@sio.event
def update_board(sid, game_data):
    for i in data.rooms[game_data["id"]]["players"]:
        if i["id"] != sid:
            sio.emit("update_board", game_data["data"], room=i["id"])
            break
    

if __name__ == "__main__":
	eventlet.wsgi.server(eventlet.listen(('', 7777)), app)
