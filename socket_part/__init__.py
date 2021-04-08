from socket_part.sockets_file import sio, socketio

asgi = socketio.ASGIApp

__all__ = [
    'sio',
    'asgi'
]
