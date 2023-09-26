from fastapi import FastAPI

from scraper_api.endpoints import (
    login,
)

app = FastAPI()

app.include_router(login.router)
