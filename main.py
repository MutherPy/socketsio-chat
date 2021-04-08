from fastapi_part import app
from socket_part import sio, asgi
import uvicorn
from settings import uvicorn_settings, get_as_dict

web = asgi(sio, app)

if __name__ == '__main__':
    uvicorn.run(**get_as_dict(uvicorn_settings()))
