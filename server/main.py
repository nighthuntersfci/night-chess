import data
import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
	print("User Connected: " + sid);

@sio.event
def set_name(sid, name):
	print("Socket " + sid + " name set: " + name)
	data.usernames[sid] = name

if __name__ == "__main__":
	eventlet.wsgi.server(eventlet.listen(('', 7777)), app)