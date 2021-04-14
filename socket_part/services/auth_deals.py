from socketio.exceptions import ConnectionRefusedError
from database_part import db
from settings import fast_api_settings
from fastapi_part.services import decrypt_jwt


async def authentication(auth: dict) -> str:
    token = auth['token']
    username = decrypt_jwt(token, fast_api_settings().SECRET_KEY)['user']
    async with db:
        exist = db.proof_user(username)
    if username is None or not exist:
        raise ConnectionRefusedError('Authentication failed')
    return username
