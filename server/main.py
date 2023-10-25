import socketio
from aiohttp import web

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

@sio.event
def connect(sid, environ):
	print("Connected")

if __name__ == "__main__":
	web.run_app(app)