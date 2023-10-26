import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
	print("Connected")

@sio.event
def set_name(sid, name):
	print("Set name: " + name)

if __name__ == "__main__":
	eventlet.wsgi.server(eventlet.listen(('', 8080)), app)