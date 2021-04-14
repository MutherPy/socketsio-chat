from fastapi_part import app
from socket_part import sio, asgi
import uvicorn
from settings import uvicorn_settings

web = asgi(sio, app)

if __name__ == '__main__':
    uvicorn.run(**uvicorn_settings().dict())
