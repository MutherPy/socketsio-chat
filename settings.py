import os
import typing as t
from pydantic import BaseSettings
from functools import lru_cache
from fernet import Fernet


def get_as_dict(source) -> dict:
    response_dict = dict()
    for field in source:
        response_dict[field[0]] = getattr(source, field[0])
    return response_dict


class FastApiSettings(BaseSettings):
    FRONT_DIR: str = 'front'
    STATIC_DIR: str = FRONT_DIR + '/static'
    TEMPLATES_DIR: str = FRONT_DIR + '/templates'
    MEDIA_DIR: str = 'media'
    SECRET_KEY: bytes = Fernet.generate_key()


class UvicornSettings(BaseSettings):
    app: str = 'main:web'
    host: str = '0.0.0.0'
    port: int = 8003
    workers: int = 1
    reload: bool = True
    reload_dirs: t.List = [
        folder for folder in os.listdir()
        if folder not in ['media', 'virt', 'front'] and
        not folder.startswith(('__', '.'))
    ]


# uvicorn_settings = UvicornSettings()
# fast_api_settings = FastApiSettings()


@lru_cache()
def uvicorn_settings():
    return UvicornSettings()


@lru_cache()
def fast_api_settings():
    return FastApiSettings()


__all__ = [
    'uvicorn_settings',
    'fast_api_settings',
    'get_as_dict',
    'FastApiSettings',
    'UvicornSettings',
]
