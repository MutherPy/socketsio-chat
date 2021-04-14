from fastapi import UploadFile
import aiofiles
import pathlib

from settings import fast_api_settings, FastApiSettings
from .crypto_deals import (encrypt_path,
                           decrypt_path)


async def saving_shared_files(room: str, file: UploadFile, setting: FastApiSettings = fast_api_settings()):
    filename = file.filename
    file = file.file.read()
    path = f'{setting.MEDIA_DIR}/{room}/{filename}'
    pathlib.Path(pathlib.os.path.dirname(path)).mkdir(parents=True, exist_ok=True)
    async with aiofiles.open(path, 'wb') as saving:
        await saving.write(file)
    return encrypt_path(path, setting.SECRET_KEY)


async def giving_shared_file(token: str, setting: FastApiSettings = fast_api_settings()):
    path = decrypt_path(token, setting.SECRET_KEY)
    return path
