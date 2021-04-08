from socketio.exceptions import ConnectionRefusedError
import typing as t


def authentication(auth: dict) -> t.Tuple[str, t.Union[str, None]]:
    username = auth.get('username', None)
    password = auth.get('password', None)
    if username is None:
        raise ConnectionRefusedError('Authentication failed')
    return username, password
