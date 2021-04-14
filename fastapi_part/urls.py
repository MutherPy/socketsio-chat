from fastapi import File, UploadFile, Depends, Form
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse

from fastapi_part import app
from fastapi_part.services import (saving_shared_files,
                                   giving_shared_file,
                                   encrypt_jwt)

from database_part import db

from settings import fast_api_settings, FastApiSettings


@app.get('/')
async def start(setting: FastApiSettings = Depends(fast_api_settings)):
    with open(f'{setting.TEMPLATES_DIR}/index.html', 'r') as index:
        resp = index.read()
        return HTMLResponse(resp, status_code=200)


@app.post('/login')
async def login(username: str = Form(...), password: str = Form(...),
                setting: FastApiSettings = Depends(fast_api_settings)):
    async with db:
        user = db.get_user(username, password)
    token = encrypt_jwt(user, setting.SECRET_KEY)
    return JSONResponse({'token': token})


@app.get('/chat')
async def enter(setting: FastApiSettings = Depends(fast_api_settings)):
    with open(f'{setting.TEMPLATES_DIR}/chat.html', 'r') as chat:
        resp = chat.read()
        return HTMLResponse(resp, status_code=200)


@app.post('/chat/sharing_file')
async def sharing(room: str, file: UploadFile = File(...)):
    e_path = await saving_shared_files(room=room, file=file)
    return {'file_token': e_path, 'download_path': '/chat/download/'}


@app.get('/chat/download/')
async def download(token: str, setting: FastApiSettings = Depends(fast_api_settings)):
    file_obj = await giving_shared_file(token)
    if file_obj:
        return FileResponse(file_obj)
    else:
        return '404'
