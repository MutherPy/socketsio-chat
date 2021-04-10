from socketio.exceptions import ConnectionRefusedError
import typing as t


def authentication(auth: dict) -> str:
    token = auth['token']
    #
    # TODO check JWT
    #
    username = 'Alex'
    if username is None:
        raise ConnectionRefusedError('Authentication failed')
    return username
