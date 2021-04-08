from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from settings import fast_api_settings


app = FastAPI(debug=True)
app.mount("/static", StaticFiles(directory=fast_api_settings().STATIC_DIR), name="static")
