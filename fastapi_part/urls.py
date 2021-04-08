from fastapi import File, UploadFile, Depends
from fastapi.responses import HTMLResponse

from fastapi_part import app
from fastapi_part.services import saving_shared_files

from settings import fast_api_settings, FastApiSettings


@app.get('/')
async def start(setting: FastApiSettings = Depends(fast_api_settings)):
    with open(f'{setting.TEMPLATES_DIR}/index.html', 'r') as index:
        resp = index.read()
        return HTMLResponse(resp, status_code=200)


@app.get('/chat')
async def enter(setting: FastApiSettings = Depends(fast_api_settings)):
    with open(f'{setting.TEMPLATES_DIR}/chat.html', 'r') as chat:
        resp = chat.read()
        return HTMLResponse(resp, status_code=200)


@app.post('/chat/sharing_file')
async def sharing(room: str, file: UploadFile = File(...)):
    e_path = await saving_shared_files(room=room, file=file)
    return {'file_token': e_path}


@app.get('/download')
async def download(token: str, setting: FastApiSettings = Depends(fast_api_settings)):
    print(token)
    from .services.crypto_deals import decrypt_path
    print(decrypt_path(token, setting.SECRET_KEY))
    return 'hello'
