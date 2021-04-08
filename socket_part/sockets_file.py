import socketio
import string
from random import randint
from pprint import pprint
from socket_part.services import (
    get_query_values,
    log_print,
    get_room,
    authentication
)


ROOM = 'common'

sio = socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi', logger=True)


@sio.event
async def connect(sid, environ, auth):
    query = get_query_values(environ=environ, needed_params=('room',))
    response = dict(
        sid=sid
    )
    username, password = authentication(auth=auth)
    response['username'] = username
    if not query['room']:
        # TODO mb add func to generating room
        # room = ''.join(string.ascii_letters[randint(0, len(string.ascii_letters)-1)] for i in range(10))
        room = ROOM
    else:
        room = query['room']
    sio.enter_room(sid=sid, room=room)
    response['room'] = room
    await sio.emit('ready', response, room=room, skip_sid=False)

# @sio.event
# async def data(sid, data):
#     peerToSend = None
#     if 'sid' in data:
#       peerToSend = data['sid']
#     data['sid'] = sid
#     await sio.emit('data', data, room=peerToSend, skip_sid=sid)


@sio.event
async def msg(sid, message):
    data = {'sid': sid, 'text': message}
    room_data = sio.rooms(sid=sid)
    room = get_room(list_to_extract_room_from=room_data, sid=sid)
    log_print(room=room, data=data)
    await sio.emit('msg', data=data, room=room)


@sio.event
async def sharing(sid):
    data = {'sid': sid, 'text': 'Start sharing file'}
    room = get_room(list_to_extract_room_from=sio.rooms(sid=sid), sid=sid)
    log_print(room=room, data=data)
    await sio.emit('msg', data=data, room=room)


@sio.event
async def disconnect(sid):
    print(f'Disconnected client {sid}')
    # await sio.emit('disconnect', {'sid': sid}, room=ROOM, skip_sid=sid)
    room_data = sio.rooms(sid=sid)
    room = get_room(list_to_extract_room_from=room_data, sid=sid)
    log_print(room=room)
    sio.leave_room(sid=sid, room=room)
