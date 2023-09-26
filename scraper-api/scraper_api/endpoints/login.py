from typing import Annotated
from fastapi import APIRouter, Form

from scraper_api.scraper.login import login_user


router = APIRouter()


@router.post('/login')
async def login(user: Annotated[str, Form()], domain: Annotated[str, Form()], password: Annotated[str, Form()]):
    result, msg = await login_user(user, domain, password)
    return {
        'logged': result,
        'message': msg,
    }