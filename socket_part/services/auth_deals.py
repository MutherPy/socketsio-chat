from socketio.exceptions import ConnectionRefusedError
import typing as t
from database_part import db


async def authentication(auth: dict) -> str:
    token = auth['token']
    #
    # TODO check JWT
    #
    username = token  # get username from token
    async with db:
        exist = db.proof_user(username)
    if username is None or not exist:
        raise ConnectionRefusedError('Authentication failed')
    return username
