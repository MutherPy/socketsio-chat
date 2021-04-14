import os
import typing as t
from pydantic import BaseSettings
from functools import lru_cache


class FastApiSettings(BaseSettings):
    FRONT_DIR: str = 'front'
    STATIC_DIR: str = FRONT_DIR + '/static'
    TEMPLATES_DIR: str = FRONT_DIR + '/templates'
    MEDIA_DIR: str = 'media'
    SECRET_KEY: bytes = b'o8ZSt2xvSfLoLsRtcX2i7j0vsgFlallLFUs8ylf5cwA='


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


@lru_cache()
def uvicorn_settings():
    return UvicornSettings()


@lru_cache()
def fast_api_settings():
    return FastApiSettings()


__all__ = [
    'uvicorn_settings',
    'fast_api_settings',
    'FastApiSettings',
    'UvicornSettings',
]
